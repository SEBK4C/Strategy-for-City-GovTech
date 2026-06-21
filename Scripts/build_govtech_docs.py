#!/usr/bin/env python3
"""
build_govtech_docs.py

Build pipeline: Markdown source of truth -> DOCX -> PDF -> HTML
for strategy-for-city-govtech.

Usage:
    python3 Scripts/build_govtech_docs.py [--lang en|de|all] [--version VERSION]

Requires: pandoc, weasyprint (or wkhtmltopdf), python-docx

All document formats are generated from the Markdown source of truth.
English is always the primary source; German (and future languages) are
derived translations stored in Doc/<lang>/.
"""

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
DOC = ROOT / "Doc"

# Document registry: (version, lang, stem)
DOCUMENTS = [
    ("0.2.0", "en", "sovereign-by-design-v0.2.0"),
    ("0.2.0", "de", "sovereign-by-design-v0.2.0.de"),
    ("0.1.0", "en", "sovereign-by-design-v0.1.0"),
    ("0.1.0", "de", "sovereign-by-design-v0.1.0.de"),
]

PANDOC_COMMON = [
    "--standalone",
    "--from", "markdown+yaml_metadata_block+smart",
    "--metadata", "lang=en",
]


def build_docx(md_path: Path, out_path: Path) -> bool:
    """Convert Markdown to DOCX via pandoc."""
    cmd = [
        "pandoc",
        str(md_path),
        "--to", "docx",
        "--output", str(out_path),
        "--reference-doc", str(ROOT / "Scripts" / "reference.docx")
        if (ROOT / "Scripts" / "reference.docx").exists()
        else "--",
    ]
    # Remove the reference-doc arg if reference.docx does not exist
    cmd = [
        "pandoc",
        str(md_path),
        "--to", "docx",
        "--output", str(out_path),
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"  [DOCX] {out_path.name}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"  [ERROR] DOCX build failed for {md_path.name}: {e.stderr}", file=sys.stderr)
        return False
    except FileNotFoundError:
        print("  [WARN] pandoc not found; skipping DOCX build", file=sys.stderr)
        return False


def build_pdf_via_html(html_path: Path, out_path: Path) -> bool:
    """Convert HTML to PDF via weasyprint."""
    try:
        result = subprocess.run(
            ["weasyprint", str(html_path), str(out_path)],
            capture_output=True, text=True, check=True
        )
        print(f"  [PDF]  {out_path.name}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"  [ERROR] PDF build failed: {e.stderr}", file=sys.stderr)
        return False
    except FileNotFoundError:
        # Try wkhtmltopdf as fallback
        try:
            result = subprocess.run(
                ["wkhtmltopdf", "--quiet", str(html_path), str(out_path)],
                capture_output=True, text=True, check=True
            )
            print(f"  [PDF]  {out_path.name} (via wkhtmltopdf)")
            return True
        except FileNotFoundError:
            print("  [WARN] Neither weasyprint nor wkhtmltopdf found; skipping PDF", file=sys.stderr)
            return False


def build_html(md_path: Path, out_path: Path, lang: str = "en") -> bool:
    """Convert Markdown to standalone HTML via pandoc."""
    cmd = [
        "pandoc",
        str(md_path),
        "--to", "html5",
        "--output", str(out_path),
        "--standalone",
        "--metadata", f"lang={lang}",
        "--wrap", "none",
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"  [HTML] {out_path.name}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"  [ERROR] HTML build failed: {e.stderr}", file=sys.stderr)
        return False
    except FileNotFoundError:
        print("  [WARN] pandoc not found; skipping HTML build", file=sys.stderr)
        return False


def build_document(version: str, lang: str, stem: str, formats: list) -> dict:
    """Build all requested formats for one document."""
    lang_dir = DOC / lang
    md_path = lang_dir / f"{stem}.md"

    if not md_path.exists():
        print(f"  [SKIP] {md_path} not found")
        return {}

    results = {}
    print(f"\nBuilding {stem} ({lang}, v{version})")

    if "docx" in formats:
        docx_path = lang_dir / f"{stem}.docx"
        results["docx"] = build_docx(md_path, docx_path)

    html_path = lang_dir / f"{stem}.html"
    if "html" in formats or "pdf" in formats:
        # HTML is built anyway because PDF derives from it
        if not html_path.exists() or "html" in formats:
            results["html"] = build_html(md_path, html_path, lang)

    if "pdf" in formats:
        pdf_path = lang_dir / f"{stem}.pdf"
        results["pdf"] = build_pdf_via_html(html_path, pdf_path)

    return results


def main():
    parser = argparse.ArgumentParser(description="Build govtech strategy documents")
    parser.add_argument("--lang", default="all", choices=["en", "de", "all"],
                        help="Language to build (default: all)")
    parser.add_argument("--version", default="0.2.0",
                        help="Document version to build (default: 0.2.0)")
    parser.add_argument("--formats", default="docx,pdf,html",
                        help="Comma-separated formats (default: docx,pdf,html)")
    args = parser.parse_args()

    formats = [f.strip() for f in args.formats.split(",")]
    langs = ["en", "de"] if args.lang == "all" else [args.lang]

    docs = [
        (ver, lang, stem)
        for ver, lang, stem in DOCUMENTS
        if ver == args.version and lang in langs
    ]

    if not docs:
        print(f"No documents found for version {args.version} and lang {args.lang}")
        sys.exit(1)

    all_results = []
    for ver, lang, stem in docs:
        results = build_document(ver, lang, stem, formats)
        all_results.append((stem, results))

    print("\n--- Build summary ---")
    for stem, results in all_results:
        status = " | ".join(f"{fmt}: {'OK' if ok else 'FAIL'}" for fmt, ok in results.items())
        print(f"  {stem}: {status}")


if __name__ == "__main__":
    main()
