#!/usr/bin/env python3
"""Validate citations across the GovTech strategy papers.

Checks, for each paper under ``Doc/<lang>/``:
  1. Every inline citation ``[N]`` resolves to a numbered entry in that paper's
     ``## References`` / ``## Literaturverzeichnis`` section.
  2. Every reference number used by the English source of truth exists in the
     canonical source registry (``Mem/source-registry.md``).
  3. Reports source-registry verification coverage (verified / unverified / archived).

Returns a non-zero exit code if any inline citation is unresolved, so it can gate a
release in CI.

Version milestones:
  v0.2.0 — 61 citations, all verified (achieved 2026-06-21)
  v0.3.0 — target: maintain 0 unverified, expand to ~75 citations

Usage:
    python3 Scripts/validate_citations.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DOC_DIR = REPO_ROOT / "Doc"
REGISTRY = REPO_ROOT / "Mem" / "source-registry.md"

REF_HEADINGS = ("## References", "## Literaturverzeichnis", "## Bibliography")
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
        key = status.lower()
        coverage[key] = coverage.get(key, 0) + 1
    return ids, coverage


def validate_paper(path: Path, registry_ids: set[int]) -> list[str]:
    text = path.read_text(encoding="utf-8")
    body, refs = split_references(text)
    problems: list[str] = []

    if not refs:
        problems.append(f"{path.name}: no References section found")
        return problems

    defined = {int(n) for n in REF_DEF_RE.findall(refs)}
    used = inline_ids(body)

    missing = sorted(used - defined)
    if missing:
        problems.append(f"{path.name}: inline citations with no reference entry: {missing}")

    unused = sorted(defined - used)
    if unused:
        # Not fatal, but worth surfacing.
        problems.append(f"{path.name}: NOTE reference entries never cited inline: {unused}")

    if registry_ids:
        not_in_registry = sorted(defined - registry_ids)
        if not_in_registry:
            problems.append(
                f"{path.name}: NOTE reference ids absent from source registry: {not_in_registry}"
            )
    return problems


def main() -> int:
    papers = []
    for lang_dir in sorted(DOC_DIR.iterdir()) if DOC_DIR.exists() else []:
        if lang_dir.is_dir() and lang_dir.name != "build":
            papers.extend(sorted(lang_dir.glob("*.md")))

    if not papers:
        print("No papers found under Doc/<lang>/.")
        return 1

    registry_ids, coverage = registry_ids_and_coverage()

    fatal = False
    print("Citation validation\n" + "=" * 60)
    for paper in papers:
        problems = validate_paper(paper, registry_ids)
        hard = [p for p in problems if "NOTE" not in p]
        if not problems:
            print(f"OK    {paper.relative_to(REPO_ROOT)}")
        else:
            for p in problems:
                marker = "FAIL " if "NOTE" not in p else "note "
                print(f"{marker} {p}")
            fatal = fatal or bool(hard)

    print("\nSource registry verification coverage\n" + "-" * 60)
    if coverage:
        total = sum(coverage.values())
        for status in ("verified", "unverified", "archived"):
            n = coverage.get(status, 0)
            pct = (100 * n / total) if total else 0
            print(f"  {status:11s} {n:3d}  ({pct:4.1f}%)")
        print(f"  {'total':11s} {total:3d}")
        if coverage.get("unverified"):
            print("\n  -> milestone target: unverified == 0 (achieved at v0.2.0, maintain for v0.3.0)")
        else:
            print("\n  -> all sources verified (v0.2.0 milestone achieved)")
    else:
        print("  (registry not found or has no verification-status entries)")

    print("\n" + ("FAILED: unresolved citations." if fatal else "PASSED."))
    return 2 if fatal else 0


if __name__ == "__main__":
    sys.exit(main())
