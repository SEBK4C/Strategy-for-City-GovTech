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
| E-government theory (Wirtz/Weyerer, Janowski) | Medium | Covered | No post-2022 literature on 4th-gen e-gov |
| Lathrop & Ruma foundational framework | High | NEW in v0.2.0 | |
| Swiss EMBAG and federal digital strategy | High | Covered | Cantonal implementation data |
| Swiss nFADP (new data protection law) | High | NEW in v0.2.0 | |
| German OZG / OZG 2.0 | High | Covered | Municipal uptake statistics |
| Sovereign Cloud Stack | High | Covered | Production metrics |
| Open Source in EU public administration (OSOR) | High | NEW in v0.2.0 | |
| Identity management (Keycloak, BundID, eID) | Medium | Covered | BundID uptake data (URL unverified) |
| Decidim / participatory platforms | High | Expanded in v0.2.0 | |
| CONSUL Democracy | Medium | NEW in v0.2.0 | |
| Matrix/Element for government | Medium | Covered | BundesMessenger adoption data |
| Nextcloud for government | Medium | Covered | Swiss federal deployment details |
| Open data portals (CKAN) | Medium | Covered | |
| DCAT-AP 3.0 | High | NEW in v0.2.0 | |
| GIS for municipalities | Low | Covered | No academic literature cited |
| Procurement frameworks | Medium | Expanded in v0.2.0 | |
| Total cost of ownership methodology | High | NEW in v0.2.0 — Section 9 | Need peer-reviewed TCO studies |
| User experience / satisfaction research | Low | Appendix B framework created | No peer-reviewed studies found |
| Small municipality case studies | Medium | Schaffhausen added v0.2.0 | Need more <50k cases |
| Change management in IT transitions | Medium | Munich LiMux expanded | No cross-case comparative studies |
| GovStack (ITU/DIAL building blocks) | High | NEW in v0.2.0 | |
| EU Data Act 2023 | High | NEW in v0.2.0 | |
| EU AI Act 2024 | High | NEW in v0.2.0 | |
| ZenDiS | High | NEW in v0.2.0 | |
| OpenDesk | High | Expanded in v0.2.0 | |
| eCH standards (Switzerland) | High | NEW in v0.2.0 | |
| OSOR Annual Report | High | NEW in v0.2.0 | |
| GAIA-X | Medium | NEW in v0.2.0 | |
| French LibreOffice migration | High | NEW in v0.2.0 | Primary source URL unverified |
| Munich LiMux post-mortem | High | NEW in v0.2.0 | Primary council document unverified |
| Decidim Social Contract | Medium | NEW in v0.2.0 | |
| XÖV 3.0 | Medium | NEW in v0.2.0 | |

### Not yet covered (v0.3.0 targets)

- **Swiss E-ID technical implementation** (post-2023 referendum; W3C DID/VC architecture)
- **EUCS (EU Cybersecurity Certification Scheme)** — cloud security certification alignment with SCS
- **Digital Services Act / Digital Markets Act** — interaction with municipal procurement
- **OpenDesk v2.x** (2025/2026 updates beyond v0.2.0 coverage)
- **Swiss OGD Strategy 2024–2027** (cantonal implementation specifics)
- **Academic peer-reviewed TCO study** — commission or locate if published 2024–2026
- **Citizen satisfaction research** — peer-reviewed comparison OSS vs. proprietary municipal services
- **Gasser et al. (2010)** — academic peer-reviewed LiMux analysis
- **PRINCE2/IPMA in public-sector OSS projects** — project management methodologies
- **BITV 2.0 accessibility standard** — German accessibility framework for public-sector IT

---

## Gaps closed in v0.2.0

All gaps marked as "open" in v0.1.0 have been addressed:

| Gap (from v0.1.0) | Resolution |
|---|---|
| eCH standards not covered | [31] added; Section 3.5 expanded |
| CONSUL Democracy not covered | [28] added; Section 3.9 expanded |
| GovStack not covered | [15] added; Section 3.3 created |
| EU Data Act not covered | [17] added; Section 3.7 created |
| ZenDiS under-covered | [18] added; Sections 3.2, 8.3 expanded |
| Lathrop & Ruma not cited | [25] added; Section 3.1 expanded |
| OSOR annual report not integrated | [32] added; Section 3.6 created |
| GAIA-X status unclear | [48] added; Sections 4.6, 4.9 expanded |
| French LibreOffice migration missing | [38] added; Section 8.4 created |
| Munich LiMux referenced but shallow | [40] added; Sections 7.2, 8.5 expanded |
| Swiss nFADP missing | [47] added; Sections 3.2, 7.4 expanded |
| OpenDesk 2024 updates missing | [49] added |
| Decidim Social Contract not cited | [50] added; Section 3.9 expanded |
| BundID details missing | [51] added (URL unverified); Section 4.1 expanded |
| XÖV 3.0 framework not cited | [52] added |
| EU AI Act not covered | [53] added; Sections 3.8, 4.10 created |
| DCAT-AP 3.0 not cited | [54] added; Sections 4.6, 6.2 expanded |
| TCO methodology absent | Section 9 created; Appendix A revised |
| Small municipality data weak | Schaffhausen case study added (Section 8.2) |
| User experience research absent | Appendix B framework created |

---

## Critical gaps (still open)

### Rigorous independent TCO studies
No independent peer-reviewed comparative Total Cost of Ownership studies cover the full
open-source vs. proprietary municipal stack. Available studies are vendor-commissioned,
context-specific, or methodologically inconsistent. The TCO methodology in Section 9 is
a proposed framework; it needs validation by independent researchers or auditors.
**Target:** Commission or locate for v0.3.0; alternatively partner with a research
institution to run the first validated study.

### Peer-reviewed citizen satisfaction research
Almost no peer-reviewed literature exists comparing citizen satisfaction with
open-source vs. proprietary municipal digital services. The Appendix B survey framework
addresses this as a tool for collecting primary data; actual results will only exist
after municipalities implement and publish findings.
**Target:** Identify municipalities running the Appendix B survey; aggregate findings
for v1.0.0.

### Small-municipality longitudinal data
Most case studies still involve large cities or federal agencies. The median EU
municipality has population <10,000. Schaffhausen (83,000) is a useful data point
but not a median municipality.
**Target:** Document 3–5 case studies of municipalities <50,000 for v0.3.0.

---

## Improvement log

| Date | Action | By | Result |
|---|---|---|---|
| 2026-06-20 | Initial literature review, v0.1.0 draft | SG | 30 primary sources identified; 46 citation slots in papers |
| 2026-06-21 | v0.2.0 citation completion round | AI-assisted | 17 new sources added ([15],[17],[18],[25],[28],[31],[32],[38],[40],[47],[48],[49],[50],[51],[52],[53],[54]); 6 case studies written; TCO section created; AI Act section created; total citations: 54 |

---

## Quarterly review checklist

When running `Scripts/update_literature_review.py`, check for:

- [ ] New Swiss e-government legislation or strategy updates
- [ ] New German OZG implementation reports or FITKO publications
- [ ] New EU legislation (AI Act implementation, Data Act compliance guidance, etc.)
- [ ] New Sovereign Cloud Stack releases or governance updates
- [ ] New openCode.de statistics or case studies
- [ ] New academic papers on e-government maturity (GIQ, ISM, EJEG)
- [ ] New municipal open-source deployments or case studies
- [ ] New security advisories affecting stack components
- [ ] OSOR annual report (EU Open Source Observatory, annual)
- [ ] UN E-Government Survey (biannual)
- [ ] OpenDesk version updates (quarterly releases)
- [ ] ZenDiS publications or programme updates
- [ ] eCH or XÖV standard updates
- [ ] GAIA-X data space progress (significant developments)
- [ ] DCAT-AP updates (SEMIC releases)
- [ ] Verify all [unverified] sources in source-registry.md
