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

| Domain | Depth | Remaining gaps |
|---|---|---|
| E-government theory (Wirtz/Weyerer, Janowski, Lathrop/Ruma) | Medium–High | No post-2022 literature on 4th-gen e-gov |
| Swiss EMBAG and federal digital strategy | High | Cantonal implementation data partial |
| German OZG / OZG 2.0 | High | Municipal uptake statistics missing |
| Sovereign Cloud Stack | High | Production metrics from Gemeinden not yet available |
| Open Source in EU public administration | High | OSOR 2024 annual report pending |
| Identity management (Keycloak, BundID, eID) | Medium | BundID uptake data missing |
| Decidim / participatory platforms | High | Schaffhausen case study documented |
| CONSUL Democracy | Medium | Added; no DACH-specific deployment data |
| Matrix/Element for government | Medium | BundesMessenger adoption data needed |
| Nextcloud for government | High | Swiss federal deployment details partial |
| Open data portals (CKAN) | High | DCAT-AP CH implementation details |
| GIS for municipalities | Low–Medium | No academic literature cited |
| Procurement frameworks | Medium | ZenDiS templates not yet linked |
| Total cost of ownership studies | Medium | v0.2.0 adds evidence base; longitudinal studies still absent |
| Small municipality case studies | Medium | 3 cases documented (Wollerau, Rangsdorf, Schaffhausen) |
| Change management in IT transitions | Low–Medium | Munich LiMux deeper analysis pending |
| ZenDiS | High | Annual report analysis not yet integrated |
| GovStack | Medium | Building-block mapping complete; implementation pilots not cited |
| eCH standards | High | Core standards (0044, 0011, 0010, 0007, 0147, 0014) covered |
| EU Data Act 2023 | High | Municipal implications covered; implementation guidance pending |
| Swiss OGD Strategy 2024–2027 | Medium | Cited; detailed analysis pending |
| GAIA-X | Medium | Architecture cited; deployment status 2025/2026 partial |
| User experience / satisfaction research | Absent | CRITICAL GAP — see below |

### Not yet covered (v0.3.0 targets)

- **Post-2022 fourth-generation e-government literature** (academic publication cycle lags 3–5 years)
- **Digital Services Act / Digital Markets Act** — interaction with municipal procurement
- **OpenDesk v2.x** (2025/2026 feature updates)
- **AI augmentation** of open-source municipal stacks (emerging; no rigorous evaluations)
- **EU AI Act implementation** — implications for automated municipal decision-making
- **SPDX / CycloneDX SBOM tooling** — practical guide for municipalities
- **Flowable** — deeper evaluation as Camunda alternative
- **BundesMessenger adoption data** (Matrix/Element)

---

## Critical gaps

### User experience research
Almost no peer-reviewed literature exists on citizen satisfaction with open-source vs.
proprietary municipal digital services. **Action:** design a citizen-satisfaction survey
framework usable by participating municipalities. Target: v1.0 appendix.

### Longitudinal TCO studies
The evidence base improved substantially in v0.2.0 (French LibreOffice, German Nextcloud,
Munich LiMux figures). However, no rigorous independent 10-year lifecycle studies exist.
**Action:** identify or commission a municipal TCO longitudinal study methodology. Target: v0.3.0.

### AI augmentation
AI-assisted document classification, service request routing, and data quality checking
for open-source municipal stacks is rapidly emerging but lacks rigorous evaluations.
**Action:** monitor and add to v0.3.0 literature review.

---

## Improvement log

| Date | Version | Action | By | Result |
|---|---|---|---|---|
| 2026-06-20 | 0.1.0 | Initial literature review | SG | 30 primary sources; 46 citation slots in papers |
| 2026-06-21 | 0.2.0 | Citation-complete expansion | SG | Added sections 3.6–3.11 (ZenDiS, GovStack, eCH, EU Data Act, TCO evidence, small-municipality cases). 9 new sources (refs 47–55). Verified 4 previously unverified entries ([6], [9], [16], [43]). 55 total sources. |

---

## Quarterly review checklist

When running `Scripts/update_literature_review.py`, check for:

- [ ] New Swiss e-government legislation or eCH standards updates
- [ ] New German OZG implementation reports or FITKO publications
- [ ] ZenDiS annual report update [49]
- [ ] New EU legislation (Data Act implementation, AI Act, DSA/DMA)
- [ ] New Interoperable Europe Act implementation guidance
- [ ] New Sovereign Cloud Stack releases or governance updates
- [ ] New openCode.de statistics or case studies
- [ ] Nextcloud, Decidim, Matrix, CKAN, Camunda, TYPO3 major releases
- [ ] New security advisories affecting stack components (BSI CERT-Bund, NCSC-CH)
- [ ] New SBOM tooling or standards updates (SPDX, CycloneDX)
- [ ] New academic papers on e-government maturity (GIQ, ISM, EJEG)
- [ ] New municipal open-source deployments or case studies
- [ ] OSOR annual report (EU Open Source Observatory, annual) [50]
- [ ] UN E-Government Survey (biannual — next: 2024) [29]
- [ ] govdigital eG annual report [23]
- [ ] Verify any source registry entries marked “unverified”
- [ ] Update dead URLs in source registry
- [ ] Check for new versions of cited documents
- [ ] Cross-check TCO figures against new published data
