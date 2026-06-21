#!/usr/bin/env python3
"""
Literature review improvement script for City GovTech Strategy.

Provides a structured checklist and prompts for quarterly literature review updates.
Reads the current state from Mem/literature-review-state.md and generates
an improvement agenda based on gaps and next-review dates.

Usage:
    python3 Scripts/update_literature_review.py [--check] [--agenda]

    --check   : Print current coverage status and highlight critical gaps
    --agenda  : Generate a structured improvement agenda for the next review cycle
"""

import re
import sys
from datetime import date, datetime
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
MEM_DIR = REPO_ROOT / "Mem"
LIT_REVIEW_STATE = MEM_DIR / "literature-review-state.md"
SOURCE_REGISTRY = MEM_DIR / "source-registry.md"


QUARTERLY_CHECKLIST = """
=== QUARTERLY LITERATURE REVIEW CHECKLIST ===
Date: {today}
Next review due: {next_review}

For each item below, check the relevant source and update Mem/source-registry.md
and Mem/literature-review-state.md if new information is found.

1. SWISS E-GOVERNMENT
   [ ] New legislation or strategy (fedlex.admin.ch, egovernment.ch)
   [ ] EMBAG implementation reports (bar.admin.ch, isb.admin.ch)
   [ ] E-Government Schweiz progress report
   [ ] opendata.swiss statistics update
   [ ] Swiss eID v2 (e-id.ch) — technical details or deployment update
   [ ] eCH standard revisions (ech.ch/standards)
   [ ] ZenDiS equivalent / cantonal sovereignty initiatives

2. GERMAN OZG / OPEN-SOURCE ECOSYSTEM
   [ ] FITKO annual report or quarterly publication (fitko.de)
   [ ] openCode.de statistics (number of repos, downloads, contributors)
   [ ] New EfA (Einer für Alle) service components available
   [ ] OZG 2.0 implementation progress (BMI)
   [ ] ZenDiS publications and OpenDesk updates (zendisgmbh.de)
   [ ] govdigital eG new members or services
   [ ] BSI IT-Grundschutz edition update (bsi.bund.de)
   [ ] BSI C5 attested operators list update

3. EUROPEAN UNION
   [ ] Interoperable Europe Act implementation guidance (joinup.ec.europa.eu)
   [ ] EU Data Act implementing measures (eur-lex.europa.eu)
   [ ] OSOR annual report (joinup.ec.europa.eu/osor)
   [ ] EU Open Source Strategy successor (DG DIGIT)
   [ ] New EU legislation affecting public sector ICT

4. TECHNOLOGY STACK COMPONENTS
   [ ] Sovereign Cloud Stack new release (scs.community)
   [ ] Keycloak major version update (keycloak.org)
   [ ] Nextcloud major version (nextcloud.com)
   [ ] Decidim new release or new deployments (decidim.org)
   [ ] Matrix specification update (spec.matrix.org)
   [ ] CKAN new release (ckan.org)
   [ ] Camunda / Flowable major update
   [ ] GovStack specification update (govstack.global)

5. ACADEMIC LITERATURE
   [ ] Search GIQ (Government Information Quarterly) last 6 months
   [ ] Search EJEG (European Journal of E-Government) last 6 months
   [ ] Search ISM (Information Systems Management) last 6 months
   [ ] Search for "open source government" AND "municipality" OR "Gemeinde"
   [ ] Search for "digital sovereignty" AND "public administration" last 12 months
   [ ] UN E-Government Survey (biannual, check if new edition available)

6. CASE STUDIES AND DEPLOYMENTS
   [ ] New municipal open-source transitions (openCode.de, OSOR case studies)
   [ ] Barcelona Decidim updates (decidim.barcelona)
   [ ] Helsinki open data updates (hri.fi)
   [ ] OpenDesk new deployments (zendisgmbh.de)
   [ ] German BundesMessenger deployment statistics
   [ ] Swiss pilot deployments (egovernment.ch)

7. SECURITY
   [ ] Critical CVEs in any stack component in the last quarter
   [ ] New BSI publications on cloud security
   [ ] NIS2 transposition status in CH/DE (NIS2 deadline: Oct 2024)

=== END CHECKLIST ===
"""

IMPROVEMENT_AGENDA = """
=== LITERATURE REVIEW IMPROVEMENT AGENDA v{version} ===
Generated: {today}

Based on the current literature review state, the following improvements
are prioritised for the next review cycle:

PRIORITY 1 — Critical gaps (block v1.0 release)
-------------------------------------------------
{priority_1}

PRIORITY 2 — Should address before v0.3.0
------------------------------------------
{priority_2}

PRIORITY 3 — Backlog (address before v1.0)
-------------------------------------------
{priority_3}

=== WORKFLOW ===
1. Complete Priority 1 items
2. Update Mem/source-registry.md with new sources
3. Update Mem/literature-review-state.md coverage map
4. Update Doc/en/sovereign-by-design-v*.md with new citations
5. Run: python3 Scripts/validate_citations.py
6. Run: python3 Scripts/build_govtech_docs.py
7. Update Mem/literature-review-state.md improvement log
8. Bump paper version if substantive new content added
"""

P1_GAPS = """\
- Independent TCO study — commission or conduct comparative analysis
  (target: v0.3.0, enables replacing indicative figures with validated data)
- User experience research framework — design citizen satisfaction survey
  (target: v1.0 appendix)
- 3-5 small-municipality case studies (population <50,000)
  (target: v0.3.0 companion paper)"""

P2_GAPS = """\
- Barcelona Digital City Plan 2017 — add as primary source [55]
- Munich LiMux post-mortem primary academic sources — identify specific papers
- Swiss eID v2 technical details — update Section 3.4
- AKDB (Bayern) reference deployment — add dedicated source entry
- EU Data Act municipal procurement practice (emerging 2025-2026)"""

P3_GAPS = """\
- Individual eCH standards (eCH-0011, eCH-0058) — dedicated section in Section 3.6
- BSI C5 catalogue (cloud hosting compliance) — add as source [56]
- CONSUL Democracy in-depth case analysis — expand Section 3.9
- GAIA-X current implementation status — determine relevance for stack
- Digital Services Act / Digital Markets Act — assess implications for Section 6.2
- OpenDesk v2.x / 2026 update — update Section 3.5 if material change"""


def parse_next_review(state_text: str) -> str:
    """Extract next review date from literature-review-state.md."""
    m = re.search(r"\*\*Next review due:\*\* (\S+)", state_text)
    return m.group(1) if m else "2026-09-20"


def parse_version(state_text: str) -> str:
    """Extract version from literature-review-state.md."""
    m = re.search(r"\*\*Version:\*\* (\S+)", state_text)
    return m.group(1) if m else "0.2.0"


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Update literature review for GovTech strategy.")
    parser.add_argument("--check", action="store_true", help="Print coverage status")
    parser.add_argument("--agenda", action="store_true", help="Print improvement agenda")
    parser.add_argument("--checklist", action="store_true", help="Print quarterly checklist")
    args = parser.parse_args()

    if not any([args.check, args.agenda, args.checklist]):
        args.check = True
        args.checklist = True

    today = date.today().isoformat()

    if LIT_REVIEW_STATE.exists():
        state_text = LIT_REVIEW_STATE.read_text(encoding="utf-8")
        next_review = parse_next_review(state_text)
        version = parse_version(state_text)
    else:
        print(f"WARNING: {LIT_REVIEW_STATE} not found — using defaults.", file=sys.stderr)
        next_review = "2026-09-20"
        version = "0.2.0"
        state_text = ""

    if args.check:
        print(f"Literature Review State: {LIT_REVIEW_STATE.relative_to(REPO_ROOT)}")
        print(f"Version: {version}")
        print(f"Next review: {next_review}")
        try:
            nr = datetime.fromisoformat(next_review).date()
            delta = (nr - date.today()).days
            if delta <= 0:
                print(f"  OVERDUE — review was due {abs(delta)} days ago!")
            elif delta <= 14:
                print(f"  Review due in {delta} days — prepare now.")
            else:
                print(f"  Review in {delta} days.")
        except ValueError:
            pass
        print()

    if args.checklist:
        print(QUARTERLY_CHECKLIST.format(today=today, next_review=next_review))

    if args.agenda:
        print(IMPROVEMENT_AGENDA.format(
            version=version,
            today=today,
            priority_1=P1_GAPS,
            priority_2=P2_GAPS,
            priority_3=P3_GAPS,
        ))


if __name__ == "__main__":
    main()
