#!/usr/bin/env python3
"""Manage and verify translations derived from the English source of truth.

The English papers under ``Doc/en/`` are canonical. Each translation lives under
``Doc/<lang>/`` with a ``.<lang>.md`` suffix and a ``translated-from:`` front-matter key
pointing back at its source. This script keeps translations honest:

  --check   (default) Compare the section structure (heading outline) of each translation
            against its English source and report drift. Non-zero exit on mismatch.
  --scaffold <lang>
            Create a new-language skeleton for every English paper by copying the source
            and inserting a translation banner, so a translator can fill it in without
            touching the source material.

The design goal: additional languages can be added later WITHOUT rewriting the source.

Usage:
    uv run python Scripts/translate_document.py --check
    uv run python Scripts/translate_document.py --scaffold fr
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DOC_DIR = REPO_ROOT / "Doc"
EN_DIR = DOC_DIR / "en"

# Known languages and the localized heading that replaces "## References".
LANGUAGES = {
    "en": {"name": "English", "references": "## References"},
    "de": {"name": "Deutsch", "references": "## Literaturverzeichnis"},
    # Add new languages here, e.g.:
    # "fr": {"name": "Français", "references": "## Références"},
}

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$", re.MULTILINE)
NUM_PREFIX_RE = re.compile(r"^\s*(\d+(?:\.\d+)*)\.?\s")


def strip_front_matter(text: str) -> str:
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4 :].lstrip("\n")
    return text


def heading_outline(text: str) -> list[tuple[int, str]]:
    """Return (level, numeric-prefix-or-marker) for each heading.

    We compare the *structure* (heading levels and any leading section numbers like
    ``4.2``) rather than the translated prose, so EN and DE can be checked for parity
    without a word-for-word match.
    """
    outline: list[tuple[int, str]] = []
    for hashes, title in HEADING_RE.findall(strip_front_matter(text)):
        level = len(hashes)
        m = NUM_PREFIX_RE.match(title)
        marker = m.group(1) if m else "¶"
        outline.append((level, marker))
    return outline


def translations_for(src: Path) -> list[Path]:
    out: list[Path] = []
    stem = src.stem  # e.g. sovereign-by-design-v0.1.0
    for lang in LANGUAGES:
        if lang == "en":
            continue
        candidate = DOC_DIR / lang / f"{stem}.{lang}.md"
        if candidate.exists():
            out.append(candidate)
    return out


def check() -> int:
    if not EN_DIR.exists():
        print("No Doc/en/ directory found.")
        return 1
    sources = sorted(EN_DIR.glob("*.md"))
    if not sources:
        print("No English sources found under Doc/en/.")
        return 1

    problems = 0
    print("Translation parity check\n" + "=" * 60)
    for src in sources:
        src_outline = heading_outline(src.read_text(encoding="utf-8"))
        targets = translations_for(src)
        if not targets:
            print(f"note  {src.name}: no translations yet")
            continue
        for tgt in targets:
            tgt_outline = heading_outline(tgt.read_text(encoding="utf-8"))
            if src_outline == tgt_outline:
                print(f"OK    {tgt.relative_to(REPO_ROOT)}  ({len(tgt_outline)} headings)")
            else:
                problems += 1
                print(f"DRIFT {tgt.relative_to(REPO_ROOT)}")
                print(f"        en headings: {len(src_outline)}, {tgt.name}: {len(tgt_outline)}")
                # Show the first divergent position.
                for i, (a, b) in enumerate(zip(src_outline, tgt_outline)):
                    if a != b:
                        print(f"        first divergence at heading #{i+1}: en={a} vs {b}")
                        break
    print("\n" + ("PASSED." if not problems else f"FAILED: {problems} translation(s) drifted."))
    return 0 if not problems else 2


def scaffold(lang: str) -> int:
    if lang in LANGUAGES and lang != "en":
        print(f"Language '{lang}' already registered ({LANGUAGES[lang]['name']}).")
    elif lang == "en":
        print("'en' is the source of truth; nothing to scaffold.")
        return 1
    else:
        print(f"note: add '{lang}' to LANGUAGES in this script to enable parity checks.")

    target_dir = DOC_DIR / lang
    target_dir.mkdir(parents=True, exist_ok=True)
    created = 0
    for src in sorted(EN_DIR.glob("*.md")):
        target = target_dir / f"{src.stem}.{lang}.md"
        if target.exists():
            print(f"  exists  {target.relative_to(REPO_ROOT)}")
            continue
        text = src.read_text(encoding="utf-8")
        banner = (
            f"\n> **TRANSLATION SKELETON ({lang}).** Derived from the English source of "
            f"truth `en/{src.name}`.\n> Translate the prose below; keep all headings, "
            f"section numbers, tables, and citation markers `[N]` intact.\n"
        )
        # Insert the banner after the first H1.
        m = re.search(r"^#\s.*$", text, re.MULTILINE)
        if m:
            idx = m.end()
            text = text[:idx] + "\n" + banner + text[idx:]
        target.write_text(text, encoding="utf-8")
        created += 1
        print(f"  created {target.relative_to(REPO_ROOT)}")
    print(f"\nScaffolded {created} file(s) for '{lang}'. Now translate them in place.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--check", action="store_true", help="Check translation parity (default).")
    group.add_argument("--scaffold", metavar="LANG", help="Scaffold a new language skeleton.")
    args = parser.parse_args()

    if args.scaffold:
        return scaffold(args.scaffold)
    return check()


if __name__ == "__main__":
    sys.exit(main())
