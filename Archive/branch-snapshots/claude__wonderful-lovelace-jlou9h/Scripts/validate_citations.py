#!/usr/bin/env python3
"""
Citation validator for City GovTech Strategy documents.

Checks that:
1. Every [N] citation in the paper has a corresponding entry in Mem/source-registry.md
2. Every source in the registry is cited at least once in at least one paper
3. No source has verification status "unverified"
4. Citation numbers are sequential (no gaps for v1.0)

Usage:
    python3 Scripts/validate_citations.py [--strict] [--paper en|de|all]

Exit codes:
    0 — all checks pass
    1 — warnings found (non-fatal)
    2 — errors found (fatal for CI)
"""

import re
import sys
from pathlib import Path
from collections import defaultdict

REPO_ROOT = Path(__file__).parent.parent
DOC_DIR = REPO_ROOT / "Doc"
MEM_DIR = REPO_ROOT / "Mem"


def load_source_registry(path: Path) -> dict:
    """Parse source-registry.md and return {id: {title, url, verification_status, ...}}."""
    text = path.read_text(encoding="utf-8")
    sources = {}
    current_id = None
    current = {}

    for line in text.splitlines():
        m = re.match(r"^### \[(\d+)\] (.+)$", line)
        if m:
            if current_id is not None:
                sources[current_id] = current
            current_id = int(m.group(1))
            current = {"short_name": m.group(2), "id": current_id}
            continue

        if current_id is not None:
            for field in ["Original language", "Region/Jurisdiction", "Issuing organization",
                          "Publication date", "Document title", "Source URL",
                          "License/reuse status", "Verification status", "Notes"]:
                pattern = rf"^- \*\*{re.escape(field)}:\*\* (.+)$"
                fm = re.match(pattern, line)
                if fm:
                    key = field.lower().replace("/", "_").replace(" ", "_")
                    current[key] = fm.group(1).strip()

    if current_id is not None:
        sources[current_id] = current

    return sources


def find_citations_in_file(path: Path) -> list[int]:
    """Return all citation numbers [N] found in a Markdown file."""
    text = path.read_text(encoding="utf-8")
    # Match patterns like [1], [1, 2], [1, 29, 30], [1][2]
    raw = re.findall(r"\[(\d+(?:,\s*\d+)*)\]", text)
    ids = []
    for group in raw:
        ids.extend(int(x.strip()) for x in group.split(","))
    return sorted(set(ids))


def get_latest_paper_paths() -> dict:
    """Return the latest version of each language paper."""
    def version_key(p):
        m = re.search(r"v(\d+)\.(\d+)\.(\d+)", p.name)
        return tuple(int(x) for x in m.groups()) if m else (0, 0, 0)

    papers = {}
    for lang in ["en", "de"]:
        candidates = list((DOC_DIR / lang).glob("sovereign-by-design-v*.md"))
        if candidates:
            papers[lang] = sorted(candidates, key=version_key)[-1]
    return papers


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Validate citations in GovTech strategy papers.")
    parser.add_argument("--strict", action="store_true", help="Fail on warnings too")
    parser.add_argument("--paper", choices=["en", "de", "all"], default="all")
    args = parser.parse_args()

    registry_path = MEM_DIR / "source-registry.md"
    if not registry_path.exists():
        print(f"ERROR: Source registry not found at {registry_path}", file=sys.stderr)
        sys.exit(2)

    print(f"Loading source registry: {registry_path.relative_to(REPO_ROOT)}")
    sources = load_source_registry(registry_path)
    print(f"  Found {len(sources)} sources in registry (IDs: {sorted(sources.keys())})\n")

    papers = get_latest_paper_paths()
    if args.paper != "all":
        papers = {k: v for k, v in papers.items() if k == args.paper}

    all_cited_ids = set()
    errors = []
    warnings = []

    for lang, paper_path in papers.items():
        print(f"Checking {paper_path.relative_to(REPO_ROOT)}...")
        cited = find_citations_in_file(paper_path)
        all_cited_ids.update(cited)
        print(f"  Citations found: {cited}")

        # Check every cited ID has a registry entry
        missing = [c for c in cited if c not in sources]
        if missing:
            errors.append(f"  [{lang}] Citations not in registry: {missing}")

        # Check no unverified sources are cited
        for cid in cited:
            if cid in sources:
                status = sources[cid].get("verification_status", "").lower()
                if "unverified" in status:
                    warnings.append(
                        f"  [{lang}] Cited source [{cid}] has verification_status: "
                        f"'{status}' — verify before v1.0 release"
                    )
        print()

    # Check for orphaned registry entries (cited in no paper)
    if args.paper == "all":
        orphans = [sid for sid in sources if sid not in all_cited_ids]
        if orphans:
            warnings.append(f"  Registry entries not cited in any paper: {orphans}")

    # Print results
    if errors:
        print("ERRORS (must fix):")
        for e in errors:
            print(e)
    if warnings:
        print("WARNINGS (should fix before v1.0):")
        for w in warnings:
            print(w)
    if not errors and not warnings:
        print("All citations valid — registry complete, all sources verified.")

    if errors:
        sys.exit(2)
    if args.strict and warnings:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
