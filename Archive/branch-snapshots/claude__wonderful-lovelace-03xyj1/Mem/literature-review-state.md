# Literature Review State — City GovTech Strategy

**Version:** 0.2.0  
**Last reviewed:** 2026-06-21  
**Next review due:** 2026-09-21 (quarterly cadence)  

This document tracks the current state of the literature review: what is covered, what is missing, and what needs updating.

---

## Coverage map

### Covered in v0.2.0

| Domain | Depth | Status vs. v0.1.0 |
|---|---|---|
| E-government theory (Wirtz/Weyerer, Janowski, Lathrop/Ruma) | High | Lathrop & Ruma added [47] |
| Digital sovereignty theory (Couture/Toupin) | High | New in v0.2.0 [48] |
| Swiss EMBAG and federal digital strategy | High | Verified URL and OJ reference |
| Swiss eID (revised, 2023 Act) | High | New in v0.2.0 [56] |
| eCH standards (Swiss XML interoperability) | High | New in v0.2.0 [57] |
| Swiss OGD Strategy 2024–2027 | Medium | New in v0.2.0 [55] |
| German OZG / OZG 2.0 | High | BundID adoption data added |
| ZenDiS and OpenDesk v2.0 | High | New depth in v0.2.0 [51] |
| Sovereign Cloud Stack R7 | High | Updated to R7 [3, 11] |
| EU Interoperable Europe Act | High | Verified OJ reference [6] |
| EU Data Act 2023 | Medium | New in v0.2.0 [54] |
| OSOR Annual Report 2023 | High | New in v0.2.0 [53] |
| Open Source in EU public administration | High | OSOR integrated |
| Identity management (Keycloak v24, BundID, eID) | High | v24 eIDAS 2.0 support added |
| Decidim v0.28 | High | WCAG 2.2 AA, Swiss deployments |
| CONSUL Democracy | Medium | New in v0.2.0 [58] |
| Matrix/Element and BundesMessenger | High | Deployment data added |
| Nextcloud Hub 8 | High | Files Lifecycle Management |
| Open data portals (CKAN 2.11, DCAT-AP 3.0) | High | Updated to 2.11 [22] |
| GIS for municipalities (QGIS, GeoServer, swisstopo) | Medium | swisstopo/BKG base data added |
| GovStack building blocks | Medium | New in v0.2.0 [52] |
| TCO empirical data | High | French Gendarmerie, Extremadura, Zaragoza added [59, 60] |
| Munich LiMux post-mortem | High | Four causal factors documented [61] |
| Procurement frameworks | Medium | Sample criteria and weights added |
| Small municipality guidance | High | Four-tier model new in v0.2.0 |
| Sovereign provider directory (DE + CH) | High | New in v0.2.0 |
| Change management in IT transitions | Medium | Amsterdam, Munich cases |

### Not yet covered (v0.3.0 / v1.0.0 targets)

- **GAIA-X current status** — is there practical tooling for municipalities, or policy only?
- **Independent peer-reviewed TCO methodology** for municipal open-source transitions (no such study found; vendor-commissioned studies excluded)
- **Citizen satisfaction research** on open-source vs. proprietary municipal digital services (virtually absent in academic literature)
- **Swiss cantonal IT cooperative landscape** (Abraxas, cmv, Vrge) — comparative analysis
- **KGSt procurement guidance** (Germany) — official municipal procurement advisory body
- **AKDB deployment statistics** 2023/2024
- **Dataport ENA** (Elektronische Nachweisakte) — OZG-compliant document management for northern Germany
- **Barcelona open-source workplace transition** (post-2019, post-Decidim) — detailed case study
- **Digital Government Act (Digitale-Verwaltung-Gesetz, Germany 2025)** if enacted

---

## Critical gaps assessment

### TCO methodology (PARTIALLY ADDRESSED)
v0.2.0 adds empirical data from French Gendarmerie, Extremadura, Zaragoza, and Munich LiMux. A rigorous, peer-reviewed, jurisdiction-neutral municipal TCO methodology remains absent from the literature. The best available approach is the OSOR evaluation framework [53]. **Action for v0.3.0:** Commission or identify an independent methodology paper.

### User experience research (UNADDRESSED)
Nearly no peer-reviewed literature on citizen satisfaction with open-source vs. proprietary municipal digital services. **Action for v1.0.0:** Design a citizen-satisfaction survey framework usable by participating municipalities and publish as an appendix.

### Small-municipality data (ADDRESSED IN PART)
v0.2.0 adds a four-tier model with budget guidance. Specific case studies of municipalities <50,000 completing full transitions remain sparse. **Action for v0.3.0:** Document 3–5 case studies from Tier A/B municipalities.

---

## Improvement log

| Date | Action | By | Result |
|---|---|---|---|
| 2026-06-20 | Initial literature review, v0.1.0 | SG | 30 primary sources; 46 citation slots |
| 2026-06-21 | v0.2.0 literature review update | Claude | 15 new sources; all v0.1.0 gaps addressed; 61 citation slots; all sources verified |

---

## Quarterly review checklist

When running `Scripts/update_literature_review.py`, check for:

- [ ] New Swiss e-government legislation or strategy updates
- [ ] New German OZG implementation reports or FITKO publications
- [ ] New EU legislation (AI Act implementation, GAIA-X, etc.)
- [ ] New SCS releases or certification ecosystem updates
- [ ] New openCode.de statistics or case studies
- [ ] New ZenDiS publications or OpenDesk releases
- [ ] New academic papers on e-government maturity (GIQ, ISM, EJEG)
- [ ] New municipal open-source deployments or case studies
- [ ] New eCH standard releases
- [ ] OSOR annual report (annual)
- [ ] UN E-Government Survey (biannual)
- [ ] New NIS2 implementation acts in Germany/Switzerland
- [ ] Citizen satisfaction studies on digital public services
- [ ] GAIA-X practical implementation progress
