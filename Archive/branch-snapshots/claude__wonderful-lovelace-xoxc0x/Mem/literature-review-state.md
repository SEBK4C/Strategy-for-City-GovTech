# Literature Review State — City GovTech Strategy

**Version:** 0.2.0  
**Last reviewed:** 2026-06-21  
**Next review due:** 2026-09-21 (quarterly cadence)  

This document tracks the current state of the literature review: what is covered, what is missing, and what needs updating. It is the primary input to `Scripts/update_literature_review.py`.

---

## Coverage map

### Covered (v0.2.0)

| Domain | Depth | Key gaps remaining |
|---|---|---|
| E-government theory (Wirtz/Weyerer, Janowski, Lathrop/Ruma) | High | No post-2022 fourth-gen e-gov empirical studies |
| Swiss EMBAG and federal digital strategy | High | Cantonal EMBAG implementation data not yet public |
| German OZG 2.0 | High | Municipal uptake statistics (municipalities <50k) missing |
| Sovereign Cloud Stack | High | Production metrics and uptime data not yet published |
| Open Source in EU public administration | High | OSOR 2024 annual report not yet integrated |
| Identity management (Keycloak, BundID, Swiss eID) | High | BundID uptake statistics missing; EUDI Wallet pilots |  
| Decidim / participatory platforms | High | Schaffhausen longitudinal outcome data |
| Matrix/Element for government | High | BundesMessenger adoption statistics |
| Nextcloud for government | High | Swiss federal deployment performance data |
| Open data portals (CKAN) | High | opendata.swiss dataset quality metrics |
| GIS for municipalities | Medium | No academic literature; practitioner sources only |
| Procurement frameworks | Medium | No comparative EU procurement studies |
| ZenDiS and OpenDesk | High | OpenDesk v2.x rollout (2025) details |
| eCH standards suite | High | eCH-0200 (OGD metadata) implementation data |
| GovStack building blocks | Medium | EU application cases thin |
| GAIA-X and data spaces | Medium | Urban data space implementations nascent |
| EU AI Act municipal implications | Medium | No implementation studies (Act too recent) |
| Case studies (Barcelona, Helsinki, Schaffhausen, OpenDesk, LiMux) | High | Helsinki longitudinal data post-2023 |
| Total cost of ownership | Medium | CRITICAL: Model is indicative; needs empirical validation |
| User experience / satisfaction research | Low | Almost no peer-reviewed literature |
| Small municipality case studies (<50k) | Low | CRITICAL GAP |
| Change management in IT transitions | Medium | Munich referenced; broader literature thin |
| CONSUL Democracy platform | Low | Added to registry; not yet integrated in paper |

### Not yet covered

- **OSOR Annual Report 2024** (EU Open Source Observatory)
- **Swiss OGD Strategy 2024–2027** (separate from E-Gov Strategy)
- **GAIA-X Credential certification list** (2025 state)
- **OpenDesk v2.x** release notes and rollout data
- **AI Act municipal conformity assessment frameworks** (emerging)
- **EU Web Accessibility Directive** / German BFSG implementation
- **OAIS standard** for digital preservation / long-term archiving
- **Swiss ISDS framework** (Informationssicherheit des Bundes)
- **DCAT-AP 3.0** (latest version, published 2023)
- **GovStack EU application cases** (beyond generic documentation)

---

## Critical gaps

### TCO studies
The TCO figures in Section 8 are indicative estimates calibrated against published procurement data but are not independently audited. No rigorous independent comparative TCO study covering a full open-source vs. proprietary municipal stack with longitudinal data exists. **Action:** identify municipalities willing to share actual cost data; design a cost-reporting template. Target: v0.3.0.

### Small-municipality data
Most case studies involve large cities or federal agencies. The median EU municipality has population <10,000. **Action:** document 3–5 case studies of municipalities <50,000 that completed open-source transitions. Target: v0.3.0.

### User experience research
Almost no peer-reviewed literature on citizen satisfaction with open-source vs. proprietary municipal digital services. **Action:** design a citizen-satisfaction survey framework for participating municipalities. Target: v1.0 appendix.

### AI Act implementation
No published studies on municipal AI Act conformity assessment programmes (too recent). **Action:** monitor ENISA and national supervisory authority publications; add to v0.3.0 review cycle.

---

## Improvement log

| Date | Action | By | Result |
|---|---|---|---|
| 2026-06-20 | Initial literature review, v0.1.0 draft | SG | 30 primary sources; 46 citation slots |
| 2026-06-21 | Expanded to v0.2.0: eCH, GovStack, GAIA-X, AI Act, case studies, TCO | SG | 64 registry entries; all v0.2.0 citations verified |

---

## Quarterly review checklist

When running `Scripts/update_literature_review.py`, check:

- [ ] New Swiss e-government legislation or strategy updates (fedlex.admin.ch)
- [ ] New German OZG implementation reports (fitko.de, bmi.bund.de)
- [ ] New EU legislation affecting municipal IT (EUR-Lex alerts)
- [ ] New Sovereign Cloud Stack releases (scs.community/blog)
- [ ] New openCode.de statistics or case studies
- [ ] New ZenDiS publications (zendis.de)
- [ ] New academic papers on e-government maturity (GIQ, ISM, EJEG — Google Scholar alerts)
- [ ] New municipal open-source deployments or case studies (joinup.ec.europa.eu)
- [ ] New security advisories affecting stack components (BSI, NCSC-CH, ENISA)
- [ ] OSOR annual report (EU Open Source Observatory, annual)
- [ ] UN E-Government Survey (biannual — next: 2024)
- [ ] GAIA-X Trust Framework updates
- [ ] EU AI Act implementation milestones and ENISA guidance
- [ ] GovStack building blocks catalogue updates
