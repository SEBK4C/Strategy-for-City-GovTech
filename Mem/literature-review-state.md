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

| Domain | Depth | Status | Key remaining gaps |
|---|---|---|---|
| E-government theory (Wirtz/Weyerer, Janowski) | Medium | stable | No post-2022 literature on 4th-gen e-gov |
| Open government foundations (Lathrop & Ruma) | Medium | added v0.2.0 | |
| Swiss EMBAG and federal digital strategy | High | stable | |
| Swiss E-Government Strategy 2024–2027 | High | added v0.2.0 | |
| eCH standards (Swiss interoperability) | Medium | added v0.2.0 | |
| German OZG / OZG 2.0 | High | stable | Municipal uptake statistics missing |
| Sovereign Cloud Stack | High | stable | |
| Open Source in EU public administration (OSOR) | High | added v0.2.0 | |
| Identity management (Keycloak, BundID, eID) | Medium | stable | BundID uptake statistics |
| Decidim / participatory platforms | High | expanded v0.2.0 | |
| CONSUL Democracy | Medium | added v0.2.0 | |
| Matrix/Element for government (BundesMessenger) | High | expanded v0.2.0 | |
| Nextcloud for government | Medium | stable | |
| Open data portals (CKAN, opendata.swiss) | Medium | stable | |
| GIS for municipalities (QGIS, OSM, GeoServer) | Medium | stable | No academic literature |
| Accessibility (BITV 2.0, EN 301 549, WCAG 2.1) | High | added v0.2.0 | Swiss P028 needs deeper coverage |
| AI tools in government (Ollama, Whisper, EU AI Act) | High | added v0.2.0 | |
| GovStack (ITU/DIAL building blocks) | Medium | added v0.2.0 | |
| Procurement frameworks (German Vergaberecht, Swiss BöB) | High | expanded v0.2.0 | No comparative EU procurement studies |
| EU Interoperable Europe Act | High | verified+expanded v0.2.0 | |
| EU Data Act 2023 | Medium | added v0.2.0 | |
| EU AI Act 2024 | High | added v0.2.0 | |
| NIS2 Cybersecurity Directive | Medium | stable | |
| BSI IT-Grundschutz | Medium | stable | |
| XÖV (German XML standards) | Medium | stable | |
| Gaia-X | Low | added v0.2.0 | Needs deeper 2024/2025 state-of-play |
| ZenDiS and German digital sovereignty policy | High | added v0.2.0 | |
| OpenDesk | High | stable | |
| Case study: Barcelona (Decidim) | High | added v0.2.0 | |
| Case study: German federal OpenDesk | High | added v0.2.0 | |
| Case study: Canton Schaffhausen (Decidim) | Medium | added v0.2.0 | Needs primary source |
| Case study: Schleswig-Holstein (Linux) | High | added v0.2.0 | |
| Case study: Moers (Ubuntu 2001–) | High | added v0.2.0 | |
| Case study: Munich LiMux (post-mortem) | High | added v0.2.0 | |
| Total cost of ownership | Low | partial v0.2.0 | CRITICAL GAP — no rigorous independent study |
| User experience / citizen satisfaction | Absent | not addressed | CRITICAL GAP |
| Small municipality pathway | High | added v0.2.0 | More case studies needed |
| Change management in IT transitions | Medium | expanded v0.2.0 | |

### Not yet covered (targets for v0.3.0 / v1.0.0)

- **DCAT-AP 3.0** — updated EU metadata standard for open data portals (2023)
- **Swiss OGD Strategy 2024–2027** — open government data cantonal implementation
- **Digital Services Act / Digital Markets Act** — interaction with municipal procurement
- **OpenDesk v2.x (2025/2026 updates)** — post-v0.2.0 OpenDesk releases
- **Gaia-X 2024/2025 state of play** — current implementation status
- **EU NIS2 national transpositions** — how individual member states transposed NIS2
- **XÖV 2024 updates** — new standard families (XJustiz, XBau)
- **Swiss eID implementation** — post-2021 referendum public-sector integration
- **Peer-reviewed TCO study** — needs commissioning or identification
- **Citizen satisfaction research** — survey framework needed
- **CONSUL vs Decidim comparative analysis** — systematic comparison missing
- **FOSS4G conference proceedings** — academic open-source GIS literature
- **CKAN 2.10/3.0 technical updates** — API v3, DCAT-AP 3.0 integration

---

## Critical gaps

### TCO studies (remains critical, partially addressed)
No rigorous independent comparative Total Cost of Ownership studies cover the full
open-source vs. proprietary municipal stack. v0.2.0 added KGSt benchmarking data [61]
and Schleswig-Holstein savings projection [54], but no peer-reviewed comparative study
exists. **Action:** identify or commission an independent municipal TCO methodology.
Target: v1.0.0 appendix.

### User experience research (remains critical, not addressed)
Almost no peer-reviewed literature exists on citizen satisfaction with open-source vs.
proprietary municipal digital services. **Action:** design a citizen-satisfaction survey
framework usable by participating municipalities. Target: v1.0.0 appendix.

### Canton Schaffhausen primary source
The Schaffhausen Decidim deployment (Case Study 5.3) is referenced but no primary
source document (cantonal press release, procurement record, or technical report) was
identified. **Action:** locate BAR-indexed or cantonal publication. Target: v0.3.0.

---

## Gaps addressed in v0.2.0

| Gap from v0.1.0 | How addressed | Sources |
|---|---|---|
| eCH standards missing | Added full eCH section 4.x; source [47] | [47] |
| CONSUL not covered | Added CONSUL to participation layer comparison | [48] |
| GovStack not covered | Added GovStack mapping in Section 4 intro | [49] |
| EU Data Act missing | Added Data Act to Section 3 (regulatory landscape) | [50] |
| ZenDiS under-covered | Added ZenDiS as key actor throughout | [51] |
| OSOR not integrated | Added OSOR statistics to Section 2 | [52] |
| Lathrop & Ruma missing | Added to Section 1 introduction | [53] |
| Small-municipality case studies critical gap | Added Moers (5.5), small pathway (6.2), Appendix A | [54][62] |
| LiMux post-mortem shallow | Expanded to full case study (5.6) with 4 failure causes | [55] |
| Barcelona not documented | Full case study (5.1) with metrics | [56] |
| EU AI Act missing | Added AI Act to Section 3; Section 4.11 AI tools | [57] |
| Accessibility absent | Added full Section 4.10 with BITV 2.0, EN 301 549 | [58] |
| Gaia-X state of play | Added Gaia-X to Section 3/4 context | [59] |
| BundesMessenger data | Added BundesMessenger reference in Matrix section | [60] |
| Municipal benchmarking | Added KGSt data to TCO analysis | [61] |
| Source verification [6][9][16][43] | All four verified with confirmed URLs/CELEX | confirmed |

---

## Improvement log

| Date | Version | Action | By | Result |
|---|---|---|---|---|
| 2026-06-20 | 0.1.0 | Initial literature review | SG | 30 primary sources; 46 citation slots; 4 unverified |
| 2026-06-21 | 0.2.0 | Major expansion | SG/AI | +16 sources ([47]–[62]); 4 previously unverified verified; all 62 sources verified; Case Studies section added; Accessibility layer added; AI Tools layer added; EU Data Act and EU AI Act added; small-municipality pathway; procurement language templates |

---

## Quarterly review checklist

When running `Scripts/update_literature_review.py`, check for:

### Legislation and policy
- [ ] New Swiss e-government legislation or strategy updates
- [ ] New German OZG implementation reports or FITKO publications
- [ ] New EU legislation (AI Act implementing acts, Data Act delegated acts)
- [ ] NIS2 national transposition updates
- [ ] EMBAG cantonal-level implementation regulations
- [ ] Swiss eID public-sector integration progress

### Technology updates
- [ ] New Sovereign Cloud Stack releases or governance updates
- [ ] OpenDesk new versions (quarterly releases)
- [ ] Decidim major releases and new deployment announcements
- [ ] Keycloak security advisories or major version changes
- [ ] CKAN 2.10/3.0 release and DCAT-AP 3.0 integration
- [ ] Ollama/Llama model updates relevant to public-sector use

### Case studies and data
- [ ] New openCode.de statistics or repository count
- [ ] OSOR annual report (EU Open Source Observatory, annual)
- [ ] UN E-Government Survey (biannual — next: 2024)
- [ ] KGSt benchmarking reports on municipal digitisation
- [ ] New case studies: municipalities <50,000 completing open-source transitions
- [ ] Schleswig-Holstein migration progress reports
- [ ] Canton Schaffhausen Decidim primary source

### Academic literature
- [ ] New papers in Government Information Quarterly (GIQ)
- [ ] New papers in Information Systems Management (ISM)
- [ ] New papers in European Journal of ePractice (EJEG)
- [ ] FOSS4G proceedings for open-source GIS literature
- [ ] EGOV/ePart conference proceedings

### Security
- [ ] New security advisories affecting any stack component
- [ ] BSI IT-Grundschutz annual update (Edition 2024/2025)
- [ ] ENISA threat landscape report updates

---

## Source statistics

| Version | Sources | Verified | Unverified | Domains covered |
|---|---|---|---|---|
| 0.1.0 | 46 | 42 | 4 | 16 |
| 0.2.0 | 62 | 62 | 0 | 29 |
