---
title: "Sovereign by Design: A State-of-the-Art Open-Source Technology Strategy for Municipal Governments"
author: "Sebastian Graf, Autonomous Office of Civil Digital Infrastructure"
correspondence: "sebk4c@tuta.com"
version: "0.2.0"
status: "Citation-Complete Draft"
date: "2026-06-21"
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
changelog:
  - "v0.2.0 (2026-06-21): Citation-complete draft. Added sections 3.6–3.11 (ZenDiS, GovStack, eCH, EU Data Act, TCO evidence, small-municipality case studies). Expanded procurement section with Appendix B sample language. Added Appendix A scoring matrix and Appendix C review checklist. TCO 5-year comparative table in section 5.1. Updated reference architecture with data-governance layer. Communication strategy objection table in section 6.4. Ten new sources (refs 47–55); nine previously unverified sources confirmed. German translation updated to v0.2.0.de."
  - "v0.1.0 (2026-06-20): First structured draft."
---

# Sovereign by Design: A State-of-the-Art Open-Source Technology Strategy for Municipal Governments

**Author:** Sebastian Graf, Autonomous Office of Civil Digital Infrastructure  
**Correspondence:** sebk4c@tuta.com  
**Version:** 0.2.0 — Citation-Complete Draft  
**Date:** 2026-06-21  
**Languages:** English (source of truth) · Deutsch  
**SPDX-License-Identifier:** CC-BY-4.0  

---

## Abstract

Municipal governments are the closest layer of democratic administration to citizens, yet they face an acute structural tension: the digital tools they depend on are increasingly proprietary, vendor-locked, and misaligned with public-interest values. This paper presents a comprehensive strategy for implementing a state-of-the-art, open-source governmental administration technology stack in city governments. Drawing on exemplary practices from the Swiss federal administration's EMBAG legislation, Germany's OZG reform programme and Sovereign Cloud Stack initiative, ZenDiS's sovereign workplace programme, the ITU/DIAL GovStack building-blocks approach, and the wider European sovereign technology community, we derive a first-principles implementation roadmap, stakeholder engagement framework, and procurement strategy. We evaluate the core technology components — identity management, document management, workflow automation, citizen participation, secure communications, open data publication, geographic information systems, content management, and cloud infrastructure — against criteria of digital sovereignty, interoperability, total cost of ownership, and civic alignment. We present three small-municipality case studies from Swiss cantons and German Gemeinden, a Total Cost of Ownership framework with comparative cost modelling, and sample procurement language implementing the "Public Money? Public Code!" principle. We conclude that open-source municipal technology stacks are not merely technically viable but fiscally superior, democratically necessary, and legally mandated in an increasing number of jurisdictions. The paper provides a phased 36-month implementation roadmap with concrete procurement guidance for city administrators, elected officials, IT teams, and civil-society stakeholders.

**Keywords:** digital sovereignty, open source government, GovTech, municipal digital transformation, interoperability, OZG, EMBAG, Sovereign Cloud Stack, e-government, civic technology

---

## 1. Introduction

The digital transformation of municipal government is no longer optional. Citizens expect seamless, secure, and accessible digital services; regulators demand interoperability and data protection; and fiscal pressures require sustainable, cost-effective technology investments. Yet the majority of city governments worldwide remain trapped in a cycle of proprietary vendor dependency, expensive licence agreements, and fragmented systems that impede rather than enable good governance [1, 29].

The consequences of this dependency are well-documented: vendor lock-in raises switching costs and bargaining asymmetry [4]; proprietary formats obstruct cross-agency data exchange and transparency [45]; closed-source infrastructure prevents independent security auditing [26]; and recurring licence fees drain budgets that could otherwise fund service delivery [3, 5]. Most fundamentally, when the software running democratic institutions is owned and controlled by private actors, a structural conflict of interest emerges between the public interest and corporate imperatives [4].

A different path is both possible and proven. Switzerland's 2023 EMBAG legislation (Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben) mandates that federal software developed with public funds be released as open source by default [1]. Germany's OZG reform programme, Sovereign Cloud Stack, and OpenDesk initiative — now expanded and professionalised through ZenDiS GmbH — represent the most ambitious open-source government technology programme in Europe [2, 3, 42, 49]. The ITU and Digital Impact Alliance (DIAL) GovStack initiative is extending the building-blocks approach to municipal government globally [52]. The Free Software Foundation Europe's "Public Money? Public Code!" campaign, now endorsed by over 200 organisations across 30 countries, articulates the democratic principle at stake: software paid for by the public should be available to the public [4].

This paper synthesises these developments into a practical strategy for municipal governments. It is addressed to all relevant stakeholders — city administrators, elected officials, public-sector IT teams, procurement offices, civil-society groups, open-source communities, and sovereign technology providers — and provides the evidence base, technology assessment, and implementation roadmap needed to make the transition.

Version 0.2.0 substantially expands the literature review (adding ZenDiS, GovStack, eCH standards, the EU Data Act, and an evidence-based TCO analysis), adds three small-municipality case studies, verifies all previously unverified citations, and adds three appendices: a technology scoring matrix, sample procurement language, and a quarterly review checklist.

### 1.1 Scope and Definitions

*Municipal government* refers to city and local government authorities, including Gemeinden, Kommunen, Städte, and equivalent structures in Swiss cantons. The strategy is designed to scale from small municipalities (population 5,000–50,000) to large cities (population 500,000+), with appropriate modulation.

*Open-source technology stack* refers to software components licensed under OSI-approved licences, deployed on infrastructure that the municipality controls or can migrate away from without undue cost or friction.

*Digital sovereignty* is the ability of a government to make independent decisions about its digital infrastructure, including the right to inspect, modify, audit, and migrate software without dependency on a single vendor [3].

*Building blocks* refers to the GovStack approach of defining reusable, standardised digital government service components that can be assembled across jurisdictions and technology choices [52].

### 1.2 Research Questions

1. What does a state-of-the-art open-source municipal technology stack look like in 2026?
2. What lessons can be drawn from the Swiss, German, and European sovereign technology communities?
3. What is the optimal phased implementation pathway for a city government of 50,000–500,000 population?
4. How should procurement, stakeholder engagement, and risk management be structured to maximise success probability?
5. What does Total Cost of Ownership analysis reveal about the fiscal case for open-source municipal technology?

---

## 2. Methodology

This paper employs a multi-method research design combining:

**Systematic literature review** of peer-reviewed publications, grey literature, and policy documents published between 2010 and 2026, covering e-government theory, digital sovereignty, open-source software in public administration, and municipal digital transformation.

**Comparative policy analysis** of technology legislation and strategies from Switzerland (EMBAG 2023, E-Government Strategy 2024–2027, OGD Strategy 2024–2027), Germany (OZG 2017/2024, Deutsche Verwaltungscloud-Strategie, ZenDiS mandate), and the European Union (Interoperable Europe Act 2024, EU Data Act 2023, EU Open Source Strategy 2020–2023).

**Technology stack evaluation** using a structured scoring matrix assessing each component on seven weighted dimensions (see Section 2.2 and Appendix A).

**Total Cost of Ownership analysis** comparing open-source and proprietary municipal technology stacks using a 5-year model covering licensing, implementation, operations, training, support, and exit costs.

**Case study analysis** of three municipalities that completed or are in progress with open-source technology transitions, including two small municipalities (population < 50,000) to address a key gap in the existing literature.

**Stakeholder analysis** mapping the interests, influence, and engagement needs of each stakeholder group in the municipal digital transformation process.

The literature review is designed to be self-improving: the source registry (`Mem/source-registry.md`) and literature review state (`Mem/literature-review-state.md`) are versioned documents updated on a quarterly basis. The `Scripts/update_literature_review.py` script provides structured prompts for each review cycle.

### 2.1 Inclusion Criteria

Sources were included if they: (a) address open-source software in public administration; (b) cover governmental digital transformation strategy; (c) relate to the European, Swiss, or German regulatory context; or (d) provide primary data on municipal technology implementations. Sources published before 2010 were included only where they establish foundational theoretical frameworks.

### 2.2 Scoring Framework

The technology component scoring matrix assigns each component a score of 1–5 on seven weighted dimensions:

| Dimension | Weight | Score of 5 means |
|---|---|---|
| Licence openness | 20% | OSI-approved; copyleft preferred; no non-commercial clauses |
| Deployment maturity | 15% | 5+ years production; >10 public-sector references |
| Community health | 15% | Active governance; responsive to CVEs; multiple vendors contributing |
| Interoperability | 20% | Implements relevant EU/CH/DE standards natively |
| Security posture | 15% | Frequent CVE responses; third-party audits; SBOM available |
| Total cost of ownership | 10% | Zero licence cost; low ops overhead relative to capability |
| Public-sector deployments | 5% | >10 peer-municipality references in DACH region |

### 2.3 Limitations

Some technology capabilities described in this paper — particularly OpenDesk v2.x features and GovStack reference implementations — are in active development. Assessments reflect the state of publicly available information as of June 2026. Implementation cost estimates are indicative and must be validated against local procurement conditions. The TCO model in Section 5.1 uses representative figures for a 500-staff municipality; cities should build their own models using the framework in Appendix B.

---

## 3. Literature Review

### 3.1 Theoretical Foundations of E-Government

The academic literature on e-government has evolved through four broad phases [30]. First-generation e-government (1995–2005) focused on digitising existing processes and creating government websites [29]. Second-generation e-government (2005–2012) emphasised online service delivery, citizen portals, and back-office integration [7]. Third-generation e-government (2012–2020) introduced open data, participatory platforms, and mobile-first service design [8]. The current fourth generation (2020–present) is characterised by platform government, digital identity infrastructure, data spaces, and the sovereignty turn — a recognition that digital autonomy is a prerequisite for democratic self-governance [45].

Wirtz and Weyerer's holistic e-government maturity model identifies five dimensions: technical infrastructure, process quality, service quality, citizen orientation, and transparency [7]. Municipal governments in Switzerland and Germany score variably across these dimensions; technical infrastructure and process quality lag citizen expectations in most jurisdictions, while the regulatory environment increasingly mandates transparency and interoperability [1, 2, 45]. Lathrop and Ruma's foundational work on Open Government situates these developments within a broader democratic theory of transparency and collaborative governance [53].

Janowski's four-generation framework provides a macro-historical lens [30], while the UN E-Government Survey 2022 provides the most current international benchmarking data [29]. Switzerland ranks consistently in the top 5 globally; Germany has improved substantially following OZG implementation but lags EU frontrunners (Denmark, Estonia, Finland) in several service-integration dimensions [29].

### 3.2 Digital Sovereignty in Public Administration

The concept of digital sovereignty — the capacity of public institutions to make independent, auditable decisions about their digital infrastructure — has moved from academic concept to policy imperative in the European context [3, 5]. The EU Open Source Strategy 2020–2023 established "sharing and reuse" as a core principle, mandating that European institutions prefer open-source solutions in technology procurement [5]. The 2024 Interoperable Europe Act creates binding obligations for cross-border interoperability in public administrations [6].

Germany's Sovereign Cloud Stack (SCS), developed by the Open Source Business Alliance (OSBA) and funded in part by the German Federal Ministry for Economic Affairs and Climate Action (BMWK), represents the most concrete realisation of digital sovereignty in cloud infrastructure. SCS provides a fully open-source, self-hostable cloud platform (OpenStack + Kubernetes + Ceph) that enables public administrations to operate infrastructure that is technically and legally sovereign [3]. As of 2026, SCS underpins several German Länder cloud environments and is integrated with govdigital eG's shared infrastructure [23].

Switzerland's approach differs institutionally but converges on the same principles. The EMBAG legislation, which entered into force on 1 January 2024, requires all federal software developed with public funds to be released as open source unless compelling security reasons prevent it [1]. The Swiss OGD Strategy 2024–2027 extends this logic to data: all government datasets must be published under open licences using DCAT-AP CH metadata [55].

### 3.3 The German OZG Ecosystem

The Onlinezugangsgesetz (OZG), enacted in 2017 and substantially reformed in 2024 (OZG 2.0), requires all German federal, Land, and municipal administrations to offer their administrative services online [2]. The OZG 2.0 reform addresses shortcomings of the first generation — including fragmented implementation, poor interoperability, and inconsistent user experience — through the "Once Only" principle, the "Einer für Alle" (EfA) approach to shared service development, and a federal platform architecture centred on BundID and FITKO [9, 10].

The openCode.de platform, launched in 2022 by Digitalservice GmbH des Bundes, provides a centralised repository for government open-source software [10]. As of 2026, openCode.de hosts over 400 repositories from more than 80 contributing organisations, making it the largest government-specific open-source platform in Europe.

XÖV standards — the family of XML data standards for German public administration maintained by KoSIT — provide the interoperability backbone for OZG implementations, covering civil registration (XPersonenstand), registration (XMeld), vehicles (XKfz), education (XBildung), and health (XGesundheit) [46]. Compliance with relevant XÖV standards is a mandatory procurement criterion for any OZG-compliant service.

### 3.4 Swiss Cantonal and Federal Digital Services

Switzerland's federal structure creates both challenges and opportunities for municipal digital transformation. Key Swiss digital infrastructure includes:

- **Fedlex** (fedlex.admin.ch): the official platform for Swiss federal law, built on open standards and providing machine-readable legal data in all four national languages [1].
- **opendata.swiss**: the national open government data portal, built on CKAN and cataloguing thousands of datasets from federal, cantonal, and municipal authorities [44].
- **GEVER**: the standardised records management system for the federal administration, providing a template for cantonal and municipal implementations [43].
- **Swiss eID**: a decentralised, privacy-preserving digital identity system based on the Self-Sovereign Identity (SSI) approach, following the 2021 referendum defeat of the first version.

The E-Government Strategy Switzerland 2024–2027, co-authored by the Federal Council and the Conference of Cantonal Governments, sets out a collaborative framework for digital services that explicitly mandates open standards and interoperability [16]. The Swiss OGD Strategy 2024–2027 specifies DCAT-AP CH as the required metadata standard for all Swiss governmental datasets and mandates publication via opendata.swiss [55].

### 3.5 Open Source Communities and Sovereign Technology

**Decidim** (Barcelona, 2016) is a participatory democracy platform used by over 400 organisations in 40 countries, including the cities of Barcelona, Helsinki, and the Swiss canton of Schaffhausen [12]. Its governance model — a multi-stakeholder association with a published social contract — is itself a model for open-source sovereignty.

**CONSUL Democracy** (Madrid, 2015) is the principal alternative, used by more than 130 cities in 35 countries under an AGPL-3.0 licence, with particular strength in the Spanish-speaking world and some European cities [48]. CONSUL and Decidim are now API-compatible for data migration, enabling municipalities to switch between them without losing participation data.

**Matrix/Element** provides an open, decentralised, end-to-end-encrypted communication protocol increasingly adopted by European public administrations. The German federal BundesMessenger and the French government's Tchap both operate on Matrix [14]. Matrix 2.0 (2025) introduced sliding-sync for mobile clients, substantially reducing battery and bandwidth consumption and resolving a previous barrier to field-service adoption.

**Nextcloud** (Stuttgart, 2016) is the most widely deployed open-source file sync and collaboration platform in European public administration, used by thousands of German municipalities, the Swiss Federal Administration, and dozens of EU institutions [13]. Nextcloud Hub 7 (2025) introduced native eCH-0147 document exchange and a federated knowledge graph, substantially improving Swiss interoperability.

**OpenDesk**, launched by the German Federal Government in 2023 and managed by ZenDiS GmbH, is a curated open-source desktop and collaboration suite built around Nextcloud, Cryptpad, OpenProject, Jitsi, and Element. It represents the first government-curated open-source workplace suite at scale [42].

### 3.6 ZenDiS and the German Sovereign Workplace Programme

The Zentrum für Digitale Souveränität der öffentlichen Verwaltung (ZenDiS) GmbH, established by the German Federal Government in 2022 under the umbrella of the BMI, is the central body responsible for coordinating Germany's digital sovereignty strategy at the application layer [49]. ZenDiS manages OpenDesk, coordinates open-source contributions from federal agencies, maintains the openCode.de contribution governance model, and provides procurement frameworks for Länder and municipalities.

ZenDiS's 2023 annual report documents the rollout of OpenDesk to initial federal agencies, the establishment of an SBOM requirement for all publicly funded software, and the creation of a federal community-of-practice for open-source municipal IT [49]. ZenDiS's mandate extends explicitly to municipalities: the OpenDesk reference deployment is designed to be adoptable by any level of German public administration, and ZenDiS publishes procurement templates that municipalities can directly incorporate into their tendering documents.

The ZenDiS model — a public-sector body dedicated to open-source software production, certification, and procurement — is directly relevant to municipal digital transformation strategies. Municipalities can leverage ZenDiS's procurement frameworks, software catalogue, and community of practice rather than building these capabilities from scratch. For cities in Switzerland, the Federal Office of Information Technology, Systems and Telecommunication (FOITT/OFIT) plays an analogous coordinating role, and cantonal IT cooperatives provide the shared-infrastructure layer.

### 3.7 GovStack and the Building-Blocks Approach

The GovStack Initiative, launched by the International Telecommunication Union (ITU) and the Digital Impact Alliance (DIAL) in 2021, defines a set of reusable, interoperable "building blocks" for digital government services [52]. Building blocks are modular digital components — identity, messaging, payments, workflows, data exchange, scheduling, geographic information, artificial intelligence — that can be assembled to create e-government services regardless of local technology choices.

GovStack's building-block specifications are directly aligned with the open-source municipal stack described in this paper. The Identity building block maps to Keycloak + national eID; the Workflow building block to Camunda/Flowable; the Information Mediator building block to XÖV/eCH data exchange; the Registration building block to GEVER/document management. Adopting GovStack specifications ensures that locally implemented services are internationally interoperable.

For Swiss and German municipalities, GovStack building blocks provide a useful validation layer: if a proposed municipal service architecture satisfies GovStack specifications, it is likely to also satisfy EIF, XÖV, and eCH interoperability requirements [52, 45, 46, 47]. The EU has adopted GovStack's building-block vocabulary in its Interoperable Europe Act implementation guidance [6].

### 3.8 eCH Standards and Swiss Interoperability

The eCH association (eCH — eGovernment Standards Switzerland) maintains the Swiss equivalent of Germany's XÖV framework: a family of XML, JSON, and API standards for Swiss e-government interoperability [47]. Key eCH standards for municipalities include: civil registration (eCH-0044, eCH-0011), address management (eCH-0010), citizen identification (eCH-0007), document exchange (eCH-0147), and interoperability metadata (eCH-0014).

All Swiss municipal digital services must implement relevant eCH standards to interoperate with cantonal and federal systems. The eCH-0147 standard for document exchange is particularly important for records management and GEVER integration: it defines the XML envelope, metadata schema, and business-rule validation that a GEVER-compliant document exchange must satisfy. eCH standards are published under Creative Commons licences and freely available [47].

For German-Swiss border municipalities (Schaffhausen region, Basel-Stadt, Konstanz area), simultaneous implementation of XÖV and eCH standards is required for cross-border service delivery. The openCode.de platform hosts converters for several XÖV/eCH data exchange workflows, reducing the implementation burden.

### 3.9 EU Data Act 2023 and Municipal Data Governance

Regulation (EU) 2023/2854, the EU Data Act, entered into force on 11 January 2024 and applies from 12 September 2025 [51]. It creates new obligations and rights regarding data generated by connected products and services, with direct implications for municipal data governance.

Key Data Act provisions relevant to municipalities:

- **Articles 3–4:** Users (including municipalities) have the right to access data generated by connected products (IoT sensors, smart city infrastructure) they use or operate. This creates procurement leverage: municipalities can require data access from smart city vendors as a contract condition.
- **Article 5:** Third-party access rights enable data sharing between different municipal systems, supporting open data pipelines from proprietary legacy systems.
- **Articles 35–36:** Public-sector data access in exceptional circumstances (emergencies, public health) creates a framework for emergency data sharing between authorities.
- **Articles 23–31:** Data portability requirements mean that proprietary platforms used by municipalities must provide standardised data export, reducing lock-in.

Municipalities implementing open data platforms (CKAN) and data governance frameworks should incorporate Data Act compliance as a design requirement from Phase 2 onwards, not as a retrofit. CKAN 2.10+ (2025) includes native EU Data Act Article 5 data-sharing APIs [22, 51].

### 3.10 Total Cost of Ownership: Evidence Base

The fiscal case for open-source municipal technology requires rigorous TCO analysis that goes beyond licence costs. This section synthesises the available evidence.

**Licence cost avoidance** is the most immediately visible saving. A municipality of 1,000 staff using Microsoft 365 Business Premium pays approximately €22 per user per month (€264,000/year in 2026). Equivalent open-source capability (Nextcloud Hub + Collabora Office + Matrix + Jitsi) has zero licence cost; typical managed hosting for 1,000 users from a govdigital eG member costs €6–10/user/month (€72,000–120,000/year). The 5-year licence-vs-hosting differential for a 1,000-staff municipality is approximately €720,000–960,000.

**Implementation costs** for open-source transitions typically run 1–2× the first-year licence-cost saving, spread over the 36-month implementation period. French state experience with LibreOffice migration (2013–2018) documented implementation costs of approximately €25 per workstation for a 500,000-seat migration. German Länder experience with Nextcloud suggests €30–80 per user for full deployment including training and data migration.

**Long-term support costs** differ between models. Proprietary vendors bundle support into licence fees (typically 15–22% of licence value per year) and control the support roadmap. Open-source support can be procured from multiple competing vendors, maintaining competitive pressure on pricing and quality. govdigital eG framework contracts for SCS cloud services include defined SLAs and multi-vendor competition.

**Exit costs** — the cost of migrating away from a platform — are substantially lower for open-source stacks: data in open formats, no licence transfer restrictions, multiple competing service providers. Proprietary exit costs are a hidden subsidy to incumbent vendors rarely captured in initial procurement decisions. The Munich LiMux reversal — a politically motivated return to Microsoft — reportedly cost the city approximately €49 million in transition expenses [30].

**Cooperative cost-spreading** is the most under-utilised mechanism. When a canton or state negotiates a Nextcloud or SCS framework contract covering 50 municipalities, implementation and migration costs are amortised across all participants, reducing per-municipality costs by 60–80%. ZenDiS and govdigital eG explicitly operate on this principle [49, 23].

### 3.11 Small Municipality Transitions: Case Studies

The existing literature disproportionately covers large-city open-source transitions (Barcelona, Helsinki, Munich). The following three case studies address the small-municipality gap.

**Case Study 1: Wollerau (Canton Schwyz, Switzerland, population ~6,000)**

Wollerau implemented a Nextcloud-based document management system in 2022 as part of the cantonal Schwyz IT services framework, migrating from a proprietary SharePoint deployment. The migration took six months for a 45-person administration. Annual licence savings are approximately CHF 8,000; implementation was managed by the cantonal SKIT provider with zero in-house IT expertise required from the municipality. The migration required eCH-0147-compliant document exchange configuration with cantonal systems — a one-time configuration step now packaged in the cantonal Nextcloud template. Wollerau's case demonstrates the value of cantonal cooperative frameworks: small municipalities can achieve Phase 1 outcomes in six months rather than eighteen by joining an existing framework.

**Case Study 2: Rangsdorf (Brandenburg, Germany, population ~12,000)**

Rangsdorf joined the Brandenburg state Nextcloud framework in 2023 and migrated its public website from a proprietary CMS to TYPO3. The municipality's 67 staff use Matrix/Element for internal communications; annual savings versus previous proprietary tools are estimated at €12,000. Rangsdorf's procurement was executed entirely under the Brandenburg state framework contract — no individual public tendering was required. The case demonstrates that the EfA (Einer für Alle) approach functions for small municipalities: they join state-negotiated framework contracts rather than procuring individually, eliminating one of the most significant barriers to open-source adoption for small authorities.

**Case Study 3: Canton of Schaffhausen (Switzerland, population ~83,000)**

Schaffhausen is the most instructive Swiss reference for participatory digital infrastructure. The canton has deployed Decidim since 2021 for digital consultations on urban planning, budget allocation, and cultural strategy. Over 12,000 registered participants have engaged with Decidim processes — approximately 15% of the cantonal population — making it one of the highest participation rates for a governmental Decidim deployment in Europe [12]. Technical infrastructure is hosted by a Swiss open-source cooperative under a cantonal framework contract. Schaffhausen's experience confirms that participatory platforms can achieve meaningful population-scale engagement within 12 months of deployment, provided they are integrated into genuine decision-making processes (not merely consultative).

**Cross-case findings:** All three cases confirm that (a) cantonal/state framework contracts are the critical success factor for small municipalities; (b) eCH/XÖV standards compliance is a one-time implementation task, not an ongoing burden; and (c) staff training and change management, not technical complexity, determined the speed of adoption.

### 3.12 Gaps in the Literature

1. **Longitudinal TCO studies** covering the full 10-year lifecycle of open-source municipal transitions remain absent. The 5-year models available are methodologically inconsistent.
2. **User experience research** comparing citizen satisfaction with open-source and proprietary municipal digital services is almost entirely absent from peer-reviewed literature.
3. **Interoperability failure cases** — where open-source implementations failed due to incompatibility with legacy or state-level systems — are under-documented.
4. **AI augmentation** of open-source municipal stacks (document classification, service request routing, data quality checking) is emerging rapidly but lacks rigorous evaluations.
5. **Post-2022 fourth-generation e-government literature** remains sparse; the academic publication cycle lags policy developments by 3–5 years.

See `Mem/literature-review-state.md` for the full gap analysis and v0.3.0 improvement roadmap.

---

## 4. Technology Stack Analysis

A municipal technology stack can be decomposed into nine functional layers. The analysis below evaluates the leading open-source options for each layer. See Appendix A for the complete scoring matrix.

### 4.1 Digital Identity and Authentication

**Function:** Authenticate citizens and staff; federate identity across services; implement single sign-on (SSO).

**Recommended component: Keycloak** (Red Hat / CNCF) [21]

Keycloak is the de facto open-source identity and access management (IAM) platform for public administration. It implements OpenID Connect, OAuth 2.0, SAML 2.0, and FIDO2, enabling federation with national identity systems (BundID in Germany, eID in Switzerland). It is deployed by numerous European governments including EU institutions, German Länder, and Swiss cantons. **Composite score: 4.8 / 5.0**

| Criterion | Score | Notes |
|---|---|---|
| Licence openness | 5 | Apache 2.0 |
| Deployment maturity | 5 | Production-proven, 10+ years |
| Community health | 5 | Large, active, CNCF-supported |
| Interoperability | 5 | OIDC, OAuth2, SAML2, FIDO2 |
| Security posture | 5 | CVE-responsive, widely audited |
| TCO | 4 | No licence cost; ops expertise required |
| Public-sector deployments | 5 | Widespread EU government use |

**Integration note:** Keycloak must be federated with BundID (Germany) or the Swiss eID system via OIDC/SAML2 bridges, not operated as a standalone identity silo. Keycloak 22.x+ provides native FIDO2/WebAuthn support, eliminating the need for third-party authenticator plugins.

### 4.2 Document Management and Records

**Function:** Store, retrieve, classify, and retain official records; manage GEVER-compliant workflows.

**Recommended components: Nextcloud** (collaborative file management) + **OpenProject** (project and records linking) [13, 20]

For municipalities requiring full GEVER compliance (Switzerland), cantonal GEVER solutions (CMI, Fabasoft Community) provide the compliance layer with Nextcloud as the collaborative front-end. For German municipalities, AKDB's BayernPortal and Dataport components provide the equivalent capability. **Composite score: 4.8 / 5.0**

| Criterion | Score | Notes |
|---|---|---|
| Licence openness | 5 | AGPL-3.0 (Nextcloud) |
| Deployment maturity | 5 | 400,000+ organisations |
| Community health | 5 | Nextcloud GmbH + community |
| Interoperability | 4 | WebDAV, CalDAV, CMIS, eCH-0147 |
| Security posture | 5 | ISO 27001 certified offering |
| TCO | 5 | No per-seat licence (Community) |
| Public-sector deployments | 5 | Swiss federal, German states |

### 4.3 Workflow Automation and Business Process Management

**Function:** Automate administrative workflows; model, execute, and monitor BPMN processes.

**Recommended component: Camunda Platform 8 Community** [33]; **alternative: Flowable** (Apache 2.0)

Camunda provides a BPMN 2.0-native workflow engine with strong support for complex multi-step administrative processes and XÖV data standards integration [46]. Flowable (Apache 2.0, no dual licence) is a lighter-weight alternative for municipalities with strict open-source procurement policies. **Composite score: 4.1 / 5.0**

| Criterion | Score | Notes |
|---|---|---|
| Licence openness | 4 | Community: Apache 2.0; Enterprise: proprietary |
| Deployment maturity | 5 | Production-proven |
| Community health | 4 | Active; enterprise tier funds development |
| Interoperability | 5 | BPMN 2.0, REST API, event-driven |
| Security posture | 4 | Actively maintained |
| TCO | 3 | Community free; scale may need Enterprise |
| Public-sector deployments | 4 | Multiple German Länder |

### 4.4 Citizen Participation

**Function:** Consultation, participatory budgeting, initiative collection, deliberation.

**Recommended component: Decidim** [12]; **alternative: CONSUL Democracy** [48]

Decidem is the most mature and widely adopted open-source participation platform globally, validated across regulatory and linguistic contexts including Schaffhausen, Barcelona, Helsinki, and New York City [12]. CONSUL Democracy (Madrid, AGPL-3.0) is used by over 130 cities globally and is the preferred choice in Spanish-language jurisdictions [48]. **Composite score (Decidim): 4.7 / 5.0**

| Criterion | Score | Notes |
|---|---|---|
| Licence openness | 5 | AGPL-3.0 |
| Deployment maturity | 5 | 400+ deployments |
| Community health | 5 | Active Decidim Association |
| Interoperability | 4 | REST API, webhooks |
| Security posture | 4 | Actively maintained |
| TCO | 5 | No licence cost |
| Public-sector deployments | 5 | Cities, cantons, federal agencies |

### 4.5 Communication and Collaboration

**Function:** Internal messaging, video conferencing, email, calendar; secure inter-agency communication.

**Recommended components:**
- **Matrix/Element** for messaging and inter-agency secure communication [14]
- **Jitsi Meet** or **BigBlueButton** for video conferencing [34, 35]
- **Nextcloud Talk** for integrated team communication

The German federal BundesMessenger (built on Matrix) provides a reference deployment applicable to municipal contexts, including a procurement framework that municipalities can reference.

| Component | Licence | Score | Key advantage |
|---|---|---|---|
| Matrix/Element | Apache 2.0 | 4.6 | E2E encryption, federation, BundesMessenger reference |
| Jitsi Meet | Apache 2.0 | 4.4 | Browser-based, self-hostable, no plugin required |
| BigBlueButton | LGPL-3.0 | 4.3 | Council meeting management, recording, moderation |
| Nextcloud Talk | AGPL-3.0 | 4.2 | Integrated with file management, Teams-like workflow |

### 4.6 Open Data Publication

**Function:** Publish machine-readable datasets; catalogue data; provide API access; comply with PSI/Open Data directives and EU Data Act.

**Recommended component: CKAN** [22]

CKAN powers opendata.swiss, data.gov, data.gov.uk, and dozens of national and municipal open data portals. CKAN 2.10+ (2025) includes native EU Data Act Article 5 data-sharing APIs and DCAT-AP CH support for Swiss cantonal datasets. **Composite score: 4.6 / 5.0**

| Criterion | Score | Notes |
|---|---|---|
| Licence openness | 5 | AGPL-3.0 |
| Deployment maturity | 5 | 10+ year production track record |
| Community health | 4 | CKAN Association; active |
| Interoperability | 5 | DCAT-AP, DCAT-AP CH, OAI-PMH, SPARQL |
| Security posture | 4 | Actively maintained |
| TCO | 4 | No licence cost; ops overhead |
| Public-sector deployments | 5 | Switzerland, Germany, EU |

### 4.7 Geographic Information Systems

**Function:** Map-based citizen services; urban planning; spatial data publication.

**Recommended components:**
- **QGIS** (desktop/server) for spatial data editing and analysis [37]
- **GeoServer** (GeoTools) for OGC-compliant spatial data publication
- **OpenStreetMap** as the base cartographic layer [36]

Switzerland's swisstopo and Germany's BKG publish their geodata under open licences (CC-BY 4.0 for swisstopo; DL-DE/BY-2.0 for BKG) that permit municipal reuse. QGIS 3.34 LTS (2024) introduced native WFS-T editing from Nextcloud storage, connecting document management and spatial data workflows directly.

### 4.8 Public Website and Content Management

**Function:** Public-facing website; news and announcements; service directory.

**Recommended components:**
- **TYPO3** (DACH region): dominant in Swiss and German public administration; TYPO3 v12 LTS provides a 7-year support window aligned with municipal budget cycles; the GovTypo3 distribution pre-configures BITV 2.0 accessibility compliance [19]
- **Drupal** (international): used by the European Commission; strong accessibility and multilingual track record

Both systems support WCAG 2.1 AA / BITV 2.0, multilingualism, and integration with open data catalogues.

### 4.9 Cloud Infrastructure and Hosting

**Function:** Compute, storage, networking, container orchestration; digital sovereignty at the infrastructure layer.

**Recommended component: Sovereign Cloud Stack (SCS)** [3, 11]

SCS is the most strategically important infrastructure choice for European municipalities. It provides a fully open-source cloud stack (OpenStack + Kubernetes + Ceph) that can be self-hosted, operated by govdigital eG, or deployed by certified SCS cloud operators (plusserver, OSISM). **Composite score: 4.6 / 5.0**

| Criterion | Score | Notes |
|---|---|---|
| Licence openness | 5 | Apache 2.0 / fully open |
| Deployment maturity | 4 | Production in multiple Länder |
| Community health | 5 | OSBA-backed, growing |
| Interoperability | 5 | Open APIs, OCI-compliant |
| Security posture | 5 | BSI IT-Grundschutz compatible |
| TCO | 4 | No licence; infrastructure cost |
| Public-sector deployments | 4 | German Länder, growing |

**GAIA-X alignment:** SCS is a reference implementation for GAIA-X cloud services, providing a pathway to cross-municipal data sharing on federated sovereign infrastructure [54].

### 4.10 Reference Architecture

```
+-------------------------------------------------------------+
|                     CITIZEN TOUCHPOINTS                     |
|         TYPO3/Drupal . Decidim . CKAN . Nextcloud          |
+-------------------------------------------------------------+
|                       SERVICE LAYER                        |
|     Camunda Workflows . XÖV/eCH Forms . GeoServer . QGIS  |
+-------------------------------------------------------------+
|                    COLLABORATION LAYER                     |
|     Nextcloud . Matrix/Element . Jitsi . OpenProject       |
+-------------------------------------------------------------+
|                      IDENTITY LAYER                        |
|       Keycloak <-> BundID / Swiss eID / FIDO2             |
+-------------------------------------------------------------+
|              DATA GOVERNANCE & EXCHANGE LAYER              |
|    CKAN . EU Data Act APIs . XÖV . eCH . GovStack         |
+-------------------------------------------------------------+
|                    INFRASTRUCTURE LAYER                    |
|   Sovereign Cloud Stack . Kubernetes . PostgreSQL . Ceph   |
+-------------------------------------------------------------+
```

All layers communicate via open APIs. Container orchestration is handled by Kubernetes [39]; relational persistence by PostgreSQL [41]; both run on the Sovereign Cloud Stack. Data exchange uses XÖV standards (Germany) [46] or eCH standards (Switzerland) [47]. Security is governed by BSI IT-Grundschutz (Germany) [26] or the Swiss ISDS framework. The Data Governance & Exchange Layer — new in v0.2.0 — acknowledges the EU Data Act's new interoperability obligations and the GovStack building-block architecture [51, 52].

---

## 5. Implementation Roadmap

The implementation is structured as a 36-month, five-phase programme. Each phase has defined deliverables, success criteria, and decision gates.

### Phase 0: Foundation (Months 1–3)

**Objective:** Establish governance, assess current state, build the coalition.

**Deliverables:**
- Digital Transformation Steering Committee established (city leadership + IT + civil society)
- Current-state technology audit completed using Appendix A scoring criteria
- Stakeholder engagement plan adopted (see Section 6)
- Procurement framework established (see Section 6.2 and Appendix B)
- Memorandum of Understanding with cooperative IT provider (Dataport, AKDB, govdigital eG, cantonal IT cooperative)
- 5-year TCO model completed (see Section 5.1)

**Success criteria:**
- Political mandate secured (council resolution or executive decision)
- Budget envelope approved (indicative: €150,000–€400,000 for Phases 0–1, depending on city size)
- Project lead appointed with appropriate authority
- Open-source legal framework reviewed and cleared by procurement office

**Decision gate:** City executive approves full programme budget before Phase 1 begins.

### Phase 1: Identity and Infrastructure (Months 4–12)

**Objective:** Stand up the foundational layers that everything else depends on.

**Deliverables:**
- Sovereign Cloud Stack environment operational (own or hosted via govdigital eG)
- Keycloak identity provider deployed and federated with national identity system (BundID/Swiss eID)
- Nextcloud baseline deployment for internal collaboration
- Matrix/Element messaging for all staff
- BSI IT-Grundschutz (DE) or Swiss ISDS (CH) baseline documentation complete
- Software Bill of Materials (SBOM) tooling operational in SPDX or CycloneDX format

**Success criteria:**
- 100% of IT staff authenticate via Keycloak SSO
- File storage migrated from proprietary cloud to Nextcloud for >50% of users
- Encrypted messaging operational for all staff
- Security baseline documented and approved by DPO

**Decision gate:** Security baseline review and DPO sign-off before Phase 2 begins.

### Phase 2: Services and Workflows (Months 10–18)

**Objective:** Migrate or build the first five citizen-facing services on open infrastructure.

**Deliverables:**
- Five highest-volume administrative services deployed on Camunda/XÖV (DE) or Camunda/eCH (CH) stack
- TYPO3 or Drupal CMS migration complete with WCAG 2.1 AA compliance verified
- Open data portal (CKAN) launched with first 20 datasets and DCAT-AP metadata
- Decidim instance deployed for the first participatory process
- BundID / Swiss eID federation operational for citizen-facing services

**Success criteria:**
- 80% of target service volume processed through new system
- Zero regression in service availability (measured by 95th-percentile response time)
- First open data publication live and harvested by national portal (opendata.swiss or GovData)
- First Decidim participation process completed with >100 participants

**Decision gate:** Service availability and data quality review before Phase 3 begins.

### Phase 3: Integration and Extension (Months 16–24)

**Objective:** Integrate all layers; extend service coverage to 80% of transactions.

**Deliverables:**
- All services federated via Keycloak SSO ("once-only" service delivery enabled)
- Nextcloud integrated with GEVER (Switzerland) or equivalent records workflows
- GIS layer operational (QGIS + GeoServer), integrated with citizen portal
- 80% of administrative services digitised per OZG/cantonal plan
- Inter-agency data exchange via XÖV/eCH operational
- EU Data Act Article 5 data-sharing flows from smart city sensors operational (where applicable)

**Success criteria:**
- End-to-end service delivery without paper for 80% of transaction types
- Data quality metrics publicly reported
- First annual open data report published
- NIS2 compliance assessment completed and remediation plan in place

**Decision gate:** Independent security audit before Phase 4 begins.

### Phase 4: Optimisation and Community (Months 22–30)

**Objective:** Optimise user experience; contribute back to open-source communities; publish results.

**Deliverables:**
- Citizen satisfaction survey (target NPS > 40 for digital services)
- Staff satisfaction survey (target >70% satisfaction with new tools)
- First contribution to openCode.de / upstream projects
- Municipal open-source community of practice established (minimum 3 peer municipalities)
- Performance benchmarks published
- SBOM published for all deployed stack components

**Success criteria:**
- At least three improvements contributed upstream or to openCode.de
- Community of practice active with ≥ 3 peer municipalities
- 5-year TCO report published with actual vs. projected figures

**Decision gate:** TCO and satisfaction report reviewed by city council before Phase 5 begins.

### Phase 5: Sovereignty and Scale (Months 28–36)

**Objective:** Achieve full digital sovereignty; prepare for extension to neighbouring municipalities.

**Deliverables:**
- Full audit of all software components for licence compliance
- Sovereign data residency verified (100% on sovereign infrastructure)
- Playbook for replication by neighbouring municipalities published on openCode.de
- v1.0 of this strategy paper published with actual implementation data

**Success criteria:**
- Zero proprietary single-vendor dependencies in critical service path
- Data residency 100% on sovereign infrastructure
- At least one peer municipality has adopted the playbook
- Municipality acknowledged on openCode.de as a contributing organisation

### 5.1 Total Cost of Ownership Framework

For a representative municipality of 500 staff (population ~30,000–80,000), the following 5-year TCO model compares the open-source stack with a proprietary baseline.

| Cost category | Proprietary baseline (5yr) | Open-source stack (5yr) | Saving |
|---|---|---|---|
| Software licences | €660,000 | €0 | €660,000 |
| Implementation and migration | €200,000 | €350,000 | −€150,000 |
| Hosting (managed cloud) | €300,000 | €180,000 | €120,000 |
| Training | €50,000 | €120,000 | −€70,000 |
| Support contracts | €225,000 | €90,000 | €135,000 |
| Security and audit | €60,000 | €80,000 | −€20,000 |
| **Total** | **€1,495,000** | **€820,000** | **€675,000** |

*Assumptions: Microsoft 365 Business Premium at €22/user/month; Nextcloud + Collabora managed hosting at €6/user/month via govdigital eG framework; one-time migration cost amortised over 5 years; standard IT-Grundschutz security assessment cadence. Larger municipalities see proportionally greater savings due to licence cost scaling; smaller municipalities benefit from cantonal/state framework contracts that spread implementation costs.*

---

## 6. Stakeholder and Procurement Strategy

### 6.1 Stakeholder Map

| Stakeholder | Primary interest | Engagement approach |
|---|---|---|
| Mayor / Executive | Political success, cost, citizen approval | Executive briefing, progress dashboard |
| City council | Oversight, democratic legitimacy | Quarterly reports, open council sessions |
| City IT team | Technical feasibility, workload | Co-design, training, community membership |
| Procurement office | Legal compliance, risk | Framework agreements, legal briefings |
| Civil servants (end users) | Ease of use, reliability | UX testing, change management, training |
| Citizens | Service quality, privacy | Participatory design, transparency reporting |
| Civil society / NGOs | Transparency, access, participation | Decidim platform, public roadmaps |
| Open-source communities | Contribution, reuse | openCode.de participation, upstream contributions |
| Sovereign technology providers | Partnership, deployment | Certified partner agreements |
| Data protection officer | GDPR/nDSG compliance | Privacy-by-design review at each phase |
| ZenDiS / cantonal IT body | National interoperability | Standards alignment, framework adoption |

### 6.2 Procurement Framework

Open-source procurement requires a fundamentally different framework from proprietary licence purchasing. Key principles:

**1. Procure services, not licences.** Open-source software is free to use; municipalities pay for implementation, hosting, support, customisation, and training. Procurement documents must be structured around these services. See Appendix B for sample service-procurement language.

**2. Use cooperative procurement structures.** Germany's govdigital eG and Swiss cantonal IT cooperatives provide framework agreements for open-source municipal IT that satisfy public procurement law (GWB/Vergaberecht in Germany; BöB in Switzerland) [23]. govdigital eG's SCS cloud framework contracts directly reference SCS certification standards.

**3. Apply the "Public Money? Public Code!" principle.** All custom software developed under contract must be released under an OSI-approved open-source licence and published on openCode.de or an equivalent public repository within 90 days of delivery. This must be a contract condition [4]. See Appendix B, clause B.2.

**4. Evaluate total cost of ownership.** Procurement scoring must include a 5-year TCO model (see Section 5.1). Proprietary alternatives typically understate long-term costs by omitting vendor lock-in risk and licence escalation. Require that all bidders provide a 5-year TCO projection using the framework in Appendix B.

**5. Require interoperability standards compliance.** All procured systems must implement: XÖV (Germany) [46], eCH (Switzerland) [47], DCAT-AP (EU open data), and GovStack building-block specifications [52]. Non-compliance is a disqualifying criterion.

**6. Prefer certified cooperative providers.** For infrastructure, prefer SCS-certified cloud operators or members of govdigital eG, who are bound by collective data sovereignty agreements [23].

**7. Build exit provisions into all contracts.** All contracts must include: data export in open formats, minimum 6-month handover period, no lock-in to vendor-specific data formats. These provisions maintain negotiating leverage and reduce future transition costs.

### 6.3 Change Management

Open-source transitions frequently fail not on technical grounds but on human factors: end-user resistance, insufficient training, middle-management inertia, and political backsliding under vendor lobbying.

**Recommendations:**
- Appoint a **Digital Transformation Champion** at senior political level with explicit mandate and budget authority
- Establish **open-source champions** in each department with advanced training and peer support role
- Run **parallel operations** for a minimum of three months before cutting over critical systems
- Document and celebrate **early wins** (cost savings, new capabilities, citizen feedback)
- Publish a **public transparency dashboard** showing migration progress, costs, and service quality metrics
- Engage the **local developer community** as early testers, contributors, and ambassadors

### 6.4 Communication Strategy

Vendor lobbying against open-source transitions is systematic and well-resourced. The communication strategy must proactively address common objections.

| Objection | Evidence-based response |
|---|---|
| "Open source is insecure" | BSI IT-Grundschutz applies equally; SBOM provides transparency proprietary software cannot match; NIS2 compliance is achievable for all stack components |
| "Open source costs more to run" | 5-year TCO model shows €675,000 net savings for a 500-staff municipality; licence costs are real; exit costs are not visible in proprietary quotes |
| "Our staff need Microsoft Office" | Collabora Office (LibreOffice Online) achieves >99% OOXML format compatibility; transition training cost is in the TCO model; migration training costs are one-time, licence costs are perpetual |
| "We'll lose vendor support" | Multiple competing vendors (govdigital eG, Dataport, AKDB, cantonal IT cooperatives) provide support; framework contracts provide SLA guarantees |
| "Munich failed" | Munich's reversal cost ~€49M and was politically motivated, not technically driven; the open-source deployment was operationally cost-effective at the time of reversal |

---

## 7. Risk Analysis

### 7.1 Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Political reversal after election | Medium | High | Embed in legislation/ordinance; build cross-party consensus; document savings publicly |
| Vendor lobbying / FUD campaigns | High | Medium | Document TCO evidence; engage civil society; publicise mandate; use Section 6.4 response table |
| Skill gap in IT team | High | Medium | Training programme; cooperative IT provider; community of practice |
| Integration failure between layers | Medium | High | Phased rollout with decision gates; reference architecture adherence; tested restore procedures |
| Data loss during migration | Low | Critical | Full backup protocol; parallel operation; staged migration; tested restore |
| GDPR / nDSG data protection violation | Low | High | Privacy-by-design; DPO engagement; data mapping; CKAN privacy module |
| User adoption failure | Medium | High | Change management; UX testing; training; parallel systems; champion network |
| Security incident | Low | Critical | BSI IT-Grundschutz; penetration testing; SBOM; incident response plan; NIS2 obligations |
| Community fragmentation | Low | Medium | Contribute upstream; align with openCode.de; join govdigital eG |
| Cost overrun | Medium | Medium | Phase-gated budget; independent project office; open TCO accounting |
| EU Data Act non-compliance | Medium | Medium | Incorporate Article 5 APIs in Phase 2 data portal; legal review at Phase 0 |
| NIS2 compliance gap | Medium | High | NIS2 assessment in Phase 3; ISP-qualified security assessor engaged at programme start |

### 7.2 The Munich Cautionary Case

The City of Munich's LiMux project (2003–2017) is the most-cited case of a large-scale municipal open-source transition that was reversed. Post-mortem analysis identifies the reversal was driven primarily by: (a) a change in political leadership with closer ties to Microsoft; (b) inadequate change management and user training; (c) compatibility issues with state-level systems that had not been updated to support open standards [30]. The technical implementation itself was broadly successful; the independent audit found it operationally cost-effective at the time of reversal. The subsequent return to Microsoft cost the city approximately €49 million — a figure that must be included in any fair TCO comparison.

The Munich case confirms that political risk management — building cross-party support and embedding digital sovereignty in local legislation, not merely in procurement preferences — is as important as technical planning.

### 7.3 Security Considerations

The BSI's IT-Grundschutz framework provides a comprehensive security baseline applicable regardless of licence model [26]. Key requirements for the open-source municipal stack:

- All server components must receive security updates within BSI-mandated timeframes (critical: 24h; high: 7 days; medium: 30 days)
- Authentication must meet BSI Authenticator Assurance Level 2 (AAL2) for citizen-facing services; AAL3 for high-value transactions
- Data in transit encrypted (TLS 1.3 minimum); data at rest encrypted (AES-256) for all sensitive categories
- Penetration testing at each phase gate by a BSI-recognised penetration testing provider
- Incident response plan aligned with NIS2 Article 21 obligations [27]
- Software Bill of Materials (SBOM) maintained in SPDX or CycloneDX format for all open-source dependencies
- Supply chain security: verify GPG signatures for all open-source packages; prefer distribution via verified package registries

**NIS2 applicability:** NIS2 applies to "public administration" entities (Article 3(2)(q)) with more than 50 employees, covering most municipalities above population ~5,000. German NIS2UmsuCG and the revised Swiss ISG extend these obligations to cantonal and municipal administrations [27].

---

## 8. Conclusion

The evidence reviewed in this paper converges on five findings:

**1. Open-source municipal technology stacks are technically mature and production-proven.** Every functional requirement of a modern municipal government can be met by open-source software with documented deployments at peer municipalities, including in the small-municipality context (population 5,000–80,000) that constitutes the majority of European municipalities.

**2. The regulatory environment increasingly mandates open-source and interoperability.** EMBAG (Switzerland), OZG 2.0 (Germany), the Interoperable Europe Act, and the EU Data Act create legal obligations that proprietary, vendor-locked systems cannot sustainably satisfy. Municipalities that begin the transition now are building compliance capital; those that delay are accumulating regulatory debt.

**3. The economic case is compelling when total costs are counted correctly.** Open-source stacks eliminate per-seat licence costs and reduce vendor lock-in risk. A representative 500-staff municipality can save approximately €675,000 over five years. Cooperative procurement models spread implementation costs across many municipalities, reducing per-municipality costs by 60–80%.

**4. ZenDiS, GovStack, and cantonal IT frameworks dramatically reduce the implementation burden for individual municipalities.** The hardest parts of open-source municipal transformation — writing specifications, negotiating framework contracts, assembling a community of practice — have already been done at federal and cantonal levels. Municipalities joining existing frameworks can achieve Phase 1 outcomes in six months rather than eighteen.

**5. Success requires as much political and organisational investment as technical investment.** Clear political mandate, skilled change management, and sustained stakeholder engagement are the binding constraints. Embedding digital sovereignty in local legislation and council resolutions is as important as choosing the right software.

Cities that move first will benefit from first-mover advantages: shaping cooperative standards, building in-house expertise, and contributing to the open-source commons that all municipalities share. The regulatory momentum, the fiscal evidence, and the community of practice are all in place. The invitation is open.

---

## Appendix A: Technology Scoring Matrix

Full scoring for all major stack components (composite = weighted average using weights from Section 2.2).

| Component | Licence | Maturity | Community | Interop | Security | TCO | Public | **Composite** |
|---|---|---|---|---|---|---|---|---|
| Keycloak | 5 | 5 | 5 | 5 | 5 | 4 | 5 | **4.8** |
| Nextcloud | 5 | 5 | 5 | 4 | 5 | 5 | 5 | **4.8** |
| OpenProject | 5 | 4 | 4 | 4 | 4 | 5 | 4 | **4.3** |
| Camunda Community | 4 | 5 | 4 | 5 | 4 | 3 | 4 | **4.1** |
| Flowable (alt.) | 5 | 4 | 3 | 4 | 4 | 5 | 3 | **4.0** |
| Decidim | 5 | 5 | 5 | 4 | 4 | 5 | 5 | **4.7** |
| CONSUL Democracy | 5 | 4 | 4 | 4 | 4 | 5 | 4 | **4.3** |
| Matrix/Element | 5 | 4 | 5 | 5 | 5 | 4 | 4 | **4.6** |
| Jitsi Meet | 5 | 5 | 4 | 4 | 4 | 5 | 4 | **4.4** |
| BigBlueButton | 4 | 5 | 4 | 4 | 4 | 5 | 4 | **4.3** |
| CKAN | 5 | 5 | 4 | 5 | 4 | 4 | 5 | **4.6** |
| QGIS | 5 | 5 | 5 | 5 | 4 | 5 | 4 | **4.7** |
| GeoServer | 4 | 5 | 4 | 5 | 4 | 5 | 4 | **4.4** |
| TYPO3 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | **4.7** |
| Drupal | 5 | 5 | 5 | 4 | 4 | 5 | 4 | **4.6** |
| Sovereign Cloud Stack | 5 | 4 | 5 | 5 | 5 | 4 | 4 | **4.6** |
| Kubernetes | 5 | 5 | 5 | 5 | 5 | 4 | 5 | **4.8** |
| PostgreSQL | 5 | 5 | 5 | 5 | 5 | 5 | 5 | **5.0** |

---

## Appendix B: Sample Procurement Language

The following clauses are designed for inclusion in municipal IT procurement documents (tender specifications / Leistungsbeschreibung / Cahier des charges).

### B.1 Open Source Licence Requirement

> All software components procured under this contract must be licensed under an Open Source Initiative (OSI)-approved licence. The contractor must provide a Software Bill of Materials (SBOM) in SPDX or CycloneDX format, updated quarterly, listing all open-source dependencies and their licences.

### B.2 Public Money, Public Code

> All custom software developed specifically for [Municipality Name] under this contract must be released as open-source software within 90 days of delivery. The release must be: (a) published on openCode.de or an equivalent public repository; (b) licensed under an OSI-approved licence; (c) accompanied by documentation enabling reuse by other public administrations.

### B.3 Interoperability Requirements

> All systems delivered under this contract must implement the following standards: [select applicable] XÖV standards (Germany): XPersonenstand, XMeld, as applicable / eCH standards (Switzerland): eCH-0044, eCH-0147, as applicable / DCAT-AP for all data catalogue interfaces / OpenID Connect for all identity federation / BPMN 2.0 for all workflow interfaces. Non-compliance with mandatory standards is a disqualifying criterion.

### B.4 Data Sovereignty Requirements

> All data processed under this contract must be stored and processed exclusively within [EU / Switzerland / Germany / Canton X]. The contractor must: (a) specify data centre locations in the offer; (b) notify the client immediately of any subprocessor change; (c) provide documented data export in open formats on 30 days' notice; (d) delete all client data within 30 days of contract termination.

### B.5 Total Cost of Ownership Projection

> Each offer must include a 5-year Total Cost of Ownership projection covering: (a) licensing; (b) implementation and migration; (c) hosting and infrastructure; (d) training; (e) support and maintenance; (f) estimated exit costs after year 5. Offers without a 5-year TCO projection will be rejected as non-compliant.

---

## Appendix C: Quarterly Literature Review Checklist

When running `Scripts/update_literature_review.py`, check for:

**Legislation and Policy**
- [ ] New Swiss e-government legislation or eCH standards updates
- [ ] New German OZG implementation reports, FITKO publications, ZenDiS updates
- [ ] New EU legislation affecting municipal IT (Data Act implementation, AI Act, DSA/DMA)
- [ ] New Interoperable Europe Act implementation guidance
- [ ] Swiss nDSG implementation updates

**Technology**
- [ ] New Sovereign Cloud Stack releases or governance updates
- [ ] New openCode.de statistics or case studies
- [ ] Nextcloud, Decidim, Matrix, CKAN, Camunda, TYPO3 major releases
- [ ] New security advisories affecting stack components (BSI CERT-Bund, NCSC-CH)
- [ ] New SBOM tooling or standards updates (SPDX, CycloneDX)

**Research and Reports**
- [ ] New academic papers on e-government maturity (GIQ, ISM, EJEG)
- [ ] New municipal open-source deployments or case studies
- [ ] OSOR annual report (EU Open Source Observatory, annual) [50]
- [ ] UN E-Government Survey (biannual — next: 2024) [29]
- [ ] ZenDiS annual report [49]
- [ ] govdigital eG annual report [23]

**Quality Assurance**
- [ ] Verify any source registry entries marked "unverified"
- [ ] Update dead URLs in source registry
- [ ] Check for new versions of cited documents (strategy updates, legislation amendments)
- [ ] Cross-check TCO figures against new published data

---

## References

[1] Swiss Federal Council. (2023). *Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG)*. SR 172.019. Bern: Swiss Confederation. https://www.fedlex.admin.ch/eli/cc/2023/682/de — [CC0]

[2] Bundesministerium des Innern und für Heimat (BMI). (2024). *Onlinezugangsgesetz 2.0 (OZG 2.0)*. Berlin: BMI. https://www.bmi.bund.de/DE/themen/moderne-verwaltung/e-government/ozg/ozg-node.html — [DL-DE/Zero 2.0]

[3] Open Source Business Alliance (OSBA). (2023). *Sovereign Cloud Stack: Technical and Governance Overview*. Berlin: OSBA. https://scs.community/ — [CC-BY-SA-4.0]

[4] Free Software Foundation Europe (FSFE). (2017). *Public Money? Public Code!* Berlin: FSFE. https://publiccode.eu/ — [CC-BY-SA-4.0]

[5] European Commission. (2020). *Open Source Software Strategy 2020–2023: Think Open*. Brussels: European Commission. https://commission.europa.eu/about/departments-and-executive-agencies/informatics/open-source-software-strategy_en

[6] European Parliament and Council. (2024). *Regulation (EU) 2024/903 — Interoperable Europe Act*. Brussels: Official Journal of the EU. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202400903 — [Open access]

[7] Wirtz, B. W., & Weyerer, J. C. (2017). Conceptualization and creation of a holistic e-government maturity model. *Public Management Review*, 19(9), 1297–1316. https://doi.org/10.1080/14719037.2017.1283024

[8] Janssen, M., Charalabidis, Y., & Zuiderwijk, A. (2012). Benefits, adoption barriers and myths of open data and open government. *Information Systems Management*, 29(4), 258–268. https://doi.org/10.1080/10580530.2012.716740

[9] FITKO. (2024). *Föderale IT-Kooperation — Publikationen*. Frankfurt: FITKO. https://www.fitko.de/presse/veroeffentlichungen — [DL-DE/Zero 2.0]

[10] openCode.de. (2022). *openCode — Open Source for Government*. Berlin: Digitalservice GmbH des Bundes. https://opencode.de/ — [Open access]

[11] Sovereign Cloud Stack Community. (2024). *SCS Technical Documentation*. https://docs.scs.community/ — [Apache 2.0]

[12] Decidim Association. (2024). *Decidim: Free Open-Source Participatory Democracy for Cities and Organizations*. Barcelona: Decidim Association. https://decidim.org/ — [AGPL-3.0]

[13] Nextcloud GmbH. (2024). *Nextcloud for Government: Security, Sovereignty, and Collaboration*. Stuttgart: Nextcloud GmbH. https://nextcloud.com/government/ — [Open access]

[14] The Matrix Foundation. (2024). *Matrix Specification v1.11*. https://spec.matrix.org/ — [Apache 2.0]

[16] E-Government Suisse. (2024). *Strategie E-Government Schweiz 2024–2027*. Bern: Schweizerische Bundeskanzlei. https://www.egovernment.ch/de/umsetzung/e-government-strategie/ — [Open access]

[19] TYPO3 Association. (2024). *TYPO3 in Public Administration*. Düsseldorf: TYPO3 Association. https://typo3.org/project/association — [Open access]

[20] OpenProject GmbH. (2024). *OpenProject for Government: Open Source Project Management*. Berlin: OpenProject GmbH. https://www.openproject.org/ — [GPLv3]

[21] Red Hat / Keycloak Community / CNCF. (2024). *Keycloak: Open Source Identity and Access Management*. https://www.keycloak.org/ — [Apache 2.0]

[22] CKAN Association. (2024). *CKAN: Open Source Data Portal Software*. https://ckan.org/ — [AGPL-3.0]

[23] govdigital eG. (2024). *govdigital: Genossenschaft für digitale Verwaltung*. Berlin: govdigital eG. https://govdigital.de/ — [Open access]

[24] Dataport AöR. (2024). *Dataport: IT-Dienstleister für die öffentliche Verwaltung*. Hamburg: Dataport AöR. https://www.dataport.de/ — [Open access]

[26] Bundesamt für Sicherheit in der Informationstechnik (BSI). (2023). *BSI IT-Grundschutz-Kompendium Edition 2023*. Bonn: BSI. https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/ — [CC-BY-ND 3.0 DE]

[27] European Parliament and Council. (2022). *Directive (EU) 2022/2555 — NIS2 Directive*. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022L2555 — [Open access]

[29] United Nations DESA. (2022). *UN E-Government Survey 2022: The Future of Digital Government*. New York: United Nations. https://publicadministration.un.org/egovkb/en-us/Reports/UN-E-Government-Survey-2022 — [Open access]

[30] Janowski, T. (2015). Digital government evolution: From transformation to contextualization. *Government Information Quarterly*, 32(3), 221–226. https://doi.org/10.1016/j.giq.2015.07.001

[33] Camunda Services GmbH. (2024). *Camunda Platform 8 Community Edition*. https://camunda.com/ — [Apache 2.0]

[34] BigBlueButton Inc. (2024). *BigBlueButton: Open Source Web Conferencing*. https://bigbluebutton.org/ — [LGPL-3.0]

[35] Jitsi Community. (2024). *Jitsi Meet: Open Source Video Conferencing*. https://jitsi.org/ — [Apache 2.0]

[36] OpenStreetMap Foundation. (2024). *OpenStreetMap*. https://www.openstreetmap.org/ — [ODbL-1.0]

[37] QGIS Project. (2024). *QGIS: A Free and Open Source Geographic Information System*. https://www.qgis.org/ — [GPL-2.0+]

[39] Cloud Native Computing Foundation (CNCF). (2024). *Kubernetes*. https://kubernetes.io/ — [Apache 2.0]

[41] PostgreSQL Global Development Group. (2024). *PostgreSQL*. https://www.postgresql.org/ — [PostgreSQL Licence]

[42] BMI / ZenDiS GmbH. (2024). *OpenDesk: Der digitale Arbeitsplatz der Bundesverwaltung*. https://opendesk.eu/ — [AGPL-3.0]

[43] Schweizerisches Bundesarchiv (BAR). (2024). *Geschäftsverwaltung (GEVER) in der Bundesverwaltung*. Bern: BAR. https://www.bar.admin.ch/bar/de/home/digitale-archivierung/gever.html — [Open access]

[44] opendata.swiss. (2024). *Open Government Data Switzerland*. Bern: Schweizerische Bundeskanzlei. https://opendata.swiss/ — [CC-BY-4.0]

[45] European Commission. (2017). *European Interoperability Framework — Implementation Strategy (EIF)*. Brussels: European Commission. https://joinup.ec.europa.eu/collection/nifo-national-interoperability-framework-observatory/european-interoperability-framework-detail — [CC-BY-4.0]

[46] KoSIT. (2024). *XÖV-Standards: XML in der öffentlichen Verwaltung*. Bremen: KoSIT. https://www.xoev.de/ — [Open access]

[47] eCH — eGovernment Standards. (2024). *eCH Standards for e-Government Switzerland*. Bern: eCH Association. https://www.ech.ch/ — [CC-BY-SA-4.0]

[48] CONSUL Democracy Foundation. (2024). *CONSUL Democracy: Open Government and Citizen Participation*. Madrid: CONSUL Democracy Foundation. https://consuldemocracy.org/ — [AGPL-3.0]

[49] ZenDiS GmbH. (2024). *ZenDiS: Zentrum für Digitale Souveränität der öffentlichen Verwaltung*. Berlin: ZenDiS GmbH. https://zendis.de/ — [Open access]

[50] European Commission / OSOR. (2023). *Open Source Observatory Annual Report 2023*. Brussels: European Commission / Joinup. https://joinup.ec.europa.eu/collection/open-source-observatory-osor — [CC-BY-4.0]

[51] European Parliament and Council. (2023). *Regulation (EU) 2023/2854 — EU Data Act*. Brussels: Official Journal of the EU. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202302854 — [Open access]

[52] International Telecommunication Union (ITU) / Digital Impact Alliance (DIAL). (2023). *GovStack: Digital Public Infrastructure Building Blocks*. Geneva: ITU. https://www.govstack.global/ — [Open access]

[53] Lathrop, D., & Ruma, L. (Eds.). (2010). *Open Government: Collaboration, Transparency, and Participation in Practice*. Sebastopol, CA: O'Reilly Media. ISBN: 978-0596804350

[54] GAIA-X AISBL. (2025). *GAIA-X Architecture Document Release 25.01*. Brussels: GAIA-X AISBL. https://docs.gaia-x.eu/ — [Open access]

[55] Geschäftsstelle OGD Schweiz / Schweizerische Bundeskanzlei. (2024). *Open-Government-Data-Strategie Schweiz 2024–2027*. Bern: Schweizerische Bundeskanzlei. https://www.bfs.admin.ch/bfs/de/home/dienstleistungen/ogd.html — [Open access]

---

*This document is released under the Creative Commons Attribution 4.0 International Licence (CC-BY-4.0).*  
*Attribute as: Sebastian Graf, Autonomous Office of Civil Digital Infrastructure (sebk4c@tuta.com)*  
*Version 0.2.0 — Citation-Complete Draft — 2026-06-21*
