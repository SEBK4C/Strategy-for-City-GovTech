# Literature Review State — City GovTech Strategy

**Version:** 0.2.0
**Last reviewed:** 2026-06-21
**Next review due:** 2026-09-21 (quarterly cadence)

This document tracks the current state of the literature review: what is covered, what is
missing, and what needs updating. It is the primary input to
`Scripts/update_literature_review.py`.

---

## Coverage map (v0.2.0)

### Covered

| Domain | Depth | Gaps remaining |
|---|---|---|
| E-government theory (Wirtz/Weyerer, Janowski, GovStack DPI) | High | No post-2022 peer-reviewed literature on 4th-gen e-gov |
| Swiss EMBAG and federal digital strategy | High | Cantonal implementation reports not yet aggregated |
| Swiss E-ID / SWIYU (Dec 2024 law, 2026 go-live) | High | Post-launch cantonal service integration data pending |
| eCH standards (0007, 0020, 0058) | Medium | eCH-0160 not yet covered; cantonal adoption rates |
| German OZG / OZG 2.0 | High | Municipal service uptake data beyond 81/581 end-2023 figure |
| Deutschland-Stack (March 2026) | High | Implementing acts still in development |
| Sovereign Cloud Stack | High | Post-binding-mandate adoption statistics (March 2026 decision) |
| OpenDesk / ZenDiS | High | Confirmed licence count for end-2025 target not yet verified |
| BundID adoption | Medium | Statistics beyond August 2025 not incorporated |
| Open Source in EU public administration (OSOR, IEA) | High | 2025 OSOR annual report not yet integrated |
| Identity management (Keycloak, BundID, eID) | High | BundID→DeutschlandID transition timeline |
| Decidim / participatory platforms | Medium | Schaffhausen canton longitudinal case study needed |
| Matrix/Element for government | Medium | BundesMessenger 2025 adoption data; French Tchap statistics |
| Nextcloud for government | High | Swiss federal deployment specifics |
| Open data portals (CKAN) | High | opendata.swiss statistics 2025 |
| GIS for municipalities | Low | No peer-reviewed academic literature cited |
| Procurement frameworks | Medium | Comparative EU procurement studies still needed |
| Total cost of ownership | High | GendBuntu + Schleswig-Holstein verified; independent audit still absent |
| User experience / satisfaction research | Absent | CRITICAL GAP — no peer-reviewed literature |
| Small municipality case studies | Medium | Signalen + eVaka covered; DE/CH small-municipality examples still needed |
| Change management in IT transitions | Medium | Munich LiMux + GendBuntu governance model; deeper change-mgmt literature needed |
| NIS2/KRITIS for municipalities | High | German implementation covered; Swiss NIS2-equivalent not covered |
| GovStack building blocks | Medium | Municipal-level implementation examples sparse |
| Sovereign Tech Agency / Fund | Medium | Project-level impact data on municipal-relevant components |
| EU Data Act 2023 | Absent | TO DO for v1.0 |
| GAIA-X | Low | Practical municipal relevance still unclear; policy-layer only |

---

## Critical gaps (updated v0.2.0 → v1.0 agenda)

### TCO — independent audit
The GendBuntu (~40% TCO reduction, ~€2M/year) and Schleswig-Holstein (€15M savings, <1yr payback) data are verified from open sources but are government-reported or secondary analyses, not independently audited. **Action:** identify/commission an independent comparative TCO methodology. Target: v1.0.

### User experience research
No peer-reviewed literature on citizen satisfaction with open-source vs. proprietary municipal digital services. **Action:** design a citizen-satisfaction survey framework usable by participating municipalities. Target: v1.0 appendix.

### Swiss small-municipality data
Cantonal-level EMBAG implementation reports and eCH adoption rates are not yet comprehensively documented. **Action:** contact eCH Association and E-Government Suisse for cantonal rollout data. Target: v0.3.0.

### EU Data Act municipal implications
The EU Data Act (2023) has significant implications for how municipalities handle data generated through public services. Not yet covered. **Action:** add section on Data Act to regulatory framework analysis. Target: v0.3.0.

### BundID→DeutschlandID transition
The evolution from BundID to DeutschlandID (anticipated 2025–2026) is referenced but not yet documented in detail. **Action:** monitor and document when publicly announced. Target: v0.3.0.

---

## Improvement log

| Date | Action | By | Result |
|---|---|---|---|
| 2026-06-20 | Initial literature review, v0.1.0 draft | SG | 30 primary sources; 46 citation slots |
| 2026-06-21 | v0.2.0 deep research round: 5 parallel searches, 8 source fetches, 13 verified findings | SG + Claude | 20 new sources added ([47]–[66]); all 66 citations verified; TCO section expanded; regulatory section added; small-municipality section added; GovStack integrated; NIS2/KRITIS documented |

---

## Quarterly review checklist (v0.2.0 → v0.3.0)

When running `Scripts/update_literature_review.py`, check for:

- [ ] ZenDiS annual report 2024/2025 (publication pending)
- [ ] Confirmed OpenDesk licence count vs. 160,000 target
- [ ] BundID/DeutschlandID migration timeline update
- [ ] Swiss eID / SWIYU post-launch cantonal service statistics (expected late 2026)
- [ ] OSOR Annual Report 2025 (expected Q1 2026)
- [ ] New UN E-Government Survey (biannual; next expected 2024)
- [ ] New Swiss e-government legislation or strategy updates
- [ ] New OZG implementation reports or FITKO publications
- [ ] EU Data Act 2023 municipal implementation guidance
- [ ] Interoperable Europe Act implementing acts (due from Commission)
- [ ] Deutschland-Stack implementing acts and municipal guidance
- [ ] New academic papers on e-government maturity (GIQ, ISM, EJEG) post-2022
- [ ] New security advisories affecting stack components
- [ ] NIS2 implementation in Switzerland (separate from Germany)
- [ ] EUCS (EU Cybersecurity Certification Scheme) final decision
- [ ] GAIA-X practical municipal tooling (vs. policy)
- [ ] Signalen expansion: new municipalities, updated citizen count
