#!/usr/bin/env python3
"""Validate citations across the GovTech strategy papers.

Checks, for each paper under ``Doc/<lang>/``:
  1. Every inline citation ``[N]`` resolves to a numbered entry in that paper's
     ``## References`` / ``## Literaturverzeichnis`` / ``## Quellenverzeichnis`` section.
  2. Every reference number used by the English source of truth exists in the
     canonical source registry (``Mem/source-registry.md``).
  3. Reports source-registry verification coverage (verified / unverified / archived).
  4. Reports the highest citation ID found, and any gaps in the numbered sequence.

Returns a non-zero exit code if any inline citation is unresolved, so it can gate a
release in CI.

Usage:
    python3 Scripts/validate_citations.py
    python3 Scripts/validate_citations.py --strict    # also fail on unverified sources
    python3 Scripts/validate_citations.py --paper Doc/en/sovereign-by-design-v0.2.0.md
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DOC_DIR = REPO_ROOT / "Doc"
REGISTRY = REPO_ROOT / "Mem" / "source-registry.md"

REF_HEADINGS = (
    "## References",
    "## Literaturverzeichnis",
    "## Quellenverzeichnis",
    "## Bibliography",
)
INLINE_RE = re.compile(r"\[(\d+(?:\s*,\s*\d+)*)\]")
REF_DEF_RE = re.compile(r"^\[(\d+)\]\s", re.MULTILINE)
REGISTRY_ID_RE = re.compile(r"^###\s*\[(\d+)\]", re.MULTILINE)
VERIFY_RE = re.compile(r"\*\*Verification status:\*\*\s*(\w+)")


def split_references(text: str) -> tuple[str, str]:
    """Return (body_before_refs, references_block)."""
    for heading in REF_HEADINGS:
        idx = text.find(heading)
        if idx != -1:
            return text[:idx], text[idx:]
    return text, ""


def inline_ids(body: str) -> set[int]:
    ids: set[int] = set()
    for group in INLINE_RE.findall(body):
        for part in group.split(","):
            ids.add(int(part.strip()))
    return ids


def registry_ids_and_coverage() -> tuple[set[int], dict[str, int]]:
    if not REGISTRY.exists():
        return set(), {}
    text = REGISTRY.read_text(encoding="utf-8")
    ids = {int(n) for n in REGISTRY_ID_RE.findall(text)}
    coverage: dict[str, int] = {}
    for status in VERIFY_RE.findall(text):
        # Skip template placeholder values
        if status.lower() in ("unverified", "verified", "archived"):
            key = status.lower()
            coverage[key] = coverage.get(key, 0) + 1
    return ids, coverage


def validate_paper(
    path: Path,
    registry_ids: set[int],
    strict: bool = False,
) -> tuple[list[str], list[str]]:
    """Return (errors, warnings) for a single paper."""
    text = path.read_text(encoding="utf-8")
    body, refs = split_references(text)
    errors: list[str] = []
    warnings: list[str] = []

    if not refs:
        errors.append(f"{path.name}: no References section found")
        return errors, warnings

    defined = {int(n) for n in REF_DEF_RE.findall(refs)}
    used = inline_ids(body)

    missing = sorted(used - defined)
    if missing:
        errors.append(f"{path.name}: inline citations with no reference entry: {missing}")

    unused = sorted(defined - used)
    if unused:
        warnings.append(f"{path.name}: reference entries never cited inline: {unused}")

    if registry_ids:
        not_in_registry = sorted(defined - registry_ids)
        if not_in_registry:
            warnings.append(
                f"{path.name}: reference ids absent from source registry: {not_in_registry}"
            )

    # Report sequence gaps in defined IDs
    if defined:
        full_range = set(range(min(defined), max(defined) + 1))
        gaps = sorted(full_range - defined)
        if gaps:
            warnings.append(
                f"{path.name}: gap in reference numbering sequence: {gaps} "
                "(these IDs are intentionally skipped)"
            )

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Fail (non-zero exit) if any sources are unverified in the registry.",
    )
    parser.add_argument(
        "--paper",
        type=Path,
        help="Validate a single paper instead of all papers under Doc/<lang>/.",
    )
    args = parser.parse_args()

    if args.paper:
        papers = [args.paper.resolve()]
    else:
        papers = []
        for lang_dir in sorted(DOC_DIR.iterdir()) if DOC_DIR.exists() else []:
            if lang_dir.is_dir() and lang_dir.name != "build":
                papers.extend(sorted(lang_dir.glob("*.md")))

    if not papers:
        print("No papers found under Doc/<lang>/. (Did you mean to pass --paper?)")
        return 1

    registry_ids, coverage = registry_ids_and_coverage()

    fatal = False
    print("Citation validation")
    print("=" * 60)
    for paper in papers:
        errors, warnings = validate_paper(paper, registry_ids, strict=args.strict)
        if not errors and not warnings:
            print(f"OK    {paper.relative_to(REPO_ROOT)}")
        else:
            for e in errors:
                print(f"FAIL  {e}")
                fatal = True
            for w in warnings:
                print(f"warn  {w}")

    print("\nSource registry verification coverage")
    print("-" * 60)
    if coverage:
        total = sum(coverage.values())
        for status in ("verified", "unverified", "archived"):
            n = coverage.get(status, 0)
            pct = (100 * n / total) if total else 0
            print(f"  {status:11s} {n:3d}  ({pct:4.1f}%)")
        print(f"  {'total':11s} {total:3d}")
        if coverage.get("unverified"):
            unverified_count = coverage["unverified"]
            if args.strict:
                print(f"\n  -> STRICT MODE: {unverified_count} unverified source(s) treated as errors.")
                fatal = True
            else:
                print(f"\n  -> {unverified_count} unverified source(s). Run with --strict to enforce.")
                print("     v1.0.0 milestone target: 0 unverified sources.")
    else:
        print("  (registry not found or has no verification-status entries)")

    print("\n" + ("FAILED: unresolved citations." if fatal else "PASSED."))
    return 2 if fatal else 0


if __name__ == "__main__":
    sys.exit(main())
