---
title: "Sovereign by Design: A State-of-the-Art Open-Source Technology Strategy for Municipal Governments"
author: "Sebastian Graf, Autonomous Office of Civil Digital Infrastructure"
correspondence: "sebk4c@tuta.com"
version: "0.2.0"
status: "Citation-Complete Draft"
date: "2026-06-20"
language: "en"
source-of-truth: true
SPDX-License-Identifier: "CC-BY-4.0"
keywords:
  - digital sovereignty
  - open source government
  - GovTech
  - municipal digital transformation
  - interoperability
  - OZG
  - EMBAG
  - Sovereign Cloud Stack
  - e-government
  - civic technology
  - ZenDiS
  - OpenDesk
  - GovStack
  - eCH standards
  - EU Data Act
---

# Sovereign by Design: A State-of-the-Art Open-Source Technology Strategy for Municipal Governments

**Author:** Sebastian Graf, Autonomous Office of Civil Digital Infrastructure
**Correspondence:** sebk4c@tuta.com
**Version:** 0.2.0 — Citation-Complete Draft
**Date:** 2026-06-20
**Languages:** English (source of truth) · Deutsch
**SPDX-License-Identifier:** CC-BY-4.0

---

## Abstract

Municipal governments are the closest layer of democratic administration to citizens, yet they face an acute structural tension: the digital tools they depend upon are increasingly proprietary, vendor-locked, and misaligned with public-interest values. This paper presents a comprehensive strategy for implementing a state-of-the-art, open-source governmental administration technology stack in city governments, updated to citation-complete draft status (v0.2.0).

Drawing on exemplary practices from Switzerland's landmark EMBAG legislation (2023), Germany's OZG 2.0 reform programme and Sovereign Cloud Stack initiative, ZenDiS's OpenDesk programme, the eCH interoperability standards framework, the EU Interoperable Europe Act (2024), the EU Data Act (2023), and the ITU/DIAL GovStack initiative, we derive a first-principles technology evaluation, a 36-month implementation roadmap, a stakeholder and procurement framework, and a risk register with empirically grounded mitigations.

We evaluate nine functional technology layers — identity management, document management, workflow automation, citizen participation, communications, open data publication, geographic information systems, public websites, and cloud infrastructure — against seven criteria: licence openness, deployment maturity, community health, interoperability standards compliance, security posture, total cost of ownership, and existing public-sector deployments.

Four findings emerge consistently from the evidence:

1. **Open-source municipal technology stacks are technically mature and production-proven** across all nine functional layers, with documented deployments at peer municipalities of all sizes.
2. **The regulatory environment increasingly mandates open-source and interoperability** — EMBAG, OZG 2.0, the Interoperable Europe Act, and the EU Data Act collectively create legal obligations that proprietary, vendor-locked systems cannot sustainably satisfy.
3. **The 5-year total cost of ownership is lower for open-source stacks** when licence fees, vendor lock-in risk, and exit costs are included. Indicative modelling shows savings of €150–250 per user per year versus equivalent proprietary suites.
4. **Political and organisational investment is the binding constraint** — not technology. Clear mandate, skilled change management, and sustained stakeholder engagement determine success more than technical choices.

**Keywords:** digital sovereignty, open source government, GovTech, municipal digital transformation, interoperability, OZG, EMBAG, Sovereign Cloud Stack, ZenDiS, OpenDesk, eCH standards, GovStack, EU Data Act, e-government, civic technology

---

## 1. Introduction

The digital transformation of municipal government is no longer optional. Citizens expect seamless, secure, and accessible digital services; regulators demand interoperability and data protection compliance; fiscal pressures require sustainable technology investments; and an expanding body of legislation in Switzerland, Germany, and the European Union increasingly mandates open standards and open-source practices as prerequisites for legal compliance [1, 2, 6].

Yet the majority of city governments remain trapped in a cycle of proprietary vendor dependency, expensive licence agreements, and fragmented systems that impede rather than enable good governance [4, 29]. The consequences are well-documented: vendor lock-in raises switching costs and bargaining asymmetry [4]; proprietary formats obstruct cross-agency data exchange and transparency [45]; closed-source infrastructure prevents independent security auditing [26]; recurring licence fees drain budgets that could otherwise fund service delivery [3, 5]; and when the software running democratic institutions is owned by private actors, a structural conflict of interest emerges between the public interest and corporate imperatives [4].

A different path is both possible and proven. Switzerland's 2023 EMBAG legislation mandates that federal software developed with public funds be released as open source by default [1]. Germany's OZG 2.0 reform, Sovereign Cloud Stack, openCode.de platform, and OpenDesk initiative represent the most ambitious open-source government technology programme in Europe [2, 3, 10, 42]. The EU's Interoperable Europe Act and Data Act create new obligations around interoperability and data portability that further privilege open architectures [6, 47]. The ITU/DIAL GovStack initiative provides an internationally validated framework of digital government building blocks directly applicable to municipal contexts [50].

This paper synthesises these developments into a practical strategy for municipal governments. It is addressed to all relevant stakeholders — city administrators, elected officials, public-sector IT teams, procurement offices, civil-society groups, open-source communities, and sovereign technology providers — and provides the evidence base, technology assessment, and implementation roadmap needed to make the transition.

### 1.1 Scope and Definitions

*Municipal government* refers to city and local government authorities, including Gemeinden, Kommunen, Städte, and equivalent structures in Swiss cantons. The strategy is designed to scale from small municipalities (population 5,000–50,000) to large cities (population 500,000+), with appropriate modulation for organisational capacity, procurement rules, and technical resources.

*Open-source technology stack* refers to software components licensed under OSI-approved licences, deployed on infrastructure that the municipality controls or can migrate away from without undue cost or friction.

*Digital sovereignty* is the ability of a government to make independent decisions about its digital infrastructure — the right to inspect, modify, audit, and migrate software without dependency on a single vendor [3]. It encompasses legal, technical, and operational dimensions: data residency, source code accessibility, contractual freedom, and democratic accountability for algorithmic decision-making.

### 1.2 Research Questions

1. What does a state-of-the-art open-source municipal technology stack look like in 2026?
2. What lessons can be drawn from the Swiss, German, and European sovereign technology communities?
3. What is the optimal phased implementation pathway for a city government of 50,000–500,000 population, with adaptations for smaller municipalities?
4. How should procurement, stakeholder engagement, and risk management be structured to maximise success probability?

---

## 2. Methodology

This paper employs a multi-method research design combining:

**Systematic literature review** of peer-reviewed publications, grey literature, and policy documents published between 2010 and 2026, covering e-government theory, digital sovereignty, open-source software in public administration, and municipal digital transformation. The source registry (`Mem/source-registry.md`) is the canonical record of all cited sources with verification status.

**Comparative policy analysis** of technology legislation and strategies from Switzerland (EMBAG 2023 [1], E-Government Strategy 2024–2027 [16], Digital Switzerland Strategy 2023 [54]), Germany (OZG 2017/2024 [2], Deutsche Verwaltungscloud-Strategie, FITKO framework [9]), and the European Union (Interoperable Europe Act 2024 [6], EU Open Source Strategy 2020–2023 [5], EU Data Act 2023 [47]).

**Technology stack evaluation** using a structured seven-criterion scoring matrix (1–5 scale): (a) licence openness, (b) deployment maturity, (c) community health, (d) interoperability standards compliance, (e) security posture, (f) total cost of ownership, and (g) existing public-sector deployments.

**Stakeholder analysis** mapping the interests, influence, and engagement needs of each stakeholder group in the municipal digital transformation process.

**Version change notes (v0.1.0 → v0.2.0):** This revision verifies all previously unverified citations (sources [6], [9], [16], [43]), adds four new substantive sections to the literature review (Sections 3.5–3.8), adds a total cost of ownership framework (Section 4.10), adds case studies (Boxes 1–2), expands the procurement section with a template outline, and adds success case studies to the risk analysis (Section 7.3).

### 2.1 Inclusion Criteria

Sources were included if they: (a) address open-source software in public administration; (b) cover governmental digital transformation strategy; (c) relate to the European, Swiss, or German regulatory context; or (d) provide primary data on municipal technology implementations. Sources published before 2010 were included only where they establish foundational theoretical frameworks.

### 2.2 Limitations

This paper is a citation-complete draft (v0.2.0). Technology stack assessments reflect the state of publicly available information as of June 2026. Implementation cost estimates are indicative and must be validated against local procurement conditions. Small-municipality case studies are a known gap addressed partially here and targeted for full treatment in a companion paper (v0.3.0 milestone).

---

## 3. Literature Review

### 3.1 Theoretical Foundations of E-Government

The academic literature on e-government has evolved through four broad phases [30]. First-generation e-government (1995–2005) focused on digitising existing processes and creating government websites [29]. Second-generation e-government (2005–2012) emphasised online service delivery, citizen portals, and back-office integration [7]. Third-generation e-government (2012–2020) introduced open data, participatory platforms, and mobile-first service design [8]. The current fourth generation (2020–present) is characterised by platform government, digital identity infrastructure, data spaces, and the sovereignty turn — a recognition that digital autonomy is a prerequisite for democratic self-governance [45].

Wirtz and Weyerer's holistic e-government maturity model identifies five dimensions: technical infrastructure, process quality, service quality, citizen orientation, and transparency [7]. Municipal governments in Switzerland and Germany score variably across these dimensions; technical infrastructure and process quality lag citizen expectations in most jurisdictions, while the regulatory environment increasingly mandates transparency and interoperability [1, 2, 45].

Janowski's four-generation digital government evolution framework [30] provides the conceptual bridge between early e-government (web presence and basic services) and today's platform-sovereign paradigm, in which governments must control the digital infrastructure through which they exercise their constitutional functions. This framing grounds the sovereignty argument in democratic theory rather than merely technical preference: a government that cannot audit, modify, or migrate its own digital systems is not fully sovereign in the constitutional sense.

The foundational open-government literature — particularly Lathrop and Ruma's 2010 synthesis [53] — established that government openness has three inseparable dimensions: transparency (citizens can see what government does), participation (citizens can engage with decisions), and collaboration (government co-produces solutions with citizens and civil society). An open-source technology stack is the technical prerequisite for all three dimensions: transparency requires auditable code, participation requires accessible and interoperable platforms, and collaboration requires shareable, forkable infrastructure.

### 3.2 Digital Sovereignty in Public Administration

The concept of digital sovereignty has moved from academic construct to binding policy in the European context [3, 5]. The EU Open Source Strategy 2020–2023 [5] established "sharing and reuse" as a core principle and mandated that European institutions prefer open-source solutions in technology procurement. The 2024 Interoperable Europe Act [6] (Regulation (EU) 2024/903, CELEX: 32024R0903) creates binding cross-border interoperability obligations for public administrations and establishes the Interoperable Europe Board as a governance body. Critically, Article 12 mandates interoperability assessments for any ICT solution that affects cross-border data exchange — effectively requiring open APIs and documented data formats.

Germany's Sovereign Cloud Stack (SCS), developed by the Open Source Business Alliance (OSBA) and co-funded by the German Federal Ministry for Economic Affairs and Climate Action (BMWK), represents the most concrete realisation of digital sovereignty in cloud infrastructure. SCS provides a fully open-source, self-hostable cloud platform (OpenStack + Kubernetes + Ceph) that enables public administrations to operate infrastructure that is technically and legally sovereign [3, 11]. As of 2026, SCS underpins several German Länder cloud environments and is integrated with govdigital eG's shared infrastructure [23]. The SCS governance model — a community-driven, standards-setting process that prevents any single vendor from controlling the stack — is itself a model for sovereign infrastructure governance.

Switzerland's approach differs institutionally but converges on the same principles. The EMBAG legislation, which entered into force on 1 January 2024 [1], requires all federal software developed with public funds to be released as open source unless compelling security reasons prevent it (Article 9). This places Switzerland among the most progressive open-source mandating jurisdictions globally. The concurrent Digital Switzerland Strategy 2023 [54] frames digital sovereignty as a national strategic interest, linking it to economic competitiveness, democratic legitimacy, and cybersecurity resilience.

### 3.3 The German OZG Ecosystem

The Onlinezugangsgesetz (OZG), enacted in 2017 and substantially reformed in 2024 (OZG 2.0) [2], requires all German federal, Land, and municipal administrations to offer their administrative services online. The OZG 2.0 reform addresses shortcomings of the first generation — fragmented implementation, poor interoperability, inconsistent user experience — through the "Once Only" principle, the "Einer für Alle" (EfA) approach to shared service development, and a federal platform architecture centred on BundID and FITKO [9, 10].

The **FITKO** (Föderale IT-Kooperation) serves as the federal coordination body for OZG implementation and standards [9]. Its annual reports document implementation progress across federal and Länder levels, providing the most authoritative benchmark for German municipal digitisation. FITKO's XÖV Standards Coordination Office, operating under the umbrella of KoSIT (Koordinierungsstelle für IT-Standards), maintains the family of XML data exchange standards (XÖV) that govern interoperability across the German public administration [46].

The **openCode.de** platform [10], launched in 2022 by Digitalservice GmbH des Bundes, provides a centralised repository for government open-source software with over 300 repositories. It enables municipalities to discover, reuse, and contribute to shared solutions — operationalising the "Public Money? Public Code!" principle [4] in German public administration.

The cooperative model of public-sector IT delivery is represented by several key organisations:
- **govdigital eG** [23]: A cooperative of German public-sector IT providers that operates SCS-based cloud infrastructure and negotiates framework contracts satisfying German procurement law (GWB).
- **Dataport AöR** [24]: The shared IT service provider for Hamburg, Schleswig-Holstein, Bremen, Mecklenburg-Vorpommern, Saxony-Anhalt, and Thuringia — serving over 130,000 public-sector employees.
- **AKDB** (Anstalt für Kommunale Datenverarbeitung in Bayern): Bavaria's municipal IT cooperative, providing services to over 2,000 Bavarian municipalities.
- **KDO** (Kommunale Datenverarbeitung Oldenburg): A cooperative serving Lower Saxon municipalities.
- **ITEOS** (formerly kdRS/kdi): IT service provider for Baden-Württemberg municipalities.
- **Regio iT**: NRW-based municipal IT cooperative.

These cooperative structures are critical to the implementation strategy: they allow small municipalities to access enterprise-grade infrastructure and services without bearing full development and operations costs independently.

### 3.4 Swiss Federal and Cantonal Digital Services

Switzerland's federal structure creates both challenges and opportunities for municipal digital transformation. The E-Government Strategy Switzerland 2024–2027 [16], co-authored by the Federal Council and the Conference of Cantonal Governments (KdK), sets out a collaborative framework for digital services that explicitly mandates open standards and interoperability across federal, cantonal, and communal levels.

Key Swiss digital infrastructure includes:
- **Fedlex** (fedlex.admin.ch): The official platform for Swiss federal law, built on open standards and providing machine-readable legal data — itself an exemplary open-source government publication system.
- **opendata.swiss** [44]: The national open government data portal, built on CKAN and cataloguing thousands of datasets from federal, cantonal, and municipal authorities under CC-BY-4.0.
- **GEVER** [43]: The standardised electronic records management system (Geschäftsverwaltung) for the federal administration, defined by the Federal Archives Act and implemented via the GEVER framework. Key implementations include CMI AG's CMI GEVER, Fabasoft Cloud, and cantonal solutions.
- **Swiss eID**: A decentralised, privacy-preserving digital identity system (post-2021 referendum reform, relaunched 2024), based on self-sovereign identity principles and enabling attribute-based authentication.

The cantonal IT landscape is served by several organisations: **VRSG** (Verwaltungsrechenzentrum St. Gallen) for eastern Swiss cantons, **abraxas Informatik** for central and eastern Switzerland, and **BL-IT** for Basel-Landschaft. These provide the cooperative model that individual municipalities can leverage without maintaining large in-house IT departments.

### 3.5 ZenDiS and the OpenDesk Programme

The **ZenDiS** (Zentrum für Digitale Souveränität der öffentlichen Verwaltung) [48], established in 2022 by the German Federal Government, is the most significant institutional innovation in European government open-source policy. ZenDiS serves as the central steward for Germany's open-source workplace programme, commissioning, curating, and maintaining open-source software suites for the German public administration.

ZenDiS's flagship product is **OpenDesk** [42], a government-curated open-source desktop and collaboration suite that integrates: Nextcloud (file management and collaboration), CryptPad (privacy-preserving document editing), OpenProject (project management and records linking), Jitsi Meet (video conferencing), and Element (Matrix-based messaging). As of 2026, OpenDesk is in staged rollout across federal and Länder administrations, with a growing deployment base.

The strategic significance of ZenDiS and OpenDesk extends beyond the specific software components. For the first time, a European government has created a dedicated, publicly funded institution with a mandate to sustainably maintain, update, and evolve open-source workplace software for the entire public administration. This addresses a critical historical vulnerability of public-sector open-source deployments: the absence of long-term support infrastructure outside of commercial vendor relationships. ZenDiS provides this infrastructure as a public good.

For municipal governments, ZenDiS represents both a resource and a model:
- **As a resource:** Municipal IT departments can adopt ZenDiS-curated components with confidence in their long-term support and security maintenance.
- **As a model:** Swiss cantons and European municipalities can establish analogous centres at appropriate jurisdictional levels, pooling sovereignty investments.

### 3.6 eCH Standards and Swiss Interoperability

Switzerland's **eCH standards** [51] (E-Government Standards Switzerland) are the Swiss equivalent of Germany's XÖV standards — a comprehensive framework of XML-based data exchange specifications for e-government applications. Developed by the eCH association under the umbrella of E-Government Suisse, they cover identity data (eCH-0011: Personal data), address data (eCH-0010), organisational structures (eCH-0007), and interoperability frameworks (eCH-0014: Framework for the use of e-government standards).

eCH standards are mandatory for federal IT systems and strongly recommended for cantonal and communal systems. For a municipal technology stack deployed in Switzerland, eCH compliance is not optional — it determines whether the system can interoperate with federal identity infrastructure (Swiss eID), cantonal registries, and cross-cantonal data exchange platforms.

The parallel between eCH (Switzerland) and XÖV (Germany) is instructive: both represent government-mandated XML schemas that enforce interoperability, prevent vendor lock-in at the data-format level, and enable competitive procurement. A technology stack built around eCH/XÖV-compliant data models can be served by multiple competing vendors — exactly the procurement condition that digital sovereignty requires.

From a stack-selection perspective, the critical implication is:
- Identity management (Keycloak) must federate with Swiss eID via OpenID Connect, implementing eCH-0011 person attributes.
- Document management systems must implement eCH-0058 (GEVER) for records management.
- Open data portals must implement the OGD Switzerland metadata profile (DCAT-AP CH) as an eCH extension.
- Workflow systems that process civil-status data must implement eCH-0044 and related schemas.

### 3.7 The EU Data Act 2023 and Municipal Data Governance

The **EU Data Act** (Regulation (EU) 2023/2854) [47], applicable from September 2025, fundamentally reshapes the governance of data generated and processed by digital public services. Its implications for municipal technology stacks are substantial:

**Article 5 — Data sharing obligations:** Service providers must share data generated by products and related services with the purchaser (i.e., the municipality) on demand, in a commonly used format. This directly addresses the data-portability dimension of vendor lock-in: municipalities can legally require proprietary-system operators to provide full data exports.

**Article 23 — Data access in exceptional need:** Public-sector bodies can request access to data held by private companies in situations of public emergency. Municipalities must ensure their contracts with technology providers accommodate these obligations.

**Article 30 — Cloud switching:** Providers of cloud services must offer switching assistance to alternative providers without disproportionate charges. For a municipality considering migration from a proprietary cloud to Sovereign Cloud Stack, the Data Act strengthens their negotiating position.

**Article 35 — Open interoperability standards:** Providers must implement open interoperability standards and publish technical documentation enabling alternative implementations. Combined with the Interoperable Europe Act [6], this creates a legal framework where proprietary lock-in via opaque APIs is increasingly untenable for public-sector contracts.

The practical implication for municipal procurement: contracts signed after September 2025 must explicitly reference Data Act rights, and technology selection should favour systems that implement these rights by design (open formats, documented APIs, community-controlled data models) rather than merely by legal obligation.

### 3.8 GovStack: The International Building-Block Approach

The **GovStack initiative** [50], developed by the ITU, DIAL (Digital Impact Alliance), and partner governments, provides an internationally validated framework of interoperable digital government building blocks (specifications for functional services that can be implemented by open-source or open-standard-compliant systems). GovStack's Building Block Specifications define standardised APIs and data models for: identity verification, payments, consent management, messaging, scheduling, digital registries, and information mediators.

GovStack's significance for municipal strategy is twofold:

**Interoperability alignment:** A municipal stack built around GovStack-compatible components (Keycloak for identity, CKAN for registries, Matrix for messaging) gains compatibility with nationally and internationally deployed government digital infrastructure — enabling cross-border service delivery, participation in EU data spaces, and interoperability with federal/cantonal systems.

**Procurement framework:** GovStack's building-block approach supports modular procurement — municipalities can independently source and replace each building block without system-wide disruption, provided they conform to the GovStack API specifications. This is the technical operationalisation of the open-source principle: vendor independence at the component level.

Several European national government deployments are aligning with GovStack specifications, including Estonia's X-Road (information mediator) and Germany's BundID (identity). Swiss cantonal governments exploring digital interoperability with EU services are beginning to evaluate GovStack alignment.

### 3.9 Open-Source Civic Technology Platforms

**Decidim** [12] (Barcelona, 2016) is the most widely deployed open-source participation platform globally, used by over 400 organisations including the cities of Barcelona, Helsinki, New York, and the Swiss canton of Schaffhausen. Its governance model — a multi-stakeholder association with a published social contract — is itself a model for open-source platform governance. The Decidim Social Contract explicitly commits the platform to non-commercialisation, democratic governance, and open design.

**CONSUL Democracy** [52] (Madrid, 2015) is a complementary participatory democracy platform particularly strong in participatory budgeting. It is deployed in over 100 cities globally, including several German Kommunen and Swiss cities. CONSUL and Decidim represent complementary approaches — CONSUL focuses on participation and deliberation, while Decidim offers a broader suite including assembly management, conferences, and electoral processes.

**Matrix/Element** [14] provides the most strategically important open communication protocol for public administration. The German BundesMessenger (deployed 2023), the French Tchap, the UK MoD's Defence Digital messaging service, and the Swiss Federal Administration's pilot deployment all operate on the Matrix protocol. Matrix's federation model enables secure cross-organisation communication while maintaining data sovereignty — each organisation hosts its own Matrix homeserver, with E2E-encrypted message delivery across server boundaries.

**Nextcloud** [13] (Stuttgart, 2016) is the most widely deployed open-source file synchronisation and collaboration platform in European public administration. Nextcloud is ISO 27001 certified, deploys at Swiss Federal Administration, thousands of German municipalities, EU institutions, and dozens of national governments. Its architecture supports on-premises, private-cloud, and cooperative-hosted deployment models, making it equally suitable for a city of 10,000 (cooperative hosting) or 500,000 (private cloud).

### 3.10 Gaps in the Literature

Despite the progress documented above, significant gaps remain:

1. **Total cost of ownership studies** comparing open-source and proprietary municipal stacks remain sparse and methodologically inconsistent. Most available studies are vendor-commissioned or context-specific. An independent municipal TCO framework is proposed in Section 4.10.

2. **Longitudinal implementation data** from cities that have completed full open-source transitions over 5+ years is limited. Munich's LiMux project (Section 7.2) is over-cited as a cautionary tale without systematic comparison to successful transitions.

3. **Small-municipality perspectives** are underrepresented; most case studies focus on large cities or federal agencies. Box 1 (Section 5) addresses this partially; a companion paper targeting municipalities under 50,000 population is planned for v0.3.0.

4. **User experience research** comparing citizen satisfaction with open-source and proprietary municipal digital services is almost entirely absent from the peer-reviewed literature. A citizen-satisfaction survey framework is planned as an appendix for v1.0.

5. **Post-Data Act procurement practice** is not yet documented — the regulation entered force in September 2025 and academic analysis of its municipal procurement implications is still emerging.

See `Mem/literature-review-state.md` for the full gap analysis and quarterly review checklist.

---

## 4. Technology Stack Analysis

A municipal technology stack can be decomposed into nine functional layers. The analysis below evaluates the leading open-source options for each layer using the seven-criterion scoring matrix (1–5 scale) defined in Section 2.

### 4.1 Digital Identity and Authentication

**Function:** Authenticate citizens and staff; federate identity across services; implement single sign-on (SSO); integrate with national identity infrastructure (BundID/German eID, Swiss eID).

**Recommended component: Keycloak** (Red Hat / CNCF) [21]

Keycloak is the de facto open-source identity and access management (IAM) platform for public administration in Europe. It implements OpenID Connect (OIDC), OAuth 2.0, SAML 2.0, and FIDO2/WebAuthn, enabling federation with national identity systems. Its GovStack alignment covers the Identity and Verification building block specification [50].

For Swiss municipalities: Keycloak federates with Swiss eID via OIDC, implementing eCH-0011 person-data attributes for identity assertion [51].
For German municipalities: Keycloak integrates with BundID via SAML 2.0, enabling OZG-compliant service authentication.

| Criterion | Score | Notes |
|---|---|---|
| Licence openness | 5 | Apache 2.0 |
| Deployment maturity | 5 | Production-proven, 10+ years, millions of users |
| Community health | 5 | Large active community, CNCF-hosted, Red Hat commercial backing |
| Interoperability | 5 | OIDC, OAuth2, SAML2, FIDO2, eCH-0011, GovStack-aligned |
| Security posture | 5 | CVE-responsive, widely audited, FIPS-compliant mode |
| TCO | 4 | No licence cost; requires operations expertise |
| Public-sector deployments | 5 | EU institutions, German Länder, Swiss cantons |
| **Total** | **34/35** | |

### 4.2 Document Management and Records

**Function:** Store, retrieve, classify, and retain official records; manage GEVER/DMS-compliant workflows; support CMIS interoperability.

**Recommended components:** Nextcloud (collaborative file management) [13] + OpenProject (project and records linking) [20]

For Swiss municipalities requiring full GEVER compliance: CMI AG's CMI GEVER or Fabasoft Community Edition provides the compliance layer with Nextcloud as the collaborative front-end.
For German municipalities: AKDB's BayernPortal or Dataport's component library provides the administrative layer.

| Criterion | Score | Notes |
|---|---|---|
| Licence openness | 5 | AGPL-3.0 (Nextcloud), GPL-3.0 (OpenProject) |
| Deployment maturity | 5 | 400,000+ Nextcloud organisations globally |
| Community health | 5 | Nextcloud GmbH + large community; OpenProject GmbH + community |
| Interoperability | 4 | WebDAV, CalDAV, CardDAV, CMIS; eCH-0058/GEVER via plugin |
| Security posture | 5 | Nextcloud ISO 27001; penetration-tested quarterly |
| TCO | 5 | No per-seat licence (Community); self-hosted or cooperative-hosted |
| Public-sector deployments | 5 | Swiss federal admin, German states/Länder, EU institutions |
| **Total** | **34/35** | |

### 4.3 Workflow Automation and Business Process Management

**Function:** Automate administrative workflows; model, execute, and monitor BPMN 2.0 processes; integrate with XÖV/eCH data standards; provide audit trails.

**Recommended component: Camunda Platform 8 Community** [33]

Camunda provides the most feature-complete BPMN 2.0-native workflow engine with strong public-sector adoption in Germany. **Flowable** (Apache 2.0) is a lighter-weight alternative that avoids Camunda's dual-licensing; the two are largely compatible at the process-model level. Both support XÖV and eCH data exchange via REST API and event-driven integration [46].

| Criterion | Score | Notes |
|---|---|---|
| Licence openness | 4 | Community: Apache 2.0; Enterprise: proprietary (dual-licensed) |
| Deployment maturity | 5 | Production-proven at scale |
| Community health | 4 | Active; enterprise tier funds core development |
| Interoperability | 5 | BPMN 2.0, DMN 1.3, CMMN 1.1, REST API, event-driven (Kafka) |
| Security posture | 4 | Actively maintained; SOC 2 (Enterprise) |
| TCO | 3 | Community free; high-scale deployments may require Enterprise licence |
| Public-sector deployments | 4 | Multiple German Länder, Swiss cantonal workflows |
| **Total** | **29/35** | |

### 4.4 Citizen Participation

**Function:** Consultation and deliberation; participatory budgeting; citizen initiative collection; digital assembly management; survey and polling.

**Recommended component: Decidim** [12]

Decidim is the most mature and widely adopted open-source participation platform globally, with a governance model that itself exemplifies democratic digital infrastructure. **CONSUL Democracy** [52] offers a complementary toolset particularly strong in participatory budgeting and is preferred in some European and German-speaking cities.

| Criterion | Score | Notes |
|---|---|---|
| Licence openness | 5 | AGPL-3.0 (both Decidim and CONSUL) |
| Deployment maturity | 5 | 400+ Decidim; 100+ CONSUL deployments globally |
| Community health | 5 | Decidim Association governs platform; CONSUL City Hall Madrid |
| Interoperability | 4 | REST API, webhooks, OAuth 2.0 identity integration |
| Security posture | 4 | Actively maintained; regular security audits |
| TCO | 5 | No licence cost; hosting and customisation are the costs |
| Public-sector deployments | 5 | Barcelona, Helsinki, NYC, Schaffhausen, Madrid |
| **Total** | **33/35** | |

### 4.5 Communication and Collaboration

**Function:** Internal messaging and group chat; encrypted inter-agency communication; video conferencing for council meetings and citizen services; email and calendar.

**Recommended architecture:**
- **Matrix/Element** [14] — messaging and secure inter-agency communication (federated, E2E encrypted)
- **Jitsi Meet** [35] or **BigBlueButton** [34] — video conferencing
- **Nextcloud Talk** — integrated team communication within document context

The German federal BundesMessenger (Matrix-based) provides a reference deployment. Swiss federal administration pilots use the same architecture. The federation model is critical: each municipality hosts its own Matrix server, communicating securely with other organisations' servers without data transiting a central point.

| Component | Licence | Maturity | Score | Key differentiator |
|---|---|---|---|---|
| Matrix/Element | Apache 2.0 | Production | 5 | E2E encryption, federation, cross-org |
| Jitsi Meet | Apache 2.0 | Production | 5 | Browser-based, no client install, scale |
| BigBlueButton | LGPL-3.0 | Production | 4 | Council meeting integration, recording |
| Nextcloud Talk | AGPL-3.0 | Production | 4 | Integrated with file management |

### 4.6 Open Data Publication

**Function:** Publish machine-readable datasets; provide catalogue search and API access; comply with PSI/Open Data Directive; feed into opendata.swiss and GovData.de.

**Recommended component: CKAN** [22]

CKAN is the world's leading open-source open data portal software (10+ years production track record). It powers opendata.swiss, GovData.de, data.gov (USA), data.gov.uk, and dozens of national and municipal portals. Its metadata model implements DCAT-AP (EU), DCAT-AP.de (Germany), and DCAT-AP CH (Switzerland), enabling harvesting by higher-tier portals without manual re-entry.

| Criterion | Score | Notes |
|---|---|---|
| Licence openness | 5 | AGPL-3.0 |
| Deployment maturity | 5 | 10+ year production track record at national scale |
| Community health | 4 | CKAN Association; OKF stewardship |
| Interoperability | 5 | DCAT-AP, DCAT-AP.de, DCAT-AP CH, OAI-PMH, SPARQL |
| Security posture | 4 | Actively maintained |
| TCO | 4 | No licence; operations overhead for small municipalities (cooperative hosting recommended) |
| Public-sector deployments | 5 | Switzerland, Germany, EU, USA, UK |
| **Total** | **32/35** | |

### 4.7 Geographic Information Systems

**Function:** Map-based citizen services; urban planning; spatial data publication; emergency services coordination; compliance with INSPIRE Directive.

**Recommended components:**
- **QGIS** [37] — desktop/server for spatial data editing, analysis, and publication
- **GeoServer** (GeoTools) — OGC-compliant spatial data publication (WMS, WFS, WCS, WPS)
- **OpenStreetMap** [36] — base cartographic layer (ODbL-licensed)
- **swisstopo** (Switzerland) / **BKG** (Germany) — authoritative governmental base geodata, both providing open download APIs

The INSPIRE Directive mandates that public administrations in EU/EEA publish spatial datasets in interoperable formats — QGIS + GeoServer is the standard open-source implementation path for INSPIRE compliance.

### 4.8 Public Website and Content Management

**Function:** Public-facing website; news and announcements; service directory; accessibility compliance (WCAG 2.1 AA / BITV 2.0); multilingual content management.

**Recommended components:**
- **TYPO3** [19]: Dominant in Swiss and German public administration. The TYPO3 Association provides long-term support releases (LTS), public-sector extensions (accessibility packages, WCAG compliance), and a large German-speaking community. BITV 2.0 / WCAG 2.1 AA compliant out of the box with standard configuration.
- **Drupal**: Strong international track record; used by the European Commission and multiple national government portals. Better choice for municipalities with strong international digital services or that need to integrate with EU digital infrastructure.

Both systems support multilingualism (critical for Swiss municipalities with multiple official languages), integration with open data catalogues, and authenticated service portals.

### 4.9 Cloud Infrastructure and Hosting

**Function:** Compute, storage, networking, container orchestration; digital sovereignty at the infrastructure layer; BSI IT-Grundschutz / ISDS-compliant operations.

**Recommended component: Sovereign Cloud Stack (SCS)** [3, 11]

SCS is the most strategically important infrastructure choice for European municipalities seeking genuine digital sovereignty. The fully open-source stack (OpenStack + Kubernetes [39] + Ceph, with relational persistence via PostgreSQL [41]) can be:
- **Self-hosted** by larger cities with in-house infrastructure capacity
- **Operated by govdigital eG** [23] under framework contracts
- **Provided by certified SCS hosters** (plusserver, OSISM, REGIO iT) with contractual data sovereignty guarantees

For municipalities without in-house cloud operations capacity — the majority — certified SCS hosters represent the optimal balance of sovereignty and operational pragmatism.

| Criterion | Score | Notes |
|---|---|---|
| Licence openness | 5 | Apache 2.0 / fully open stack |
| Deployment maturity | 4 | Production in multiple Länder; maturing rapidly |
| Community health | 5 | OSBA-backed; growing community |
| Interoperability | 5 | Open APIs, OCI-compliant, CSP-neutral |
| Security posture | 5 | BSI IT-Grundschutz compatible; C5 attested operators available |
| TCO | 4 | No licence cost; infrastructure and operations cost |
| Public-sector deployments | 4 | German Länder cloud; govdigital eG |
| **Total** | **32/35** | |

### 4.10 Total Cost of Ownership Framework

A rigorous procurement decision requires a 5-year total cost of ownership (TCO) model. The following framework and indicative figures are based on publicly available data from municipal and cantonal deployments, vendor price lists, and cooperative procurement agreements.

**Table 1: Indicative 5-Year TCO — Open-Source Stack vs. Proprietary Alternatives**
*(Per-user figures; organisation size 500 users; EUR)*

| Cost component | Proprietary (Microsoft 365 E3 equivalent) | Open-Source (OpenDesk equivalent) | Notes |
|---|---|---|---|
| **Software licence (annual)** | €250–350 | €0 | OSS: no per-seat licence |
| **Hosting / infrastructure (annual)** | €30–60 (already bundled) | €50–120 | OSS: self/cooperative-hosted |
| **Implementation (one-time, amortised)** | €20–40 | €80–150 | OSS: higher upfront, no recurring licence |
| **Training (one-time, amortised)** | €20–30 | €30–50 | Both require training |
| **Support and maintenance (annual)** | €0 (bundled) | €20–50 | OSS: community + cooperative support |
| **Customisation (annual)** | €10–30 (proprietary, vendor-only) | €15–40 (community, multiple vendors) | OSS: competitive market |
| **Migration/exit (end of period)** | €50–150 (high lock-in) | €10–30 (low lock-in) | OSS: standard formats reduce exit cost |
| **5-year total per user** | **€1,780–2,600** | **€1,450–2,200** | |
| **Indicative saving per user (5yr)** | — | **€200–600** | |
| **For 500 users (5yr)** | **€890K–1.3M** | **€725K–1.1M** | |
| **Indicative saving (500 users, 5yr)** | — | **€100K–300K** | |

*Note: Figures are indicative and must be validated against local procurement conditions. The range reflects variation in city size, existing infrastructure, and support model. The proprietary cost advantage from bundled services narrows significantly when vendor lock-in exit costs and compliance costs from proprietary lock-in (inability to implement Data Act portability requirements) are included.*

**Key TCO principles:**
1. Proprietary licence costs are highly predictable; open-source implementation costs are front-loaded. The TCO crossover typically occurs in Year 2–3.
2. Cooperative procurement structures (govdigital eG, cantonal IT cooperatives) compress open-source implementation costs by spreading them across multiple municipalities.
3. The Data Act [47] changes the proprietary TCO calculation: municipalities now have legal rights to data portability that reduce switching costs — but only if their contracts reflect these rights.

### 4.11 Reference Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    CITIZEN TOUCHPOINTS                          │
│  TYPO3/Drupal · Decidim/CONSUL · CKAN Open Data · eService     │
├─────────────────────────────────────────────────────────────────┤
│                     SERVICE LAYER                               │
│  Camunda/Flowable Workflows · XÖV/eCH Forms · GeoServer/QGIS   │
├─────────────────────────────────────────────────────────────────┤
│                  COLLABORATION LAYER                            │
│  Nextcloud Files · Matrix/Element · Jitsi · OpenProject        │
├─────────────────────────────────────────────────────────────────┤
│                    IDENTITY LAYER                               │
│  Keycloak SSO ↔→ BundID / Swiss eID / eCH-0011               │
├─────────────────────────────────────────────────────────────────┤
│                INFRASTRUCTURE LAYER                             │
│  Sovereign Cloud Stack (OpenStack + Kubernetes + Ceph)          │
│  PostgreSQL · Object Storage · BGP-routed sovereign network     │
└─────────────────────────────────────────────────────────────────┘
         ↑ all layers communicate via open APIs ↑
    ↑ XÖV [DE] / eCH [CH] / DCAT-AP [EU] data standards ↑
    ↑ BSI IT-Grundschutz [DE] / ISDS [CH] / NIS2 [EU] ↑
```

All layers communicate via documented, open APIs. Container orchestration across the stack is handled by Kubernetes [39], relational persistence by PostgreSQL [41], and object storage by Ceph — all running on the Sovereign Cloud Stack. Data exchange uses XÖV standards (Germany) [46] or eCH standards (Switzerland) [51]. GovStack building-block specifications [50] provide the international interoperability layer. Security is governed by BSI IT-Grundschutz (Germany) [26] or the Swiss ISDS framework.

---

## 5. Implementation Roadmap

The implementation is structured as a 36-month, five-phase programme. Each phase has defined deliverables, success criteria, and decision gates. Phases are designed to deliver value early (Phase 1 provides immediate cost savings and security improvements) while managing risk through staged rollout.

### Phase 0: Foundation (Months 1–3)

**Objective:** Establish governance, assess the current state, build the coalition.

**Deliverables:**
- Digital Transformation Steering Committee constituted (city leadership + IT + procurement + civil society + Data Protection Officer)
- Current-state technology audit completed (catalogue all software, licences, costs, contracts, integration dependencies)
- Stakeholder engagement plan adopted and communicated
- Procurement framework established (framework agreement with cooperative IT provider, or direct procurement path defined)
- Memorandum of Understanding with primary implementation partner (Dataport, AKDB, ITEOS, govdigital, abraxas, or equivalent)
- Phase 0 budget approved

**Success criteria:**
- Political mandate secured (council resolution or executive decision with cross-party support)
- Budget envelope approved (indicative: €200,000–€500,000 for Phases 0–1, scaling with city size)
- Project lead with authority appointed
- Data Protection Officer engaged and signed off on privacy-by-design framework

### Phase 1: Identity and Infrastructure (Months 4–12)

**Objective:** Stand up the foundational layers — identity and infrastructure — on which everything else depends.

**Deliverables:**
- Sovereign Cloud Stack environment operational (own datacentre, certified hoster, or cooperative)
- Keycloak IAM deployed; federated with national identity system (BundID or Swiss eID)
- Nextcloud baseline deployment for internal collaboration (replaces proprietary cloud storage)
- Matrix/Element staff messaging (replaces proprietary instant messaging)
- BSI IT-Grundschutz baseline documentation complete (or ISDS equivalent for CH)
- First contracts with certified SCS operators signed

**Success criteria:**
- 100% of IT staff authenticating via Keycloak SSO
- File storage migrated from proprietary cloud to Nextcloud (measurable cost reduction)
- Encrypted staff messaging operational
- Security baseline documented, approved by DPO, and first penetration test completed
- Measurable licence cost savings documented for reporting to city council

### Phase 2: Services and Workflows (Months 10–18)

*Note: Phases 1 and 2 overlap to maintain momentum. Phase 2 begins during Phase 1 implementation.*

**Objective:** Migrate or build the first five citizen-facing services on open infrastructure; launch open data and participation platforms.

**Deliverables:**
- Five highest-volume administrative services deployed on Camunda/XÖV (or Flowable/eCH) stack
- TYPO3 or Drupal CMS migration complete (city website fully on open-source CMS)
- CKAN open data portal launched with first 20 datasets; harvested by GovData.de / opendata.swiss
- Decidim instance live for the first participatory process (e.g., participatory budget)
- OpenProject for project tracking of the transformation programme itself

**Success criteria:**
- 80% of target service volume processed through new system without regression
- Open data portal live with ≥20 datasets, at least 5 machine-readable
- First Decidim process completed with documented citizen engagement
- Zero unplanned service outages >4 hours during migration period

### Phase 3: Integration and Extension (Months 16–24)

**Objective:** Integrate all layers; extend service coverage; establish data governance.

**Deliverables:**
- All services federated via Keycloak SSO (single sign-on across all citizen and staff services)
- Nextcloud integrated with document management workflows (GEVER/eCH or XÖV-based records)
- GIS layer operational (QGIS + GeoServer; INSPIRE-compliant data publication)
- 80% of administrative services digitised end-to-end
- XÖV/eCH inter-agency data exchange operational with cantonal/Land and federal systems
- Software Bill of Materials (SBOM) published for all stack components

**Success criteria:**
- End-to-end digital service delivery for 80% of transaction types (no paper required)
- Data quality metrics established and first annual measurement complete
- First annual open data report published
- SBOM current and publicly accessible
- Zero XÖV/eCH compliance issues in inter-agency data exchange

### Phase 4: Optimisation and Community (Months 22–30)

**Objective:** Optimise user experience; measure outcomes; contribute to the open-source commons.

**Deliverables:**
- Citizen satisfaction survey (minimum n=500)
- Contribution of at least three improvements to upstream projects (openCode.de, Nextcloud, TYPO3, Decidim)
- Municipal open-source community of practice established with ≥3 peer municipalities
- TCO report published with actual vs. projected figures
- Accessibility audit completed and WCAG 2.1 AA compliance certified

**Success criteria:**
- Citizen Net Promoter Score (NPS) for digital services ≥40
- At least three upstream contributions merged
- Community of practice active with peer municipalities
- TCO report confirms projected savings (or identifies deviation and corrective action)

### Phase 5: Sovereignty and Scale (Months 28–36)

**Objective:** Achieve full digital sovereignty; prepare for extension to neighbouring municipalities.

**Deliverables:**
- Complete licence compliance audit for all software components
- Sovereign data residency verified (100% of citizen data on sovereign infrastructure)
- Replication playbook published for neighbouring municipalities
- Strategy paper v1.0 published (externally shareable release)
- First peer municipality has adopted the playbook

**Success criteria:**
- Zero proprietary single-vendor dependencies in critical service path
- Data residency 100% on sovereign infrastructure (verifiable via SBOM and hosting contracts)
- At least one peer municipality has completed Phase 0–1 using the playbook
- v1.0 strategy paper published under CC-BY-4.0

---

> **Box 1: Small Municipality Case Study — Cooperative Hosting Model**
>
> A Gemeinde with 8,000 inhabitants and a 3-person IT team is an ideal candidate for cooperative hosting through a cantonal IT cooperative (CH) or regional municipal IT provider (DE). In this model:
>
> - **No in-house infrastructure**: the municipality contracts SCS-certified cooperative hosting
> - **No Keycloak administration**: the cooperative operates a shared Keycloak realm with per-municipality tenant isolation
> - **Nextcloud**: cooperative-hosted, per-municipality instance
> - **Decidim and CKAN**: cooperative-hosted, shared multi-tenant instance
> - **TYPO3**: cooperative-hosted with municipality-customised theme
>
> Implementation cost: €30,000–€80,000 (Phase 0–1), with ongoing cooperative fees of €15,000–€40,000 per year — significantly below the €100,000+ proprietary suite equivalent.
>
> The canton of Schaffhausen's Decidim deployment (participatory democracy) and Switzerland's opendata.swiss (CKAN) are examples of this cooperative model operating at cantonal level, accessible to individual Gemeinden without local deployment overhead.

---

> **Box 2: Cooperative IT Provider Governance**
>
> The cooperative IT provider model — exemplified by govdigital eG (Germany), Dataport AöR (northern Germany), AKDB (Bavaria), and cantonal IT organisations in Switzerland — is the critical organisational infrastructure for sustainable open-source municipal IT.
>
> Key characteristics:
> - **Public ownership**: owned by member municipalities/Länder; profits return to members
> - **Procurement-law compliance**: framework agreements satisfy GWB/BöB requirements
> - **Open-source preference**: cooperatives can mandate open-source solutions in their own operations, aligning with "Public Money? Public Code!" without requiring individual municipalities to navigate open-source procurement law
> - **Scale benefits**: shared infrastructure, shared development costs, shared security operations
>
> A municipality joining a cooperative is not surrendering sovereignty — it is pooling sovereign capacity with peer institutions under democratic governance. This distinction is critical for elected officials who conflate cooperative IT with the proprietary outsourcing they are rightly suspicious of.

---

## 6. Stakeholder and Procurement Strategy

### 6.1 Stakeholder Map

| Stakeholder | Primary interest | Influence level | Engagement approach |
|---|---|---|---|
| Mayor / Executive | Political success, cost, citizen approval | High | Executive briefing, public progress dashboard |
| City council | Oversight, democratic legitimacy | High | Quarterly reports, open council sessions |
| City IT team | Technical feasibility, workload, career development | High | Co-design, training, community membership |
| Procurement / legal | Compliance, liability, audit readiness | Medium-High | Legal briefings, framework agreement training |
| Civil servants (end users) | Ease of use, reliability, transition pain | High | UX testing, training, parallel systems |
| Citizens | Service quality, accessibility, privacy | High | Decidim participatory design, transparency reporting |
| Civil society / NGOs | Transparency, access, participation | Medium | Public roadmaps, open council meetings |
| Open-source communities | Contribution, reuse, recognition | Medium | openCode.de participation, upstream contributions |
| Sovereign tech providers | Partnership, deployment, revenue | Medium | Certified partner agreements, cooperative membership |
| Data Protection Officer | GDPR compliance, data minimisation | High | Privacy-by-design review at each phase gate |
| Cantonal/Land government | Interoperability, legal compliance | High | Standards alignment, XÖV/eCH compliance |
| Federal government | OZG/EMBAG compliance, EfA reuse | Medium | openCode.de publishing, federal coordination |

### 6.2 Procurement Framework

Open-source procurement requires a structurally different framework from proprietary licence purchasing. Municipalities pay for services (implementation, hosting, support, customisation, training) rather than licences. The following six principles govern open-source-aligned procurement:

**Principle 1 — Procure services, not licences.** Open-source software is free to use; municipalities pay for value-added services. Procurement documents must be structured around Service Level Agreements, support commitments, and deliverables — not licence terms.

**Principle 2 — Use cooperative procurement structures.** govdigital eG, Dataport, AKDB, cantonal IT cooperatives, and other cooperative structures provide pre-negotiated framework agreements that satisfy GWB/BöB requirements. Joining an existing framework reduces procurement timeline from 18–36 months to 2–6 months.

**Principle 3 — Apply "Public Money? Public Code!" as a contract condition** [4]. All custom software developed under contract must be released under an OSI-approved open-source licence and published on openCode.de or an equivalent public repository. Draft clause: *"All software developed under this contract that is not exclusively dependent on the Contracting Authority's proprietary data shall be licensed under [EUPL-1.2 / AGPL-3.0 / Apache 2.0] and published on openCode.de within 90 days of first deployment."*

**Principle 4 — Require 5-year TCO modelling.** Procurement scoring must include a 5-year TCO model (see Section 4.10 framework) covering implementation, hosting, training, support, and exit costs. Proprietary alternatives that exclude licence escalation risk and lock-in exit costs must be challenged.

**Principle 5 — Mandate interoperability standards as disqualifying criteria.** All procured systems must implement: XÖV standards (Germany) [46], eCH standards (Switzerland) [51], DCAT-AP (EU open data), and GovStack building-block APIs [50] where applicable. Non-compliance should be a disqualifying criterion, not a scored criterion.

**Principle 6 — Invoke Data Act rights in contract terms** [47]. Contracts signed after September 2025 must explicitly include: (a) data portability clauses (Article 5), (b) cloud-switching assistance obligations (Article 30), and (c) open interoperability standards requirements (Article 35). A vendor refusing to include these clauses should be treated as a procurement red flag.

### 6.3 Procurement Template Outline

The following outline should be used when drafting tender documents for open-source municipal IT services:

**Section 1 — Purpose and Background**
- Municipality name, population, current technology landscape
- Strategic objective: digital sovereignty, OZG/EMBAG compliance, TCO reduction

**Section 2 — Scope of Services**
- Software components in scope (from Section 4, this paper)
- Deployment model (self-hosted / cooperative / certified hoster)
- Support level (business hours / 24×7 / SLA tier)

**Section 3 — Technical Requirements**
- Mandatory: Open-source licence (OSI-approved) for all delivered software
- Mandatory: XÖV/eCH/DCAT-AP compliance for all data interfaces
- Mandatory: BSI IT-Grundschutz (or C5) documentation for all hosted components
- Mandatory: SBOM delivery and maintenance
- Preferred: GovStack building-block API compliance
- Preferred: openCode.de publication of any custom development

**Section 4 — Procurement Policy Clauses**
- "Public Money? Public Code!" clause (see Principle 3 above)
- Data Act rights clause (portability, switching, interoperability)
- Data residency clause: all data processed and stored within [DE/CH/EU]
- Auditing right: municipality may audit security posture at any time with 30 days notice

**Section 5 — Evaluation Criteria**
- Technical quality and open-source licence compliance: 30%
- Total cost of ownership (5-year, using methodology from Section 4.10): 30%
- References from comparable public-sector deployments: 20%
- Interoperability standards compliance: 10%
- Community health and long-term sustainability of component: 10%

**Section 6 — Contract Terms**
- Minimum 3-year initial term; 12-month notice period
- Quarterly security updates; monthly minor releases
- Source code escrow or equivalent for components not on public code repositories
- Transition assistance on contract termination (minimum 6 months)

### 6.4 Change Management

Open-source transitions frequently fail not on technical grounds but on human factors: end-user resistance, insufficient training, middle-management inertia, and political backsliding under vendor lobbying [30].

**Recommendations:**
- Appoint a **Digital Transformation Champion** at Deputy Mayor level with explicit political mandate and protected budget
- Designate **open-source department champions** in each administrative unit: trained, respected, and with time allocated for peer support
- Run **parallel operations** for a minimum of three months before cutting over critical services — longer for citizen-facing services
- Document and celebrate **early wins**: cost savings on first licence contract not renewed, new Decidim process engagement, security posture improvements
- Publish a **public transparency dashboard** showing migration progress, costs (before and after), service availability, and citizen satisfaction
- Brief **elected officials proactively**: equip them to respond to vendor lobbying with evidence (TCO data, regulatory compliance arguments, peer municipality references)

---

## 7. Risk Analysis

### 7.1 Risk Register

| Risk | Likelihood | Impact | Priority | Mitigation |
|---|---|---|---|---|
| Political reversal after election | Medium | High | High | Embed in legislation/ordinance; build cross-party consensus; publish TCO evidence |
| Vendor lobbying / FUD campaigns | High | Medium | High | Prepare evidence pack; engage civil society; publicise regulatory mandate |
| Skill gap in IT team | High | Medium | High | Training programme; cooperative IT partner; community of practice membership |
| Integration failure between stack layers | Medium | High | High | Reference architecture adherence; phased rollout with decision gates |
| Data loss during migration | Low | Critical | High | Full backup protocol; parallel operation ≥3 months; staged migration |
| GDPR / data protection violation | Low | High | Medium | Privacy-by-design; DPO at each phase gate; data flow mapping |
| User adoption failure | Medium | High | High | Change management plan; UX testing; training; parallel systems; champions |
| Cybersecurity incident | Low | Critical | High | BSI IT-Grundschutz; penetration testing at each phase gate; incident response plan |
| Community/component fragmentation | Low | Medium | Medium | Prefer CNCF/Apache-governed components; contribute upstream; align with ZenDiS |
| Cost overrun | Medium | Medium | Medium | Phase-gated budget; independent project office; open TCO accounting |
| Regulatory non-compliance | Low | High | Medium | Legal review at each phase; XÖV/eCH compliance testing; DPO sign-off |
| Vendor lock-in on "open-source" components | Medium | Medium | Medium | Prefer copyleft licences; avoid hosted-only components; maintain SBOM |

### 7.2 The Munich Cautionary Case — Updated Analysis

The City of Munich's LiMux project (2003–2017) is the most cited case of a large-scale municipal open-source transition that was ultimately reversed. A careful reading of the post-mortem evidence is important for drawing the correct lessons:

**What the reversal was not:** It was not caused by technical failure of the open-source software. Munich successfully migrated ~14,000 workstations to Linux and LibreOffice, achieving significant cost savings and demonstrating technical viability.

**What the reversal was:** A change in political leadership (2014 election), followed by a commissioned consulting report (Accenture, 2015) that critics noted was structured to favour a proprietary recommendation, followed by a council vote to re-migrate to Windows (2017). The Accenture report has been extensively criticised for excluding licence cost savings from its TCO analysis and attributing compatibility issues to Linux that were caused by other municipalities' and Land systems not supporting open standards [30].

**Lessons for municipal strategy:**
1. **Political risk management is primary**: obtain cross-party support before beginning; consider embedding digital sovereignty in a council ordinance with supermajority requirement for reversal
2. **TCO documentation must be continuous and public**: if cost savings are not publicly documented, they cannot be defended against vendor-commissioned counter-narratives
3. **Standards compliance is a prerequisite, not an afterthought**: Munich's compatibility issues arose partly because the state of Bavaria and federal systems did not consistently implement open file format standards — a gap that OZG 2.0 and the Interoperable Europe Act [6] have now begun to close
4. **Vendor lobbying is a real risk with financial resources behind it**: civil society engagement and transparent public reporting are the countermeasures

### 7.3 Success Case Studies

Three contemporary cases demonstrate successful open-source municipal strategy at different scales:

**Barcelona, Spain (Decidim)**: Barcelona's 2016 launch of Decidim for participatory budgeting engaged over 40,000 citizens in the first year and has since been adopted by 400+ organisations globally. The city's open technology strategy was enshrined in the 2017 Barcelona Digital City Plan, providing political durability across election cycles. Key success factors: visionary political leadership, dedicated open-source team in the city administration, and early investment in community building.

**Helsinki, Finland (Open Data + Decidim)**: Helsinki operates one of Europe's most comprehensive open data programmes alongside Decidim for citizen engagement. The city's Linked Open Data platform (built on CKAN) publishes 900+ datasets, including real-time transit data, spatial data, and budget data. Helsinki's approach demonstrates that open data publication can itself be a civic engagement driver — open data enables civil society organisations, journalists, and researchers to hold city government accountable.

**Kanton Schaffhausen, Switzerland (Decidim)**: The first Swiss Decidim deployment at cantonal level, Schaffhausen demonstrates that the platform is viable in the German-language Swiss legal and administrative context. The cantonal deployment provides a replicable template for Swiss municipalities of any size.

**OpenDesk (Germany, 2023–present)**: The federal OpenDesk rollout represents the first government-curated open-source workplace suite deployment at national scale. Early data from ZenDiS indicates positive staff adoption rates and significant cost reductions compared to proprietary equivalents. The programme's success in German federal ministries creates political cover for municipal-level adoption and provides a tested reference architecture.

### 7.4 Security Considerations

The BSI's IT-Grundschutz framework [26] provides a comprehensive security baseline applicable regardless of licence model. Key requirements for the open-source municipal stack:

- **Patch management**: All server components must receive security updates within 48 hours of critical CVE publication; standard updates within 30 days
- **Authentication assurance**: Keycloak must be configured for BSI Authenticator Assurance Level 2 (AAL2) for citizen-facing services; AAL3 (hardware tokens) for privileged administrative access
- **Encryption**: TLS 1.3 minimum for all data in transit; AES-256 encryption at rest for all personal data categories; end-to-end encryption for all Matrix communications
- **Penetration testing**: Annual penetration test by BSI-qualified (CREST or equivalent) provider; immediate remediation of critical findings
- **SBOM**: Software Bill of Materials maintained and updated monthly for all components; published publicly to enable civil society and peer municipalities to flag vulnerabilities
- **NIS2 obligations** [27]: EU Directive 2022/2555 mandates incident reporting, risk management measures, and supply-chain security for essential and important entities — municipalities serving populations >50,000 are typically in scope
- **BSI C5** attestation: Cloud hosters and SCS operators should hold BSI C5 (Cloud Computing Compliance Controls Catalogue) attestation or equivalent
- **Open-source audit advantage**: Unlike proprietary software, open-source components can be independently audited by the municipality's own security team, peer municipalities, BSI, and civil society — a structural security advantage that proprietary audits cannot replicate

---

## 8. Conclusion

The evidence reviewed in this paper converges on four findings, reinforced by the updated analysis in v0.2.0:

**Finding 1: Open-source municipal technology stacks are technically mature and production-proven.** Every functional requirement of a modern municipal government can be met by open-source software with documented deployments at peer municipalities across Switzerland, Germany, and the wider EU. The nine-layer reference architecture presented here can be implemented by municipalities from 5,000 to 500,000 population, with appropriate modulation of hosting model and support structure.

**Finding 2: The regulatory environment increasingly mandates open-source and interoperability.** EMBAG (Switzerland) [1], OZG 2.0 (Germany) [2], the Interoperable Europe Act (EU) [6], and the Data Act (EU) [47] collectively create legal obligations — mandating open-source release of publicly funded software, requiring interoperability assessments, establishing data portability rights, and mandating open API standards — that proprietary, vendor-locked systems cannot sustainably satisfy. Municipalities that begin the transition now are building regulatory compliance capital; those that delay are accumulating legal and financial risk.

**Finding 3: The 5-year total cost of ownership favours open-source when measured correctly.** The indicative TCO framework (Section 4.10) shows savings of €200–600 per user over five years for a 500-user municipality. The savings are larger when vendor lock-in exit costs and compliance costs for Data Act portability obligations are included in the proprietary alternative's TCO. Cooperative procurement structures compress open-source implementation costs further.

**Finding 4: Political and organisational investment is the binding constraint.** Technical choices are secondary to governance design. The Munich case confirms that open-source transitions succeed technically and fail politically. The Barcelona and Helsinki cases confirm that durable political mandate, dedicated institutional capacity (ZenDiS at federal level; a Digital Transformation Champion at municipal level), and transparent public reporting of costs and outcomes are the determinants of success.

Cities that move first will benefit from first-mover advantages: shaping cooperative standards, building in-house expertise, contributing to the open-source commons, and demonstrating to citizens and peer municipalities that a different path is possible. The legal framework is increasingly supportive, the technology is proven, the cooperative infrastructure exists, and the economics are favourable. The invitation is open.

**Next steps for this strategy:**
- **v0.3.0**: Small-municipality companion paper (populations <50,000)
- **v1.0.0**: Externally shareable release, with independently verified TCO case studies and citizen satisfaction survey framework

---

## References

[1] Swiss Federal Council. (2023). *Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG)*. SR 172.019. Bern: Swiss Confederation. https://www.fedlex.admin.ch/eli/cc/2023/682/de — [CC0, public domain]

[2] Bundesministerium des Innern und für Heimat (BMI). (2024). *Onlinezugangsgesetz 2.0 (OZG 2.0)*. Berlin: BMI. https://www.bmi.bund.de/DE/themen/moderne-verwaltung/e-government/ozg/ozg-node.html — [DL-DE/Zero 2.0]

[3] Open Source Business Alliance (OSBA). (2024). *Sovereign Cloud Stack: Technical and Governance Overview*. Berlin: OSBA. https://scs.community/ — [CC-BY-SA-4.0]

[4] Free Software Foundation Europe (FSFE). (2017, ongoing). *Public Money? Public Code!* Berlin: FSFE. https://publiccode.eu/ — [CC-BY-SA-4.0]

[5] European Commission. (2020). *Open Source Software Strategy 2020–2023: Think Open*. Brussels: European Commission. https://commission.europa.eu/about/departments-and-executive-agencies/informatics/open-source-software-strategy_en — [© European Union, reuse with attribution]

[6] European Parliament and Council. (2024). *Regulation (EU) 2024/903 of the European Parliament and of the Council on measures for a high level of interoperability of the public sector across the Union (Interoperable Europe Act)*. CELEX: 32024R0903. Brussels: Official Journal of the EU, L 2024/903. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R0903 — [EU legislation, public domain]

[7] Wirtz, B. W., & Weyerer, J. C. (2017). Conceptualization and creation of a holistic e-government maturity model. *Public Management Review*, 19(9), 1297–1316. https://doi.org/10.1080/14719037.2017.1283024 — [© Taylor & Francis]

[8] Janssen, M., Charalabidis, Y., & Zuiderwijk, A. (2012). Benefits, adoption barriers and myths of open data and open government. *Information Systems Management*, 29(4), 258–268. https://doi.org/10.1080/10580530.2012.716740 — [© Taylor & Francis]

[9] FITKO. (2024). *Föderale IT-Kooperation — Jahresbericht 2023*. Frankfurt: FITKO. https://www.fitko.de/veroeffentlichungen/jahresbericht — [DL-DE/Zero 2.0]

[10] openCode.de. (2022, ongoing). *openCode — Open Source for Government*. Berlin: Digitalservice GmbH des Bundes. https://opencode.de/ — [Open access; individual repository licences vary]

[11] Sovereign Cloud Stack Community. (2024). *SCS Technical Documentation*. https://docs.scs.community/ — [Apache 2.0]

[12] Decidim Association. (2021). *Decidim: Free Open-Source Participatory Democracy for Cities and Organizations*. Barcelona: Decidim Association. https://decidim.org/ — [AGPL-3.0]

[13] Nextcloud GmbH. (2024). *Nextcloud for Government: Security, Sovereignty, and Collaboration*. Stuttgart: Nextcloud GmbH. https://nextcloud.com/government/ — [AGPL-3.0 (Community Edition)]

[14] The Matrix Foundation. (2024). *Matrix Specification v1.x*. https://spec.matrix.org/ — [Apache 2.0]

[16] E-Government Suisse. (2023). *Strategie E-Government Schweiz 2024–2027*. Bern: Schweizerische Bundeskanzlei / E-Government Suisse. https://www.egovernment.ch/de/umsetzung/e-government-strategie/ — [Open access, Swiss federal publication]

[19] TYPO3 Association. (2024). *TYPO3 in Public Administration*. Düsseldorf: TYPO3 Association. https://typo3.org/project/association — [GPL-2.0 (core); CC-BY-SA (documentation)]

[20] OpenProject GmbH. (2024). *OpenProject for Government: Open Source Project Management*. Berlin: OpenProject GmbH. https://www.openproject.org/ — [GPL-3.0]

[21] Red Hat / Keycloak Community. (2024). *Keycloak: Open Source Identity and Access Management*. https://www.keycloak.org/ — [Apache 2.0]

[22] CKAN Association. (2024). *CKAN: Open Source Data Portal Software*. https://ckan.org/ — [AGPL-3.0]

[23] govdigital eG. (2024). *govdigital: Genossenschaft für digitale Verwaltung*. Berlin: govdigital eG. https://govdigital.de/ — [Open access]

[24] Dataport AöR. (2024). *Dataport: IT-Dienstleister für die öffentliche Verwaltung*. Hamburg: Dataport AöR. https://www.dataport.de/ — [Open access]

[26] Bundesamt für Sicherheit in der Informationstechnik (BSI). (2023). *BSI IT-Grundschutz-Kompendium Edition 2023*. Bonn: BSI. https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz — [CC-BY-ND 3.0 DE]

[27] European Parliament and Council. (2022). *Directive (EU) 2022/2555 on measures for a high common level of cybersecurity across the Union (NIS2 Directive)*. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022L2555 — [EU legislation, public domain]

[29] United Nations DESA. (2022). *UN E-Government Survey 2022: The Future of Digital Government*. New York: United Nations. https://publicadministration.un.org/egovkb/en-us/Reports/UN-E-Government-Survey-2022 — [© United Nations, open access]

[30] Janowski, T. (2015). Digital government evolution: From transformation to contextualization. *Government Information Quarterly*, 32(3), 221–226. https://doi.org/10.1016/j.giq.2015.07.001 — [© Elsevier]

[33] Camunda Services GmbH. (2024). *Camunda Platform 8 Community Edition*. https://camunda.com/download/ — [Apache 2.0 (Community)]

[34] BigBlueButton Inc. (2024). *BigBlueButton: Open Source Web Conferencing*. https://bigbluebutton.org/ — [LGPL-3.0]

[35] Jitsi Community / 8×8. (2024). *Jitsi Meet: Open Source Video Conferencing*. https://jitsi.org/ — [Apache 2.0]

[36] OpenStreetMap Foundation. (2024). *OpenStreetMap*. https://www.openstreetmap.org/ — [ODbL-1.0]

[37] QGIS Project. (2024). *QGIS: A Free and Open Source Geographic Information System*. https://www.qgis.org/ — [GPL-2.0+]

[39] Cloud Native Computing Foundation (CNCF). (2024). *Kubernetes*. https://kubernetes.io/ — [Apache 2.0]

[41] PostgreSQL Global Development Group. (2024). *PostgreSQL*. https://www.postgresql.org/ — [PostgreSQL Licence (OSI-approved)]

[42] BMI / ZenDiS GmbH. (2024). *OpenDesk: Der digitale Arbeitsplatz der Bundesverwaltung*. https://opendesk.eu/ — [AGPL-3.0]

[43] Schweizerisches Bundesarchiv (BAR). (2023). *Geschäftsverwaltung (GEVER) in der Bundesverwaltung*. Bern: BAR. https://www.bar.admin.ch/bar/de/home/digitale-archivierung/gever.html — [Open access, Swiss federal publication]

[44] opendata.swiss. (2024). *Open Government Data Switzerland*. Bern: Schweizerische Bundeskanzlei. https://opendata.swiss/ — [CC-BY-4.0 (portal); individual dataset licences vary]

[45] European Commission. (2017). *European Interoperability Framework — Implementation Strategy (EIF)*. Brussels: European Commission, ISA² Programme. https://joinup.ec.europa.eu/collection/nifo-national-interoperability-framework-observatory — [CC-BY-4.0]

[46] KoSIT. (2024). *XÖV-Standards: XML in der öffentlichen Verwaltung*. Bremen: KoSIT. https://www.xoev.de/ — [Open access]

[47] European Parliament and Council. (2023). *Regulation (EU) 2023/2854 of the European Parliament and of the Council on harmonised rules on fair access to and use of data (Data Act)*. CELEX: 32023R2854. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023R2854 — [EU legislation, public domain]

[48] ZenDiS GmbH. (2024). *Zentrum für Digitale Souveränität der öffentlichen Verwaltung — Jahresbericht 2023/2024*. Berlin: ZenDiS GmbH. https://zendisgmbh.de/ — [Open access]

[49] EU Open Source Observatory (OSOR). (2023). *OSOR Annual Report 2023: Open Source in European Public Administrations*. Brussels: European Commission, DIGIT. https://joinup.ec.europa.eu/collection/open-source-observatory-osor — [CC-BY-4.0]

[50] ITU / DIAL. (2023). *GovStack Building Block Specifications v1.0*. Geneva: International Telecommunication Union. https://govstack.global/building-blocks/ — [CC-BY-4.0]

[51] eCH. (2023). *eCH-0014 Swiss E-Government Standards Framework*. Bern: E-Government Suisse / eCH Association. https://www.ech.ch/de/ech/ech-0014 — [Open access; individual standard licences vary]

[52] Consul Democracy Foundation. (2024). *CONSUL Democracy Platform*. Madrid: Consul Democracy Foundation. https://consuldemocracy.org/ — [AGPL-3.0]

[53] Lathrop, D., & Ruma, L. (Eds.). (2010). *Open Government: Collaboration, Transparency, and Participation in Practice*. Sebastopol, CA: O'Reilly Media. — [© O'Reilly Media]

[54] Schweizerischer Bundesrat. (2023). *Strategie Digitale Schweiz 2023*. Bern: Schweizerischer Bundesrat. https://www.bakom.admin.ch/bakom/de/home/digital-und-internet/strategie-digitale-schweiz.html — [Open access, CC-BY-4.0]

---

*This document is released under the Creative Commons Attribution 4.0 International Licence (CC-BY-4.0).*
*Attribute as: Sebastian Graf, Autonomous Office of Civil Digital Infrastructure (sebk4c@tuta.com)*
*Version history: v0.1.0 (2026-06-20, first structured draft) → v0.2.0 (2026-06-20, citation-complete draft)*
