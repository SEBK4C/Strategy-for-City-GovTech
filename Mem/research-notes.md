# Research Notes — City GovTech Strategy v0.2.0

**Version:** 0.2.0  
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
The first E-ID proposal (rejected March 2021, 64.4% against) was defeated primarily because it relied on private identity providers. The revised system uses a state-issued but privacy-preserving approach based on W3C Verifiable Credentials and Selective Disclosure JWT (SD-JWT). This is architecturally aligned with the Self-Sovereign Identity (SSI) paradigm. Infrastructure is being built by the Swiss Federal IT Steering Unit (ISIO). The Keycloak integration pathway for municipal service federation with the new E-ID will need to be documented in v0.3.0 as implementation details become available.

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
Rosenheim's CKAN deployment is notable for being driven by the municipality's smart city coordinator, not the IT department. This illustrates that open data initiatives can originate outside IT and succeed. The challenge was the data quality process: 12 of the initial 47 datasets required significant data cleaning before publication. AKDB's shared-service model was essential; without it, a municipality of 64,000 would not have had the resources to deploy CKAN independently.

---

## GovStack Analysis

GovStack's building-block framework is directly applicable to the recommended stack:

| GovStack Building Block | Recommended Component | Gap |
|---|---|---|
| Identity and Verification | Keycloak + BundID/Swiss E-ID | GovStack API spec not yet verified |
| Consent Management | Nextcloud Privacy Dashboard | Partial; full BB spec not covered |
| Registration | Custom (Camunda/Flowable) | Mapping needed |
| Messaging | Matrix/Element | Partial; BB spec is SMS/push-oriented |
| Scheduling | OpenProject | Partial |
| Payments | Not in current stack | Gap; relevant for municipal fees |

A formal GovStack compliance mapping should be conducted in v0.3.0 once GovStack Spec v1.0 is published.

---

## Security Notes

### SBOM Requirements
The NIS2 Directive implementation (deadline December 2024, extended in some member states) is beginning to create SBOM obligations for operators of essential services — a category that includes some municipal IT infrastructure. The recommended practice (SPDX/CycloneDX SBOM at contract signature) is ahead of current regulatory requirements but aligned with expected 2026-2027 guidance from ENISA.

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

## Quarterly Review Priorities (Q3 2026)

1. **OSOR Annual Report 2023** — download and extract municipal statistics
2. **GovStack Specification v1.0** — expected publication Q3 2026
3. **ZenDiS Jahresbericht 2024** — budget and programme data
4. **BundID adoption statistics** — request from BMI press office
5. **Swiss BGEID pilot deployment data** — contact ISIO or E-Government Suisse
6. **Biberach follow-up** — Year 2 TCO data request
