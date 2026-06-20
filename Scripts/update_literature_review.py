#!/usr/bin/env python3
"""Print the recurring literature-review improvement agenda.

This script makes the literature review *self-improving* by surfacing, on each run, the
work needed to raise the quality of the review and the source registry:

  - the review's next-due date and whether it is overdue,
  - the critical gaps and not-yet-covered topics from ``Mem/literature-review-state.md``,
  - the open questions and follow-up leads from ``Mem/research-notes.md``,
  - the sources still pending verification in ``Mem/source-registry.md``.

It is read-only: it prints an agenda for a human (or a future agent run) to act on. Run it
at the start of each improvement cycle (suggested cadence: quarterly).

Usage:
    python3 Scripts/update_literature_review.py
"""
from __future__ import annotations

import datetime as dt
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
MEM = REPO_ROOT / "Mem"
STATE = MEM / "literature-review-state.md"
NOTES = MEM / "research-notes.md"
REGISTRY = MEM / "source-registry.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def extract_section(text: str, heading: str) -> str:
    """Return the lines under a Markdown heading until the next same-or-higher heading."""
    lines = text.splitlines()
    out: list[str] = []
    level = heading.count("#", 0, heading.find(" "))
    capturing = False
    for line in lines:
        if line.strip() == heading.strip():
            capturing = True
            continue
        if capturing and line.startswith("#"):
            this_level = len(line) - len(line.lstrip("#"))
            if this_level <= level:
                break
        if capturing:
            out.append(line)
    return "\n".join(out).strip()


def find_due_date(state: str) -> dt.date | None:
    m = re.search(r"Next review due:\*\*\s*(\d{4}-\d{2}-\d{2})", state)
    if not m:
        m = re.search(r"Next review due:\s*(\d{4}-\d{2}-\d{2})", state)
    if m:
        try:
            return dt.date.fromisoformat(m.group(1))
        except ValueError:
            return None
    return None


def unverified_sources(registry: str) -> list[str]:
    out: list[str] = []
    current_id = None
    for line in registry.splitlines():
        m = re.match(r"^###\s*(\[\d+\].*)$", line)
        if m:
            current_id = m.group(1).strip()
        # Match a real status line ("**Verification status:** unverified"), not the
        # template placeholder ("[unverified | verified | archived]").
        if re.search(r"Verification status:\*\*\s*unverified\b", line) and current_id:
            out.append(current_id)
    return out


def checkbox_items(block: str) -> list[str]:
    return [ln.strip() for ln in block.splitlines() if ln.strip().startswith(("- [ ]", "- [x]"))]


def bullet_items(block: str) -> list[str]:
    return [ln.strip() for ln in block.splitlines() if ln.strip().startswith(("- ", "* "))]


def main() -> int:
    today = dt.date.today()
    state = read(STATE)
    notes = read(NOTES)
    registry = read(REGISTRY)

    print("=" * 70)
    print("  LITERATURE-REVIEW IMPROVEMENT AGENDA")
    print(f"  Generated: {today.isoformat()}")
    print("=" * 70)

    due = find_due_date(state)
    if due:
        delta = (due - today).days
        if delta < 0:
            print(f"\n[!] Review is OVERDUE by {-delta} days (was due {due}).")
        else:
            print(f"\n[ ] Next review due in {delta} days ({due}).")
    else:
        print("\n[ ] No 'Next review due' date found in literature-review-state.md.")

    pending = unverified_sources(registry)
    print("\n--- Sources pending verification (target: 0 for v0.2.0) ---")
    if pending:
        for s in pending:
            print(f"  - {s}")
    else:
        print("  none — all registry sources verified or archived.")

    crit = extract_section(state, "## Critical gaps")
    print("\n--- Critical gaps to close ---")
    print("  " + (crit.replace("\n", "\n  ") if crit else "(none recorded)"))

    notyet = extract_section(state, "### Not yet covered")
    print("\n--- Topics not yet covered ---")
    items = bullet_items(notyet)
    for it in items[:20]:
        print("  " + it)
    if not items:
        print("  (none recorded)")

    leads = extract_section(notes, "### Leads to follow up")
    print("\n--- Open leads (from research-notes.md) ---")
    todo = checkbox_items(leads)
    for it in todo:
        print("  " + it)
    if not todo:
        print("  (none recorded)")

    checklist = extract_section(state, "## Quarterly review checklist")
    print("\n--- Quarterly review checklist ---")
    cl = checkbox_items(checklist)
    for it in cl:
        print("  " + it)
    if not cl:
        print("  (none recorded)")

    print("\n" + "=" * 70)
    print("  Next steps: research the items above, update Mem/source-registry.md and")
    print("  Mem/literature-review-state.md, then revise Doc/ papers and bump the version.")
    print("  Finish by running: python3 Scripts/validate_citations.py")
    print("=" * 70)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
