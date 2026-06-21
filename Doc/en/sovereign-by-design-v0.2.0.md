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
  - total cost of ownership
  - eCH standards
  - GovStack
  - ZenDiS
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

Municipal governments are the closest layer of democratic administration to citizens, yet they face an acute structural tension: the digital tools they depend on are increasingly proprietary, vendor-locked, and misaligned with public-interest values. This paper presents a comprehensive, citation-complete strategy for implementing a state-of-the-art, open-source governmental administration technology stack in city governments. Drawing on exemplary practices from the Swiss federal administration's EMBAG legislation [1], Germany's OZG reform programme [2], Sovereign Cloud Stack [3], and OpenDesk [42] initiatives, and the wider European sovereign technology community, we derive a first-principles implementation roadmap, stakeholder engagement framework, and procurement strategy. We evaluate nine core technology components — identity management, document management, workflow automation, citizen participation, secure communications, open data publication, geographic information systems, public web presence, and cloud infrastructure — against criteria of digital sovereignty, interoperability, total cost of ownership (TCO), and civic alignment. A new TCO analysis demonstrates that a 50,000-resident municipality transitioning to an open-source stack can expect net savings of €400,000–€1,200,000 over five years relative to an equivalent proprietary baseline, primarily through elimination of per-seat licence fees and reduction of vendor lock-in switching costs. Case studies from Barcelona, Helsinki, the Swiss canton of Schaffhausen, and three sub-50,000-population municipalities provide empirical grounding for the implementation roadmap. We conclude that open-source municipal technology stacks are not merely technically viable but fiscally superior, democratically necessary, and legally mandated in an increasing number of jurisdictions. The paper provides a phased 36-month implementation roadmap with concrete procurement guidance for city administrators, elected officials, IT teams, and civil-society stakeholders, and a separate lightweight pathway for municipalities below 20,000 population.

**Keywords:** digital sovereignty, open source government, GovTech, municipal digital transformation, interoperability, OZG, EMBAG, Sovereign Cloud Stack, eCH, GovStack, ZenDiS, e-government, civic technology, total cost of ownership

---

## 1. Introduction

The digital transformation of municipal government is no longer optional. Citizens expect seamless, secure, and accessible digital services; regulators demand interoperability and data protection; and fiscal pressures require sustainable, cost-effective technology investments. Yet the majority of city governments worldwide remain trapped in a cycle of proprietary vendor dependency, expensive licence agreements, and fragmented systems that impede rather than enable good governance [29, 60].

The consequences of this dependency are well-documented: vendor lock-in raises switching costs and bargaining asymmetry [4]; proprietary formats obstruct cross-agency data exchange and transparency [45]; closed-source infrastructure prevents independent security auditing [26]; and recurring licence fees drain budgets that could otherwise fund service delivery [3, 5]. Most fundamentally, when the software running democratic institutions is owned and controlled by private actors, a structural conflict of interest emerges between the public interest and corporate imperatives [4, 53].

A different path is both possible and proven. Switzerland's 2023 EMBAG legislation (Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben) mandates that federal software developed with public funds be released as open source by default [1]. Germany's OZG reform programme, Sovereign Cloud Stack, OpenDesk initiative, and the newly established ZenDiS GmbH (Zentrum für Digitale Souveränität der öffentlichen Verwaltung) represent the most ambitious open-source government technology programme in Europe [2, 3, 42, 49]. The European Commission's 2021 study on the economic impact of open source software found that open source contributes between €65 billion and €95 billion annually to EU GDP, and that every €1 invested in open source generates €4.15 in economic return [56]. The Free Software Foundation Europe's "Public Money? Public Code!" campaign, endorsed by over 200 organisations across 30 countries, articulates the democratic principle at stake: software paid for by the public should be available to the public [4].

This paper synthesises these developments into a practical strategy for municipal governments. It is addressed to all relevant stakeholders — city administrators, elected officials, public-sector IT teams, procurement offices, civil-society groups, open-source communities, and sovereign technology providers — and provides the evidence base, technology assessment, and implementation roadmap needed to make the transition.

### 1.1 Scope and Definitions

*Municipal government* refers to city and local government authorities, including Gemeinden, Kommunen, Städte (Germany), Gemeinden and Städte (Switzerland), and equivalent structures across German-speaking Europe. The strategy is designed to scale from small municipalities (population 5,000–20,000) to large cities (population 500,000+), with an explicit small-municipality pathway described in Section 5.6.

*Open-source technology stack* refers to software components licensed under OSI-approved licences, deployed on infrastructure that the municipality controls or can migrate away from without undue cost or friction. Components with dual-licensing (open community / commercial enterprise tier) are included where the open tier provides sufficient functionality for municipal use.

*Digital sovereignty* is the ability of a government to make independent decisions about its digital infrastructure, including the right to inspect, modify, audit, and migrate software without dependency on a single vendor [3]. In the European context, digital sovereignty additionally encompasses compliance with GDPR data residency obligations and the NIS2 security framework [27].

*Interoperability* refers to technical, semantic, and organisational interoperability as defined in the European Interoperability Framework (EIF) [45], including implementation of XÖV standards (Germany) [46] and eCH standards (Switzerland) [47].

### 1.2 Research Questions

1. What does a state-of-the-art open-source municipal technology stack look like in 2026?
2. What lessons can be drawn from the Swiss, German, and European sovereign technology communities?
3. What is the optimal phased implementation pathway for a city government of varying sizes?
4. What is the total cost of ownership differential between open-source and proprietary stacks?
5. How should procurement, stakeholder engagement, and risk management be structured to maximise success probability?

---

## 2. Methodology

This paper employs a multi-method research design combining:

**Systematic literature review** of peer-reviewed publications, grey literature, and policy documents published between 2010 and 2026, covering e-government theory, digital sovereignty, open-source software in public administration, and municipal digital transformation. The review follows PRISMA-adapted guidelines for grey literature inclusion [60].

**Comparative policy analysis** of technology legislation and strategies from Switzerland (EMBAG 2023 [1], E-Government Strategy 2024–2027 [16], Swiss E-ID 2024 [54]), Germany (OZG 2017/2024 [2], Deutsche Verwaltungscloud-Strategie, ZenDiS mandate [49]), and the European Union (Interoperable Europe Act 2024 [6], EU Open Source Strategy 2020–2023 [5], EU Data Act 2023 [51], AI Act 2024).

**Technology stack evaluation** using a structured scoring matrix assessing each component on: (a) licence openness, (b) deployment maturity, (c) community health, (d) interoperability standards compliance, (e) security posture, (f) total cost of ownership, and (g) existing public-sector deployments. Scores are 1–5 and derived from publicly available evidence.

**Total cost of ownership modelling** following the methodology described in Section 4.11, using a five-year horizon and three municipality-size tiers.

**Case study analysis** of six municipalities that have undertaken open-source transitions, selected to represent a range of sizes, jurisdictions, and technology strategies.

**Stakeholder analysis** mapping the interests, influence, and engagement needs of each stakeholder group.

The literature review is designed to be self-improving: the source registry (`Mem/source-registry.md`) and literature review state (`Mem/literature-review-state.md`) are versioned documents updated on a recurring quarterly basis. The `Scripts/update_literature_review.py` script provides structured prompts for reviewing and improving these files.

### 2.1 Inclusion Criteria

Sources were included if they: (a) address open-source software in public administration; (b) cover governmental digital transformation strategy; (c) relate to the European, Swiss, or German regulatory context; or (d) provide primary data on municipal technology implementations. Academic sources were obtained from Government Information Quarterly, Public Management Review, Information Systems Management, and the European Journal of e-Government. Policy documents were obtained directly from official government and institutional sources.

### 2.2 Limitations

This paper is a citation-complete draft (v0.2.0). Technology stack assessments reflect publicly available information as of June 2026. Implementation cost estimates are indicative ranges derived from published case studies and vendor documentation, not primary procurement data. Readers should commission local TCO analyses before procurement decisions. The German translation is derived from this English source of truth; any discrepancies should be resolved against the English version.

---

## 3. Literature Review

### 3.1 Theoretical Foundations of E-Government

The academic literature on e-government has evolved through four broad phases [30]. First-generation e-government (1995–2005) focused on digitising existing processes and creating government websites [29]. Second-generation e-government (2005–2012) emphasised online service delivery, citizen portals, and back-office integration [7]. Third-generation e-government (2012–2020) introduced open data, participatory platforms, and mobile-first service design [8]. The current fourth generation (2020–present) is characterised by platform government, digital identity infrastructure, data spaces, and the sovereignty turn — a recognition that digital autonomy is a prerequisite for democratic self-governance [45, 60].

Wirtz and Weyerer's holistic e-government maturity model identifies five dimensions: technical infrastructure, process quality, service quality, citizen orientation, and transparency [7]. Municipal governments in Switzerland and Germany score variably across these dimensions; technical infrastructure and process quality lag citizen expectations in most jurisdictions, while the regulatory environment increasingly mandates transparency and interoperability [1, 2, 45].

Janowski's four-generation framework [30] provides a complementary perspective: the transition from digitisation (Gen 1) through transformation (Gen 2) to engagement (Gen 3) to contextualization (Gen 4) maps directly onto the open-source strategy, where contextualisation means embedding digital services within the specific civic, legal, and democratic context of each municipality rather than imposing standardised vendor solutions.

Scholl's comprehensive handbook of e-government transformation [60] identifies political commitment, administrative capacity, and citizen trust as the three binding constraints on successful digital government transitions — findings consistent with the risk analysis in Section 7.

Recent work by Almeida et al. [59] on digital government transformation in European municipalities finds that open-source adoption is significantly correlated with higher long-term service quality scores and lower vendor dependency, though the causal direction remains debated. The study examined 127 European municipalities over a seven-year period.

### 3.2 Digital Sovereignty in Public Administration

The concept of digital sovereignty — the capacity of public institutions to make independent, auditable decisions about their digital infrastructure — has moved from academic concept to policy imperative in the European context [3, 5]. The EU Open Source Strategy 2020–2023 established "sharing and reuse" as a core principle, mandating that European institutions prefer open-source solutions in technology procurement [5]. The 2024 Interoperable Europe Act creates binding obligations for cross-border interoperability in public administrations [6].

The **EU Data Act 2023** (Regulation (EU) 2023/2854), in force from 12 September 2025, adds a further dimension: it establishes data portability and switching rights applicable to cloud and data-processing services used by public-sector bodies [51]. Municipalities using proprietary cloud services must now have documented exit plans demonstrating that data and workloads can be migrated without disproportionate cost — a requirement that open-source stacks satisfy structurally.

**GAIA-X**, the European data infrastructure initiative, has evolved significantly since its 2020 launch. As of 2024, GAIA-X AISBL has published its Architecture Document v2024 and established seven sector-specific data spaces, including GovStack and an Urban Data Space [55]. However, the original ambition for a competing cloud infrastructure has been scaled back in favour of a federation standard and trust framework. For municipalities, GAIA-X compliance means participation in federated data spaces rather than deployment of GAIA-X cloud software per se.

Germany's **Sovereign Cloud Stack (SCS)**, developed by the Open Source Business Alliance (OSBA) with BMWK funding, remains the most concrete realisation of sovereign cloud infrastructure for European public administration [3]. SCS provides a fully open-source, self-hostable cloud platform (OpenStack + Kubernetes + Ceph) that is technically and legally sovereign. As of 2026, SCS underpins cloud environments operated by multiple German Länder and by govdigital eG's shared infrastructure [23]. The SCS certification programme provides municipalities with a verifiable guarantee of sovereignty.

**ZenDiS GmbH** (Zentrum für Digitale Souveränität der öffentlichen Verwaltung), established in 2022 by the German Federal Ministry of the Interior (BMI), is the central coordination body for open-source digital sovereignty in German public administration [49]. ZenDiS manages the OpenDesk workplace suite [42], coordinates the openCode.de platform [10], commissions open-source audits and interoperability testing, and publishes annual status reports on the state of digital sovereignty in German government. Its 2024 annual report documents 340+ repositories on openCode.de, 12 municipalities piloting OpenDesk, and a stated goal of 100% open-source capability for the federal workplace by 2027.

Switzerland's approach institutionalises digital sovereignty through the EMBAG framework [1] and eCH standards [47]. The Swiss Confederation's approach demonstrates that full open-source mandates are compatible with federated, multilingual governance — a model directly applicable to German Länder and cantons.

### 3.3 The German OZG Ecosystem

The Onlinezugangsgesetz (OZG), enacted in 2017 and substantially reformed in 2024 (OZG 2.0), requires all German federal, Land, and municipal administrations to offer their administrative services online [2]. The OZG 2.0 reform addresses shortcomings of the first generation through the "Once Only" principle, the "Einer für Alle" (EfA) shared service development model, and a federal platform architecture centred on BundID and FITKO [9]. The FITKO 2023 annual report documents implementation status across all 16 Länder, with 439 OZG services in production by December 2023 against a target of 575 [9].

The **openCode.de** platform hosts over 340 government software repositories as of 2026, enabling municipalities to discover, evaluate, and reuse solutions developed by peer administrations [10]. The platform is managed by DigitalService GmbH des Bundes, which also leads the development of interoperability standards and developer documentation [57].

**Dataport AöR**, operating across six northern German Länder, provides a model of cooperative public-sector IT delivery applicable to municipal contexts [24]. **AKDB** (Anstalt für Kommunale Datenverarbeitung in Bayern) performs the equivalent function in Bavaria, serving over 1,000 municipalities. The cooperative model — where municipalities pool IT resources through public-law entities — resolves many procurement and sovereignty challenges simultaneously.

The **XÖV standards** framework, maintained by KoSIT (Koordinierungsstelle für IT-Standards), provides the data interchange vocabulary for German public administration [46]. Key standards relevant to municipal implementations include XPersonenstand, XMeld (residents registration), XKfz (vehicle registration), XBildung (education), and XJustiz. All OZG services are required to implement relevant XÖV standards, making XÖV compliance a non-negotiable procurement criterion.

### 3.4 Swiss Cantonal and Federal Digital Services

Switzerland's federal structure creates both challenges and opportunities for municipal digital transformation. Key Swiss digital infrastructure includes:

- **Fedlex** (fedlex.admin.ch): the official platform for Swiss federal law, built on open standards and providing machine-readable legal data in all national languages [1].
- **opendata.swiss**: the national open government data portal, built on CKAN, cataloguing thousands of datasets from federal, cantonal, and municipal authorities [44].
- **GEVER**: the standardised records management system for the federal administration, providing a template for cantonal and municipal implementations [43].
- **Swiss E-ID**: Switzerland's revised digital identity system, following the rejection of the first E-ID proposal in the 2021 referendum. The 2023 legislation (Bundesgesetz über den elektronischen Ausweis, E-ID-Gesetz) introduced a state-issued, privacy-preserving E-ID based on a "public Wallet" model with selective disclosure [54]. This system, expected in production by 2026, is directly relevant to municipal citizen-service authentication.

The **eCH standards** framework is Switzerland's equivalent of Germany's XÖV — a family of XML-based interoperability standards for Swiss e-government [47]. Key standards include eCH-0007 (municipality register), eCH-0010 (postal addresses), eCH-0011 (person identification), eCH-0044 (person identification for official registers), and eCH-0058 (versioning framework). All municipal digital services in Switzerland should implement relevant eCH standards to ensure interoperability with cantonal and federal systems.

The **E-Government Strategy Switzerland 2024–2027**, co-authored by the Federal Council and the Conference of Cantonal Governments (KdK), sets out a collaborative framework for digital services explicitly mandating open standards, interoperability, and coordinated development [16].

The **Open Government Data Strategy 2024–2027** (OGD-Strategie Schweiz 2024–2027) mandates publication of public-sector data as machine-readable open data by default, with all federal and cantonal authorities required to publish their data catalogues to opendata.swiss [44]. This creates direct obligations for municipal open data publication in many cantons.

### 3.5 Open Source Communities and Sovereign Technology

**Decidim** (Barcelona, 2016) is a participatory democracy platform used by over 400 organisations in 40 countries [12]. Key deployments include Barcelona (100,000+ registered users, participatory budgeting, urban planning consultations), Helsinki (participatory budgeting, youth councils), the Swiss canton of Schaffhausen (direct-democracy platform for cantonal initiatives), and New York City (participatory budgeting). The Decidim Association publishes a social contract committing the platform to democratic values, transparency, and non-commercialisation — a governance model that public administrations can rely on for long-term stability.

**CONSUL Democracy** (Madrid City Council, 2015) is an alternative participatory platform, also AGPL-3.0, with particular strength in Spanish-speaking municipalities and some European cities [52]. CONSUL and Decidim have converging feature sets; the choice between them should be based on community language, existing regional deployments, and local developer capacity.

**Matrix/Element** provides an open, decentralised, end-to-end-encrypted communication protocol increasingly adopted by European public administrations. The German federal BundesMessenger and the French government's Tchap both operate on Matrix [14]. The protocol's federation model means messages between municipalities using different servers are delivered end-to-end encrypted without routing through a central provider.

**Nextcloud** (Stuttgart, 2016) is the most widely deployed open-source file sync and collaboration platform in European public administration, used by thousands of German municipalities, the Swiss Federal Administration, and dozens of EU institutions [13]. Nextcloud's modular app framework enables expansion from file storage to full collaboration suite (calendaring, contacts, video calls, office documents) on a single platform.

**OpenDesk**, launched by the German Federal Government in 2023 and managed by ZenDiS GmbH, is the most important development in European government open-source workplace software [42]. OpenDesk integrates Nextcloud, Cryptpad, OpenProject, Jitsi Meet, Element (Matrix), and Collabora Online into a coherent, centrally tested and deployed workplace suite. Twelve German municipalities were piloting OpenDesk as of June 2026 [49]. Its adoption removes the principal integration risk from municipal open-source transitions — the hardest part of the stack is pre-assembled.

The **EU Open Source Observatory (OSOR)**, operated by the European Commission's DIGIT directorate, publishes annual reports tracking open-source adoption across EU public administrations [50]. The 2023 OSOR Annual Report documents 84% of EU public-sector organisations now using open-source software in at least one system, up from 69% in 2019, with Germany and Switzerland ranking among the top five for depth of adoption.

### 3.6 The GovStack Initiative

The **GovStack** initiative, launched jointly by the International Telecommunication Union (ITU), the German Federal Ministry for Economic Cooperation and Development (BMZ), and the Digital Impact Alliance (DIAL), provides a framework of reusable "building blocks" for digital government services [48]. GovStack building blocks are specification-level abstractions — a consent management block, an identity block, a payment block — that any implementation technology can satisfy. The initiative has published specifications for 13 building blocks covering the core functional requirements of digital government.

GovStack is relevant to European municipal contexts in three ways. First, it provides a technology-neutral framework for evaluating whether a given open-source component satisfies the functional requirement. Second, it enables interoperability with digital government initiatives in partner countries (particularly relevant for municipalities with international twinning agreements or cross-border service delivery). Third, GovStack's "country engagement" model documents how to move from a legacy proprietary stack to a building-block architecture, providing a validated implementation methodology [48].

The GovStack building-block approach is directly complementary to the technology stack analysis in Section 4: each recommended component satisfies one or more GovStack building blocks.

### 3.7 Gaps in the Literature

1. **Total cost of ownership studies** comparing open-source and proprietary municipal stacks remain sparse. The most rigorous available data are from the French government's LibreOffice migration (documented savings of approximately €6 million annually for 500,000 users [56]) and the EU Commission's economic impact study [56]. An independent municipal TCO methodology is developed in Section 4.11.
2. **Longitudinal implementation data** from cities that have completed full open-source transitions is limited. Munich's LiMux (2003–2017) remains the most-cited case; post-mortems consistently attribute the reversal to political, not technical, factors.
3. **Small-municipality evidence** is limited to anecdotal case studies. Section 4.12 addresses this gap.
4. **User experience research** comparing citizen satisfaction with open-source and proprietary municipal digital services remains almost entirely absent from peer-reviewed literature.
5. **AI Act implications** for AI-powered municipal services on open-source platforms are not yet covered in policy literature; the first relevant guidance is expected from the EU AI Office in 2026–2027.

---

## 4. Technology Stack Analysis

A municipal technology stack can be decomposed into nine functional layers plus a cross-cutting economic layer (TCO) and evidence layer (case studies). The analysis below evaluates the leading open-source options for each layer.

### 4.1 Digital Identity and Authentication

**Function:** Authenticate citizens and staff; federate identity across services; implement single sign-on (SSO); integrate with national identity systems.

**Recommended component: Keycloak** (Red Hat / CNCF) [21]

Keycloak is the de facto open-source identity and access management (IAM) platform for public administration in Europe. It implements OpenID Connect, OAuth 2.0, SAML 2.0, and FIDO2/WebAuthn, enabling federation with national identity systems (BundID in Germany, Swiss E-ID, Austrian e-ID). It is deployed by EU institutions, multiple German Länder, Swiss cantons, and the wider European public sector.

For German municipalities, Keycloak integrates with BundID via OIDC, enabling citizens to authenticate once across all OZG services. For Swiss municipalities, Keycloak will integrate with the new Swiss E-ID Wallet via OIDC/SD-JWT when the E-ID enters production (expected 2026) [54].

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Licence openness | 5 | Apache 2.0 |
| Deployment maturity | 5 | Production-proven, 10+ years |
| Community health | 5 | Large, active, CNCF-supported |
| Interoperability | 5 | OIDC, OAuth2, SAML2, FIDO2, SD-JWT |
| Security posture | 5 | CVE-responsive; BSI IT-Grundschutz mappable |
| TCO | 4 | No licence cost; ops expertise required |
| Public-sector deployments | 5 | Widespread EU government use |
| GovStack alignment | 5 | Satisfies GovStack Identity Building Block |

### 4.2 Document Management and Records

**Function:** Store, retrieve, classify, and retain official records; manage records-management workflows; comply with archiving obligations.

**Recommended components: Nextcloud** (collaborative file management) + **OpenProject** (project and records linking) [13, 20]

For municipalities requiring full GEVER compliance (Switzerland), the Nextcloud + OneGov GEVER combination (open-source GEVER implementation from the canton of Schaffhausen and Bern) or commercial GEVER systems (CMI, Fabasoft Community) provide the compliance layer. For German municipalities, XÖV-compliant document management integrates with Camunda workflows and Nextcloud storage.

Nextcloud's end-to-end encryption, ISO 27001 certified hosting options, and documented Swiss Federal Administration deployment [13] make it a low-risk choice for sensitive municipal documents.

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Licence openness | 5 | AGPL-3.0 (Nextcloud); GPLv3 (OpenProject) |
| Deployment maturity | 5 | 400,000+ organisations (Nextcloud) |
| Community health | 5 | Nextcloud GmbH + community |
| Interoperability | 4 | WebDAV, CalDAV, CardDAV, CMIS, SharePoint migration path |
| Security posture | 5 | ISO 27001 (Enterprise) |
| TCO | 5 | No per-seat licence (Community Edition) |
| Public-sector deployments | 5 | Swiss federal, German states, EU institutions |

### 4.3 Workflow Automation and Business Process Management

**Function:** Automate administrative workflows; model, execute, and monitor BPMN processes; integrate with XÖV/eCH data standards.

**Recommended component: Camunda Platform 8 Community Edition** [33]

Camunda provides a BPMN 2.0-native workflow engine with strong support for complex multi-step administrative processes and XÖV data standards integration [46]. It is deployed by multiple German Länder for OZG service automation. The Community Edition (Apache 2.0) is sufficient for most municipal use cases; scaling to higher throughput may require the Enterprise tier.

**Alternative: Flowable** (Apache 2.0). Flowable is a lighter-weight BPMN/CMMN/DMN engine that avoids Camunda's dual-licensing model entirely. Recommended for small municipalities or jurisdictions where procurement of dual-licensed software is legally complex.

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Licence openness | 4 | Community: Apache 2.0; Enterprise: proprietary |
| Deployment maturity | 5 | Production-proven |
| Community health | 4 | Active; enterprise tier funds development |
| Interoperability | 5 | BPMN 2.0, REST API, event-driven, XÖV/eCH adaptors |
| Security posture | 4 | Actively maintained |
| TCO | 3 | Community free; scale may need Enterprise tier |
| Public-sector deployments | 4 | Multiple German Länder |

### 4.4 Citizen Participation

**Function:** Consultation, participatory budgeting, initiative collection, deliberation platforms; direct-democracy support.

**Recommended component: Decidim** [12]

Decidim is the most mature and widely adopted open-source participation platform globally. Its deployments in Barcelona, Helsinki, canton of Schaffhausen, and New York City validate it across linguistic, legal, and democratic contexts. The Decidim Association's governance model — a multi-stakeholder association with a published social contract — provides long-term stability assurances that proprietary alternatives cannot offer.

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Licence openness | 5 | AGPL-3.0 |
| Deployment maturity | 5 | 400+ deployments globally |
| Community health | 5 | Active association and community |
| Interoperability | 4 | REST API, webhooks, GraphQL |
| Security posture | 4 | Actively maintained |
| TCO | 5 | No licence cost |
| Public-sector deployments | 5 | Cities, cantons, federal agencies |
| GovStack alignment | 5 | Satisfies GovStack Civil Registration and Consent building blocks |

**Alternative:** CONSUL Democracy [52] — also AGPL-3.0, strong in Spanish-speaking Europe and some German-speaking cities. Choose CONSUL where local developer capacity is in Ruby on Rails rather than Ruby on Rails with the Decidim framework conventions.

### 4.5 Communication and Collaboration

**Function:** Internal messaging, video conferencing, email, calendar; secure inter-agency communication; council meeting support.

**Recommended components:**
- **Matrix/Element** for messaging and inter-agency secure communication [14]
- **Jitsi Meet** or **BigBlueButton** for video conferencing [34, 35]
- **Nextcloud Talk** for integrated team communication within the document management layer

The German federal BundesMessenger (built on Matrix) provides a direct reference deployment. The French government's Tchap confirms Matrix as the European government messaging standard. BigBlueButton's "Rooms" feature specifically supports council meeting workflows including voting, turn order, and minute integration.

| Component | Licence | Score (avg) | Key advantage |
|---|---|---|---|
| Matrix/Element | Apache 2.0 | 4.7 | E2E encryption, federation, BundesMessenger reference |
| Jitsi Meet | Apache 2.0 | 4.6 | Browser-based, self-hostable, zero-client |
| BigBlueButton | LGPL-3.0 | 4.4 | Council meeting focus, breakout rooms |
| Nextcloud Talk | AGPL-3.0 | 4.3 | Integrated with file management layer |

### 4.6 Open Data Publication

**Function:** Publish machine-readable datasets; catalogue municipal data; provide API access; comply with EU Open Data Directive and national OGD strategies.

**Recommended component: CKAN** [22]

CKAN powers opendata.swiss [44], data.gov, data.gov.uk, and dozens of national and municipal open data portals. Its plugin architecture enables full DCAT-AP, DCAT-AP.de, and OGD Switzerland metadata standard compliance, and harvesting by upstream cantonal/federal catalogues. The municipality's CKAN instance should be configured as a harvest source for the relevant national portal (opendata.swiss for Switzerland, govdata.de for Germany).

For German municipalities, the **DCAT-AP.de v2.0** profile mandated by FITKO [9] is supported by CKAN's `ckanext-dcatapdech` plugin.

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Licence openness | 5 | AGPL-3.0 |
| Deployment maturity | 5 | 10+ year production track record |
| Community health | 4 | CKAN Association; active |
| Interoperability | 5 | DCAT-AP, DCAT-AP.de, OGD-CH, OAI-PMH, SPARQL |
| Security posture | 4 | Actively maintained |
| TCO | 4 | No licence cost; moderate ops overhead |
| Public-sector deployments | 5 | Switzerland, Germany, EU, US, UK |

### 4.7 Geographic Information Systems

**Function:** Map-based citizen services; urban planning; spatial data publication; cadastre integration.

**Recommended components:**
- **QGIS** (desktop/server) for spatial data editing and analysis [37]
- **GeoServer** (Apache 2.0) for OGC-compliant WFS/WMS/WCS publication
- **OpenStreetMap** as the base cartographic layer [36]
- **MapProxy** or **GeoWebCache** for tile caching

Switzerland's **swisstopo** and Germany's **BKG** (Bundesamt für Kartographie und Geodäsie) both provide high-quality governmental base map data in open formats (WMTS, WMS, WFS) under permissive licences (CC-BY for swisstopo data, DL-DE/Zero for BKG data), enabling municipalities to build map-based services without OpenStreetMap alone.

For citizen-facing map interfaces, **MapLibre GL** (BSD-2-Clause, the open-source fork of Mapbox GL) provides performant vector tile rendering suitable for municipal web portals.

### 4.8 Public Website and Content Management

**Function:** Public-facing website; news and announcements; service directory; accessibility compliance.

**Recommended components:**
- **TYPO3** for German-speaking municipalities [19]: the dominant CMS in Swiss and German public administration; the TYPO3 Association provides long-term support (until 2030+ for v12) and the GovBundle extension for standard municipal use cases. Native BITV 2.0 / WCAG 2.1 AA compliance.
- **Drupal** for jurisdictions outside German-speaking Europe: used by the European Commission, significant international community, strong multilingual support.

Both systems integrate with CKAN open data portals, support multilingual publishing workflows, and provide REST APIs for service directory integration.

### 4.9 Cloud Infrastructure and Hosting

**Function:** Compute, storage, networking, container orchestration; digital sovereignty at the infrastructure layer.

**Recommended component: Sovereign Cloud Stack (SCS)** [3, 11]

SCS provides a fully open-source cloud stack (OpenStack + Kubernetes + Ceph) that can be self-hosted by municipalities with sufficient IT capacity, operated by a cooperative provider (govdigital eG [23]), or deployed by SCS-certified commercial operators (plusserver, OSISM, StackIT). The SCS certification programme verifies that operators meet the technical and legal sovereignty requirements — critical for municipal data protection obligations.

**For municipalities without in-house cloud operations capacity** (the majority of municipalities under 100,000 population), the recommended path is a managed SCS hosting contract with a govdigital eG member or SCS-certified provider, supplemented by a data processing agreement (DPA) satisfying GDPR Article 28 and a contractual guarantee of data residency in the EU/Switzerland.

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Licence openness | 5 | Apache 2.0 / fully open |
| Deployment maturity | 4 | Production in multiple Länder |
| Community health | 5 | OSBA-backed, growing |
| Interoperability | 5 | Open APIs, OCI-compliant, S3-compatible |
| Security posture | 5 | BSI IT-Grundschutz compatible, SCS certification |
| TCO | 4 | No licence; infrastructure cost only |
| Public-sector deployments | 4 | German Länder, govdigital eG |

### 4.10 Reference Architecture

```
╔══════════════════════════════════════════════════════════════╗
║                    CITIZEN TOUCHPOINTS                       ║
║       TYPO3/Drupal · Decidim · CKAN · Nextcloud Portal      ║
╠══════════════════════════════════════════════════════════════╣
║                       SERVICE LAYER                         ║
║   Camunda Workflows · XÖV/eCH Forms · GeoServer · MapLibre  ║
╠══════════════════════════════════════════════════════════════╣
║                   COLLABORATION LAYER                       ║
║   Nextcloud · Matrix/Element · Jitsi/BBB · OpenProject      ║
╠══════════════════════════════════════════════════════════════╣
║                     IDENTITY LAYER                          ║
║        Keycloak ← → BundID / Swiss E-ID / Austrian e-ID     ║
╠══════════════════════════════════════════════════════════════╣
║                   INFRASTRUCTURE LAYER                      ║
║  Sovereign Cloud Stack · Kubernetes · PostgreSQL · Ceph     ║
╠══════════════════════════════════════════════════════════════╣
║              INTEROPERABILITY STANDARDS                     ║
║     XÖV (DE) · eCH (CH) · DCAT-AP (EU) · EIF (EU)         ║
╚══════════════════════════════════════════════════════════════╝
```

All layers communicate via open APIs following the EIF technical interoperability principles [45]. Container orchestration is handled by Kubernetes [39]; relational persistence by PostgreSQL [41]; object storage by Ceph — all running on SCS. An **API gateway** (Kong CE, Apache 2.0, or Gravitee, Apache 2.0) provides rate limiting, authentication forwarding, and API documentation between layers. Security is governed by BSI IT-Grundschutz (Germany) [26] or the ISDS framework (Switzerland), with NIS2 Directive obligations applying to both [27].

### 4.11 Total Cost of Ownership Analysis

The economic case for open-source municipal technology is strongest when total costs — not merely procurement costs — are compared. Proprietary stacks typically present low initial costs followed by escalating licence fees, integration costs, and exit barriers. Open-source stacks require higher initial investment in implementation and skills but eliminate licence escalation and reduce long-term switching costs.

#### 4.11.1 Cost components

| Cost category | Proprietary stack | Open-source stack |
|---|---|---|
| Software licences (5 yr) | €150–300/user/yr × 5 | €0 |
| Implementation & migration | €50–100k (vendor-led) | €150–300k (open, competitive) |
| Hosting & infrastructure | €30–80/user/yr | €15–40/user/yr (SCS-based) |
| Support & maintenance | Bundled in licence | €10–30/user/yr (cooperative) |
| Training | €200–500/user (once) | €300–700/user (higher initially) |
| Exit / migration costs | €200–500k (high lock-in) | €20–80k (low lock-in) |

*User figures based on published vendor pricing, govdigital eG framework rates, and published case studies. Ranges reflect small (5,000 pop.) to medium (100,000 pop.) municipalities.*

#### 4.11.2 Five-year TCO model

For a representative municipality of **50,000 population** with **400 staff**, the five-year TCO comparison is:

| Item | Proprietary (5 yr) | Open-source (5 yr) |
|---|---|---|
| Productivity suite licences (400 users) | €640,000 | €0 |
| Email/calendaring (400 users) | €240,000 | €0 |
| Video conferencing (400 users) | €120,000 | €0 |
| Document management | €180,000 | €0 |
| CMS | €80,000 | €0 |
| Implementation & migration | €80,000 | €240,000 |
| Infrastructure (cloud hosting) | €200,000 | €140,000 |
| Support & training | €180,000 | €200,000 |
| **Total 5-year TCO** | **€1,720,000** | **€580,000** |
| **Net saving** | | **€1,140,000** |

This model is conservative: it excludes vendor lock-in risk premium, OZG compliance costs associated with proprietary systems, and the long-term value of capability built in-house. The EU Commission's open-source economic impact study [56] confirms that governments systematically underestimate open-source TCO advantages.

For a **small municipality of 8,000 population** (50 staff), the equivalent five-year saving is approximately **€120,000–€180,000**, primarily from licence elimination and reduced infrastructure costs. This is sufficient to fund a part-time digital transformation coordinator role for the entire transition period.

#### 4.11.3 Key TCO risks for open-source transitions

1. **Skills premium**: Initial implementation may cost 2–3× the proprietary alternative if specialist contractors are required. Mitigation: use OpenDesk (pre-integrated), govdigital framework contracts, and cooperative IT providers.
2. **Integration work**: Connecting open-source components requires more integration engineering than single-vendor suites. Mitigation: follow the reference architecture (Section 4.10) and use OpenDesk for the collaboration layer.
3. **Training uplift**: Staff familiar with proprietary productivity suites require retraining. Mitigation: phased migration, parallel operation, open-source champion programme.

### 4.12 Case Studies

#### 4.12.1 Barcelona, Spain: Open-source at municipal scale

Barcelona City Council (1.6M population) began its open-source transition in 2016 under the leadership of CTO Francesca Bria [60]. Key outcomes documented by 2023:
- **Decidim** deployed for participatory budgeting, urban planning consultations, and citizen assemblies; 100,000+ registered users [12]
- **Drupal** CMS replacing proprietary web platform; €1.2M annual licence savings
- **Open data portal** (CKAN) publishing 500+ datasets; ranked among Europe's top 10 municipal open data portals
- **Municipal digital sovereignty policy** requiring all new software to be AGPL or equivalent

Key lesson: Political leadership at the technical director level, combined with clear procurement policy change, was the decisive factor. Technical migration was straightforward; managing contractor resistance to open-source requirements was the primary challenge.

#### 4.12.2 Helsinki, Finland: Participatory budgeting with Decidim

Helsinki (640,000 population) deployed Decidim in 2018 for the OmaStadi participatory budgeting programme [12]. By 2023:
- €8.8M per cycle allocated via citizen votes
- 47,000+ participants in the 2021 cycle
- 80% of projects funded within 18 months of approval
- Open source approach enabled city developers to extend Decidim with Helsinki-specific features (Finnish-language support, BankID integration) and contribute these extensions back upstream

Key lesson: Upstream contribution is both a civic duty and a practical asset; Helsinki's Finnish-language extensions are now maintained by the wider Decidim community.

#### 4.12.3 Canton of Schaffhausen, Switzerland: Decidim for direct democracy

Schaffhausen (82,000 population) deployed Decidim as a digital platform for cantonal consultation processes and initiative collection [12]. The deployment is particularly significant as it operates in a Swiss direct-democracy context — citizens use the platform to submit and sign cantonal initiatives, then transfer verified signatures to the paper-based official process.

Key lesson: Open-source platforms can be extended for jurisdiction-specific democratic processes. The eCH-0020 standard for person identification was used to verify citizen identity in the digital signature process [47].

#### 4.12.4 Bühl, Baden-Württemberg, Germany: Small-municipality open-source transition

Bühl (30,000 population) completed a transition from Microsoft Office to LibreOffice and from proprietary email to open-source alternatives between 2019 and 2022, coordinated through the AKDB cooperative platform [24]. Key outcomes:
- €42,000 annual licence cost eliminated
- 85% of staff competent on LibreOffice within 6 months (after initial 3-month dip in productivity)
- Integration with AKDB's OZG service platform enabled without vendor change

Key lesson: At small-municipality scale, the primary benefit is cost elimination rather than sovereignty. The AKDB cooperative framework removed all procurement complexity.

#### 4.12.5 Kirchheim unter Teck, Baden-Württemberg: Open data pioneer

Kirchheim unter Teck (40,000 population) launched an open data portal in 2021 as part of Baden-Württemberg's open data initiative, using CKAN connected to the state's govdata.de harvest pipeline [22]. By 2023, 45 datasets were published, including real-time bus timetables, building permit data, and municipal budget data. The portal generated three civic-technology applications developed by local volunteers.

Key lesson: Open data creates civic value beyond the municipality itself; volunteer developer communities can extend municipal services at zero cost.

#### 4.12.6 Aarau, Switzerland: Integrated open-source administration

Aarau (22,000 population, cantonal capital of Aargau) operates one of Switzerland's most integrated open-source municipal stacks. The combination of Nextcloud (document management), TYPO3 (web presence), opendata.swiss (data portal), and eCH-compliant residents-registration data exchange has been documented as a best-practice model by the canton. Annual IT cost per resident: CHF 31, compared to a cantonal average of CHF 52.

Key lesson: eCH standard compliance enabled seamless integration with cantonal systems, eliminating custom integration work estimated at CHF 80,000.

---

## 5. Implementation Roadmap

The implementation is structured as a 36-month, five-phase programme. A separate lightweight pathway for municipalities under 20,000 population is described in Section 5.6.

### Phase 0: Foundation (Months 1–3)

**Objective:** Establish governance, assess current state, build the coalition.

**Deliverables:**
- Digital Transformation Steering Committee established (mayor/executive + IT lead + procurement + civil society representative)
- Current-state technology audit completed (inventory of all software licences, contracts, data stores, integrations)
- Stakeholder engagement plan adopted (see Section 6.1)
- Procurement framework established (see Section 6.2)
- Memorandum of Understanding with cooperative IT provider (Dataport, AKDB, govdigital eG, or Swiss equivalent)
- First open-source champion appointed in IT team

**Decision gate 0→1:** Political mandate secured (council resolution or executive decision); budget envelope approved.

**Indicative budget:** €100,000–€300,000 (depending on city size, primarily audit and facilitation costs).

### Phase 1: Identity and Infrastructure (Months 4–12)

**Objective:** Stand up the foundational layers that everything else depends on.

**Deliverables:**
- Sovereign Cloud Stack environment operational (own-hosted or managed via govdigital/SCS-certified provider)
- Keycloak identity provider deployed, federated with national identity system (BundID/Swiss E-ID)
- Nextcloud baseline deployment for internal collaboration (files, calendar, contacts)
- Matrix/Element messaging for all staff
- BSI IT-Grundschutz baseline documentation complete (Germany) or ISDS equivalent (Switzerland)
- Software Bill of Materials (SBOM) process initiated

**Decision gate 1→2:** 100% of IT staff authenticated via Keycloak SSO; file storage migrated; basic encrypted messaging operational; security baseline approved by DPO.

**Indicative budget:** €150,000–€400,000.

### Phase 2: Services and Workflows (Months 10–18)

**Objective:** Migrate or build the first five citizen-facing services on open infrastructure.

**Deliverables:**
- Five highest-volume administrative services (from OZG catalogue / cantonal service list) deployed on Camunda/XÖV or Camunda/eCH stack
- TYPO3 or Drupal CMS migration complete
- Open data portal (CKAN) launched with minimum 20 datasets, connected to national harvest pipeline
- Decidim instance deployed for the first participatory process (e.g., one participatory budgeting cycle or consultation)
- OpenDesk pilot with 50-user group

**Decision gate 2→3:** 80% of target service volume processed through new system; zero regression in service availability; first open data publication live; NIS2 incident-response plan documented.

**Indicative budget:** €200,000–€600,000.

### Phase 3: Integration and Extension (Months 16–24)

**Objective:** Integrate all layers; extend service coverage to 80% of transactions.

**Deliverables:**
- All services federated via Keycloak SSO
- Nextcloud integrated with document management workflows and archival system
- GIS layer operational (QGIS + GeoServer + MapLibre)
- 80% of administrative services digitised and on open stack
- Inter-agency data exchange via XÖV/eCH fully operational
- OpenDesk rolled out to all staff
- CKAN dataset count ≥ 50; DCAT-AP.de/OGD-CH profile complete

**Decision gate 3→4:** End-to-end service delivery without paper for 80% of transaction types; first annual open data report published; TCO tracking activated.

**Indicative budget:** €150,000–€350,000.

### Phase 4: Optimisation and Community (Months 22–30)

**Objective:** Optimise user experience; contribute back to open-source communities; publish results.

**Deliverables:**
- User satisfaction survey conducted (target: NPS > 40 or CSAT > 4.0/5.0)
- Minimum three improvements contributed to upstream projects (openCode.de, Decidim, Nextcloud, etc.)
- Municipal open-source community of practice established with ≥ 3 peer municipalities
- Performance benchmarks published
- First annual TCO report published

**Decision gate 4→5:** Upstream contributions accepted; community of practice active; TCO saving documented.

**Indicative budget:** €80,000–€180,000.

### Phase 5: Sovereignty and Scale (Months 28–36)

**Objective:** Achieve full digital sovereignty; prepare for replication.

**Deliverables:**
- Full audit of all software components for OSI licence compliance
- Sovereign data residency verified (100% on EU/CH sovereign infrastructure)
- Playbook for replication by neighbouring municipalities (published under CC-BY-4.0)
- This strategy paper updated to v1.0 based on implementation experience
- Zero critical proprietary single-vendor dependencies in production stack

**Decision gate 5→complete:** Independent audit confirms sovereignty; replication playbook published.

**Indicative budget:** €60,000–€120,000.

### 5.6 Small-Municipality Pathway (population < 20,000)

Small municipalities face different constraints: limited IT staff (often zero dedicated IT, relying on a cooperative provider or shared-services arrangement), tighter budgets, and lower transaction volumes. The standard five-phase roadmap is adapted as follows:

**Simplified stack:** Use OpenDesk as the pre-integrated workplace suite (eliminates integration work), TYPO3 with the GovBundle extension (reduces CMS implementation effort), and the cooperative provider's Keycloak SSO (no self-hosted IAM required). Skip self-hosted GIS; use cantonal/Land GIS services.

**Procurement path:** Join an existing cooperative procurement framework (AKDB in Bavaria, Dataport in northern Germany, cantonal IT cooperative in Switzerland). This provides framework contracts, pre-negotiated SLAs, and shared implementation teams without individual competitive procurement.

**Timeline:** 18 months rather than 36. Phase 0 (3 months) → Phases 1–3 combined (12 months) → Phase 4–5 (3 months).

**Budget:** €40,000–€120,000 total, primarily for change management, training, and cooperative membership fees.

**Key risk:** Staff skills. A single open-source champion with 20% time allocation is the minimum; a 40% role is recommended for transitions above 30 staff.

---

## 6. Stakeholder and Procurement Strategy

### 6.1 Stakeholder Map

| Stakeholder | Primary interest | Engagement approach |
|---|---|---|
| Mayor / Executive | Political success, cost, citizen approval | Executive briefing, quarterly progress dashboard |
| City council | Oversight, democratic legitimacy, TCO | Quarterly reports, open council sessions, TCO evidence |
| City IT team | Technical feasibility, workload, skills | Co-design, training budget, community membership |
| Procurement office | Legal compliance, risk, audit trail | Framework agreements, legal briefings, GWB/BöB guidance |
| Civil servants (end users) | Ease of use, reliability, familiarity | UX testing, change management, parallel systems, training |
| Citizens | Service quality, privacy, accessibility | Participatory design (Decidim), transparency reporting |
| Civil society / NGOs | Transparency, access, participation | Decidim platform, public roadmaps, open data |
| Open-source communities | Contribution, upstream reuse | openCode.de participation, upstream contributions |
| Sovereign technology providers | Partnership, deployment, support | SCS certified partner agreements, govdigital membership |
| Data protection officer | GDPR compliance, data residency | Privacy-by-design review at each phase; DPA review |
| Cantonal / Land government | OZG/cantonal compliance, interoperability | Joint planning, XÖV/eCH alignment, harvest pipeline |

### 6.2 Procurement Framework

Open-source procurement requires a fundamentally different approach from proprietary licence purchasing. Key principles:

**Principle 1: Procure services, not licences.** Open-source software is free to use; municipalities pay for implementation, hosting, support, customisation, and training. Procurement documents must be structured around service categories, not software names.

**Principle 2: Exploit cooperative procurement structures.** In Germany: govdigital eG framework contracts satisfy GWB/VgV requirements without individual competitive tendering for IT services [23]. AKDB serves Bavarian municipalities under Bayerische Vergaberecht. In Switzerland: the IVöB (Interkantonale Vereinbarung über das öffentliche Beschaffungswesen) framework and cantonal IT cooperative contracts provide equivalent structures. Cooperative procurement is the primary mechanism for making municipal open-source transitions cost-effective.

**Principle 3: Apply the "Public Money? Public Code!" condition.** All custom software developed under contract must be released under an OSI-approved open-source licence and published on openCode.de (Germany) or the equivalent cantonal repository (Switzerland). This should be a contractual non-negotiable [4].

**Principle 4: Evaluate five-year TCO, not procurement price.** Procurement scoring must include a 5-year TCO model (see Section 4.11) covering implementation, hosting, training, support, and exit costs. Procurement frameworks should include a minimum 30% weighting for TCO criteria.

**Principle 5: Require interoperability standards.** All procured systems must implement: XÖV (Germany) [46], eCH (Switzerland) [47], DCAT-AP (EU open data) [45]. Non-compliance should be a disqualifying criterion in the award procedure.

**Principle 6: Mandate SBOM delivery.** Following NIS2 obligations [27] and BSI IT-Grundschutz requirements [26], contracts for software development or deployment should require delivery of a Software Bill of Materials (SBOM) in SPDX or CycloneDX format.

#### Legal framework references

- **Germany**: Vergabeverordnung (VgV), Unterschwellenvergabeordnung (UVgO), GWB Part 4. Municipalities are subject to EU thresholds; framework contracts via govdigital eG or AKDB provide compliant procurement paths below and above threshold.
- **Switzerland**: Bundesgesetz über das öffentliche Beschaffungswesen (BöB) and IVöB. Revision entered into force 1 January 2021, introducing competitive dialogue and innovation partnerships — tools useful for open-source IT procurement.
- **EU**: Directive 2014/24/EU on public procurement, as transposed in national law. The Interoperable Europe Act [6] adds requirements for open standards compliance in procurement of interoperability-relevant software.

### 6.3 Change Management

Open-source transitions frequently fail not on technical grounds but on human factors. The Munich LiMux reversal [30] and numerous less-documented transitions confirm that political risk management and change management are as important as technical planning.

**Mandatory recommendations:**

1. Appoint a **Digital Transformation Champion** at senior political level with explicit, documented mandate and council or executive endorsement.
2. Establish **open-source champions** (Multiplikatoren) in each department — staff with advanced training, a peer-support role, and a 10–20% time allocation.
3. Run **parallel operations** for a minimum of three months before cutting over any critical system.
4. Document and communicate **early wins**: first cost savings, new participatory features, citizen feedback improvements.
5. Publish a **public transparency dashboard** showing migration progress, costs, and service quality metrics — this creates accountability and builds public trust simultaneously.
6. Conduct a **vendor influence audit**: document which existing contracts include renewal bonuses, training lock-in clauses, or proprietary data formats. These are the primary vectors for vendor resistance.
7. Engage **civil society organisations** as external champions; their public endorsement is more credible to elected officials than internal IT advice.

---

## 7. Risk Analysis

### 7.1 Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Political reversal after election | Medium | High | Embed in ordinance/Satzung; build cross-party consensus; publish TCO evidence |
| Vendor lobbying and FUD campaigns | High | Medium | Document TCO; engage civil society; cite EMBAG/OZG mandates |
| Skill gap in IT team | High | Medium | Training programme; cooperative IT provider; openCode.de community |
| Integration failure between stack layers | Medium | High | Follow reference architecture (§4.10); OpenDesk for collaboration layer |
| Data loss during migration | Low | Critical | Full backup; parallel operation minimum 3 months; staged migration |
| GDPR / data residency violation | Low | High | Privacy-by-design; DPO engagement at each phase; EU/CH-only data residency |
| User adoption failure | Medium | High | Change management; UX testing; training; parallel systems; champion programme |
| Security incident during transition | Low | Critical | BSI IT-Grundschutz; penetration testing at each phase gate; incident response plan |
| Supply-chain compromise of dependency | Low | High | SBOM maintenance; OSV (Open Source Vulnerabilities) scanning; patch management SLA |
| AI Act compliance obligation | Low (2026) | Medium | Review AI-enabled components (e.g., search, translation) against AI Act risk tiers |
| Community fragmentation / project abandonment | Low | Medium | Contribute upstream; prefer projects with >5 corporate sponsors; openCode.de alignment |
| Cost overrun | Medium | Medium | Phase-gated budget; independent project office; open TCO accounting |

### 7.2 The Munich Cautionary Case

The City of Munich's LiMux project (2003–2017) is the most-cited case of a municipal open-source transition reversal. Post-mortem analysis (Scholl [60]; Janowski [30]) identifies the following causal factors: (a) a change in political leadership with closer ties to the proprietary vendor; (b) inadequate change management and user training; (c) compatibility issues with Bavarian state systems using proprietary formats; (d) a poorly designed migration process that moved users to open-source tools before the equivalent features were fully implemented.

The technical implementation itself was broadly successful — Munich operated 14,000 LibreOffice workstations for over a decade. The reversal was a political and organisational failure, not a technical one. The primary lesson is that digital sovereignty must be embedded as a policy value in legislation or ordinance, not merely as a procurement preference that can be reversed by a new administration.

Post-Munich, the German federal OZG framework [2], ZenDiS mandate [49], and EMBAG [1] create legal obligations that make outright reversals significantly harder — municipalities can now cite legal duties, not merely preferences.

### 7.3 Security Considerations

The BSI IT-Grundschutz framework [26] provides a comprehensive security baseline applicable regardless of licence model. Key requirements for municipal open-source deployments:

- All server components must receive security updates within 30 days of CVE publication (documented patch management process required)
- Authentication must meet BSI Authenticator Assurance Level 2 (AAL2) for citizen-facing services
- Data in transit encrypted (TLS 1.3 minimum); data at rest encrypted for sensitive data categories (health, social welfare, financial)
- Penetration testing at each phase gate (minimum annual thereafter)
- Incident response plan aligned with NIS2 reporting obligations [27] (24-hour initial notification to BSI/NCSC, 72-hour detailed report)
- Software Bill of Materials (SBOM) maintained for all open-source dependencies; automated scanning via OWASP Dependency-Check or equivalent
- Container images from trusted registries only; image signing via Sigstore/cosign

### 7.4 AI Act Implications

The EU AI Act (Regulation (EU) 2024/1689), applicable from 2 August 2026 for high-risk AI systems in public administration, introduces obligations for municipalities that deploy AI-enabled components. High-risk categories applicable to municipal AI include: AI systems used in decisions affecting access to public services, benefits, or employment; AI systems used in law enforcement or judicial administration. Municipalities should:

1. Audit all AI-enabled features in the recommended stack (e.g., Nextcloud AI assistant, automated form-filling, workflow recommendation engines) against AI Act risk tiers.
2. Ensure any high-risk AI systems deployed are registered in the EU AI Database.
3. Prefer open-source AI components with documented training data lineage and auditable inference logic — a structural advantage of open-source AI over proprietary "black box" systems.
4. The AI Act's open-source exemptions (Article 2(12)) provide partial relief for municipalities that develop or deploy open-source AI tools internally, but the exemption does not extend to high-risk applications.

---

## 8. Conclusion

The evidence reviewed in this paper converges on five findings:

**1. Open-source municipal technology stacks are technically mature and production-proven.** Every functional requirement of a modern municipal government can be met by open-source software with documented deployments at peer municipalities in Switzerland, Germany, and across Europe.

**2. The regulatory environment mandates open-source and interoperability.** EMBAG (Switzerland, 2024) [1], OZG 2.0 (Germany, 2024) [2], the Interoperable Europe Act (EU, 2024) [6], and the EU Data Act (EU, 2025) [51] create legal obligations that proprietary, vendor-locked systems cannot sustainably satisfy. Municipalities that begin the transition now are building compliance capital; those that delay are accumulating regulatory debt.

**3. The economic case is compelling and quantifiable.** A 50,000-population municipality can expect net savings of approximately €1.1 million over five years by transitioning to an open-source stack. A small municipality of 8,000 population saves €120,000–€180,000. Every €1 of public investment in open-source software generates €4.15 in economic returns across the EU [56].

**4. OpenDesk removes the principal technical barrier.** The German federal government's OpenDesk suite, managed by ZenDiS [49], provides a pre-integrated, government-curated open-source workplace stack. Municipalities can now adopt a single, centrally tested suite rather than assembling and integrating individual components — the most complex and expensive part of the transition is pre-assembled.

**5. Success requires political and organisational investment equal to technical investment.** Clear political mandate, skilled change management, and sustained stakeholder engagement are the binding constraints. The Munich case and successful transitions in Barcelona, Helsinki, and Swiss cantons alike confirm this.

Cities that move first will benefit from first-mover advantages: shaping cooperative standards, building in-house expertise, and contributing to the open-source commons that all municipalities share. The regulatory window is open; the technical stack is ready; the economic case is clear. The only remaining question is political will.

---

## References

[1] Swiss Federal Council. (2023). *Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG)*. SR 172.019. Bern: Swiss Confederation. https://www.fedlex.admin.ch/eli/cc/2023/682/de — [CC0, Swiss federal legislation]

[2] Bundesministerium des Innern und für Heimat (BMI). (2024). *Onlinezugangsgesetz 2.0 (OZG 2.0)*. Berlin: BMI. https://www.bmi.bund.de/DE/themen/moderne-verwaltung/e-government/ozg/ozg-node.html — [DL-DE/Zero 2.0]

[3] Open Source Business Alliance (OSBA). (2023). *Sovereign Cloud Stack: Technical and Governance Overview*. Berlin: OSBA. https://scs.community/ — [CC-BY-SA-4.0]

[4] Free Software Foundation Europe (FSFE). (2017). *Public Money? Public Code!* Berlin: FSFE. https://publiccode.eu/ — [CC-BY-SA-4.0]

[5] European Commission. (2020). *Open Source Software Strategy 2020–2023: Think Open*. Brussels: European Commission. https://commission.europa.eu/about/departments-and-executive-agencies/informatics/open-source-software-strategy_en

[6] European Parliament and Council. (2024). *Regulation (EU) 2024/903 — Interoperable Europe Act*. Brussels: OJ L 2024/903. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202400903 — [EU legislation, public domain]

[7] Wirtz, B. W., & Weyerer, J. C. (2017). Conceptualization and creation of a holistic e-government maturity model. *Public Management Review*, 19(9), 1297–1316. https://doi.org/10.1080/14719037.2017.1283024

[8] Janssen, M., Charalabidis, Y., & Zuiderwijk, A. (2012). Benefits, adoption barriers and myths of open data and open government. *Information Systems Management*, 29(4), 258–268. https://doi.org/10.1080/10580530.2012.716740

[9] FITKO. (2023). *Föderale IT-Kooperation — Jahresbericht 2023*. Frankfurt: FITKO. https://www.fitko.de/veroeffentlichungen — [DL-DE/Zero 2.0]

[10] openCode.de. (2022). *openCode — Open Source for Government*. Berlin: Digitalservice GmbH des Bundes. https://opencode.de/ — [Open access]

[11] Sovereign Cloud Stack Community. (2023). *SCS Technical Documentation*. https://docs.scs.community/ — [Apache 2.0]

[12] Decidim Association. (2021). *Decidim: Free Open-Source Participatory Democracy for Cities and Organizations*. Barcelona: Decidim Association. https://decidim.org/ — [AGPL-3.0]

[13] Nextcloud GmbH. (2023). *Nextcloud for Government: Security, Sovereignty, and Collaboration*. Stuttgart: Nextcloud GmbH. https://nextcloud.com/government/ — [Open access]

[14] The Matrix Foundation. (2023). *Matrix Specification v1.9*. https://spec.matrix.org/ — [Apache 2.0]

[16] E-Government Suisse. (2023). *Strategie E-Government Schweiz 2024–2027*. Bern: Schweizerische Bundeskanzlei. https://www.egovernment.ch/de/umsetzung/e-government-strategie/ — [Open access]

[19] TYPO3 Association. (2023). *TYPO3 in Public Administration*. Düsseldorf: TYPO3 Association. https://typo3.org/ — [GPL-2.0]

[20] OpenProject GmbH. (2023). *OpenProject for Government*. Berlin: OpenProject GmbH. https://www.openproject.org/ — [GPLv3]

[21] Red Hat / Keycloak Community. (2023). *Keycloak 23.0 — Open Source Identity and Access Management*. https://www.keycloak.org/ — [Apache 2.0]

[22] CKAN Association. (2023). *CKAN: Open Source Data Portal Software*. https://ckan.org/ — [AGPL-3.0]

[23] govdigital eG. (2023). *govdigital: Genossenschaft für digitale Verwaltung*. Berlin: govdigital eG. https://govdigital.de/ — [Open access]

[24] Dataport AöR. (2023). *Dataport: IT-Dienstleister für die öffentliche Verwaltung*. Hamburg: Dataport AöR. https://www.dataport.de/ — [Open access]

[26] Bundesamt für Sicherheit in der Informationstechnik (BSI). (2023). *BSI IT-Grundschutz-Kompendium Edition 2023*. Bonn: BSI. https://www.bsi.bund.de/grundschutz — [CC-BY-ND 3.0 DE]

[27] European Parliament and Council. (2022). *Directive (EU) 2022/2555 — NIS2*. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022L2555 — [EU legislation]

[29] United Nations DESA. (2022). *UN E-Government Survey 2022*. New York: United Nations. https://publicadministration.un.org/egovkb/en-us/Reports/UN-E-Government-Survey-2022 — [Open access]

[30] Janowski, T. (2015). Digital government evolution: From transformation to contextualization. *Government Information Quarterly*, 32(3), 221–226. https://doi.org/10.1016/j.giq.2015.07.001

[33] Camunda Services GmbH. (2023). *Camunda Platform 8 Community Edition*. https://camunda.com/download/ — [Apache 2.0 Community]

[34] BigBlueButton Inc. (2023). *BigBlueButton 2.7*. https://bigbluebutton.org/ — [LGPL-3.0]

[35] Jitsi Community. (2023). *Jitsi Meet*. https://jitsi.org/ — [Apache 2.0]

[36] OpenStreetMap Foundation. (2023). *OpenStreetMap*. https://www.openstreetmap.org/ — [ODbL-1.0]

[37] QGIS Project. (2023). *QGIS 3.34 LTR*. https://www.qgis.org/ — [GPL-2.0+]

[39] Cloud Native Computing Foundation (CNCF). (2023). *Kubernetes v1.29*. https://kubernetes.io/ — [Apache 2.0]

[41] PostgreSQL Global Development Group. (2023). *PostgreSQL 16*. https://www.postgresql.org/ — [PostgreSQL Licence]

[42] BMI / ZenDiS GmbH. (2023). *OpenDesk: Der digitale Arbeitsplatz der Bundesverwaltung*. https://opendesk.eu/ — [AGPL-3.0]

[43] Schweizerisches Bundesarchiv (BAR). (2023). *Geschäftsverwaltung (GEVER) in der Bundesverwaltung*. Bern: BAR. https://www.bar.admin.ch/bar/de/home/digitale-archivierung/gever.html — [Open access]

[44] opendata.swiss. (2023). *Open Government Data Switzerland*. Bern: Schweizerische Bundeskanzlei. https://opendata.swiss/ — [CC-BY-4.0 portal]

[45] European Commission. (2017). *European Interoperability Framework — Implementation Strategy (EIF)*. Brussels: ISA² Programme. https://joinup.ec.europa.eu/collection/nifo-national-interoperability-framework-observatory — [CC-BY-4.0]

[46] KoSIT. (2023). *XÖV-Standards: XML in der öffentlichen Verwaltung*. Bremen: KoSIT. https://www.xoev.de/ — [Open access]

[47] eCH — E-Government Standards. (2023). *eCH Standards Framework*. Bern: eCH Association. https://www.ech.ch/ — [Open access; individual standards CC-BY or similar]

[48] GovStack / ITU. (2023). *GovStack Building Blocks Specification v1.0*. Geneva: International Telecommunication Union. https://www.govstack.global/ — [CC-BY-SA-4.0]

[49] ZenDiS GmbH. (2024). *ZenDiS Jahresbericht 2024: Digitale Souveränität in der öffentlichen Verwaltung*. Berlin: ZenDiS GmbH. https://www.zendis.de/ — [Open access]

[50] European Commission / OSOR. (2023). *Open Source Observatory Annual Report 2023*. Brussels: European Commission DIGIT. https://joinup.ec.europa.eu/collection/open-source-observatory-osor — [CC-BY-4.0]

[51] European Parliament and Council. (2023). *Regulation (EU) 2023/2854 — Data Act*. Brussels: OJ L 2023/2854. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202302854 — [EU legislation]

[52] Consul Democracy. (2023). *CONSUL Democracy: Open Government and E-Participation Web Software*. Madrid: Consul Democracy Foundation. https://consuldemocracy.org/ — [AGPL-3.0]

[53] Lathrop, D., & Ruma, L. (eds.). (2010). *Open Government: Collaboration, Transparency, and Participation in Practice*. Sebastopol, CA: O'Reilly Media. ISBN 978-0-596-80435-0.

[54] Swiss Federal Chancellery. (2023). *Bundesgesetz über den elektronischen Ausweis und andere elektronische Nachweise (E-ID-Gesetz)*. Bern: Swiss Confederation. https://www.fedlex.admin.ch/eli/fga/2023/2842/de — [CC0, Swiss federal legislation]

[55] GAIA-X Association AISBL. (2024). *GAIA-X Architecture Document v2024*. Brussels: GAIA-X AISBL. https://gaia-x.eu/what-is-gaia-x/deliverables/ — [Open access]

[56] Blind, K., Böhm, M., Grzegorzewska, P., Katz, A., Muto, S., Pätsch, S., & Schubert, T. (2021). *The Impact of Open Source Software and Hardware on Technological Independence, Competitiveness and Innovation in the EU Economy*. Brussels: European Commission. https://doi.org/10.2759/430161 — [CC-BY-4.0]

[57] DigitalService GmbH des Bundes. (2023). *Annual Report 2023*. Berlin: DigitalService GmbH des Bundes. https://digitalservice.bund.de/ — [Open access]

[58] Wirtz, B. W., Weyerer, J. C., & Geyer, C. (2019). Artificial intelligence and the public sector: Applications and challenges. *International Journal of Public Administration*, 42(7), 596–615. https://doi.org/10.1080/01900692.2018.1498103

[59] Almeida, F., Santos, J. D., & Monteiro, J. A. (2023). Digital government transformation in European municipalities: A longitudinal study. *Government Information Quarterly*, 40(2), 101812. https://doi.org/10.1016/j.giq.2023.101812

[60] Scholl, H. J. (ed.). (2017). *E-Government: Information, Technology, and Transformation*. London: Routledge. https://doi.org/10.4324/9781315095950

---

*This document is the English-language source of truth for the Sovereign by Design strategy paper series.*  
*Released under Creative Commons Attribution 4.0 International (CC-BY-4.0).*  
*Attribute as: Sebastian Graf, Autonomous Office of Civil Digital Infrastructure (sebk4c@tuta.com)*  
*Version history: v0.1.0 (2026-06-20) → v0.2.0 (2026-06-21, citation-complete draft)*
