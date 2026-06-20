---
title: "Sovereign by Design — Appendices v0.2.0"
author: "Sebastian Graf, Autonomous Office of Civil Digital Infrastructure"
version: "0.2.0"
date: "2026-06-20"
language: "en"
source-of-truth: true
SPDX-License-Identifier: "CC-BY-4.0"
---

# Appendices — Sovereign by Design v0.2.0

These appendices accompany `Doc/en/sovereign-by-design-v0.2.0.md`. They provide operational tools: a terminology glossary, a TCO calculation worksheet, and a quarterly literature-review protocol.

---

## Appendix A — Glossary of Key Terms

| Term | Definition | Context |
|---|---|---|
| **AGPL-3.0** | GNU Affero General Public License v3.0. A strong copyleft licence that requires source code disclosure even when software is offered as a network service. | Preferred licence for government SaaS deployments. |
| **AKDB** | Anstalt für Kommunale Datenverarbeitung in Bayern. Bavarian communal IT service provider. | Primary IT broker for Bavarian municipalities. |
| **API** | Application Programming Interface. A defined contract for machine-to-machine communication. | Prerequisite for interoperability between stack components. |
| **BITV 2.0** | Barrierefreie-Informationstechnik-Verordnung. German federal regulation implementing WCAG 2.1 AA for public-sector web services. | Mandatory for German federal digital services; model for Länder/municipalities. |
| **BPMN 2.0** | Business Process Model and Notation 2.0. ISO 19510 standard for graphical workflow modelling. | Required for OZG process automation interoperability. |
| **BSI** | Bundesamt für Sicherheit in der Informationstechnik. German Federal Office for Information Security. | Issues IT-Grundschutz, C5 cloud criteria, security advisories. |
| **BundID** | The German federal citizen identity account. OIDC-based, federated across Länder. | Required integration target for OZG online services. |
| **C5** | Cloud Computing Compliance Criteria Catalogue (BSI). Security baseline for cloud services. | Reference for selecting SCS-certified hosting providers. |
| **CKAN** | Comprehensive Knowledge Archive Network. Open-source data portal platform. | Powers opendata.swiss, data.gov, EU Open Data Portal. |
| **CoP** | Community of Practice. A group of practitioners sharing knowledge and developing expertise collectively. | Inter-municipal open-source cooperation model. |
| **CONSUL** | Open-source citizen participation platform developed in Madrid. AGPL-3.0. | Alternative/complement to Decidim; 40+ country deployments. |
| **CVE** | Common Vulnerabilities and Exposures. Standard identifier for publicly disclosed security vulnerabilities. | Used in patch-management SLA specifications. |
| **DCAT-AP** | Data Catalog Vocabulary — Application Profile. EU metadata standard for open data portals. | Required for CKAN interoperability with GovData.de and EU Open Data Portal. |
| **Decidim** | Open-source participatory democracy platform. AGPL-3.0. Origin: Barcelona. | 400+ global deployments including NYC, Helsinki, Schaffhausen. |
| **Digital sovereignty** | The ability of an organisation to control, audit, and modify its digital systems and data without dependency on single commercial vendors. | Core concept of this strategy. |
| **DMS** | Document Management System. Software for creation, storage, retrieval, and management of digital documents. | Nextcloud is the recommended DMS for municipalities. |
| **DSGVO / GDPR** | Datenschutz-Grundverordnung / General Data Protection Regulation (EU) 2016/679. | Mandatory compliance for all municipal data processing. |
| **DVS** | Digitale Verwaltung Schweiz. Swiss federal-cantonal coordination body for digital administration. | Swiss counterpart to German FITKO. |
| **E2E** | End-to-End encryption. Encryption applied at the sender, decryptable only by the intended recipient. | CryptPad, Matrix/Element provide E2E by default. |
| **eCH** | E-Government Standards Switzerland. Swiss voluntary interoperability standards body. | Swiss equivalent of German XÖV standards. |
| **EfA** | Einer für Alle (One for All). German OZG principle: a service built by one Länder is reusable by all. | Core OZG 2.0 delivery mechanism. |
| **eID** | Electronic Identity. In CH context: the forthcoming state digital identity based on W3C Verifiable Credentials. | BGEID implementation; SSI-based wallet architecture. |
| **EMBAG** | Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben. Swiss federal law (SR 172.019) mandating open-source release of publicly funded software. | Strongest OSS mandate globally at federal level. |
| **ETSI** | European Telecommunications Standards Institute. | Issues EN 301 549 (accessibility standard). |
| **EFA** | European Free and Open Source Software Auditing community. | Security audits of OSS used in EU public administration. |
| **FITKO** | Föderale IT-Kooperation. German federal-Länder IT coordination body for OZG implementation. | Operates FIT-Store; primary OZG technical governance body. |
| **Forgejo** | Community-governed fork of Gitea. Git hosting platform. MIT/GPL-2.0. | Recommended for municipal code and configuration management. |
| **FSFE** | Free Software Foundation Europe. Advocacy organisation for free software. | "Public Money? Public Code!" campaign. |
| **FUD** | Fear, Uncertainty and Doubt. Marketing strategy to discourage adoption of competing products. | See Section 7.3 of main paper. |
| **GAIA-X** | European initiative for a federated, secure cloud infrastructure. | Policy framework; SCS is the technical implementation. |
| **GIS** | Geographic Information System. | QGIS + GeoServer + PostGIS is the recommended open-source GIS stack. |
| **govdigital eG** | German cooperative of public-sector IT providers. | Framework contracts for municipalities; SCS-based cloud operation. |
| **GovStack** | ITU/DIAL initiative specifying reusable digital governance building blocks. | API specifications for Identity, Payments, Registration, etc. |
| **IAM** | Identity and Access Management. Systems for authentication, authorisation, and identity lifecycle. | Keycloak is the recommended IAM platform. |
| **INSPIRE** | Infrastructure for Spatial Information in Europe. EU directive for geodata interoperability. | Mandatory for municipal geodata publication. |
| **IT-Grundschutz** | BSI baseline security methodology. | Mandatory reference for German public-sector IT security. |
| **Keycloak** | Open-source IAM platform. Apache-2.0. Red Hat/CNCF. | Recommended for all municipal identity and SSO needs. |
| **LibreOffice** | Open-source office productivity suite. LGPL-3.0/MPL-2.0. The Document Foundation. | Desktop component; Collabora Online is the server/browser version. |
| **Matrix** | Open decentralised communication protocol. Apache-2.0. | Basis for BundesMessenger (DE), Tchap (FR), UK MoD deployments. |
| **nDSG** | Neues Datenschutzgesetz (CH). Revised Swiss Federal Act on Data Protection (SR 235.1), in force 2023-09-01. | Swiss equivalent of GDPR. |
| **NIS2** | Directive (EU) 2022/2555. Network and Information Security Directive 2. | Extends cybersecurity obligations to municipalities operating critical infrastructure. |
| **OIDC** | OpenID Connect. Authentication layer on top of OAuth 2.0. | Standard protocol for single sign-on; Keycloak implements it natively. |
| **OpenSlides** | Open-source council management and meeting system. MIT. Intevation GmbH. | Recommended for municipal council and committee administration. |
| **OSI** | Open Source Initiative. Body that maintains the Open Source Definition and approves licences. | Reference for licence compliance assessment. |
| **OSOR** | Open Source Observatory. European Commission platform documenting OSS in public administration. | Source for EU-wide deployment statistics. |
| **OZG** | Onlinezugangsgesetz. German Online Access Act (2017, amended 2024). | Legal mandate for digital municipal services. |
| **SAML 2.0** | Security Assertion Markup Language 2.0. Federated identity protocol. | Required for legacy system integration alongside OIDC. |
| **SCS** | Sovereign Cloud Stack. Open-source IaaS/PaaS reference architecture. Apache-2.0. OSBA. | Recommended infrastructure layer for municipalities. |
| **SSI** | Self-Sovereign Identity. Identity model where the user controls their credentials in a wallet. | Architecture of Swiss eID (BGEID). |
| **TCO** | Total Cost of Ownership. Full lifecycle cost including licences, hosting, support, training, migration. | Framework for economic comparison in Section 3.6 and Appendix B. |
| **TYPO3** | Open-source enterprise CMS. GPL-2.0. TYPO3 Association. | Dominant CMS for German-speaking public-sector websites. |
| **VgV** | Vergabeverordnung. German procurement regulation implementing EU directives. | Governs above-threshold public procurement in Germany. |
| **WCAG** | Web Content Accessibility Guidelines. W3C standard (currently v2.1; v2.2 published 2023). | Accessibility baseline for all public-facing digital services. |
| **XÖV** | XML in der öffentlichen Verwaltung. Family of German public-sector XML interoperability standards. | KoSIT-maintained; mandatory for OZG data exchange. |
| **ZenDiS** | Zentrum für Digitale Souveränität der öffentlichen Verwaltung. German federal centre for digital sovereignty. GmbH des Bundes. | Coordinates OpenDesk; key actor for federal/municipal OSS strategy. |

---

## Appendix B — TCO Calculation Worksheet

This worksheet provides a structured method for calculating and documenting Total Cost of Ownership (TCO) when comparing an open-source stack against a proprietary incumbent. Complete one worksheet per scenario.

### B.1 Scenario Parameters

| Parameter | Value |
|---|---|
| Municipality name | ________________ |
| Population | ________________ |
| Number of civil servants in scope | ________________ |
| Analysis period (years) | 5 |
| Discount rate (%) | 3 |
| Calculation date | ________________ |
| Prepared by | ________________ |

### B.2 Incumbent (Proprietary) Costs

**Annual recurring costs (€/year):**

| Category | Current cost (€/yr) | Notes |
|---|---|---|
| Software licences (office productivity) | | |
| Software licences (email/collaboration) | | |
| Software licences (video conferencing) | | |
| Software licences (IAM/SSO) | | |
| Software licences (CMS/web) | | |
| Software licences (other) | | |
| Hosting/cloud fees | | |
| Vendor support contracts | | |
| External IT service contracts | | |
| Internal IT staff (FTE × salary) | | |
| Training (annual refresher) | | |
| **Total annual recurring (A1)** | | |

**One-time costs already sunk (for reference only, not included in future TCO):**

| Category | Historical cost (€) | Notes |
|---|---|---|
| Initial licences/setup | | |
| Past migrations | | |
| Hardware (amortised) | | |

### B.3 Open-Source Stack Costs

**One-time migration costs (€, year 0–1):**

| Category | Estimated cost (€) | Notes |
|---|---|---|
| Discovery and planning (Phase 0) | | |
| Infrastructure setup (Phase 1) | | |
| Core stack deployment (Phase 2) | | |
| Specialist integrations (Phase 3) | | |
| Citizen-facing services (Phase 4) | | |
| Contingency (15%) | | |
| **Total one-time (B0)** | | |

**Annual recurring costs (€/year, years 2–5):**

| Category | Estimated cost (€/yr) | Notes |
|---|---|---|
| Hosting (SCS-certified provider or own RZ) | | |
| Software support contracts (Nextcloud, Collabora, etc.) | | |
| Internal IT staff (FTE × salary) | | |
| External managed services | | |
| Annual training | | |
| Community contributions/upstream sponsorship | | |
| Security audits (annual) | | |
| **Total annual recurring (B1)** | | |

### B.4 Five-Year Net Present Value Calculation

Using discount rate r = 3%:

**Proprietary 5-year PV:**
```
PV_prop = A1 × [(1 - (1+r)^-5) / r]
         = A1 × 4.580
```

**Open-source 5-year PV:**
```
PV_oss = B0 + B1 × [(1 - (1+r)^-4) / r] × (1/(1+r))
       = B0 + B1 × 3.717
```

**Net advantage:**
```
Net advantage = PV_prop - PV_oss
```

| Metric | Value (€) |
|---|---|
| PV_prop | ________________ |
| PV_oss | ________________ |
| **Net 5-year advantage** | ________________ |
| Break-even year | ________________ |
| Annual savings (years 3–5) | ________________ |
| Per-seat annual saving (years 3–5) | ________________ |

### B.5 Non-Quantifiable Benefits (Narrative)

Document qualitative benefits that the TCO model cannot capture:

- **Regulatory alignment:** ________________
- **Vendor independence:** ________________
- **Data protection improvement:** ________________
- **Auditability / democratic accountability:** ________________
- **Interoperability improvements:** ________________
- **Staff skill development:** ________________
- **Community contributions received:** ________________

### B.6 Risk Adjustments

For each high-rated risk in the risk register (Appendix C / Section 7.1), estimate the cost impact and probability:

| Risk ID | Description | Probability | Impact (€) | Expected cost (€) |
|---|---|---|---|---|
| R01 | Skill gaps | | | |
| R03 | Political reversal | | | |
| R05 | Security incident | | | |
| R06 | User resistance | | | |
| **Risk-adjusted total** | | | | |

### B.7 Reporting Template

Summary paragraph for council/management presentation:

> "Over a five-year horizon, migrating [N] civil-servant workstations to an open-source technology stack is projected to deliver a net present value advantage of **€[X]** compared to renewing current proprietary contracts. One-time migration costs of **€[B0]** are recovered by year **[Y]**. Annual savings from year 3 onward are **€[Z]** (€[Z/N] per seat). Non-quantifiable benefits include improved regulatory alignment with EMBAG/OZG 2.0, elimination of third-country data transfer risk, and full auditability of municipal IT systems."

---

## Appendix C — Quarterly Literature Review Protocol

This protocol governs the recurring update of the literature review and source registry. It feeds into `Mem/literature-review-state.md` and is executed by `Scripts/update_literature_review.py`.

### C.1 Review Cadence

| Review type | Frequency | Trigger |
|---|---|---|
| Full quarterly review | Every 3 months | Calendar: March, June, September, December |
| Rapid update | As needed | Major legislation, significant CVE, community governance change |
| Annual deep review | Once per year (December) | Version bump to next minor version |

### C.2 Quarterly Review Checklist

**Regulatory and legislative monitoring:**
- [ ] Swiss Federal Gazette (Bundesblatt) — new ordinances/acts affecting digital government
- [ ] German Bundesanzeiger / BMI publications — OZG progress, IT-Planungsrat decisions
- [ ] EUR-Lex new acts — Digital acts (AI Act impl., Data Act implementing measures, Interoperable Europe Acts)
- [ ] BSI publications — new IT-Grundschutz modules, C5 updates, security advisories
- [ ] eCH — new or revised standards
- [ ] KoSIT — new XÖV standards

**Community and project monitoring:**
- [ ] Nextcloud — new major release, security advisories, government case studies
- [ ] Keycloak — new major release, FIPS/BSI compliance updates
- [ ] Matrix — spec changes, new government deployments
- [ ] Decidim / CONSUL — major releases, new municipal deployments
- [ ] OpenSlides — new releases, council adoption
- [ ] CryptPad — new releases, NGI funding status
- [ ] Forgejo — governance changes, major releases
- [ ] Sovereign Cloud Stack — new releases, new certified providers
- [ ] CKAN — major releases, DCAT-AP compliance updates
- [ ] TYPO3 / Drupal — security releases, accessibility improvements

**Research and reports monitoring:**
- [ ] OSOR — new publications, case studies, annual report
- [ ] ZenDiS — OpenDesk updates, new publications
- [ ] Europ. Commission — Digital Economy and Society Index (DESI), eGovernment Benchmark
- [ ] GovStack — new building block specifications
- [ ] Academic journals: Government Information Quarterly (GIQ), EJEG, ISM — new relevant papers
- [ ] Bertelsmann Stiftung, KGSt — German municipal IT reports
- [ ] Swiss Federal Chancellery / DVS — strategy updates

### C.3 Source Addition Protocol

When adding a new source to `Mem/source-registry.md`:

1. Assign the next sequential ID ([N+1])
2. Complete all metadata fields per the template
3. Set `Verification status: unverified`
4. Add citation to the relevant paper section in a `[DRAFT]` annotation
5. Verify URL is accessible and content matches description
6. Update status to `verified`
7. Remove `[DRAFT]` annotation
8. Update `Mem/literature-review-state.md` coverage map

### C.4 Version Bumping Criteria

| Change type | Version bump |
|---|---|
| Add ≥5 new sources, update ≥2 paper sections | Minor version (e.g., 0.2.0 → 0.3.0) |
| Structural change to paper or major section rewrite | Minor version |
| Fix typos, update URLs, add 1–2 sources | Patch (e.g., 0.2.0 → 0.2.1) |
| Peer-reviewed, externally validated, widely shared | Major version (e.g., 0.x.y → 1.0.0) |

### C.5 Gap-Tracking Template

For each identified gap, record in `Mem/literature-review-state.md`:

```markdown
### Gap: [short name]
- **Domain:** [technology | regulation | case-study | TCO | UX]
- **Severity:** [critical | high | medium | low]
- **Description:** [1–2 sentences]
- **Action:** [what to do to close this gap]
- **Target version:** [e.g., v0.3.0]
- **Assigned:** [name or "unassigned"]
- **Status:** [open | in-progress | resolved]
```

### C.6 Translation Synchronisation

After updating the English source-of-truth document:

1. Run `Scripts/translate_document.py --check-diff` to identify changed sections
2. Update German translation (`Doc/de/`) manually for substantive changes
3. For patch-level changes (URLs, typos), machine-assisted translation with human review is acceptable
4. Bump version in German document's YAML frontmatter to match English
5. Update `changelog` block in both documents

---

*Appendices v0.2.0 · CC-BY-4.0 · Sebastian Graf, Autonomous Office of Civil Digital Infrastructure*
