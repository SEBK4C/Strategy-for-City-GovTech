#!/usr/bin/env python3
"""
validate_citations.py -- Check that every citation in the EN paper exists in source-registry.md.

Usage:
    python3 Scripts/validate_citations.py
    python3 Scripts/validate_citations.py --paper Doc/en/sovereign-by-design-v0.2.0.md
    python3 Scripts/validate_citations.py --all

Exit codes: 0 = all citations found; 1 = missing citations detected.
"""

import re
import sys
import pathlib
import argparse

ROOT = pathlib.Path(__file__).parent.parent
REGISTRY = ROOT / "Mem" / "source-registry.md"
EN_DIR = ROOT / "Doc" / "en"


def load_registry_ids(registry_path: pathlib.Path) -> set:
    text = registry_path.read_text(encoding="utf-8")
    return set(re.findall(r"^### \[(\d+)\]", text, re.MULTILINE))


def extract_citations(md_text: str) -> set:
    """Extract all citation numbers from [N] or [N, M, ...] patterns."""
    hits = re.findall(r"\[([\d,\s]+)\]", md_text)
    ids = set()
    for h in hits:
        for part in re.split(r"[,\s]+", h):
            if part.isdigit():
                ids.add(part)
    return ids


def validate_paper(paper_path: pathlib.Path, registry_ids: set) -> list:
    text = paper_path.read_text(encoding="utf-8")
    cited = extract_citations(text)
    missing = [cid for cid in sorted(cited, key=int) if cid not in registry_ids]
    return missing


def main():
    parser = argparse.ArgumentParser(description="Validate citations against source registry")
    parser.add_argument("--paper", help="Path to Markdown paper to validate")
    parser.add_argument("--all", action="store_true", help="Validate all .md files in Doc/en/")
    args = parser.parse_args()

    if not REGISTRY.exists():
        print(f"ERROR: Source registry not found at {REGISTRY}", file=sys.stderr)
        sys.exit(1)

    registry_ids = load_registry_ids(REGISTRY)
    print(f"Source registry loaded: {len(registry_ids)} entries ({', '.join(sorted(registry_ids, key=int))})")

    papers = []
    if args.paper:
        papers = [pathlib.Path(args.paper)]
    elif args.all:
        papers = list(EN_DIR.glob("*.md"))
    else:
        # Default: most recent EN paper
        candidates = sorted(EN_DIR.glob("sovereign-by-design-*.md"), reverse=True)
        if not candidates:
            print("No EN paper found in Doc/en/", file=sys.stderr)
            sys.exit(1)
        papers = [candidates[0]]

    all_ok = True
    for paper in papers:
        missing = validate_paper(paper, registry_ids)
        if missing:
            print(f"\n[FAIL] {paper.name}: missing registry entries for citations: {missing}")
            all_ok = False
        else:
            cited_count = len(extract_citations(paper.read_text(encoding="utf-8")))
            print(f"[OK]   {paper.name}: all {cited_count} citations found in registry")

    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
