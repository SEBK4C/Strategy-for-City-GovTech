# Literature Review State — City GovTech Strategy

**Version:** 0.1.1
**Last reviewed:** 2026-06-20
**Next review due:** 2026-09-20 (quarterly cadence)

This document tracks the current state of the literature review: what is covered, what is
missing, and what needs updating. It is the primary input to
`Scripts/update_literature_review.py`.

---

## Coverage map

### Covered (v0.1.0–0.1.1)

| Domain | Depth | Key gaps |
|---|---|---|
| E-government theory (Wirtz/Weyerer, Janowski) | Medium | No post-2022 literature on 4th-gen e-gov |
| Swiss EMBAG and federal digital strategy | High | Cantonal implementation data lacking |
| German OZG / OZG 2.0 | High | Municipal uptake statistics missing |
| Sovereign Cloud Stack | High | Production metrics not yet available |
| Open Source in EU public administration | Medium | OSOR annual report [50] listed; verification pending |
| Identity management (Keycloak, BundID, eID) | Medium | Swiss E-ID [51] now added |
| Decidim / participatory platforms | High | CONSUL Democracy [47] now added |
| Matrix/Element for government | Medium | BundesMessenger adoption data needed |
| Nextcloud for government | Medium | Swiss federal deployment details |
| Open data portals (CKAN) | Medium | opendata.swiss technical details |
| GIS for municipalities | Low | No academic literature cited |
| Procurement frameworks | Low | No comparative EU procurement studies |
| Total cost of ownership studies | Low | CRITICAL GAP — see below |
| User experience / satisfaction research | Absent | CRITICAL GAP — see below |
| Small municipality case studies | Low | CRITICAL GAP — see below |
| Change management in IT transitions | Low | Munich LiMux referenced but not deep |
| eCH standards (Switzerland) | Medium | [48] added; detailed eCH profiles needed |
| GovStack building blocks | Medium | [53] added; EU alignment analysis needed |
| EU Data Act implications | Low | [54] added; municipal impact analysis needed |
| ZenDiS / OpenDesk governance | Medium | [49] listed; annual report unverified |
| Foundational open-government theory | Medium | Lathrop & Ruma [52] added |

### Not yet covered

- **EU Data Governance Act 2022** (data sharing framework; interaction with municipal open data)
- **Digital Services Act / Digital Markets Act** — interaction with municipal procurement
- **OpenDesk v2.x** (2025/2026 updates)
- **Swiss OGD Strategy 2024–2027** (distinct from E-Government Strategy)
- **GAIA-X implementation status** (2025 state of play; relevance to municipal cloud)
- **Limesurvey / open-source survey tools** for citizen feedback
- **Nextcloud Hub 8 / Hub 9** (latest major releases; new features for government)
- **LibreOffice in public administration** (document format sovereignty)
- **Academic literature on participatory budgeting outcomes** (to support Decidim claims)
- **eIDAS 2.0 / EU Digital Identity Wallet** (interoperability with Swiss E-ID and BundID)

---

## Critical gaps

### TCO studies
No rigorous independent comparative Total Cost of Ownership studies cover the full
open-source vs. proprietary municipal stack. Available studies are vendor-commissioned
or context-specific (Munich LiMux 2003–2017; French state LibreOffice migration).
**Action:** identify/commission an independent municipal TCO methodology. Target: v0.2.0.

### User experience research
Almost no peer-reviewed literature exists on citizen satisfaction with open-source vs.
proprietary municipal digital services. **Action:** design a citizen-satisfaction survey
framework usable by participating municipalities. Target: v1.0 appendix.

### Small-municipality data
Most case studies involve large cities (Barcelona, Helsinki, Munich) or federal agencies.
The median EU municipality has population <10,000. **Action:** document 3–5 case studies
of municipalities <50,000 that completed open-source transitions. Target: v0.2.0.

---

## Improvement log

| Date | Action | By | Result |
|---|---|---|---|
| 2026-06-20 | Initial literature review, v0.1.0 draft | SG | 30 primary sources identified; 46 citation slots in papers |
| 2026-06-20 | Sources [47]–[54] added to registry | SG/AI | CONSUL, eCH, ZenDiS, OSOR, Swiss E-ID, Lathrop & Ruma, GovStack, EU Data Act |
| 2026-06-20 | German translation v0.1.0 completed | SG/AI | Full translation added at Doc/de/souveraen-von-grund-auf-v0.1.0.md |
| 2026-06-20 | Literature review state updated to v0.1.1 | SG/AI | Coverage map expanded; 10 new "not yet covered" items identified |

---

## Quarterly review checklist

When running `Scripts/update_literature_review.py`, check for:

- [ ] New Swiss e-government legislation or strategy updates
- [ ] New German OZG implementation reports or FITKO publications
- [ ] New EU legislation (Data Act, AI Act implementation, eIDAS 2.0, etc.)
- [ ] New Sovereign Cloud Stack releases or governance updates
- [ ] New openCode.de statistics or case studies
- [ ] New academic papers on e-government maturity (GIQ, ISM, EJEG)
- [ ] New municipal open-source deployments or case studies
- [ ] New security advisories affecting stack components
- [ ] OSOR annual report (EU Open Source Observatory, annual)
- [ ] UN E-Government Survey (biannual)
- [ ] ZenDiS annual report / OpenDesk release notes
- [ ] GovStack building block updates
- [ ] Swiss E-ID / BGEID implementation milestones
- [ ] Decidim and CONSUL Democracy new deployments
