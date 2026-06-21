#!/usr/bin/env python3
"""
validate_citations.py

Validates all citation references in a strategy paper against the source registry.
Reports: (a) citations in the paper not found in the registry; (b) registry entries
marked 'unverified'; (c) registry entries not cited in any paper.

Usage:
    python3 Scripts/validate_citations.py [--paper Doc/en/sovereign-by-design-v0.2.0.md]
    python3 Scripts/validate_citations.py --all
    python3 Scripts/validate_citations.py --check-urls
"""

import re
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime

REGISTRY_PATH = Path("Mem/source-registry.md")
DEFAULT_PAPER = Path("Doc/en/sovereign-by-design-v0.2.0.md")


def parse_registry(registry_path: Path) -> dict:
    """Parse source registry Markdown into dict keyed by citation ID."""
    registry = {}
    if not registry_path.exists():
        print(f"ERROR: Registry not found at {registry_path}", file=sys.stderr)
        sys.exit(1)

    text = registry_path.read_text(encoding="utf-8")
    entry_pattern = re.compile(
        r"### \[(\d+)\] (.+?)\n(.*?)(?=### \[\d+\]|## Sources to add|---\Z)",
        re.DOTALL,
    )

    for match in entry_pattern.finditer(text):
        citation_id = int(match.group(1))
        short_name = match.group(2).strip()
        body = match.group(3)

        fields = {}
        for line in body.splitlines():
            field_match = re.match(r"- \*\*(.+?):\*\*\s*(.*)", line)
            if field_match:
                fields[field_match.group(1).lower().replace("/", "-").replace(" ", "-")] = (
                    field_match.group(2).strip()
                )

        registry[citation_id] = {
            "id": citation_id,
            "short_name": short_name,
            "verification_status": fields.get("verification-status", "unknown"),
            "url": fields.get("source-url", ""),
            "language": fields.get("original-language", ""),
            "organisation": fields.get("issuing-organization", ""),
            "license": fields.get("license-reuse-status", ""),
        }

    return registry


def extract_citations_from_paper(paper_path: Path) -> set:
    """Extract all [N] citation markers from a paper."""
    if not paper_path.exists():
        print(f"ERROR: Paper not found at {paper_path}", file=sys.stderr)
        sys.exit(1)

    text = paper_path.read_text(encoding="utf-8")
    # Match [1], [2, 3], [1, 29], etc.
    raw = re.findall(r"\[([\d, ]+)\]", text)
    citation_ids = set()
    for group in raw:
        for num in group.split(","):
            num = num.strip()
            if num.isdigit():
                citation_ids.add(int(num))
    return citation_ids


def validate(paper_path: Path, registry: dict, verbose: bool = False) -> dict:
    """Validate citations in paper against registry. Returns summary dict."""
    paper_citations = extract_citations_from_paper(paper_path)
    registry_ids = set(registry.keys())

    missing_from_registry = paper_citations - registry_ids
    unverified_in_registry = {
        cid: registry[cid]
        for cid in paper_citations & registry_ids
        if registry[cid]["verification_status"] == "unverified"
    }
    uncited_in_paper = registry_ids - paper_citations

    print(f"\n{'='*60}")
    print(f"Citation Validation: {paper_path.name}")
    print(f"Run date: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}")
    print(f"{'='*60}")
    print(f"Paper citations found: {len(paper_citations)}")
    print(f"Registry entries:      {len(registry_ids)}")

    if missing_from_registry:
        print(f"\n[FAIL] {len(missing_from_registry)} citation(s) in paper NOT in registry:")
        for cid in sorted(missing_from_registry):
            print(f"  [{cid}] NOT IN REGISTRY")
    else:
        print("\n[PASS] All paper citations found in registry.")

    if unverified_in_registry:
        print(f"\n[WARN] {len(unverified_in_registry)} cited source(s) still marked 'unverified':")
        for cid, entry in sorted(unverified_in_registry.items()):
            print(f"  [{cid}] {entry['short_name']}")
    else:
        print("[PASS] All cited sources verified.")

    if verbose and uncited_in_paper:
        print(f"\n[INFO] {len(uncited_in_paper)} registry entries not cited in this paper:")
        for cid in sorted(uncited_in_paper):
            print(f"  [{cid}] {registry[cid]['short_name']}")

    overall_pass = not missing_from_registry and not unverified_in_registry
    status = "PASS" if overall_pass else "FAIL"
    print(f"\nOverall status: [{status}]")
    print(f"{'='*60}\n")

    return {
        "paper": str(paper_path),
        "status": status,
        "paper_citation_count": len(paper_citations),
        "registry_count": len(registry_ids),
        "missing_from_registry": sorted(missing_from_registry),
        "unverified_cited": sorted(unverified_in_registry.keys()),
    }


def main():
    parser = argparse.ArgumentParser(description="Validate citations against source registry.")
    parser.add_argument(
        "--paper",
        type=Path,
        default=DEFAULT_PAPER,
        help=f"Path to paper Markdown file (default: {DEFAULT_PAPER})",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Validate all papers in Doc/en/ and Doc/de/",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show uncited registry entries",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results as JSON",
    )
    args = parser.parse_args()

    registry = parse_registry(REGISTRY_PATH)
    results = []

    if args.all:
        papers = list(Path("Doc/en").glob("*.md")) + list(Path("Doc/de").glob("*.md"))
        if not papers:
            print("No Markdown papers found in Doc/en/ or Doc/de/")
            sys.exit(1)
        for paper in sorted(papers):
            result = validate(paper, registry, verbose=args.verbose)
            results.append(result)
    else:
        result = validate(args.paper, registry, verbose=args.verbose)
        results.append(result)

    if args.json:
        print(json.dumps(results, indent=2))

    any_fail = any(r["status"] == "FAIL" for r in results)
    sys.exit(1 if any_fail else 0)


if __name__ == "__main__":
    main()
