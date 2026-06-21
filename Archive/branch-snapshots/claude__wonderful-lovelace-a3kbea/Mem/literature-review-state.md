# Literature Review State — City GovTech Strategy

**Version:** 0.2.0
**Last reviewed:** 2026-06-21
**Next review due:** 2026-09-21 (quarterly cadence)

This document tracks the current state of the literature review: what is covered, what
is missing, and what needs updating. It is the primary input to
`Scripts/update_literature_review.py`.

---

## Coverage map (v0.2.0)

### Covered

| Domain | Depth | Status |
|---|---|---|
| E-government theory (Wirtz/Weyerer, Janowski, Scholl, Lucke/Reinermann) | High | v0.2.0 ✓ |
| Swiss EMBAG and federal digital strategy | High | v0.2.0 ✓ |
| Swiss E-ID (BGEID, post-2021 redesign) | High | v0.2.0 ✓ NEW |
| German OZG / OZG 2.0 | High | v0.2.0 ✓ |
| Sovereign Cloud Stack | High | v0.2.0 ✓ |
| Open Source in EU public administration (OSOR, FSFE) | High | v0.2.0 ✓ |
| ZenDiS and OpenDesk | High | v0.2.0 ✓ NEW |
| Identity management (Keycloak, BundID, eID) | High | v0.2.0 ✓ |
| Decidim / CONSUL participatory platforms | High | v0.2.0 ✓ |
| Matrix/Element for government | Medium | v0.2.0 ✓ |
| Nextcloud for government | High | v0.2.0 ✓ |
| Open data portals (CKAN, opendata.swiss) | High | v0.2.0 ✓ |
| GIS for municipalities (QGIS, OSM) | Medium | v0.2.0 ✓ |
| eCH standards (Swiss interoperability) | Medium | v0.2.0 ✓ NEW |
| XÖV standards (German interoperability) | High | v0.2.0 ✓ |
| FIM / Föderales Informationsmanagement | Medium | v0.2.0 ✓ NEW |
| GovStack building blocks | Medium | v0.2.0 ✓ NEW |
| EU Digital Compass 2030 | Medium | v0.2.0 ✓ NEW |
| OECD Digital Government Framework | Medium | v0.2.0 ✓ NEW |
| Total cost of ownership evidence | Medium | v0.2.0 ✓ NEW |
| Procurement frameworks | Medium | v0.2.0 ✓ |
| Legal/regulatory compliance matrix | Medium | v0.2.0 ✓ NEW |
| Citizen experience and digital inclusion | Medium | v0.2.0 ✓ NEW |
| Change management in IT transitions | Medium | v0.2.0 ✓ |
| Cooperative IT structures (govdigital, AKDB, Dataport) | High | v0.2.0 ✓ |
| AI in public administration | Low | v0.2.0 ✓ NEW — needs deepening in v0.3.0 |
| BSI security frameworks | High | v0.2.0 ✓ |
| NIS2 and cybersecurity law | High | v0.2.0 ✓ |

### Not yet covered (to address in v0.3.0+)

- **EU Data Act 2023** (Regulation 2023/2854) — municipal data governance
- **EU AI Act 2024** (Regulation 2024/1689) — AI in public administration
- **eIDAS 2.0** (European Digital Identity Regulation) — cross-border digital identity
- **GAIA-X** (2025 state of play) — European data space infrastructure
- **LocalAI / Ollama** — sovereign open-source AI inference for public sector
- **Swiss OGD-Strategie 2024–2027** — dedicated open data strategy
- **IT-Planungsrat Annual Report 2024** — German federal IT planning council
- **GeoServer** — detailed analysis of OGC-compliant map server
- **Flowable BPM** — Apache 2.0 alternative to Camunda
- **Barcelona Decidim case study** — detailed post-2020 outcomes
- **Helsinki Hel.fi open-source journey** — Nordic case study
- **Schleswig-Holstein Linux migration** — current German Land OS migration
- **Small municipality implementations** (<10,000 population)
- **Rural municipality challenges** — connectivity, skills, shared services
- **Citizen trust in digital government services** — dedicated survey literature
- **Digital accessibility standards** (WCAG 2.2, EN 301 549, Swiss P028)

---

## Critical gaps (v0.3.0 priorities)

### 1. AI Act compliance for municipal AI use
The EU AI Act (Regulation (EU) 2024/1689, applicable August 2026) classifies several
municipal AI applications as High Risk: benefits assessment, credit scoring,
population surveillance. A v0.3.0 section on sovereign AI tooling with AI Act
compliance requirements is needed.

### 2. EU Data Act and data sharing obligations
The Data Act (Regulation (EU) 2023/2854, applicable September 2025) requires public
sector bodies to share data upon request under FAIR conditions. Implications for
municipal open data portals and inter-agency data exchange must be documented.

### 3. Longitudinal cost data from completed transitions
The Munich LiMux case (2003–2017) is available but the reversal confounds cost
analysis. Schleswig-Holstein's ongoing Linux migration (2021–2026) and
Bourgogne-Franche-Comté (LibreOffice, 2017–2022) offer cleaner data once published.
Target: cite 3 independent TCO comparisons with methodology documented.

### 4. Small municipality implementation data
Most case studies involve cities >100,000. The median EU municipality has <5,000
residents. Shared-service models (Zweckverbände, IT-Kooperationen) deserve detailed
analysis. Target: 3 case studies of municipalities <20,000 for v0.3.0.

---

## Improvement log

| Date | Version | Action | By | Result |
|---|---|---|---|---|
| 2026-06-20 | 0.1.0 | Initial literature review | SG | 30 primary sources; 46 citation slots |
| 2026-06-21 | 0.2.0 | Citation-complete review | SG | 55 verified sources; all citations verified; 5 new sections added |

---

## Quarterly review checklist

When running `Scripts/update_literature_review.py`, check for:

- [ ] New Swiss e-government legislation or strategy updates (fedlex.admin.ch)
- [ ] New German OZG implementation reports or FITKO publications (fitko.de)
- [ ] New EU legislation affecting digital government (eur-lex.europa.eu)
- [ ] New Sovereign Cloud Stack releases (scs.community, docs.scs.community)
- [ ] New openCode.de statistics or case studies (opencode.de)
- [ ] New ZenDiS publications (zendis.de)
- [ ] New academic papers on e-government maturity (GIQ, ISM, EJEG, IP journals)
- [ ] New municipal open-source case studies (OSOR, Joinup)
- [ ] New security advisories affecting stack components (BSI, CERT-Bund)
- [ ] OSOR annual review (joinup.ec.europa.eu — published Q1 each year)
- [ ] UN E-Government Survey (next edition: 2024, then 2026)
- [ ] eCH standard updates (ech.ch)
- [ ] XÖV standard updates (xoev.de)
- [ ] IT-Planungsrat resolutions (it-planungsrat.de)
- [ ] Swiss IT-Planungsrat equivalent (E-Government Suisse)
