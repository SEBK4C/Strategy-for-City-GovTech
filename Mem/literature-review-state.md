# Literature Review State — City GovTech Strategy

**Version:** 0.2.0
**Last reviewed:** 2026-06-21
**Next review due:** 2026-09-21 (quarterly cadence)

This document tracks the current state of the literature review: what is covered, what is
missing, and what needs updating. It is the primary input to
`Scripts/update_literature_review.py`.

---

## Coverage map

### Covered (v0.2.0)

| Domain | Depth | Key gaps |
|---|---|---|
| E-government theory (Wirtz/Weyerer, Janowski) | Medium | No post-2022 literature on 4th-gen e-gov |
| Swiss EMBAG and federal digital strategy | High | Cantonal implementation data lacking |
| German OZG / OZG 2.0 | High | Municipal uptake statistics missing |
| Sovereign Cloud Stack | High | Production metrics not yet available |
| Open Source in EU public administration | High | OSOR Annual Report 2023 now integrated [18] |
| Identity management (Keycloak, BundID, eID) | Medium | BundID uptake data missing |
| Decidim / participatory platforms | High | Schaffhausen canton case study still needed |
| CONSUL Democracy platform | Low | Added [31]; depth coverage v0.3.0 |
| Matrix/Element for government | Medium | BundesMessenger adoption data needed |
| Nextcloud for government | Medium | Swiss federal deployment details |
| Open data portals (CKAN) | Medium | opendata.swiss technical details |
| GIS for municipalities | Low | No academic literature cited |
| Procurement frameworks | Medium | Procurement clauses now in Appendix B |
| Total cost of ownership studies | Medium | Economic analysis Section 3.6; no independent study |
| User experience / satisfaction research | Absent | CRITICAL GAP — see below |
| Small municipality case studies | Low | CRITICAL GAP — see below |
| Change management in IT transitions | Low | Munich LiMux referenced but not deep |
| eCH standards (Switzerland) | Low | Added [15]; depth coverage v0.3.0 |
| GovStack (ITU/DIAL building blocks) | Low | Added [28]; depth coverage v0.3.0 |
| ZenDiS / OpenDesk governance | Low | Added [17]; depth coverage v0.3.0 |
| Open Government theory (Lathrop/Ruma) | Low | Added [32]; depth coverage v0.3.0 |
| eIDAS 2.0 Regulation | Medium | Added [40]; EU Digital Identity Wallet framing |
| AKDB / cooperative IT providers | Low | Added [25]; depth coverage v0.3.0 |
| OpenTofu / infrastructure-as-code | Low | Added [38]; practical tooling for IaC |

### Not yet covered (target v0.3.0)

- **eCH standards depth** (eCH-0058, eCH-0020, eCH-0007 — which matter most for municipalities?)
- **Heeks (2006)** — "Implementing and Managing eGovernment" (foundational failure analysis text)
- **OSOR factsheets** (individual component assessments from the EU Open Source Observatory)
- **Swiss E-ID technical specification** (mid-2026 state; cantonal adoption map)
- **EU Data Act 2023** (Regulation EU 2023/2854) — implications for municipal data governance
- **Digital Services Act / Digital Markets Act** — interaction with municipal procurement
- **OpenDesk v2.x** (2025/2026 updates; ZenDiS Jahresbericht 2024 when published)
- **GAIA-X implementation status 2026** — practical municipal tools or policy only?
- **UN E-Government Survey 2024** (biannual; last was 2022)
- **German OZG implementation statistics 2025–2026** (FITKO annual report)
- **Schaffhausen Decidim case study** — direct contact required
- **Independent municipal TCO methodology** (non-vendor; target: commission or locate)
- **Small-municipality case studies** (3–5 municipalities <50,000 with completed OS transitions)

---

## Critical gaps

### TCO studies — partially resolved
Section 3.6 of v0.2.0 includes an economic analysis (licence cost savings, 5-year TCO
model, vendor lock-in quantification). The analysis is based on available data (French
Gendarmerie, LiMux post-mortems, licence price benchmarks) rather than an independent
municipal TCO study. **Action:** locate or commission an independent government-software
TCO methodology applicable to municipalities <100,000. Target: v0.3.0.

### User experience research — still absent
Almost no peer-reviewed literature exists on citizen satisfaction with open-source vs.
proprietary municipal digital services. **Action:** design a citizen-satisfaction survey
framework usable by participating municipalities. Target: v1.0 appendix.

### Small-municipality data — still a gap
Most case studies involve large cities (Barcelona, Helsinki, Munich) or federal agencies.
The median EU municipality has population <10,000. **Action:** document 3–5 case studies
of municipalities <50,000 that completed open-source transitions. Target: v0.3.0.

---

## Improvement log

| Date | Action | By | Result |
|---|---|---|---|
| 2026-06-20 | Initial literature review, v0.1.0 draft | SG | 30 primary sources identified; 46 citation slots in papers |
| 2026-06-21 | Citation verification and gap-fill for v0.2.0 | SG | All 46 sources verified; 9 new source IDs added ([15], [17], [18], [25], [28], [31], [32], [38], [40]); 4 URLs corrected ([6], [9], [16], [43]); economic analysis, civic tech, and accessibility sections new; Appendices A–C added |

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
- [ ] UN E-Government Survey (biannual — next 2024)
- [ ] ZenDiS Jahresbericht (annual — 2024 edition due)
- [ ] Swiss E-ID cantonal adoption map update
- [ ] openCode.de statistics: repo count, most-reused components
- [ ] eCH standards new publications (ech.ch)
