#!/usr/bin/env python3
"""
translate_document.py

Translation workflow management for strategy-for-city-govtech.

English is the single source of truth. German (and future languages) are
derived translations. This script:
  - Checks translation parity (same headings, same citation count)
  - Reports sections present in EN but missing in DE
  - Provides a structured translation checklist when called with --checklist

Usage:
    python3 Scripts/translate_document.py [--check] [--checklist] [--lang de]
    python3 Scripts/translate_document.py --add-language fr

To add a new language:
    1. Run: python3 Scripts/translate_document.py --add-language <code>
    2. Follow the checklist output
    3. Create Doc/<code>/<stem>.<code>.md as a translation of the EN source
    4. Run --check to verify parity
"""

import re
import sys
import argparse
from pathlib import Path

ROOT = Path(__file__).parent.parent
DOC = ROOT / "Doc"

SUPPORTED_LANGUAGES = {
    "en": "English",
    "de": "Deutsch",
}

# Add new languages here when extending
ADDITIONS = {
    "fr": "Français",
    "it": "Italiano",
    "rm": "Rumantsch",  # Romansh (Swiss official language)
}

LATEST_VERSION = "0.2.0"


def get_headings(md_path: Path) -> list:
    """Extract all headings from a Markdown file."""
    text = md_path.read_text(encoding="utf-8")
    return [line for line in text.splitlines() if line.startswith("#")]


def get_citations(md_path: Path) -> set:
    """Extract all citation IDs from a Markdown file."""
    text = md_path.read_text(encoding="utf-8")
    raw = re.findall(r"\[([\d,\s]+)\]", text)
    citations = set()
    for group in raw:
        for num in group.split(","):
            num = num.strip()
            if num.isdigit():
                citations.add(int(num))
    return citations


def check_parity(version: str, target_lang: str) -> bool:
    """Check that translation has the same headings and citation count as EN."""
    en_dir = DOC / "en"
    tl_dir = DOC / target_lang

    stem_en = f"sovereign-by-design-v{version}"
    stem_tl = f"sovereign-by-design-v{version}.{target_lang}"

    en_path = en_dir / f"{stem_en}.md"
    tl_path = tl_dir / f"{stem_tl}.md"

    if not en_path.exists():
        print(f"ERROR: EN source not found: {en_path}", file=sys.stderr)
        return False

    if not tl_path.exists():
        print(f"MISSING: Translation not found: {tl_path}")
        return False

    en_headings = get_headings(en_path)
    tl_headings = get_headings(tl_path)
    en_cites = get_citations(en_path)
    tl_cites = get_citations(tl_path)

    print(f"\nParity check: EN vs {target_lang.upper()} (v{version})")
    print(f"  EN headings: {len(en_headings)} | {target_lang.upper()} headings: {len(tl_headings)}")
    print(f"  EN citations: {len(en_cites)} unique | {target_lang.upper()} citations: {len(tl_cites)} unique")

    ok = True

    # Check citation parity (translations should have same citations)
    missing_in_tl = sorted(en_cites - tl_cites)
    extra_in_tl = sorted(tl_cites - en_cites)
    if missing_in_tl:
        print(f"  [WARN] Citations in EN not in {target_lang.upper()}: {missing_in_tl}")
        ok = False
    if extra_in_tl:
        print(f"  [WARN] Citations in {target_lang.upper()} not in EN: {extra_in_tl}")
        ok = False

    # Check heading count
    if len(en_headings) != len(tl_headings):
        print(f"  [WARN] Heading count mismatch: EN={len(en_headings)}, {target_lang.upper()}={len(tl_headings)}")
        ok = False

    if ok:
        print(f"  [OK] Parity check passed")

    return ok


def print_add_language_checklist(lang_code: str):
    """Print instructions for adding a new language."""
    lang_name = ADDITIONS.get(lang_code, lang_code)
    print(f"""
ADDING LANGUAGE: {lang_code} ({lang_name})

1. Create directory: Doc/{lang_code}/

2. Create translation file:
   Doc/{lang_code}/sovereign-by-design-v{LATEST_VERSION}.{lang_code}.md

   Requirements:
   - Same section structure and heading hierarchy as EN source
   - Same citation numbers [N] — do NOT renumber
   - Add YAML front matter: language: "{lang_code}", source-of-truth: false, source-language: "en"
   - Translate abstract, all body text, and section headings
   - Keep all code blocks, tables, and ASCII diagrams as-is
   - Translate table content; do not alter table structure

3. Create HTML version:
   Doc/{lang_code}/sovereign-by-design-v{LATEST_VERSION}.{lang_code}.html

   Either:
   a. Run: python3 Scripts/build_govtech_docs.py --lang {lang_code}
   b. Or write the HTML manually following Doc/en/sovereign-by-design-v{LATEST_VERSION}.html structure

4. Update Scripts/translate_document.py:
   Add '{lang_code}': '{lang_name}' to SUPPORTED_LANGUAGES dict

5. Update Scripts/build_govtech_docs.py:
   Add ('latest_version', '{lang_code}', 'sovereign-by-design-v{LATEST_VERSION}.{lang_code}')
   to DOCUMENTS list

6. Verify parity:
   python3 Scripts/translate_document.py --check --lang {lang_code}

7. Update README.md: add {lang_name} to the languages table

8. Commit:
   git commit -m 'feat: add {lang_name} translation of sovereign-by-design v{LATEST_VERSION}'
""")


def main():
    parser = argparse.ArgumentParser(description="Translation workflow management")
    parser.add_argument("--check", action="store_true", help="Check EN/translation parity")
    parser.add_argument("--lang", default="de", help="Target language code (default: de)")
    parser.add_argument("--version", default=LATEST_VERSION, help="Document version")
    parser.add_argument("--add-language", metavar="LANG_CODE",
                        help="Print checklist for adding a new language")
    args = parser.parse_args()

    if args.add_language:
        print_add_language_checklist(args.add_language)
        return

    if args.check:
        ok = check_parity(args.version, args.lang)
        if not ok:
            sys.exit(1)
        return

    # Default: print status
    print("Supported languages:")
    for code, name in SUPPORTED_LANGUAGES.items():
        en_path = DOC / "en" / f"sovereign-by-design-v{args.version}.md"
        if code == "en":
            exists = en_path.exists()
            print(f"  {code} ({name}): {'OK' if exists else 'MISSING'} [source of truth]")
        else:
            tl_path = DOC / code / f"sovereign-by-design-v{args.version}.{code}.md"
            exists = tl_path.exists()
            print(f"  {code} ({name}): {'OK' if exists else 'MISSING'}")

    print("\nTo check parity: python3 Scripts/translate_document.py --check --lang de")
    print("To add a language: python3 Scripts/translate_document.py --add-language fr")


if __name__ == "__main__":
    main()
