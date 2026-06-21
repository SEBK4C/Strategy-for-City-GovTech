#!/usr/bin/env python3
"""Print the recurring literature-review improvement agenda.

This script makes the literature review *self-improving* by surfacing, on each run, the
work needed to raise the quality of the review and the source registry:

  - the review's next-due date and whether it is overdue,
  - the critical gaps and not-yet-covered topics from ``Mem/literature-review-state.md``,
  - the open questions and research hypotheses from ``Mem/research-notes.md``,
  - the sources still pending verification in ``Mem/source-registry.md``.

It is read-only: it prints an agenda for a human (or a future agent run) to act on. Run it
at the start of each improvement cycle (suggested cadence: quarterly).

Usage:
    python3 Scripts/update_literature_review.py
    python3 Scripts/update_literature_review.py --brief   # shorter output
"""
from __future__ import annotations

import argparse
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
    level = len(heading) - len(heading.lstrip("#"))
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


def find_version(state: str) -> str:
    m = re.search(r"\*\*Version:\*\*\s*(\S+)", state)
    return m.group(1) if m else "unknown"


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


def unverified_sources(registry: str) -> list[tuple[str, str]]:
    """Return list of (id_header, notes) for unverified sources."""
    out: list[tuple[str, str]] = []
    current_id = None
    for line in registry.splitlines():
        m = re.match(r"^###\s*(\[\d+\].*)$", line)
        if m:
            current_id = m.group(1).strip()
        if re.search(r"Verification status:\*\*\s*unverified\b", line) and current_id:
            # Extract the note on the same line after 'unverified'
            note_match = re.search(r"unverified\s*—?\s*(.+)", line)
            note = note_match.group(1).strip() if note_match else ""
            out.append((current_id, note))
    return out


def checkbox_items(block: str) -> list[str]:
    return [ln.strip() for ln in block.splitlines() if ln.strip().startswith(("- [ ]", "- [x]"))]


def bullet_items(block: str) -> list[str]:
    return [ln.strip() for ln in block.splitlines() if ln.strip().startswith(("- ", "* "))]


def extract_open_questions(notes: str) -> list[str]:
    """Extract all open question bullet points from the most recent research round."""
    questions: list[str] = []
    # Find all '### Open questions' sections and take only the most recent round's items
    sections = re.split(r"(?=### Open questions)", notes)
    for section in reversed(sections):
        if section.strip().startswith("### Open questions"):
            items = bullet_items(section)
            if items:
                questions = items
                break
    return questions


def extract_hypotheses(notes: str) -> list[str]:
    """Extract research hypotheses from research-notes.md."""
    block = extract_section(notes, "### Hypotheses to test (priority order)")
    if not block:
        block = extract_section(notes, "### Hypotheses")
    return bullet_items(block)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--brief", action="store_true", help="Shorter output (skip hypotheses and checklist)")
    args = parser.parse_args()

    today = dt.date.today()
    state = read(STATE)
    notes = read(NOTES)
    registry = read(REGISTRY)

    print("=" * 70)
    print("  LITERATURE-REVIEW IMPROVEMENT AGENDA")
    print(f"  Generated: {today.isoformat()}")
    version = find_version(state)
    print(f"  Current version: {version}")
    print("=" * 70)

    # 1. Due-date check
    due = find_due_date(state)
    if due:
        delta = (due - today).days
        if delta < 0:
            print(f"\n[!] Review is OVERDUE by {-delta} days (was due {due}).")
        else:
            print(f"\n[ ] Next review due in {delta} days ({due}).")
    else:
        print("\n[ ] No 'Next review due' date found in literature-review-state.md.")

    # 2. Unverified sources
    pending = unverified_sources(registry)
    print(f"\n--- Sources pending verification ({len(pending)} remaining) ---")
    if pending:
        for sid, note in pending:
            print(f"  - {sid}" + (f" [{note}]" if note else ""))
    else:
        print("  none — all registry sources verified or archived.")

    # 3. Critical gaps
    crit = extract_section(state, "## Critical gaps (still open)")
    if not crit:
        crit = extract_section(state, "## Critical gaps")
    print("\n--- Critical gaps to close ---")
    print("  " + (crit.replace("\n", "\n  ") if crit else "(none recorded)"))

    # 4. Not-yet-covered topics (v.next targets)
    notyet = extract_section(state, "### Not yet covered (v0.3.0 targets)")
    if not notyet:
        notyet = extract_section(state, "### Not yet covered")
    print("\n--- Topics not yet covered ---")
    items = bullet_items(notyet)
    for it in items[:15]:
        print("  " + it)
    if not items:
        print("  (none recorded)")

    # 5. Open questions from latest research round
    print("\n--- Open research questions (latest round) ---")
    questions = extract_open_questions(notes)
    for q in questions[:10]:
        print("  " + q)
    if not questions:
        print("  (none recorded)")

    if not args.brief:
        # 6. Hypotheses
        print("\n--- Research hypotheses to test ---")
        hyps = extract_hypotheses(notes)
        for h in hyps[:6]:
            print("  " + h)
        if not hyps:
            print("  (none recorded)")

        # 7. Quarterly checklist
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
