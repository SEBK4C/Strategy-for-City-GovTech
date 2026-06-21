# Literature Review State — City GovTech Strategy

**Version:** 0.2.0  
**Last reviewed:** 2026-06-21  
**Next review due:** 2026-09-21 (quarterly cadence)  

This document tracks the current state of the literature review. It is the primary input to `Scripts/update_literature_review.py`.

---

## Coverage map

### Covered (v0.2.0)

| Domain | Depth | Key gaps |
|---|---|---|
| E-government theory (Wirtz/Weyerer, Janowski, Lathrop/Ruma) | High | No post-2022 4th-gen literature |
| Swiss EMBAG and federal digital strategy | High | Cantonal implementation metrics pending |
| German OZG / OZG 2.0 | High | EfA uptake statistics (2025) |
| Sovereign Cloud Stack | High | Production performance metrics |
| Open Source in EU public administration | High | OSOR 2024 report not yet published |
| Identity management (Keycloak, BundID, BGEID, eIDAS-2) | High | BGEID integration patterns (pre-launch) |
| Decidim / participatory platforms | High | Schaffhausen case study depth limited |
| CONSUL Democracy | Medium | EU deployments data sparse |
| GovStack building blocks | Medium | Reference implementations status |
| Matrix/Element for government | Medium | BundesMessenger adoption statistics |
| Nextcloud for government | High | Swiss federal deployment metrics |
| Open data portals (CKAN, opendata.swiss) | High | Lausanne deployment details |
| GIS for municipalities | Medium | Academic literature still thin |
| Procurement frameworks (DE + CH) | High | Small municipality procurement patterns |
| Total cost of ownership | Medium | Framework added (§4.11); empirical data sparse |
| ZenDiS and OpenDesk | High | v2.x roadmap details |
| eCH Standards | High | Individual standard details (eCH-0160 etc.) |
| EU Data Act implications | Medium | Municipal implementation guidance lacking |
| EU AI Act in public admin | Medium | High-risk classification mapping needed |
| Change management in IT transitions | Medium | Munich LiMux covered; wider cases needed |
| Small municipality case studies | Medium | Added 5 cases (§3.7); more needed |
| User experience / satisfaction research | Low | CRITICAL GAP — see below |

### Not yet covered

- **KGSt GovTech reports** — German municipal management consultancy
- **Fraunhofer FOKUS** open-source public-sector research
- **EU eIDAS-2 Wallet** implementation details (2025)
- **GAIA-X implementation status** (2025 detailed progress)
- **GovStack sandbox reference implementations** (deployment case studies)
- **Nextcloud Hub 9+ features** (2025–2026 release cycles)
- **Swiss Municipal Association (SGV/UCV)** digitalisation guidance
- **OpenProject 14+** features for public admin
- **Decidim 0.28+** major feature additions

---

## Critical gaps (carry-forward to v0.3.0)

### TCO empirical data
The framework in §4.11 provides a structured model; independent verified cost data for full open-source municipal stacks remains sparse. The French Gendarmerie LibreOffice migration (€2M/year saving, 70,000 seats) is the best available large-scale comparator. **Action for v0.3.0:** identify or request published TCO reports from 3–5 EfA-participating municipalities.

### User experience research
Almost no peer-reviewed literature exists on citizen satisfaction with open-source vs. proprietary municipal digital services. **Action for v0.3.0:** design a survey framework; contact Decidim Association and openCode.de for community data.

### eIDAS-2 / BGEID integration
The Swiss BGEID enters service in 2026; eIDAS-2 wallets are in pilot across EU member states. Keycloak integration patterns are emerging but not yet documented in peer-reviewed literature. **Action for v0.3.0:** monitor BGEID technical specifications once published; update §4.1.

---

## Improvement log

| Date | Action | By | Result |
|---|---|---|---|
| 2026-06-20 | Initial literature review, v0.1.0 | SG | 30 primary sources; full scientific structure |
| 2026-06-21 | v0.2.0 citation-complete update | SG/AI | 58 sources total; 4 unverified resolved; 12 new sources; §3.7, §4.11, §7.4 added |

---

## Quarterly review checklist

When running `Scripts/update_literature_review.py`, check for:

- [ ] New Swiss e-government legislation or strategy updates
- [ ] New German OZG implementation reports or FITKO publications
- [ ] New EU legislation (AI Act implementation guidance, Data Act delegated acts)
- [ ] New Sovereign Cloud Stack releases or governance updates
- [ ] New openCode.de statistics or EfA service counts
- [ ] New OSOR annual report (European Commission, annual)
- [ ] New ZenDiS annual report or OpenDesk release notes
- [ ] New GovStack reference implementations
- [ ] New academic papers on e-government maturity (GIQ, ISM, EJEG)
- [ ] New municipal open-source deployments or case studies
- [ ] New BGEID / eIDAS-2 technical specifications
- [ ] New security advisories affecting stack components
- [ ] UN E-Government Survey (biannual)
- [ ] KGSt GovTech publications
- [ ] Fraunhofer FOKUS open-source public-sector research
