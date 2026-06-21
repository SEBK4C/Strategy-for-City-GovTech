#!/usr/bin/env python3
"""
update_literature_review.py

Self-improving literature review maintenance script.
Provides structured prompts and checklists for quarterly review cycles.
Can output a Markdown agenda, check for stale sources, and generate
a summary of what's missing relative to the next version milestone.

Usage:
    python3 Scripts/update_literature_review.py          # print review agenda
    python3 Scripts/update_literature_review.py --agenda  # same
    python3 Scripts/update_literature_review.py --gaps    # print gap analysis only
    python3 Scripts/update_literature_review.py --stale   # report sources older than N years
"""

import re
import sys
import argparse
from pathlib import Path
from datetime import datetime

REGISTRY_PATH = Path("Mem/source-registry.md")
LIT_REVIEW_PATH = Path("Mem/literature-review-state.md")

# Version milestones and their critical gaps
MILESTONES = {
    "v0.2.0": {
        "description": "Citation-complete draft",
        "achieved": True,
        "gaps_closed": [
            "eCH standards [47]",
            "GovStack [48]",
            "EU Data Act [49]",
            "EU AI Act [50]",
            "ZenDiS [51]",
            "GAIA-X [52]",
            "CONSUL Democracy [54]",
            "Swiss OGD Strategy [55]",
            "Lathrop & Ruma [56]",
            "EU Data Governance Act [58]",
            "Munich LiMux post-mortem [59]",
            "DINUM open source report [60]",
        ],
    },
    "v1.0.0": {
        "description": "Externally shareable release",
        "achieved": False,
        "required_gaps_to_close": [
            "Longitudinal TCO study (5+ year)",
            "Citizen satisfaction survey instrument",
            "AI Act compliance cost data",
            "Swiss E-ID Act integration architecture",
            "OSOR Annual Report 2024",
            "EU Cyber Resilience Act [CRA] implications",
            "eIDAS 2.0 implementing acts / EUDI Wallet architecture",
            "Small municipality sample expanded to 5+ cases",
        ],
    },
}

QUARTERLY_REVIEW_TOPICS = [
    ("Swiss e-government", [
        "New EMBAG cantonal implementation legislation or reports",
        "E-Government Strategy 2024-2027 annual progress report",
        "Swiss E-ID Act progress, implementing regulations, and timeline",
        "OGD Strategy Switzerland 2024-2027 annual implementation update",
        "eCH new or updated standards (ech.ch/standards)",
        "opendata.swiss portal statistics and new datasets",
    ]),
    ("German e-government / OZG", [
        "OZG 2.0 implementation progress report (bmi.bund.de)",
        "FITKO annual report or major publication (fitko.de)",
        "ZenDiS annual report or OpenDesk release notes (zendis.de)",
        "openCode.de repository count and notable new projects",
        "govdigital eG new member municipalities or SCS deployments",
        "Dataport, AKDB, or other cooperative IT provider updates",
    ]),
    ("EU legislation and policy", [
        "EU AI Act: delegated acts and implementing regulations (EUR-Lex)",
        "EU Data Act: implementing acts and cloud-switching guidance (EUR-Lex)",
        "EU Cyber Resilience Act: timeline and SBOM requirements",
        "Interoperable Europe Board: first annual report and decisions",
        "EUCS (EU Cloud Certification Scheme): ENISA publication updates",
        "eIDAS 2.0: EUDI Wallet Architecture and Reference Framework updates",
        "EU Open Source Strategy successor (expected 2024-2026)",
    ]),
    ("Technology stack", [
        "Sovereign Cloud Stack: new release, SCS R7+, new SCS-certified operators",
        "Keycloak: major version updates, eIDAS 2.0 / OID4VC support",
        "Nextcloud: government edition updates, new Swiss/German deployments",
        "Matrix/Element: BundesMessenger adoption data, new government deployments",
        "Decidim: new major deployments, social contract updates",
        "CKAN: DGA compliance plugin, DCAT-AP.de updates",
        "Camunda / Flowable: government-specific features, XÖV/eCH connectors",
        "OpenDesk: v2.x component updates",
    ]),
    ("Academic literature", [
        "New papers in Government Information Quarterly (GIQ)",
        "New papers in Information Systems Management (ISM)",
        "New papers in Electronic Journal of e-Government (EJEG)",
        "OSOR Annual Report (joinup.ec.europa.eu/collection/open-source-observatory-osor)",
        "UN E-Government Survey 2024 (biannual)",
        "New municipal open-source transition case studies",
        "New comparative TCO studies for government software",
    ]),
    ("Security", [
        "BSI IT-Grundschutz: new edition or module updates (bsi.bund.de)",
        "NIS2 transposition status across EU member states",
        "New CVEs affecting stack components (prometheus, keycloak, nextcloud, etc.)",
        "Sigstore / supply chain security best practices for government",
        "SBOM tooling updates (SPDX 3.0, CycloneDX 1.6+)",
    ]),
    ("Small municipalities", [
        "New case studies: municipalities < 100,000 implementing open-source stacks",
        "Kommunales Open-Data-Netzwerk NRW: new member municipalities",
        "Schweizer Gemeinden: new open-source or OGD deployments",
        "Austrian Gemeinden: open-source initiatives (datenschutz.gv.at, etc.)",
    ]),
]


def print_review_agenda(next_review_date: str = None):
    """Print a structured quarterly review agenda."""
    today = datetime.now().strftime("%Y-%m-%d")
    if not next_review_date:
        from datetime import timedelta
        next_q = datetime.now().replace(
            month=((datetime.now().month - 1) // 3 + 1) * 3 % 12 + 1,
            day=1,
        )
        next_review_date = (next_q).strftime("%Y-%m-%d")

    print(f"\n# Literature Review Agenda")
    print(f"Generated: {today} | Next review due: {next_review_date}")
    print(f"Source: {LIT_REVIEW_PATH} | Registry: {REGISTRY_PATH}\n")

    print("## Version Milestones\n")
    for version, info in MILESTONES.items():
        status = "✅ Achieved" if info["achieved"] else "⏳ In progress"
        print(f"### {version} — {info['description']} [{status}]")
        if info["achieved"] and "gaps_closed" in info:
            print(f"Gaps closed: {len(info['gaps_closed'])}")
            for gap in info["gaps_closed"]:
                print(f"  - {gap}")
        elif not info["achieved"] and "required_gaps_to_close" in info:
            print(f"Required to achieve:")
            for gap in info["required_gaps_to_close"]:
                print(f"  - [ ] {gap}")
        print()

    print("## Quarterly Review Checklist\n")
    for topic, items in QUARTERLY_REVIEW_TOPICS:
        print(f"### {topic}\n")
        for item in items:
            print(f"- [ ] {item}")
        print()

    print("## How to update sources\n")
    print("1. For each checked item above, verify against primary source.")
    print("2. If new source found: add entry to Mem/source-registry.md using template.")
    print("3. If source updates existing entry: update 'Publication date' and 'Notes' fields.")
    print("4. If gap is now closed: update Mem/literature-review-state.md coverage map.")
    print("5. If new content warrants paper update: create new version branch and update")
    print("   the relevant paper sections with new citations.")
    print("6. Run: python3 Scripts/validate_citations.py --all to check citation integrity.")
    print("7. Run: python3 Scripts/build_govtech_docs.py to rebuild all outputs.")


def print_gap_analysis():
    """Print only the gap analysis for the next version."""
    print("\n# Gap Analysis: What's needed for v1.0.0\n")
    v1 = MILESTONES.get("v1.0.0", {})
    required = v1.get("required_gaps_to_close", [])
    if not required:
        print("No gaps recorded for v1.0.0.")
        return
    print(f"{len(required)} gaps to close before external release:\n")
    for i, gap in enumerate(required, 1):
        print(f"{i}. [ ] {gap}")


def report_stale_sources(years: int = 3):
    """Report registry entries with publication dates older than N years."""
    if not REGISTRY_PATH.exists():
        print(f"Registry not found: {REGISTRY_PATH}")
        return

    text = REGISTRY_PATH.read_text(encoding="utf-8")
    current_year = datetime.now().year
    threshold_year = current_year - years

    print(f"\n# Stale Sources (publication year <= {threshold_year})\n")
    stale = []
    for match in re.finditer(r"### \[(\d+)\] (.+?)\n(.*?)(?=### \[\d+\]|## |---| *$)", text, re.DOTALL):
        cid = match.group(1)
        name = match.group(2).strip()
        body = match.group(3)
        date_match = re.search(r"\*\*Publication date:\*\*\s*(\d{4})", body)
        if date_match:
            year = int(date_match.group(1))
            if year <= threshold_year:
                stale.append((int(cid), name, year))

    if stale:
        for cid, name, year in sorted(stale):
            print(f"[{cid}] {name} ({year})")
        print(f"\nTotal: {len(stale)} source(s) published in {threshold_year} or earlier.")
        print("Review these for new editions, updated URLs, or superseding documents.")
    else:
        print(f"No sources older than {years} years found.")


def main():
    parser = argparse.ArgumentParser(description="Self-improving literature review maintenance.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--agenda", action="store_true", default=True, help="Print quarterly review agenda (default)")
    group.add_argument("--gaps", action="store_true", help="Print gap analysis for next version")
    group.add_argument("--stale", action="store_true", help="Report sources older than 3 years")
    parser.add_argument("--years", type=int, default=3, help="Stale threshold in years (default: 3)")
    args = parser.parse_args()

    if args.gaps:
        print_gap_analysis()
    elif args.stale:
        report_stale_sources(years=args.years)
    else:
        print_review_agenda()


if __name__ == "__main__":
    main()
