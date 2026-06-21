#!/usr/bin/env python3
"""
validate_citations.py

Validate every citation in the Markdown papers against the source registry.
Reports:
  - Citations in paper not found in registry
  - Registry entries not cited in any paper
  - Registry entries marked 'unverified'

Usage:
    python3 Scripts/validate_citations.py [--strict]

--strict: exit code 1 if any unverified sources or missing citations
"""

import re
import sys
import argparse
from pathlib import Path

ROOT = Path(__file__).parent.parent
DOC_EN = ROOT / "Doc" / "en"
MEM = ROOT / "Mem"


def extract_citations_from_md(md_path: Path) -> set:
    """Extract all [N] citation references from a Markdown file."""
    text = md_path.read_text(encoding="utf-8")
    # Match [1], [2, 3], [1, 29], etc.
    raw = re.findall(r"\[([\d,\s]+)\]", text)
    citations = set()
    for group in raw:
        for num in group.split(","):
            num = num.strip()
            if num.isdigit():
                citations.add(int(num))
    return citations


def extract_registry_entries(registry_path: Path) -> dict:
    """Extract {id: {title, verification_status}} from source registry."""
    text = registry_path.read_text(encoding="utf-8")
    entries = {}
    # Match ### [N] lines
    current_id = None
    current = {}
    for line in text.splitlines():
        m = re.match(r"^### \[(\d+)\]", line)
        if m:
            if current_id is not None:
                entries[current_id] = current
            current_id = int(m.group(1))
            current = {"title": line, "verification_status": "unknown"}
        elif current_id is not None:
            if "Verification status:** " in line:
                status = line.split("Verification status:** ", 1)[1].strip()
                current["verification_status"] = status
            elif "Document title:** " in line:
                current["title"] = line.split("Document title:** ", 1)[1].strip()
    if current_id is not None:
        entries[current_id] = current
    return entries


def main():
    parser = argparse.ArgumentParser(description="Validate citations against source registry")
    parser.add_argument("--strict", action="store_true",
                        help="Exit 1 if any issues found")
    args = parser.parse_args()

    registry_path = MEM / "source-registry.md"
    if not registry_path.exists():
        print(f"ERROR: Registry not found at {registry_path}", file=sys.stderr)
        sys.exit(1)

    registry = extract_registry_entries(registry_path)
    print(f"Registry entries: {len(registry)}")

    # Collect all citations from all English papers
    all_citations = set()
    papers = list(DOC_EN.glob("*.md"))
    if not papers:
        print("No papers found in Doc/en/", file=sys.stderr)
        sys.exit(1)

    for paper in papers:
        cites = extract_citations_from_md(paper)
        print(f"  {paper.name}: {len(cites)} citation references")
        all_citations |= cites

    print(f"Total unique citation IDs in papers: {len(all_citations)}")

    issues = []

    # Citations in paper not in registry
    missing_in_registry = sorted(all_citations - set(registry.keys()))
    if missing_in_registry:
        issues.append(f"Citations in paper NOT in registry: {missing_in_registry}")
        for cid in missing_in_registry:
            print(f"  [MISSING] [{cid}] not in source-registry.md")

    # Registry entries not cited
    uncited = sorted(set(registry.keys()) - all_citations)
    if uncited:
        print(f"\nRegistry entries not cited in any paper ({len(uncited)}):")
        for cid in uncited:
            print(f"  [UNCITED] [{cid}] {registry[cid].get('title', '')}")

    # Unverified sources that ARE cited
    unverified_cited = [
        cid for cid in all_citations
        if cid in registry and "unverified" in registry[cid].get("verification_status", "")
    ]
    if unverified_cited:
        issues.append(f"Unverified cited sources: {unverified_cited}")
        for cid in sorted(unverified_cited):
            print(f"  [UNVERIFIED] [{cid}] {registry[cid].get('title', '')}")

    print("\n--- Validation summary ---")
    if issues:
        for issue in issues:
            print(f"  ISSUE: {issue}")
        if args.strict:
            sys.exit(1)
    else:
        print("  All citations verified. No issues found.")


if __name__ == "__main__":
    main()
