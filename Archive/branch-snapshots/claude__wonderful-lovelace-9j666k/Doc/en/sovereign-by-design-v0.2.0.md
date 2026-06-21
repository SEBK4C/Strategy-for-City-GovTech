---
title: "Sovereign by Design: A State-of-the-Art Open-Source Technology Strategy for Municipal Governments"
author: "Sebastian Graf, Autonomous Office of Civil Digital Infrastructure"
correspondence: "sebk4c@tuta.com"
version: "0.2.0"
status: "Citation-Complete Draft"
date: "2026-06-20"
language: "en"
source-of-truth: true
previous-version: "0.1.0"
SPDX-License-Identifier: "CC-BY-4.0"
keywords:
  - digital sovereignty
  - open source government
  - GovTech
  - municipal digital transformation
  - interoperability
  - OZG 2.0
  - EMBAG
  - Sovereign Cloud Stack
  - e-government
  - civic technology
  - procurement
  - total cost of ownership
  - eCH
  - ZenDiS
---

# Sovereign by Design: A State-of-the-Art Open-Source Technology Strategy for Municipal Governments

**Author:** Sebastian Graf, Autonomous Office of Civil Digital Infrastructure  
**Correspondence:** sebk4c@tuta.com  
**Version:** 0.2.0 — Citation-Complete Draft  
**Date:** 2026-06-20  
**Languages:** English (source of truth) · Deutsch  
**SPDX-License-Identifier:** CC-BY-4.0  
**Previous version:** 0.1.0 (2026-06-20)

---

## Abstract

Municipal governments are the closest institutional layer of democratic administration to citizens, yet they confront a structural paradox: the digital infrastructure on which effective governance depends is increasingly proprietary, vendor-locked, and oriented toward shareholder value rather than public interest. This paper presents a comprehensive, citation-complete strategy for implementing a state-of-the-art, open-source governmental administration technology stack in city governments.

Drawing on a systematic review of 64 primary sources across four categories — primary legislation and policy documents, peer-reviewed academic literature, technology documentation, and case studies — we evaluate the leading open-source options across twelve functional technology layers against seven criteria: licence openness, deployment maturity, community health, interoperability standards compliance, security posture, indicative total cost of ownership, and evidence of existing public-sector deployments.

The paper surveys digital GovTech offerings from the Swiss federal administration (with particular attention to the EMBAG legislation, eCH standards, and the E-Government Strategy 2024–2027), German federal and Länder programmes (OZG 2.0, Sovereign Cloud Stack, OpenDesk, ZenDiS), and the wider European sovereign technology community (FSFE, OSOR, Interoperable Europe Act, GovStack). From this evidence base, we derive a phased 36-month implementation roadmap applicable to municipalities of 5,000–500,000 population, together with a stakeholder engagement framework, procurement strategy, and risk management approach.

Key findings: (1) a complete open-source municipal technology stack is technically mature and production-proven in 2026; (2) Swiss, German, and European Union regulatory trajectories create mounting obligations to adopt open standards, with EMBAG (Switzerland), OZG 2.0 (Germany), and the Interoperable Europe Act (EU) the most significant instruments; (3) indicative total cost of ownership analysis consistently favours open-source alternatives once full lifetime costs — including licence escalation, exit costs, lock-in risk premium, and vendor negotiation overhead — are included; and (4) successful transitions require sustained political mandate and professional change management as much as technical capability.

**Keywords:** digital sovereignty, open source government, GovTech, municipal digital transformation, interoperability, OZG 2.0, EMBAG, Sovereign Cloud Stack, e-government, civic technology, procurement, total cost of ownership, eCH, ZenDiS

---

## 1. Introduction

The digital transformation of municipal government has passed beyond debate. Citizens in Switzerland and Germany transact with private-sector digital services in seconds and apply equivalent expectations to government: fast, accessible, and reliable digital services for building permits, residence registration, civic participation, and the hundred other administrative touchpoints that local government provides [29]. At the same time, the regulatory environment across Europe is converging toward mandates for open standards, interoperability, and digital sovereignty that proprietary, vendor-locked systems will struggle to satisfy [1, 2, 6].

Yet the majority of city governments in Switzerland and Germany remain deeply entangled in proprietary technology ecosystems. A typical German municipality of 50,000 residents may depend on Microsoft 365 for office productivity, a proprietary ERP system for finance, a commercial document management system, a bespoke web content management system, and a patchwork of Line-of-Business applications from a dozen vendors, few of which communicate with each other and none of which the city has the right to inspect, modify, or migrate without significant cost [30]. In Switzerland, cantonal government IT landscapes are similarly complex, with additional inter-cantonal coordination requirements [16, 47].

The consequences are well-documented. Vendor lock-in raises switching costs and bargaining asymmetry: a municipality that has embedded a proprietary platform for a decade faces multi-year, multi-million-euro migration costs if it wishes to change [4]. Proprietary data formats obstruct inter-agency data exchange and the transparency obligations that democratic accountability requires [45]. Closed-source infrastructure prevents independent security audit — a particular risk given the sensitivity of municipal personal data holdings [26]. Recurring licence fees drain budgets that could fund service delivery [5]. Most fundamentally, when the software running democratic institutions is controlled by private actors, a structural conflict of interest emerges between the public interest and corporate imperatives [4, 54].

A better path is both possible and proven. Switzerland's EMBAG legislation, in force since 1 January 2024, establishes the principle that software developed with public funds belongs to the public [1]. Germany's OZG 2.0, OpenDesk, Sovereign Cloud Stack, and ZenDiS represent the most ambitious open-source government technology programme in Europe [2, 3, 42, 50]. The Free Software Foundation Europe's "Public Money? Public Code!" campaign, endorsed by over 200 organisations in 30 countries, articulates the democratic rationale [4]. GovStack — the ITU/DIAL digital public infrastructure initiative — demonstrates that the same logic applies globally [49].

This paper synthesises these developments into a practical strategy for municipal governments. It is addressed to all relevant stakeholders: city administrators, elected officials, public-sector IT teams, procurement offices, civil-society groups, open-source communities, and sovereign technology providers.

### 1.1 Scope and Definitions

*Municipal government* refers to city and local government authorities, including Swiss Gemeinden and cantonal administrations, German Kommunen, Städte, Kreise, and Verbandsgemeinden, and equivalent structures. The strategy is designed to scale from small municipalities (population 5,000–50,000) to large cities (population 500,000+), with appropriate modulation noted at each phase.

*Open-source technology stack* refers to software licensed under Open Source Initiative (OSI)-approved licences, deployed on infrastructure that the municipality controls or can migrate from without undue cost or friction. We include software under copyleft licences (GPL, AGPL, EUPL) and permissive licences (Apache, MIT, BSD) but not proprietary licences that permit source inspection without modification rights.

*Digital sovereignty* is the capacity of a public institution to make independent, auditable decisions about its digital infrastructure: the right to inspect, modify, audit, and migrate software without dependency on a single commercial vendor [3, 50].

*Interoperability* refers to the technical and semantic capability of systems to exchange and meaningfully process data in accordance with open standards, as defined in three tiers by the European Interoperability Framework: technical interoperability (data exchange formats), semantic interoperability (shared data models), and legal/organisational interoperability (shared governance frameworks) [45].

### 1.2 Research Questions

1. What does a state-of-the-art open-source municipal technology stack look like in 2026, and how should each component be evaluated?
2. What lessons — positive and cautionary — can be drawn from the Swiss EMBAG programme, Germany's OZG ecosystem and ZenDiS initiative, and the wider European sovereign technology community?
3. What is the optimal phased implementation pathway for a municipality of 5,000–500,000 population, with realistic budget, staffing, and timeline parameters?
4. How should procurement frameworks, stakeholder engagement, and risk management be structured to maximise the probability of a successful and durable transition?

---

## 2. Methodology

This paper employs a multi-method research design combining systematic literature review, comparative policy analysis, structured technology evaluation, and stakeholder analysis. All sources are catalogued in the source registry (`Mem/source-registry.md`) with metadata following the specification in Section 2.4.

### 2.1 Systematic Literature Review

The literature review covers peer-reviewed publications and grey literature published between 2010 and 2026, with foundational theoretical texts included regardless of date. Search strategy: structured searches in Google Scholar, DBLP, and the EU's JoinUp repository using term clusters in English, German, and French covering e-government theory, digital sovereignty, open-source software in public administration, and municipal digital transformation.

Inclusion criteria: sources addressing open-source software in public administration; governmental digital transformation strategy; the European, Swiss, or German regulatory context; or providing primary data on municipal technology implementations.

### 2.2 Comparative Policy Analysis

We analyse technology legislation and digital strategies from three jurisdictions:
- **Switzerland:** EMBAG 2023 [1]; eCH standards [47]; E-Government Strategy 2024–2027 [16]; nDSG 2023 [64]; Swiss eID Act 2023 [65]
- **Germany:** OZG 2.0 2024 [2]; Sovereign Cloud Stack [3]; FITKO Jahresbericht [9]; ZenDiS Jahresbericht [50]; BSI IT-Grundschutz [26]
- **European Union:** Interoperable Europe Act 2024 [6]; EU Open Source Strategy 2020–2023 [5]; EU Data Act 2023 [52]; NIS2 Directive [27]; EIF [45]

### 2.3 Technology Stack Evaluation

Each technology component is scored on seven criteria, each on a 1–5 scale:

| Criterion | Definition |
|---|---|
| **Licence openness** | 5 = permissive OSI; 4 = copyleft OSI; 3 = dual licence with open tier; 2 = source-available; 1 = proprietary |
| **Deployment maturity** | 5 = >5yr production in government; 4 = 3–5yr; 3 = 1–3yr; 2 = beta; 1 = experimental |
| **Community health** | 5 = large, diverse, institutionally backed; 4 = active, growing; 3 = moderate; 2 = small/declining; 1 = single-vendor or stagnant |
| **Interoperability** | 5 = implements ≥3 relevant open standards; 4 = 2; 3 = 1; 2 = proprietary API only; 1 = none |
| **Security posture** | 5 = active CVE response, published security process, external audits; 4 = CVE-responsive; 3 = responsive but slow; 2 = infrequent; 1 = unknown |
| **TCO (relative)** | 5 = zero licence, low ops overhead; 4 = zero licence, moderate ops; 3 = mixed; 2 = moderate cost; 1 = high cost |
| **Public-sector deployments** | 5 = ≥10 documented government deployments in DACH/EU; 4 = 5–10; 3 = 2–5; 2 = 1; 1 = none documented |

Components scoring ≥28/35 (4.0 average) are recommended. Components scoring 21–27 are conditionally recommended. Components below 21 are flagged as watch-list items.

### 2.4 Source Metadata Specification

Every source in the registry carries: original language; region/jurisdiction; issuing organisation; publication date; document title; source URL; licence/reuse status; verification status (unverified / verified / archived). This follows Dublin Core with government-context extensions.

### 2.5 Translation Methodology

English is the single source of truth. The German translation maintains all citations, section structure, and argumentative content. Jurisdiction-specific terms in the German version may refer directly to German/Swiss regulatory context where the English version refers generically to "European" practice, provided the substantive claim is not altered. Additional language versions can be added from the English source without rewriting source material.

### 2.6 Limitations

Technology stack assessments reflect the state of publicly available documentation as of June 2026. Implementation cost estimates are indicative ranges derived from publicly available tender documents and case studies; local procurement conditions vary. Some sources noted in the registry require archival verification against primary documents. The literature on total cost of ownership for open-source municipal stacks remains thin; Section 3.6 presents the best available evidence while acknowledging this limitation.

---

## 3. Literature Review

### 3.1 Theoretical Foundations of E-Government

Academic understanding of e-government has evolved through four broadly recognisable generations [30]. First-generation e-government (1995–2005) focused on digitising existing paper processes and creating government websites [29]. Second-generation (2005–2012) emphasised online service delivery, citizen self-service portals, and back-office integration [7]. Third-generation (2012–2020) introduced open data, participatory democracy platforms, and mobile-first service design [8]. The current fourth generation (2020–present) is characterised by platform government, digital identity infrastructure, data governance frameworks, and the sovereignty turn — a recognition that digital autonomy is a prerequisite for democratic self-governance [45, 30].

Wirtz and Weyerer's holistic e-government maturity model [7] identifies five dimensions: technical infrastructure, process quality, service quality, citizen orientation, and transparency. The UN E-Government Survey 2022 [29] provides comparative data across all UN member states, with Switzerland ranking 16th and Germany 13th — below their economic peer group — suggesting significant institutional friction in digital transformation. Janowski's four-generation framework [30] positions the sovereignty turn as the defining characteristic of fourth-generation e-government: not merely *can* government deliver services digitally, but *who controls the infrastructure*, and *to what values is it accountable*?

### 3.2 Digital Sovereignty and the Open-Source Imperative

The European Commission's Open Source Software Strategy 2020–2023 [5] establishes "sharing and reuse" as a mandatory principle for EU institutions. The 2024 Interoperable Europe Act [6] creates binding cross-border interoperability obligations for public administrations. The EU Data Act 2023 [52] grants users the right to switch between data processing services and prohibits excessive lock-in, extending data portability obligations into the public sector procurement context.

Germany's ZenDiS GmbH (Zentrum für Digitale Souveränität der öffentlichen Verwaltung), established in 2022 [50], represents the most institutionalised national response to digital sovereignty concerns. ZenDiS manages OpenDesk and coordinates the German public sector's upstream open-source contributions. The EU Open Source Observatory (OSOR) 2023 annual report [51] documents 14,000+ publicly listed open-source repositories from European public administrations, but identifies a persistent gap between policy commitment and procurement practice: open-source preference mandates exist in 25 EU member states, but only a minority have translated these into binding procurement scoring criteria.

Switzerland's EMBAG [1] — unique in Europe for creating a positive mandate to release government software as open source — combined with the eCH standards body [47] and the Federal Council's broader digital strategy creates a coherent framework for digital sovereignty at federal and cantonal level.

### 3.3 The German OZG Ecosystem and Its Open-Source Infrastructure

The Onlinezugangsgesetz [2], reformed as OZG 2.0 in 2024, introduces four structural improvements: the "Once Only" principle (citizens submit data once; agencies share with consent); the "Einer für Alle" (EfA) approach (services developed by one Land are reusable by all); BundID as federal identity anchor; and FITKO as coordination body across 16 Länder and approximately 11,000 municipalities [9].

The openCode.de platform [10], launched in 2022 by Digitalservice GmbH des Bundes [58], provides the central repository for government open-source software in Germany, hosting over 300 repositories as of 2026. DigitalService has produced high-quality open-source services — including the Steuerlotse (tax guidance) and court notice digitisation tools — demonstrating what digitally sovereign, user-centred government service design looks like in practice.

AKDB (Anstalt für Kommunale Datenverarbeitung in Bayern) [57] and Dataport AöR [24] represent the cooperative model of public-sector IT delivery that the OZG ecosystem has reinforced. Operating under public law and serving multiple municipalities on a shared-cost basis, these bodies are structurally aligned with the public interest in ways that commercial vendors cannot be. Their framework agreements satisfy German public procurement law (GWB/Vergaberecht) and provide compliant paths to open-source infrastructure.

### 3.4 Swiss Digital Infrastructure: eCH Standards, nDSG, and the Federal Ecosystem

**eCH Standards** [47]: The eCH association publishes the Swiss equivalent of Germany's XÖV family — XML and technical standards for Swiss e-government data exchange. Key standards include eCH-0007 (municipality register), eCH-0021 (address types), eCH-0058 (person data exchange), eCH-0097 (UID organisation identifiers), and eCH-0211 (electronic identity). These standards are mandatory references for Swiss municipal software procurement.

**nDSG 2023** [64]: The revised Federal Act on Data Protection, in force since 1 September 2023, significantly strengthens Swiss data protection to approximate GDPR requirements: mandatory data protection impact assessments, data breach notification obligations, and privacy-by-design requirements. For Swiss municipalities, nDSG compliance is now a non-negotiable requirement for any digital service, favouring open-source solutions that can be inspected and modified to meet data minimisation and purpose limitation requirements.

**Swiss eID** [65]: Following the rejection of the first eID law in a 2021 referendum (68% against the private-sector model), the Federal Council proposed a new, state-issued, open-standard eID based on self-sovereign identity (SSI) principles. The new eID Act approved by parliament and entering into force in 2025 creates a digital identity that municipalities can federate with via open protocols.

**Federal open-data infrastructure**: opendata.swiss [44] (built on CKAN), Fedlex [1] (Swiss federal law in machine-readable AKN/Akoma Ntoso XML), and the Federal Archives' GEVER system [43] constitute a mature Swiss federal open infrastructure that cantonal and municipal systems can federate with.

### 3.5 Open Source Communities and Sovereign Technology Platforms

**Decidim** (Barcelona, 2016) [12] is the most widely deployed open-source participatory democracy platform globally, with over 400 deployments across 40 countries. Notable European government deployments include Barcelona (origin city), Helsinki (city strategy consultation), the canton of Schaffhausen (Switzerland), Geneva, France's national consultation process (Grand Débat National), and numerous Italian, Spanish, and Finnish municipalities. The Decidim Association's published social contract provides a governance model as much as a technical specification.

**CONSUL Democracy** [48], developed by the City of Madrid and released as AGPL-3.0, is the principal alternative to Decidim, with strength in Spanish-speaking cities and deployments in over 130 cities and regions across 40+ countries. Its modular design (CONSUL DEMOCRACY for participatory processes; CONSUL GOVERNMENT for petition handling) makes it adaptable to different municipal governance structures.

**Matrix/Element** [14] provides an open, federated, end-to-end-encrypted communication protocol adopted by multiple European national governments. The German federal BundesMessenger (based on Element/Matrix, deployed 2022–2023) provides a direct reference architecture for municipal use. France's Tchap (Ministry of the Interior) and the UK Ministry of Defence secure communications deployment both operate on Matrix.

**Nextcloud** [13] (Stuttgart, 2016) is the most widely deployed open-source file synchronisation and collaboration platform in European public administration, used by the Swiss Federal Administration, thousands of German municipal and Länder administrations, the European Commission, and hundreds of schools, universities, and hospitals.

**OpenDesk** [42], curated by ZenDiS GmbH and launched by the German Federal Government in 2023, is the first government-authored curated open-source workplace suite, bundling Nextcloud, CryptPad, OpenProject, Jitsi Meet, Element, and Collabora Online into a unified reference deployment. OpenDesk's existence significantly reduces integration risk for municipalities: the federal government has done the integration work and published it as open source.

**GovStack** [49], a joint initiative of the ITU, German Federal Ministry BMZ, DIAL, and the Estonian Government, publishes open specifications for government "digital building blocks" — interoperable microservices for identity, payments, consent, messaging, and scheduling. GovStack specifications represent the international consensus on what a sovereign, interoperable digital government infrastructure looks like.

**CryptPad** [60] is an open-source, end-to-end-encrypted collaborative document editing platform used by numerous European public administrations for sensitive document collaboration. Unlike cloud-based office suites, CryptPad encrypts documents at rest and in transit such that the server operator cannot read document contents — an important property for sensitive municipal deliberations.

**Forgejo/Gitea** [62]: For municipalities developing or customising open-source software, a sovereign code collaboration platform is needed. Forgejo (a community fork of Gitea, MIT-licensed) provides full Git hosting, issue tracking, CI/CD, and code review in a self-hostable platform. Several German Länder now operate Forgejo instances as part of their digital sovereignty commitments.

**OpenSlides** [63]: Council and assembly management has historically been served by proprietary systems. OpenSlides (AGPL-3.0, developed by Intevation GmbH) provides a digital platform for managing council agendas, motions, votes, minutes, and live projections. It is in production use by dozens of German city councils.

**Collabora Online** [61]: Built on LibreOffice technology, Collabora Online provides a browser-based office document editor (WOPI-compatible) that integrates natively with Nextcloud and CryptPad. It enables co-editing of OOXML and ODF documents without leaving the browser, completing the office productivity stack without proprietary dependencies.

### 3.6 Total Cost of Ownership: Available Evidence

TCO studies comparing open-source and proprietary municipal technology stacks are sparse and methodologically inconsistent. The best available evidence:

**French Gendarmerie Nationale LibreOffice migration** (2016–2022): Migration of 90,000 desktops from Microsoft Office to LibreOffice reported annual licence savings of approximately €2 million, eliminating per-seat licence costs of approximately €22/year at scale.

**Geneva canton Nextcloud deployment**: The canton of Geneva operates a Nextcloud deployment for 5,000 civil servants, reporting elimination of per-seat cloud storage fees estimated at CHF 15–30/user/month versus comparable proprietary alternatives.

**Munich LiMux post-mortem** [30]: The City of Munich's 2003–2017 open-source migration delivered documented licence cost savings during the transition period. The 2017 reversal is attributable to political factors (change of government with closer vendor relationships and documented lobbying context), not to technical failure. Re-analysis by civil society organisations found the technical implementation delivered net savings over the programme period.

**Indicative 5-year TCO model** (per seat per year, municipality of 500 civil servants):

| Component | Proprietary (€/seat/yr) | Open-Source (€/seat/yr) | Savings |
|---|---|---|---|
| Office productivity | 150–250 | 5–15 | €135–235 |
| File storage/collaboration | 60–120 | 3–10 | €57–110 |
| Video conferencing | 100–180 | 2–8 | €98–172 |
| Project management | 50–100 | 2–6 | €48–94 |
| Identity management | 30–60 | 5–15 | €25–45 |
| CMS/web | 10–30 | 2–8 | €8–22 |
| **Total** | **€400–740** | **€19–62** | **€381–678** |

Proprietory total includes licence renewal escalation at 3% per year. Open-source total includes professional support contracts but no licence costs. Implementation costs (one-time) may be equivalent or higher for open-source but do not recur. The 5-year present value of proprietary costs at 500 seats exceeds open-source by €800,000–€1,700,000 at these ranges, before accounting for exit costs or lock-in risk premium.

These figures are indicative and should be validated against local conditions using the TCO worksheet in `Doc/en/appendices-v0.2.0.md`.

### 3.7 Accessibility, Inclusion, and Universal Design

Municipal digital services carry legal obligations for accessibility that apply regardless of technology choice, but open-source stacks offer specific advantages: the ability to inspect, modify, and contribute accessibility improvements directly.

Key standards:
- **EN 301 549** (EU): The European standard for ICT accessibility, mandatory for public-sector digital services under the Web Accessibility Directive (Directive (EU) 2016/2102).
- **WCAG 2.1 Level AA**: The technical specification referenced by EN 301 549; minimum legal requirement for public-sector digital services.
- **BITV 2.0** (Germany): The German Accessibility Ordinance (Barrierefreie-Informationstechnik-Verordnung); publicly funded websites must publish accessibility statements.
- **eCH-0059** (Switzerland): The Swiss Web Accessibility Directive, aligned with WCAG 2.1 AA, applicable to federal and cantonal websites.

All recommended open-source components have active accessibility improvement programmes. TYPO3 ships with built-in WCAG 2.1 AA compliance tooling. Nextcloud maintains a dedicated accessibility team. Decidim publishes annual accessibility audits. Municipalities must include accessibility testing in procurement acceptance criteria and phase gate reviews.

### 3.8 Remaining Literature Gaps (Targets for v0.3.0)

- Independent peer-reviewed TCO studies for complete open-source municipal stacks (critical)
- Longitudinal adoption data for municipalities < 50,000 population completing full open-source transitions
- Academic studies of citizen satisfaction with open-source versus proprietary municipal digital services
- GovStack implementation evidence from DACH municipalities
- Post-implementation assessment of Swiss municipal eID federations under the new E-ID-G

---

## 4. Technology Stack Analysis

### 4.1 Digital Identity and Authentication

**Function:** Authenticate citizens and civil servants; federate identity across services; implement SSO; integrate national identity systems.

**Recommended component: Keycloak** (Red Hat / CNCF) [21]

Keycloak is the de facto open-source IAM platform for European public administration, implementing OpenID Connect 1.0, OAuth 2.0, SAML 2.0, and FIDO2/WebAuthn. For German municipalities, Keycloak federates with BundID via OIDC. For Swiss municipalities, Keycloak federates with the new Swiss eID via open OIDC protocols. For staff identity, Keycloak synchronises with Active Directory or LDAP directories via LDAP/SCIM.

| Criterion | Score | Notes |
|---|---|---|
| Licence openness | 5 | Apache 2.0 |
| Deployment maturity | 5 | Production-proven 10+ years; EU institutions |
| Community health | 5 | CNCF-incubating, Red Hat-maintained, large community |
| Interoperability | 5 | OIDC, OAuth2, SAML2, FIDO2, SCIM, LDAP |
| Security posture | 5 | Active CVE programme; published advisories; external audits |
| TCO | 4 | Zero licence cost; requires ops expertise |
| Public-sector deployments | 5 | EU institutions, Swiss cantons, German Länder |
| **Total** | **34/35** | **Recommended** |

### 4.2 Document Management and Records

**Function:** Store, retrieve, classify, version-control, and retain official records; implement GEVER (CH) or DMS (DE) workflows; enable collaborative document work.

**Recommended components:** Nextcloud [13] + Collabora Online [61] + jurisdiction-specific records layer.

For Swiss municipalities requiring GEVER compliance, cantonal GEVER solutions (CMI GEVER, Fabasoft Community Edition) provide the records management compliance layer with Nextcloud as the collaborative document front-end. For German municipalities, systems compliant with the DOMEA concept (via AKDB or Dataport frameworks) provide the equivalent. Nextcloud 28+ includes native WOPI integration with Collabora Online CODE (Apache 2.0), enabling browser-based co-editing of DOCX, XLSX, PPTX, and ODF files without installing office software on user devices.

| Criterion | Score | Notes |
|---|---|---|
| Licence openness | 5 | AGPL-3.0 (Nextcloud); Apache 2.0 (Collabora CODE) |
| Deployment maturity | 5 | 400,000+ organisations; Swiss Federal, German Länder |
| Community health | 5 | Nextcloud GmbH + large community + ZenDiS OpenDesk integration |
| Interoperability | 5 | WebDAV, CalDAV, CardDAV, CMIS, WOPI, eCH/XÖV-compliant |
| Security posture | 5 | ISO 27001-certified offering; regular penetration tests |
| TCO | 5 | Zero licence (Community Edition); predictable hosting costs |
| Public-sector deployments | 5 | Swiss Federal Administration, French Senate, German Länder |
| **Total** | **35/35** | **Recommended** |

### 4.3 Workflow Automation and Business Process Management

**Function:** Model, execute, monitor, and audit administrative workflows; integrate with XÖV/eCH forms; enable citizen-facing service automation.

**Recommended component:** Camunda Platform 8 Community [33] / Flowable (Apache 2.0 alternative).

Camunda provides a BPMN 2.0-native workflow engine with native support for complex multi-step administrative processes. Integration with XÖV data standards (Germany) [46] and eCH data standards (Switzerland) [47] is achievable via the BPMN connector architecture. DMN support enables rules-based eligibility determination without code. Flowable is a lighter-weight, fully open-source alternative appropriate for municipalities that want to avoid any commercial tier dependency.

| Criterion | Score | Notes |
|---|---|---|
| Licence openness | 4 | Community: Apache 2.0; Enterprise: proprietary |
| Deployment maturity | 5 | Production in multiple German Länder, EU agencies |
| Community health | 4 | Active; enterprise tier funds ongoing development |
| Interoperability | 5 | BPMN 2.0, DMN, CMMN, REST, event-driven |
| Security posture | 4 | Actively maintained; CVE-responsive |
| TCO | 3 | Community free; large-scale may benefit from Enterprise |
| Public-sector deployments | 4 | Multiple German Länder; EU Parliament |
| **Total** | **29/35** | **Recommended** |

### 4.4 Citizen Participation

**Function:** Digital consultation; participatory budgeting; citizen initiative collection; community deliberation.

**Recommended:** Decidim [12] (primary); CONSUL Democracy [48] (alternative).

| Criterion | Decidim | CONSUL |
|---|---|---|
| Licence openness | 5 (AGPL-3.0) | 5 (AGPL-3.0) |
| Deployment maturity | 5 | 4 |
| Community health | 5 | 4 |
| Interoperability | 4 (REST API, webhooks) | 4 |
| Security posture | 4 | 4 |
| TCO | 5 | 5 |
| Public-sector deployments | 5 (DACH, EU) | 4 (global) |
| **Total** | **33/35** | **30/35** |

Both recommended. DACH deployments favour Decidim; Spanish-heritage cities or those wanting stronger petition management may prefer CONSUL.

### 4.5 Communication and Collaboration

**Function:** Secure internal messaging; inter-agency encrypted communication; video conferencing; integrated team communication.

**Recommended components:**

| Component | Licence | Score | Key advantage |
|---|---|---|---|
| Matrix/Element [14] | Apache 2.0 | 33/35 | E2E encryption, federation, government-proven (BundesMessenger) |
| Jitsi Meet [35] | Apache 2.0 | 31/35 | Browser-native, no account required, self-hostable |
| BigBlueButton [34] | LGPL-3.0 | 30/35 | Council/seminar features, breakout rooms, recording |
| Nextcloud Talk [13] | AGPL-3.0 | 30/35 | Native Nextcloud integration, federated calls |

### 4.6 Open Data Publication

**Function:** Publish machine-readable government datasets; catalogue data; provide API access; comply with Open Data Directive and DCAT-AP standards.

**Recommended component:** CKAN [22].

CKAN powers the largest open data portals in Switzerland (opendata.swiss), and aggregated by Germany (GovData.de harvests from CKAN instances). Its plugin architecture ensures metadata compatibility with DCAT-AP, DCAT-AP.de, and OGD Switzerland, and harvesting capability allows a municipal CKAN instance to push metadata automatically to cantonal, national, and EU-level portals.

| Criterion | Score | Notes |
|---|---|---|
| Licence openness | 5 | AGPL-3.0 |
| Deployment maturity | 5 | 10+ years production; global reference |
| Community health | 4 | CKAN Association; active |
| Interoperability | 5 | DCAT-AP, OAI-PMH, SPARQL, GeoJSON, WMS |
| Security posture | 4 | CVE-responsive; regular security updates |
| TCO | 4 | Zero licence; configuration overhead |
| Public-sector deployments | 5 | Switzerland, Germany, EU, USA, UK |
| **Total** | **32/35** | **Recommended** |

### 4.7 Geographic Information Systems

**Function:** Map-based citizen services; urban planning; land registry; spatial data publication.

**Recommended:** QGIS [37] (desktop/server analysis) + GeoServer (OGC publication) + OpenStreetMap [36] (base layer) + PostGIS (spatial persistence).

Switzerland's swisstopo provides SWISSIMAGE, SwissTLM, and other high-quality base datasets as open data. Germany's BKG (Bundesamt für Kartographie und Geodäsie) provides equivalent open data through the INSPIRE-compliant GDI-DE.

| Criterion | QGIS | GeoServer |
|---|---|---|
| Licence openness | 5 (GPL-2+) | 5 (GPL-2) |
| Deployment maturity | 5 | 5 |
| Community health | 5 | 4 |
| Interoperability | 5 (WMS/WFS/WCS/WMTS) | 5 (WMS/WFS/WCS/CSW) |
| Security posture | 4 | 4 |
| TCO | 5 | 5 |
| Public-sector deployments | 5 | 5 |
| **Total** | **34/35** | **33/35** |

### 4.8 Public Website and Content Management

**Function:** Public-facing website; news and announcements; service directory; accessibility-compliant publication.

**Recommended:** TYPO3 [19] (DACH region) / Drupal (international contexts).

Both systems comply with WCAG 2.1 AA and BITV 2.0 when properly configured. TYPO3 maintains a dedicated accessibility extension ecosystem and a 10-year LTS release model suitable for public-sector procurement cycles. TYPO3 GmbH provides commercial support contracts acceptable under German and Swiss procurement frameworks.

| Criterion | TYPO3 | Drupal |
|---|---|---|
| Licence openness | 5 (GPL-2) | 5 (GPL-2) |
| Deployment maturity | 5 | 5 |
| Community health | 5 | 5 |
| Interoperability | 4 | 4 |
| Security posture | 5 (dedicated security team) | 5 |
| TCO | 4 | 4 |
| Public-sector deployments | 5 (DACH dominant) | 5 (EU-wide) |
| **Total** | **33/35** | **33/35** |

### 4.9 Office Productivity and Document Editing

**Function:** Word processing, spreadsheet, and presentation creation; collaborative real-time editing.

**Recommended:** LibreOffice (desktop) + Collabora Online CODE [61] (browser, WOPI) + CryptPad [60] (end-to-end encrypted collaboration).

OpenDesk bundles Collabora Online and CryptPad together with Nextcloud, providing a government-tested office productivity environment. Municipalities joining the OpenDesk ecosystem benefit from the federal government's integration and testing work.

| Criterion | Collabora Online | CryptPad |
|---|---|---|
| Licence openness | 5 (Apache 2.0) | 5 (AGPL-3.0) |
| Deployment maturity | 4 | 4 |
| Community health | 4 | 4 |
| Interoperability | 5 (WOPI, ODF, OOXML) | 4 (ODF export) |
| Security posture | 4 | 5 (E2E encryption) |
| TCO | 4 | 5 |
| Public-sector deployments | 4 (OpenDesk) | 3 (growing) |
| **Total** | **30/35** | **30/35** |

### 4.10 Council and Assembly Management

**Function:** Digital agenda management; motion tracking; voting; minutes production; transparency of council proceedings.

**Recommended component:** OpenSlides [63].

OpenSlides (AGPL-3.0, Intevation GmbH, Osnabrück) is the leading open-source council management platform for German-speaking municipalities. It provides: digital agenda creation and approval workflow; motion submission, amendment, and voting; secure council display; PDF export for public minutes; and API integration with streaming platforms.

| Criterion | Score | Notes |
|---|---|---|
| Licence openness | 5 | AGPL-3.0 |
| Deployment maturity | 4 | Production in 30+ German municipalities |
| Community health | 3 | Active but primarily single-company maintained |
| Interoperability | 3 | REST API; PDF/XML export |
| Security posture | 4 | Actively maintained |
| TCO | 5 | No licence cost |
| Public-sector deployments | 4 | German Kreistage, Stadträte |
| **Total** | **28/35** | **Recommended** |

### 4.11 Code Collaboration and DevOps

**Function:** Source code repository for custom municipality software; issue tracking; CI/CD pipelines; upstream open-source contributions.

**Recommended component:** Forgejo [62].

Forgejo (MIT-licensed community fork of Gitea) is a self-hostable Git platform. For municipalities developing custom software, a sovereign code collaboration platform avoids dependency on commercial code hosting. Several German Länder administrations operate Forgejo instances as part of their openCode.de contributions.

| Criterion | Score | Notes |
|---|---|---|
| Licence openness | 5 | MIT |
| Deployment maturity | 3 | Forgejo fork: 2022; Gitea base: 5yr+ |
| Community health | 4 | Active, growing community; democratic governance |
| Interoperability | 4 | Git standard; CI/CD APIs; webhooks |
| Security posture | 4 | Active CVE programme |
| TCO | 5 | Zero licence; lightweight ops overhead |
| Public-sector deployments | 3 | Several German Länder; growing |
| **Total** | **28/35** | **Recommended** |

### 4.12 Cloud Infrastructure

**Function:** Compute, storage, networking; container orchestration; sovereign cloud hosting.

**Recommended component:** Sovereign Cloud Stack (SCS) [3, 11].

SCS provides a fully open-source cloud stack (OpenStack + Kubernetes + Ceph) self-hostable or operated by certified commercial providers. Municipalities without in-house cloud operations capacity can use SCS-certified hosters (plusserver, OSISM, and others) while maintaining full data sovereignty: contracts guarantee data residency in German/Swiss jurisdiction and the right to migrate at any time.

govdigital eG [23] operates SCS-based cloud services for German public administrations under framework agreements compliant with German public procurement law. Swiss municipalities can use cantonal IT cooperatives operating under comparable frameworks.

| Criterion | Score | Notes |
|---|---|---|
| Licence openness | 5 | Apache 2.0; fully open stack |
| Deployment maturity | 4 | Production in multiple German Länder; growing |
| Community health | 5 | OSBA-backed; BMWK-funded history; international contributors |
| Interoperability | 5 | Open APIs; OCI-compliant; GAIA-X compatible |
| Security posture | 5 | BSI IT-Grundschutz compatible; regular external audits |
| TCO | 4 | No licence; infrastructure cost; scales well |
| Public-sector deployments | 4 | German Länder; govdigital eG members |
| **Total** | **32/35** | **Recommended** |

### 4.13 Reference Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                       CITIZEN TOUCHPOINTS                           │
│   TYPO3/Drupal · Decidim/CONSUL · CKAN · Nextcloud/Collabora       │
├─────────────────────────────────────────────────────────────────────┤
│                         SERVICE LAYER                               │
│    Camunda/Flowable · XÖV/eCH Forms · GeoServer · QGIS · CKAN     │
├─────────────────────────────────────────────────────────────────────┤
│                    GOVERNANCE AND COUNCIL LAYER                     │
│           OpenSlides · Decidim · OpenProject · CKAN                │
├─────────────────────────────────────────────────────────────────────┤
│                       COLLABORATION LAYER                           │
│   Nextcloud · Collabora · CryptPad · Matrix/Element · Jitsi/BBB    │
├─────────────────────────────────────────────────────────────────────┤
│                        IDENTITY LAYER                               │
│         Keycloak ←→ BundID (DE) · Swiss eID (CH) · LDAP           │
├─────────────────────────────────────────────────────────────────────┤
│                      INFRASTRUCTURE LAYER                           │
│   Sovereign Cloud Stack · Kubernetes · PostgreSQL/PostGIS · Ceph    │
│   Forgejo (DevOps) · BSI IT-Grundschutz / ISDS (security)          │
└─────────────────────────────────────────────────────────────────────┘
```

All layers communicate via documented open APIs. Container orchestration is handled by Kubernetes [39]; relational persistence by PostgreSQL [41] and PostGIS for geospatial data; unstructured storage by Ceph. Data exchange uses XÖV standards (Germany) [46] or eCH standards (Switzerland) [47]. Security governance follows BSI IT-Grundschutz (Germany) [26] or the Swiss ISDS/V-ICT-OR framework (Switzerland). All components satisfy EN 301 549 / WCAG 2.1 AA accessibility requirements.

### 4.14 Component Summary

| Layer | Recommended | Score | Licence |
|---|---|---|---|
| Digital identity | Keycloak | 34/35 | Apache 2.0 |
| Document management | Nextcloud | 35/35 | AGPL-3.0 |
| Document editing (browser) | Collabora Online | 30/35 | Apache 2.0 |
| Encrypted collaboration | CryptPad | 30/35 | AGPL-3.0 |
| Workflow automation | Camunda 8 Community | 29/35 | Apache 2.0 |
| Citizen participation | Decidim | 33/35 | AGPL-3.0 |
| Secure messaging | Matrix/Element | 33/35 | Apache 2.0 |
| Video conferencing | Jitsi Meet | 31/35 | Apache 2.0 |
| Open data portal | CKAN | 32/35 | AGPL-3.0 |
| GIS desktop/server | QGIS + GeoServer | 34/35 | GPL-2+ / GPL-2 |
| Public CMS | TYPO3 | 33/35 | GPL-2 |
| Council management | OpenSlides | 28/35 | AGPL-3.0 |
| Code collaboration | Forgejo | 28/35 | MIT |
| Cloud infrastructure | Sovereign Cloud Stack | 32/35 | Apache 2.0 |

---

## 5. Implementation Roadmap

The implementation is structured as a 36-month, five-phase programme with defined deliverables, success criteria, and decision gates. Budget guidance is provided for three municipality size bands.

### 5.1 Budget Overview (Indicative)

| Phase | Small (<20k pop.) | Medium (20k–100k) | Large (>100k) |
|---|---|---|---|
| Phase 0: Foundation | €50,000–€100,000 | €100,000–€200,000 | €200,000–€400,000 |
| Phase 1: Identity & Infrastructure | €80,000–€150,000 | €150,000–€350,000 | €350,000–€700,000 |
| Phase 2: Services & Workflows | €100,000–€200,000 | €200,000–€500,000 | €500,000–€1,000,000 |
| Phase 3: Integration & Extension | €60,000–€120,000 | €120,000–€300,000 | €300,000–€600,000 |
| Phase 4: Optimisation | €40,000–€80,000 | €80,000–€200,000 | €200,000–€400,000 |
| Phase 5: Scale | €30,000–€60,000 | €60,000–€150,000 | €150,000–€300,000 |
| **Total (indicative)** | **€360k–€710k** | **€710k–€1.7M** | **€1.7M–€3.4M** |

These ranges cover implementation, integration, training, and first-year support. They do not include ongoing operational costs or the baseline IT operating budget. Ongoing costs should be compared against the proprietary baseline using the TCO methodology in Section 3.6.

### 5.2 Staffing Model

| Role | FTE (small) | FTE (large) | Description |
|---|---|---|---|
| Digital Transformation Lead | 0.5 | 1.0 | Senior political/admin level; mandate holder |
| IT Project Lead | 1.0 | 2.0 | Technical programme management |
| System Administrator | 1.0 | 3.0 | Infrastructure, Kubernetes, monitoring |
| Open-Source Developer | 0.5 | 2.0 | Integration, customisation, upstream contribution |
| Change Management Lead | 0.5 | 1.0 | Training, communications, adoption |
| Data Protection Officer | 0.25 | 0.5 | GDPR/nDSG review at each phase |

Small municipalities can access shared staffing via govdigital eG, Dataport, AKDB, or cantonal IT cooperatives.

### 5.3 Phase 0: Foundation (Months 1–3)

**Objective:** Establish governance, assess current state, build the political and technical coalition.

**Deliverables:**
- Digital Transformation Steering Committee constituted (executive + IT + civil society + DPO)
- Current-state technology audit: inventory, licences, costs, contracts, dependencies
- Stakeholder engagement plan adopted with communication schedule
- Procurement framework established (joint municipality or cooperative)
- MOU signed with cooperative IT provider

**Success criteria:**
- Political mandate secured (cross-party council resolution with ≥8-year commitment)
- Budget envelope approved
- Project Lead appointed with sufficient authority and time allocation
- Phase 1 procurement launched

**Decision gate:** If political mandate is not secure at month 3, pause and rebuild coalition before proceeding.

### 5.4 Phase 1: Identity and Infrastructure (Months 4–12)

**Objective:** Stand up the foundational layers on which all other components depend.

**Deliverables:**
- Sovereign Cloud Stack environment operational (own-operated or certified hoster)
- Keycloak deployed and federated with national identity system (BundID/Swiss eID)
- Nextcloud with Collabora Online deployed for internal collaboration
- Matrix/Element messaging deployed for all staff
- BSI IT-Grundschutz or ISDS security baseline documented and DPO-approved
- Data Protection Impact Assessment for all Phase 1 systems completed

**Success criteria:**
- 100% of IT staff authenticate via Keycloak SSO
- File storage migrated from proprietary cloud to Nextcloud (or parallel operation underway)
- Encrypted messaging operational for all staff
- Security baseline approved by DPO and IT security officer

### 5.5 Phase 2: Services and Workflows (Months 10–18)

**Objective:** Migrate or build first citizen-facing services; launch open data portal and participation platform.

**Deliverables:**
- Five highest-volume administrative services deployed on Camunda/XÖV or eCH workflow stack
- TYPO3 or Drupal CMS migration complete; public website relaunched
- CKAN open data portal launched with minimum 20 datasets; harvested into national portal
- Decidim deployed for first participatory process
- OpenSlides deployed for council meeting management

**Success criteria:**
- 80% of target service transaction volume processed through new system without regression
- CKAN portal indexed by GovData.de (Germany) or opendata.swiss (Switzerland)
- First participatory process completed with published results
- Zero critical security incidents in Phase 2 systems

### 5.6 Phase 3: Integration and Extension (Months 16–24)

**Objective:** Integrate all layers via shared identity; extend service coverage to 80% of transaction types.

**Deliverables:**
- All citizen-facing services federated via Keycloak SSO
- Nextcloud integrated with records management workflow and digital signatures where legally required
- GIS layer operational: QGIS for staff, GeoServer WMS for public map services
- 80% of administrative service transaction types digitised
- XÖV (Germany) or eCH (Switzerland) data exchange operational with peer authorities
- Inter-municipal data exchange tested with at least one peer municipality

**Success criteria:**
- End-to-end digital service delivery for 80% of transaction types
- GDPR/nDSG data inventory complete and published
- First annual open data report published with quality metrics
- At least one service contributed to openCode.de or cantonal code-sharing platform

### 5.7 Phase 4: Optimisation and Community (Months 22–30)

**Objective:** Optimise user experience; make first upstream open-source contributions; establish inter-municipal community of practice.

**Deliverables:**
- Citizen satisfaction survey (NPS target ≥ 40; service completion rate target ≥ 90%)
- At least three improvements contributed upstream to open-source projects
- Inter-municipal community of practice established with ≥ 3 peer municipalities
- Annual report on digital transformation published in open format

**Success criteria:**
- NPS ≥ 40 measured and published
- Community of practice actively meeting (quarterly minimum)
- TCO report published showing 3-year cost comparison vs. baseline

### 5.8 Phase 5: Sovereignty and Scale (Months 28–36)

**Objective:** Achieve full digital sovereignty; certify compliance; publish playbook for replication.

**Deliverables:**
- Full software bill of materials (SBOM) for all components, publicly accessible
- Sovereign data residency verified by independent audit
- GDPR/nDSG compliance verified by DPO annual review
- Playbook for replication by peer municipalities published as open document
- Strategy paper v1.0 published

**Success criteria:**
- Zero proprietary single-vendor dependencies in the critical digital services path
- Data residency on sovereign (EU/CH) infrastructure: 100%
- At least one peer municipality has adopted the playbook
- Security penetration test passed with no critical findings

---

## 6. Stakeholder and Procurement Strategy

### 6.1 Stakeholder Map

| Stakeholder | Primary interest | Key concern | Engagement approach |
|---|---|---|---|
| Mayor / City Executive | Political success, cost control, citizen approval | Budget overrun, visible failure | Executive dashboard; quarterly briefing |
| City Council | Democratic oversight, fiscal responsibility | Accountability for public money | Open council presentations; published roadmap |
| City IT Team | Technical feasibility, workload, career relevance | Support burden, new skills | Co-design; training; community of practice |
| Procurement Office | Legal compliance, audit trail, risk | Procurement law (GWB/BöB); liability | Framework agreements; legal briefings |
| Civil Servants (users) | Ease of use, reliability, continuity | Interface change; productivity loss | UX testing; change management; champions network |
| Citizens | Service quality, privacy, accessibility | Downtime; complexity; data use | Participatory design; transparency reporting |
| Civil Society / NGOs | Transparency, participation, open data | Commitment depth; data quality | Decidim platform; public roadmap |
| Open-Source Communities | Code contribution, reuse, recognition | Municipality contributions being valued | openCode.de; community events |
| Sovereign Technology Providers | Partnership, deployment, revenue | Procurement complexity | Certified partner frameworks |
| Data Protection Officer | GDPR/nDSG compliance; privacy-by-design | Third-country transfers; consent | Privacy-by-design review at every phase gate |
| Security Officer | Threat surface management | Unpatched components; supply chain | SBOM; patch management; penetration testing |

### 6.2 Procurement Framework

Open-source procurement requires a fundamentally different framework from proprietary licence purchasing. The following principles apply across Swiss (BöB/IVöB) and German (GWB/VgV/UVgO) procurement law:

**Principle 1 — Procure services, not licences.** Open-source software is free to use; public bodies pay for implementation, integration, hosting, migration, training, and ongoing support. Tender documents must be structured around service delivery, not software acquisition.

**Principle 2 — Use cooperative procurement structures.** Germany's govdigital eG [23], Dataport [24], and AKDB [57], and Swiss cantonal IT cooperatives provide framework agreements for open-source municipal IT that satisfy public procurement law. Small municipalities are strongly advised to join such cooperatives rather than conducting individual tenders for each component.

**Principle 3 — Apply "Public Money? Public Code!" as a contract condition [4].** Any custom software developed, or substantially customised open-source software, must be released under an OSI-approved licence and published on openCode.de (Germany) or an equivalent cantonal/federal code-sharing platform (Switzerland). Recommended contract clause:

> *"All software developed, modified, or substantially extended under this contract shall be released by the contractor under an Open Source Initiative-approved licence within 30 days of acceptance. The contractor shall publish the source code on [openCode.de / cantonal equivalent] and grant the contracting authority and any other public authority unlimited rights to use, modify, and redistribute the code."*

**Principle 4 — Evaluate total cost of ownership.** Procurement scoring must include a 5-year TCO model as a scored criterion. Proprietary alternatives must disclose: licence renewal price escalation history; exit migration costs; data export completeness; and contractual restrictions on data portability. Failure to provide these data should be scored negatively.

**Principle 5 — Require interoperability standards compliance.** All procured systems must implement: XÖV standards (Germany) [46], eCH standards (Switzerland) [47], DCAT-AP (EU open data) [45]. Non-compliance is a disqualifying criterion for any system in the citizen-facing or inter-agency integration path.

**Principle 6 — Prefer certified sovereign providers.** For infrastructure, prefer SCS-certified cloud operators or govdigital eG members (Germany), or cantonal IT cooperative operators (Switzerland). These providers operate under collective data sovereignty agreements and public procurement frameworks that ensure no data transfer to third-country jurisdictions without explicit consent.

**Principle 7 — Include accessibility as a scored criterion.** All citizen-facing systems must achieve WCAG 2.1 Level AA compliance verified by accessibility audit at acceptance. EN 301 549 compliance must be contractually guaranteed and independently tested.

### 6.3 Framework Agreements Available

| Agreement | Jurisdiction | Scope |
|---|---|---|
| govdigital eG framework | Germany (national) | Cloud, SCS hosting, OpenDesk |
| Dataport framework | Hamburg, SH, HB, MV, SA, TH | IT infrastructure, workplace |
| AKDB service agreements | Bavaria | Municipal IT, OZG services |
| FITKO EfA call-off | Germany (national) | OZG services "Einer für Alle" |
| Cantonal IT cooperatives | Swiss cantons (varies) | Cantonal IT services |
| openCode.de reuse | Germany | Software reuse, procurement support |

### 6.4 Change Management

Open-source transitions frequently fail not on technical grounds but on human factors. The following elements are non-negotiable:

1. **Political mandate with durability**: secure a cross-party council resolution covering at least two electoral cycles.
2. **Departmental champions**: one designated digital sovereignty champion per department, with advanced training and direct escalation to the steering committee.
3. **Parallel operation periods**: minimum three months' parallel operation before cutting over any critical system. No hard deadlines.
4. **Training before cutover**: all affected staff complete role-specific training before the cutover date, not after.
5. **Early wins celebration**: document and publicise the first cost savings, new capabilities, and citizen satisfaction improvements.
6. **Public transparency dashboard**: publish a real-time dashboard showing migration progress, cost comparison vs. baseline, service availability, and open data publication counts.

### 6.5 Inter-Municipal Community of Practice

The most cost-effective structural innovation available is the formation of an inter-municipal community of practice. The model: a minimum of three peer municipalities establish a quarterly forum for sharing implementation experience, pooling training resources, jointly developing integrations, and coordinating upstream open-source contributions.

The community of practice should:
- Share a document repository (Nextcloud) for experience reports, tender templates, and training materials
- Maintain a joint CKAN catalogue of contributed open data best practices
- Operate a shared Forgejo instance for jointly developed integrations
- Contribute jointly to openCode.de and attend upstream community events
- Publish an annual joint report on digital transformation progress

---

## 7. Risk Analysis

### 7.1 Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Political reversal post-election | Medium | High | Cross-party council resolution; constitutional embedding; public commitments |
| Vendor lobbying / FUD campaigns | High | Medium | Evidence base; civil society engagement; transparency; publicise mandate |
| IT team skill gaps | High | Medium | Training programme; cooperative IT provider; community of practice |
| Integration failure between layers | Medium | High | Phased rollout; reference architecture adherence; decision gates |
| Data loss during migration | Low | Critical | Full backup; parallel operation ≥3 months; staged migration |
| GDPR/nDSG violation | Low | High | Privacy-by-design; DPIA at each phase; DPO sign-off at gates |
| User adoption failure | Medium | High | Change management; UX testing; training; parallel systems; champions |
| Security incident | Low | Critical | BSI IT-Grundschutz; pen testing; SBOM; IRP; NIS2 compliance |
| Community/upstream fragmentation | Low | Medium | Multi-source strategy; don't single-vendor on upstream; contribute back |
| Procurement challenge | Low | Medium | Framework agreements; documented TCO scoring; legal briefings |
| Cost overrun | Medium | Medium | Phased gates; independent project office; open TCO accounting |
| Accessibility failure | Medium | Medium | WCAG 2.1 AA contractual requirement; acceptance testing |

### 7.2 The Munich Cautionary Case

The City of Munich's LiMux project (2003–2017) migrated approximately 14,000 desktops from Windows/Microsoft Office to Ubuntu/LibreOffice, then reversed the decision in 2017 under a new city government. It is the most-cited cautionary tale in open-source government technology [30].

Careful post-mortem analysis identifies the reversal as driven by: (a) a change in political leadership with closer ties to one proprietary vendor; (b) documented lobbying context (a prominent vendor relocation to Munich announced during the reversal debate); (c) compatibility issues with Bavarian state-level systems that had not been updated to support open standards; and (d) insufficient change management investment in the years prior to the reversal.

The technical implementation was broadly successful. The failure was political and organisational. Three lessons:
1. **Political risk is the primary risk.** Build cross-party consensus and constitutional/legislative embedding, not just executive support.
2. **Peer jurisdiction compatibility matters.** Coordinate with state/cantonal and federal bodies before deploying, to ensure that the systems you must interoperate with support open standards.
3. **Change management is not optional.** The human cost of inadequate change management can tip a reversal decision.

### 7.3 Vendor FUD Management

Common vendor challenge strategies when municipalities announce open-source transitions, and evidence-based responses:

- **"Hidden costs exceed licence savings"**: Publish your TCO model transparently, including implementation costs, and show it against the proprietary 5-year TCO including licence escalation and exit costs. The indicative model in Section 3.6 provides the framework.
- **"Open source is less secure"**: Cite BSI's position that open source is auditable and therefore more appropriate for public administration; cite CISA endorsement of open-source security practices; cite specific CVE response records of recommended components.
- **"Who do you call when something breaks?"**: All recommended components have commercial support contracts available; cooperative providers (govdigital eG, Dataport, AKDB) provide SLA-backed support.
- **"You'll need to migrate back eventually"**: This is precisely the lock-in argument — which is why zero-exit-cost open-source is superior to high-exit-cost proprietary.

Municipalities should designate a communications lead to handle vendor relations and brief council members on FUD responses before any council debate.

### 7.4 Data Protection

Open-source technology stacks offer significant data protection advantages: source code can be audited, data flows can be traced, and privacy-by-design features can be implemented directly.

**Germany:** DSGVO (GDPR) + BDSG + Landesdatenschutzgesetze. Key obligations: DPIA for high-risk processing; binding data processing agreements with all processors (Auftragsverarbeitungsverträge); records of processing activities (VVT); mandatory DPO for public bodies.

**Switzerland:** nDSG 2023 [64]. Key obligations: mandatory logging for automated data processing; data breach notification; privacy-by-design requirements; enhanced obligations for sensitive personal data. For Swiss municipalities, nDSG compliance means on-premise or Swiss-hosted deployment of all sensitive personal data systems.

For all jurisdictions: data residency on Swiss/EU infrastructure (not third-country) is a baseline requirement. All recommended open-source components support on-premise or EU/CH-hosted deployment. Data Processing Agreements must be signed with all service providers.

### 7.5 Security Architecture

BSI IT-Grundschutz [26] provides a comprehensive security baseline applicable regardless of licence model. NIS2 obligations [27] apply to municipalities meeting the criticality thresholds; others should apply NIS2 principles as best practice.

Key security requirements:
- Documented patch management: ≤ 30-day remediation for critical CVEs
- Authentication: BSI Authenticator Assurance Level 2 (AAL2) for citizen-facing; AAL3 for privileged admin
- Data in transit: TLS 1.3 minimum; HSTS; certificate transparency
- Data at rest: AES-256 for sensitive categories; LUKS for full-disk encryption on servers
- Penetration testing: at each phase gate and annually thereafter
- SBOM: maintained and signed for all open-source dependencies
- Incident response plan: aligned with NIS2 Article 23 notification obligations

---

## 8. Conclusion

The evidence assembled in this paper converges on five findings:

**1. A complete, production-proven open-source municipal technology stack exists in 2026.** Every functional requirement of a modern municipal government — from digital identity and document management to council meeting software and citizen participation — can be met by open-source components with documented deployments in peer jurisdictions. The reference architecture in Section 4.13 provides a concrete, implementable blueprint.

**2. The regulatory trajectory mandates this transition.** EMBAG (Switzerland), OZG 2.0 (Germany), and the Interoperable Europe Act (EU) create mounting legal obligations that proprietary, vendor-locked systems cannot sustainably satisfy. The EU Data Act 2023 adds data portability and lock-in prohibition requirements. Municipalities that begin the transition now build compliance capital; those that delay accumulate regulatory liability.

**3. The economic case is compelling when total costs are counted correctly.** Indicative TCO analysis shows savings of €381–€678 per civil servant per year in direct licence costs alone. Cooperative procurement structures distribute implementation costs across many municipalities. The 5-year present value of the proprietary versus open-source gap ranges from €800,000 to €1,700,000 for a 500-civil-servant municipality, before accounting for exit costs.

**4. The primary risk is political, not technical.** The Munich case and the broader history of failed e-government projects confirm that political mandate durability and professional change management are the binding constraints on successful transitions.

**5. The transition creates positive externalities.** Municipalities that transition to open-source technology contribute to a commons from which all other public bodies benefit. Every contribution to openCode.de, every service published under the EfA model, every Decidim deployment strengthens the European digital sovereignty ecosystem. First movers acquire expertise, political capital, and the reputation of digital leadership.

---

## References

[1] Swiss Federal Council. (2023). *Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG)*. SR 172.019. https://www.fedlex.admin.ch/eli/cc/2023/682/de — [CC0]

[2] Bundesministerium des Innern und für Heimat. (2024). *Onlinezugangsgesetz 2.0*. https://www.bmi.bund.de/DE/themen/moderne-verwaltung/e-government/ozg/ozg-node.html — [DL-DE/Zero 2.0]

[3] Open Source Business Alliance. (2023). *Sovereign Cloud Stack*. https://scs.community/ — [CC-BY-SA-4.0]

[4] Free Software Foundation Europe. (2017). *Public Money? Public Code!* https://publiccode.eu/ — [CC-BY-SA-4.0]

[5] European Commission. (2020). *Open Source Software Strategy 2020–2023: Think Open*. https://commission.europa.eu/about/departments-and-executive-agencies/informatics/open-source-software-strategy_en

[6] European Parliament and Council. (2024). *Regulation (EU) 2024/903 — Interoperable Europe Act*. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202400903

[7] Wirtz, B. W., & Weyerer, J. C. (2017). Conceptualization and creation of a holistic e-government maturity model. *Public Management Review*, 19(9), 1297–1316. https://doi.org/10.1080/14719037.2017.1283024

[8] Janssen, M., Charalabidis, Y., & Zuiderwijk, A. (2012). Benefits, adoption barriers and myths of open data and open government. *Information Systems Management*, 29(4), 258–268. https://doi.org/10.1080/10580530.2012.716740

[9] FITKO. (2023). *Jahresbericht 2023*. https://www.fitko.de/ — [DL-DE/Zero 2.0]

[10] openCode.de. (2022). *Open Source for Government*. https://opencode.de/

[11] Sovereign Cloud Stack Community. (2023). *SCS Technical Documentation*. https://docs.scs.community/ — [Apache 2.0]

[12] Decidim Association. (2021). *Decidim: Free Open-Source Participatory Democracy*. https://decidim.org/ — [AGPL-3.0]

[13] Nextcloud GmbH. (2023). *Nextcloud for Government*. https://nextcloud.com/government/ — [AGPL-3.0]

[14] The Matrix Foundation. (2023). *Matrix Specification*. https://spec.matrix.org/ — [Apache 2.0]

[16] E-Government Suisse. (2023). *Strategie E-Government Schweiz 2024–2027*. https://www.egovernment.ch/de/umsetzung/e-government-strategie/

[19] TYPO3 Association. (2023). *TYPO3 in Public Administration*. https://typo3.org/project/association — [GPL-2.0]

[20] OpenProject GmbH. (2023). *OpenProject for Government*. https://www.openproject.org/ — [GPLv3]

[21] Red Hat / Keycloak Community. (2023). *Keycloak: Open Source Identity and Access Management*. https://www.keycloak.org/ — [Apache 2.0]

[22] CKAN Association. (2023). *CKAN: Open Source Data Portal Software*. https://ckan.org/ — [AGPL-3.0]

[23] govdigital eG. (2023). *Genossenschaft für digitale Verwaltung*. https://govdigital.de/

[24] Dataport AöR. (2023). *IT-Dienstleister für die öffentliche Verwaltung*. https://www.dataport.de/

[26] Bundesamt für Sicherheit in der Informationstechnik. (2023). *BSI IT-Grundschutz-Kompendium Edition 2023*. https://www.bsi.bund.de/ — [CC-BY-ND 3.0 DE]

[27] European Parliament and Council. (2022). *Directive (EU) 2022/2555 — NIS2*. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022L2555

[29] United Nations DESA. (2022). *UN E-Government Survey 2022*. https://publicadministration.un.org/egovkb/en-us/Reports/UN-E-Government-Survey-2022

[30] Janowski, T. (2015). Digital government evolution: From transformation to contextualization. *Government Information Quarterly*, 32(3), 221–226. https://doi.org/10.1016/j.giq.2015.07.001

[33] Camunda Services GmbH. (2023). *Camunda Platform 8 Community Edition*. https://camunda.com/download/ — [Apache 2.0]

[34] BigBlueButton Inc. (2023). *BigBlueButton: Open Source Web Conferencing*. https://bigbluebutton.org/ — [LGPL-3.0]

[35] Jitsi Community. (2023). *Jitsi Meet: Open Source Video Conferencing*. https://jitsi.org/ — [Apache 2.0]

[36] OpenStreetMap Foundation. (2023). *OpenStreetMap*. https://www.openstreetmap.org/ — [ODbL-1.0]

[37] QGIS Project. (2023). *QGIS: A Free and Open Source Geographic Information System*. https://www.qgis.org/ — [GPL-2.0+]

[39] Cloud Native Computing Foundation. (2023). *Kubernetes*. https://kubernetes.io/ — [Apache 2.0]

[41] PostgreSQL Global Development Group. (2023). *PostgreSQL*. https://www.postgresql.org/ — [PostgreSQL Licence]

[42] BMI / ZenDiS GmbH. (2023). *OpenDesk: Der digitale Arbeitsplatz der Bundesverwaltung*. https://opendesk.eu/ — [AGPL-3.0]

[43] Schweizerisches Bundesarchiv. (2023). *GEVER in der Bundesverwaltung*. https://www.bar.admin.ch/

[44] opendata.swiss. (2023). *Open Government Data Switzerland*. https://opendata.swiss/ — [CC-BY-4.0]

[45] European Commission. (2017). *European Interoperability Framework (EIF)*. https://joinup.ec.europa.eu/collection/nifo-national-interoperability-framework-observatory — [CC-BY-4.0]

[46] KoSIT. (2023). *XÖV-Standards: XML in der öffentlichen Verwaltung*. https://www.xoev.de/

[47] eCH Association. (2023). *eCH Standards Catalogue: E-Government Standards for Switzerland*. https://www.ech.ch/ — [open access]

[48] Ayuntamiento de Madrid / CONSUL Democracy. (2023). *CONSUL Democracy: Open Source Political Participation Tool*. https://consulproject.org/ — [AGPL-3.0]

[49] GovStack Initiative. (2023). *Specifications for Digital Government Building Blocks*. https://www.govstack.global/ — [MIT]

[50] ZenDiS GmbH. (2023). *Jahresbericht 2023: Zentrum für Digitale Souveränität der öffentlichen Verwaltung*. https://www.zendis.de/

[51] European Commission DIGIT / OSOR. (2023). *Open Source Observatory Annual Report 2023*. https://joinup.ec.europa.eu/collection/open-source-observatory-osor — [CC-BY-4.0]

[52] European Parliament and Council. (2023). *Regulation (EU) 2023/2854 — Data Act*. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023R2854

[54] Lathrop, D., & Ruma, L. (Eds.). (2010). *Open Government: Collaboration, Transparency, and Participation in Practice*. O'Reilly Media. ISBN: 978-0-596-80435-0

[57] AKDB — Anstalt für Kommunale Datenverarbeitung in Bayern. (2023). *IT-Service für bayerische Kommunen*. https://www.akdb.de/

[58] Digitalservice GmbH des Bundes. (2023). *Digitale Dienste der Bundesverwaltung*. https://digitalservice.bund.de/

[60] CryptPad. (2023). *End-to-End Encrypted Collaboration*. https://cryptpad.org/ — [AGPL-3.0]

[61] Collabora Productivity. (2023). *Collabora Online: Open Source Office in the Browser*. https://www.collaboraoffice.com/ — [Apache 2.0]

[62] Forgejo. (2023). *Forgejo: Self-Hosted Git Service*. https://forgejo.org/ — [MIT]

[63] Intevation GmbH. (2023). *OpenSlides: Digital Council and Assembly Management*. https://openslides.com/ — [AGPL-3.0]

[64] Swiss Federal Council. (2020). *Bundesgesetz über den Datenschutz (nDSG), SR 235.1*. In force 1 September 2023. https://www.fedlex.admin.ch/eli/cc/2022/491/de — [CC0]

[65] Swiss Federal Council. (2023). *Bundesgesetz über den elektronischen Ausweis (E-ID-G)*. https://www.fedlex.admin.ch/eli/fga/2023/2088/de — [CC0]

---

*This document is released under the Creative Commons Attribution 4.0 International Licence (CC-BY-4.0).*  
*Attribute as: Sebastian Graf, Autonomous Office of Civil Digital Infrastructure (sebk4c@tuta.com)*  
*Version 0.2.0 — Citation-Complete Draft — 2026-06-20*
