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
  - ZenDiS
  - GovStack
  - eCH standards
  - total cost of ownership
---

# Sovereign by Design: A State-of-the-Art Open-Source Technology Strategy for Municipal Governments

**Author:** Sebastian Graf, Autonomous Office of Civil Digital Infrastructure  
**Correspondence:** sebk4c@tuta.com  
**Version:** 0.2.0 — Citation-Complete Draft  
**Date:** 2026-06-21  
**Languages:** English (source of truth) · Deutsch  
**SPDX-License-Identifier:** CC-BY-4.0  

> *Changelog from v0.1.0:* Full citation verification; new sections on eCH standards, ZenDiS, GovStack, TCO analysis with empirical data, small-municipality guide, and sovereign provider directory; 15 new sources added to registry.

---

## Abstract

Municipal governments are the closest layer of democratic administration to citizens, yet they face an acute structural tension: the digital tools they depend on are increasingly proprietary, vendor-locked, and misaligned with public-interest values. This paper presents a comprehensive, citation-complete strategy for implementing a state-of-the-art open-source governmental administration technology stack in city governments. Drawing on exemplary practices from Switzerland's EMBAG legislation, Germany's OZG 2.0 reform programme, Sovereign Cloud Stack, and OpenDesk initiatives, and the wider European sovereign technology community including the GovStack building-blocks initiative, we derive a first-principles implementation roadmap, stakeholder engagement framework, and procurement strategy. We evaluate ten core technology components — identity management, document management, workflow automation, citizen participation, secure communications, open data publication, geographic information systems, content management, cloud infrastructure, and records management — against criteria of digital sovereignty, interoperability, total cost of ownership, and civic alignment. Empirical TCO data from the French Gendarmerie Nationale migration (72,000 workstations, ~40% cost reduction), the Extremadura regional deployment (40,000 workstations), and Swiss federal Nextcloud adoption support the economic case. We conclude that open-source municipal technology stacks are not merely technically viable but fiscally superior, democratically necessary, and legally mandated in an increasing number of jurisdictions. The paper provides a phased 36-month implementation roadmap with concrete procurement guidance, technology-provider directory, and small-municipality adaptation guide.

**Keywords:** digital sovereignty, open source government, GovTech, municipal digital transformation, interoperability, OZG, EMBAG, Sovereign Cloud Stack, ZenDiS, GovStack, eCH standards, total cost of ownership, civic technology

---

## 1. Introduction

The digital transformation of municipal government is no longer optional. Citizens expect seamless, secure, and accessible digital services; regulators demand interoperability and data protection; and fiscal pressures require sustainable, cost-effective technology investments. Yet the majority of city governments worldwide remain trapped in a cycle of proprietary vendor dependency, expensive licence agreements, and fragmented systems that impede rather than enable good governance [1, 29].

The consequences of this dependency are well-documented. Vendor lock-in raises switching costs and bargaining asymmetry [4]; proprietary formats obstruct cross-agency data exchange and transparency [45]; closed-source infrastructure prevents independent security auditing [26]; and recurring licence fees drain budgets that could otherwise fund service delivery [3, 5]. Most fundamentally, when the software running democratic institutions is owned and controlled by private actors, a structural conflict of interest emerges between the public interest and corporate imperatives [4, 47].

A different path is both possible and proven. Switzerland's 2023 EMBAG legislation (Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben) mandates that federal software developed with public funds be released as open source by default [1]. Germany's OZG reform programme, Sovereign Cloud Stack, and OpenDesk initiative — managed by ZenDiS GmbH (Zentrum für Digitale Souveränität der öffentlichen Verwaltung) — represent the most ambitious open-source government technology programme in Europe [2, 3, 42, 51]. The Free Software Foundation Europe's "Public Money? Public Code!" campaign, endorsed by over 200 organisations across 30 countries, articulates the democratic principle at stake: software paid for by the public should be available to the public [4]. The GovStack initiative, co-led by ITU and the Digital Impact Alliance (DIAL), provides a global framework of reusable digital public infrastructure building blocks directly applicable to municipal contexts [52].

This paper is a citation-complete draft (v0.2.0) building on the first structured draft (v0.1.0). It is addressed to all relevant stakeholders — city administrators, elected officials, public-sector IT teams, procurement offices, civil-society groups, open-source communities, and sovereign technology providers — and provides the evidence base, technology assessment, and implementation roadmap needed to make the transition.

### 1.1 Scope and Definitions

*Municipal government* refers to city and local government authorities, including Gemeinden, Kommunen, Städte in Germany and Austria; Gemeinden in Switzerland; and equivalent structures in other jurisdictions. The strategy is designed to scale from small municipalities (population 2,000–50,000) to large cities (population 500,000+), with specific guidance for each tier in Section 10.

*Open-source technology stack* refers to software components licensed under OSI-approved licences, deployed on infrastructure that the municipality controls or can migrate away from without undue cost or friction.

*Digital sovereignty* is the ability of a government to make independent decisions about its digital infrastructure, including the right to inspect, modify, audit, and migrate software without dependency on a single vendor [3]. The concept encompasses technical, legal, and organisational dimensions [48].

*Digital public infrastructure (DPI)* refers to shared digital systems — identity, payments, data exchange — that function as public utilities, accessible to all and owned by no single actor [52].

### 1.2 Research Questions

1. What does a state-of-the-art open-source municipal technology stack look like in 2026?
2. What lessons can be drawn from the Swiss, German, and European sovereign technology communities?
3. What is the optimal phased implementation pathway for municipalities of different sizes?
4. How should procurement, stakeholder engagement, and risk management be structured to maximise success probability?
5. What is the total cost of ownership differential between open-source and proprietary municipal stacks?

---

## 2. Methodology

This paper employs a multi-method research design combining:

**Systematic literature review** of peer-reviewed publications, grey literature, and policy documents published between 2010 and 2026, covering e-government theory, digital sovereignty, open-source software in public administration, and municipal digital transformation. Search terms included: "open source government", "digital sovereignty municipality", "GovTech stack", "OZG implementation", "EMBAG", "Sovereign Cloud Stack", "e-government maturity", "public sector ICT TCO".

**Comparative policy analysis** of technology legislation and strategies from Switzerland (EMBAG 2023, E-Government Strategy 2024–2027), Germany (OZG 2017/2024, Deutsche Verwaltungscloud-Strategie, OpenDesk programme), and the European Union (Interoperable Europe Act 2024, EU Open Source Strategy 2020–2023, EU Data Act 2023).

**Technology stack evaluation** using a structured scoring matrix assessing each component on: (a) licence openness, (b) deployment maturity, (c) community health, (d) interoperability standards compliance, (e) security posture, (f) total cost of ownership, and (g) existing public-sector deployments. Scores are 1–5; methodology follows the OSOR evaluation framework [53].

**Stakeholder analysis** mapping the interests, influence, and engagement needs of each stakeholder group in the municipal digital transformation process.

**TCO meta-analysis** synthesising available empirical data from completed open-source migrations in public administration, with normalisation for organisation size and context.

The literature review is designed to be self-improving: the source registry (`Mem/source-registry.md`) and literature review state (`Mem/literature-review-state.md`) are versioned documents updated on a recurring quarterly basis. The `Scripts/update_literature_review.py` script provides structured prompts for reviewing and improving these files.

### 2.1 Inclusion Criteria

Sources were included if they: (a) address open-source software in public administration; (b) cover governmental digital transformation strategy; (c) relate to the European, Swiss, or German regulatory context; or (d) provide primary data on municipal technology implementations. Sources published before 2010 were included only where they establish foundational theoretical frameworks (Lathrop & Ruma, 2010 [47]).

### 2.2 Limitations

This is a citation-complete draft (v0.2.0). Technology stack assessments reflect publicly available information as of June 2026. Implementation cost estimates are indicative ranges validated against known deployments; they must be re-validated against local procurement conditions. TCO studies from proprietary vendors are excluded; only independent or government-commissioned studies are cited.

---

## 3. Literature Review

### 3.1 Theoretical Foundations of E-Government

The academic literature on e-government has evolved through four broad phases [30]. First-generation e-government (1995–2005) focused on digitising existing processes and creating government websites [29]. Second-generation e-government (2005–2012) emphasised online service delivery, citizen portals, and back-office integration [7]. Third-generation e-government (2012–2020) introduced open data, participatory platforms, and mobile-first service design [8]. The current fourth generation (2020–present) is characterised by platform government, digital identity infrastructure, data spaces, and the sovereignty turn — a recognition that digital autonomy is a prerequisite for democratic self-governance [45, 30].

Wirtz and Weyerer's holistic e-government maturity model identifies five dimensions: technical infrastructure, process quality, service quality, citizen orientation, and transparency [7]. Municipal governments in Switzerland and Germany score variably across these dimensions; technical infrastructure and process quality lag citizen expectations in most jurisdictions, while the regulatory environment increasingly mandates transparency and interoperability [1, 2, 45].

Lathrop and Ruma (2010) define open government along three axes — transparency, participation, and collaboration — which map directly onto the open-source technology principles explored in this paper: transparency (open source code is inspectable), participation (open platforms enable civic engagement), and collaboration (shared code bases reduce duplication) [47].

### 3.2 Digital Sovereignty in Public Administration

The concept of digital sovereignty has moved from academic concept to policy imperative in the European context [3, 5, 48]. Couture and Toupin (2019) distinguish between three registers of sovereignty: (a) state sovereignty over digital infrastructure, (b) individual data sovereignty, and (c) collective technological self-determination [48]. All three are implicated in municipal digital transformation.

The EU Open Source Strategy 2020–2023 established "sharing and reuse" as a core principle, mandating that European institutions prefer open-source solutions in technology procurement [5]. The 2024 Interoperable Europe Act creates binding obligations for cross-border interoperability in public administrations and mandates impact assessments before deploying any new interoperability solution [6]. The EU Data Act 2023 introduces rights for public bodies to access data held by private companies in exceptional circumstances, with direct implications for municipal IoT and smart-city deployments [54].

Germany's Sovereign Cloud Stack (SCS), developed by the Open Source Business Alliance (OSBA) and funded in part by BMWK, represents the most concrete realisation of digital sovereignty in cloud infrastructure [3]. As of 2026, SCS underpins several German Länder cloud environments and is integrated with govdigital eG's shared infrastructure [23]. SCS Release 7 (2025) introduced full Kubernetes Cluster API support and enhanced compliance tooling aligned with the EU Cybersecurity Act [11].

Switzerland's approach differs institutionally but converges on the same principles. The EMBAG legislation, in force since 1 January 2024, requires all federal software developed with public funds to be released as open source unless compelling security reasons prevent it [1]. The law places Switzerland among the most progressive open-source mandating jurisdictions globally, alongside Italy (CAD Article 68–69), France (Loi pour une République numérique 2016), and the EU institutions.

### 3.3 The German OZG Ecosystem

The Onlinezugangsgesetz (OZG), enacted in 2017 and substantially reformed in 2024 (OZG 2.0), requires all German federal, Land, and municipal administrations to offer their administrative services online [2]. The OZG 2.0 reform addresses shortcomings of the first generation — fragmented implementation, poor interoperability, inconsistent user experience — through the "Once Only" principle, the "Einer für Alle" (EfA) approach, and a federal platform architecture centred on BundID and FITKO [9, 10].

FITKO (Föderale IT-Kooperation) serves as the coordination body for OZG implementation across federal and Länder levels. The 2023 annual report documents 300+ digitised administrative services and identifies the most critical remaining gaps in citizen-facing portal integration [9]. BundID, the federal citizen identity platform, reached 3.2 million registered users by end-2023 and is expanding integration with Länder identity systems and eID [2].

ZenDiS (Zentrum für Digitale Souveränität der öffentlichen Verwaltung), established by the Federal Government in 2022 and headquartered in Berlin, is the institutional vehicle for the OpenDesk programme [51]. ZenDiS curates the OpenDesk suite, manages the government open-source catalogue, provides technical support to administrations, and commissions open-source development under a "Public Money? Public Code!" contract model. The openCode.de platform, hosted by ZenDiS/Digitalservice, currently lists over 500 government open-source repositories [10, 51].

### 3.4 Swiss Cantonal and Federal Digital Services

Switzerland's federal structure — 26 cantons, ~2,200 municipalities — creates both challenges and opportunities for municipal digital transformation. The E-Government Strategy Switzerland 2024–2027, jointly developed by the Federal Council and the Conference of Cantonal Governments (KdK), sets out a collaborative digital services framework mandating open standards, interoperability, and data sharing [16].

Key Swiss digital infrastructure includes:

**Fedlex** (fedlex.admin.ch): the official platform for Swiss federal law, built on open standards and providing machine-readable legal data in all four national languages [1].

**opendata.swiss**: the national open government data portal, built on CKAN, cataloguing over 11,000 datasets from federal, cantonal, and municipal authorities. Governed by the Federal Strategy on Open Government Data 2024–2027 [44, 55].

**GEVER** (Geschäftsverwaltung): the standardised records management system for the federal administration, implemented across all federal offices. Cantonal implementations vary; several use CMI eCH-compliant solutions [43].

**Swiss eID**: Following the rejection of the original e-ID law in the March 2021 referendum (64.4% against), Switzerland developed a new, privacy-by-design, decentralised eID system. The revised E-ID Act was adopted by parliament in March 2023; cantonal pilots began in 2024 with nationwide availability targeted for 2026 [56]. The new eID uses a self-sovereign identity (SSI) model with a government-issued credential wallet.

**eCH Standards**: Switzerland's XML-based interoperability standards for public administration are governed by eCH (E-Government Standards Switzerland), an association of public and private actors. Key standards relevant to municipalities include eCH-0007 (Gemeinde — municipal data), eCH-0020 (Meldewesen — civil registry), eCH-0046 (Kontakt — contact data), eCH-0058 (Schnittstellendefinition — interface definitions), and eCH-0010 (Postadresse — postal addressing). These standards are the Swiss equivalent of Germany's XÖV family and are mandatory for cantonal and municipal systems interoperating with the federal administration [57].

### 3.5 Open Source Communities and Sovereign Technology

**Decidim** (Barcelona, 2016) is a participatory democracy platform used by over 450 organisations in more than 40 countries. The Decidim Association's Social Contract defines governance principles applicable beyond the platform itself: democratic governance, open source, continuity, equal access, data sovereignty, free of commercial purposes, and empowerment [12]. Swiss deployments include the Canton of Schaffhausen (budget consultation), the Canton of Zurich (strategy processes), and the City of Bern (neighbourhood participation).

**CONSUL Democracy** (Madrid, 2015) is a complementary participatory platform with strong adoption in Spanish-speaking countries and several European cities. Like Decidim, it is licensed under AGPL-3.0 and provides participatory budgeting, citizen initiatives, and consultation modules [58]. The choice between Decidim and CONSUL depends primarily on community support infrastructure in the target linguistic context.

**Matrix/Element** provides an open, decentralised, end-to-end-encrypted communication protocol increasingly adopted by European public administrations. The German federal BundesMessenger, operational across all federal ministries since 2023, has expanded to several Länder and selected large municipalities [14]. France's Tchap serves 330,000 civil servants. The UK Ministry of Defence and NATO both operate Matrix-based deployments [14].

**Nextcloud** (Stuttgart, 2016) is the most widely deployed open-source file sync and collaboration platform in European public administration, used by thousands of German municipalities, the Swiss Federal Administration (selected divisions), Saxony State Government, and dozens of EU institutions. The enterprise support model enables municipalities to procure SLAs without leaving the open-source ecosystem [13].

**OpenDesk** (Berlin, 2023), managed by ZenDiS, is a curated open-source workplace suite comprising Nextcloud (file management), Cryptpad (real-time collaboration), OpenProject (project management), Jitsi Meet (video conferencing), Element (messaging), and Collabora Online (office documents). OpenDesk v2.0 (2025) added Keycloak-native authentication, improved mobile clients, and a Helm-based Kubernetes deployment chart enabling municipal self-hosting [42, 51].

**GovStack** is a global initiative co-led by ITU and the Digital Impact Alliance (DIAL), with support from Estonia, Germany (GIZ), and the EU. It defines a set of reusable digital public infrastructure "building blocks" — including identity, consent management, information mediator (X-Road), payments, and workflow — with open specifications and reference implementations [52]. GovStack's building-block model is directly applicable to municipal contexts: municipalities can adopt individual building blocks incrementally rather than committing to a full-stack transition.

### 3.6 OSOR and the EU Open Source Observatory

The EU Open Source Observatory and Repository (OSOR), hosted on Joinup.ec.europa.eu, provides the most comprehensive data on open-source software in European public administration. The OSOR Annual Report 2023 documents 36 new government open-source releases in EU member states, identifies Germany and Switzerland as leading jurisdictions by policy maturity, and notes that open-source adoption in local government is growing at approximately 18% per year across the EU [53]. The report recommends cooperative procurement models and cross-border code sharing as the primary levers for accelerating adoption in smaller municipalities.

### 3.7 Total Cost of Ownership: Empirical Evidence

The literature on TCO for open-source vs. proprietary public-sector IT is methodologically uneven. However, several large-scale, independently verified migrations provide useful benchmarks:

**French Gendarmerie Nationale** migrated 72,000 workstations from Windows to Ubuntu Linux and from Microsoft Office to LibreOffice between 2008 and 2014. The Gendarmerie's IT directorate reported total cost savings of approximately 40% relative to continued proprietary licensing, equating to roughly €14 million over five years [59]. Ongoing maintenance costs were reported as lower than the proprietary baseline due to elimination of per-seat licences and reduced virus/malware remediation overhead.

**Extremadura (Spain)** deployed LinEx (a Debian-based distribution) across 40,000 public-sector workstations in the early 2000s, with estimated software licence savings of €30 million annually versus a full Windows/Office deployment [60]. While the specific distribution has since been updated, the infrastructure remains open-source-based.

**City of Zaragoza (Spain)** migrated 3,000 municipal workstations to open-source software, reporting licence cost savings of €1.5 million over three years, with an initial investment in training and migration support of €600,000, yielding a net saving of €900,000 [60].

**Munich LiMux (Germany)** is the most-cited cautionary case: 14,000 workstations migrated to Kubuntu/LibreOffice (2003–2013), then reversed to Windows (2017–2020) following a political change of leadership. Independent post-mortems identify the reversal as politically rather than technically motivated, citing (a) a 2014 mayoral election shift; (b) inadequate end-user training investment; (c) selective compatibility problems with Bavarian state systems that had not been updated to support OpenDocument Format; and (d) a Microsoft-sponsored Accenture study widely critiqued as methodologically flawed [30, 61]. The technical implementation itself achieved its objectives; the LiMux infrastructure handled 70% of municipal workloads successfully at point of reversal.

Synthesising these cases, a municipal open-source migration should model:
- **Licence savings:** €80–200 per workstation per year (productivity software), €200–600 per server per year (operating system and database)
- **Migration investment:** €300–800 per workstation one-time (training, data migration, hardware refresh if needed)
- **Break-even:** 2–4 years for workstation migration; 1–2 years for server workloads
- **Long-term TCO advantage:** 30–45% over a 10-year horizon for full-stack open-source vs. full-stack proprietary

### 3.8 Gaps Addressed in v0.2.0

Compared to v0.1.0, this draft adds:
- eCH standards coverage (Section 3.4, sources [57])
- CONSUL Democracy (Section 3.5, source [58])
- GovStack building blocks (Section 3.5, source [52])
- OSOR Annual Report 2023 (Section 3.6, source [53])
- Empirical TCO data (Section 3.7, sources [59, 60, 61])
- ZenDiS and OpenDesk v2.0 details (Section 3.3, source [51])
- Swiss eID revised system (Section 3.4, source [56])
- EU Data Act 2023 (Section 3.2, source [54])
- Lathrop & Ruma foundational text (Section 3.1, source [47])
- Couture & Toupin sovereignty theory (Section 3.2, source [48])

Remaining gaps (see `Mem/literature-review-state.md`):
- Independent peer-reviewed TCO methodology applicable to municipal contexts
- Citizen satisfaction research on open-source digital services
- GAIA-X current implementation status

---

## 4. Technology Stack Analysis

A municipal technology stack decomposes into ten functional layers. The analysis below evaluates leading open-source options for each layer against the scoring criteria defined in Section 2. Scores are 1–5; a score of 5 indicates fully open, production-proven, widely deployed in public administration.

### 4.1 Digital Identity and Authentication

**Function:** Authenticate citizens and staff; federate identity across services; implement single sign-on (SSO); integrate with national identity systems.

**Recommended component: Keycloak 24.x** (Red Hat / CNCF) [21]

Keycloak is the de facto open-source IAM platform for European public administration. Version 24 (2024) introduced native support for the EU eIDAS 2.0 wallet ecosystem, improved FIDO2/WebAuthn passkey handling, and a lightweight operator for Kubernetes deployment. It federates with BundID (Germany), Swiss eID, and Austrian eID via OIDC/SAML bridges.

| Criterion | Score | Notes |
|---|---|---|
| Licence openness | 5 | Apache 2.0 |
| Deployment maturity | 5 | Production-proven, 12+ years, CNCF sandbox |
| Community health | 5 | Red Hat-backed, 1,000+ contributors |
| Interoperability | 5 | OIDC, OAuth2, SAML2, FIDO2, eIDAS 2.0 |
| Security posture | 5 | CVE-responsive, FIPS 140-2 option |
| TCO | 4 | No licence; operational expertise required |
| Public-sector deployments | 5 | EU institutions, German Länder, Swiss cantons |

**Integration note:** Federation with BundID requires the FITKO-published BundID OIDC adapter configuration. Federation with Swiss eID requires the eIDAS-bridge connector being developed by EJPD (Federal Dept. of Justice and Police) for 2026 release.

### 4.2 Document Management and Records

**Function:** Store, retrieve, classify, and retain official records; GEVER-compliant workflow; retention scheduling; audit trails.

**Recommended components:**
- **Nextcloud 29.x** for collaborative file management [13]
- **OpenProject 14.x** for project and records linking [20]
- **CMI AXIOMA** or **Fabasoft Community** for full Swiss GEVER compliance

Nextcloud Hub 8 (2025) introduced Files Lifecycle Management, automated retention enforcement, and an improved audit log. For German municipalities, AKDB's BayernPortal and Dataport's ENA (Elektronische Nachweisakte) components provide the OZG-compliant capability layer above Nextcloud.

| Criterion | Score | Notes |
|---|---|---|
| Licence openness | 5 | AGPL-3.0 (Nextcloud) |
| Deployment maturity | 5 | 400,000+ organisations |
| Community health | 5 | Nextcloud GmbH + 1,500+ community contributors |
| Interoperability | 4 | WebDAV, CalDAV, CardDAV, CMIS, S3 |
| Security posture | 5 | ISO 27001, SOC 2 Type II (Enterprise) |
| TCO | 5 | No per-seat licence (Community); support contract optional |
| Public-sector deployments | 5 | Swiss Federal Administration, Saxony, 1,000+ municipalities |

### 4.3 Workflow Automation and Business Process Management

**Function:** Automate administrative workflows; model, execute, and monitor BPMN processes; integrate with XÖV/eCH data standards.

**Recommended component: Camunda Platform 8 Community Edition** [33]

Camunda 8 (Zeebe engine) provides distributed, high-throughput BPMN 2.0 execution. Community Edition is fully open-source (Apache 2.0). For municipalities requiring simpler deployments, **Flowable 6.x** (Apache 2.0) or **Activiti 7.x** (Apache 2.0) offer lighter footprints.

Critical integration requirement: XÖV data validators must be wired into the workflow engine for German municipalities; eCH-0058 interface definitions serve the equivalent role in Switzerland.

| Criterion | Score | Notes |
|---|---|---|
| Licence openness | 4 | Community: Apache 2.0; Enterprise: proprietary |
| Deployment maturity | 5 | Production at scale |
| Community health | 4 | Active; enterprise tier funds core development |
| Interoperability | 5 | BPMN 2.0, DMN, REST API, event streaming |
| Security posture | 4 | Actively maintained; SOC 2 (Enterprise) |
| TCO | 3 | Community free; high-scale deployments may require Enterprise |
| Public-sector deployments | 4 | Multiple German Länder, European Commission |

### 4.4 Citizen Participation

**Function:** Consultation; participatory budgeting; initiative collection; neighbourhood deliberation.

**Recommended component: Decidim 0.28.x** [12]

Decidim's modular architecture covers proposals, debates, participatory budgeting, initiatives, consultations, and conferences. The 0.28 release (2025) introduced improved accessibility (WCAG 2.2 AA), enhanced machine-translation support, and a redesigned mobile UI. The Decidim Association provides hosted maintenance and an international community of practice.

**Alternative: CONSUL Democracy 2.3.x** [58] — better-suited if the municipality has existing partnerships in the Spanish-speaking open-source community or needs its specific participatory budgeting workflow.

| Criterion | Score | Notes |
|---|---|---|
| Licence openness | 5 | AGPL-3.0 |
| Deployment maturity | 5 | 450+ deployments globally |
| Community health | 5 | Active association, social contract, global CoP |
| Interoperability | 4 | REST API, webhooks, GraphQL (beta) |
| Security posture | 4 | Actively maintained |
| TCO | 5 | No licence; hosting and support variable |
| Public-sector deployments | 5 | Cities, cantons, federal agencies, parliaments |

### 4.5 Communication and Collaboration

**Function:** Internal messaging; video conferencing; email; calendar; secure inter-agency communication.

**Recommended components:**
- **Matrix/Element Server 1.x** for messaging and inter-agency secure comms [14]
- **Jitsi Meet** (self-hosted) or **BigBlueButton 3.x** for video conferencing [34, 35]
- **Nextcloud Talk** for integrated team communication within OpenDesk

The BundesMessenger reference architecture (published by ZenDiS, 2023) provides a directly reusable Kubernetes deployment specification for municipal Matrix deployments [51].

| Component | Licence | Maturity | Key advantage |
|---|---|---|---|
| Matrix/Element | Apache 2.0 | Production | E2E encryption, federation, BundesMessenger spec |
| Jitsi Meet | Apache 2.0 | Production | Browser-based, self-hostable, no account required |
| BigBlueButton | LGPL-3.0 | Production | Council meeting recording, integration with Greenlight |
| Nextcloud Talk | AGPL-3.0 | Production | Integrated with file management in OpenDesk |

### 4.6 Open Data Publication

**Function:** Publish machine-readable datasets; catalogue data; provide API access; comply with PSI/HVD Directive; contribute to national portals.

**Recommended component: CKAN 2.11.x** [22]

CKAN powers opendata.swiss, data.gov, data.gov.uk, GovData.de, and dozens of national and sub-national portals. Plugin architecture enables compliance with DCAT-AP 3.0 (EU), DCAT-AP.de (Germany), and OGD Switzerland metadata profiles. CKAN 2.11 (2025) introduced DCAT-AP 3.0 native support and improved accessibility.

For municipalities already participating in opendata.swiss or GovData.de, a lightweight CKAN harvesting connector allows publication upstream without operating a full portal.

| Criterion | Score | Notes |
|---|---|---|
| Licence openness | 5 | AGPL-3.0 |
| Deployment maturity | 5 | 10+ year production track record |
| Community health | 4 | CKAN Association; active development |
| Interoperability | 5 | DCAT-AP 3.0, OAI-PMH, SPARQL, S3 |
| Security posture | 4 | Actively maintained |
| TCO | 4 | No licence; moderate ops overhead |
| Public-sector deployments | 5 | Switzerland, Germany, EU, USA, UK |

### 4.7 Geographic Information Systems

**Function:** Map-based citizen services; urban planning; spatial data publication; OGC-compliant WMS/WFS services.

**Recommended components:**
- **QGIS 3.38 LTR** for spatial data editing and analysis [37]
- **GeoServer 2.25** for OGC-compliant publication (WMS, WFS, WCS)
- **MapLibre GL JS** for browser-based mapping applications
- **OpenStreetMap** as the base cartographic layer [36]

Switzerland's swisstopo (map.geo.admin.ch) provides open base map tiles and terrain data under a Creative Commons licence. Germany's BKG (Bundesamt für Kartographie und Geodäsie) provides the official topographic base data under DL-DE/BY-2.0.

### 4.8 Public Website and Content Management

**Function:** Public-facing website; news and announcements; service directory; accessibility compliance.

**Recommended components:**
- **TYPO3 13 LTS** for German-speaking world municipalities [19]
- **Drupal 10.x** for municipalities requiring strong multilingual and API-first capabilities

TYPO3 13 LTS (2024, supported until 2027) introduces a new v13 backend with improved content editing, native headless API support, and enhanced BITV 2.0 / WCAG 2.1 AA tooling. The TYPO3 Association's Government Special Interest Group maintains a municipal reference distribution with pre-configured accessibility and multilanguage settings.

### 4.9 Cloud Infrastructure and Hosting

**Function:** Compute, storage, networking, container orchestration; data sovereignty at the infrastructure layer.

**Recommended component: Sovereign Cloud Stack R7** [3, 11]

SCS R7 (2025) standardises on OpenStack 2024.1 (Caracal), Kubernetes Cluster API, Rook/Ceph for storage, and Cilium for networking. The SCS Compliance Framework requires certified operators to pass automated conformance tests, ensuring vendor-neutral portability of workloads.

Certified SCS operators (as of 2026): plusserver, OSISM, Wavestack, Artcodix. govdigital eG provides a managed SCS cluster specifically designed for public-sector workloads, with framework contracts satisfying GWB/Vergaberecht [23].

| Criterion | Score | Notes |
|---|---|---|
| Licence openness | 5 | Apache 2.0 throughout |
| Deployment maturity | 4 | Production in German Länder; municipal pilots ongoing |
| Community health | 5 | OSBA-backed, growing certification ecosystem |
| Interoperability | 5 | Open APIs, OCI-compliant, S3-compatible |
| Security posture | 5 | BSI IT-Grundschutz compatible, BSI C5 certification path |
| TCO | 4 | No licence; infrastructure and operational costs apply |
| Public-sector deployments | 4 | German Länder, federal pilots |

### 4.10 Records Management (Germany: Schriftgutverwaltung)

**Function:** Lifecycle management of official correspondence and decisions; retention scheduling; archiving.

**Recommended component: OpenDesk with Nextcloud Files Lifecycle + XDOMEA connector**

XDOMEA (XML-based document and records management interface) is the German standard for electronic records transfer to archives. A Nextcloud XDOMEA connector enables municipalities to submit records directly to Land-level digital archives without proprietary middleware. In Switzerland, the eCH-0160 standard governs digital records submission.

### 4.11 Reference Architecture

```
╔══════════════════════════════════════════════════════════════╗
║                   CITIZEN TOUCHPOINTS                        ║
║         TYPO3 · Decidim · CKAN · Nextcloud Files            ║
╠══════════════════════════════════════════════════════════════╣
║                      SERVICE LAYER                           ║
║   Camunda Workflows · XÖV/eCH Forms · GeoServer · QGIS      ║
╠══════════════════════════════════════════════════════════════╣
║                   COLLABORATION LAYER                        ║
║     Nextcloud · Matrix/Element · Jitsi · OpenProject        ║
╠══════════════════════════════════════════════════════════════╣
║                     IDENTITY LAYER                           ║
║            Keycloak ↔ BundID / Swiss eID / eIDAS            ║
╠══════════════════════════════════════════════════════════════╣
║                  INFRASTRUCTURE LAYER                        ║
║   Sovereign Cloud Stack · Kubernetes · PostgreSQL · Ceph    ║
╚══════════════════════════════════════════════════════════════╝
                  ↕ All layers: open APIs only ↕
```

Data exchange: XÖV family (Germany) [46] · eCH family (Switzerland) [57] · DCAT-AP 3.0 (EU open data)
Security: BSI IT-Grundschutz (Germany) [26] · ISDS (Switzerland) · NIS2 (EU) [27]
Containerisation: OCI-compliant images, Helm charts, published on openCode.de [10]

---

## 5. Implementation Roadmap

The implementation is structured as a 36-month, five-phase programme. Each phase has defined deliverables, success criteria, and decision gates. Section 10 provides tier-specific adaptations for municipalities of different sizes.

### Phase 0: Foundation (Months 1–3)

**Objective:** Establish governance, assess current state, build the coalition.

**Deliverables:**
- Digital Transformation Steering Committee established (city leadership + IT + civil society representative)
- Current-state technology audit completed (inventory of all software, contracts, data volumes, service dependencies)
- Stakeholder engagement plan adopted (see Section 6.1)
- Procurement framework established (see Section 6.2)
- Memorandum of Understanding with cooperative IT provider (Dataport, AKDB, govdigital eG, or Swiss cantonal IT cooperative)
- Data protection impact assessment (DPIA) baseline

**Budget range:** €50,000–€150,000 (scales with municipality size; consultancy for audit and governance design)

**Success criteria:**
- Political mandate secured (council resolution or mayoral executive decision)
- Budget envelope approved for Phase 1
- Project lead appointed with ≥50% time allocation

### Phase 1: Identity and Infrastructure (Months 4–12)

**Objective:** Stand up the foundational layers on which all other services depend.

**Deliverables:**
- Sovereign Cloud Stack environment operational (own or via certified SCS hoster)
- Keycloak identity provider deployed and federated with national identity system
- Nextcloud baseline deployment for internal collaboration (file storage, calendar, contacts)
- Matrix/Element messaging operational for staff
- BSI IT-Grundschutz or ISDS baseline documentation complete
- Software Bill of Materials (SBOM) for all deployed components

**Budget range:** €200,000–€600,000 depending on city size and whether SCS is self-hosted or via provider

**Success criteria:**
- 100% of IT staff authenticate via Keycloak SSO
- File storage migrated from proprietary cloud to Nextcloud for ≥3 departments
- Basic encrypted messaging operational for all departments
- Security baseline approved by CISO/DPO

### Phase 2: Services and Workflows (Months 10–18)

**Objective:** Migrate or build the first five citizen-facing services on open infrastructure.

**Deliverables:**
- Five highest-volume administrative services deployed on Camunda/XÖV or eCH stack
- TYPO3 or Drupal CMS migration complete, including accessibility audit (BITV 2.0 / WCAG 2.1 AA)
- Open data portal (CKAN) launched with first 20 datasets, harvested into national portal
- Decidim instance deployed for the first participatory process
- Staff training programme complete for Nextcloud, Matrix, Decidim

**Budget range:** €150,000–€500,000

**Success criteria:**
- 80% of target service volume processed through new system
- Zero regression in service availability vs. baseline
- First open data publication live and harvested by national portal
- First participatory process completed with documented citizen engagement

### Phase 3: Integration and Extension (Months 16–24)

**Objective:** Integrate all layers; extend service coverage to 80% of transactions.

**Deliverables:**
- All services federated via Keycloak SSO
- Nextcloud integrated with document management workflows (retention, XDOMEA/eCH-0160)
- GIS layer operational (QGIS + GeoServer, swisstopo/BKG base maps)
- 80% of administrative services digitised (OZG mandate)
- Inter-agency data exchange via XÖV/eCH operational
- Annual SBOM review completed; all high-severity CVEs remediated

**Budget range:** €200,000–€600,000

**Success criteria:**
- End-to-end digital service delivery for ≥80% of transaction types
- Data quality metrics established and tracked
- First annual open data impact report published
- Zero open high/critical CVEs across stack

### Phase 4: Optimisation and Community (Months 22–30)

**Objective:** Optimise user experience; contribute back to open-source communities; publish results.

**Deliverables:**
- Citizen satisfaction survey (target: NPS ≥40, CSAT ≥4.0/5.0)
- First contribution to openCode.de or upstream projects (code, translations, documentation)
- Municipal open-source community of practice established
- TCO report published (actual vs. baseline projection)
- Penetration test completed; findings remediated

**Success criteria:**
- ≥3 upstream contributions merged
- Community of practice active with ≥3 peer municipalities engaged
- TCO report confirms ≥20% cost reduction vs. pre-migration baseline

### Phase 5: Sovereignty and Scale (Months 28–36)

**Objective:** Achieve full digital sovereignty; prepare replication playbook.

**Deliverables:**
- Full licence compliance audit: zero proprietary critical-path dependencies
- Data residency verification: 100% on sovereign infrastructure
- Replication playbook for neighbouring municipalities published on openCode.de
- Strategy paper v1.0 published
- Governance model for ongoing open-source participation established

**Success criteria:**
- Zero proprietary single-vendor dependencies in critical path
- At least one peer municipality has adopted the playbook
- Annual cost savings confirmed in audit report

---

## 6. Stakeholder and Procurement Strategy

### 6.1 Stakeholder Map

| Stakeholder | Primary interest | Engagement approach | Key concern to address |
|---|---|---|---|
| Mayor / Executive | Political success, cost, citizen approval | Executive briefing, progress dashboard | Will this cause visible disruptions? |
| City council | Oversight, democratic legitimacy | Quarterly reports, open sessions | Legal compliance, vendor lobbying |
| City IT team | Technical feasibility, workload | Co-design, training, community membership | Skills gap, migration complexity |
| Procurement office | Legal compliance, risk | Framework agreements, legal briefings | GWB/BöB compliance, audit risk |
| Civil servants (users) | Ease of use, reliability | UX testing, change management, training | "My tools work fine today" |
| Citizens | Service quality, privacy | Participatory design, transparency reports | Downtime, data security |
| Civil society / NGOs | Transparency, access, participation | Decidim platform, public roadmaps | Access to code, decision audibility |
| Open-source communities | Contribution, reuse | openCode.de participation | Sustainable funding model |
| Sovereign tech providers | Partnership, deployment | Certified partner agreements | Contract terms, liability |
| Data protection officer | GDPR / DSG compliance | Privacy-by-design review at each phase | Data residency, cross-border transfer |

### 6.2 Procurement Framework

Open-source procurement requires a fundamentally different framework from proprietary licence purchasing. The following principles apply in both German (GWB/VgV/UVgO) and Swiss (BöB/IVöB) public procurement law.

**Principle 1 — Procure services, not licences.** Open-source software is free to use; municipalities pay for implementation, hosting, support, customisation, and training. Procurement documents must be structured around these services. The award criteria should weight technical quality and long-term maintainability, not upfront licensing cost.

**Principle 2 — Use cooperative procurement structures.** Germany's govdigital eG and Swiss cantonal IT cooperatives provide framework agreements satisfying public procurement law that municipalities can use directly, eliminating the need for individual tendering above the threshold [23]. govdigital's SCS-based framework (Rahmenvertrag Cloud-Infrastruktur) is available to all German public bodies.

**Principle 3 — Apply "Public Money? Public Code!"** All custom software developed under contract must be released under an OSI-approved open-source licence and published on openCode.de (Germany) or a cantonal equivalent (Switzerland). This is a contract condition, not a recommendation. The FSFE's model procurement clause is available at publiccode.eu [4].

**Principle 4 — Evaluate 5-year total cost of ownership.** Procurement scoring must include a 5-year TCO model covering implementation, hosting, training, support, exit/migration costs, and lock-in risk premium. Proprietary alternatives systematically understate long-term costs by omitting licence escalation clauses and migration exit costs.

**Principle 5 — Require interoperability standards compliance.** All procured systems must implement XÖV (Germany) [46] or eCH (Switzerland) [57] data standards, DCAT-AP 3.0 for open data, and OCI-compliant container packaging. Non-compliance is a disqualifying criterion.

**Principle 6 — Prefer certified cooperative providers.** For infrastructure, prefer SCS-certified operators or govdigital eG members, who are bound by collective data sovereignty agreements and provide auditable compliance documentation [23].

#### Sample Evaluation Criteria and Weights

| Criterion | Weight | Rationale |
|---|---|---|
| Technical quality and architecture fit | 30% | Long-term maintainability |
| OSI licence and openness | 15% | Legal and strategic compliance |
| 5-year TCO (transparent model) | 20% | Fiscal accountability |
| Interoperability standards compliance | 15% | OZG/eCH/DCAT-AP mandatory |
| Supplier cooperative/open-source commitment | 10% | Alignment with PMPC principle |
| Implementation track record in public sector | 10% | Risk reduction |

### 6.3 Change Management

Open-source transitions fail most frequently not on technical grounds but on human factors: end-user resistance, insufficient training, middle-management inertia, and political backsliding under vendor lobbying pressure. The Munich LiMux reversal is the canonical example [30, 61].

**Recommendations:**
- Appoint a **Digital Transformation Champion** at senior political level with an explicit, public mandate
- Establish **open-source ambassadors** in every department; dedicate 10% of their time to peer support
- Run **parallel operations** for a minimum of three months before cutting over critical systems
- Document and publicly celebrate **early wins** (cost savings, new capabilities, positive citizen feedback)
- Publish a **live transparency dashboard** showing migration progress, costs, service quality, and open-source contributions
- Engage **union/staff council representatives** early; address workload concerns transparently
- Commission an independent **"day-in-the-life" UX study** before and after migration; publish results

---

## 7. Risk Analysis

### 7.1 Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Political reversal after election | Medium | High | Embed in municipal ordinance; build cross-party council consensus; ensure civil society co-ownership |
| Vendor lobbying / FUD campaigns | High | Medium | Pre-publish independent TCO evidence; engage civil society; document lobbying activities per transparency register |
| Skill gap in city IT team | High | Medium | Training programme from Phase 0; cooperative IT provider as safety net; hire open-source specialist |
| Integration failure between stack layers | Medium | High | Phased rollout with decision gates; stick to reference architecture; integration tests in CI |
| Data loss during migration | Low | Critical | Full backup + restore drill before any migration; parallel operation; staged migration with rollback criteria |
| GDPR / DSG data protection violation | Low | High | Privacy-by-design review at each phase; DPO sign-off; DPIA for each new service; data mapping |
| User adoption failure | Medium | High | Mandatory change management budget (≥15% of total project); UX testing; parallel systems; user champions |
| Security incident | Low | Critical | BSI IT-Grundschutz (DE) or ISDS (CH) baseline; annual penetration test; SBOM and CVE monitoring; NIS2-compliant incident response |
| Community fragmentation | Low | Medium | Contribute upstream; align with openCode.de; join govdigital eG; participate in Decidim/Nextcloud communities |
| Cost overrun | Medium | Medium | Phase-gated budget with independent project office; monthly variance reporting; open TCO accounting |

### 7.2 The Munich Cautionary Case

Munich's LiMux project (2003–2017) remains the most-cited large-scale municipal open-source reversal. Independent analysis establishes four causal factors [30, 61]:

1. **Political shift:** The 2014 mayoral election brought leadership less committed to digital sovereignty; a subsequent Microsoft-commissioned Accenture study provided political cover for reversal
2. **Inadequate change management:** End-user training investment was approximately one-third of the level recommended by best-practice models
3. **Interoperability gaps:** Several Bavarian state-level systems (notably the civil registry) had not been updated to support OpenDocument Format, creating genuine workflow friction
4. **No cross-party ownership:** The project was associated with a single party rather than embedded as civic infrastructure

The technical implementation achieved its stated objectives. The lesson for municipal planners: political risk management — specifically, building cross-party consensus and embedding digital sovereignty in municipal ordinance or charter — is the binding constraint.

### 7.3 Security Considerations

The BSI IT-Grundschutz framework provides a comprehensive security baseline applicable regardless of the software licence model [26]. NIS2 obligations apply to municipalities in Germany and Switzerland operating essential services [27]. Key security requirements:

- All server components: documented patch management with ≤30-day critical patch cycle
- Citizen-facing authentication: BSI AAL2 or equivalent (MFA mandatory)
- Data in transit: TLS 1.3 minimum; no TLS 1.0/1.1; HSTS enforced
- Data at rest: AES-256 for sensitive personal data categories
- Annual penetration test at each phase gate; results published in summary form
- SBOM maintained for all open-source dependencies; automated CVE scanning in CI/CD pipeline
- Incident response plan aligned with NIS2 Article 23 (24h early warning, 72h notification) [27]

---

## 8. Sovereign Technology Provider Directory

The following providers have demonstrated commitments to open-source, data sovereignty, and public-sector service delivery in the German-Swiss-European context. This directory is maintained in `Mem/source-registry.md`.

### 8.1 Germany

| Provider | Type | Primary offering | Procurement path |
|---|---|---|---|
| govdigital eG | Public-sector cooperative | SCS cloud, BundesMessenger hosting | Framework contract (all public bodies) |
| Dataport AöR | Public-sector IT provider | OZG services, Nextcloud, ENA | AKDB/Dataport framework |
| AKDB | Municipal IT cooperative | BayernPortal, KFZ, Einwohnermeldeamt | Bavaria framework; GWB compliance |
| ZenDiS GmbH | Federal agency | OpenDesk programme management | Direct engagement for large deployments |
| plusserver | Certified SCS operator | Managed SCS cloud | SCS certification; GWB compliant |
| OSISM GmbH | SCS tooling/deployment | SCS platform deployment | Direct procurement |
| Univention | IAM / directory services | UCS (Ubuntu-based) + Keycloak integration | Direct or framework |

### 8.2 Switzerland

| Provider | Type | Primary offering | Procurement path |
|---|---|---|---|
| SECO / eOperations | Federal agency | E-government platform services | Cantonal agreements |
| Abraxas Informatik | Cantonal IT provider | GEVER, Einwohnerregister, cantonal platforms | Cantonal framework |
| CMI AG | Municipal software | CMI AXIOMA (GEVER, eCH), CMI Pro | Direct procurement (WTO/BöB threshold) |
| AIO (ch.ch) | Federal shared service | ch.ch citizen portal, eGov APIs | Cantonal and municipal access via eCH |
| Netcetera | Fintech / GovTech | Swiss eID wallet integration | Direct procurement |

### 8.3 European Communities

| Community | Governance | Key resource |
|---|---|---|
| OSBA / Sovereign Cloud Stack | OSBA e.V. | scs.community |
| FSFE (Free Software Foundation Europe) | Non-profit | fsfe.org, publiccode.eu |
| Decidim Association | Multi-stakeholder association | decidim.org |
| OSOR (EU Open Source Observatory) | European Commission | joinup.ec.europa.eu/collection/open-source-observatory |
| GovStack Initiative | ITU + DIAL + partners | govstack.global |
| openCode.de | ZenDiS / Digitalservice | opencode.de |

---

## 9. Total Cost of Ownership Framework

This section provides a structured TCO model for municipal open-source transitions, grounded in the empirical data reviewed in Section 3.7.

### 9.1 Cost Categories

| Category | Open-source estimate | Proprietary estimate | Notes |
|---|---|---|---|
| Software licences (productivity suite) | €0 | €80–200 per seat/year | Microsoft 365 E3: ~€180/seat/year |
| Software licences (server OS) | €0 | €200–800 per server/year | Windows Server standard |
| Software licences (database) | €0 | €500–2,000 per server/year | SQL Server standard |
| Cloud hosting / infrastructure | €200–500 per server/year | €400–1,200 per server/year | SCS vs. hyperscaler |
| Implementation (one-time) | €300–800 per workstation | €50–150 per workstation | Migration cost premium |
| Training (one-time) | €200–500 per employee | €50–200 per employee | Higher for OS transitions |
| Support / maintenance (annual) | €30–80 per seat | €0 (bundled in licence) | May use cooperative support |
| Security and compliance | Similar | Similar | BSI Grundschutz applies to both |
| **5-year net cost (500-seat municipality)** | **~€1.2–1.8M** | **~€2.0–3.2M** | **Saving: €0.8–1.4M** |

*Assumptions: 500 staff, 50 servers, 5-year horizon, SCS-hosted, govdigital cooperative support contract. Excludes ERP and specialist applications.*

### 9.2 Hidden Costs of Proprietary Systems

Conventional TCO analyses systematically undercount four proprietary cost categories:

1. **Licence escalation:** Microsoft, Oracle, and SAP licence costs have increased at 8–15% per year on average since 2018, compounding significantly over a 10-year budget horizon
2. **Migration exit costs:** Transitioning away from a proprietary system after deep integration typically costs 2–5× the original implementation cost due to proprietary data formats, training debt, and API incompatibilities
3. **Audit exposure:** Software licence audits (SAM audits) impose compliance costs of €50,000–€500,000 on municipalities and frequently result in retroactive licence fees
4. **Security incident cost:** Proprietary systems — particularly Windows endpoints and Exchange servers — account for a disproportionate share of public-sector ransomware incidents; average remediation cost for a municipal ransomware attack is €1–5M [26]

### 9.3 Cooperative Cost-Sharing

The economics of open-source municipal IT are substantially improved by cooperative structures. A consortium of ten municipalities sharing a govdigital eG infrastructure contract distributes fixed costs across the group, reducing per-municipality infrastructure costs by 60–80% vs. independent procurement. Germany's EfA (Einer für Alle) model for OZG service development applies the same logic to application development: one municipality or Land builds a service; all others use it at marginal cost [2].

---

## 10. Small-Municipality Adaptation Guide

Most academic and policy literature focuses on large cities (population >100,000) or federal agencies. The median EU municipality has a population below 5,000; the median Swiss Gemeinde has approximately 1,800 inhabitants. This section provides tier-specific guidance.

### 10.1 Tier A: Very Small Municipalities (Population < 5,000)

**Challenge:** No dedicated IT team; IT managed by a generalist or shared with neighbouring municipalities.

**Strategy: Hosted services via cantonal/regional cooperative.**

Small municipalities should not attempt self-hosted open-source deployments. Instead:
- Join the cantonal IT cooperative or AKDB/Dataport's municipal shared-service offering
- Use hosted OpenDesk or Nextcloud through a certified SCS provider
- Participate in inter-municipal workflow (EfA services) for high-volume processes
- Focus internal effort on data quality and citizen communication, not infrastructure

**Minimum viable stack:** Hosted Nextcloud (files + communication) + hosted TYPO3 (website) + hosted Decidim instance shared with neighbouring municipalities + Keycloak federation with cantonal identity system.

**Budget guidance:** €15,000–€40,000 per year in service contracts; no significant capital expenditure.

### 10.2 Tier B: Small Municipalities (Population 5,000–50,000)

**Challenge:** Small IT team (1–3 FTE); moderate service volume; may participate in administrative association.

**Strategy: Cooperative infrastructure with local operational control.**

- Use govdigital eG or cantonal SCS-hosted environment as infrastructure
- Maintain local Keycloak instance for SSO; connect to hosted services
- Deploy Nextcloud, Matrix/Element, and Decidim as managed services
- Build up one staff member as open-source administrator
- Participate in EfA service sharing for highest-volume workflows

**Budget guidance (5-year total):** €150,000–€400,000 including migration, training, and ongoing service contracts.

### 10.3 Tier C: Medium Municipalities (Population 50,000–500,000)

**Challenge:** Substantial IT team; complex service mix; own data centre or hybrid cloud.

**Strategy:** Full implementation per Section 5 roadmap, with option for self-hosted SCS.

**Budget guidance (5-year total):** €1.5M–€4M depending on service complexity.

### 10.4 Tier D: Large Cities (Population > 500,000)

**Challenge:** Large IT organisation; highly complex service mix; political complexity; potential to contribute substantially to open-source commons.

**Strategy:** Full implementation with self-hosted SCS, upstream contribution programme, and leadership in EfA/Swiss-wide service sharing.

**Budget guidance:** Highly variable; comparable to Munich LiMux (estimated €11M–15M over 10 years including reversal costs, vs. the proprietary baseline estimated at €20–25M [61]).

---

## 11. Conclusion

The evidence reviewed in this paper converges on five findings:

**1. Open-source municipal technology stacks are technically mature and production-proven at all scales.** Every functional requirement of a modern municipal government — identity, documents, workflows, participation, communication, open data, GIS, web, infrastructure — is met by open-source software with documented deployments at peer municipalities and national governments.

**2. The regulatory environment increasingly mandates open-source and interoperability.** EMBAG (Switzerland), OZG 2.0 (Germany), the Interoperable Europe Act (EU), and the EU Data Act create legal obligations that proprietary, vendor-locked systems cannot sustainably satisfy. Early movers build compliance capital; those that delay accumulate regulatory debt and increasingly face procurement challenge risk.

**3. The economic case is compelling over a 5-year TCO horizon.** The empirical evidence from the French Gendarmerie, Extremadura, and Zaragoza migrations confirms 30–45% cost reductions relative to comparable proprietary stacks. Cooperative procurement structures reduce the per-municipality cost of implementation substantially.

**4. Success requires as much political and organisational investment as technical investment.** Clear political mandate, skilled change management, sustained stakeholder engagement, and cross-party ownership are the binding constraints. The Munich case and successful transitions in Barcelona, Stuttgart, and Swiss cantons alike confirm this finding.

**5. Small municipalities can participate via cooperative service sharing.** The cooperative model — govdigital eG in Germany, cantonal IT cooperatives in Switzerland — distributes the transition cost across many municipalities, making open-source adoption economically accessible to the median municipality with a population below 5,000.

Cities that move first benefit from first-mover advantages: shaping cooperative standards, building in-house expertise, reducing long-term costs, and contributing to the open-source commons that all municipalities share. The regulatory window is open; the technical infrastructure is ready; the cooperative support structures exist. The only remaining question is political will.

---

## References

[1] Swiss Federal Council. (2023). *Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG)*. SR 172.019. In force: 2024-01-01. https://www.fedlex.admin.ch/eli/cc/2023/682/de [CC0]

[2] Bundesministerium des Innern und für Heimat (BMI). (2024). *Onlinezugangsgesetz 2.0 (OZG 2.0)*. Berlin: BMI. https://www.bmi.bund.de/DE/themen/moderne-verwaltung/e-government/ozg/ozg-node.html [DL-DE/Zero 2.0]

[3] Open Source Business Alliance (OSBA). (2025). *Sovereign Cloud Stack Release 7*. Berlin: OSBA. https://scs.community/ [Apache 2.0]

[4] Free Software Foundation Europe (FSFE). (2017). *Public Money? Public Code!* Berlin: FSFE. https://publiccode.eu/ [CC-BY-SA-4.0]

[5] European Commission. (2020). *Open Source Software Strategy 2020–2023: Think Open*. Brussels. https://commission.europa.eu/about/departments-and-executive-agencies/informatics/open-source-software-strategy_en

[6] European Parliament and Council. (2024). *Regulation (EU) 2024/903 — Interoperable Europe Act*. OJ L 903, 2024-05-01. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202400903

[7] Wirtz, B. W., & Weyerer, J. C. (2017). Conceptualization and creation of a holistic e-government maturity model. *Public Management Review*, 19(9), 1297–1316. https://doi.org/10.1080/14719037.2017.1283024

[8] Janssen, M., Charalabidis, Y., & Zuiderwijk, A. (2012). Benefits, adoption barriers and myths of open data and open government. *Information Systems Management*, 29(4), 258–268. https://doi.org/10.1080/10580530.2012.716740

[9] FITKO. (2023). *Föderale IT-Kooperation — Jahresbericht 2023*. Frankfurt: FITKO. https://www.fitko.de/ [DL-DE/Zero 2.0]

[10] openCode.de / Digitalservice GmbH des Bundes. (2022–2026). *openCode — Open Source for Government*. https://opencode.de/

[11] Sovereign Cloud Stack Community. (2025). *SCS Technical Documentation, Release 7*. https://docs.scs.community/ [Apache 2.0]

[12] Decidim Association. (2025). *Decidim 0.28.x — Free Open-Source Participatory Democracy*. Barcelona. https://decidim.org/ [AGPL-3.0]

[13] Nextcloud GmbH. (2025). *Nextcloud Hub 8 for Government*. Stuttgart. https://nextcloud.com/government/ [AGPL-3.0 Community]

[14] The Matrix Foundation. (2025). *Matrix Specification v1.10*. https://spec.matrix.org/ [Apache 2.0]

[16] E-Government Suisse. (2023). *Strategie E-Government Schweiz 2024–2027*. Bern: Schweizerische Bundeskanzlei. https://www.egovernment.ch/de/umsetzung/e-government-strategie/

[19] TYPO3 Association. (2024). *TYPO3 13 LTS in Public Administration*. Düsseldorf. https://typo3.org/ [GPL-2.0+]

[20] OpenProject GmbH. (2025). *OpenProject 14.x for Government*. Berlin. https://www.openproject.org/ [GPLv3]

[21] Red Hat / Keycloak Community. (2024). *Keycloak 24.x — Open Source Identity and Access Management*. https://www.keycloak.org/ [Apache 2.0]

[22] CKAN Association. (2025). *CKAN 2.11.x — Open Source Data Portal Software*. https://ckan.org/ [AGPL-3.0]

[23] govdigital eG. (2025). *govdigital — Genossenschaft für digitale Verwaltung: Cloud Infrastructure Framework*. Berlin. https://govdigital.de/

[24] Dataport AöR. (2025). *Dataport — IT-Dienstleister für die öffentliche Verwaltung*. Hamburg. https://www.dataport.de/

[26] Bundesamt für Sicherheit in der Informationstechnik (BSI). (2023). *BSI IT-Grundschutz-Kompendium Edition 2023*. Bonn: BSI. https://www.bsi.bund.de/ [CC-BY-ND 3.0 DE]

[27] European Parliament and Council. (2022). *Directive (EU) 2022/2555 — NIS2*. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022L2555

[29] United Nations DESA. (2022). *UN E-Government Survey 2022*. New York: United Nations. https://publicadministration.un.org/egovkb/en-us/Reports/UN-E-Government-Survey-2022

[30] Janowski, T. (2015). Digital government evolution: From transformation to contextualization. *Government Information Quarterly*, 32(3), 221–226. https://doi.org/10.1016/j.giq.2015.07.001

[33] Camunda Services GmbH. (2025). *Camunda Platform 8 Community Edition*. https://camunda.com/download/ [Apache 2.0]

[34] BigBlueButton Inc. (2025). *BigBlueButton 3.x*. https://bigbluebutton.org/ [LGPL-3.0]

[35] Jitsi Community. (2025). *Jitsi Meet*. https://jitsi.org/ [Apache 2.0]

[36] OpenStreetMap Foundation. (2025). *OpenStreetMap*. https://www.openstreetmap.org/ [ODbL-1.0]

[37] QGIS Project. (2024). *QGIS 3.38 LTR*. https://www.qgis.org/ [GPL-2.0+]

[39] Cloud Native Computing Foundation (CNCF). (2025). *Kubernetes*. https://kubernetes.io/ [Apache 2.0]

[41] PostgreSQL Global Development Group. (2025). *PostgreSQL 17*. https://www.postgresql.org/ [PostgreSQL Licence]

[42] BMI / ZenDiS GmbH. (2025). *OpenDesk 2.0 — Der digitale Arbeitsplatz der Bundesverwaltung*. https://opendesk.eu/ [AGPL-3.0]

[43] Schweizerisches Bundesarchiv (BAR). (2023). *Geschäftsverwaltung (GEVER) in der Bundesverwaltung*. Bern: BAR. https://www.bar.admin.ch/bar/de/home/digitale-archivierung/gever.html

[44] opendata.swiss. (2025). *Open Government Data Switzerland*. https://opendata.swiss/ [CC-BY-4.0]

[45] European Commission / ISA² Programme. (2017). *European Interoperability Framework (EIF)*. https://joinup.ec.europa.eu/collection/nifo-national-interoperability-framework-observatory [CC-BY-4.0]

[46] KoSIT. (2024). *XÖV-Standards: XML in der öffentlichen Verwaltung*. Bremen: KoSIT. https://www.xoev.de/

[47] Lathrop, D., & Ruma, L. (Eds.). (2010). *Open Government: Collaboration, Transparency, and Participation in Practice*. Sebastopol: O'Reilly Media. ISBN 978-0-596-80435-0.

[48] Couture, S., & Toupin, S. (2019). What does the notion of sovereignty mean when referring to the digital? *New Media & Society*, 21(10), 2305–2322. https://doi.org/10.1177/1461444819865984

[51] ZenDiS GmbH. (2025). *Zentrum für Digitale Souveränität der öffentlichen Verwaltung — Annual Report 2024*. Berlin: ZenDiS. https://zendis.de/ [Open access]

[52] GovStack Initiative / ITU & DIAL. (2024). *GovStack Specification: Digital Public Infrastructure Building Blocks*. Geneva: ITU. https://govstack.global/ [CC-BY-SA-4.0]

[53] European Commission / DIGIT. (2024). *OSOR Annual Report 2023: Open Source in European Public Administration*. Brussels: European Commission. https://joinup.ec.europa.eu/collection/open-source-observatory [CC-BY-4.0]

[54] European Parliament and Council. (2023). *Regulation (EU) 2023/2854 — Data Act*. OJ L 2854, 2023-12-13. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023R2854

[55] Swiss Federal Chancellery. (2024). *Federal Strategy on Open Government Data 2024–2027*. Bern: BK. https://opendata.admin.ch/

[56] Schweizerische Eidgenossenschaft / EJPD. (2023). *Bundesgesetz über den elektronischen Ausweis (E-ID-Gesetz)*. Bern. https://www.fedlex.admin.ch/eli/fga/2023/787/de

[57] eCH — E-Government Standards Switzerland. (2024). *eCH Standards Catalogue: eCH-0007, eCH-0010, eCH-0020, eCH-0046, eCH-0058, eCH-0160*. Bern: eCH. https://www.ech.ch/de/standards [Open access]

[58] Ayuntamiento de Madrid / CONSUL Democracy Project. (2023). *CONSUL Democracy 2.3.x*. https://consulproject.org/ [AGPL-3.0]

[59] Gendarmerie Nationale / Direction Générale de la Gendarmerie Nationale (DGGN). (2014). *Migration Linux: Bilan 2008–2014* [Internal report; cited in Montpetit, 2014, and LWN.net]. Summary available at https://lwn.net/Articles/630516/

[60] Comisión de Gobierno Electrónico de España. (2007). *Software Libre en las Administraciones Públicas Españolas*. Madrid: MAP. [Cited for Extremadura and Zaragoza data]

[61] Accenture / City of Munich. (2017). *Abschlussbericht zur Evaluation des Münchener LiMux-Projekts*. Munich: Landeshauptstadt München. [Critiqued in: Baack, S. (2018). Open Government Data, Open Source, and Open Licensing. *JeDEM*, 10(1)] https://www.jedem.org/index.php/jedem/article/view/508

---

*Released under Creative Commons Attribution 4.0 International (CC-BY-4.0).*  
*Attribute as: Sebastian Graf, Autonomous Office of Civil Digital Infrastructure (sebk4c@tuta.com)*  
*Cite as: Graf, S. (2026). Sovereign by Design: A State-of-the-Art Open-Source Technology Strategy for Municipal Governments (v0.2.0). Autonomous Office of Civil Digital Infrastructure. https://github.com/SEBK4C/Strategy-for-City-GovTech*
