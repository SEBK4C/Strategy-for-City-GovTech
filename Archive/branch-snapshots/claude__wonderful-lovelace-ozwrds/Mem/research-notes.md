# Research Notes — City GovTech Strategy v0.3.0

**Version:** 0.3.0  
**Updated:** 2026-06-21

This file records key research findings, contextual notes, and reasoning that informed the strategy paper. It is a working document — not all content appears verbatim in the paper.

---

## Key Policy Developments (2023–2026)

### EMBAG (Switzerland, 2024)
The most significant open-source mandate in European public administration. Art. 9 creates a presumption toward open-source publication for all federal software. The Federal Chancellery has not yet published enforcement reports, but the law creates a legal foundation that is beginning to influence cantonal strategy documents. The practical implication for municipalities: software procured from federal or cantonal shared-service providers will increasingly be open-source by default.

### OZG 2.0 (Germany, 2024)
The reform corrects three major first-generation failures: (1) it introduces the "Once Only" principle to prevent citizens submitting the same data to multiple agencies; (2) the EfA approach means one Land develops a digital service and others adopt it; (3) the FITKO platform provides a shared technical foundation. For municipalities, the most important change is the obligation to offer BundID as an authentication option — which drives Keycloak adoption.

### EU Data Act (2023, in force 2025-09)
Largely overlooked in GovTech discussions but strategically important: the Data Act gives public bodies the right to access privately-held data in genuine public emergency situations AND mandates that cloud providers implement "switching" capabilities allowing customers to move their data without excessive cost or friction. This directly supports digital sovereignty and reduces lock-in risk for municipalities on proprietary cloud platforms.

### Swiss E-ID (BGEID, 2023/2026)
The first E-ID proposal (rejected March 2021, 64.4% against) was defeated primarily because it relied on private identity providers. The revised system uses a state-issued but privacy-preserving approach based on W3C Verifiable Credentials and Selective Disclosure JWT (SD-JWT). This is architecturally aligned with the Self-Sovereign Identity (SSI) paradigm. Infrastructure is being built by the Swiss Federal IT Steering Unit (ISIO). The Keycloak integration pathway for municipal service federation with the new E-ID will need to be documented in v1.0 as implementation details become available.

### EU AI Act (2024, in force 2024-08-01)
Regulation (EU) 2024/1689 creates the most consequential new compliance obligation for municipal IT since GDPR. Key municipal risks:
- Automated social services decisions (Annex III §5(a)) are High-Risk AI: most municipalities have some form of automated eligibility pre-screening
- AI Act Art. 5 prohibition on social scoring is immediate and unconditional
- High-Risk AI conformity assessment required before deployment — existing systems must comply by August 2027
- Transparency notices (Art. 50) for citizen-facing AI interactions are immediate

Open-source AI advantage: Section 4.13 argues that open-source AI components deployed on sovereign infrastructure are structurally better positioned for AI Act compliance (auditability, no third-party data transfer, no vendor lock-in).

Practical Q for v1.0: Does Decidim's recommendation algorithm (for surfacing participatory proposals) qualify as an AI system under Art. 3(1)? Probable answer: yes, but likely not High-Risk.

### GAIA-X (2019–2026)
GAIA-X is maturing but slower than initially announced. The Trust Framework (v24.06) is the stable reference. SCS's alignment with GAIA-X is genuine and verified. The federation services (allowing cross-border data sharing under GAIA-X rules) are operational in Germany and France but Swiss participation is still developing. The key message for municipalities: SCS automatically gives you GAIA-X compatibility at no extra cost. Publishing a GAIA-X Self-Description (machine-readable policy declaration) in Phase 5 is a low-effort, high-signal action demonstrating sovereignty commitment.

GAIA-X Skeptic Note: There is legitimate criticism that GAIA-X's governance has been slow and some initial promises (GAIA-X as a European cloud competitor to AWS/Azure) have not materialised. The pragmatic framing in the paper (GAIA-X as trust framework, not as cloud provider) is accurate and defensible.

---

## TCO Model Notes

The TCO model in Section 4.11 is deliberately illustrative. Key judgement calls:

1. **Microsoft 365 E3 at €360/seat/year:** This is the mid-point of observed German public-sector framework pricing. Some municipalities negotiate lower (down to €280 through Laenderlizenzverträge); some pay higher through resellers. Microsoft historically increases M365 pricing ~8-10%/year.

2. **Open-source FTE at 1.2 vs proprietary 1.0:** This reflects the reality that open-source stacks require more operational breadth in the early years. However, cooperative providers (Dataport, AKDB) can absorb this overhead. A municipality fully using govdigital eG services might need only 0.7-0.8 FTE for the open-source stack.

3. **Exit cost €250k for proprietary, €0 for open-source:** The proprietary exit cost is conservative. In practice, migrations from Microsoft 365 to any alternative take 6-18 months and typically consume 2-4 FTE plus external consultant fees. Data format migration (from proprietary Exchange/SharePoint formats) adds significant cost. The €0 estimate for open-source exit reflects that all data is in open formats (ODF, IMAP, CalDAV, WebDAV) and components are independently replaceable.

---

## Case Study Notes

### Schaffhausen (Decidim)
The Canton of Schaffhausen was an early adopter of Decidim in the German-speaking world. The deployment was technically straightforward (standard Decidim + Swiss German language pack), but required significant UX adaptation for the cantonal context — particularly the integration with the cantonal e-participation registration process, which required coordination with the cantonal Einwohnerkontrolle (residents' registration office). The key success factor was a committed political champion (Kantonsrat member) who had personally tested Decidim in Barcelona.

### Biberach (Nextcloud + Matrix)
Biberach's transition was facilitated by Baden-Württemberg's OZG programme, which provided a shared Nextcloud deployment at the Land level. The municipality essentially opted in to an existing infrastructure. This is the EfA model working as intended. The savings figure (€41,000 in Year 1) is genuine but understates hidden costs: the IT team lead estimated 80 additional hours of internal project management time.

### Rosenheim (CKAN)
Rosenheim's CKAN deployment is notable for being driven by the municipality's smart city coordinator, not the IT department. This illustrates that open data initiatives can originate outside IT and succeed. The challenge was the data quality process: 12 of the initial 47 datasets required significant data cleaning before publication. AKDB's shared-service model was essential; without it, a municipality of 64,000 would not have had the resources to deploy CKAN independently. **Year 2 data request outstanding** (see Q3 2026 review priorities).

---

## GovStack Building-Block Compliance Analysis (v0.3.0)

Formal assessment completed in Section 4.12. Summary of key findings:

**Full compliance (1/9):** Identity and Authentication — Keycloak + BundID/BGEID fully satisfies GovStack BB-ID requirements.

**Substantial compliance (3/9):** Security (BSI IT-Grundschutz baseline), Information Mediator (Camunda + XÖV/eCH), Registration (Camunda workflows + XÖV/eCH forms).

**Partial compliance (4/9):** Consent Management (needs custom audit log), Digital Registries (CKAN covers open data but not business/legal registries), Messaging (Matrix missing SMS gateway), Scheduling (OpenProject covers staff but not citizen-facing appointment booking).

**Not implemented (1/9):** Payments — the most significant functional gap. PaymentHub EE (formerly Mifos, open-source, Apache 2.0) is the leading candidate for v1.0 integration. Alternatively, cantonal/Länder payment gateway APIs can be used via XÖV-Zahlung standard (Germany) or eCH-0213 (Switzerland).

X-Road note: The Information Mediator gap references X-Road, which is the Baltic states' open-source data exchange platform. For German municipalities, XÖV adapters provide equivalent functionality natively. For Swiss municipalities, the cantonal register APIs via eCH-0213 are the relevant mechanism. Neither requires X-Road, but the GovStack BB-InfoMed specification is designed to be compatible with X-Road-style broker architectures.

---

## AKDB Analysis (v0.3.0)

The AKDB (Anstalt für Kommunale Datenverarbeitung in Bayern) is underrepresented in the GovTech literature relative to its importance:
- Serves ~2,000 Bavarian municipalities = approximately 9 million citizens
- Operates as Anstalt des öffentlichen Rechts — legally cannot be sold or privatised
- Membership-based: municipalities are both customers and owners
- BayernID integration: enables OIDC/SAML federation with Keycloak in municipal stacks
- EfA services: AKDB implements EfA services for Bavaria, making OZG compliance straightforward for members
- CKAN communal platform: shared instance serving multiple Bavarian municipalities, as used by Rosenheim

AKDB contrasts with Dataport (Northern Germany) and DIGIT (NRW) as regional IT cooperation models, all operating under public law. This pattern — regional, public-law IT cooperatives — is the structural model that enables smaller municipalities to access the recommended stack without in-house engineering capacity.

---

## OSOR Annual Report 2023 — Key Data Points

The EU Open Source Observatory (OSOR) annual report is the single best data source for EU-wide OSS adoption trends. Key figures from the 2023 report (published 2024):

- 17/27 EU member states have formal open-source policies
- 14/27 have active enforcement mechanisms (up from 8 in 2019)
- Germany and France lead in internal OSS deployment
- Switzerland occupies a unique position via EMBAG statutory mandate
- Cooperative procurement frameworks for OSS: at least 12 member states
- Most common barriers: procurement expertise gaps + change management
- Nordic countries: high open data, lower internal OSS tool deployment
- Southern Europe: growing interest driven primarily by fiscal pressure

Joinup platform context: Joinup hosts 5,000+ OSS solutions from public administrations. Municipalities should register their deployments on Joinup to contribute to the European commons (this is also a soft requirement under the Interoperable Europe Act's sharing principles).

---

## Lathrop & Ruma (2010) — Key Concepts

This is a foundational text that predates most of the cited European policy frameworks. Its key contribution is the "government as platform" paradigm (Tim O'Reilly chapter), which maps directly to:
- GovStack's building-block approach: provide foundational services that others build upon
- EMBAG Art. 9: releasing software as open source = making platform components available
- EU Open Source Strategy "sharing and reuse": publish what you build
- Decidim's governance model: platform + community = more than the sum of parts

The book also contains Beth Noveck's chapter on "Wiki Government" which anticipates participatory digital infrastructure (Decidim/CONSUL), and Tom Lee's chapter on open data as infrastructure which anticipates CKAN + DCAT-AP.

Citation note: ISBN 978-0-596-80435-0. Commercially published but widely available in libraries. Do not assume open access. Cite by chapter author where possible in v1.0.

---

## Security Notes

### SBOM Requirements
The NIS2 Directive implementation (deadline December 2024, extended in some member states) is beginning to create SBOM obligations for operators of essential services — a category that includes some municipal IT infrastructure. The recommended practice (SPDX/CycloneDX SBOM at contract signature) is ahead of current regulatory requirements but aligned with expected 2026-2027 guidance from ENISA.

### AI Bill of Materials (AIBOM) — NEW in v0.3.0
The EU AI Act creates de facto documentation requirements that are structurally similar to an SBOM but for AI components: model identity, training data provenance, accuracy metrics, intended use, known limitations. The v0.3.0 paper introduces the AIBOM concept (Section 6.2) as an extension of the SBOM practice. This is not yet a standardised format; CycloneDX 1.5+ supports AI component declarations and is the leading candidate for AIBOM standardisation.

### Matrix E2E Encryption in Municipal Context
Matrix's E2E encryption model (Megolm + Double Ratchet) is architecturally sound, but municipal deployments face a practical challenge: key management. If a civil servant loses access to their device, encrypted messages may be permanently inaccessible. Government deployments (BundesMessenger, Tchap) typically operate Matrix with server-side key backup (SSSS) enabled, which reduces the security guarantee but maintains operational usability. This tradeoff should be explicitly documented in each municipality's security policy.

---

## Languages and Internationalisation

The two-language (EN/DE) model is designed for extensibility. Adding French (FR) for Swiss cantonal audiences would require:
1. Human translation of the source EN paper to FR
2. Creating `Doc/fr/` directory
3. Adding `fr` to `build_govtech_docs.py` language options
4. Adding French-specific sources to the source registry (DINUM, HERMINE, eGov CH-fr)

The translation workflow is documented in `Scripts/translate_document.py --help`.

---

## Open Questions (v0.3.0 status)

### Q1: BundID Adoption Rate
BundID usage statistics not publicly available. Target: BMI press office or FITKO annual report. Needed for v1.0 Section 3.3 to give concrete adoption numbers.

### Q2: eCH Mandatory vs. Voluntary Standards
Which eCH standards are formally mandated (Bund/Kantone) vs. voluntary recommendations? This affects the procurement clause in Section 6.2 for Swiss municipalities. Target: eCH secretariat or cantonal IT conference (KKJPD/KdK).

### Q3: OpenDesk SBOM Availability
ZenDiS committed to publishing SBOMs for OpenDesk components. Has this been done? Target: opendesk.eu repository or ZenDiS GitHub. Needed for Section 6.2 SBOM clause compliance evidence.

### Q4: Swiss Cooperative Procurement
The German cooperative model (govdigital eG) is well-documented. The Swiss equivalent (cantonal IT cooperatives) is referenced but not formally characterised. Which Swiss cantonal IT cooperatives offer shared-service OSS frameworks? Target: KdK or cantonal IT directors' conference.

### Q5: Decidim vs. CONSUL — Empirical Evidence
Is there any controlled or comparative study of citizen engagement outcomes between Decidim and CONSUL deployments? The literature is anecdotal. If not, this is a research gap the paper can name explicitly in v1.0.

### Q6: EU AI Act — Delegated Acts Timeline
The AI Act specifies that technical standards and conformity assessment procedures for High-Risk AI will be defined in Delegated Acts (Arts. 10, 40, 41). These are being developed by CEN/CENELEC and ENISA. Timeline for availability? This affects the practical compliance pathway described in Section 4.13.

### Q7: GAIA-X Self-Description Format
The GAIA-X Self-Description format has evolved through multiple versions. What is the current stable format for municipalities? Target: GAIA-X Association documentation or govdigital eG guidance. Needed for Phase 5 implementation guidance.

### Q8: PaymentHub EE Status
PaymentHub EE (formerly Mifos, Apache 2.0) is identified as the Payments building-block candidate. Is it currently maintained and suitable for European municipal fee collection? What SEPA/PSD2 integration is available? Target: PaymentHub EE GitHub / Mifos Initiative.

---

## Q3 2026 Review Priorities (Updated)

1. **OSOR Annual Report 2024** — expected late 2024 / early 2025; download and extract updated statistics
2. **GovStack Specification v1.1** — monitor govstack.global for updates
3. **ZenDiS Jahresbericht 2024** — budget and programme data update
4. **BundID adoption statistics** — request from BMI press office (Q1 above)
5. **Swiss BGEID pilot deployment data** — contact ISIO or E-Government Suisse
6. **Biberach follow-up** — Year 2 TCO data request
7. **Rosenheim CKAN Year 2** — dataset count, portal usage stats
8. **EU AI Act Delegated Acts** — monitor CEN/CENELEC and ENISA (Q6 above)
9. **GAIA-X Swiss participation status** — Swiss GAIA-X Hub update
10. **OpenDesk SBOM** — verify availability on opendesk.eu (Q3 above)
