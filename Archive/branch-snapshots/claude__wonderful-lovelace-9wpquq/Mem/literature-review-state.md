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
| E-government theory (Wirtz/Weyerer, Janowski) | Medium | No post-2022 literature on 4th-gen e-gov |
| Swiss EMBAG and federal digital strategy | High | Cantonal implementation statistics not yet systematically collected |
| German OZG / OZG 2.0 | High | Municipal uptake statistics incomplete |
| Sovereign Cloud Stack | High | Production deployment metrics sparse |
| Open Source in EU public administration | High | OSOR 2024 report (if available) not yet integrated |
| Identity management (Keycloak, BundID, eID) | High | BundID uptake data; Swiyu test-phase data unavailable until 2026 |
| Decidim / participatory platforms | High | Schaffhausen canton case study; Barcelona formal academic post-mortem |
| CONSUL Democracy platform (Madrid) | Medium | Comparative Decidim vs CONSUL study needed |
| Matrix/Element for government | Medium | BundesMessenger quantitative adoption data |
| Nextcloud for government | High | Swiss federal deployment performance metrics |
| Open data portals (CKAN, opendata.swiss) | High | Dataset quality/completeness metrics |
| GIS for municipalities | Medium | No peer-reviewed academic literature cited |
| Procurement frameworks | Medium | No comparative EU procurement empirical studies |
| Total cost of ownership studies | Medium | No rigorous independent cross-municipality study; anchored on DGFiP and Barcelona cases |
| User experience / satisfaction research | Low | No peer-reviewed citizen satisfaction data; survey framework recommended |
| Small-municipality case studies | Medium | Three structural mechanisms documented; individual case studies still sparse |
| Change management in IT transitions | Medium | Munich LiMux well-covered; positive small-municipality cases still lacking |
| eCH standards (Switzerland) | High | Complete standards family documented [47] |
| GovStack (ITU/DIAL) | High | Building-block architecture integrated [49] |
| ZenDiS (German sovereignty centre) | High | Full coverage including OpenDesk and partner ecosystem [50] |
| OSOR Annual Report 2023 | Medium | Integrated [51]; 2024 report pending |
| EU Data Act | High | Full coverage including Art. 5, 23–31 implications [52] |
| GAIA-X implementation | Medium | Architecture covered [56]; 2025 state-of-play data sparse |
| Lathrop & Ruma (2010) | Low | Theoretical grounding cited [53]; deeper engagement planned |

### Not yet covered (v0.3.0 targets)

- **BundID technical architecture** — official identity federation documentation
- **Swiss eID (Swiyu) technical specification** — W3C VC / OpenID4VC implementation details; data unavailable until 2026 launch
- **OKD (Origin Kubernetes Distribution)** — open alternative to OpenShift for municipalities wanting Red Hat ecosystem without licence
- **EU AI Act** (Regulation (EU) 2024/1689) — obligations for municipalities deploying AI-assisted services
- **Digital Services Act / Digital Markets Act** — interaction with municipal procurement decisions
- **Swiss OGD Strategy 2024–2027** — successor to OGD Switzerland 2019–2023 strategy
- **EU Cybersecurity Act** certification schemes — relevant for municipal cloud infrastructure evaluation
- **Fraunhofer or Bertelsmann municipal TCO studies** — any commissioned independent comparative studies
- **Barcelona Decidim formal post-mortem** — peer-reviewed academic or municipal evaluation of 18-month TCO claim

---

## Critical gaps — status after v0.2.0

### TCO studies [was CRITICAL → now MEDIUM]
v0.1.0 gap: No independent comparative TCO studies.
v0.2.0 resolution: Section 3.9 builds a 7-category TCO methodology framework and anchors it with
two documented cases: DGFiP LibreOffice (€14M savings, 170,000 workstations) [54] and Barcelona
Decidim (TCO-neutral at 18 months). Independent rigorous cross-municipality study still needed
for v1.0. Gap remains but is no longer blocking.

### User experience research [CRITICAL → LOW, remains open]
v0.2.0 resolution: Citizen satisfaction survey framework described in Section 3.10 and Appendix C.
No peer-reviewed data yet. Survey framework now documented as v1.0 deliverable. Gap acknowledged.

### Small-municipality data [CRITICAL → MEDIUM]
v0.2.0 resolution: Section 3.10 documents three structural mechanisms enabling small municipalities
to transition (cooperative model, EfA shared services, GovStack building blocks). Named reference
municipalities include St. Gallen, Zug (Schaffhausen), municipalities in Mecklenburg-Vorpommern
(Dataport). Individual small-municipality case studies with full before/after data still lacking.
Action for v0.3.0: contact openCode.de and kantonale Informatikleistungscenter for case data.

---

## Improvement log

| Date | Action | By | Result |
|---|---|---|---|
| 2026-06-20 | Initial literature review, v0.1.0 draft | SG | 30 primary sources identified; 46 citation slots in papers |
| 2026-06-21 | v0.2.0 expansion | SG | Added sources [47]–[56]: eCH, CONSUL, GovStack, ZenDiS, OSOR, EU Data Act, Lathrop & Ruma, DGFiP, Munich LiMux, GAIA-X. All v0.1.0 critical gaps addressed. Three coverage areas elevated from absent/low to medium/high. |

---

## Quarterly review checklist

When running `Scripts/update_literature_review.py`, check for:

- [ ] New Swiss e-government legislation or strategy updates (fedlex.admin.ch, egovernment.ch)
- [ ] New German OZG implementation reports or FITKO publications (fitko.de, bmi.bund.de)
- [ ] New EU legislation affecting municipal digital infrastructure (eur-lex.europa.eu)
- [ ] New Sovereign Cloud Stack releases or governance updates (scs.community, docs.scs.community)
- [ ] New openCode.de statistics or case studies (opencode.de)
- [ ] New academic papers on e-government maturity (GIQ, ISM, EJEG, IFIP journals)
- [ ] New municipal open-source deployments or case studies — especially small municipalities
- [ ] New security advisories affecting stack components (OSV.dev, CVE feeds)
- [ ] OSOR Annual Report update (joinup.ec.europa.eu/collection/open-source-observatory-osor)
- [ ] UN E-Government Survey (biannual — next due 2024)
- [ ] ZenDiS / OpenDesk release announcements (zendis.de, opendesk.eu)
- [ ] GovStack specification updates (govstack.global)
- [ ] eCH standards new publication or revision (ech.ch)
- [ ] Swiss eID (Swiyu) pilot/launch data (once available 2026)
- [ ] BundID uptake statistics (bmi.bund.de)
- [ ] govdigital eG annual report or new framework contracts (govdigital.de)
- [ ] New EU AI Act implementing acts with public-sector implications
- [ ] GAIA-X Trust Framework updates and implementation metrics
