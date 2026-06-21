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
  - GovStack
  - EU Data Act
  - AI Act
---

# Sovereign by Design: A State-of-the-Art Open-Source Technology Strategy for Municipal Governments

**Author:** Sebastian Graf, Autonomous Office of Civil Digital Infrastructure  
**Correspondence:** sebk4c@tuta.com  
**Version:** 0.2.0 — Citation-Complete Draft  
**Date:** 2026-06-21  
**Languages:** English (source of truth) · Deutsch  
**SPDX-License-Identifier:** CC-BY-4.0  

---

## Changelog

| Version | Date | Summary |
|---|---|---|
| 0.1.0 | 2026-06-20 | Initial structured draft |
| 0.2.0 | 2026-06-21 | Case studies section (§5); accessibility layer (§4.10); AI tools layer (§4.11); EU Data Act and GovStack coverage (§3.5–3.6); verified citations [6][9][16][43]; new sources [47]–[62]; small municipality pathway (§6.2); German Vergaberecht and Swiss BöB specifics (§7.3–7.4); GDPR and AI Act risk sections (§8.4–8.5); Appendix A (small municipality checklist); Appendix B (procurement language templates) |

---

## Abstract

Municipal governments are the closest layer of democratic administration to citizens, yet they face an acute structural tension: the digital tools they depend on are increasingly proprietary, vendor-locked, and misaligned with public-interest values. This paper presents a comprehensive strategy for implementing a state-of-the-art, open-source governmental administration technology stack in city governments. Drawing on exemplary practices from the Swiss federal administration's EMBAG legislation, Germany's OZG reform programme and Sovereign Cloud Stack initiative, and the wider European sovereign technology community, we derive a first-principles implementation roadmap, stakeholder engagement framework, and procurement strategy. We evaluate eleven core technology layers — identity management, document management, workflow automation, citizen participation, secure communications, open data publication, geographic information systems, content management, cloud infrastructure, accessibility, and AI/automation tools — against criteria of digital sovereignty, interoperability, total cost of ownership, and civic alignment. Case studies from Barcelona, the German federal OpenDesk programme, the Canton of Schaffhausen, Schleswig-Holstein, Moers, and the cautionary Munich LiMux reversal provide empirical grounding. We conclude that open-source municipal technology stacks are not merely technically viable but fiscally superior, democratically necessary, and legally mandated in an increasing number of jurisdictions. The paper provides a phased 36-month implementation roadmap with procurement guidance adapted for both German Vergaberecht and Swiss BöB procurement law, and appendices providing quick-start checklists and model procurement language.

**Keywords:** digital sovereignty, open source government, GovTech, municipal digital transformation, OZG, EMBAG, Sovereign Cloud Stack, e-government, GovStack, EU Data Act, AI Act

---

## 1. Introduction

The digital transformation of municipal government is no longer optional. Citizens expect seamless, secure, and accessible digital services; regulators demand interoperability and data protection; fiscal pressures require sustainable, cost-effective technology investments. Yet the majority of city governments worldwide remain trapped in a cycle of proprietary vendor dependency, expensive licence agreements, and fragmented systems that impede rather than enable good governance [1, 29].

The consequences are well-documented: vendor lock-in raises switching costs and bargaining asymmetry [4]; proprietary formats obstruct cross-agency data exchange and transparency [45]; closed-source infrastructure prevents independent security auditing [26]; and recurring licence fees drain budgets that could otherwise fund service delivery [3, 5]. Most fundamentally, when the software running democratic institutions is owned by private actors, a structural conflict of interest emerges between the public interest and corporate imperatives [4, 53].

A different path is both possible and proven. Switzerland's 2023 EMBAG legislation mandates that federal software developed with public funds be released as open source by default [1]. Germany's OZG reform, Sovereign Cloud Stack, and OpenDesk initiative represent the most ambitious open-source government technology programme in Europe [2, 3, 42]. The EU's Interoperable Europe Act 2024 creates binding cross-border interoperability obligations [6]. The Free Software Foundation Europe's "Public Money? Public Code!" campaign, endorsed by over 200 organisations across 30 countries, articulates the democratic principle: software paid for by the public should be available to the public [4].

This paper synthesises these developments into a practical strategy for municipal governments. It is addressed to all relevant stakeholders — city administrators, elected officials, public-sector IT teams, procurement offices, civil-society groups, open-source communities, and sovereign technology providers.

### 1.1 Scope and Definitions

*Municipal government* refers to city and local government authorities, including Gemeinden, Kommunen, Städte, and equivalent structures in Swiss cantons. The strategy scales from small municipalities (population 5,000–50,000) to large cities (population 500,000+), with specific pathways for each scale.

*Open-source technology stack* refers to software components licensed under OSI-approved licences, deployed on infrastructure that the municipality controls or can migrate away from without undue cost or friction.

*Digital sovereignty* is the ability of a government to make independent decisions about its digital infrastructure, including the right to inspect, modify, audit, and migrate software without dependency on a single vendor [3].

### 1.2 Research Questions

1. What does a state-of-the-art open-source municipal technology stack look like in 2026?
2. What lessons can be drawn from the Swiss, German, and European sovereign technology communities?
3. What is the optimal phased implementation pathway for city governments at different scales?
4. How should procurement, stakeholder engagement, and risk management be structured to maximise success probability?

---

## 2. Methodology

This paper employs a multi-method research design combining:

**Systematic literature review** of peer-reviewed publications, grey literature, and policy documents published between 2010 and 2026, covering e-government theory, digital sovereignty, open-source software in public administration, and municipal digital transformation.

**Comparative policy analysis** of technology legislation and strategies from Switzerland (EMBAG 2023, E-Government Strategy 2024–2027), Germany (OZG 2017/2024, Deutsche Verwaltungscloud-Strategie), and the European Union (Interoperable Europe Act 2024, EU Open Source Strategy 2020–2023, EU Data Act 2023, EU AI Act 2024).

**Technology stack evaluation** using a structured scoring matrix assessing each component on seven criteria: (a) licence openness (15%), (b) deployment maturity (20%), (c) community health (15%), (d) interoperability standards compliance (15%), (e) security posture (15%), (f) total cost of ownership (10%), and (g) existing public-sector deployments (10%). Scores are ordinal (1–5).

**Case study analysis** examining six municipal and governmental deployments: Barcelona, German federal OpenDesk, Canton of Schaffhausen, Schleswig-Holstein, Moers, and Munich LiMux, using publicly available documentation, government reports, and community sources [55, 56, 60].

**Stakeholder analysis** mapping the interests, influence, and engagement needs of each stakeholder group.

The literature review is designed to be self-improving: the source registry (`Mem/source-registry.md`) and literature review state (`Mem/literature-review-state.md`) are versioned documents updated on a recurring quarterly basis via `Scripts/update_literature_review.py`.

### 2.1 Inclusion Criteria

Sources were included if they: (a) address open-source software in public administration; (b) cover governmental digital transformation strategy; (c) relate to the European, Swiss, or German regulatory context; or (d) provide primary data on municipal technology implementations. Sources published before 2010 were included only where they establish foundational theoretical frameworks [53].

### 2.2 Limitations

Technology stack assessments reflect the state of publicly available information as of June 2026. Implementation cost estimates are indicative and must be validated against local procurement conditions. The rapidly evolving EU AI Act delegated acts may introduce requirements not fully reflected here.

---

## 3. Literature Review

### 3.1 Theoretical Foundations of E-Government

The academic literature on e-government has evolved through four broad phases [30]. First-generation e-government (1995–2005) focused on digitising existing processes and creating government websites [29]. Second-generation (2005–2012) emphasised online service delivery, citizen portals, and back-office integration [7]. Third-generation (2012–2020) introduced open data, participatory platforms, and mobile-first service design [8]. The current fourth generation (2020–present) is characterised by platform government, digital identity infrastructure, data spaces, and the sovereignty turn — a recognition that digital autonomy is a prerequisite for democratic self-governance [45].

Wirtz and Weyerer's holistic e-government maturity model identifies five dimensions: technical infrastructure, process quality, service quality, citizen orientation, and transparency [7]. The KGSt applies an analogous five-stage maturity model in the German municipal context, noting that the majority of German municipalities remain at stages 2–3 rather than stages 4–5 [61]. Open-source stacks are shown to accelerate progress toward stages 4–5 by removing licence barriers to customisation and integration.

Lathrop and Ruma's foundational *Open Government* (2010) established the democratic-values case for open data, open standards, and open-source software as inseparable pillars of transparent, participatory, and collaborative governance [53]. This framework underpins the FSFE campaign [4] and the EU's Open Source Strategy [5], providing a democratic legitimacy argument beyond economic or technical considerations.

### 3.2 Digital Sovereignty in Public Administration

The concept of digital sovereignty has moved from academic concept to policy imperative in the European context [3, 5]. The EU Open Source Strategy 2020–2023 established "sharing and reuse" as a core principle, mandating that European institutions prefer open-source solutions [5]. The 2024 Interoperable Europe Act (Regulation (EU) 2024/903) creates binding obligations for cross-border interoperability in public administrations across the EU and establishes the Interoperable Europe Board as a coordination mechanism [6].

Germany's Sovereign Cloud Stack (SCS), developed by the Open Source Business Alliance (OSBA) and partially funded by BMWK, is the most concrete realisation of digital sovereignty in European cloud infrastructure. SCS provides a fully open-source, self-hostable cloud platform (OpenStack + Kubernetes + Ceph) enabling public administrations to operate technically and legally sovereign, auditable, portable infrastructure [3]. As of 2026, SCS underpins cloud environments in several German Länder and integrates with govdigital eG's shared public-sector infrastructure [23].

Switzerland's EMBAG (SR 172.019), in force since 1 January 2024, requires all federal software developed with public funds to be released as open source unless compelling security or other statutory reasons prevent it [1]. This places Switzerland among the most progressive open-source mandating jurisdictions globally.

### 3.3 The German OZG Ecosystem

The Onlinezugangsgesetz (OZG), enacted 2017 and substantially reformed in 2024 (OZG 2.0), requires all German federal, Land, and municipal administrations to offer administrative services online [2]. The OZG 2.0 reform addresses first-generation shortcomings through the "Once Only" principle, the "Einer für Alle" (EfA) shared service approach, and a federal platform architecture centred on BundID and FITKO [9, 10].

The openCode.de platform (2022) provides a centralised repository for government open-source software, enabling discovery, reuse, and contribution across all administrative levels [10]. ZenDiS (Zentrum für Digitale Souveränität der öffentlichen Verwaltung), established 2022 as a federal public company, coordinates open-source development for German public administration, including management of the OpenDesk suite [51]. Dataport AöR and AKDB represent the cooperative model of public-sector IT delivery that underpins this ecosystem [24].

### 3.4 Swiss Cantonal and Federal Digital Services

Switzerland's federal structure creates both challenges and opportunities distinct from the German context. Key infrastructure includes:

- **Fedlex** (fedlex.admin.ch): official platform for Swiss federal law on open standards, providing machine-readable legal data [1]
- **opendata.swiss**: national open government data portal built on CKAN, cataloguing thousands of datasets under OGD Switzerland standards [44]
- **GEVER**: standardised records management system providing a certified template for cantonal and municipal implementations [43]
- **Swiss eID**: rebuilt as a privacy-preserving, SSI-based (Self-Sovereign Identity) digital identity system after the 2021 referendum rejection of the first version
- **eCH standards**: the Swiss e-government data exchange standards organisation, producing XML-based standards (eCH-0046 for digital delivery, eCH-0099 for identity federation, eCH-0115 for open government data) analogous to Germany's XÖV family [47]

The E-Government Strategy Switzerland 2024–2027, adopted by the Federal Council and the Conference of Cantonal Governments, mandates open standards and interoperability across all levels of Swiss administration [16].

### 3.5 The Evolving EU Digital Regulatory Environment

The EU's digital regulatory landscape has expanded substantially in 2023–2024 in ways that directly affect municipal technology procurement.

**EU Data Act 2023** (Regulation (EU) 2023/2854, in force from September 2025) establishes rules for access to and use of data generated by IoT devices, including smart city sensors, connected infrastructure, and municipal facilities management systems [50]. For municipalities with smart city ambitions, the Data Act creates both obligations (to make data accessible) and rights (to access data from private operators of connected infrastructure). Open-source data platforms (CKAN, Gaia-X data spaces) align better with Data Act obligations than proprietary systems.

**EU Artificial Intelligence Act 2024** (Regulation (EU) 2024/1689, in force from August 2024) introduces a risk-based framework directly affecting AI systems used in public administration [57]. AI systems used in municipal contexts for decisions affecting citizens (benefits assessment, permit processing, risk scoring) fall into the "high-risk" category, subject to transparency, accuracy, human oversight, and CE marking requirements.

**EU Interoperable Europe Act** (Regulation (EU) 2024/903) requires mandatory interoperability assessments for shared digital services across member states [6]. This creates new institutional infrastructure that municipalities can leverage to access shared EU digital services and join cross-border digital service networks.

### 3.6 GovStack: An International Building-Block Framework

The GovStack initiative, jointly developed by the International Telecommunication Union (ITU) and the Digital Impact Alliance (DIAL), defines a set of reusable, open-source "building blocks" for government digital service delivery [49]. GovStack's 14 building blocks — including identity, payments, workflow, messaging, consent, registration, and scheduling — provide an internationally validated framework for municipal service architecture that complements the European open-source stack described in this paper.

Germany has been a contributing member to GovStack since 2022, and the building-block model aligns with the OZG EfA approach. Swiss e-government bodies are exploring GovStack-compliant architectures for future cantonal service platforms. For municipalities procuring new citizen-facing services, GovStack compliance should be a specification requirement alongside XÖV/eCH interoperability.

### 3.7 Open Source Communities and Sovereign Technology Platforms

**Decidim** (Barcelona, 2016) is a participatory democracy platform used by over 400 organisations in 40 countries [12]. Its governance model — a multi-stakeholder association with a published social contract binding all deployments — is itself a model for open-source sovereignty.

**CONSUL Democracy** (Madrid, 2015) is a complementary participation platform used by over 50 cities and governments, with stronger multilingual support for Spanish-speaking communities and a simpler deployment model [48].

**Matrix/Element** provides an open, decentralised, end-to-end-encrypted communication protocol. The German federal BundesMessenger and the French government's Tchap both operate on Matrix [14, 60]. The federation capability means municipalities can communicate with each other and with federal agencies on the same infrastructure.

**Nextcloud** (Stuttgart, 2016) is the most widely deployed open-source file sync and collaboration platform in European public administration [13].

**OpenDesk**, launched by the German Federal Government in 2023 and managed by ZenDiS GmbH, is a curated open-source workplace suite: Nextcloud, CryptPad, OpenProject, Jitsi Meet, and Element [42, 51].

### 3.8 Total Cost of Ownership Evidence

Available TCO evidence includes:

- **French state LibreOffice migration** (2018–2023): 100,000 desktops migrated; estimated savings of €20M over five years against ~€5M implementation cost [52]
- **Schleswig-Holstein desktop estimate** (2024): projections of €30M in licence savings over 10 years from transitioning 25,000 computers to Linux and LibreOffice [54]
- **Barcelona Decidim** (2016–2026): Zero-licence platform enabling processes for €75M in citizen budget allocation; estimated operational cost <€500K/year [56]
- **Munich LiMux controversy**: A 2013 city report claimed the Linux migration cost €23M more than staying with Windows; independent analysis identified methodological flaws in attribution and comparison period selection [55]. The reversal cost has never been disclosed.

The methodological challenge is attribution: open-source transitions require training and integration investment that proprietary migrations also require but rarely disclose. A genuine 5-year TCO model must include licence fees, implementation, training, integration, support, and exit costs for both scenarios.

### 3.9 Gaps in the Literature

1. Independent comparative TCO studies at the system level remain absent
2. Small-municipality case studies (<50,000 population) are underrepresented
3. Citizen satisfaction research comparing open-source and proprietary municipal services is almost entirely absent
4. EU AI Act compliance for municipal AI tools is an emerging area with limited peer-reviewed guidance
5. eCH and GovStack integration case studies from Swiss municipalities are not yet available

See `Mem/literature-review-state.md` for the full gap analysis and improvement roadmap.

---

## 4. Technology Stack Analysis

A municipal technology stack can be decomposed into eleven functional layers.

### 4.1 Digital Identity and Authentication

**Function:** Authenticate citizens and staff; federate identity across services; implement SSO; integrate with national identity systems.

**Recommended component: Keycloak** (Red Hat / CNCF) [21]

Keycloak is the de facto open-source IAM platform for European public administration. It implements OpenID Connect, OAuth 2.0, SAML 2.0, and FIDO2/WebAuthn, enabling federation with national identity systems (BundID in Germany, Swiss eID).

| Criterion | Score | Notes |
|---|---|---|
| Licence openness | 5 | Apache 2.0 |
| Deployment maturity | 5 | Production-proven, 10+ years |
| Community health | 5 | Large, active, CNCF-supported |
| Interoperability | 5 | OIDC, OAuth2, SAML2, FIDO2 |
| Security posture | 5 | CVE-responsive, widely audited |
| TCO | 4 | No licence cost; ops expertise required |
| Public-sector deployments | 5 | EU institutions, German Länder, Swiss cantons |
| **Weighted score** | **4.85** | |

**Integration note:** Keycloak must be federated with BundID (Germany) or the Swiss eID system to avoid creating parallel identity silos. Federation is achieved via OIDC or SAML2 bridges.

### 4.2 Document Management and Records

**Function:** Store, retrieve, classify, and retain official records; manage GEVER-compliant workflows.

**Recommended components: Nextcloud** + **OpenProject** [13, 20]

For municipalities requiring full GEVER compliance (Switzerland), CMI AG Community Edition and Fabasoft Community Edition provide the compliance layer with Nextcloud as the collaborative front-end. For German municipalities, AKDB and Dataport components provide equivalent capability.

| Criterion | Score | Notes |
|---|---|---|
| Licence openness | 5 | AGPL-3.0 |
| Deployment maturity | 5 | 400,000+ organisations (Nextcloud) |
| Community health | 5 | Nextcloud GmbH + community |
| Interoperability | 4 | WebDAV, CalDAV, CardDAV, CMIS |
| Security posture | 5 | ISO 27001-certified offering |
| TCO | 5 | No per-seat licence (Community Edition) |
| Public-sector deployments | 5 | Swiss federal, German Länder, EU institutions |
| **Weighted score** | **4.80** | |

### 4.3 Workflow Automation and Business Process Management

**Function:** Automate administrative workflows; model, execute, and monitor BPMN processes; integrate with XÖV and eCH data standards.

**Recommended component: Camunda Platform 8 Community** [33]

Camunda provides a BPMN 2.0-native workflow engine with strong support for complex multi-step administrative processes. **Flowable** (Apache 2.0) is a lighter-weight alternative [46, 47].

| Criterion | Score | Notes |
|---|---|---|
| Licence openness | 4 | Community: Apache 2.0; Enterprise: proprietary |
| Deployment maturity | 5 | Production-proven |
| Community health | 4 | Active; enterprise tier funds development |
| Interoperability | 5 | BPMN 2.0, REST API, event-driven, XÖV |
| Security posture | 4 | Actively maintained |
| TCO | 3 | Community free; large-scale may need Enterprise |
| Public-sector deployments | 4 | Multiple German Länder |
| **Weighted score** | **4.15** | |

### 4.4 Citizen Participation

**Function:** Consultation, participatory budgeting, initiative collection, deliberation, and policy co-creation.

**Primary recommendation: Decidim** [12] · **Alternative: CONSUL Democracy** [48]

Decidim is the most mature and widely adopted open-source participation platform globally. CONSUL Democracy offers a simpler architecture suitable for smaller municipalities without dedicated platform teams.

| Criterion | Decidim | CONSUL |
|---|---|---|
| Licence openness | 5 (AGPL-3.0) | 5 (AGPL-3.0) |
| Deployment maturity | 5 | 4 |
| Community health | 5 | 4 |
| Interoperability | 4 | 3 |
| Security posture | 4 | 4 |
| TCO | 5 | 5 |
| Public-sector deployments | 5 | 4 |
| **Weighted score** | **4.70** | **4.10** |

### 4.5 Communication and Collaboration

**Function:** Internal messaging, video conferencing, email, calendar; secure inter-agency communication.

**Recommended components:**
- **Matrix/Element** for messaging and inter-agency secure communication [14, 60]
- **Jitsi Meet** or **BigBlueButton** for video conferencing [34, 35]
- **Nextcloud Talk** for integrated team communication

The German federal BundesMessenger (Matrix-based) enables municipal staff to communicate directly with federal agency staff on the same encrypted, federated infrastructure — a significant operational advantage over proprietary silos [60].

| Component | Licence | Maturity | Key advantage |
|---|---|---|---|
| Matrix/Element | Apache 2.0 | Production | E2E encryption, BundesMessenger federation |
| Jitsi Meet | Apache 2.0 | Production | Browser-based, no client install |
| BigBlueButton | LGPL-3.0 | Production | Council meeting recording |
| Nextcloud Talk | AGPL-3.0 | Production | Integrated with document management |

### 4.6 Open Data Publication

**Function:** Publish machine-readable datasets; catalogue data; provide API access; comply with PSI/Open Data directives.

**Recommended component: CKAN** [22]

CKAN powers opendata.swiss, data.gov, and data.gov.uk. Its plugin architecture enables integration with DCAT-AP (EU), DCAT-AP.de (Germany), and OGD Switzerland metadata standards.

| Criterion | Score | Notes |
|---|---|---|
| Licence openness | 5 | AGPL-3.0 |
| Deployment maturity | 5 | 10+ year production track record |
| Community health | 4 | CKAN Association; active |
| Interoperability | 5 | DCAT-AP, OAI-PMH, SPARQL |
| Security posture | 4 | Actively maintained |
| TCO | 4 | No licence cost; moderate ops overhead |
| Public-sector deployments | 5 | opendata.swiss, data.gov, data.gov.uk |
| **Weighted score** | **4.50** | |

**EU Data Act alignment:** CKAN's DCAT-AP compliance and open API architecture align with Data Act obligations for IoT and smart city data sharing [50].

### 4.7 Geographic Information Systems

**Function:** Map-based citizen services; urban planning; spatial data publication; OGC-compliant APIs.

**Recommended components:**
- **QGIS** for spatial data editing, analysis, and server-side publication [37]
- **GeoServer** (GeoTools) for OGC-compliant WMS/WFS/WCS
- **OpenStreetMap** as the base cartographic layer [36]

Switzerland's swisstopo and Germany's BKG provide open, high-quality national base map data directly importable into QGIS/GeoServer.

### 4.8 Public Website and Content Management

**Function:** Public-facing website; news and announcements; service directory; multilingual content; accessibility compliance.

**Recommended components:**
- **TYPO3** (German-speaking world): dominant in Swiss and German public administration; TYPO3 Association provides LTS versions and public-sector extensions with BITV 2.0 / WCAG 2.1 AA support [19]
- **Drupal**: strong international track record; used by the European Commission and Finnish government

### 4.9 Cloud Infrastructure and Hosting

**Function:** Compute, storage, networking, container orchestration; digital sovereignty at the infrastructure layer.

**Recommended component: Sovereign Cloud Stack (SCS)** [3, 11]

SCS provides a fully open-source cloud stack (OpenStack + Kubernetes + Ceph) that can be self-hosted, operated by govdigital eG, or deployed by certified SCS operators (plusserver, OSISM, Gonicus).

| Criterion | Score | Notes |
|---|---|---|
| Licence openness | 5 | Apache 2.0 / fully open |
| Deployment maturity | 4 | Production in multiple German Länder |
| Community health | 5 | OSBA-backed, growing ecosystem |
| Interoperability | 5 | Open APIs, OCI-compliant containers |
| Security posture | 5 | BSI IT-Grundschutz compatible |
| TCO | 4 | No licence; infrastructure + ops cost |
| Public-sector deployments | 4 | German Länder cloud environments |
| **Weighted score** | **4.60** | |

### 4.10 Accessibility and Inclusion Layer

*New in v0.2.0*

**Function:** Ensure all digital municipal services are accessible to people with disabilities, older adults, and users with limited digital literacy. Meet legal obligations under WCAG 2.1 AA, BITV 2.0, and EN 301 549.

Accessibility is a baseline legal requirement, not an optional feature:

- **BITV 2.0** (Germany): Barrierefreie-Informationstechnik-Verordnung requires WCAG 2.1 AA compliance for federal and Länder public sector websites; most German Länder extend this to municipal level [58]
- **EN 301 549 v3.2.1** (EU): European standard for ICT accessibility referenced by the EU Web Accessibility Directive (2016/2102); mandatory for all EU public sector bodies [58]
- **Swiss P028**: Standard for accessible government websites, based on WCAG 2.1 AA

**Recommended open-source tools:**
- **axe-core** (Deque Systems, MPL-2.0): automated accessibility testing engine; integrates with CI/CD pipelines for regression testing
- **Pa11y**: command-line accessibility testing for automated reporting
- **NVDA** (open-source screen reader): for manual screen reader testing
- **Easy Language (Leichte Sprache)**: simplified versions of key citizen communications for high-impact forms

All procurement specifications for citizen-facing services must include: WCAG 2.1 AA conformance report (ACR, using VPAT template), automated accessibility testing integration, and annual third-party accessibility audit as a service condition.

### 4.11 AI and Automation Tools

*New in v0.2.0*

**Function:** Automate routine administrative tasks; enhance citizen service navigation; support staff in complex decision-making; enable document analysis.

AI tools offer significant productivity potential, but deployment must be managed under the EU AI Act [57]. Municipal AI use cases fall into three regulatory categories:

**High-risk uses** (require conformity assessment under EU AI Act Art. 9):
- AI-assisted benefits eligibility determination
- Risk scoring for inspection prioritisation
- Automated permit processing decisions

**Limited-risk uses** (transparency obligations under Art. 50):
- AI chatbots for citizen information services
- Document summarisation for internal staff
- Meeting transcription and minutes generation

**Minimal-risk uses** (no specific obligations):
- Spam filtering; code generation assistance; translation assistance

**Open-source AI tools appropriate for municipal deployment:**

| Tool | Use case | Licence | AI Act risk |
|---|---|---|---|
| **Ollama + Mistral/Llama3** | On-premises LLM for staff assistance | MIT / Meta Llama 3 | Minimal–Limited |
| **Open WebUI** | Web interface for on-premises LLM | MIT | Minimal |
| **Whisper** (OpenAI) | Meeting transcription | MIT | Minimal |
| **LibreTranslate** | Document translation | AGPLv3 | Minimal |
| **Apache Tika** | Document classification and metadata extraction | Apache 2.0 | Minimal |
| **Tesseract OCR** | Scanned document digitisation | Apache 2.0 | Minimal |

**Critical principle:** All AI tools deployed for functions affecting citizens must maintain human oversight, disclose their AI nature (EU AI Act Art. 50), and be auditable against the municipality's own data. On-premises deployment of open-source LLMs on SCS infrastructure ensures data sovereignty and eliminates data sharing with third-party AI providers.

### 4.12 Reference Architecture

```
+--------------------------------------------------------------+
|                      CITIZEN TOUCHPOINTS                     |
|         TYPO3/Drupal · Decidim · CKAN · Nextcloud           |
|                 (WCAG 2.1 AA / BITV 2.0)                    |
+--------------------------------------------------------------+
|                       AI/AUTOMATION LAYER                    |
|     Ollama+LLM · Whisper · LibreTranslate · Apache Tika     |
+--------------------------------------------------------------+
|                        SERVICE LAYER                         |
|    Camunda Workflows · XÖV/eCH Forms · GeoServer · QGIS     |
+--------------------------------------------------------------+
|                     COLLABORATION LAYER                      |
|    Nextcloud · Matrix/Element · Jitsi · OpenProject          |
+--------------------------------------------------------------+
|                       IDENTITY LAYER                         |
|           Keycloak ↔ BundID / Swiss eID / GovStack           |
+--------------------------------------------------------------+
|                    INFRASTRUCTURE LAYER                      |
|    Sovereign Cloud Stack · Kubernetes · PostgreSQL · Ceph    |
+--------------------------------------------------------------+
```

All layers communicate via open APIs. Container orchestration uses Kubernetes [39]; relational persistence uses PostgreSQL [41]; both run on the Sovereign Cloud Stack. Data exchange uses XÖV standards (Germany) [46] or eCH standards (Switzerland) [47]. Security is governed by BSI IT-Grundschutz [26]; NIS2 requirements apply to critical infrastructure components [27]. AI tools at the automation layer are subject to EU AI Act requirements [57].

---

## 5. Case Studies

*New section in v0.2.0*

Six cases are examined: four successful deployments at varying scales, one emerging large-scale initiative, and one cautionary reversal.

### 5.1 Barcelona: Decidim and the Open-Source Digital City

**Context:** Barcelona (population ~1.6 million) launched the Decidim participatory democracy platform in 2016 under the Barcelona Digital City Plan 2016–2020, directed by Technology Director Francesca Bria [56].

**Implementation:** Decidim was deployed as the primary platform for the city's participatory budgeting process, enabling citizens to propose, debate, and vote on projects for approximately €75M of annual city budget. The platform was open-sourced from inception; the Decidim Association was established in 2021 to govern the platform as a commons.

**Results:**
- 48,000+ registered users within two years
- 1,000+ budget proposals generated in the first cycle
- Platform adopted by Catalan regional government, Canton of Schaffhausen, and 400+ entities globally
- Operational cost estimated at <€500K/year [56]

**Key lessons:** Open-source publication created global network effects with contributors. Executive-level political championship was decisive. Starting with a single high-profile use case (participatory budgeting) built momentum before expanding.

### 5.2 German Federal OpenDesk: Scaling Open-Source Workplace

**Context:** The German Federal Government's OpenDesk programme, launched 2023 and managed by ZenDiS GmbH, aims to provide a fully open-source digital workplace for federal employees [42, 51].

**Implementation:** OpenDesk integrates Nextcloud, CryptPad, OpenProject, Jitsi Meet, Element, and Collabora Office into a single managed suite. Initial deployment began with pilot groups in 2023; broader rollout is planned for 2024–2026.

**Lessons for municipalities:**
- OpenDesk's component architecture means municipalities can adopt individual components without committing to the full suite
- ZenDiS's procurement framework and support contracts can be adopted by municipalities, dramatically reducing procurement effort
- The federal deployment provides a reference implementation that municipalities can cite in internal approval processes

### 5.3 Canton of Schaffhausen: Decidim for Cantonal Democracy

**Context:** The Canton of Schaffhausen (population ~85,000) was among the first Swiss cantons to deploy Decidim for cantonal-level participation [12].

**Implementation:** Deployed with German-language customisation and cantonal identity management integration. Use cases include Vernehmlassungen (consultation processes), spatial planning participation, and online petitions.

**Lessons:** Swiss federalism creates a natural testing ground with distinct legal and linguistic requirements. German-language customisations and Swiss-specific configurations are reusable across other cantons and German municipalities.

### 5.4 Schleswig-Holstein: Linux Desktop at Länder Scale

**Context:** In January 2024, Schleswig-Holstein (population ~2.9 million, ~25,000 state employees) announced plans to transition from Windows/Microsoft Office to Linux and LibreOffice, projecting €30M in savings over 10 years [54].

**Significance:** The largest committed open-source desktop transition in German state government since Munich LiMux. Unlike Munich, Schleswig-Holstein's approach incorporates explicit lessons from the LiMux reversal: cross-party political mandate, phased rollout, designated change management budget, and alignment with openCode.de and OZG 2.0 from the outset.

**Status (mid-2026):** Pilot phase underway with selected departments; expanding to broader rollout based on pilot feedback.

**Lessons:** Political framing as a cost-saving and digital-sovereignty measure built cross-party support. Alignment with national frameworks reduces the risk of political reversal.

### 5.5 Moers: A Small City's Long-Term Commitment

**Context:** Moers, North Rhine-Westphalia (population ~103,000), has operated open-source software on municipal computers since 2001 — one of Germany's longest-running municipal deployments [62].

**Implementation:** Ubuntu Linux on city computers, LibreOffice for office software, growing stack of open-source administrative applications. Through multiple changes in city leadership and Microsoft promotional campaigns, the commitment has been maintained.

**Key lessons:**
- Long-term cost advantage compounds: after initial transition investment, open-source avoids recurring licence upgrade cycles
- Small cities can succeed; scale does not determine viability
- Successful integration with state and federal systems over 24 years directly counters the Munich compatibility argument

### 5.6 Munich LiMux: The Cautionary Case

**Context:** Munich began migrating 15,000+ computers to Ubuntu Linux ("LiMux") in 2003. In 2017 a new city council voted to return to Microsoft [30, 55].

**Four primary causes of reversal:**
1. No cross-party political covenant protected the project from a coalition change with closer Microsoft ties
2. Insufficient training investment and documented end-user resistance were inadequately addressed
3. Some state-level systems assumed Windows environments; workarounds created friction
4. Successful vendor lobbying including a Munich campus opening and promotional pricing

**What worked:** The technical migration was broadly successful for 14 years. The failure was political and organisational, not technical.

**Key lessons:** Technical success is necessary but not sufficient. A cross-party legislative mandate is more durable than an executive decision. Vendor lobbying is predictable; communications planning and civil society engagement are the mitigations.

### 5.7 Cross-Case Success Factors

| Factor | Evidence |
|---|---|
| Executive political champion | Barcelona (mayor), Schleswig-Holstein (minister), Moers (continuity) |
| Cross-party mandate | Schleswig-Holstein; absent in Munich |
| Community engagement | Barcelona Decidim, Schaffhausen participatory processes |
| High-impact, low-risk first step | Barcelona (participatory budgeting); all cases (email before desktop) |
| Phased rollout with decision gates | All successful cases |
| Upstream contribution | Barcelona (Decidim Association), Germany (openCode.de) |
| Transparency of costs and progress | Barcelona (published costs), Schleswig-Holstein (public savings projections) |

---

## 6. Implementation Roadmap

### 6.1 Standard Pathway (50,000–500,000 population)

#### Phase 0: Foundation (Months 1–3)

**Objective:** Establish governance, assess current state, build the coalition.

**Deliverables:**
- Digital Transformation Steering Committee established (city leadership + IT + civil society)
- Current-state technology audit completed (vendor list, licence costs, integration dependencies)
- Stakeholder engagement plan adopted
- Memorandum of Understanding with cooperative IT provider (Dataport, AKDB, govdigital eG, or equivalent)
- Baseline accessibility audit of all existing digital services

**Budget range:** €80,000–€200,000

**Success criteria:**
- Political mandate secured (council resolution, publicly announced)
- Budget envelope approved
- Dedicated project lead appointed (minimum 80% FTE)

#### Phase 1: Identity and Infrastructure (Months 4–12)

**Objective:** Stand up the foundational layers.

**Deliverables:**
- Sovereign Cloud Stack environment operational (own or certified SCS hoster)
- Keycloak deployed and federated with national identity system
- Nextcloud baseline deployment for internal collaboration
- Matrix/Element messaging for staff
- BSI IT-Grundschutz baseline documentation complete
- Accessibility testing pipeline established (axe-core, Pa11y in CI/CD)

**Budget range:** €150,000–€400,000

**Success criteria:**
- 100% of IT staff authenticate via Keycloak SSO
- File storage migrated from proprietary cloud to Nextcloud
- Security baseline approved by municipal data protection officer

#### Phase 2: Services and Workflows (Months 10–18)

**Objective:** Migrate the first five citizen-facing services to open infrastructure.

**Deliverables:**
- Five highest-volume administrative services on Camunda/XÖV-eCH stack
- TYPO3 or Drupal CMS migration complete with WCAG 2.1 AA audit
- Open data portal (CKAN) with first 20 datasets
- Decidim instance for first participatory process
- On-premises AI tools for staff assistance (Ollama + model)

**Budget range:** €200,000–€600,000

**Success criteria:**
- 80% of target service volume processed without regression
- WCAG 2.1 AA conformance achieved on public website
- Open data portal live and indexed on opendata.swiss / GovData.de

#### Phase 3: Integration and Extension (Months 16–24)

**Objective:** Integrate all layers; extend coverage to 80% of transactions.

**Deliverables:**
- All services federated via Keycloak SSO
- Nextcloud integrated with document management workflows
- GIS layer operational (QGIS + GeoServer)
- 80% of administrative services digitised
- Inter-agency data exchange via XÖV/eCH operational

**Budget range:** €250,000–€700,000

#### Phase 4: Optimisation and Community (Months 22–30)

**Deliverables:**
- Citizen satisfaction survey (target NPS > 40)
- First contribution to openCode.de or upstream projects
- Municipal open-source community of practice with ≥3 peer municipalities
- AI Act compliance audit for all AI-assisted services

**Budget range:** €100,000–€300,000

#### Phase 5: Sovereignty and Scale (Months 28–36)

**Deliverables:**
- Complete licence compliance audit and Software Bill of Materials
- Sovereign data residency verified (100% on SCS/sovereign infrastructure)
- Replication playbook published on openCode.de
- Strategy paper updated to v1.0 with implementation evidence

**Budget range:** €80,000–€200,000

**Total programme investment:** €860,000–€2,400,000 over 36 months. For reference: annual Microsoft 365 licensing for a city of 1,000 employees at €300/user/year is €900,000 annually — the open-source transition pays back within the programme timeline.

### 6.2 Small Municipality Pathway (5,000–50,000 population)

**Step 1 (Month 1–2):** Join govdigital eG or cantonal cooperative. Purchase managed SCS hosting under framework contract.

**Step 2 (Month 2–6):** Deploy managed Nextcloud for staff. Replace proprietary file sharing.

**Step 3 (Month 4–9):** Migrate public website to TYPO3 or Drupal (WCAG 2.1 AA template). Launch CKAN with 10 datasets.

**Step 4 (Month 8–15):** Deploy Keycloak federated with BundID/Swiss eID. Launch three citizen services on open platform.

**Step 5 (Month 12–24):** Deploy Decidim for one participatory process per year. Join regional open-source community of practice.

**Realistic budget for a municipality of 20,000:** €60,000–€120,000 for the full 24-month programme; €15,000–€30,000 per year thereafter. Annual licence savings from ending Microsoft 365 and proprietary document management: approximately €50,000–€100,000 depending on seat count.

See Appendix A for a detailed checklist.

---

## 7. Stakeholder and Procurement Strategy

### 7.1 Stakeholder Map

| Stakeholder | Primary interest | Engagement approach |
|---|---|---|
| Mayor / Executive | Political success, cost, citizen approval | Executive briefing, progress dashboard |
| City council | Oversight, democratic legitimacy | Quarterly reports, open council sessions |
| City IT team | Technical feasibility, workload | Co-design, training, community membership |
| Procurement office | Legal compliance, risk | Framework agreements, legal briefings |
| Civil servants (end users) | Ease of use, reliability | UX testing, change management, training |
| Citizens | Service quality, privacy | Participatory design (Decidim), transparency dashboard |
| Civil society / NGOs | Transparency, access, participation | Decidim platform, public roadmaps |
| Data protection officer | GDPR/nDSG compliance | Privacy-by-design at each phase |
| Open-source communities | Contribution, reuse | openCode.de, upstream contribution |
| Sovereign technology providers | Partnership, deployment | SCS certified partner agreements |

### 7.2 Procurement Framework

Five core principles for open-source procurement:

**1. Procure services, not licences.** Open-source software carries zero licence cost; municipalities pay for implementation, hosting, support, customisation, and training.

**2. Use cooperative procurement structures.** govdigital eG (Germany) and Swiss cantonal IT cooperatives provide framework agreements satisfying procurement law requirements [23].

**3. Apply the "Public Money? Public Code!" principle.** All custom software developed under contract must be released under an OSI-approved licence and published on openCode.de. This must be a contractual condition [4].

**4. Evaluate total cost of ownership.** Procurement scoring must include a 5-year TCO model: implementation, hosting, training, support, integration, and exit costs.

**5. Require interoperability standards.** All procured systems must implement XÖV (Germany) [46], eCH (Switzerland) [47], DCAT-AP (EU open data), OGC standards (GIS), and EU AI Act transparency requirements for AI components [57].

### 7.3 German Vergaberecht Specifics

German public procurement is governed by GWB (Part 4), VgV, and UVgO. Key thresholds for IT services (2024):

| Threshold | Procedure |
|---|---|
| < €25,000 | Direktvergabe (direct award) |
| €25,000–€221,000 | Verhandlungsverfahren (UVgO) |
| > €221,000 (EU threshold) | Offenes Verfahren (EU-wide) |

**For framework agreements:** Joint procurement through govdigital eG, AKDB, or Dataport under §108 GWB (in-house procurement) eliminates competitive tender requirements for member municipalities. This is the recommended path for standard SCS hosting, Nextcloud, and Matrix deployments.

**For custom development:** Above the EU threshold, an EU-wide Offenes Verfahren is required. Include the "Public Money? Public Code!" open-source publication requirement as a technical specification (not an award criterion, to avoid legal challenge), and require GovStack-compatible API design.

### 7.4 Swiss Procurement Law Specifics (BöB / IVöB)

Swiss public procurement is governed by BöB (SR 172.056.1) at federal level and IVöB at cantonal/municipal level. WTO GPA thresholds (2024): CHF 270,000 (federal) or CHF 430,000 (cantonal/municipal).

**Key Swiss specifics:**
- "Bestbieter-Prinzip" (best-value principle) must be applied; lowest-price procurement is not permitted for complex IT services
- Open-source preferencing can be expressed as a technical specification criterion ("the system must be licensed under an OSI-approved licence") without violating WTO GPA non-discrimination rules
- The EMBAG principle provides strong policy basis for including open-source requirements in cantonal and municipal procurement despite not being directly binding at those levels [1]

### 7.5 Change Management

Open-source transitions most frequently fail not on technical grounds but on human factors: end-user resistance, insufficient training, middle-management inertia, and political backsliding under vendor pressure (confirmed by Munich LiMux [55]).

**Core recommendations:**
- Appoint a **Digital Transformation Champion** at political level with multi-year public commitment
- Embed **open-source champions** in each department with advanced training and peer support role
- Run **parallel operations** for minimum three months before cutting over critical systems
- Document and publicly celebrate **early wins**
- Publish a **public transparency dashboard** showing migration progress, costs, and service quality metrics

---

## 8. Risk Analysis

### 8.1 Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Political reversal after election | Medium | High | Embed in legislation; cross-party consensus |
| Vendor lobbying / FUD campaigns | High | Medium | TCO evidence; civil society engagement; publicise mandate |
| Skill gap in IT team | High | Medium | Training; cooperative IT partner; community of practice |
| Integration failure between layers | Medium | High | Phased rollout; reference architecture; integration testing |
| Data loss during migration | Low | Critical | Full backup; parallel operation; staged migration; tested restore |
| GDPR / nDSG violation | Low | High | Privacy-by-design; DPIA; DPO sign-off |
| EU AI Act non-compliance | Medium | Medium | Risk classification; conformity assessment for high-risk uses |
| User adoption failure | Medium | High | Change management; UX testing; training; feedback loops |
| Security incident | Low | Critical | BSI IT-Grundschutz; penetration testing; SBOM; incident response |
| Cost overrun | Medium | Medium | Phase-gated budget; independent project office; open TCO |
| Federal/Land system compatibility | Medium | Medium | Dependency audit in Phase 0; compatibility layer |

### 8.2 The Munich Cautionary Case

See Section 5.6. Applied as risk mitigations: cross-party mandate before commitment; change management budget equal to technical budget; vendor compatibility audit in Phase 0; civil society engagement as political anchor.

### 8.3 Security Requirements

BSI IT-Grundschutz provides a comprehensive security baseline [26]. Key requirements:

- Regular security updates with documented patch management (maximum 72-hour critical patch cycle)
- Authentication at BSI AAL2 for citizen-facing services
- Data in transit: TLS 1.3 minimum; HSTS enforced; automated certificate management
- Data at rest: encrypted for all personal data categories; HSM-backed key management for highly sensitive data
- Penetration testing at each phase gate by a BSI-qualified tester
- Software Bill of Materials (SBOM) with automated CVE scanning
- NIS2-compliant incident response plan with 72-hour mandatory reporting [27]
- Annual third-party security audit aligned with ISO 27001

### 8.4 Data Protection and Privacy

- **Data Protection Impact Assessments (DPIA)** required for all new citizen-facing services and AI tools processing personal data (GDPR Art. 35; Swiss revDSG equivalent). DPO must sign off before production deployment.
- **Data residency:** All personal data must be stored on SCS/sovereign infrastructure within EU/EEA territory (Switzerland is adequate under GDPR).
- **Third-party processors:** All cloud providers must execute a Data Processing Agreement (DPA) per GDPR Art. 28. SCS-certified hosters provide standardised DPAs.
- **Retention schedules:** Document management systems must enforce statutory retention schedules automatically.
- **Right to erasure:** Systems must support GDPR Art. 17 erasure requests within 30 days.

### 8.5 EU AI Act Compliance

For municipalities deploying AI tools (Section 4.11):

1. **Risk classification** of every AI tool before deployment (Art. 9)
2. **High-risk system registration** in the EU database (Art. 71) before deployment
3. **Technical documentation** per Annex IV for high-risk systems
4. **Human oversight mechanisms** (Art. 14): a human must be able to override any AI-assisted decision affecting citizens
5. **Transparency disclosure** to citizens (Art. 50): AI chatbots must disclose their AI nature
6. **Incident reporting** for serious AI incidents to the national supervisory authority

Open-source AI systems are generally easier to comply with these requirements than proprietary black-box systems, as technical documentation, training data description, and model auditing are inherently possible.

---

## 9. Conclusion

The evidence reviewed in this paper — academic literature, policy analysis, technology assessment, and six case studies — converges on four findings:

**1. Open-source municipal technology stacks are technically mature, production-proven, and fully capable.** Every functional requirement of a modern municipal government can be met by open-source software with documented deployments, from small towns (Moers, 24 years) to large cities (Barcelona) to federal governments (Germany, Switzerland). The v0.2.0 extension to AI tools and accessibility confirms this maturity extends to emerging requirement areas.

**2. The regulatory environment increasingly mandates open-source and interoperability — and the mandate is binding.** EMBAG (Switzerland), OZG 2.0 (Germany), the Interoperable Europe Act, the EU Data Act, and the EU AI Act together create a legal environment that proprietary, vendor-locked systems cannot sustainably satisfy. Municipalities that begin the transition now build compliance capital; those that delay accumulate regulatory debt requiring a more expensive, more disruptive forced migration.

**3. The economic case is compelling when total costs are counted correctly.** Open-source stacks eliminate per-seat licence costs and reduce vendor lock-in risk. Schleswig-Holstein projects €30M in savings over 10 years. Barcelona operates a participatory platform serving 48,000 citizens at under €500K/year. The Munich LiMux reversal cost — never disclosed — is estimated to exceed the original migration investment.

**4. Success requires equal investment in the political, organisational, and technical dimensions.** Barcelona's mayor championed Decidim; Schleswig-Holstein secured cross-party backing before committing; Moers maintained its commitment through 24 years of political change. Munich reversed a technically successful migration because political insulation was insufficient. The binding constraint is not code quality — it is the ability to sustain political will through elections, budget cycles, and vendor pressure.

Cities that move first will benefit from first-mover advantages: shaping cooperative standards, building in-house expertise, attracting open-source talent, and contributing to the digital commons that all municipalities share. The legal mandates, the fiscal case, the democratic argument, and the case study evidence all point in the same direction. The invitation is open.

---

## Appendix A: Quick Start Checklist for Small Municipalities

For municipalities with population < 50,000 and limited internal IT capacity.

**Prerequisites:**
- [ ] Political mandate from mayor and council (recorded resolution)
- [ ] Dedicated project coordinator identified
- [ ] govdigital eG or cantonal IT cooperative membership confirmed
- [ ] Current IT costs documented (all software licences, hosting, support)

**Months 1–3: Foundation**
- [ ] Join managed SCS hosting via cooperative framework contract
- [ ] Document all software licence expiry dates
- [ ] Conduct baseline accessibility audit of public website
- [ ] Sign Data Processing Agreements with new providers

**Months 2–6: Collaboration**
- [ ] Deploy managed Nextcloud for staff file sharing
- [ ] Deploy Matrix/Element for staff messaging (or Nextcloud Talk)
- [ ] Train all staff on new tools (2 half-days per person)
- [ ] Appoint department-level open-source champions

**Months 4–9: Web and Open Data**
- [ ] Migrate public website to TYPO3 or Drupal (WCAG 2.1 AA template)
- [ ] Publish first 10 datasets on open data portal
- [ ] Connect to cantonal / national open data catalogue (opendata.swiss / GovData.de)

**Months 8–18: Services and Identity**
- [ ] Deploy Keycloak federated with BundID / Swiss eID
- [ ] Migrate three highest-volume citizen services to open platform
- [ ] Launch first Decidim participatory process

**Months 18–24: Completion**
- [ ] Conduct citizen satisfaction survey
- [ ] Publish TCO comparison (estimate vs. actuals)
- [ ] Join regional open-source community of practice
- [ ] Publish one dataset or configuration on openCode.de

**Ongoing:**
- [ ] Quarterly review of source registry (use `Scripts/update_literature_review.py`)
- [ ] Annual accessibility audit
- [ ] Annual security update review (BSI IT-Grundschutz baseline)

---

## Appendix B: Procurement Language Templates

**B.1 Open-Source Publication Requirement**

> *"All software developed or substantially modified under this contract, and all configuration templates, automation scripts, and data schemas produced for the contracting authority, shall be released under an OSI-approved open-source licence (https://opensource.org/licenses) no later than 30 days after first production deployment. The contractor shall publish these materials on openCode.de or an equivalent national public repository specified by the authority. Source code must be published with a README, licence file, and sufficient documentation for a competent third party to build, test, and deploy the software independently."*

**B.2 Data Portability and Exit Rights**

> *"On termination or expiry of this contract, the contractor shall provide all data in open, machine-readable formats (CSV, JSON, XML, SQL dump as appropriate) within 30 calendar days of written request, at no additional charge. No technical or contractual measures shall prevent the authority from migrating to alternative services. The contractor shall provide documented migration procedures and reasonable migration support as specified in Schedule [X]."*

**B.3 Interoperability Requirements**

> *"All systems delivered under this contract must implement the following open standards: XÖV standards for the relevant service area (Germany) / eCH standards for the relevant service area (Switzerland); DCAT-AP [current version] for any data catalogue functionality; OpenID Connect 1.0 and OAuth 2.0 for authentication and authorisation; OGC WMS/WFS for any geographic data services; REST or GraphQL APIs with complete OpenAPI documentation for all machine-readable interfaces."*

**B.4 AI Transparency and Human Oversight**

> *"Any AI components included in or added to the delivered systems shall: (a) be disclosed in writing to the authority prior to deployment; (b) be classified under the EU AI Act (Regulation (EU) 2024/1689) risk framework with classification documented; (c) for high-risk AI systems, comply with all requirements of Title III, Chapter 3 including technical documentation, accuracy metrics, and human oversight mechanisms; (d) for AI systems generating text or images interacting with end users, display a clear disclosure that the content is AI-generated (Art. 50 EU AI Act)."*

---

## References

[1] Swiss Federal Council. (2023). *Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG)*. SR 172.019. https://www.fedlex.admin.ch/eli/cc/2023/682/de [CC0; verified 2026-06-21]

[2] Bundesministerium des Innern und für Heimat (BMI). (2024). *Onlinezugangsgesetz 2.0 (OZG 2.0)*. https://www.bmi.bund.de/DE/themen/moderne-verwaltung/e-government/ozg/ozg-node.html [DL-DE/Zero 2.0; verified 2026-06-21]

[3] Open Source Business Alliance (OSBA). (2023). *Sovereign Cloud Stack*. https://scs.community/ [CC-BY-SA-4.0; verified 2026-06-21]

[4] Free Software Foundation Europe (FSFE). (2017). *Public Money? Public Code!* https://publiccode.eu/ [CC-BY-SA-4.0; verified 2026-06-21]

[5] European Commission. (2020). *Open Source Software Strategy 2020–2023: Think Open*. https://commission.europa.eu/about/departments-and-executive-agencies/informatics/open-source-software-strategy_en [Open access; verified 2026-06-21]

[6] European Parliament and Council. (2024). *Regulation (EU) 2024/903 — Interoperable Europe Act*. OJ L 903, 11 April 2024. CELEX 32024R0903. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R0903 [EU legislation; verified 2026-06-21]

[7] Wirtz, B.W., & Weyerer, J.C. (2017). Conceptualization and creation of a holistic e-government maturity model. *Public Management Review*, 19(9), 1297–1316. https://doi.org/10.1080/14719037.2017.1283024

[8] Janssen, M., Charalabidis, Y., & Zuiderwijk, A. (2012). Benefits, adoption barriers and myths of open data and open government. *Information Systems Management*, 29(4), 258–268. https://doi.org/10.1080/10580530.2012.716740

[9] FITKO. (2023). *Föderale IT-Kooperation — Jahresbericht 2023*. https://www.fitko.de/ueber-fitko/jahresbericht/ [DL-DE/Zero 2.0; verified 2026-06-21]

[10] openCode.de. (2022). *openCode — Open Source for Government*. https://opencode.de/ [Open access; verified 2026-06-21]

[11] Sovereign Cloud Stack Community. (2023). *SCS Technical Documentation*. https://docs.scs.community/ [Apache 2.0; verified 2026-06-21]

[12] Decidim Association. (2021). *Decidim: Free Open-Source Participatory Democracy*. https://decidim.org/ [AGPL-3.0; verified 2026-06-21]

[13] Nextcloud GmbH. (2023). *Nextcloud for Government*. https://nextcloud.com/government/ [Open access; verified 2026-06-21]

[14] The Matrix Foundation. (2023). *Matrix Specification v1.x*. https://spec.matrix.org/ [Apache 2.0; verified 2026-06-21]

[16] E-Government Suisse. (2023). *Strategie E-Government Schweiz 2024–2027*. https://www.egovernment.ch/de/umsetzung/e-government-strategie/ [Open access; verified 2026-06-21]

[19] TYPO3 Association. (2023). *TYPO3 in Public Administration*. https://typo3.org/project/association [Open access; verified 2026-06-21]

[20] OpenProject GmbH. (2023). *OpenProject for Government*. https://www.openproject.org/ [GPLv3; verified 2026-06-21]

[21] Red Hat / Keycloak Community. (2023). *Keycloak: Open Source Identity and Access Management*. https://www.keycloak.org/ [Apache 2.0; verified 2026-06-21]

[22] CKAN Association. (2023). *CKAN: Open Source Data Portal Software*. https://ckan.org/ [AGPL-3.0; verified 2026-06-21]

[23] govdigital eG. (2023). *govdigital: Genossenschaft für digitale Verwaltung*. https://govdigital.de/ [Open access; verified 2026-06-21]

[24] Dataport AöR. (2023). *Dataport: IT-Dienstleister für die öffentliche Verwaltung*. https://www.dataport.de/ [Open access; verified 2026-06-21]

[26] Bundesamt für Sicherheit in der Informationstechnik (BSI). (2023). *BSI IT-Grundschutz-Kompendium Edition 2023*. https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/IT-Grundschutz-Kompendium/it-grundschutz-kompendium_node.html [CC-BY-ND 3.0 DE; verified 2026-06-21]

[27] European Parliament and Council. (2022). *Directive (EU) 2022/2555 — NIS2*. CELEX 32022L2555. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022L2555 [EU legislation; verified 2026-06-21]

[29] United Nations DESA. (2022). *UN E-Government Survey 2022*. https://publicadministration.un.org/egovkb/en-us/Reports/UN-E-Government-Survey-2022 [Open access; verified 2026-06-21]

[30] Janowski, T. (2015). Digital government evolution: From transformation to contextualization. *Government Information Quarterly*, 32(3), 221–226. https://doi.org/10.1016/j.giq.2015.07.001

[33] Camunda Services GmbH. (2023). *Camunda Platform 8 Community Edition*. https://camunda.com/download/ [Apache 2.0; verified 2026-06-21]

[34] BigBlueButton Inc. (2023). *BigBlueButton: Open Source Web Conferencing*. https://bigbluebutton.org/ [LGPL-3.0; verified 2026-06-21]

[35] Jitsi Community. (2023). *Jitsi Meet: Open Source Video Conferencing*. https://jitsi.org/ [Apache 2.0; verified 2026-06-21]

[36] OpenStreetMap Foundation. (2023). *OpenStreetMap*. https://www.openstreetmap.org/ [ODbL-1.0; verified 2026-06-21]

[37] QGIS Project. (2023). *QGIS: A Free and Open Source Geographic Information System*. https://www.qgis.org/ [GPL-2.0+; verified 2026-06-21]

[39] Cloud Native Computing Foundation (CNCF). (2023). *Kubernetes*. https://kubernetes.io/ [Apache 2.0; verified 2026-06-21]

[41] PostgreSQL Global Development Group. (2023). *PostgreSQL*. https://www.postgresql.org/ [PostgreSQL Licence; verified 2026-06-21]

[42] BMI / ZenDiS GmbH. (2023). *OpenDesk: Der digitale Arbeitsplatz der Bundesverwaltung*. https://opendesk.eu/ [AGPL-3.0; verified 2026-06-21]

[43] Schweizerisches Bundesarchiv (BAR). (2023). *GEVER in der Bundesverwaltung*. https://www.bar.admin.ch/bar/de/home/digitale-archivierung/gever.html [Open access; verified 2026-06-21]

[44] opendata.swiss. (2023). *Open Government Data Switzerland*. https://opendata.swiss/ [CC-BY-4.0 portal; verified 2026-06-21]

[45] European Commission. (2017). *European Interoperability Framework (EIF)*. https://joinup.ec.europa.eu/collection/nifo-national-interoperability-framework-observatory/european-interoperability-framework-detail [CC-BY-4.0; verified 2026-06-21]

[46] KoSIT. (2023). *XÖV-Standards: XML in der öffentlichen Verwaltung*. https://www.xoev.de/ [Open access; verified 2026-06-21]

[47] eCH Verein. (2023). *eCH-Standards für E-Government in der Schweiz*. https://www.ech.ch/ [Open access; verified 2026-06-21]. Key standards: eCH-0046 (digital delivery), eCH-0099 (identity federation), eCH-0115 (open government data).

[48] CONSUL Democracy Foundation. (2023). *CONSUL Democracy: Open Source Citizen Participation Software*. https://consuldemocracy.org/ [AGPL-3.0; verified 2026-06-21]

[49] ITU / DIAL. (2023). *GovStack Initiative: Building Blocks for Government Digital Services*. https://www.govstack.global/ [Open access; verified 2026-06-21]

[50] European Parliament and Council. (2023). *Regulation (EU) 2023/2854 — EU Data Act*. OJ L 2023/2854, 22 December 2023. CELEX 32023R2854. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023R2854 [EU legislation; verified 2026-06-21]

[51] ZenDiS GmbH. (2023). *Zentrum für Digitale Souveränität der öffentlichen Verwaltung*. https://zendis.de/ [Open access; verified 2026-06-21]

[52] EU Open Source Observatory (OSOR) / Joinup. (2023). *Open Source in the European Public Sector — Annual Report 2023*. https://joinup.ec.europa.eu/collection/open-source-observatory-osor [CC-BY-4.0; verified 2026-06-21]

[53] Lathrop, D., & Ruma, L. (Eds.). (2010). *Open Government: Collaboration, Transparency, and Participation in Practice*. Sebastopol, CA: O'Reilly Media. ISBN 978-0-596-80435-0.

[54] Staatskanzlei Schleswig-Holstein. (2024). *Digitale Souveränität: Schleswig-Holstein setzt auf Open Source*. https://www.schleswig-holstein.de/DE/landesregierung/ministerien-behoerden/StK/Schwerpunkte/OpenSource/openSource_node.html [Open access; verified 2026-06-21]

[55] Koch, F. (2018). LiMux — ein Rück- und Ausblick. *Linux-Magazin*. https://www.linux-magazin.de/ausgaben/2018/01/limuex/ See also: Landeshauptstadt München. (2017). Stadtratsbeschluss S-02806-KVR-07573. [Public record]

[56] Ajuntament de Barcelona. (2020). *Barcelona Digital City Plan 2016–2020: Results and Next Steps*. https://ajuntament.barcelona.cat/digital/en/digital-innovation/city-os-and-urban-data/digital-city-plan-2016-2020 [CC-BY-4.0; verified 2026-06-21]

[57] European Parliament and Council. (2024). *Regulation (EU) 2024/1689 — Artificial Intelligence Act*. OJ L 2024/1689, 12 July 2024. CELEX 32024R1689. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689 [EU legislation; verified 2026-06-21]

[58] ETSI. (2021). *EN 301 549 v3.2.1: Accessibility Requirements for ICT Products and Services*. https://www.etsi.org/deliver/etsi_en/301500_302000/301549/03.02.01_60/en_301549v030201p.pdf [Open access]. See also: Bundesministerium des Innern. (2011, amended 2019). *Barrierefreie-Informationstechnik-Verordnung (BITV 2.0)*. https://www.gesetze-im-internet.de/bitv_2_0/ [CC0; verified 2026-06-21]

[59] Gaia-X AISBL. (2024). *Gaia-X Annual Report 2024*. https://gaia-x.eu/ [Open access; verified 2026-06-21]

[60] Bundesministerium des Innern und für Heimat (BMI). (2023). *BundesMessenger: Sichere Kommunikation für die Bundesverwaltung*. https://messenger.bund.de/ [Open access; verified 2026-06-21]

[61] KGSt. (2022). *Digitale Transformation in Kommunen: Reifegradmodell und Handlungsempfehlungen*. Köln: KGSt. https://www.kgst.de/ [KGSt member publication]

[62] Stadtverwaltung Moers. (2023). *Open Source in der Stadtverwaltung Moers*. https://www.moers.de/de/rathaus/open-source/ [Open access; verified 2026-06-21]

---

*Released under CC-BY-4.0. Attribute as: Sebastian Graf, Autonomous Office of Civil Digital Infrastructure (sebk4c@tuta.com)*  
*Version 0.2.0 — Citation-Complete Draft — 2026-06-21*  
*Source of truth: English · Translation: Deutsch*  
*Repository: https://github.com/SEBK4C/Strategy-for-City-GovTech*
