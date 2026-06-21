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

| Domain | Depth | Status | Change from v0.1.0 |
|---|---|---|---|
| E-government theory (Wirtz/Weyerer, Janowski, Mergel) | Medium | ✔ | Added Mergel et al. 2019 |
| Digital sovereignty theory (Frischmann, Eghbal, Chesbrough, Zittrain) | Medium | ✔ | New: 4 foundational sources added |
| Swiss EMBAG and federal digital strategy | High | ✔ | Added DVS reference |
| Swiss nDSG (revised data protection law) | High | ✔ | **New** |
| Swiss eID (BGEID, SSI architecture) | Medium | ✔ | **New** |
| eCH standards (Swiss XML interoperability) | Medium | ✔ | **New** |
| German OZG / OZG 2.0 | High | ✔ | Added FITKO, AKDB, DigitalService refs |
| Sovereign Cloud Stack | High | ✔ | Stable from v0.1.0 |
| govdigital eG | Medium | ✔ | Stable |
| ZenDiS (German Centre for Digital Sovereignty) | Medium | ✔ | **New** |
| OSOR (EU Open Source Observatory) | Medium | ✔ | **New** |
| Open Source in EU public administration (OSOR study) | Medium | ✔ | Added Blind et al. 2021 |
| Identity management (Keycloak, BundID, eID) | Medium | ✔ | eID now covered |
| Decidim / participatory platforms | High | ✔ | Stable |
| CONSUL Democracy platform | Medium | ✔ | **New** |
| GovStack (ITU/DIAL building blocks) | Medium | ✔ | **New** |
| Matrix/Element for government | Medium | ✔ | BundesMessenger referenced |
| CryptPad (E2E collaboration) | Medium | ✔ | **New** |
| Collabora Online (browser office) | Medium | ✔ | **New** |
| OpenSlides (council management) | Medium | ✔ | **New** |
| Forgejo (code hosting) | Medium | ✔ | **New** |
| Nextcloud for government | Medium | ✔ | Stable |
| Open data portals (CKAN) | Medium | ✔ | DCAT-AP added |
| GIS for municipalities | Medium | ✔ | INSPIRE compliance added |
| Procurement frameworks (GWB, VgV, BöB, IVöB) | Medium | ✔ | **New** |
| TCO evidence (Blind et al., Gartner/OSOR, French Gendarmerie) | Medium | ✔ | **New** (was CRITICAL GAP) |
| Accessibility (EN 301 549, WCAG 2.1, BITV 2.0, eCH-0059) | Medium | ✔ | **New** |
| EU Data Act 2023 | Low | ✔ | **New** |
| Security (BSI IT-Grundschutz, NIS2, ISO 27001) | Medium | ✔ | Consolidated |
| Munich LiMux post-mortem | Medium | ✔ | Deepened with evaluation source |
| FUD analysis (Halloween Documents) | Low | ✔ | **New** |
| Austrian OSS strategy | Low | ✔ | **New** (comparative) |
| Change management (Mergel et al.) | Medium | ✔ | **New** |
| User experience / satisfaction research | Absent | ⚠ | **Still a gap** |
| Small municipality case studies | Low | ⚠ | **Still a gap (partially)** |

### Still not covered / planned for v0.3.0

- **Longitudinal UX studies** post-migration: peer-reviewed, large-sample
- **Accessibility performance benchmarks**: OSS vs. proprietary government portals (no comparative studies found)
- **Small-municipality data** (< 5,000 inhabitants): only anecdotal; no systematic case studies
- **OpenDesk v2.x** (2025/2026): current deployment statistics and municipal access framework
- **GAIA-X practical tools** (2025 state of play for municipalities)
- **Austrian e-government** depth (only high-level via [65])
- **Cantonal implementation data** for EMBAG

---

## Gap register (v0.2.0 close-out)

### Gap resolved: TCO studies
- **Status:** Resolved (partially)
- **Resolution:** Added EC Blind et al. (2021) [8], Gartner/OSOR TCO summary [9], French
  Gendarmerie migration as empirical data point (research-notes), Vinnova Sweden [35],
  Lathrop & Ruma [36] for political economy framing. Indicative model in Section 3.6.
- **Remaining:** No single rigorous comparative study for DACH-region municipalities exists.
  Need: commission an independent municipal TCO study or identify forthcoming academic work.

### Gap resolved: eCH standards
- **Status:** Resolved
- **Resolution:** eCH overview [27] added; key standards cited inline (eCH-0059, eCH-0070,
  eCH-0175, eCH-0229, eCH-0014). Will need individual standard entries as paper matures.

### Gap resolved: CONSUL
- **Status:** Resolved
- **Resolution:** [30] CONSUL Democracy platform added; Section 4.8 covers CONSUL vs. Decidim
  comparison with full scoring matrix.

### Gap resolved: GovStack
- **Status:** Resolved
- **Resolution:** [7] GovStack ITU/DIAL added; referenced in Sections 3.5 and 6.2.

### Gap resolved: ZenDiS
- **Status:** Resolved
- **Resolution:** [4] ZenDiS GmbH added; detailed coverage in Section 3.2.

### Gap resolved: OSOR Annual Report
- **Status:** Resolved
- **Resolution:** [5] OSOR added as institutional source; OSOR 2023 study on OSS in public
  sector cited in Section 3.2.

### Gap open: User experience research
- **Status:** Open — target v0.3.0 or v1.0.0
- **Action:** Design a citizen-satisfaction survey framework for participating municipalities.
  Consider partnering with academic institution.

### Gap open: Small-municipality case studies
- **Status:** Partially open — target v0.3.0
- **Action:** Document 3–5 case studies of municipalities < 50,000 that completed OSS
  transitions. Leads: Schaffhausen (CH), small Bavarian municipalities via AKDB.

---

## Improvement log

| Date | Action | By | Result |
|---|---|---|---|
| 2026-06-20 | Initial literature review, v0.1.0 draft | SG | 30 primary sources identified; 46 citation slots in papers |
| 2026-06-20 | v0.2.0 literature expansion | SG | 65 citations; added eCH, nDSG, eID, CONSUL, GovStack, ZenDiS, OSOR, EU Data Act, CryptPad, Collabora, OpenSlides, Forgejo, LiMux evaluation, FUD analysis, accessibility frameworks, procurement law (GWB/VgV/BöB), DSGVO/BDSG, ISO 27001 |

---

## Quarterly review checklist

When running `Scripts/update_literature_review.py`, check for:

- [ ] New Swiss e-government legislation or strategy updates
- [ ] New German OZG implementation reports or FITKO publications
- [ ] New EU legislation (Data Act implementing acts, AI Act implementation, etc.)
- [ ] New Sovereign Cloud Stack releases or governance updates
- [ ] New openCode.de statistics or case studies
- [ ] New academic papers on e-government maturity (GIQ, ISM, EJEG)
- [ ] New municipal open-source deployments or case studies
- [ ] New security advisories affecting stack components
- [ ] OSOR annual report (EU Open Source Observatory, annual)
- [ ] UN E-Government Survey (biannual)
- [ ] eCH new/revised standards (quarterly publication cycle)
- [ ] ZenDiS OpenDesk updates and deployment statistics
- [ ] GovStack new building block specifications
- [ ] Bertelsmann Stiftung / KGSt municipal IT reports
- [ ] BfDI cloud guidance updates
- [ ] Cantonal EMBAG implementation regulations (CH)
