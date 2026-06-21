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
| E-government theory (Wirtz/Weyerer, Janowski, Scholl) | High | No post-2023 peer-reviewed work on 4th-gen e-gov |
| Swiss EMBAG and federal digital strategy | High | Cantonal implementation statistics still lacking |
| German OZG / OZG 2.0 | High | FITKO production data verified; municipal uptake statistics still limited |
| Sovereign Cloud Stack | High | SCS production load metrics not publicly available |
| Open Source in EU public administration | High | OSOR 2023 integrated; OSOR 2024 not yet published |
| Identity management (Keycloak, BundID, Swiss E-ID) | High | Swiss E-ID production data not yet available (goes live 2026) |
| Decidim / participatory platforms | High | Schaffhausen case study added; Helsinki and Barcelona documented |
| Matrix/Element for government | Medium | BundesMessenger user statistics not published |
| Nextcloud for government | High | Swiss federal deployment confirmed |
| Open data portals (CKAN) | High | DCAT-AP.de v2.0 and OGD-CH profiles documented |
| GIS for municipalities | Medium | swisstopo and BKG open data added; no academic literature |
| Procurement frameworks | High | GWB/VgV, BöB/IVöB, EU Directive 2014/24 added |
| Total cost of ownership | Medium | TCO model built (Section 4.11); no independent academic study yet |
| eCH standards | High | Framework documented; individual standard details need expansion |
| GovStack | High | Building blocks framework documented |
| ZenDiS | High | 2024 Annual Report integrated |
| EU Data Act 2023 | High | Regulatory implications documented |
| GAIA-X | Medium | Architecture v2024 documented; sector data spaces need deeper analysis |
| CONSUL Democracy | Medium | Platform documented; limited deployment data outside Spain |
| User experience / satisfaction research | Absent | CRITICAL GAP — see below |
| Small municipality case studies | Medium | 3 small-municipality cases added (Bühl, Kirchheim, Aarau); need 2 more |
| Change management in IT transitions | Medium | Munich LiMux analysis improved; Scholl reference added |
| AI Act implications | Low | §7.4 added; needs deeper technical analysis |

### Not yet covered

- **AKDB** (Anstalt für Kommunale Datenverarbeitung in Bayern) — Bavarian municipal IT; key actor under-documented
- **OneGov GEVER** (open-source Swiss GEVER from Kanton Schaffhausen)
- **Swiss OGD Strategy 2024–2027** (Bundesrat strategy document)
- **Collabora Online** (document editing component in OpenDesk)
- **Flowable** (alternative to Camunda, no dual-licensing)
- **MapLibre GL** (open-source vector tile rendering)
- **Swisstopo open data** (Federal Office of Topography open data programme)
- **EU AI Act (Regulation (EU) 2024/1689)** — needs full regulatory citation and detailed analysis
- **GovStack Country Engagement Framework** — practical implementation methodology
- **Digital Services Act / Digital Markets Act** — interaction with municipal procurement

---

## Critical gaps

### User experience research (CRITICAL — unresolved)
Almost no peer-reviewed literature exists on citizen satisfaction with open-source vs.
proprietary municipal digital services. The Almeida et al. (2023) study [59] provides
correlational evidence but not causal data on satisfaction differences.  
**Action:** Design a citizen-satisfaction survey framework usable by participating
municipalities. Target: v1.0 appendix.

### TCO — independent academic validation (PARTIALLY ADDRESSED)
The v0.2.0 TCO model (Section 4.11) is built from vendor documentation and grey
literature. No independent peer-reviewed study has validated the specific cost ranges
for German/Swiss municipal contexts.  
**Action:** Identify or commission an independent municipal TCO methodology. Contact
FITKO, OSBA, and Swiss OGD programme for unpublished data. Target: v0.3.0.

### Small-municipality data (PARTIALLY ADDRESSED)
Three small-municipality case studies added (Bühl, Kirchheim, Aarau). The median German
Gemeinde has population <3,000 — below even the smallest documented case.  
**Action:** Document 2–5 additional case studies of municipalities <20,000 that completed
open-source transitions. Target: v0.3.0.

---

## Improvement log

| Date | Action | By | Result |
|---|---|---|---|
| 2026-06-20 | Initial literature review, v0.1.0 draft | SG | 30 primary sources identified; 46 citation slots |
| 2026-06-21 | v0.2.0 review: fill gaps, add sources, verify citations | SG/AI | 14 new sources [47]–[60]; 4 unverified entries resolved; TCO analysis added; 6 case studies added |

---

## Quarterly review checklist

When running `Scripts/update_literature_review.py`, check for:

- [ ] New Swiss e-government legislation or strategy updates (fedlex.admin.ch)
- [ ] New German OZG implementation reports (fitko.de/veroeffentlichungen)
- [ ] New EU legislation: EU AI Act guidance from EU AI Office; Data Act implementation acts
- [ ] New Sovereign Cloud Stack releases and certified operator list updates (scs.community)
- [ ] New openCode.de statistics and featured projects (opencode.de)
- [ ] New academic papers on e-government maturity (GIQ, ISM, EJEG — Google Scholar alert)
- [ ] New municipal open-source deployments (OSOR case studies, openCode.de)
- [ ] ZenDiS publications and OpenDesk version updates (zendis.de)
- [ ] Swiss E-ID production deployment status (expected 2026)
- [ ] New eCH standard publications (ech.ch)
- [ ] New GovStack building block specifications (govstack.global)
- [ ] New security advisories: BSI advisories for stack components; NIS2 implementing acts
- [ ] OSOR annual report (EU Open Source Observatory, annual, usually Q2)
- [ ] UN E-Government Survey (biannual; next: 2024)
- [ ] New small-municipality case studies (<20,000 population)
- [ ] AKDB and Dataport annual reports
- [ ] GAIA-X data space progress reports

## v0.3.0 milestone targets

- [ ] Independent TCO validation or contact with FITKO/OSBA
- [ ] 2 additional small-municipality case studies
- [ ] Swiss OGD Strategy 2024–2027 integrated
- [ ] AKDB documented as key actor
- [ ] OneGov GEVER documented
- [ ] EU AI Act full citation and detailed analysis
- [ ] Citizen satisfaction survey framework (Appendix A draft)
- [ ] OSOR 2024 Annual Report integrated (if published)
