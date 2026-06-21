---
title: "Sovereign by Design: A State-of-the-Art Open-Source Technology Strategy for Municipal Governments"
author: "Sebastian Graf"
affiliation: "Autonomous Office of Civil Digital Infrastructure"
email: "sebk4c@tuta.com"
version: "0.2.0"
status: "Citation-Complete Draft"
date: "2026-06-21"
SPDX-License-Identifier: CC-BY-4.0
lang: en
source-of-truth: true
keywords:
  - digital sovereignty
  - open-source software
  - municipal government
  - e-government
  - public administration
  - OZG
  - EMBAG
  - sovereign cloud
  - GovTech
  - civic technology
changelog:
  - version: "0.1.0"
    date: "2026-06-20"
    description: "First structured draft — sections, initial technology survey, 30 sources"
  - version: "0.2.0"
    date: "2026-06-21"
    description: "Citation-complete draft — 55 verified references; new sections 3.6, 3.7, 4.10, 6.4, 7.4; cost ranges per phase; compliance matrices; Appendices A–C"
---

# Sovereign by Design: A State-of-the-Art Open-Source Technology Strategy for Municipal Governments

**Author:** Sebastian Graf  
**Organisation:** Autonomous Office of Civil Digital Infrastructure  
**Contact:** sebk4c@tuta.com  
**Version:** 0.2.0 — Citation-Complete Draft  
**Date:** 2026-06-21  
**Licence:** CC-BY-4.0

---

## Abstract

Municipal governments across Europe face an unprecedented convergence of pressures: accelerating obligations under national digitalisation mandates such as Germany’s Onlinezugangsgesetz 2.0 [2] and Switzerland’s Federal Electronic Means Act (EMBAG) [1]; rising cybersecurity requirements under the NIS2 Directive [27]; growing citizen expectations for accessible, responsive public services; and a structural dependency on a small number of proprietary software vendors whose licensing costs consume an increasing share of constrained public budgets. The concept of digital sovereignty — the capacity of public institutions to control, audit, adapt, and sustain their own digital infrastructure — has moved from academic abstraction to operational policy imperative.

This paper presents a comprehensive, evidence-based open-source technology strategy for municipal governments with populations in the range of 50,000 to 200,000 inhabitants, with primary reference to the German and Swiss regulatory contexts and secondary applicability across the European Union. Drawing on a systematic literature review of 55 peer-reviewed and grey-literature sources, comparative analysis of municipal deployments in Barcelona, Munich, Schleswig-Holstein, and Swiss cantons, and structured evaluation of eleven technology domains, the paper argues that a coherent open-source stack — built on identifiable, mature, community-supported components — can meet or exceed the functional requirements of proprietary alternatives while delivering measurable reductions in long-run total cost of ownership, eliminating single-vendor dependencies, and producing digital public goods that benefit the wider civic commons.

The strategy is organised around a phased implementation roadmap covering six phases from organisational readiness through operational excellence, with indicative cost ranges calibrated to a medium-sized municipality. A stakeholder and procurement framework addresses the political economy of technology transition, including change management, legal compliance, and inter-municipal cooperation structures. A risk register and regulatory risk matrix identify the principal failure modes, with Munich’s LiMux transition as the canonical cautionary case. Three appendices provide operational tools: a procurement checklist of twenty-three questions, a seven-criterion technology evaluation scoring matrix, and a fifteen-question municipal digital sovereignty self-assessment instrument.

The paper concludes that digital sovereignty is not a utopian aspiration but an achievable engineering and governance outcome, provided that municipalities approach the transition with appropriate preparation, realistic cost expectations, and sustained political commitment. Public money should produce public code [4].

**Keywords:** digital sovereignty, open-source government, GovTech, municipal digital transformation, interoperability, OZG, EMBAG, Sovereign Cloud Stack, e-government, civic technology

---

## 1. Introduction

The digital transformation of public administration is no longer optional. Citizens in democratic societies increasingly expect government services to be available, accessible, and trustworthy across digital channels. At the same time, the institutional structures through which municipalities deliver those services — legacy enterprise software stacks, proprietary cloud dependencies, bilateral vendor agreements — were largely designed for a different era and a different threat environment.

The European Union’s 2030 Digital Compass [51] sets an explicit target that all key public services should be available online by 2030 and that 100 percent of citizens should have access to electronic identity documents. The Interoperable Europe Act [6] requires public sector bodies to assess the interoperability of digital components before procurement. Germany’s OZG 2.0 [2] mandates federated online service delivery across federal, state, and municipal levels. Switzerland’s EMBAG [1] requires that software developed with federal funds be published as open source unless specific exceptions apply. These legislative signals are directionally consistent: European public administration is moving, haltingly but unmistakably, toward open, interoperable, and accountable digital infrastructure.

### 1.1 The European Moment for Digital Sovereignty

The term “digital sovereignty” entered mainstream policy discourse following a series of disruptions that exposed the fragility of European public-sector technology dependencies: the 2020 SolarWinds supply-chain attack, repeated outages of US-headquartered cloud providers, and legal uncertainties arising from the invalidation of Privacy Shield and the subsequent Schrems II ruling on transatlantic data transfers. The European Commission’s Open Source Strategy 2020–2023 [5] explicitly identified open-source software as a strategic enabler of digital sovereignty. The Open Source Observatory (OSOR) [28, 53] has catalogued hundreds of replicable government open-source deployments across member states.

For municipalities specifically, the sovereignty question is acute. A mid-sized German city of 80,000 inhabitants may spend €2–5 million per year on software licences, maintenance contracts, and cloud subscriptions to a handful of vendors. The marginal leverage of that municipality in any individual negotiation is negligible. Collective action — through shared platforms, cooperative procurement, and inter-municipal development consortia — is the structural alternative. Institutions such as govdigital eG [23], Dataport AöR [24], and ZenDiS GmbH [25] represent emerging German models of exactly this kind.

### 1.2 Scope and Definitions

For the purposes of this paper:

**Municipal government** refers to the executive and administrative functions of a city or municipality (Gemeinde / Gemeinderat) with a population between approximately 50,000 and 200,000, primarily in Germany and Switzerland, with generalisation to comparable EU jurisdictions.

**Digital sovereignty** is defined as the capacity of a public institution to govern its own digital infrastructure: to choose, deploy, audit, modify, and if necessary replace the software components that underpin its administrative functions, without structural dependency on any single private vendor. This definition synthesises academic treatments by Janowski [30], the OECD Digital Government Policy Framework [49], and the operational framing of the GovStack Initiative [31].

**Open-source software (OSS)** refers to software licensed under an Open Source Initiative-approved licence, making the source code available for inspection, modification, and redistribution. The paper follows the taxonomy of the European Interoperability Framework (EIF) [45] in distinguishing between software freedom (licence) and operational autonomy (deployment and hosting).

**Technology stack** refers to the layered ensemble of software components — from infrastructure through middleware to citizen-facing applications — that together constitute a municipality’s digital operating environment.

### 1.3 Research Questions

This paper addresses four primary research questions:

**RQ1:** What open-source technology components are sufficiently mature, well-governed, and publicly deployed to constitute a credible municipal digital stack in the 2024–2028 planning horizon?

**RQ2:** What is the comparative total cost of ownership of open-source versus proprietary alternatives at municipal scale, taking into account licence, implementation, operations, and transition costs?

**RQ3:** What governance, procurement, and change-management structures maximise the probability of a successful open-source transition for a medium-sized municipality?

**RQ4:** What regulatory requirements — at EU, national, and cantonal/Länder levels — must a municipal open-source strategy satisfy, and how do open-source components support or complicate compliance?

---

## 2. Methodology

### 2.1 Systematic Literature Review

The literature review was conducted following an adapted PRISMA framework. Search queries covering the terms “open source government”, “digital sovereignty municipality”, “e-government open source”, “OZG open source”, “EMBAG open source”, “municipal cloud”, and combinations thereof were executed against Google Scholar, BASE (Bielefeld Academic Search Engine), and the Joinup / OSOR repository [28, 53]. Publication dates were restricted to 2000–2026, with preference for post-2015 material except for foundational theoretical works. The reference list of 55 sources was curated from an initial retrieval of approximately 280 candidate items.

### 2.2 Comparative Policy Analysis

Policy documents from Germany (OZG 2.0 [2], Digitalstrategie Deutschland [50], FIM [32], FITKO Jahresbericht [9], ZenDiS [25, 42]), Switzerland (EMBAG [1], E-Government Strategie Schweiz 2024–2027 [16], BGEID [38], eCH standards [17], GEVER [43], opendata.swiss [44]), and the European Union (Interoperable Europe Act [6], EU Open Source Strategy [5], EIF [45], NIS2 [27], 2030 Digital Compass [51]) were systematically reviewed to identify mandatory requirements, recommended architectures, and incentive structures relevant to municipal OSS adoption.

### 2.3 Technology Evaluation Framework

Each technology domain was evaluated against a seven-criterion scoring matrix (detailed in Appendix B): Licence Openness, Deployment Maturity, Community Health, Interoperability, Security, Total Cost of Ownership, and Public-Sector Deployments. Scores were drawn from vendor and community documentation, OSOR case studies, BSI IT-Grundschutz compatibility assessments [26], and peer-reviewed evaluations where available.

### 2.4 Stakeholder Analysis

Stakeholder categories were identified through the GovStack Building Blocks framework [31], the Wirtz–Weyerer e-government maturity model [7], and analysis of German Digitallotsen and Swiss E-Government Schweiz implementation structures [16]. Stakeholder interests, influence levels, and engagement strategies were mapped using a modified power–interest matrix.

### 2.5 Inclusion/Exclusion Criteria

**Included:** Software components with an OSI-approved licence; active upstream community (commit activity within 12 months); documented production deployments in public administration; compatibility with EU/DE/CH regulatory requirements; sufficient documentation for independent deployment.

**Excluded:** Components under a single-vendor source-available licence without OSI approval; components with no public-sector reference deployments; components with unresolved security advisories rated CVSS ≥9.0 at time of writing.

### 2.6 Limitations

This paper is a strategic policy document, not a controlled empirical study. Cost figures are indicative ranges derived from published case studies and procurement data rather than primary field research. Technology assessments reflect the state of upstream projects as of mid-2026 and will require regular review. The paper’s primary regulatory frame is German and Swiss; municipalities in other EU member states should verify applicability of specific legislative references. The Munich LiMux case is treated as a cautionary illustration, not a falsification of the general open-source proposition.

---

## 3. Literature Review

### 3.1 Theoretical Foundations

The academic study of electronic government has evolved through several distinct phases. Lucke and Reinermann’s Speyerer Definition [47] established the foundational vocabulary for German-language e-government scholarship: the provision of government information and services via electronic networks, structured along the axes of Government-to-Citizen (G2C), Government-to-Business (G2B), and Government-to-Government (G2G) interactions. Dunleavy et al.’s Digital Era Governance [54] offered a structural critique of new public management’s IT outsourcing pathologies — fragmentation, agencification, and single-vendor dependency — and prefigured many of the sovereignty concerns that animate current policy.

Janowski [30] articulated a four-stage digital government evolution model — digitisation, transformation, engagement, and contextualisation — that provides a developmental framework for assessing municipal readiness. The OECD Digital Government Policy Framework [49] operationalised digital government as a multidimensional construct encompassing digital by design, data-driven public sector, government as a platform, open by default, user-driven, and proactiveness. Scholl [55] provided a reflective survey of the field’s intellectual trajectory. Bertot, Jaeger and Grimes [48] established the empirical linkage between ICT deployment and transparency outcomes — a central justification for the open-data components of the stack described in Section 4.

### 3.2 Digital Sovereignty

Digital sovereignty as a policy concept lacks a single canonical definition. This paper adopts a composite definition synthesising the FSFE’s “Public Money? Public Code!” manifesto [4], the European Commission’s Open Source Strategy [5], and the GovStack Building Blocks framing [31]. At its core, sovereignty requires: auditability (the ability to inspect code), modifiability (the ability to adapt code to local requirements), portability (the ability to migrate away from a vendor or hosting provider without prohibitive switching costs), and accountability (clear governance over who controls the software and its data).

The Interoperable Europe Act [6] operationalises a dimension of sovereignty through mandatory interoperability assessment, requiring public sector bodies to conduct and publish interoperability assessments before deploying new ICT solutions. The “Public Money? Public Code!” principle [4] has been formally adopted by a growing number of European municipal and regional governments. Lathrop and Ruma [15] provide the normative foundation linking open government — characterised by transparency, collaboration, and participation — to open-source infrastructure as a necessary (though not sufficient) condition.

### 3.3 The German OZG Ecosystem

Germany’s Onlinezugangsgesetz (OZG), enacted in 2017 and substantially revised as OZG 2.0 in 2024 [2], is the legislative spine of German municipal digitalisation. OZG 2.0 introduces the principle of “Once Only” — citizens should not need to submit the same data to multiple government offices — and establishes a federal marketplace of digitalised administrative services (Leistungen) that municipalities can consume. FITKO (Föderale IT-Kooperation) coordinates the technical implementation across Länder [9]. The Föderales Informationsmanagement (FIM) programme [32] provides the semantic standards (FIM-Prozesse, FIM-Leistungen, FIM-Daten) necessary for cross-jurisdictional service reuse.

The openCode.de platform [10], operated by Digitalservice GmbH des Bundes, provides a public code repository for federal and state OSS components that municipalities can reuse. govdigital eG [23] and Dataport AöR [24] provide cooperative hosting and managed-service models that reduce the operational burden on individual municipalities. ZenDiS GmbH [25] — the Centre for Digital Sovereignty — coordinates the OpenDesk federal workplace suite [42] and advises public bodies on sovereignty-compatible procurement. AKDB (Anstalt für Kommunale Datenverarbeitung in Bayern) [18] serves Bavarian municipalities with shared IT services and has begun integrating open-source components into its service catalogue. The XÖV standards [46], developed by KoSIT, provide XML-based data exchange formats for inter-administrative communication, underpinning the technical interoperability that OZG 2.0 requires.

### 3.4 Swiss Cantonal and Federal Digital Services

Switzerland’s digital government landscape is shaped by its federal structure: the Confederation, 26 cantons, and approximately 2,200 municipalities each exercise significant administrative autonomy. The EMBAG [1] — Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben, in force since 1 January 2024 — is a landmark provision: Article 9 requires that software developed by or for federal authorities be published as open source unless security, third-party rights, or disproportionate effort exceptions apply. This “Open Source by Default” mandate represents one of the most progressive OSS requirements in European public administration.

The E-Government Strategie Schweiz 2024–2027 [16] identifies interoperability, digital identity, and data reuse as the three strategic pillars. The eCH standards body [17] publishes technical standards for e-government data exchange that parallel Germany’s XÖV but reflect Swiss constitutional peculiarities including quadrilingual administration. The Bundesgesetz über den elektronischen Identitätsnachweis (BGEID) [38] establishes the legal basis for the Swiss electronic identity (E-ID), based on a decentralised, privacy-preserving wallet model. The Schweizerisches Bundesarchiv’s GEVER framework [43] governs electronic records management across federal agencies. opendata.swiss [44] is the Swiss national open data portal, providing a federated catalogue of machine-readable government datasets under standardised licences.

### 3.5 Open Source Communities and Sovereign Technology

The open-source ecosystem for public administration has matured substantially since the first wave of government Linux deployments in the early 2000s. The OSOR [28, 53] catalogues over 700 public-sector OSS deployments across EU member states. The FSFE [4] continues to advocate for open-source procurement mandates and has achieved formal endorsements from multiple European cities and regions. GovStack [31] provides a building-blocks specification that maps generic government service components to open-source reference implementations, facilitating reuse across jurisdictions.

Community governance is a material risk factor. The GovStack framework [31] distinguishes between foundation-governed projects (e.g., Nextcloud under the Nextcloud GmbH + community dual model [13]), consortium-governed projects (e.g., Sovereign Cloud Stack under OSBA governance [3, 11]), and municipality-governed forks (carrying highest maintenance risk). For sovereign deployment, this paper recommends preference for foundation-governed and consortium-governed projects with demonstrated public-sector adoption.

### 3.6 Total Cost of Ownership and Economic Evidence

The economics of municipal software are frequently misrepresented in both pro-proprietary and pro-open-source advocacy. A balanced TCO analysis must encompass: licence fees, implementation and integration costs, operational staffing, training, support contracts, migration costs, and the opportunity cost of lock-in.

**Proprietary benchmark costs.** Microsoft 365 Government licensing (G3/G5 tiers) typically costs €150–400 per user per year for core productivity and collaboration suites, exclusive of additional modules, compliance add-ons, Azure hosting, and implementation services. For a municipality of 800 staff, annual licence exposure is therefore €120,000–320,000 for productivity software alone, before infrastructure and line-of-business applications.

**Open-source TCO evidence.** Barcelona’s digital transformation programme (2016–2019), anchored by the Decidim participatory democracy platform [12] and an explicit ethical digital standards policy, reportedly saved the city €30–40 million over four years through reduced proprietary licensing and in-sourced development. Schleswig-Holstein announced in 2021 a structured migration of 25,000 state workstations to LibreOffice and Linux, with the Land government citing licence cost reductions as a primary driver. The OpenDesk project [42] is building the federal evidence base for German-language open-source productivity suites.

**Munich LiMux (cautionary data).** The Munich LiMux migration (2003–2013) converted approximately 15,000 workstations to Linux and LibreOffice, reportedly saving €10 million in licence costs. The subsequent reversal (2017–2021, return to Windows/Microsoft 365) is frequently cited as evidence that open-source fails at scale. A careful reading of the Munich post-mortem literature reveals that the reversal was primarily driven by: political change of municipal leadership, inadequate change management and staff training investment, compatibility issues with state-government Windows-dependent workflows, and a deliberate political decision rather than demonstrated technical failure.

**Swiss evidence.** Swiss cantonal administrations that have adopted open-source components through eCH-standardised interfaces [17] and the GEVER framework [43] report that interoperability standardisation — rather than licence choice per se — is the primary TCO driver. Municipalities that adopt eCH-compliant open-source components benefit from shared data models, reducing integration costs. The OSOR Annual Report [28] and the Joinup platform [53] provide the most comprehensive comparative dataset currently available for European government OSS TCO.

### 3.7 Citizen Experience and Digital Inclusion

Digital sovereignty is not only an institutional concern. Citizens interact with municipal digital services across a wide spectrum of technical capability, linguistic background, and access to devices. The OECD [49] and the UN E-Government Survey [29] both document persistent digital divides that open-source strategies must explicitly address.

**Accessibility.** The EU Web Accessibility Directive (2016/2102) and implementing Decision (EU) 2018/1524 require public-sector websites and mobile applications to conform to WCAG 2.1 Level AA. In Germany, BITV 2.0 (Barrierefreie-Informationstechnik-Verordnung) transposes this requirement. In Switzerland, P028 federal accessibility guidelines apply. Municipalities selecting open-source CMSs, citizen portals, and participation platforms must verify WCAG 2.1 AA compliance. TYPO3 [19] and Decidim [12] maintain active accessibility working groups and publish conformance statements.

**Multilingual requirements.** Swiss municipalities may need to serve citizens in German, French, Italian, or Romansh. German municipalities in border regions increasingly provide services in Turkish, Arabic, and other community languages. Open-source CMS and portal platforms generally support multilingual content through established modules, but municipalities must budget for translation workflows and content governance.

**Citizen trust.** The UN E-Government Survey [29] identifies citizen trust as the most significant demand-side barrier to e-government adoption. Trust is built through transparency (open source provides auditability), data protection (GDPR compliance, data minimisation), and service reliability. The FSFE [4] and Janssen et al. [8] both argue that open-source e-government infrastructure has intrinsic trust-building properties relative to black-box proprietary systems.

**Inclusive service design.** Janssen, Charalabidis and Zuiderwijk [8] identify service design — not technology choice — as the primary determinant of open-data and e-government adoption by citizens. Open-source platforms are a necessary but not sufficient condition for inclusive digital services. Municipalities must invest in UX research, plain-language content, and assisted-digital support channels alongside technical platform deployment.

### 3.8 Gaps and Agenda

The literature reveals several significant gaps:

- Longitudinal TCO studies at municipal scale, comparing full-stack open-source versus proprietary deployments over five-year-plus horizons, are largely absent. The Munich case is illustrative but confounded by political variables.
- Regulatory interoperability between the German OZG ecosystem and Swiss EMBAG/eCH frameworks has not been systematically mapped; cross-border municipalities face unstudied compliance complexity.
- AI governance in public administration is an emerging area; sovereign AI deployment at municipal level has no established literature base as of mid-2026.
- Citizen trust in open-source e-government specifically has not been empirically studied in European municipal contexts.

---

## 4. Technology Stack Analysis

The following sections evaluate eleven technology domains against the seven-criterion framework described in Appendix B.

### 4.1 Digital Identity — Keycloak

**Recommended component:** Keycloak [21] | **Licence:** Apache 2.0 | **Score: 4.70/5**

Keycloak provides OpenID Connect (OIDC), OAuth 2.0, and SAML 2.0 identity and access management for municipal applications. It supports multi-factor authentication, fine-grained authorisation, and integration with external identity providers including Germany’s BundID and Switzerland’s E-ID [38]. Keycloak’s federation capabilities allow a municipality to maintain a single authoritative identity store while delegating authentication to citizen identity providers in compliance with OZG 2.0 [2] and EMBAG [1] requirements.

Deployment references include Dataport’s hosted Keycloak service for northern German municipalities [24] and ZenDiS’s inclusion of Keycloak as the identity layer of OpenDesk [42]. BSI IT-Grundschutz [26] compatibility is achievable through standard hardening procedures.

**Key integration:** Keycloak should be configured as the central identity broker, with citizen-facing applications consuming OIDC tokens and staff applications using SAML for legacy compatibility.

### 4.2 Document Management — Nextcloud + OpenProject

**Recommended components:** Nextcloud [13] (AGPL-3.0, score 4.20) + OpenProject [20] (GPLv3, score 3.65)

Nextcloud provides federated file storage, sharing, and collaboration, with enterprise-grade features including end-to-end encryption, audit logging, and mobile clients. Nextcloud for Government [13] deployments include multiple German Länder administrations and Swiss cantonal offices. OpenProject provides project management, task tracking, and document workflows.

**GEVER integration (CH):** Swiss municipalities must evaluate this combination against the GEVER framework requirements [43] for records management. A compliant records management layer (eCH-0039 [17]) may need to sit above Nextcloud for formal records subject to retention obligations.

### 4.3 Workflow Automation — Camunda / Flowable

**Recommended components:** Camunda Platform 8 Community [33] (Apache 2.0, score 4.20) / Flowable (Apache 2.0)

BPMN 2.0-based workflow engines are essential for digitising administrative processes under OZG 2.0 [2] and FIM [32]. The FIM Prozessbibliothek provides reusable BPMN process templates for 575+ standardised administrative procedures, reducing custom development effort significantly. Both platforms support XÖV data exchange standards [46] and are compatible with FIM process models.

**Key integration:** Workflow engines should be integrated with Keycloak [21] for authentication, Nextcloud [13] for document attachments, and deployed on Kubernetes [39] on SCS infrastructure [3].

### 4.4 Citizen Participation — Decidim / CONSUL

**Recommended components:** Decidim [12] (AGPL-3.0, score 3.90) / CONSUL Democracy [40] (AGPL-3.0)

Digital participation platforms are increasingly mandated or expected under municipal democratic participation obligations. Decidim — developed in Barcelona and maintained by the Decidim Association [12] — provides participatory budgeting, proposals, assemblies, and deliberative processes. CONSUL Democracy [40], developed by the Ayuntamiento de Madrid, offers comparable features with a stronger track record in Spanish-speaking jurisdictions.

Decidim is the recommended primary choice for German- and French-speaking municipalities due to its more active internationalisation community, WCAG 2.1 AA audit history, and integration with European digital participation networks. The platform is deployed in over 400 municipalities globally, including Barcelona, Helsinki, and multiple Swiss communes.

### 4.5 Communication — Matrix / Jitsi / BigBlueButton

**Recommended components:** Matrix/Synapse [14] (Apache 2.0, score 4.35), Jitsi Meet [35] (Apache 2.0), BigBlueButton [34] (LGPL-3.0, score 3.90)

The Matrix protocol [14] provides a federated, end-to-end encrypted messaging fabric for staff communication. Element (the flagship Matrix client) is the communication backbone of the French government’s Tchap platform and the German BundesMessenger. Jitsi Meet [35] provides lightweight, browser-based video conferencing. BigBlueButton [34] provides a more feature-complete platform suitable for public council meetings and citizen consultations.

### 4.6 Open Data — CKAN

**Recommended component:** CKAN [22] | **Licence:** AGPL-3.0 | **Score: 4.25/5**

CKAN is the de facto standard open-data portal platform for European government, underpinning data.gov.uk, the EU Open Data Portal, opendata.swiss [44], and GovData.de. For municipalities, CKAN provides a standards-compliant data catalogue (DCAT-AP), dataset management, API access, and harvesting from other CKAN instances. Municipalities publishing on CKAN can federate with cantonal/Länder portals and national portals through DCAT-AP harvesting, fulfilling open-data obligations under OZG 2.0 [2] and the Swiss open government data strategy [44].

### 4.7 GIS — QGIS / GeoServer / OpenStreetMap

**Recommended components:** QGIS [37] (GPL-2.0+, score 4.85), GeoServer, OpenStreetMap [36] (ODbL-1.0)

QGIS [37] provides a full-featured desktop GIS for municipal staff, with native support for OGC standards (WMS, WFS, WCS). GeoServer provides server-side spatial data publishing and OGC web services. OpenStreetMap [36] provides a globally maintained, royalty-free base map. GeoServer should expose WMS/WFS services consumed by the municipal web portal for public-facing map applications. QGIS integrates with PostgreSQL/PostGIS [41] for spatial data storage.

### 4.8 CMS — TYPO3 / Drupal

**Recommended components:** TYPO3 [19] (GPL-2.0, score 4.20) / Drupal

The municipal website and citizen portal require a CMS combining editorial accessibility with technical security, accessibility compliance, and long-term maintainability. TYPO3 [19] holds a dominant position in German and Swiss public administration, with exceptionally high public-sector penetration in the DACH region. The TYPO3 Association publishes specific guidance for public administration deployments including BITV 2.0 / WCAG 2.1 AA compliance toolkits. For most German and Swiss municipalities, TYPO3 is the pragmatic recommendation based on existing service provider ecosystem density.

### 4.9 Cloud Infrastructure — Sovereign Cloud Stack

**Recommended component:** Sovereign Cloud Stack (SCS) [3, 11] | **Licence:** Apache 2.0 | **Score: 4.40/5**

The Sovereign Cloud Stack [3] is an OSBA-coordinated open-source cloud infrastructure specification built on OpenStack, Kubernetes [39], and Ceph, with additional layers for identity, monitoring, and security aligned with BSI IT-Grundschutz [26] and BSI Cloud Minimum Standards [52].

SCS addresses the fundamental infrastructure sovereignty question: a municipality or its cooperative service provider can operate SCS on owned or leased hardware within German or Swiss jurisdiction, eliminating dependencies on US-based hyperscalers and resolving the Schrems II / transatlantic data transfer compliance problem. Multiple SCS-certified providers are commercially available, and govdigital eG [23] is developing a multi-tenant SCS offering for municipal use.

### 4.10 AI and Data Services

**Sovereign AI principles for public administration.** The deployment of artificial intelligence in municipal administration raises distinct sovereignty concerns. Reliance on proprietary Large Language Model (LLM) APIs creates dependencies that may conflict with GDPR Article 22 obligations regarding automated decision-making, expose citizen data to third-party processing under terms that cannot be audited, and create vendor lock-in at the level of inference rather than software.

This paper adopts five sovereign AI principles for municipal public administration:

1. **Data minimisation and pseudonymisation:** Any AI component processing citizen data must apply GDPR data minimisation and pseudonymisation. Inputs to AI models should not contain directly identifying information unless strictly necessary and explicitly consented.
2. **Local inference by default:** AI inference should be performed on infrastructure within the municipality’s or its cooperative provider’s control, not sent to external APIs.
3. **Model transparency:** Municipalities should prefer open-weight models (Llama 3.x, Mistral, Falcon) with published model cards over closed proprietary models.
4. **Human in the loop:** Consistent with GDPR Article 22 [27], decisions with legal or similarly significant effects on citizens must not be made solely through automated processing. AI tools in municipal contexts should function as decision-support tools, not autonomous decision-makers.
5. **Vendor diversification:** Where AI capabilities are procured externally, contracts must ensure data portability, avoid exclusivity, and permit migration to alternative providers.

**Recommended open-source AI components:**

| Component | Licence | Function |
|---|---|---|
| LocalAI | MIT | OpenAI-compatible REST API server; runs open-weight LLMs locally |
| Ollama | MIT | Runtime for local LLM deployment; growing model library |
| OpenWebUI | MIT | Browser-based chat interface for LocalAI/Ollama backends |

**Municipal AI use cases:** Document summarisation (processing council minutes, legal texts), FAQ chatbots for citizen enquiries (with human escalation path), GIS analysis assistance, translation assistance for multilingual service content, and internal knowledge management.

**Data warehouse integration:** Municipal AI services should be integrated with a PostgreSQL [41]-based data warehouse or a CKAN [22] data catalogue, enabling retrieval-augmented generation (RAG) over municipal datasets. This approach constrains AI outputs to verified municipal data, reducing hallucination risk and improving auditability.

### 4.11 Reference Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│  LAYER 9 — CITIZEN & STAFF INTERFACES                               │
│  TYPO3/Drupal (portal)  │ Decidim/CONSUL (participation)           │
│  OpenWebUI (AI chat)    │ Mobile apps (TYPO3 REST)                 │
└────────────────────────────┬───────────────────────────────────────┘
                             │
┌────────────────────────────▼───────────────────────────────────────┐
│  LAYER 8 — COLLABORATION & COMMUNICATION                            │
│  Nextcloud (files/docs) │ OpenProject (PM) │ Matrix/Element (chat) │
│  Jitsi Meet (video)     │ BigBlueButton (webinar/council)          │
└────────────────────────────┬───────────────────────────────────────┘
                             │
┌────────────────────────────▼───────────────────────────────────────┐
│  LAYER 7 — PROCESS & WORKFLOW                                       │
│  Camunda / Flowable (BPMN 2.0)  │ FIM Prozessbibliothek            │
│  XÖV/eCH Connectors              │ XForms / form engine             │
└────────────────────────────┬───────────────────────────────────────┘
                             │
┌────────────────────────────▼───────────────────────────────────────┐
│  LAYER 6 — AI & DATA SERVICES                                       │
│  LocalAI / Ollama (LLM inference)  │ OpenWebUI (interface)         │
│  CKAN (open data portal)           │ PostgreSQL/PostGIS (warehouse)│
│  RAG pipeline                      │ Anonymisation / pseudonymise  │
└────────────────────────────┬───────────────────────────────────────┘
                             │
┌────────────────────────────▼───────────────────────────────────────┐
│  LAYER 5 — GEOSPATIAL                                               │
│  GeoServer (OGC WMS/WFS) │ QGIS (desktop/server) │ OSM (base map)│
│  PostGIS (spatial DB)    │ Public map portal                      │
└────────────────────────────┬───────────────────────────────────────┘
                             │
┌────────────────────────────▼───────────────────────────────────────┐
│  LAYER 4 — IDENTITY & SECURITY                                      │
│  Keycloak (IAM / OIDC / SAML)  │ BundID federation (DE)           │
│  Swiss E-ID / BGEID (CH)        │ BSI IT-Grundschutz controls      │
│  NIS2-compliant SIEM / logging  │ Vulnerability scanning           │
└────────────────────────────┬───────────────────────────────────────┘
                             │
┌────────────────────────────▼───────────────────────────────────────┐
│  LAYER 3 — INTEGRATION & API GATEWAY                                │
│  REST / GraphQL API gateway  │ XÖV / eCH adapters                  │
│  FIM connectors              │ Event bus (Kafka / NATS)            │
│  Audit logging               │ OpenAPI specifications               │
└────────────────────────────┬───────────────────────────────────────┘
                             │
┌────────────────────────────▼───────────────────────────────────────┐
│  LAYER 2 — CONTAINER ORCHESTRATION                                  │
│  Kubernetes [39] │ Helm charts │ GitOps (Flux / ArgoCD)           │
│  Prometheus/Grafana (monitoring) │ Loki/OpenSearch (logging)      │
└────────────────────────────┬───────────────────────────────────────┘
                             │
┌────────────────────────────▼───────────────────────────────────────┐
│  LAYER 1 — SOVEREIGN CLOUD INFRASTRUCTURE — SCS [3]               │
│  OpenStack (compute/network/storage) │ Ceph (block/object/file)   │
│  SCS-certified hoster OR on-premise  │ DE/CH/EU jurisdiction only  │
│  govdigital eG [23] / Dataport [24] / cantonal ICT provider        │
└─────────────────────────────────────────────────────────────────────┘
```

All layers communicate via open APIs documented in OpenAPI specifications. Container orchestration across the stack is handled by Kubernetes [39], relational persistence by PostgreSQL [41], and object storage by Ceph on SCS [3]. Data exchange uses XÖV standards (Germany) [46] or eCH standards (Switzerland) [17]. Security is governed by BSI IT-Grundschutz [26] (DE) or the Swiss ISDS framework.

---

## 5. Implementation Roadmap

The following phased roadmap is designed for a municipality of 50,000–200,000 inhabitants with 200–1,000 administrative staff. Cost ranges are indicative and should be refined through a municipal-specific feasibility study. All figures are in EUR and represent total investment including external services, hardware (where applicable), and internal staff time at market rates. Municipalities participating in cooperative procurement (govdigital [23], Dataport [24], cantonal ICT) should expect costs at the lower end of each range.

### Phase 0 — Organisational Readiness and Baseline Assessment

**Duration:** 3–6 months | **Indicative cost range: €50,000–200,000**

**Objectives:** Conduct digital sovereignty self-assessment (Appendix C); map current technology portfolio and licence costs; establish political and executive mandate; define governance structure; identify cooperative partners.

**Deliverables:**
- Digital sovereignty baseline report
- Software asset inventory with TCO baseline
- Municipal council resolution
- Partnership agreements with cooperative service providers

**Success criteria:**
- Executive sponsor identified and committed
- Software asset inventory complete
- At least one cooperative partnership established
- Budget envelope for Phase 1 approved by council

### Phase 1 — Infrastructure and Identity Foundation

**Duration:** 6–12 months | **Indicative cost range: €150,000–500,000**

**Objectives:** Deploy SCS-based [3] cloud infrastructure; implement Keycloak [21] federated with BundID/E-ID; establish Kubernetes cluster [39] with GitOps pipeline; implement NIS2-compliant security baseline [27].

**Deliverables:**
- SCS infrastructure operational with SLA-backed cooperative support
- Keycloak identity platform in production with national identity federation
- BSI IT-Grundschutz [26] baseline documentation complete
- NIS2 incident response procedures in place

**Success criteria:**
- Infrastructure uptime ≥99.5% over 60-day observation period
- All staff can authenticate via Keycloak SSO
- First IT-Grundschutz gap analysis completed and remediation plan approved

### Phase 2 — Collaboration and Communication Platform

**Duration:** 6–12 months | **Indicative cost range: €200,000–600,000**

**Objectives:** Deploy Nextcloud [13] and OpenProject [20]; deploy Matrix/Element [14] for staff messaging; deploy Jitsi [35] and BigBlueButton [34]; deliver staff training programme.

**Deliverables:**
- Nextcloud with department-level rollout plan
- Matrix homeserver federated with state-government instances where available
- Video conferencing operational and tested for council meetings
- Training materials and internal OSS champion network

**Success criteria:**
- ≥80% of pilot department staff using Nextcloud for primary file management
- ≥60% of internal meetings via self-hosted conferencing
- Staff satisfaction survey score ≥3.5/5.0

### Phase 3 — Workflow Automation and Digital Services

**Duration:** 9–18 months | **Indicative cost range: €150,000–400,000**

**Objectives:** Deploy Camunda/Flowable [33] workflow engine; digitise top 10 citizen-facing processes using FIM templates [32]; integrate OZG 2.0 services [2]; deploy CKAN [22] open data portal; launch TYPO3 [19] citizen portal with WCAG 2.1 AA compliance.

**Deliverables:**
- Top 10 citizen processes digitised and published
- OZG 2.0 services integrated and confirmed by state authority
- CKAN portal live with minimum 20 datasets federated to national portal
- TYPO3 portal with published BITV 2.0 / WCAG 2.1 AA conformance statement

**Success criteria:**
- Top 10 services available end-to-end online without mandatory paper step
- CKAN portal harvested by govdata.de or opendata.swiss
- WCAG 2.1 AA audit passed by independent third party

### Phase 4 — Advanced Services and Citizen Participation

**Duration:** 6–12 months | **Indicative cost range: €100,000–300,000**

**Objectives:** Deploy Decidim [12] or CONSUL [40] for citizen participation; deploy GIS stack (QGIS [37], GeoServer, OSM [36]); launch sovereign AI services (LocalAI/Ollama, OpenWebUI); implement PostgreSQL [41] data warehouse with RAG.

**Deliverables:**
- Participation platform operational with first participatory process
- GIS stack operational with public map portal
- Staff AI assistant for document summarisation and FAQ drafting
- Data warehouse operational; no citizen data sent to external AI APIs

**Success criteria:**
- ≥500 citizen participants in first participatory budgeting cycle
- GIS datasets published under open licence on CKAN
- AI assistant adopted by ≥50% of administrative staff

### Phase 5 — Optimisation, Contribution, and Replication

**Duration:** Ongoing from month 30+ | **Indicative annual cost: €50,000–150,000/year**

**Objectives:** Optimise operational costs; contribute to upstream OSS communities; publish municipal components on openCode.de [10]; share learnings with peer municipalities; annual self-assessment review.

**Deliverables:**
- Documented contributions to upstream OSS projects
- At least one module/template published on openCode.de
- Inter-municipal knowledge-sharing agreement
- Annual digital sovereignty report to municipal council

**Success criteria:**
- Net licence cost savings demonstrable versus pre-transition baseline
- At least one OSS contribution accepted upstream
- Peer municipality engaged in cooperative procurement or knowledge exchange

---

## 6. Stakeholder and Procurement Strategy

### 6.1 Stakeholder Map

| Stakeholder | Role | Primary Interest | Influence | Engagement Strategy |
|---|---|---|---|---|
| Municipal Council | Political mandate | Fiscal responsibility, citizen benefit | High | Progress reports, TCO dashboards |
| Mayor / Chief Executive | Executive sponsor | Strategic vision, risk management | High | One-to-one briefings, milestone reviews |
| CIO / Head of IT | Technical lead | Operational reliability, staff capacity | High | Co-design of roadmap, technical working group |
| Administrative Staff | End users | Usability, training, workflow continuity | Medium–High | Change management, champion network |
| Citizens | Service recipients | Service availability, data protection | Medium | Participation platforms, transparency reporting |
| State / Cantonal IT Authority | Regulatory oversight | OZG/EMBAG compliance, interoperability | High | Early alignment, joint procurement |
| govdigital / Dataport [23, 24] | Cooperative service provider | Commercial relationship, shared services | Medium | Framework agreements, SLA definition |
| OSS Communities | Software suppliers | Adoption, contribution, funding | Low | Community engagement, upstream contributions |
| Civil Society / Digital Rights Orgs | Advocacy, scrutiny | OSS principles, data protection | Low–Medium | Transparency reporting, public code pledge |
| Local ICT SMEs | Implementation partners | Commercial opportunity | Medium | Open procurement, UVgO / VgV tenders |

### 6.2 Procurement Framework

Municipal OSS procurement must navigate EU public procurement rules, German VgV/UVgO or Swiss BöB/VöB procedures, and the Interoperable Europe Act [6] interoperability assessment obligation. Six principles govern the framework:

1. **Functional specification, not product specification.** Tender documents must specify required functions (e.g., “federated identity management conforming to OIDC 1.0 and SAML 2.0”) rather than named products, ensuring open competition while permitting OSS bids. This is a legal requirement under EU procurement rules.

2. **Total cost of ownership evaluation.** Award criteria must include multi-year TCO covering licence, implementation, operations, training, exit, and migration costs. Zero licence cost for OSS does not mean zero total cost; proprietary alternatives typically understate downstream lock-in costs.

3. **Open standards mandatory.** All procured components must support XÖV [46] (DE), eCH [17] (CH), DCAT-AP (open data), OGC (GIS), OIDC/SAML (identity), BPMN 2.0 (workflow). Non-compliance should be a disqualifying criterion.

4. **Source code escrow or open licence.** For any bespoke development, the contract must either require open-source publication (EMBAG Article 9 [1] for Swiss municipalities; best practice for German municipalities) or establish source code escrow ensuring the municipality retains access.

5. **Data portability and exit rights.** All contracts must include unambiguous data portability: the supplier must provide a complete, machine-readable export of all municipal data in an open format within 30 days of contract termination, at no additional cost.

6. **Cooperative and framework procurement.** Municipalities should prioritise framework agreements established by govdigital [23], Dataport [24], BeschA, or cantonal procurement bodies to reduce administrative burden and benefit from collective negotiating power.

### 6.3 Change Management

The Munich LiMux post-mortem [Section 7.2] demonstrates that technical quality is insufficient for a successful OSS transition. Change management is the critical success factor:

- **Appoint internal OSS champions** in each department, trained and empowered to provide peer support.
- **Invest in training proportional to staff size.** A rule of thumb of 3–5 days of training per staff member for a productivity-suite transition is consistent with enterprise software implementation best practice.
- **Communicate openly about the transition.** Municipal council resolutions, staff newsletters, and public website announcements should explain the digital sovereignty rationale in plain language.
- **Establish a feedback loop.** A structured staff feedback mechanism (quarterly survey, visible issue tracker) allows problems to be identified before they become political liabilities.
- **Pilot before mandate.** Each platform should be piloted in a volunteer department before mandated rollout. Pilot departments should be selected for enthusiasm rather than urgency.

### 6.4 Legal and Regulatory Compliance Matrix

| Regulation | Jurisdiction | Key Requirement | OSS Stack Impact | Compliance Mechanism |
|---|---|---|---|---|
| GDPR / DSGVO | EU / DE / CH (nFADP) | Lawful basis, data minimisation, access rights | All citizen-facing components; AI services | Privacy-by-design in Nextcloud/Keycloak; DSGVO-compliant hosting; DPO appointment; Art. 22 human-in-loop for AI |
| NIS2 Directive [27] | EU (DE: KRITIS-Dachgesetz) | Incident reporting (24h), risk management, supply chain security | SCS infrastructure; all critical services | BSI IT-Grundschutz [26]; NIS2-compatible ISMS; incident response playbook |
| OZG 2.0 [2] | DE | Online service availability; BundID; Once Only | Workflow [4.3]; portal [4.8]; identity [4.1] | Camunda FIM integration; Keycloak BundID federation; OZG marketplace |
| EMBAG [1] | CH | Open source by default (Art. 9); publication obligation | All bespoke development | OSS licence on custom code; publication on cantonal/federal repository |
| Interoperable Europe Act [6] | EU | Interoperability assessment before deployment | All procured components | EIF [45] assessment checklist; Joinup publication of solutions |
| BITV 2.0 / WCAG 2.1 AA | DE | AA conformance; accessibility statement | Portal [4.8]; participation [4.4]; all web apps | Third-party WCAG audit; TYPO3 accessibility toolkit |
| BSI IT-Grundschutz [26] | DE | Baseline security measures; documentation | SCS [4.9]; identity [4.1]; all infrastructure | IT-Grundschutz implementation project; annual review |
| ISDS / P028 | CH | Security baseline; accessibility | All federal/cantonal SW | P028 conformance assessment; ISDS risk management |
| eCH Standards [17] | CH | Data exchange compliance (eCH-0039, eCH-0058) | Workflow [4.3]; DMS [4.2]; open data [4.6] | eCH-compliant interfaces; eCH certification where available |

---

## 7. Risk Analysis

### 7.1 Risk Register

| # | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R1 | Political reversal — new municipal leadership reverses OSS mandate | Medium | High | Municipal council resolution; documented citizen benefit and TCO savings |
| R2 | Staff resistance — end users refuse adoption of new tools | Medium | High | Change management programme; champion network; phased rollout; usability investment |
| R3 | Integration failure with Länder/cantonal legacy systems | Medium | Medium | XÖV/eCH standard compliance; early integration testing; Länder coordination |
| R4 | Ecosystem collapse — key OSS component loses community support | Low | High | Multi-supplier support contracts; upstream contribution; fork readiness |
| R5 | Security incident — breach of sovereign infrastructure | Low | Very High | BSI IT-Grundschutz [26]; NIS2 ISMS [27]; penetration testing; SCS security baseline [3] |
| R6 | Cost overrun — implementation costs exceed estimates | Medium | Medium | Phased funding; 20% contingency reserve; cooperative procurement |
| R7 | Compliance failure — GDPR/NIS2/OZG/EMBAG non-compliance | Low | High | Legal compliance matrix [Section 6.4]; DPO involvement from Phase 0 |
| R8 | AI governance failure — citizen data exposed through AI services | Medium | High | Local inference only; data minimisation; no proprietary LLM APIs for citizen data; GDPR Art. 22 |
| R9 | Skill gap — insufficient OSS technical capacity internally | High | Medium | Training investment; cooperative service model; gradual in-sourcing |
| R10 | Scope creep — roadmap expands beyond municipal capacity | Medium | Medium | Phase gate governance; executive sponsor sign-off; MVP discipline |

### 7.2 Munich Cautionary Case

The Munich LiMux programme (2003–2013) is the most extensively documented large-scale municipal open-source transition in European history, and its reversal is the most frequently cited argument against municipal OSS adoption. A rigorous reading of the evidence [30, see also Section 3.6] yields a more nuanced lesson.

The LiMux migration successfully converted approximately 14,800 workstations to Ubuntu Linux and LibreOffice, achieving documented licence savings of approximately €10 million. The programme was technically functional: the majority of migrated workstations operated the open-source stack without reported productivity loss exceeding that of equivalent Windows migrations.

The reversal (initiated by CSU/SPD coalition agreement 2014, completed by approximately 2021) is attributable to: the election of a new mayor with a different technology orientation; a 2016 internal assessment commissioned by the new administration that critiqued LiMux’s coordination overhead; lobbying pressure from Microsoft (which subsequently relocated its German headquarters to Munich); and compatibility challenges with Bavaria’s state-government Windows-dependent workflows.

**Lessons:**
1. Political mandate must be institutionalised in council resolution, not only executive decision.
2. Interoperability with vertical government systems is existential; XÖV/eCH compliance at Länder level is a prerequisite.
3. Change management investment must be proportionate; user-interface differences are addressable through training, not inherent to OSS.
4. Economic evidence must be pre-emptively documented to survive political contestation.

### 7.3 Security Considerations

Municipal digital infrastructure is a target for ransomware, data theft, and nation-state interference. BSI IT-Grundschutz [26] provides the authoritative German baseline. NIS2 [27] requires municipalities classified as essential or important entities to implement risk management measures and report significant incidents within 24 hours.

Open-source software offers intrinsic security advantages (public code review, rapid community patch cycles) alongside challenges (smaller municipalities may lack staff to monitor CVE advisories). The cooperative service model (govdigital [23], Dataport [24]) addresses this by centralising security operations for multiple municipal clients.

**Key security measures:**
- SCS infrastructure [3] operated with BSI Cloud Minimum Standards [52] as baseline
- Keycloak [21] enforcing MFA for all staff and privileged access
- Security updates within 48 hours of critical CVE publication (CVSS ≧7.0)
- Annual penetration testing by a BSI-qualified auditor
- NIS2-compliant incident response plan in place before Phase 1 go-live

### 7.4 Regulatory Risk Matrix

| Regulatory Development | Probability (3-year) | Municipal Impact | Response |
|---|---|---|---|
| NIS2 expanded scope to smaller municipalities | Medium | Mandatory ISMS; incident reporting costs | Implement ISMS in Phase 1 proactively |
| EU AI Act tier reclassification of municipal AI use cases | Medium | Conformity assessment requirements | Document AI use cases; avoid high-risk categories; maintain human-in-loop |
| OZG 2.0 interoperability mandate tightened | High | Faster implementation timeline | Prioritise Phase 3 OZG integration; close contact with Länder IT authority |
| DSGVO enforcement on non-EU cloud hosting | Medium | Challenge to non-SCS deployments | Migrate to SCS [4.9] in Phase 1; avoid non-EU hyperscalers |
| Swiss BGEID rollout acceleration [38] | High (CH) | Faster E-ID integration required | Integrate Keycloak E-ID federation in Phase 1 |
| Interoperable Europe Act compliance deadline | High | Interoperability assessment required | Include EIF [45] assessment in all Phase 3+ procurements |
| EMBAG Article 9 cantonal extension (CH) | Medium | OSS publication obligations | Include OSS publication clause in all development contracts |

---

## 8. Conclusion

The case for open-source digital sovereignty in municipal government has moved decisively from advocacy to evidence over the past decade. Legislative frameworks in Germany (OZG 2.0 [2]), Switzerland (EMBAG [1]), and the European Union (Interoperable Europe Act [6], EU Open Source Strategy [5]) now create structural incentives — and in some cases obligations — for public administrations to prefer open, interoperable, and auditable software. The technology components to deliver a complete municipal digital stack are mature, well-governed, and in production at comparable scale across Europe.

This paper has argued, across eleven technology domains and a six-phase implementation roadmap, that a municipality of 50,000–200,000 inhabitants can deploy a fully sovereign open-source digital stack that meets or exceeds the functional requirements of proprietary alternatives. The critical success factors are not technical but organisational: political mandate with institutional durability; investment in change management and training proportionate to staff size; procurement frameworks that penalise lock-in rather than rewarding lowest initial price; and cooperative structures that allow municipalities to share the operational burden of complex infrastructure.

The Munich LiMux experience is a cautionary illustration, not a refutation. Its lessons — institutionalise the mandate, invest in interoperability, document the economics — are fully incorporated into the roadmap and governance framework presented here. The Barcelona, Schleswig-Holstein, and Swiss cantonal cases demonstrate that the proposition is viable when these conditions are met.

Digital sovereignty is not an end state but a continuous practice. The municipality that deploys this stack in 2027 will need to renew its technology choices in 2032. The advantage of the open-source approach is precisely that this renewal is possible: components can be replaced, upgraded, or forked without vendor permission or contractual penalty. The public’s digital infrastructure should be as auditable, adaptable, and democratic as the institutions it serves. Public money should produce public code [4].

---

## References

[1] Swiss Federal Chancellery (2023). *Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG)*, SR 172.019. Bern: Swiss Confederation. https://fedlex.admin.ch/eli/cc/2023/682/de. Licence: CC0.

[2] Bundesministerium des Innern und für Heimat (2024). *Onlinezugangsgesetz 2.0 (OZG 2.0)*. Berlin: BMI. https://www.bmi.bund.de. Licence: DL-DE/Zero 2.0.

[3] Open Source Business Alliance (OSBA) (2023). *Sovereign Cloud Stack (SCS)*. Berlin: OSBA. https://scs.community. Licence: Apache 2.0 / CC-BY-SA-4.0.

[4] Free Software Foundation Europe (FSFE) (2017). *Public Money? Public Code!* Berlin: FSFE. https://publiccode.eu. Licence: CC-BY-SA-4.0.

[5] European Commission (2020). *Open Source Software Strategy 2020–2023: Think Open*. Brussels: European Commission. https://commission.europa.eu. Licence: CC-BY.

[6] European Parliament and Council (2024). *Regulation (EU) 2024/903 — Interoperable Europe Act*, OJ L 903/2024, 22 March 2024. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202400903. Licence: EU legislation (public domain).

[7] Wirtz, B.W. & Weyerer, J.C. (2017). Holistic e-government maturity model. *Public Management Review*, 19(9), 1297–1316. https://doi.org/10.1080/14719037.2017.1283024.

[8] Janssen, M., Charalabidis, Y. & Zuiderwijk, A. (2012). Benefits, adoption barriers and myths of open data. *Information Systems Management*, 29(4), 258–268. https://doi.org/10.1080/10580530.2012.716740.

[9] FITKO (2024). *FITKO Jahresbericht 2023*. Frankfurt: FITKO. https://fitko.de. Licence: DL-DE/Zero 2.0.

[10] Digitalservice GmbH des Bundes (2023). *openCode.de*. Berlin: Digitalservice. https://opencode.de.

[11] SCS Community / OSBA (2024). *Sovereign Cloud Stack Technical Documentation*. Berlin: OSBA. https://docs.scs.community. Licence: Apache 2.0.

[12] Decidim Association (2021). *Decidim: Free Open-Source Participatory Democracy*. Barcelona: Decidim Association. https://decidim.org. Licence: AGPL-3.0.

[13] Nextcloud GmbH (2023). *Nextcloud for Government*. Stuttgart: Nextcloud GmbH. https://nextcloud.com/government/. Licence: AGPL-3.0.

[14] The Matrix Foundation (2023). *Matrix Specification v1.9*. London: Matrix Foundation. https://spec.matrix.org. Licence: Apache 2.0.

[15] Lathrop, D. & Ruma, L. (Eds.) (2010). *Open Government: Collaboration, Transparency, and Participation in Practice*. Sebastopol: O’Reilly Media. ISBN 978-0-596-80435-0.

[16] E-Government Suisse (2023). *Strategie E-Government Schweiz 2024–2027*. Adopted 22 November 2023. Bern: Swiss Confederation. https://egovernment.ch. Licence: open access.

[17] eCH Association (2023). *eCH-Standards für E-Government Schweiz*. Zürich: eCH. https://ech.ch. Licence: CC-BY-4.0.

[18] AKDB (2023). *IT-Services für Kommunen in Bayern*. Munich: AKDB. https://akdb.de.

[19] TYPO3 Association (2023). *TYPO3 in Public Administration*. Düsseldorf: TYPO3 Association. https://typo3.org. Licence: GPL-2.0.

[20] OpenProject GmbH (2023). *OpenProject for Government*. Berlin: OpenProject GmbH. https://openproject.org. Licence: GPLv3.

[21] Keycloak Community / Red Hat (2023). *Keycloak: Open Source Identity and Access Management*. https://keycloak.org. Licence: Apache 2.0.

[22] CKAN Association (2023). *CKAN: Open Source Data Portal Software*. https://ckan.org. Licence: AGPL-3.0.

[23] govdigital eG (2023). *Genossenschaft für digitale Verwaltung*. Berlin: govdigital. https://govdigital.de.

[24] Dataport AöR (2023). *IT-Dienstleister für die öffentliche Verwaltung*. Altenholz: Dataport. https://dataport.de.

[25] ZenDiS GmbH (2024). *Zentrum für Digitale Souveränität — Jahresbericht 2023*. Berlin: ZenDiS. https://zendis.de.

[26] BSI (2023). *IT-Grundschutz-Kompendium Edition 2023*. Bonn: BSI. https://bsi.bund.de. Licence: CC-BY-ND 3.0 DE.

[27] European Parliament and Council (2022). *Directive (EU) 2022/2555 — NIS2 Directive*, OJ L 333/80, 27 December 2022. https://eur-lex.europa.eu. Licence: EU legislation (public domain).

[28] European Commission / Joinup (2023). *OSOR Annual Review 2023*. Brussels: European Commission. https://joinup.ec.europa.eu/collection/open-source-observatory-osor. Licence: CC-BY-4.0.

[29] UN DESA (2022). *UN E-Government Survey 2022*. New York: United Nations. https://publicadministration.un.org. Licence: UN open access.

[30] Janowski, T. (2015). Digital government evolution. *Government Information Quarterly*, 32(3), 221–226. https://doi.org/10.1016/j.giq.2015.07.001.

[31] GovStack Initiative / ITU & DIAL (2023). *GovStack Building Blocks Specification v1.0*. Geneva: ITU. https://govstack.global. Licence: CC-BY-SA-4.0.

[32] Bundesverwaltungsamt / BMI (2023). *Föderales Informationsmanagement (FIM)*. Cologne: BVA. https://bva.bund.de. Licence: DL-DE/Zero 2.0.

[33] Camunda Services GmbH (2023). *Camunda Platform 8 Community Edition*. Berlin: Camunda. https://camunda.com. Licence: Apache 2.0.

[34] BigBlueButton Inc. (2023). *Open Source Web Conferencing*. Ottawa: BigBlueButton. https://bigbluebutton.org. Licence: LGPL-3.0.

[35] Jitsi Community (2023). *Jitsi Meet*. San Francisco: 8x8 / Jitsi Community. https://jitsi.org. Licence: Apache 2.0.

[36] OpenStreetMap Foundation (2023). *OpenStreetMap*. London: OSMF. https://openstreetmap.org. Licence: ODbL-1.0.

[37] QGIS Project (2023). *QGIS: A Free and Open Source Geographic Information System*. https://qgis.org. Licence: GPL-2.0+.

[38] Bundesamt für Justiz / Eidgenössische Kanzlei (2023). *Bundesgesetz über den elektronischen Identitätsnachweis und andere elektronische Nachweise (BGEID)*, SR 161.5. Bern: Swiss Confederation. https://fedlex.admin.ch. Licence: CC0.

[39] Cloud Native Computing Foundation (CNCF) (2023). *Kubernetes*. San Francisco: Linux Foundation. https://kubernetes.io. Licence: Apache 2.0.

[40] Consul Project / Ayuntamiento de Madrid (2023). *CONSUL Democracy*. Madrid: Ayuntamiento de Madrid. https://consulproject.org. Licence: AGPL-3.0.

[41] PostgreSQL Global Development Group (2023). *PostgreSQL*. https://postgresql.org. Licence: PostgreSQL Licence.

[42] ZenDiS GmbH / BMI (2023). *OpenDesk: Der digitale Arbeitsplatz der Bundesverwaltung*. Berlin: ZenDiS. https://opendesk.eu. Licence: AGPL-3.0.

[43] Schweizerisches Bundesarchiv (BAR) (2023). *Geschäftsverwaltung (GEVER) in der Bundesverwaltung*. Bern: BAR. https://bar.admin.ch/bar/de/home/digitale-archivierung/gever.html. Licence: open access.

[44] opendata.swiss (2023). *Open Government Data Switzerland*. Bern: Swiss Federal Archives / BFS. https://opendata.swiss. Licence: CC-BY-4.0 (portal).

[45] European Commission, ISA² Programme (2017). *European Interoperability Framework (EIF)*. Brussels: European Commission. https://joinup.ec.europa.eu. Licence: CC-BY-4.0.

[46] KoSIT (2023). *XÖV-Standards: XML in der öffentlichen Verwaltung*. Bremen: KoSIT. https://xoev.de.

[47] Lucke, J. & Reinermann, H. (2000). *Speyerer Definition von Electronic Government*. Speyer: Forschungsinstitut für öffentliche Verwaltung. https://foev.dhv-speyer.de. Licence: open access.

[48] Bertot, J.C., Jaeger, P.T. & Grimes, J.M. (2010). Using ICTs to create a culture of transparency. *Government Information Quarterly*, 27(3), 264–271. https://doi.org/10.1016/j.giq.2010.04.003.

[49] OECD (2020). *The OECD Digital Government Policy Framework*. OECD Public Governance Policy Papers No. 02. Paris: OECD. https://doi.org/10.1787/f64fed2a-en.

[50] Bundesregierung Deutschland (2022). *Digitalstrategie Deutschland*. Berlin: Bundesregierung. https://digitalstrategie-deutschland.de. Licence: DL-DE/Zero 2.0.

[51] European Commission (2021). *2030 Digital Compass*, COM(2021) 118 final. Brussels: European Commission. Licence: CC-BY.

[52] BSI (2022). *Mindeststandard des BSI zur Nutzung externer Cloud-Dienste*, Version 1.1. Bonn: BSI. https://bsi.bund.de. Licence: CC-BY-ND 3.0 DE.

[53] Joinup / European Commission (2023). *Open Source Observatory and Repository (OSOR)*. Brussels: European Commission. https://joinup.ec.europa.eu/collection/open-source-observatory-osor. Licence: CC-BY-4.0.

[54] Dunleavy, P., Margetts, H., Bastow, S. & Tinkler, J. (2006). *Digital Era Governance*. Oxford: Oxford University Press. ISBN 978-0-19-929414-8.

[55] Scholl, H.J. (2017). Electronic government: A study domain past its zenith? *Information Polity*, 22(4), 313–329. https://doi.org/10.3233/IP-170417.

---

## Appendix A — Procurement Checklist (23 Questions)

Complete this checklist before issuing any tender for digital components covered by this strategy. Questions answered “No” or “Partial” require documented justification.

| # | Question | Yes | Partial | No |
|---|---|---|---|---|
| 1 | Is the component licensed under an OSI-approved open-source licence? | | | |
| 2 | Is the source code publicly available in a version-controlled repository? | | | |
| 3 | Has the component been audited for GDPR/DSGVO compliance by an independent authority? | | | |
| 4 | Does the component comply with WCAG 2.1 Level AA (or does the tender require this)? | | | |
| 5 | Does the component support OIDC 1.0 or SAML 2.0 for integration with Keycloak? | | | |
| 6 | Is the component deployable on Kubernetes/SCS without vendor-specific cloud dependencies? | | | |
| 7 | Does the contract include unconditional data export in an open format within 30 days of termination? | | | |
| 8 | Does the contract prohibit using municipal data for training AI models or secondary purposes? | | | |
| 9 | Does the tender specify functional requirements (not product names), ensuring open competition? | | | |
| 10 | Has the evaluation criterion included multi-year TCO (licence + implementation + operations + exit)? | | | |
| 11 | Are mandatory open standards specified (XÖV/DE, eCH/CH, DCAT-AP, BPMN 2.0, OGC)? | | | |
| 12 | Has an interoperability assessment been conducted per the Interoperable Europe Act [6]? | | | |
| 13 | Does the contract include source code escrow or OSS publication obligation for bespoke development? | | | |
| 14 | Is the upstream OSS community active (commits within 12 months; responsive issue tracker)? | | | |
| 15 | Are there documented public-sector production deployments at comparable scale? | | | |
| 16 | Does the component have a published security policy and CVE response process with SLA? | | | |
| 17 | Is the component compatible with BSI IT-Grundschutz [26] or ISDS (CH) hardening guidelines? | | | |
| 18 | Has the supplier demonstrated ability to provide support in the required municipal language(s)? | | | |
| 19 | Is cooperative or framework procurement (govdigital, Dataport, cantonal body) available and used? | | | |
| 20 | Has the DPO reviewed the DPIA for this component? | | | |
| 21 | Does the component support NIS2 [27] incident notification workflow (logging, alerting, 24h)? | | | |
| 22 | Has the municipal data protection authority been notified where required? | | | |
| 23 | Is a transition plan documented for migration away from this component if discontinued? | | | |

---

## Appendix B — Technology Evaluation Scoring Methodology

### Seven Criteria and Weights

| Criterion | Weight | Scores 1–5 (brief description) |
|---|---|---|
| C1 Licence Openness | 20% | 1=proprietary; 3=OSI copyleft; 5=OSI permissive or confirmed gov-compatible copyleft |
| C2 Deployment Maturity | 15% | 1=alpha; 3=stable, limited upgrade docs; 5=LTS, zero-downtime upgrades documented |
| C3 Community Health | 15% | 1=single-vendor stale; 3=multi-contributor monthly releases; 5=foundation-governed, weekly activity |
| C4 Interoperability | 15% | 1=proprietary APIs only; 3=1–2 mandatory standards; 5=all applicable standards natively supported |
| C5 Security | 15% | 1=no security policy; 3=patches within 30d; 5=dedicated security team, patches within 7d critical |
| C6 TCO | 10% | 1=high licence + lock-in; 3=zero licence, moderate impl; 5=zero licence, low impl, commodity ops |
| C7 Public-Sector Deployments | 10% | 1=none; 3=1–5 documented; 5=>20 documented, OSOR case study available |

**Weighted aggregate score** = (C1×0.20) + (C2×0.15) + (C3×0.15) + (C4×0.15) + (C5×0.15) + (C6×0.10) + (C7×0.10)

Components scoring below 3.0 on any single criterion, or below 3.5 aggregate, are not recommended without documented mitigating factors.

### Reference Scores

| Component | C1 | C2 | C3 | C4 | C5 | C6 | C7 | **Score** |
|---|---|---|---|---|---|---|---|---|
| Keycloak [21] | 5 | 5 | 4 | 5 | 4 | 5 | 5 | **4.70** |
| Nextcloud [13] | 3 | 5 | 4 | 4 | 4 | 5 | 5 | **4.20** |
| OpenProject [20] | 3 | 4 | 3 | 4 | 3 | 5 | 4 | **3.65** |
| Camunda CE [33] | 5 | 4 | 3 | 5 | 4 | 5 | 4 | **4.20** |
| Decidim [12] | 3 | 4 | 4 | 4 | 3 | 5 | 5 | **3.90** |
| Matrix/Synapse [14] | 5 | 4 | 4 | 5 | 4 | 5 | 4 | **4.35** |
| BigBlueButton [34] | 4 | 4 | 3 | 4 | 3 | 5 | 5 | **3.90** |
| CKAN [22] | 3 | 5 | 4 | 5 | 4 | 5 | 5 | **4.25** |
| QGIS [37] | 5 | 5 | 5 | 5 | 4 | 5 | 5 | **4.85** |
| TYPO3 [19] | 3 | 5 | 4 | 4 | 4 | 5 | 5 | **4.20** |
| SCS [3] | 5 | 4 | 4 | 5 | 5 | 4 | 3 | **4.40** |

---

## Appendix C — Municipal Digital Sovereignty Self-Assessment

This instrument provides a structured self-assessment for municipalities evaluating their current digital sovereignty posture. Complete in Phase 0 and repeat annually from Phase 5 onward. Completed jointly by CIO, legal/compliance officer, and a member of municipal leadership.

**Scoring:** Yes = 2 pts, Partial = 1 pt, No = 0 pts. Maximum: 30 points.

**Interpretation:** 25–30: Strong sovereignty; 18–24: Developing; 10–17: Emerging — transition programme recommended; 0–9: Critical dependency — immediate action required.

| # | Question | Yes (2) | Partial (1) | No (0) |
|---|---|---|---|---|
| 1 | Does the municipality have a documented digital sovereignty policy approved by the municipal council? | | | |
| 2 | Does the municipality maintain a complete software asset inventory including SaaS subscriptions and cloud contracts? | | | |
| 3 | Can the municipality migrate its primary data out of any single vendor within 90 days without prohibitive cost? | | | |
| 4 | Does the municipality use open, standardised data formats (XÖV/eCH, DCAT-AP, OGC, OIDC) for all primary data exchanges? | | | |
| 5 | Is the municipality’s primary infrastructure hosted within EU/EEA jurisdiction subject to EU data protection law? | | | |
| 6 | Does the municipal portal conform to WCAG 2.1 Level AA with a published accessibility statement? | | | |
| 7 | Does the municipality have a DPO and current DPIAs for all major digital services? | | | |
| 8 | Has the municipality implemented BSI IT-Grundschutz (DE) or ISDS (CH) baseline controls? | | | |
| 9 | Is the municipality compliant with or actively preparing for NIS2 requirements? | | | |
| 10 | Does the municipality use at least one open-source component in its current operational stack? | | | |
| 11 | Does the municipality participate in at least one cooperative IT structure? | | | |
| 12 | Does the municipality publish at least five open government datasets on a DCAT-AP compliant portal? | | | |
| 13 | Does the municipality offer at least five citizen processes fully online (end-to-end digital)? | | | |
| 14 | Does the municipality have a written policy prohibiting external AI APIs for processing citizen personal data? | | | |
| 15 | Has the municipality made at least one contribution to an upstream open-source project in the past 12 months? | | | |

**Total Score:** _____ / 30 | **Date:** _______________ | **Completed by:** _______________

**Priority gaps identified (scoring 0):** ______________________________

**Next scheduled review:** _______________

---

*This document is released under the Creative Commons Attribution 4.0 International Licence (CC-BY-4.0).*  
*Attribute as: Sebastian Graf, Autonomous Office of Civil Digital Infrastructure (sebk4c@tuta.com)*
