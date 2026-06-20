#!/usr/bin/env python3
"""
Build script for City GovTech Strategy documents.

Converts Markdown source files to HTML (and optionally DOCX/PDF if dependencies
are available). Follows the versioning convention: vX.Y.Z suffix in filename.

Usage:
    python3 Scripts/build_govtech_docs.py [--lang en|de|all] [--format md|html|docx|pdf|all]

Requires:
    - markdown (pip install markdown)
    - Optional: mammoth, weasyprint (for DOCX/PDF conversion)
"""

import argparse
import os
import re
import sys
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).parent.parent
DOC_DIR = REPO_ROOT / "Doc"
SCRIPTS_DIR = REPO_ROOT / "Scripts"

SOURCE_FILES = {
    "en": list(DOC_DIR.glob("en/sovereign-by-design-v*.md")),
    "de": list(DOC_DIR.glob("de/sovereign-by-design-v*.de.md")),
}

HTML_TEMPLATE = """\
<!DOCTYPE html>
<html lang="{lang}" dir="ltr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="author" content="Sebastian Graf, Autonomous Office of Civil Digital Infrastructure">
  <meta name="generator" content="build_govtech_docs.py v0.2.0">
  <meta name="version" content="{version}">
  <meta name="date" content="{date}">
  <style>
    :root {{
      --color-bg: #ffffff;
      --color-text: #1a1a1a;
      --color-accent: #005a9c;
      --color-border: #d0d7de;
      --color-code-bg: #f6f8fa;
      --font-body: 'Georgia', 'Times New Roman', serif;
      --font-mono: 'SFMono-Regular', 'Consolas', 'Liberation Mono', monospace;
      --max-width: 860px;
    }}
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{ font-size: 17px; scroll-behavior: smooth; }}
    body {{
      font-family: var(--font-body);
      color: var(--color-text);
      background: var(--color-bg);
      line-height: 1.7;
      padding: 2rem 1.5rem;
    }}
    main {{
      max-width: var(--max-width);
      margin: 0 auto;
    }}
    /* --- Typography --- */
    h1 {{ font-size: 2rem; color: var(--color-accent); margin: 2rem 0 1rem; line-height: 1.25; }}
    h2 {{ font-size: 1.5rem; margin: 2.5rem 0 0.75rem; padding-bottom: 0.25rem; border-bottom: 2px solid var(--color-border); }}
    h3 {{ font-size: 1.2rem; margin: 1.75rem 0 0.5rem; }}
    h4 {{ font-size: 1.05rem; margin: 1.25rem 0 0.4rem; }}
    p {{ margin: 0.85rem 0; }}
    a {{ color: var(--color-accent); text-decoration: underline; }}
    a:hover {{ text-decoration: none; }}
    /* --- Header block --- */
    .doc-header {{
      border: 1px solid var(--color-border);
      border-left: 4px solid var(--color-accent);
      padding: 1rem 1.25rem;
      margin-bottom: 2rem;
      background: var(--color-code-bg);
      font-size: 0.9rem;
    }}
    .doc-header p {{ margin: 0.25rem 0; }}
    /* --- Tables --- */
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 1.25rem 0;
      font-size: 0.92rem;
      overflow-x: auto;
      display: block;
    }}
    th, td {{ border: 1px solid var(--color-border); padding: 0.45rem 0.75rem; text-align: left; }}
    th {{ background: var(--color-code-bg); font-weight: 600; }}
    tr:nth-child(even) {{ background: #f8f9fa; }}
    /* --- Code/preformatted --- */
    pre, code {{
      font-family: var(--font-mono);
      font-size: 0.85rem;
      background: var(--color-code-bg);
      border: 1px solid var(--color-border);
      border-radius: 4px;
    }}
    pre {{ padding: 1rem; overflow-x: auto; margin: 1rem 0; }}
    code {{ padding: 0.15em 0.35em; }}
    pre code {{ border: none; padding: 0; background: none; }}
    /* --- Blockquotes (infoboxes) --- */
    blockquote {{
      border-left: 4px solid var(--color-accent);
      padding: 0.75rem 1.25rem;
      margin: 1.5rem 0;
      background: #f0f6ff;
      font-size: 0.95rem;
    }}
    blockquote p:first-child {{ font-weight: 600; color: var(--color-accent); }}
    /* --- Lists --- */
    ul, ol {{ margin: 0.75rem 0 0.75rem 1.75rem; }}
    li {{ margin: 0.3rem 0; }}
    /* --- HR --- */
    hr {{ border: none; border-top: 1px solid var(--color-border); margin: 2rem 0; }}
    /* --- Footer --- */
    footer {{
      margin-top: 3rem;
      padding-top: 1rem;
      border-top: 1px solid var(--color-border);
      font-size: 0.85rem;
      color: #666;
    }}
    /* --- Print --- */
    @media print {{
      body {{ padding: 0; font-size: 12pt; }}
      h2 {{ page-break-before: always; }}
      table {{ font-size: 10pt; }}
      a {{ color: inherit; text-decoration: none; }}
      a[href]::after {{ content: " (" attr(href) ")"; font-size: 9pt; color: #666; }}
      .doc-header {{ break-inside: avoid; }}
    }}
    @media (max-width: 600px) {{
      html {{ font-size: 15px; }}
      h1 {{ font-size: 1.6rem; }}
    }}
  </style>
</head>
<body>
<main>
{body}
<footer>
  <p>Published under <a href="https://creativecommons.org/licenses/by/4.0/">CC-BY-4.0</a>.
  Attribute as: Sebastian Graf, Autonomous Office of Civil Digital Infrastructure
  (<a href="mailto:sebk4c@tuta.com">sebk4c@tuta.com</a>).
  Version {version} &middot; Generated {date}.</p>
</footer>
</main>
</body>
</html>
"""


def extract_frontmatter(text):
    """Parse YAML front matter from Markdown. Returns (metadata_dict, body_text)."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    yaml_block = text[3:end].strip()
    body = text[end + 4:].lstrip("\n")
    meta = {}
    for line in yaml_block.splitlines():
        if ":" in line and not line.startswith(" "):
            key, _, val = line.partition(":")
            meta[key.strip()] = val.strip().strip('"')
    return meta, body


def md_to_html_body(md_text):
    """Convert Markdown to HTML body. Uses 'markdown' library if available."""
    try:
        import markdown
        extensions = ["tables", "fenced_code", "toc", "attr_list"]
        return markdown.markdown(md_text, extensions=extensions)
    except ImportError:
        # Minimal fallback: wrap in <pre>
        escaped = md_text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        return f"<pre>{escaped}</pre>"


def build_html(md_path: Path, output_path: Path):
    """Build an HTML file from a Markdown source."""
    src = md_path.read_text(encoding="utf-8")
    meta, body_md = extract_frontmatter(src)

    title = meta.get("title", md_path.stem)
    lang = meta.get("language", "en")
    version = meta.get("version", "0.0.0")
    date = meta.get("date", datetime.now().strftime("%Y-%m-%d"))

    html_body = md_to_html_body(body_md)
    html = HTML_TEMPLATE.format(
        lang=lang,
        title=title,
        version=version,
        date=date,
        body=html_body,
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html, encoding="utf-8")
    print(f"  [HTML] {output_path.relative_to(REPO_ROOT)}")


def build_docx(md_path: Path, output_path: Path):
    """Build DOCX from Markdown via HTML intermediate. Requires mammoth + python-docx."""
    try:
        import subprocess
        # Try pandoc first (most reliable)
        result = subprocess.run(
            ["pandoc", str(md_path), "-o", str(output_path),
             "--from=markdown+smart", "--to=docx",
             f"--metadata=author:Sebastian Graf",
             f"--metadata=date:{datetime.now().strftime('%Y-%m-%d')}"],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            print(f"  [DOCX] {output_path.relative_to(REPO_ROOT)} (via pandoc)")
            return
        print(f"  [DOCX] pandoc failed: {result.stderr.strip()}")
    except FileNotFoundError:
        pass
    print(f"  [DOCX] Skipped (pandoc not found). Install pandoc: https://pandoc.org/installing.html")


def build_pdf(md_path: Path, output_path: Path):
    """Build PDF from Markdown via pandoc+LaTeX or weasyprint."""
    try:
        import subprocess
        result = subprocess.run(
            ["pandoc", str(md_path), "-o", str(output_path),
             "--from=markdown+smart", "--to=pdf",
             "--pdf-engine=weasyprint",
             f"--metadata=author:Sebastian Graf"],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            print(f"  [PDF]  {output_path.relative_to(REPO_ROOT)} (via pandoc+weasyprint)")
            return
        # Try xelatex
        result2 = subprocess.run(
            ["pandoc", str(md_path), "-o", str(output_path),
             "--from=markdown+smart", "--pdf-engine=xelatex",
             "-V", "fontsize=11pt",
             "-V", "geometry:margin=2.5cm"],
            capture_output=True, text=True
        )
        if result2.returncode == 0:
            print(f"  [PDF]  {output_path.relative_to(REPO_ROOT)} (via pandoc+xelatex)")
            return
        print(f"  [PDF]  pandoc failed: {result2.stderr.strip()[:200]}")
    except FileNotFoundError:
        print(f"  [PDF]  Skipped (pandoc not found). Install pandoc: https://pandoc.org/installing.html")


def find_latest_version(paths):
    """Return the path with the highest semantic version number."""
    def version_key(p):
        m = re.search(r"v(\d+)\.(\d+)\.(\d+)", p.name)
        return tuple(int(x) for x in m.groups()) if m else (0, 0, 0)
    return sorted(paths, key=version_key)[-1] if paths else None


def main():
    parser = argparse.ArgumentParser(description="Build GovTech strategy documents.")
    parser.add_argument("--lang", choices=["en", "de", "all"], default="all")
    parser.add_argument("--format", choices=["html", "docx", "pdf", "all"], default="all")
    parser.add_argument("--all-versions", action="store_true",
                        help="Build all versions (default: only latest)")
    args = parser.parse_args()

    langs = ["en", "de"] if args.lang == "all" else [args.lang]
    formats = ["html", "docx", "pdf"] if args.format == "all" else [args.format]

    for lang in langs:
        files = SOURCE_FILES.get(lang, [])
        if not files:
            print(f"[{lang}] No source files found in Doc/{lang}/")
            continue

        if args.all_versions:
            targets = sorted(files)
        else:
            latest = find_latest_version(files)
            targets = [latest] if latest else []

        for md_path in targets:
            print(f"\nBuilding: {md_path.relative_to(REPO_ROOT)}")
            stem = md_path.stem  # e.g. "sovereign-by-design-v0.2.0" or "sovereign-by-design-v0.2.0.de"

            if "html" in formats:
                html_path = md_path.with_suffix(".html")
                build_html(md_path, html_path)

            if "docx" in formats:
                docx_path = md_path.with_suffix(".docx")
                build_docx(md_path, docx_path)

            if "pdf" in formats:
                pdf_path = md_path.with_suffix(".pdf")
                build_pdf(md_path, pdf_path)

    print("\nDone. Run `python3 Scripts/validate_citations.py` to verify all citations.")


if __name__ == "__main__":
    main()
