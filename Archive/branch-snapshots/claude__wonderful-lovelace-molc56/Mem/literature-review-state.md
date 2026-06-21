# Literature Review State — City GovTech Strategy

**Version:** 0.2.0  
**Last reviewed:** 2026-06-21  
**Next review due:** 2026-09-21 (quarterly cadence)  

This document tracks the current state of the literature review: what is covered, what is
missing, and what needs updating. It is the primary input to
`Scripts/update_literature_review.py`.

---

## Coverage map

### Covered and verified (v0.2.0)

| Domain | Depth | Status | Key remaining gaps |
|---|---|---|---|
| E-government theory (Wirtz/Weyerer, Janowski) | High | ✅ Verified | Post-2022 literature thin |
| Swiss EMBAG and federal digital strategy | High | ✅ Verified | Cantonal implementation data sparse |
| German OZG / OZG 2.0 | High | ✅ Verified | Municipal uptake statistics limited |
| ZenDiS and German digital sovereignty | High | ✅ Added v0.2.0 | Annual report 2024 not yet available |
| Sovereign Cloud Stack | High | ✅ Verified | Production metrics not yet published |
| EU Data Governance Act (2022) | High | ✅ Added v0.2.0 | Municipal DGA compliance guidance sparse |
| EU Data Act (2023) | High | ✅ Added v0.2.0 | Implementing acts not yet published |
| EU AI Act (2024) | High | ✅ Added v0.2.0 | Delegated acts and implementing regulations pending |
| Interoperable Europe Act (2024) | High | ✅ Verified | Board first report not yet available |
| Open Source in EU public administration | Medium | ✅ Verified | OSOR 2024 report not yet available |
| GovStack building blocks | Medium | ✅ Added v0.2.0 | Reference implementation v2 pending |
| eCH standards (Switzerland) | High | ✅ Added v0.2.0 | Individual standard documents not individually registered |
| Identity management (Keycloak, BundID, eID) | High | ✅ Verified | Swiss E-ID not yet in force |
| eIDAS 2.0 / EU Digital Identity Wallet | Medium | Partial | Implementing acts pending |
| Decidim / participatory platforms | High | ✅ Verified | Schaffhausen case study needs primary data |
| CONSUL Democracy | Medium | ✅ Added v0.2.0 | No comparative Decidim/CONSUL study found |
| Matrix/Element for government | Medium | ✅ Verified | BundesMessenger adoption data not public |
| Nextcloud for government | High | ✅ Verified | Swiss federal deployment details limited |
| OpenDesk | High | ✅ Verified | v2.x update documentation pending |
| Open data portals (CKAN) | High | ✅ Verified | DGA compliance implementation details |
| GIS for municipalities | Medium | ✅ Improved v0.2.0 | No academic literature found; grey lit used |
| Procurement frameworks | Medium | ✅ Improved v0.2.0 | No comparative EU municipal procurement studies |
| Total cost of ownership | High | ✅ Added v0.2.0 | No longitudinal study >5 years; vendor-neutral studies sparse |
| User experience / satisfaction | Low | ⚠️ Partial | CRITICAL GAP: no peer-reviewed citizen satisfaction studies |
| Small municipality case studies | Medium | ✅ Added v0.2.0 | Only 3 cases documented; need broader sample |
| Change management in IT transitions | Medium | ✅ Improved v0.2.0 | Munich LiMux used; need positive comparative cases |
| AI-assisted government services | Medium | ✅ Added v0.2.0 | Empirical AI Act compliance cost data absent |
| Supply chain security (SBOM) | Medium | ✅ Added v0.2.0 | Government-specific SBOM practice guidance sparse |
| Climate / sustainability of municipal IT | Low | Mentioned | No cited primary study on municipal ICT carbon |
| GAIA-X | Medium | ✅ Added v0.2.0 | Label adoption rates not documented |
| FITKO framework | High | ✅ Verified | Annual report URL confirmed |
| openCode.de | High | ✅ Verified | Updated repository count (500+ as of mid-2026) |

### Still not covered (target v1.0)

- **EU Cyber Resilience Act (CRA)**: implications for SBOM and open-source dependency management
- **EUCS (EU Cloud Certification Scheme)**: ENISA scheme; impacts SCS certification claims
- **Swiss E-ID Act (post-entry into force)**: integration architecture with cantonal services
- **eIDAS 2.0 implementing acts**: European Digital Identity Wallet architecture reference implementation
- **OSOR Annual Report 2024**: EU Open Source Observatory (annual publication)
- **UN E-Government Survey 2024**: biannual; covers post-2022 developments
- **Interoperable Europe Board first annual report**: expected 2025
- **GovStack Reference Implementation v2.0**: expected 2026
- **Longitudinal municipal TCO study**: 5+ year data with consistent methodology
- **Citizen satisfaction RCTs**: randomised comparison of open-source vs. proprietary service interfaces

---

## Critical gaps (residual after v0.2.0)

### User experience research (CRITICAL)
No randomised or quasi-experimental studies compare citizen satisfaction with open-source
vs. proprietary municipal digital services. Available evidence is anecdotal or
vendor-commissioned. **Action for v1.0:** design a citizen-satisfaction survey instrument
and coordinate deployment across 3–5 municipalities implementing the recommended stack.
Target instrument: adapted GDS Service Standard satisfaction framework.

### Longitudinal TCO data (CRITICAL)
The longest TCO comparison available (Munich LiMux) covers ~14 years but was not
methodologically designed as a TCO study. The DINUM study covers only 4 years. No study
tracks a full open-source municipal stack with consistent, independent methodology over
5+ years. **Action for v1.0:** develop a TCO tracking template and deploy with
municipal partners beginning in Phase 1.

### AI Act compliance costs
No empirical data exists on the cost and timeline of AI Act conformity assessment for
municipalities deploying AI systems under Annex III. **Action for v1.0:** interview
2–3 municipalities or Länder agencies that have undergone AI Act assessment.

---

## Improvement log

| Date | Action | By | Result |
|---|---|---|---|
| 2026-06-20 | Initial literature review, v0.1.0 draft | SG | 30 primary sources identified; 46 citation slots |
| 2026-06-21 | Gap-filling review for v0.2.0 | SG / Claude | 18 new sources added (IDs 47–63); 8 gaps closed; 3 critical gaps remaining |

---

## Quarterly review checklist

When running `Scripts/update_literature_review.py`, check for:

- [ ] New Swiss e-government legislation or strategy updates (fedlex.admin.ch, egovernment.ch)
- [ ] New German OZG implementation reports or FITKO publications (fitko.de)
- [ ] New ZenDiS publications or openCode.de statistics (zendis.de, opencode.de)
- [ ] New EU legislation or implementing acts (EUR-Lex: Data Act, AI Act, CRA, eIDAS 2.0)
- [ ] Interoperable Europe Board publications (joinup.ec.europa.eu)
- [ ] New Sovereign Cloud Stack releases or governance updates (scs.community)
- [ ] New academic papers on e-government maturity (GIQ, ISM, EJEG, Gov Inf Q)
- [ ] New municipal open-source deployments or case studies (opencode.de, joinup.ec.europa.eu)
- [ ] New security advisories affecting stack components (CVE feeds, BSI)
- [ ] OSOR annual report (EU Open Source Observatory, annual: joinup.ec.europa.eu/collection/open-source-observatory-osor)
- [ ] UN E-Government Survey (biannual: publicadministration.un.org)
- [ ] GAIA-X Label adoption statistics (gaia-x.eu)
- [ ] EU AI Act delegated acts and implementing regulations (EUR-Lex)
- [ ] Swiss E-ID Act progress and implementing regulations (fedlex.admin.ch)
