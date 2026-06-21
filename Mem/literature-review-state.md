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

| Domain | Depth | Key gaps |
|---|---|---|
| E-government theory (Wirtz/Weyerer, Janowski) | Medium | No post-2022 literature on 4th-gen e-gov |
| Swiss EMBAG and federal digital strategy | High | Cantonal implementation data lacking |
| Swiss eCH interoperability standards | Medium | Individual standard specs not yet cited |
| Swiss BGElD / e-ID 2026 | Medium | Implementation details (wallet spec) pending |
| German OZG / OZG 2.0 | High | Municipal uptake statistics missing |
| German BundID | Medium | Uptake statistics (user count) not yet cited |
| Sovereign Cloud Stack | High | Production performance metrics not yet available |
| Open Source in EU public administration | Medium | OSOR annual report (v0.2.0 entry added; URL unverified) |
| Identity management (Keycloak) | High | Covered well |
| Participatory democracy (Decidim, CONSUL) | Medium | Both platforms now covered |
| Matrix/Element for government | Medium | BundesMessenger adoption statistics needed |
| Nextcloud for government | Medium | Swiss federal deployment details |
| Open data portals (CKAN) | Medium | DCAT-AP.ch compliance details |
| GIS for municipalities | Low | No academic literature cited |
| Procurement frameworks | Low | No comparative EU procurement studies |
| Total cost of ownership studies | **Medium** | French Gendarmerie + Vitoria-Gasteiz added; no independent CH/DE study |
| Small municipality case studies | **Medium** | Schaffhausen, Vitoria-Gasteiz, Bolzano, Rennes added (Section 3.8) |
| Change management in IT transitions | Low | Munich LiMux referenced; no systematic change-mgmt framework |
| EU regulatory framework (AI Act, Data Act, NIS2) | **High** | All three now covered in Section 3.7 |
| ZenDiS / OpenDesk | **High** | ZenDiS entry [51] added; OpenDesk [42] previously covered |
| GovStack building blocks | **Medium** | Entry [49] added; integration into tech-stack section needed |
| AI services for municipalities | **Low** | Ollama [59] added; Section 4.10 drafted; EU AI Act compliance framework needs expansion |
| Data governance and GDPR architecture | **Medium** | New Section 7 drafted; specific DPA guidance citations still needed |
| GAIA-X implementation | **Low** | Entry [61] added; 2025 state-of-play analysis pending |
| Foundational open-government theory | **Medium** | Lathrop & Ruma [56] added |

### Not yet covered (target: v0.3.0)

- **OKD** (Origin Kubernetes Distribution) — open alternative to OpenShift
- **Munich LiMux post-mortem** — detailed political-failure academic analysis beyond brief narrative
- **EU Data Spaces** (health, mobility, smart cities) — implementation status 2025
- **Citizen satisfaction research** — quantitative studies on UX of open-source vs. proprietary municipal services
- **OpenDesk v2.x** (2025/2026 feature updates)
- **OSOR Annual Report 2024** (when published)
- **Swiss cantonal case studies** — beyond Schaffhausen (e.g., Zurich, Berne digital strategy)
- **Accessibility research** — BITV 2.0 / EN 301 549 compliance studies for open-source stacks

---

## Critical gaps — status update

### TCO studies
**Status: Partially addressed at v0.2.0.**
French Gendarmerie (~40% savings, 72,000 workstations) and Vitoria-Gasteiz (>€200k savings)
added as reference cases. A 5-year TCO comparison table (1,000 users: open-source €1.8M–€4.5M
vs. proprietary €2.2M–€5.5M) added to Section 3.6 using methodology drawn from those cases.
**Remaining gap:** No independent CH/DE study. Commission or identify such a study for v0.3.0.

### User experience research
**Status: Unchanged — still absent from literature.**
No peer-reviewed literature exists on citizen satisfaction with open-source vs. proprietary
municipal digital services. **Action:** design a citizen-satisfaction survey framework usable
by participating municipalities. Target: v1.0 appendix.

### Small-municipality data
**Status: Addressed at v0.2.0.**
Section 3.8 now covers four case studies: Schaffhausen CH (~80,000), Vitoria-Gasteiz ES
(~252,000), Bolzano IT (~108,000), Rennes FR (~220,000). All below the mega-city tier.
**Remaining gap:** Case studies below 50,000 population still thin. Target: v0.3.0.

### AI governance
**Status: New gap identified and partially addressed at v0.2.0.**
EU AI Act Article annotations added. Section 4.10 on local AI services drafted.
**Remaining gap:** Specific DPA (data protection authority) guidance on AI in municipal
context; real-world Ollama deployment case studies in government.

---

## Improvement log

| Date | Action | By | Result |
|---|---|---|
| 2026-06-20 | Initial literature review, v0.1.0 draft | SG | 30 primary sources; 46 citation slots in papers |
| 2026-06-21 | v0.2.0 citation-complete round | SG/AI | Added [47]–[61]: CONSUL, eCH, GovStack, OSOR, ZenDiS, Swiss OGD, French Gendarmerie TCO, EU AI Act, EU Data Act, Lathrop & Ruma, BundID, BGElD, Ollama, Vitoria-Gasteiz, GAIA-X. New sections: 3.6 (TCO), 3.7 (EU regulatory), 3.8 (small municipalities), 4.10 (AI), 7 (Data Governance). Papers promoted to v0.2.0. |

---

## Quarterly review checklist

When running `Scripts/update_literature_review.py`, check for:

- [ ] New Swiss e-government legislation or strategy updates (EMBAG implementation decrees)
- [ ] BGElD implementation progress (wallet spec, cantonal rollout)
- [ ] New German OZG implementation reports or FITKO publications
- [ ] BundID uptake statistics (user count, service integrations)
- [ ] EU AI Act phased application milestones (2025: GPAI rules; 2026: high-risk system audits)
- [ ] EU Data Act Art. 23/25 implementation: cloud-switching and interoperability standards
- [ ] New Sovereign Cloud Stack releases or governance updates
- [ ] New openCode.de statistics or case studies
- [ ] New academic papers on e-government maturity (GIQ, ISM, EJEG, EGOV conference)
- [ ] New municipal open-source deployments or case studies (especially <50k population)
- [ ] OSOR annual report (EU Open Source Observatory, annual publication)
- [ ] ZenDiS / OpenDesk new releases or deployment statistics
- [ ] GAIA-X Trust Framework updates and Data Space implementation progress
- [ ] New security advisories affecting stack components (CVE watch: Keycloak, Nextcloud, Matrix)
- [ ] UN E-Government Survey (biannual; next edition: 2024)
- [ ] GovStack specification updates (ITU/DIAL)
