#!/usr/bin/env python3
"""
update_literature_review.py

Quarterly literature review improvement script.
Prints a structured checklist of sources and topics to check for updates,
then generates a diff of what has changed since the last review.

Usage:
    python3 Scripts/update_literature_review.py [--since YYYY-MM-DD]

Designed to be run quarterly by the project maintainer. Output is a
structured prompt for manual research, not an automated crawler.
"""

import sys
import argparse
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).parent.parent
MEM = ROOT / "Mem"

CHECKLIST = [
    ("Swiss legislation", [
        "New Swiss e-government legislation (fedlex.admin.ch/eli/oc)",
        "EMBAG cantonal implementation reports",
        "E-Government Strategy 2024-2027 annual progress report (egovernment.ch)",
        "Swiss OGD Strategy updates (opendata.swiss/de/organization/bk)",
        "New eCH standards published (ech.ch/standards)",
        "Swiss E-ID (BGEID) implementation milestones (e-id.ch)",
    ]),
    ("German federal and state", [
        "New OZG 2.0 implementation reports (fitko.de)",
        "FITKO annual report (fitko.de/jahresbericht)",
        "ZenDiS publications and OpenDesk release notes (zendis.de, opendesk.eu)",
        "openCode.de statistics and new repos (opencode.de)",
        "Sovereign Cloud Stack releases and governance updates (scs.community/blog)",
        "govdigital eG news (govdigital.de)",
        "BSI IT-Grundschutz updates (bsi.bund.de)",
        "Dataport and AKDB annual reports",
    ]),
    ("EU legislation and policy", [
        "EU AI Act implementation: ENISA guidance, CEN/CENELEC standards",
        "EU Data Act implementation updates",
        "Interoperable Europe Act Board decisions (interoperable-europe.eu)",
        "eIDAS 2.0 / EUDI Wallet pilot results",
        "EU Open Source Strategy renewal (post-2023)",
        "New European Interoperability Framework (EIF) updates",
        "DCAT-AP 3.0 adoption in national portals",
        "NIS2 transposition status in DE and CH",
    ]),
    ("Open-source ecosystem", [
        "OSOR Annual Report (joinup.ec.europa.eu) - search 'OSOR report'",
        "Decidim Association annual report (decidim.org/blog)",
        "Matrix Foundation releases and government deployments (matrix.org/blog)",
        "Nextcloud government reference deployments (nextcloud.com/blog)",
        "CKAN community updates (ckan.org/blog)",
        "CONSUL Democracy new deployments (consuldemocracy.org)",
        "TYPO3 GovPack updates (typo3.org)",
        "Camunda / Flowable government use case publications",
    ]),
    ("Academic literature", [
        "Google Scholar alert: 'e-government maturity' site:doi.org (last 12 months)",
        "Government Information Quarterly (GIQ) new issues",
        "Information Systems Management (ISM) new issues",
        "Electronic Journal of e-Government (EJEG) new issues",
        "New case studies of municipal open-source transitions (any size)",
        "New TCO studies comparing open-source and proprietary in public sector",
        "User experience / citizen satisfaction with digital government services",
        "Small municipality (<50k) digital transformation case studies",
    ]),
    ("Security and infrastructure", [
        "New CVEs in stack components: Keycloak, Nextcloud, Camunda, CKAN, TYPO3, Matrix",
        "BSI warnings or advisories for open-source government software",
        "NIS2 incident reports involving open-source municipal systems",
        "GAIA-X certification updates (gaia-x.eu/news)",
        "SCS compliance certification new entrants",
    ]),
    ("New municipal deployments to document", [
        "Decidim new deployments (decidim.org/census)",
        "Matrix/Element government deployments (matrix.org)",
        "CKAN-based national/municipal portals",
        "Municipalities <100k that have completed open-source transitions",
        "OpenDesk pilot municipality results",
    ]),
]


def main():
    parser = argparse.ArgumentParser(description="Generate quarterly literature review checklist")
    parser.add_argument("--since", default=None,
                        help="Date of last review (YYYY-MM-DD). Defaults to 90 days ago.")
    args = parser.parse_args()

    if args.since:
        try:
            since_date = date.fromisoformat(args.since)
        except ValueError:
            print(f"ERROR: Invalid date format: {args.since}", file=sys.stderr)
            sys.exit(1)
    else:
        since_date = date.today() - timedelta(days=90)

    today = date.today()

    print(f"="*70)
    print(f"QUARTERLY LITERATURE REVIEW CHECKLIST")
    print(f"City GovTech Strategy — Autonomous Office of Civil Digital Infrastructure")
    print(f"Review date: {today}")
    print(f"Covering changes since: {since_date}")
    print(f"="*70)
    print()

    # Load current literature review state
    state_path = MEM / "literature-review-state.md"
    if state_path.exists():
        state_text = state_path.read_text(encoding="utf-8")
        print("CURRENT STATE (from Mem/literature-review-state.md):")
        # Print critical gaps section
        in_gaps = False
        for line in state_text.splitlines():
            if "## Critical gaps" in line:
                in_gaps = True
            elif in_gaps and line.startswith("## ") and "Critical" not in line:
                break
            if in_gaps:
                print(f"  {line}")
        print()

    print("CHECKLIST (work through each category; note findings in Mem/research-notes.md):")
    print()

    for category, items in CHECKLIST:
        print(f"## {category}")
        for item in items:
            print(f"  [ ] {item}")
        print()

    print("="*70)
    print("AFTER COMPLETING REVIEW:")
    print("  1. Update Mem/source-registry.md with new entries")
    print("  2. Update Mem/literature-review-state.md coverage map")
    print("  3. Update Mem/research-notes.md with key findings")
    print("  4. Update paper sections where coverage gaps were filled")
    print("  5. Run: python3 Scripts/validate_citations.py --strict")
    print("  6. Bump paper version if changes are substantial")
    print("  7. Commit with message: 'docs: quarterly literature review YYYY-QN'")
    print("="*70)


if __name__ == "__main__":
    main()
