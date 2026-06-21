# Literature Review State — City GovTech Strategy

**Version:** 0.2.0
**Last reviewed:** 2026-06-20
**Next review due:** 2026-09-20 (quarterly cadence)

This document tracks the current state of the literature review: what is covered, what is
missing, and what needs updating. It is the primary input to
`Scripts/update_literature_review.py`.

---

## Coverage map

### Covered (v0.2.0)

| Domain | Depth | Key gaps |
|---|---|---|
| E-government theory (Wirtz/Weyerer, Janowski) | Medium | No post-2022 literature on 4th-gen e-gov |
| Swiss EMBAG and federal digital strategy | High | Cantonal implementation data lacking |
| German OZG / OZG 2.0 | High | Municipal uptake statistics missing |
| Sovereign Cloud Stack | High | Production metrics not yet available |
| Open Source in EU public administration | Medium | OSOR annual report [58] supplementary only |
| Identity management (Keycloak, BundID, eID) | High | Swiss E-ID [52] covered; eIDAS 2.0 wallet pending |
| Decidim / participatory platforms | High | CONSUL Democracy [53] added; Barcelona case [54] added |
| Matrix/Element for government | Medium | BundesMessenger adoption data needed |
| Nextcloud for government | Medium | Swiss federal deployment details |
| Open data portals (CKAN, opendata.swiss) | High | Helsinki [56] case study added |
| GIS for municipalities | Low | No academic literature cited |
| Procurement frameworks | Medium | RFP template added (§6.3); no comparative EU procurement studies |
| Total cost of ownership studies | Medium | TCO methodology and model added (§6.1–6.2) |
| User experience / satisfaction research | Absent | CRITICAL GAP — see below |
| Small municipality case studies | Low | CRITICAL GAP — see below |
| Change management in IT transitions | Medium | §6.4 added; Munich LiMux referenced |
| eCH standards (Switzerland) | Medium | [51] added; detailed eCH profiles pending |
| GovStack building blocks | Medium | [50] added; EU alignment analysis pending |
| EU Data Act implications | Medium | [55] added; §7.3 analysis added |
| EU Data Governance Act | Medium | [48] added; §3.6 added |
| ZenDiS / OpenDesk governance | Medium | [49] cited; annual report unverified |
| Schleswig-Holstein migration | High | [47] cited; case study in §3.8 |
| Barcelona Digital City | High | [54] cited; case study in §3.8 |
| Helsinki digital city | Medium | [56] cited; case study in §3.8 |
| Swiss Federal open-source | Medium | Case study in §3.8 (EMBAG, Nextcloud) |
| DSK analytics ruling | High | [57] cited; §7.3 GDPR analysis |
| Vendor exit strategy | Medium | §7.5 added |
| GDPR/DSGVO compliance | High | §7.3 added with detailed analysis |
| Cybersecurity maturity | Medium | §7.4 table added (BSI, NIS2) |
| Glossary / terminology | High | §9 glossary added (25 terms) |
| Regulatory reference table | High | Appendix A added |
| Office productivity (LibreOffice) | High | §4.10 added |
| Web analytics (Matomo) | High | §4.11 added; DSK ruling cited |
| DevOps / code hosting (Forgejo) | Medium | §4.12 added |
| Municipal ERP | Low | Advisory note only (§4.13) |
| KPI framework | Medium | §5.1 table added (12 KPIs) |

### Not yet covered

- **EU Digital Services Act / Digital Markets Act** — interaction with municipal procurement
- **OpenDesk v2.x** (2025/2026 updates and roadmap)
- **Swiss OGD Strategy 2024–2027** (distinct from E-Government Strategy)
- **GAIA-X implementation status** (2025 state of play; relevance to municipal cloud)
- **LibreOffice in public administration** — peer-reviewed literature on document format sovereignty and migration outcomes
- **Academic literature on participatory budgeting outcomes** (to support Decidim/CONSUL claims)
- **eIDAS 2.0 / EU Digital Identity Wallet** (interoperability with Swiss E-ID and BundID)
- **Post-2022 academic literature on 4th-generation e-government**
- **OKD (Origin Kubernetes Distribution)** — open alternative to OpenShift for container orchestration
- **OSOR Annual Report 2023** — in supplementary registry [58]; full incorporation pending

---

## Critical gaps

### TCO studies
No rigorous independent comparative Total Cost of Ownership studies cover the full
open-source vs. proprietary municipal stack. A TCO methodology and 5-year model have been
added to §6.1–6.2 of the v0.2.0 paper, but the underlying numerical inputs remain
estimates pending empirical validation.
**Action:** Identify or commission an independent municipal TCO study. Target: v1.0.0.

### User experience research
Almost no peer-reviewed literature exists on citizen satisfaction with open-source vs.
proprietary municipal digital services.
**Action:** Design a citizen-satisfaction survey framework usable by participating
municipalities. Target: v1.0.0 appendix.

### Small-municipality data
Most case studies involve large cities (Barcelona, Helsinki, Munich) or federal agencies.
The median EU municipality has population <10,000.
**Action:** Document 3–5 case studies of municipalities <50,000 that completed open-source
transitions. Target: v0.3.0.

---

## Improvement log

| Date | Action | By | Result |
|---|---|---|---|
| 2026-06-20 | Initial literature review, v0.1.0 draft | SG | 30 primary sources identified; 46 citation slots in paper |
| 2026-06-20 | German translation v0.1.0 completed | SG/AI | Full translation added at Doc/de/ |
| 2026-06-20 | v0.2.0 paper drafted and pushed (EN + DE + HTML) | SG/AI | Full citation-complete draft; 57 references; 10 sections + 2 appendices |
| 2026-06-20 | Source registry realigned to v0.2.0 citation numbering | SG/AI | Entries [47]–[57] corrected; [58]–[59] as supplementary |
| 2026-06-20 | Literature review state updated to v0.2.0 | SG/AI | Coverage map expanded to 30+ domains; 3 critical gaps identified |

---

## Quarterly review checklist

When running `Scripts/update_literature_review.py`, check for:

- [ ] New Swiss e-government legislation or strategy updates
- [ ] New German OZG implementation reports or FITKO publications
- [ ] New EU legislation (Data Act implementation, AI Act, eIDAS 2.0, etc.)
- [ ] New Sovereign Cloud Stack releases or governance updates
- [ ] New openCode.de statistics or case studies
- [ ] New academic papers on e-government maturity (GIQ, ISM, EJEG)
- [ ] New municipal open-source deployments or case studies (esp. <50k population)
- [ ] New security advisories affecting stack components (BSI, CERT-Bund)
- [ ] OSOR annual report (EU Open Source Observatory, annual; update [58])
- [ ] UN E-Government Survey (biannual; next 2024)
- [ ] ZenDiS annual report / OpenDesk release notes (update [49] → next version)
- [ ] GovStack building block updates
- [ ] Swiss E-ID / BGEID implementation milestones
- [ ] Decidim and CONSUL Democracy new deployment statistics
- [ ] LibreOffice peer-reviewed adoption literature
- [ ] eIDAS 2.0 EU Digital Identity Wallet implementation status
- [ ] DSK / DPA guidance updates on analytics and cloud tools
