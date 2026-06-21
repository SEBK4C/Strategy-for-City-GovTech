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

| Domain | Depth | Key gaps remaining |
|---|---|---|
| E-government theory (Wirtz/Weyerer, Janowski) | Medium | Post-2022 4th-gen e-gov literature still limited |
| Foundational open government (Lathrop & Ruma 2010) | Medium | Added in v0.2.0 |
| Swiss EMBAG and federal digital strategy | High | Cantonal implementation data still lacking |
| German OZG / OZG 2.0 | High | BundID uptake data now included (v0.2.0) |
| Sovereign Cloud Stack | High | Production metrics for municipalities still limited |
| Open Source in EU public administration | Medium | OSOR 2024 annual report not yet integrated |
| ZenDiS GmbH and OpenDesk | Medium | Added in v0.2.0; annual report not yet available |
| Identity management (Keycloak, BundID, eID) | High | BundID stats now included; eID detailed in v0.2.0 |
| Swiss eID implementation | High | Added in v0.2.0; rollout summer 2026 |
| eCH Standards (Switzerland) | Medium | Added in v0.2.0; specific standards surveyed |
| Decidim / participatory platforms | Medium | Schaffhausen case study not yet a standalone section |
| CONSUL Democracy | Medium | Added in v0.2.0; OSOR case study referenced |
| GovStack (ITU/DIAL) | Medium | Added in v0.2.0; municipality case (Montenegro) included |
| Matrix/Element for government | Medium | BundesMessenger deployment stats still TBC |
| Nextcloud for government | Medium | Swiss federal deployment data confirmed |
| Open data portals (CKAN, opendata.swiss) | Medium | Technical implementation details still limited |
| GIS for municipalities | Low | No peer-reviewed academic literature yet cited |
| Procurement frameworks | Low | No comparative EU procurement studies yet |
| Total cost of ownership studies | Medium | CRITICAL GAP PARTIALLY ADDRESSED in v0.2.0 |
| User experience / satisfaction research | Absent | CRITICAL GAP — still unaddressed |
| Small municipality case studies | Medium | PARTIALLY ADDRESSED in v0.2.0 (eVaka, Cityvizor, Bolzano) |
| Change management in IT transitions | Low | Munich LiMux referenced; no systematic review |
| EU Data Act 2023 | Medium | Added in v0.2.0; Data Governance Act also added |
| EPRS Digital Sovereignty Study 2023 | Medium | Added in v0.2.0 |
| French government open-source migrations | High | Added in v0.2.0 (Gendarmerie, Toulouse) |
| Fraunhofer IESE municipality research | Low | Added in v0.2.0; full report not yet retrieved |

### Not yet covered (v0.3.0 targets)

- **GAIA-X implementation status** — 2025 state of play for public administration
- **Academic post-2022 e-government literature** — 4th-generation digital government, platform government, AI in e-government
- **BundesMessenger adoption statistics** — German federal agencies
- **User experience research** — citizen satisfaction comparative studies
- **Meijer — E-government and democratic legitimacy** (foundational academic)
- **Bertot et al. — Social media in government** (foundational academic)
- **ZenDiS annual report 2024** (when published)
- **OSOR Annual Report 2024** (EU Open Source Observatory)
- **Swiss OGD Strategy 2024–2027** (distinct from E-Government Strategy)
- **CONSUL Democracy Foundation statistics** (current deployment count)
- **GovStack implementation guide for municipalities** (practical toolkit)
- **eCH-0058 specification** (specific delivery interface standard)
- **Accessibility standards** (BITV 2.0, WCAG 2.2, EN 301 549) in depth

---

## Critical gaps

### TCO studies — PARTIALLY ADDRESSED in v0.2.0
French Gendarmerie GendBuntu: 40% TCO reduction, €2M/year licence savings (103,164 workstations by June 2024). Toulouse: €1.8M over 3 years (90% desktops). 11 French ministries on LibreOffice (500,000 workstations). Province of Bolzano-Bozen (Italy) desktop migration documented.

**Remaining gap:** No rigorous independent comparative TCO study covers the full open-source vs. proprietary *municipal administration* stack (including document management, identity, workflow, citizen portal). Available studies focus on desktop/productivity suite only. **Action:** Design municipal-specific TCO methodology for appendix in v1.0.

### User experience research — STILL ABSENT
No peer-reviewed literature on citizen satisfaction with open-source vs. proprietary municipal digital services. **Action:** Design citizen satisfaction survey framework for v1.0 appendix. Partner with Decidim or CONSUL deployments for data collection.

### Small-municipality data — PARTIALLY ADDRESSED in v0.2.0
eVaka (Espoo), Cityvizor (Czech Republic), and Bolzano-Bozen (Italy) cases added. Small-municipality specific track added to implementation roadmap (Section 5.6). **Remaining gap:** Case studies of German Gemeinden <10,000 population. **Action:** Contact Fraunhofer IESE and KoSIT for referrals.

### Post-2022 academic e-government theory — STILL ABSENT
Literature review theory section relies primarily on Wirtz/Weyerer (2017) and Janowski (2015). **Action:** Systematic search for GIQ, ISM, EJEG publications 2022–2026 in next quarterly review.

---

## Improvement log

| Date | Action | By | Result |
|---|---|---|---|
| 2026-06-20 | Initial literature review, v0.1.0 draft | SG | 30 primary sources; 46 citation slots in papers |
| 2026-06-21 | Quarterly update cycle (Q1), v0.2.0 | AI research loop | 16 new sources added (47–62); TCO gaps partially addressed; eCH, CONSUL, GovStack, ZenDiS, Swiss eID, EU Data Act, EPRS covered; source registry updated to 62 entries |

---

## Quarterly review checklist

When running `Scripts/update_literature_review.py`, check for:

- [ ] New Swiss e-government legislation or strategy updates
- [ ] Swiss eID rollout status (target: summer 2026)
- [ ] New German OZG implementation reports or FITKO publications
- [ ] ZenDiS annual report (when published)
- [ ] New EU legislation (AI Act implementations, Data Spaces, etc.)
- [ ] New Sovereign Cloud Stack releases or governance updates
- [ ] New openCode.de statistics or case studies
- [ ] New academic papers on e-government maturity (GIQ, ISM, EJEG) — post-2022 focus
- [ ] OSOR Annual Report (EU Open Source Observatory, annual)
- [ ] UN E-Government Survey (biannual; next: 2024)
- [ ] New municipal open-source deployments or case studies — focus on <50,000 population
- [ ] New security advisories affecting stack components (Keycloak, Nextcloud, Matrix)
- [ ] GovStack specification updates and municipal implementation guides
- [ ] EU Data Act implementing acts and municipal compliance guidance
- [ ] CONSUL Democracy Foundation annual community statistics
- [ ] BundesMessenger adoption data (federal agencies + Länder)
- [ ] New security frameworks (BSI updates, ENISA publications)
- [ ] User experience / citizen satisfaction research (any new publications)

## Version history

| Version | Date | Summary |
|---|---|---|
| 0.1.0 | 2026-06-20 | Initial state; 46 source registry entries; critical gaps identified |
| 0.2.0 | 2026-06-21 | 62 source registry entries; TCO, ZenDiS, eCH, CONSUL, GovStack, Swiss eID, EU Data Acts added; small-municipality cases added; 4 critical gaps remain |
