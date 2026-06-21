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
| E-government theory (Wirtz/Weyerer, Janowski, Lathrop/Ruma) | High | Post-2024 literature on 4th-gen e-gov AI governance |
| Swiss EMBAG and federal digital strategy | High | Municipal implementation data from specific cantons |
| Swiss eCH standards | Medium | Deep technical analysis of eCH-0058 for system integration |
| Swiss E-ID (new SSI model) | Medium | Practical deployment data (system launched 2025) |
| German OZG / OZG 2.0 | High | Municipal uptake statistics (% services live) |
| German ZenDiS and OpenDesk | Medium | Municipal adoption numbers, version 2.x specifics |
| Sovereign Cloud Stack | High | SCS-certified hoster comparison (pricing, SLAs) |
| Open Source in EU public administration | High | OSOR 2024 report (2023 is latest integrated) |
| EU Interoperable Europe Act | High | Implementing acts and delegated legislation |
| EU Data Act | Medium | Municipal smart-city application guidance |
| EU AI Act | Medium | Municipal AI Act implementation guidance (few examples) |
| EU Cyber Resilience Act | Low | Practical compliance guidance for open-source procurement |
| Identity management (Keycloak, BundID, Swiss eID) | High | BundID uptake data (citizen registration rates) |
| Decidim / participatory platforms | High | Schaffhausen canton detailed case study |
| CONSUL Democracy | Low | European municipal deployment statistics |
| Matrix/Element for government | Medium | BundesMessenger deployment statistics (agencies, users) |
| Nextcloud for government | High | Swiss federal deployment technical details |
| Open data portals (CKAN) | High | DCAT-AP.ch (Swiss DCAT-AP profile) specifics |
| Office productivity (LibreOffice/Collabora) | High | German municipal deployment statistics beyond BVA |
| GIS for municipalities | Medium | Swiss swisstopo open data integration specifics |
| Procurement frameworks (Swiss BöB, German GWB/UVgO) | High | Below-threshold UVgO small-municipality specifics |
| Total cost of ownership studies | Medium | Independent (non-vendor) 10-year municipal TCO study |
| Implementation case studies | High | More small-municipality (<20,000) case studies needed |
| Change management in IT transitions | Medium | Quantitative data on training impact on adoption rates |
| AI in open-source government | Low | CRITICAL GAP — see below |
| GovStack (ITU/DIAL) | Low | Integration with Swiss/German implementations |

### Not yet covered

- **EU Digital Identity Wallet (EUDIW)** — interaction between ARF and Swiss eID/BundID
- **GAIA-X 2026 state** — practical municipal tools vs. policy framework
- **Swiss OGD Strategy 2024–2027** — separate from E-Government Strategy
- **ZenDiS Open-Source-Beschaffungs-Leitfaden** (procurement guide) — detailed analysis
- **Collabora Online CODE** — separate technical documentation entry
- **Local LLM infrastructure** (Ollama, AnythingLLM, OpenWebUI) — technical docs
- **Academic literature on AI fairness in public administration** — for AI Act context
- **Digital Services Act** — interaction with municipal website obligations
- **OpenProject case studies** — specific government project management deployments
- **AKDB specific services** — BayernPortal, OZG services, e-Akte architecture

---

## Critical gaps

### AI governance in municipal open-source contexts
Almost no empirical literature exists on municipal deployment of open-source AI systems
under the EU AI Act framework. The Act is new (applicable from 2025–2027 in phases);
municipal guidance is still being developed by national competent authorities.
**Action:** Monitor BMUV/BMI AI guidance for municipalities; integrate when published.
Target: v0.3.0.

### Independent TCO studies (10-year horizon)
The Paris (5-year) and Gendarmerie (6-year) case studies remain the best available.
No independent 10-year longitudinal TCO study exists for a municipal full-stack
open-source transition.
**Action:** Design and publish a replicable municipal TCO methodology as a working paper.
Target: v1.0 appendix.

### Small-municipality case studies (<20,000 population)
Most case studies involve large cities or federal agencies. The cooperative model
(AKDB, Dataport, TIT) may not translate to very small municipalities.
**Action:** Document 3–5 case studies of municipalities <20,000 that completed
open-source transitions through cooperative IT structures. Target: v0.3.0.

### User experience / citizen satisfaction research
Peer-reviewed literature on citizen satisfaction with open-source vs. proprietary
municipal digital services is almost entirely absent.
**Action:** Design a citizen-satisfaction survey framework for participating municipalities.
Target: v1.0 appendix.

---

## Improvement log

| Date | Action | By | Result |
|---|---|---|---|
| 2026-06-20 | Initial literature review, v0.1.0 draft | SG | 30 primary sources identified; 46 citation slots in papers |
| 2026-06-21 | Major expansion to v0.2.0 | SG | 52 sources in registry; all unverified resolved; added: EU Data Act [28], EU AI Act [49], CRA [48], eCH [15], Swiss E-ID [40], ZenDiS [25], CONSUL [17], GovStack [18], Lathrop/Ruma [32], OSOR [38], Gendarmerie [31], LibreOffice [47], Paris migration [51], BVA [52] |

---

## Quarterly review checklist

When running `Scripts/update_literature_review.py`, check for:

- [ ] New Swiss e-government legislation or strategy updates (Fedlex, egovernment.ch)
- [ ] New German OZG implementation reports or FITKO publications
- [ ] New EU legislation or implementing acts (Data Act delegated acts, AI Act guidance)
- [ ] New Sovereign Cloud Stack releases or governance updates (scs.community)
- [ ] New openCode.de statistics or case studies
- [ ] New academic papers on e-government maturity (GIQ, ISM, EJEG, Information Polity)
- [ ] New municipal open-source deployments or case studies (OSOR, openCode.de)
- [ ] New security advisories affecting stack components (BSI, CERT-Bund)
- [ ] OSOR annual report (EU Open Source Observatory, annual, usually Q1)
- [ ] UN E-Government Survey (biannual: next 2024)
- [ ] ZenDiS annual report (annual)
- [ ] New EU AI Act national implementation guidance (BMI, BMUV, Swiss EDÖB)
- [ ] New CRA compliance guidance for open-source procurement
- [ ] EU Digital Identity Wallet (EUDIW) implementation updates
- [ ] eCH standards updates (new or revised standards)
