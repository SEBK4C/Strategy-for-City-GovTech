# Literature Review State — City GovTech Strategy

**Version:** 0.2.0
**Last reviewed:** 2026-06-20
**Next review due:** 2026-09-20 (quarterly cadence)

This document tracks the current state of the literature review: what is covered, what is
missing, and what needs updating. It is the primary input to
`Scripts/update_literature_review.py`.

**v0.2.0 changes:** Coverage updated to reflect new sections 3.5–3.8 added to the main
paper. Four new domains (ZenDiS/OpenDesk, eCH standards, EU Data Act, GovStack) added
at Medium depth. Critical gaps updated.

---

## Coverage map

### Covered (v0.2.0)

| Domain | Depth | Key gaps |
|---|---|---|
| E-government theory (Wirtz/Weyerer [7], Janowski [30], Lathrop/Ruma [53]) | Medium-High | No post-2022 peer-reviewed literature on 4th-gen e-gov |
| Swiss EMBAG and federal digital strategy | High | Cantonal implementation statistics lacking |
| German OZG / OZG 2.0 | High | Municipal uptake statistics missing; 2024 reform implementation still early |
| Sovereign Cloud Stack | High | Production deployment metrics not yet publicly available |
| Open source in EU public administration (OSOR [49]) | Medium | 2024 OSOR report not yet available |
| Identity management (Keycloak [21], BundID, Swiss eID) | Medium | Swiss eID v2 (2024 relaunch) technical details needed |
| Decidim / participatory platforms [12] | Medium | Schaffhausen canton case study data needed |
| CONSUL Democracy [52] | Low-Medium | Only cited; no in-depth analysis |
| Matrix/Element for government [14] | Medium | BundesMessenger adoption data 2024 needed |
| Nextcloud for government [13] | Medium | Swiss federal deployment technical details |
| Open data portals (CKAN) [22] | Medium | opendata.swiss technical architecture |
| GIS for municipalities [37] | Low | No academic literature cited on municipal GIS outcomes |
| Procurement frameworks | Low | No comparative EU procurement law analysis |
| Total cost of ownership studies | Low-Medium | TCO framework added (Section 4.10); still needs independent validation |
| User experience / satisfaction research | Absent | CRITICAL GAP — targeted for v1.0 appendix |
| Small municipality case studies | Low | CRITICAL GAP — targeted for v0.3.0 companion paper |
| Change management in IT transitions | Low | Munich LiMux referenced; needs broader analysis |
| **ZenDiS and OpenDesk [42][48]** | Medium | ADDED v0.2.0; ZenDiS deployment data limited |
| **eCH standards [51]** | Medium | ADDED v0.2.0; individual standard deep-dives pending |
| **EU Data Act [47]** | Medium | ADDED v0.2.0; municipal procurement implications evolving |
| **GovStack building blocks [50]** | Low-Medium | ADDED v0.2.0; alignment with recommended stack components |

### Not yet covered (targets for v0.3.0 and v1.0)

- **CONSUL Democracy in-depth** — beyond citation, case study analysis
- **Individual eCH standards** — eCH-0011, eCH-0058, eCH-0010 detailed coverage
- **BSI Cloud Computing Compliance Controls Catalogue (C5)** — cloud hosting compliance
- **Digital Services Act / Digital Markets Act** — interaction with municipal procurement
- **OpenDesk v2.x update** (2026) — if materially changed from v0.2.0 coverage
- **GAIA-X implementation status** (2025/2026 state of play)
- **Swiss E-ID v2 technical details** — post-2024 relaunch implementation
- **Barcelona Digital City Plan 2017** — primary source for Barcelona case study
- **Munich LiMux post-mortem primary sources** — need to identify and cite specific academic analyses
- **EU Data Act municipal procurement case law** — still emerging (2025–2026)
- **AKDB (Bayern) reference deployment details** — technical architecture
- **Lathrop & Ruma (2010)** — integrated into theoretical framework but deserves dedicated section

---

## Critical gaps

### TCO Studies
v0.1.0 identified this gap. v0.2.0 adds an indicative TCO framework (Section 4.10) based on publicly available data. However, **no independent, peer-reviewed TCO study** specifically comparing open-source and proprietary municipal administration stacks exists in the literature. The closest are:
- French state LibreOffice migration study (Ciril Group, 2019) — context-specific
- Munich LiMux TCO analyses — contested and vendor-influenced
- OSOR's open-source migration cost studies — aggregate EU, not municipal-specific
**Action:** Draft a TCO methodology framework for participating municipalities to use, targeting v0.3.0.

### User Experience Research
Almost no peer-reviewed literature exists on citizen satisfaction with open-source vs. proprietary municipal digital services. The gap is structural: few municipalities have run comparable services on both platforms with controlled measurement.
**Action:** Design a citizen-satisfaction survey framework usable by participating municipalities. Target: v1.0 appendix.

### Small-Municipality Data
Most case studies involve large cities (Barcelona, Helsinki) or federal agencies. The median EU municipality has population <5,000 and the median Swiss Gemeinde <2,500. These contexts differ fundamentally from large-city deployments in IT staffing, budget, procurement authority, and political dynamics.
**Action:** Document 3–5 case studies of municipalities <50,000 that completed open-source transitions. Target: v0.3.0 companion paper.

### Post-Data Act Procurement Practice
The EU Data Act became applicable in September 2025, and academic analysis of its municipal procurement implications is still emerging. Practitioners are ahead of the literature here.
**Action:** Monitor and document emerging practice via OSOR, openCode.de community, and municipal IT cooperative publications. Target: v0.4.0.

---

## Improvement log

| Date | Action | By | Result |
|---|---|---|---|
| 2026-06-20 | Initial literature review, v0.1.0 draft | SG | 30 primary sources identified; 46 citation slots in papers |
| 2026-06-20 | v0.2.0 update: verify [6][9][16][43]; add [47]-[54]; new sections 3.5-3.8 | SG | 4 citations verified; 8 new sources; 4 new domains covered |

---

## Quarterly review checklist

When running `Scripts/update_literature_review.py`, check for:

- [ ] New Swiss e-government legislation or strategy updates (fedlex.admin.ch, egovernment.ch)
- [ ] New German OZG implementation reports or FITKO publications (fitko.de)
- [ ] New EU legislation or regulations affecting municipal digital services
- [ ] New Sovereign Cloud Stack releases or governance updates (scs.community)
- [ ] New openCode.de statistics or case studies
- [ ] New academic papers on e-government maturity (GIQ, ISM, EJEG databases)
- [ ] New municipal open-source deployments or case studies (OSOR, openCode.de)
- [ ] New security advisories affecting stack components (BSI, CERT-Bund)
- [ ] OSOR annual report (joinup.ec.europa.eu, published Q1 each year)
- [ ] UN E-Government Survey (biannual, UNDESA)
- [ ] ZenDiS publications and OpenDesk updates (zendisgmbh.de)
- [ ] eCH standard revisions (ech.ch)
- [ ] New GovStack specification releases (govstack.global)
- [ ] EU Data Act implementation guidance and case law
- [ ] BSI publications on cloud computing and AI security

## Next review priorities (Q3 2026)

1. OSOR Annual Report 2024 (expected Q1 2026)
2. Swiss eID v2 implementation status update
3. OpenDesk deployment statistics from ZenDiS 2026
4. OZG 2.0 implementation progress report (FITKO Q2 2026)
5. GovStack v1.1 specification update (expected 2026)
