# Literature Review State — City GovTech Strategy

**Version:** 0.1.0
**Last reviewed:** 2026-06-20
**Next review due:** 2026-09-20 (quarterly cadence)

This document tracks the current state of the literature review: what is covered, what is
missing, and what needs updating. It is the primary input to
`Scripts/update_literature_review.py`.

---

## Coverage map

### Covered (v0.1.0)

| Domain | Depth | Key gaps |
|---|---|---|
| E-government theory (Wirtz/Weyerer, Janowski) | Medium | No post-2022 literature on 4th-gen e-gov |
| Swiss EMBAG and federal digital strategy | High | Cantonal implementation data lacking |
| German OZG / OZG 2.0 | High | Municipal uptake statistics missing |
| Sovereign Cloud Stack | High | Production metrics not yet available |
| Open Source in EU public administration | Medium | OSOR annual report not yet integrated |
| Identity management (Keycloak, BundID, eID) | Medium | BundID uptake data missing |
| Decidim / participatory platforms | Medium | Schaffhausen canton case study needed |
| Matrix/Element for government | Medium | BundesMessenger adoption data needed |
| Nextcloud for government | Medium | Swiss federal deployment details |
| Open data portals (CKAN) | Medium | opendata.swiss technical details |
| GIS for municipalities | Low | No academic literature cited |
| Procurement frameworks | Low | No comparative EU procurement studies |
| Total cost of ownership studies | Low | CRITICAL GAP — see below |
| User experience / satisfaction research | Absent | CRITICAL GAP — see below |
| Small municipality case studies | Low | CRITICAL GAP — see below |
| Change management in IT transitions | Low | Munich LiMux referenced but not deep |

### Not yet covered

- **eCH standards** (Swiss XML interoperability, equivalent to German XÖV)
- **CONSUL Democracy platform** (Madrid; alternative/complement to Decidim)
- **GovStack** (ITU/DIAL initiative for government digital building blocks)
- **EU Data Act 2023** (implications for municipal data governance)
- **Digital Services Act / Digital Markets Act** — interaction with municipal procurement
- **OpenDesk v2.x** (2025/2026 updates)
- **ZenDiS** (German Centre for Digital Sovereignty — key actor, under-covered)
- **Lathrop & Ruma (2010)** — Open Government foundational text
- **OSOR Annual Report 2023** (EU Open Source Observatory)
- **Swiss OGD Strategy 2024–2027**
- **GAIA-X implementation status** (2025 state of play)

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

---

## Quarterly review checklist

When running `Scripts/update_literature_review.py`, check for:

- [ ] New Swiss e-government legislation or strategy updates
- [ ] New German OZG implementation reports or FITKO publications
- [ ] New EU legislation (Data Act, AI Act implementation, etc.)
- [ ] New Sovereign Cloud Stack releases or governance updates
- [ ] New openCode.de statistics or case studies
- [ ] New academic papers on e-government maturity (GIQ, ISM, EJEG)
- [ ] New municipal open-source deployments or case studies
- [ ] New security advisories affecting stack components
- [ ] OSOR annual report (EU Open Source Observatory, annual)
- [ ] UN E-Government Survey (biannual)
