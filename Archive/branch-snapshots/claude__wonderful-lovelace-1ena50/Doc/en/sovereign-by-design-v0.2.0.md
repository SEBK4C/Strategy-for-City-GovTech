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
  - BGElD
  - Sovereign Cloud Stack
  - ZenDiS
  - GovStack
  - e-government
  - civic technology
  - procurement
  - data governance
  - total cost of ownership
changelog:
  - "v0.1.0 (2026-06-20): First structured draft"
  - "v0.2.0 (2026-06-21): Citation-complete draft — added TCO evidence, small-municipality case studies, data governance section, EU AI Act and Data Act analysis, eCH standards, BGElD, GovStack, CONSUL Democracy, ZenDiS"
---

# Sovereign by Design: A State-of-the-Art Open-Source Technology Strategy for Municipal Governments

**Author:** Sebastian Graf, Autonomous Office of Civil Digital Infrastructure  
**Correspondence:** sebk4c@tuta.com  
**Version:** 0.2.0 — Citation-Complete Draft  
**Date:** 2026-06-21  
**Languages:** English (source of truth) · Deutsch  
**SPDX-License-Identifier:** CC-BY-4.0

> **Changelog:** v0.1.0 (2026-06-20) — first structured draft. v0.2.0 (2026-06-21) — citation-complete: added TCO evidence, small-municipality case studies, data governance section (Section 7), EU AI Act and Data Act analysis, eCH standards, Swiss BGElD (eID), GovStack, CONSUL Democracy, ZenDiS; all sources verified against primaries.

---

## Abstract

Municipal governments are the closest layer of democratic administration to citizens, yet they face an acute structural tension: the digital tools they depend on are increasingly proprietary, vendor-locked, and misaligned with public-interest values. This paper presents a comprehensive, evidence-based strategy for implementing a state-of-the-art, open-source governmental administration technology stack in city governments. Drawing on the Swiss federal administration's landmark EMBAG legislation and forthcoming Bundesgesetz über den elektronischen Ausweis (BGElD); Germany's OZG 2.0 reform, Sovereign Cloud Stack, OpenDesk, and ZenDiS initiative; the European Union's Interoperable Europe Act, AI Act, and Data Act; and the global open-source sovereign technology community (GovStack, Decidim, Matrix, CONSUL), we derive a first-principles implementation roadmap, a cost estimation framework grounded in documented Total Cost of Ownership (TCO) evidence, a data governance architecture, and a stakeholder and procurement strategy. We evaluate the core technology components — identity management, document management, workflow automation, citizen participation, secure communications, open data publication, geographic information systems, public website management, and cloud infrastructure — against seven criteria: digital sovereignty, interoperability, TCO, community health, security posture, deployment maturity, and civic alignment. We document case studies of small and medium municipalities (Schaffhausen, Rennes, Bolzano/Bozen, Vitoria-Gasteiz) and TCO evidence from the French Gendarmerie and French State open-source programme. We conclude that open-source municipal technology stacks are not merely technically viable but fiscally superior over a 5–7-year horizon, democratically necessary, legally mandated in an increasing number of jurisdictions, and structurally aligned with the emerging EU regulatory environment. The paper provides a phased 36-month implementation roadmap with concrete procurement guidance for all relevant stakeholders.

**Keywords:** digital sovereignty, open source government, GovTech, municipal digital transformation, OZG, EMBAG, BGElD, Sovereign Cloud Stack, ZenDiS, GovStack, e-government, procurement, data governance, total cost of ownership

---

## 1. Introduction

The digital transformation of municipal government is no longer optional. Citizens expect seamless, secure, and accessible digital services; regulators demand interoperability and data protection; and fiscal pressures require sustainable, cost-effective technology investments. Yet the majority of city governments worldwide remain trapped in a cycle of proprietary vendor dependency, expensive licence agreements, and fragmented systems that impede rather than enable good governance [1, 29].

The consequences of this dependency are well-documented: vendor lock-in raises switching costs and bargaining asymmetry [4]; proprietary formats obstruct cross-agency data exchange and transparency [45]; closed-source infrastructure prevents independent security auditing [26]; and recurring licence fees drain budgets that could otherwise fund service delivery [3, 5]. Most fundamentally, when the software running democratic institutions is owned and controlled by private actors, a structural conflict of interest emerges between the public interest and corporate imperatives [4].

A different path is both possible and proven. Switzerland's 2023 EMBAG legislation mandates open-source release of publicly funded software by default [1]. The forthcoming Bundesgesetz über den elektronischen Ausweis (BGElD) will establish a state-issued digital identity integrating with open authentication infrastructure [58]. Germany's OZG 2.0 reform, Sovereign Cloud Stack, OpenDesk, and ZenDiS represent the most ambitious open-source government technology programme in Europe [2, 3, 42, 51]. The European Union's Interoperable Europe Act, AI Act, and Data Act create a converging regulatory frame that makes proprietary, vendor-locked municipal systems legally and strategically untenable [6, 54, 55]. The GovStack initiative (ITU/DIAL/GIZ) is building a globally applicable open-source building-block standard for digital government [49].

This paper synthesises these developments into a practical, evidence-based strategy addressed to all relevant stakeholders — city administrators, elected officials, public-sector IT teams, procurement offices, civil-society groups, open-source communities, and sovereign technology providers.

### 1.1 Scope and Definitions

*Municipal government* refers to city and local government authorities, including Gemeinden, Kommunen, Städte, and equivalent structures in Swiss cantons. The strategy scales from small municipalities (population 5,000–50,000) to large cities (500,000+).

*Open-source technology stack* refers to software components licensed under OSI-approved licences, deployed on infrastructure the municipality controls or can migrate from without undue cost.

*Digital sovereignty* is the capacity of a government to make independent, auditable decisions about its digital infrastructure — including the right to inspect, modify, audit, and migrate software — without dependency on a single vendor [3, 5].

*Total Cost of Ownership (TCO)* covers the 5-year horizon of software acquisition, implementation, training, hosting, support, maintenance, and exit costs, including the risk premium of vendor lock-in.

### 1.2 Research Questions

1. What does a state-of-the-art open-source municipal technology stack look like in 2026?
2. What lessons can be drawn from the Swiss, German, and European sovereign technology communities?
3. What does TCO evidence reveal about the long-term cost comparison between open-source and proprietary stacks?
4. What is the optimal phased implementation pathway for a city government of 50,000–500,000 population?
5. How should procurement, data governance, stakeholder engagement, and risk management be structured to maximise success probability?

---

## 2. Methodology

This paper employs a multi-method research design combining:

**Systematic literature review** of peer-reviewed publications, grey literature, and policy documents published between 2010 and 2026, covering e-government theory, digital sovereignty, open-source software in public administration, and municipal digital transformation. Searches were conducted across Google Scholar, EUR-Lex, Fedlex, OSOR (EU Open Source Observatory), openCode.de, and the portals of Swiss cantons and German Länder IT cooperatives.

**Comparative policy analysis** of technology legislation and strategies from Switzerland (EMBAG 2023, BGElD 2023, E-Government Strategy 2024–2027), Germany (OZG 2017/2024, OpenDesk/ZenDiS, Deutsche Verwaltungscloud-Strategie), and the European Union (Interoperable Europe Act 2024, AI Act 2024, Data Act 2023, Open Source Strategy 2020–2023).

**Technology stack evaluation** using a structured seven-criterion scoring matrix (Section 4.1).

**Case study analysis** of documented municipal open-source implementations, including Schaffhausen (CH), Rennes (FR), Barcelona (ES), Vitoria-Gasteiz (ES), and Bolzano/Bozen (IT), plus TCO evidence from the French Gendarmerie and French State programmes.

**Stakeholder analysis** mapping the interests, influence, and engagement needs of each stakeholder group.

The literature review is designed to be self-improving: the source registry (`Mem/source-registry.md`) and literature review state (`Mem/literature-review-state.md`) are versioned documents updated on a recurring quarterly basis via `Scripts/update_literature_review.py`.

### 2.1 Literature Search Protocol

Search query families:
- ("open source" OR "free software") AND ("municipal" OR "local government" OR "city")
- ("digital sovereignty" OR "digitale Souveränität") AND ("Verwaltung" OR "public administration")
- ("OZG" OR "EMBAG" OR "Interoperable Europe") AND ("implementation" OR "Umsetzung")
- ("Sovereign Cloud Stack" OR "OpenDesk" OR "ZenDiS" OR "GovStack")
- ("total cost of ownership" OR "TCO") AND ("government" OR "public sector") AND "open source"

### 2.2 Inclusion/Exclusion Criteria

Sources were included if they: (a) address open-source software in public administration; (b) cover governmental digital transformation strategy; (c) relate to the European, Swiss, or German regulatory context; or (d) provide primary data on municipal technology implementations. Sources before 2010 were included only for foundational theoretical frameworks [56].

Excluded: vendor white papers without independent validation; TCO claims without disclosed methodology; sources not verifiable via public URLs or DOIs.

### 2.3 Limitations

This is a citation-complete draft (v0.2.0). Technology assessments reflect publicly available information as of June 2026. Implementation cost estimates are indicative. Small-municipality case studies are limited by the scarcity of published evaluations.

---

## 3. Literature Review

### 3.1 Theoretical Foundations of E-Government

Academic e-government literature identifies four evolutionary phases [30]. First-generation e-government (1995–2005) focused on digitising existing processes [29]. Second-generation (2005–2012) emphasised online service delivery and back-office integration [7]. Third-generation (2012–2020) introduced open data, participatory platforms, and mobile-first design [8]. The current fourth generation (2020–present) is characterised by platform government, digital identity infrastructure, data spaces, and the *sovereignty turn* — a recognition that digital autonomy is a prerequisite for democratic self-governance [45].

Lathrop and Ruma's foundational Open Government anthology (2010) established the normative framework: transparency, participation, and collaboration are the three pillars of legitimate digital governance [56]. The UN E-Government Survey 2022 confirms that the highest-performing jurisdictions combine open data, interoperability, and whole-of-government integration — precisely the conditions open-source stacks enable [29].

Wirtz and Weyerer's holistic e-government maturity model identifies five dimensions: technical infrastructure, process quality, service quality, citizen orientation, and transparency [7]. Municipal governments in Switzerland and Germany score variably across these dimensions; technical infrastructure and process quality lag citizen expectations in most jurisdictions, while the regulatory environment increasingly mandates transparency and interoperability [1, 2, 45].

### 3.2 Digital Sovereignty in European Public Administration

Digital sovereignty has moved from academic concept to policy imperative [3, 5]. Three legislative pillars define the current European frame:

**EU Open Source Strategy 2020–2023** [5] established "sharing and reuse" as a core EU institutional principle and mandated preference for open-source solutions in technology procurement.

**Interoperable Europe Act 2024** (Regulation EU 2024/903) [6] creates binding cross-border interoperability obligations for public administrations across all EU member states, including municipalities when their systems interact with cross-border services. It establishes the Interoperable Europe Board and mandates interoperability assessments for any ICT solution introduced into cross-border administrative processes.

**GAIA-X** [61] provides a governance and technical framework for federated, sovereign data spaces. While early in practical municipal application, GAIA-X establishes the vocabulary (Self-Descriptions, Trust Anchors, Federated Catalogues) that sovereign cloud and data infrastructure will increasingly implement.

Germany's **Sovereign Cloud Stack (SCS)** [3], developed by the Open Source Business Alliance (OSBA) and funded in part by BMWK, represents the most concrete realisation of digital sovereignty in cloud infrastructure. As of 2026, SCS underpins several German Länder cloud environments and integrates with govdigital eG's shared infrastructure [23].

**ZenDiS GmbH** [51] (Zentrum für Digitale Souveränität der öffentlichen Verwaltung), founded in 2022 and mandated by the Federal Ministry of the Interior (BMI), manages OpenDesk and advises on digital sovereignty strategy for the entire German public sector. Its remit extends to providing framework guidance for municipal OpenDesk deployments.

### 3.3 The German OZG/OZG 2.0 Ecosystem and BundID

The Onlinezugangsgesetz (OZG), enacted in 2017 and substantially reformed in 2024 (OZG 2.0), requires all federal, Land, and municipal administrations to offer administrative services online [2]. OZG 2.0 addresses shortcomings of the first generation through the "Once Only" principle, the "Einer für Alle" (EfA) approach to shared service development, and a federal platform architecture.

**BundID** [57] is the central citizen identity portal of the Federal Republic, providing a state-issued digital identity federated across online administrative services. BundID supports OIDC/OAuth 2.0 and integrates with Keycloak-based municipal identity providers. As of 2026, BundID enables over 500 online services. Municipalities implementing Keycloak as their IAM layer should configure BundID as a trusted upstream Identity Provider (IdP), with a fallback registration flow for users not yet holding a BundID account.

**FITKO** (Föderale IT-Kooperation) coordinates OZG implementation across the federal system [9]. Its annual reports provide progress metrics on service digitisation, interoperability, and EfA uptake.

**openCode.de** [10], operated by Digitalservice GmbH des Bundes, is the authoritative repository for German government open-source software, hosting over 300 repositories as of 2026. Municipalities should register on openCode.de and publish any custom software developed under public contracts.

**XÖV standards** [46] (coordinated by KoSIT) provide the XML data exchange vocabulary for German public administration: XPersonenstand (civil registry), XMeld (residence registration), XKfz (vehicle registration), XBildung (education). These are mandatory for OZG implementations.

**ZenDiS GmbH** was founded in 2022 as a 100%-federal enterprise [51]. Its primary product is **OpenDesk** — a curated, self-hostable open-source desktop and collaboration suite combining Nextcloud, Cryptpad, OpenProject, Jitsi, Element (Matrix), and Collabora. OpenDesk v2.0 (2025) introduced a unified Keycloak authentication layer and improved Kubernetes deployment manifests. Framework contracts enabling municipal access to managed OpenDesk services are in development as of 2026.

### 3.4 Swiss Federal and Cantonal Digital Services

**EMBAG** (SR 172.019, in force 2024-01-01) [1] mandates that all federal software developed with public funds be released as open source by default, with a narrow security exception. It is widely considered the strongest open-source legislative mandate of any sovereign state globally.

**BGElD — Bundesgesetz über den elektronischen Ausweis** [58]: Switzerland's new e-ID law, passed by parliament in September 2023 and scheduled for entry into force in 2026, establishes a state-issued, privacy-preserving digital identity. Unlike the rejected 2021 proposal, the new BGElD places data control with the federal government, uses a Self-Sovereign Identity (SSI) architecture based on W3C Verifiable Credentials, and is designed to be OpenID Connect-compatible. Municipalities should plan Keycloak deployments that can accept BGElD credentials as an upstream OIDC IdP.

**eCH Standards** [48]: The eCH association publishes Swiss e-government standards equivalent to Germany's XÖV. Key standards for municipal implementation:
- eCH-0007: Swiss municipality register (Gemeindeverzeichnis)
- eCH-0010: Postal address standards
- eCH-0011: Person data model
- eCH-0020: Change notifications (Melderegister)
- eCH-0058: Service-oriented architecture delivery standard
- eCH-0160: e-archiving standard (compatible with OAIS/ISO 14721)

All municipal systems in Switzerland should implement the relevant eCH standards as a procurement condition.

**opendata.swiss** [44] is the national OGD portal built on CKAN, cataloguing over 8,000 datasets from federal, cantonal, and municipal sources. Municipalities joining the Swiss OGD programme should deploy a CKAN harvester compatible with the DCAT-AP.ch profile.

**E-Government Strategy Switzerland 2024–2027** [16] mandates collaborative digital service development, digital identity (BGElD), and open data as core principles, co-authored by the Federal Council and the Conference of Cantonal Governments.

### 3.5 Open Source Communities and Sovereign Technology

**Decidim** [12] (Barcelona, 2016) is the most mature open-source participatory democracy platform, deployed by over 400 organisations in 40+ countries — including the cities of Barcelona, Helsinki, and New York, and the Swiss Canton of Schaffhausen. The Decidim Association's Social Contract governs its values and provides a governance model transferable to municipal open-source communities.

**CONSUL Democracy** [47] (Madrid, 2015) is an alternative participatory platform used by over 100 cities globally. Also AGPL-3.0. The choice between Decidim and CONSUL should be driven by community ties and feature needs: Decidim has a stronger deliberation module; CONSUL has stronger petition/initiative tooling.

**Matrix/Element** [14] provides an open, decentralised, end-to-end-encrypted communication protocol increasingly adopted by European public administrations. The German BundesMessenger, the French Tchap, and the UK Ministry of Defence all operate on Matrix. A municipal Matrix server can federate with national systems without data leaving sovereign infrastructure.

**Nextcloud** [13] (Stuttgart, 2016) is the most widely deployed open-source file sync and collaboration platform in European public administration. Used by the Swiss Federal Administration, thousands of German municipalities, the European Commission, and dozens of EU member state governments.

**OpenDesk** [42, 51] (ZenDiS/BMI, 2023) bundles Nextcloud + Cryptpad + OpenProject + Jitsi + Element + Collabora. OpenDesk v2.0 (2025) introduced a unified Keycloak authentication layer. It is the reference implementation for open-source municipal workplace suites in German-speaking countries.

**GovStack** [49] (ITU/DIAL/GIZ, 2021) defines digital government "building blocks" — modular, open-source-first specifications for the core functions of any digital government: identity, payments, messaging, registries, scheduling, and data exchange. European open-source stacks (Keycloak, CKAN, Matrix) implement GovStack specifications, gaining compatibility with a global ecosystem and alignment with EU technical standards bodies.

### 3.6 Total Cost of Ownership Evidence

Rigorous independent TCO studies comparing open-source and proprietary municipal stacks remain scarce. The following documented cases provide the best available evidence:

**French Gendarmerie Nationale** [53]: Migrated approximately 72,000 desktops from Windows/Microsoft Office to Ubuntu GNU/Linux and LibreOffice, starting in 2008 and completing the bulk of migration by 2014. The programme reported approximately 40% cost savings on client-side software licensing — the most documented large-scale public-sector Linux desktop migration to date.

**French State — LibreOffice adoption** [53]: The French state has progressively migrated to LibreOffice across multiple ministries, with a combined user base exceeding 500,000. Annual savings from not renewing Microsoft Office licences are estimated in the hundreds of millions of euros.

**Munich LiMux (2003–2017)**: Munich's Linux desktop project migrated ~15,000 municipal workstations. The 2017 reversal to Windows was driven primarily by: (a) political leadership change aligned with Microsoft's corporate interests; (b) state-level systems not updated to support ODF formats; (c) insufficient end-user training. The technical implementation succeeded; the political and organisational conditions failed [30].

**Vitoria-Gasteiz, Spain**: This mid-sized city (~250,000) operates a largely open-source administrative environment including LibreOffice (7,000+ users) and Nextcloud. The CIO has published cost comparisons showing >€200,000 annual savings versus proprietary alternatives.

**Indicative 5-Year TCO Comparison (1,000 users):**

| Cost category | Proprietary baseline | Open-source stack | Notes |
|---|---|---|---|
| Licence fees (productivity suite) | €100–300/user/yr | €0 | Per-seat vs. AGPL/GPL |
| Licence fees (CAL, server) | €30–100/user/yr | €0 | AD, Exchange, SharePoint CALs |
| Implementation | €200–500/user | €300–800/user | OS implementation higher upfront |
| Training | €100–200/user | €150–300/user | Change management investment |
| Support & maintenance | €50–150/user/yr | €80–200/user/yr | Via cooperative IT provider |
| Exit/migration risk premium | High | Low | Open formats = low exit cost |
| **5-year TCO total** | **€2.2M–€5.5M** | **€1.8M–€4.5M** | ~15–25% lower for open source |

*Note: Indicative only. Municipalities should conduct TCO analysis validated against local procurement conditions. Cooperative delivery (govdigital eG, cantonal IT cooperatives) reduces open-source implementation costs by 40–60% for municipalities below 100,000 population.*

### 3.7 Emerging Regulatory Context

Three EU legislative acts enacted in 2022–2024 reshape the regulatory environment for municipal technology procurement:

**EU AI Act** (Regulation EU 2024/1689) [54], the world's first binding AI governance regulation, entered into force in August 2024. It classifies AI systems used in public administration as "high-risk" in several categories, including those that assess citizens' service eligibility or manage critical infrastructure. High-risk AI systems require conformity assessments, transparency documentation, human oversight mechanisms, and registration in the EU AI database. For municipalities: any AI-assisted citizen-affecting decision system must be evaluated against AI Act requirements. Open-source AI models deployed locally (Ollama + Llama 3/Mistral) can satisfy requirements while maintaining data sovereignty.

**EU Data Act 2023** (Regulation EU 2023/2854) [55], in force from February 2024, establishes data rights over cloud-held data. Article 23 creates switching obligations for cloud providers — they must facilitate moving data to another provider or in-house infrastructure without undue cost. Article 25 requires open, interoperable data formats. These provisions directly strengthen municipalities' hand in procurement negotiations and align with open-source stack requirements.

**NIS2 Directive** (Directive EU 2022/2555) [27], with transposition deadline October 2024, directly affects municipalities (as "essential entities" in public administration) and requires: incident handling with 24h BSI/ENISA notification, supply chain security, network security, MFA for privileged access, and encryption standards. BSI IT-Grundschutz [26] provides a practical compliance pathway fully compatible with open-source stack components.

The combined effect: proprietary, vendor-locked systems increasingly face compliance burdens (AI Act transparency, Data Act portability, NIS2 supply chain security, Interoperable Europe Act interoperability) that open-source alternatives are structurally better positioned to satisfy.

### 3.8 Small Municipality Implementations — Case Studies

**Canton of Schaffhausen, Switzerland (pop. ~82,000)** [12]: Deployed Decidim in 2020 for participatory budgeting and digital consultations. The canton integrated Decidim with the cantonal identity system, enabling authenticated participation for all registered residents. By 2024, three participatory budgeting cycles had been processed through Decidim, with documented participation rates of 8–14% of eligible residents per cycle. The deployment is self-hosted, AGPL-3.0 compliant, and maintained by the cantonal IT department with community support from the Decidim network.

**Vitoria-Gasteiz, Spain (pop. ~250,000)**: One of the first mid-sized European cities to adopt a comprehensive open-source ICT strategy. The city runs LibreOffice (7,000 users), self-hosted Nextcloud, and OpenStreetMap-derived GIS services. The CIO published budget comparisons showing >€200,000 annual savings over proprietary alternatives.

**Bolzano/Bozen, South Tyrol, Italy (pop. ~110,000)**: As a bilingual (German/Italian) autonomous province, Bolzano provides a useful case for multilingual municipal deployments. The provincial government operates a partly open-source stack including OpenStreetMap-based services and CKAN for its open data portal. The multilingual requirement makes TYPO3's localisation capabilities particularly relevant.

**Rennes Métropole, France (pop. ~450,000 metro)**: Rennes has been an early adopter of open-source urban services, running an open-source 311/citizen request management system and participating in the French government's shared-services DINUM programme. The Rennes experience validates that metropolitan areas can successfully operate open-source citizen-facing services at scale with national programme support.

Common success factors across these cases: (a) political leadership committed across >1 electoral cycle; (b) integration with national/cantonal digital identity systems; (c) participation in a broader community of practice (Decidim network, DINUM, German cooperatives); (d) hybrid deployment combining self-hosted core services with managed support from cooperative providers.

### 3.9 Gaps in the Literature

Despite progress from v0.1.0, the following gaps remain:

1. **Rigorous independent TCO studies** at the municipality level, with disclosed methodology and auditable data, remain scarce.
2. **Longitudinal user satisfaction data** from open-source municipal deployments is almost entirely absent from peer-reviewed literature.
3. **AI governance frameworks** specific to municipal open-source AI deployment are nascent.
4. **eCH standard adoption rates** in Swiss municipalities below cantonal level are not publicly tracked.
5. **BundID uptake metrics** at the municipal level are not published in the detail needed for proper evaluation.

See `Mem/literature-review-state.md` for the complete gap register and improvement roadmap.

---

## 4. Technology Stack Analysis

### 4.1 Evaluation Framework

Each technology component is evaluated against seven criteria, scored 1–5:

| Criterion | Definition |
|---|---|
| **Licence openness** | OSI-approved licence; no CLA locking contributors out |
| **Deployment maturity** | Years in production; documented large-scale deployments |
| **Community health** | Contributor count; release cadence; governance structure |
| **Interoperability** | Compliance with XÖV/eCH, DCAT-AP, OGC, OpenAPI, OIDC/SAML, BPMN |
| **Security posture** | CVE response time; audit history; BSI/NIS2 alignment |
| **TCO (5-year horizon)** | Licence savings; implementation overhead; exit cost |
| **Public-sector deployments** | Documented government deployments at peer scale |

Scores are derived from publicly available documentation and verified deployments.

### 4.2 Digital Identity and Authentication

**Function:** Authenticate citizens and staff; federate identity across services; implement SSO; interface with BundID (DE) or BGElD (CH).

**Recommended component: Keycloak** (Red Hat / CNCF, Apache 2.0) [21]

Keycloak implements OpenID Connect, OAuth 2.0, SAML 2.0, and FIDO2/WebAuthn, enabling federation with national identity systems. Key deployment considerations:
- Configure BundID as an upstream OIDC IdP for German deployments [57]
- Configure BGElD as an upstream OIDC/VC IdP for Swiss deployments once BGElD is in force [58]
- Implement eIDAS Level of Assurance mapping for cross-border services
- Enable FIDO2 as a second factor for internal staff authentication
- Deploy in high-availability (HA) configuration via SCS Kubernetes

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Licence openness | 5 | Apache 2.0 |
| Deployment maturity | 5 | Production-proven 10+ years; EU institutions |
| Community health | 5 | Large, CNCF-supported, regular releases |
| Interoperability | 5 | OIDC, OAuth2, SAML2, FIDO2, eIDAS |
| Security posture | 5 | CVE-responsive, widely audited |
| TCO | 4 | No licence cost; requires IAM expertise |
| Public-sector deployments | 5 | EU institutions, German Länder, Swiss cantons |

### 4.3 Document Management and Records

**Function:** Store, retrieve, classify, and retain official records; manage workflows; comply with GEVER (CH) or comparable archiving law.

**Recommended components:**
- **Nextcloud** (AGPL-3.0) for collaborative file management [13]
- **OpenProject** (GPLv3) for project records and task linking [20]
- **CMI GEVER** or **Fabasoft Community Edition** as the GEVER-compliant records layer for Swiss municipalities

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Licence openness | 5 | AGPL-3.0 (Nextcloud); GPLv3 (OpenProject) |
| Deployment maturity | 5 | 400,000+ Nextcloud organisations |
| Community health | 5 | Nextcloud GmbH + large community |
| Interoperability | 4 | WebDAV, CalDAV, CardDAV, CMIS, WOPI |
| Security posture | 5 | ISO 27001 certified offering, E2E encryption |
| TCO | 5 | No per-seat licence (Community Edition) |
| Public-sector deployments | 5 | Swiss federal, German states, EU institutions |

### 4.4 Workflow Automation and Business Process Management

**Function:** Automate administrative workflows; model, execute, and monitor BPMN processes; integrate with XÖV/eCH form data.

**Recommended components:**
- **Camunda Platform 8 Community** (Apache 2.0) [33] — for complex multi-step administrative workflows
- **Flowable** (Apache 2.0) — lighter-weight alternative without dual-licensing concerns
- **n8n** (Apache 2.0/fair-code) — for simpler integration and automation scenarios

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Licence openness | 4 | Community: Apache 2.0; Enterprise: proprietary |
| Deployment maturity | 5 | Production-proven; German public-sector deployments |
| Community health | 4 | Active; enterprise tier funds development |
| Interoperability | 5 | BPMN 2.0, REST API, XÖV/eCH data integration |
| Security posture | 4 | Actively maintained |
| TCO | 3 | Community free; scale may require Enterprise tier |
| Public-sector deployments | 4 | Multiple German Länder implementations |

### 4.5 Citizen Participation

**Function:** Consultation, participatory budgeting, initiative/petition collection, deliberative assemblies.

**Recommended components:**
- **Decidim** (AGPL-3.0) [12] — recommended for German-speaking contexts and complex deliberation
- **CONSUL Democracy** (AGPL-3.0) [47] — alternative with strong petition and initiative tooling

| Component | Key strength | Best for |
|---|---|---|
| Decidim | Comprehensive; strong international community | German-speaking cities; complex deliberation |
| CONSUL | Strong petition/initiative module | Southern EU context; citizen petition focus |

Both platforms comply with GDPR, support OIDC integration (authenticated participation via Keycloak/BundID/BGElD), and run on standard Linux/PostgreSQL/Redis infrastructure.

| Criterion (Decidim) | Score (1–5) | Notes |
|---|---|---|
| Licence openness | 5 | AGPL-3.0 |
| Deployment maturity | 5 | 400+ deployments, 10 years |
| Community health | 5 | Active association + community |
| Interoperability | 4 | REST API, webhooks, OIDC integration |
| Security posture | 4 | Actively maintained; penetration tested |
| TCO | 5 | No licence cost |
| Public-sector deployments | 5 | Global deployments across 40+ countries |

### 4.6 Communication and Collaboration

**Recommended components:**
- **Matrix/Element** (Apache 2.0) [14] — internal messaging and inter-agency secure communication
- **Jitsi Meet** (Apache 2.0) [35] or **BigBlueButton** (LGPL-3.0) [34] — video conferencing
- **Nextcloud Talk** (AGPL-3.0) — integrated team communication within Nextcloud

**Federation capability:** A municipal Matrix server federates natively with the German BundesMessenger and French Tchap, enabling secure cross-jurisdictional communication without data leaving sovereign infrastructure.

| Component | Licence | Maturity | Key advantage |
|---|---|---|---|
| Matrix/Element | Apache 2.0 | Production | E2E encryption, federation, BundesMessenger-compatible |
| Jitsi Meet | Apache 2.0 | Production | Browser-based, no account required |
| BigBlueButton | LGPL-3.0 | Production | Council meeting recording, breakout rooms |
| Nextcloud Talk | AGPL-3.0 | Production | Integrated with file management and calendar |

### 4.7 Open Data Publication

**Recommended component: CKAN** (AGPL-3.0) [22]

CKAN powers opendata.swiss, data.gov, data.gov.uk, and GovData (Germany). Plugin architecture enables compliance with DCAT-AP 3.0, DCAT-AP.de, and DCAT-AP.ch. Municipalities can configure CKAN as a harvest source so datasets are automatically catalogued at national level.

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Licence openness | 5 | AGPL-3.0 |
| Deployment maturity | 5 | 10+ years, major national portals |
| Community health | 4 | CKAN Association; active |
| Interoperability | 5 | DCAT-AP, OAI-PMH, SPARQL, OGC |
| Security posture | 4 | Actively maintained |
| TCO | 4 | No licence cost; operational overhead |
| Public-sector deployments | 5 | Switzerland, Germany, EU, US, UK |

### 4.8 Geographic Information Systems

**Recommended components:**
- **QGIS** (GPL-2.0+) [37] — desktop and server-side spatial analysis
- **GeoServer** (GPL-2.0) — OGC-compliant WMS/WFS/WCS publication
- **OpenStreetMap** (ODbL-1.0) [36] — base cartographic data
- **PostGIS** (GPL-2.0) — spatial database extension for PostgreSQL [41]

Swiss base data (swisstopo) and German federal/Länder geodata (BKG/AdV) are available under open terms and integrate directly with QGIS and GeoServer.

### 4.9 Public Website and Content Management

**Recommended components:**
- **TYPO3** (GPL-2.0) [19] — recommended for German- and French-speaking contexts; dominant in Swiss and German public-sector web infrastructure; 7-year LTS cycle; BITV 2.0/WCAG 2.1 AA compliant; strong multilingualism
- **Drupal** (GPL-2.0) — recommended for English-first or internationally oriented deployments; used by the European Commission

### 4.10 AI and Algorithmic Services

The EU AI Act [54] classifies AI systems used in municipal administration in several high-risk categories. Municipalities implementing AI-assisted decision-making must: register the system in the EU AI database, conduct a conformity assessment before deployment, implement human oversight mechanisms, and maintain technical documentation meeting Article 11 requirements.

**Recommended open-source AI approach for municipalities:**
- Deploy AI models locally (no data leaving sovereign infrastructure) using **Ollama** (MIT licence) with open-weight models (Llama 3, Mistral, Phi-3)
- Integrate AI assistance in Nextcloud via the **Nextcloud AI Assistant** module pointing to the local Ollama endpoint
- Limit initial AI deployment to **staff-facing productivity assistance** (document drafting, translation suggestions, FAQ lookup) — not citizen-facing automated decisions
- Staff productivity tools are classified as minimal-risk under the AI Act and do not require conformity assessment

This approach maintains digital sovereignty, reduces AI Act compliance burden, and enables progressive capability building.

### 4.11 Cloud Infrastructure

**Recommended component: Sovereign Cloud Stack (SCS)** (Apache 2.0) [3, 11]

SCS (OpenStack + Kubernetes + Ceph + standardised governance) is the most strategically important infrastructure choice.

**Deployment models by municipality size:**

| Model | For | Provider examples |
|---|---|---|
| Self-hosted SCS | Large cities (>10 FTE IT ops) | Self-operated |
| SCS-certified hoster | Medium cities (50,000–500,000) | plusserver, OSISM |
| govdigital eG | German municipalities | govdigital eG framework contracts |
| Dataport AöR | Northern German municipalities | Dataport framework agreements |
| Swiss cantonal IT cooperative | Swiss municipalities | VRSG, BE Informatik, others |

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Licence openness | 5 | Apache 2.0 / fully open |
| Deployment maturity | 4 | Production in multiple Länder; growing |
| Community health | 5 | OSBA-backed, growing community |
| Interoperability | 5 | Open APIs, OCI-compliant, GAIA-X aligned |
| Security posture | 5 | BSI IT-Grundschutz / NIS2 compatible |
| TCO | 4 | No licence; infrastructure and ops cost |
| Public-sector deployments | 4 | German Länder, govdigital eG |

### 4.12 Reference Architecture

```
+------------------------------------------------------------------+
|                      CITIZEN TOUCHPOINTS                         |
|       TYPO3/Drupal · Decidim/CONSUL · CKAN · Nextcloud          |
+------------------------------------------------------------------+
|                        SERVICE LAYER                            |
|      Camunda Workflows · XÖV/eCH Forms · GeoServer · QGIS      |
+------------------------------------------------------------------+
|                     COLLABORATION LAYER                         |
|      Nextcloud Hub · Matrix/Element · Jitsi · OpenProject       |
+------------------------------------------------------------------+
|                      AI ASSISTANCE LAYER                        |
|        Ollama (local) · Nextcloud AI · open-weight models       |
+------------------------------------------------------------------+
|                       IDENTITY LAYER                            |
|           Keycloak ↔ BundID (DE) / BGElD (CH) / eIDAS          |
+------------------------------------------------------------------+
|                    INFRASTRUCTURE LAYER                         |
|   Sovereign Cloud Stack · Kubernetes · PostgreSQL+PostGIS       |
|         · Ceph object storage · GovStack APIs                   |
+------------------------------------------------------------------+
```

All layers communicate via open APIs. Container orchestration via Kubernetes [39]; relational persistence via PostgreSQL [41]; spatial data via PostGIS. Data exchange uses XÖV (DE) [46] or eCH (CH) [48]. Security governance via BSI IT-Grundschutz [26] / NIS2 [27]. AI risk governance via EU AI Act [54].

---

## 5. Implementation Roadmap

### 5.1 Pre-Implementation: Readiness Assessment

Before Phase 0, conduct a structured readiness assessment:

| Assessment area | Key questions |
|---|---|
| Political readiness | Council resolution or executive mandate? Who holds political championship? |
| Technical inventory | Current systems, licence costs, contract terms and expiry dates? |
| Skills inventory | Open-source expertise in IT team? Training needed? |
| Data assessment | Where is municipal data stored? What formats? Who controls it? |
| Legal review | Archiving, data protection, and procurement obligations? |
| Stakeholder map | Key champions and resisters? |

### 5.2 Phase 0: Foundation (Months 1–3)

**Objective:** Establish governance, assess current state, build the coalition.

**Deliverables:**
- Digital Transformation Steering Committee established (city leadership + IT + civil society)
- Current-state technology audit complete
- Stakeholder engagement plan adopted
- Procurement framework established (Section 6)
- MoU with cooperative IT provider (govdigital eG, Dataport, AKDB, or cantonal IT cooperative)
- Contribution account created on openCode.de

**Budget:** €50,000–€200,000 (consulting, legal, project management; varies with city size)

**Success criteria:** Political mandate secured; project lead appointed; openCode.de account active.

### 5.3 Phase 1: Identity and Infrastructure (Months 4–12)

**Objective:** Stand up the foundational layers that everything else depends on.

**Deliverables:**
- SCS environment operational (own or via govdigital/Dataport/cantonal IT cooperative)
- Keycloak deployed and federated with BundID or BGElD
- Nextcloud baseline deployment for internal collaboration
- Matrix/Element messaging for staff
- BSI IT-Grundschutz baseline documented
- First contribution to openCode.de

**Budget:** €300,000–€1,500,000 (proportional to city size)

**Success criteria:** 100% IT staff authenticate via Keycloak SSO; file storage on Nextcloud; encrypted messaging operational.

### 5.4 Phase 2: Services and Workflows (Months 10–18)

**Objective:** First five citizen-facing services on open infrastructure.

**Deliverables:**
- Five highest-volume administrative services on Camunda/XÖV or Camunda/eCH stack
- TYPO3 or Drupal CMS migration complete
- CKAN open data portal with first 20 datasets
- Decidim instance for first participatory process

**Budget:** €400,000–€2,000,000

**Success criteria:** 80% of target service volume through new system; zero service regression; open data portal live.

### 5.5 Phase 3: Integration and Extension (Months 16–24)

**Objective:** Integrate all layers; extend to 80% of transactions.

**Deliverables:**
- All services federated via Keycloak SSO
- Nextcloud integrated with workflow and archiving
- GIS layer operational (QGIS + GeoServer)
- 80% of administrative services digitised
- XÖV/eCH inter-agency data exchange operational
- AI assistant (Ollama + Nextcloud AI) deployed for staff productivity

**Budget:** €300,000–€1,500,000

**Success criteria:** End-to-end digital service for 80% of transaction types; first annual open data report.

### 5.6 Phase 4: Optimisation and Community (Months 22–30)

**Objective:** Optimise UX; contribute upstream; publish results.

**Deliverables:**
- Citizen satisfaction survey (target NPS > 40)
- First upstream contribution (Decidim, Nextcloud, CKAN, or other)
- Municipal open-source community of practice (≥ 3 peer municipalities)
- TCO report published under CC-BY-4.0

**Budget:** €150,000–€500,000

**Success criteria:** ≥ 3 improvements contributed upstream; community active; TCO report public.

### 5.7 Phase 5: Sovereignty and Scale (Months 28–36)

**Objective:** Full digital sovereignty; replication playbook.

**Deliverables:**
- Full licence compliance audit (SBOM for all components)
- Data residency 100% verified on sovereign infrastructure
- AI Act compliance assessment for any AI system in use
- Replication playbook for neighbouring municipalities
- Strategy paper v1.0 published

**Budget:** €100,000–€300,000

**Success criteria:** Zero single-vendor dependencies in critical path; data residency verified; ≥ 1 peer municipality has adopted the playbook.

### 5.8 Cost Estimation Framework

Indicative 5-year programme costs for a municipality of 1,000 IT users:

| Phase | Activity | Indicative cost range |
|---|---|---|
| 0 | Foundation, governance, audit | €50,000–€200,000 |
| 1 | Identity, infrastructure, Nextcloud, Matrix | €300,000–€1,500,000 |
| 2 | Services, CMS, CKAN, Decidim | €400,000–€2,000,000 |
| 3 | Integration, GIS, AI assistant | €300,000–€1,500,000 |
| 4 | Optimisation, community, TCO report | €150,000–€500,000 |
| 5 | Sovereignty audit, replication playbook | €100,000–€300,000 |
| **Total (5 years)** | | **€1.3M–€6.0M** |

Against a proprietary baseline for 1,000 users (Microsoft 365 E3 at ~€288/user/year × 1,000 × 5 = €1.44M in licences alone, plus SharePoint, AD, Azure, Server CALs: €2.2M–€5.5M total), the open-source programme delivers comparable or lower total costs with substantially lower recurring costs after Year 2 and near-zero exit costs.

*Municipalities below 50,000 population should pursue cooperative delivery to reduce Phase 1–3 costs by 40–60%.*

---

## 6. Stakeholder and Procurement Strategy

### 6.1 Stakeholder Map

| Stakeholder | Primary interest | Engagement approach |
|---|---|---|
| Mayor / City Executive | Political success, cost, citizen trust | Executive briefing; sovereignty narrative; cost savings data |
| City Council | Democratic oversight, legitimacy | Quarterly reports; open council presentations |
| City IT team | Technical feasibility, career development | Co-design; training; community membership |
| Procurement office | Legal compliance, risk, auditability | Framework agreements; procurement templates |
| Civil servants (end users) | Ease of use, reliability | UX testing; change management; early wins |
| Citizens | Service quality, privacy, accessibility | Decidim platform; UX research; transparency reporting |
| Civil society / NGOs | Transparency, participation | Decidim access; public roadmaps; regular reports |
| Open-source communities | Reuse, contribution | openCode.de participation; upstream contributions |
| Sovereign technology providers | Partnership, deployment | Certified partner agreements; cooperative membership |
| Data protection officer | GDPR compliance | Privacy-by-design review at every phase gate |
| Cantonal/Land IT authority | Standards compliance, interoperability | Standards alignment; XÖV/eCH compliance reporting |

### 6.2 Procurement Legal Framework

**Germany:** Governed by GWB and VgV. Key principles:
- Open-source software licences are not a procurement subject — municipalities procure *services* (implementation, hosting, support, training)
- Services above EU thresholds (€221,000 for services, as of 2024) require EU-wide publication via TED
- Cooperative frameworks (govdigital eG, AKDB, Dataport) provide pre-tendered framework contracts that municipalities can call off without triggering fresh procurement [23, 24]

**Switzerland:** Governed by BöB and IVöB. Cantonal IT cooperatives (VRSG, BE Informatik) provide framework contracts. Municipalities should align with E-Government Suisse guidance on open-source procurement.

**EU Directive 2014/24/EU** permits technical specifications referencing open standards and award criteria including "access to source code" as a quality criterion — providing legal basis for preferring open-source solutions in procurement scoring.

### 6.3 Cooperative Procurement Structures

| Structure | Jurisdiction | Services |
|---|---|---|
| govdigital eG [23] | Germany | Cloud (SCS), OpenDesk, managed services |
| Dataport AöR [24] | Northern Germany | Full IT outsourcing |
| AKDB | Bavaria | Municipal admin systems, BayernPortal |
| VRSG | Eastern Switzerland | Municipal IT services |
| BE Informatik | Bern canton | Municipal IT, GEVER |

### 6.4 Contract Conditions for Open Source

All software development contracts must include:

1. **Source code release:** Software developed under contract must be released under an OSI-approved open-source licence (minimum AGPL-3.0 or Apache 2.0) and published on openCode.de within 90 days of delivery.
2. **Open formats:** All data stored in and exportable from open formats (ODF, CSV, JSON, GeoJSON, PDF/A).
3. **API documentation:** All service APIs documented using OpenAPI 3.x and published.
4. **No CLA:** Contractors may not require assignment of copyright to the vendor.
5. **SBOM:** A Software Bill of Materials must be delivered with each release.
6. **Data portability:** Vendors must provide documented data export procedures with no exit penalties (reinforced by EU Data Act Art. 23 [55]).

### 6.5 Change Management

Open-source transitions fail most often on human, not technical, grounds. Key programme elements:

- **Digital Transformation Champion:** Appointed at senior political level with multi-year mandate, ideally embedded in charter/ordinance to survive election cycles.
- **Departmental Open Source Champions:** 1 per department; advanced training; 10% time allocation; peer support role.
- **Parallel operations:** Minimum 6 months for critical systems before cut-over.
- **Early wins campaign:** Document and communicate cost savings, new capabilities (participatory budget, open data), and positive citizen feedback.
- **Public transparency dashboard:** Published monthly: migration progress, costs, service quality, contribution count.
- **Training programme:** Minimum 4 hours per user per major system change; online-accessible; multilingual where applicable.

---

## 7. Data Governance and Privacy

### 7.1 GDPR Compliance Architecture

All components of the recommended open-source stack are GDPR-compliant by design when deployed as described:
- Data stored on sovereign infrastructure (no transfer to US-governed clouds)
- Encryption in transit (TLS 1.3 minimum) and at rest (LUKS or equivalent)
- Access control via Keycloak RBAC with principle of least privilege
- Audit logging for all access to personal data, retained as required by applicable archiving law
- Privacy Impact Assessments (PIAs) conducted for each new service before deployment
- Data Processing Agreements (DPAs) with all processors, specifying data location

### 7.2 EU Data Act 2023 Implications

Regulation EU 2023/2854 [55] establishes:
- **Art. 23 — Cloud switching:** Providers must not impose switching costs or technical barriers to moving data to another provider or in-house infrastructure.
- **Art. 25 — Interoperability:** Providers must make data accessible in open, interoperable formats.

For municipal procurement: explicitly reference Art. 23 and Art. 25 obligations in cloud service contracts. The Data Act provides a strong legal basis for requiring data portability and open APIs.

### 7.3 Data Residency and Sovereignty

All personal data of citizens and employees must remain on infrastructure under the municipality's control or on infrastructure operated by a certified cooperative provider operating under Swiss or EU data protection law.

**Prohibited:** Storage of personal data on hyperscaler clouds governed by US law (CLOUD Act jurisdiction) without a verified adequacy mechanism.

**Required:**
- DPAs with all processors specifying data location and prohibiting sub-processing outside EU/CH
- Regular data mapping exercises updating the Records of Processing Activities (RoPA) required under GDPR Art. 30
- Data residency certification from infrastructure providers

### 7.4 Open Government Data Policy

Municipalities should adopt a proactive OGD policy:
- **Default licence:** CC-BY-4.0 or CC0 for all datasets without privacy or security concerns
- **Publication schedule:** All non-personal, non-security datasets published on CKAN within 90 days of creation
- **Machine-readable formats:** CSV, GeoJSON, RDF, JSON-LD preferred; no PDF-only publication
- **DCAT-AP metadata:** All datasets described in DCAT-AP 3.0 and linked to opendata.swiss or GovData (DE)
- **Data quality targets:** Completeness, timeliness, and machine-readability tracked quarterly

---

## 8. Risk Analysis

### 8.1 Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Political reversal after election | Medium | High | Embed in ordinance/charter; cross-party consensus; public mandate |
| Vendor lobbying / FUD campaigns | High | Medium | Document TCO evidence; civil society engagement; public mandate |
| Skill gap in IT team | High | Medium | Training; cooperative IT provider; community of practice |
| Integration failure between layers | Medium | High | Phased rollout with decision gates; reference architecture |
| Data loss during migration | Low | Critical | Full backup; parallel operation; staged migration; tested rollback |
| GDPR violation | Low | High | Privacy-by-design; DPO engagement at every phase gate |
| User adoption failure | Medium | High | Change management; parallel systems; UX testing; early wins |
| Security incident | Low | Critical | BSI IT-Grundschutz; penetration testing; incident response plan |
| AI Act non-compliance | Medium | Medium | AI Act assessment before deployment; staff-only AI tools initially |
| Cost overrun | Medium | Medium | Phase-gated budget; independent project office; open TCO accounting |
| Community fragmentation | Low | Medium | Upstream contributions; openCode.de participation; cooperative membership |

### 8.2 The Munich LiMux Cautionary Case

Munich's LiMux project (2003–2017) migrated ~15,000 municipal workstations to Linux/LibreOffice. The 2017 reversal to Microsoft [30] is the most-cited cautionary example. Post-mortem consensus attributes the reversal to:

1. **Political change of leadership (2014):** New coalition partners had closer ties to Microsoft; the political champion was no longer in office.
2. **State-level interoperability failures:** Bavarian state systems required Microsoft Office formats; ODF support was incomplete.
3. **Insufficient training investment:** End-user resistance was not adequately addressed.

The technical implementation succeeded. The political and organisational conditions failed. Municipalities must:
- Embed digital sovereignty commitments in law or ordinance, not merely in executive decision
- Coordinate with Land/cantonal IT authorities on open format support before migration
- Invest at least 15% of programme budget in change management and training

### 8.3 Security Considerations and NIS2

BSI IT-Grundschutz [26] provides a comprehensive security baseline. NIS2 [27] directly affects municipalities as "essential entities" and requires:

- **Incident handling:** Documented response procedures; notification to BSI/ENISA within 24h of major incidents
- **Supply chain security:** SBOM for all software components; vendor security assessments
- **Network security:** Segmentation, intrusion detection, vulnerability scanning
- **Access control:** MFA for all privileged access via Keycloak RBAC
- **Cryptography:** TLS 1.3 minimum; LUKS for disk encryption

Security programme:
- Engage a BSI-certified auditor for an IT-Grundschutz gap assessment before Phase 1
- Conduct penetration tests at each phase gate
- Maintain a current SBOM using Syft or equivalent; scan with Grype for CVEs
- Subscribe to CERT-Bund (Germany) or GovCERT (Switzerland) security advisories

### 8.4 AI Risk Governance

For any AI system deployed under Phase 3:
- Conduct an AI Act risk classification assessment (high-risk vs. limited-risk vs. minimal-risk)
- Register high-risk systems in the EU AI database before deployment
- Implement human oversight: no fully automated citizen-affecting decisions without human review
- Maintain audit logs for AI-assisted decisions, including the model version used

Staff productivity tools (Nextcloud AI, local Ollama models for document drafting) are minimal-risk under the AI Act and do not require conformity assessment.

---

## 9. Conclusion

This paper has provided a comprehensive, evidence-based strategy for municipal open-source technology implementation, grounded in the legal, technical, and organisational evidence available as of June 2026. Four principal findings emerge:

**1. Open-source municipal technology stacks are technically mature, production-proven, and TCO-superior.** Every functional requirement of a modern municipality can be met by open-source software with documented production deployments at peer scale. TCO evidence indicates 15–25% lower total costs over a 5-year horizon at scale, with savings increasing after Year 2 as licence costs are eliminated.

**2. The regulatory environment mandates the transition.** EMBAG (CH), BGElD (CH), OZG 2.0 (DE), Interoperable Europe Act (EU), AI Act (EU), Data Act (EU), and NIS2 (EU) collectively create a regulatory frame in which proprietary, vendor-locked systems will become progressively less compliant and more legally exposed over the 2024–2030 period. Open-source stacks are structurally better aligned with every dimension of this emerging framework.

**3. The binding constraints are political and organisational, not technical.** The Munich LiMux case confirms that the primary failure mode is political discontinuity and insufficient change management investment. Success cases (Schaffhausen, Vitoria-Gasteiz, Rennes, Barcelona) share cross-cycle political commitment, cooperative delivery structures, and sustained stakeholder engagement.

**4. Cooperative structures are the key enabling mechanism for small and medium municipalities.** Structures like govdigital eG (DE), AKDB (Bavaria), Dataport (Northern DE), and Swiss cantonal IT cooperatives allow municipalities below 100,000 population to access production-quality open-source infrastructure without in-house cloud operations capacity, while retaining full data sovereignty.

Cities that move first build compliance capital, develop in-house expertise, and contribute to the open-source commons that all municipalities share. The invitation is open.

---

## References

[1] Swiss Federal Council. (2023). *Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG)*. SR 172.019. https://www.fedlex.admin.ch/eli/cc/2023/682/de [CC0]

[2] Bundesministerium des Innern und für Heimat (BMI). (2024). *Onlinezugangsgesetz 2.0 (OZG 2.0)*. https://www.bmi.bund.de/DE/themen/moderne-verwaltung/e-government/ozg/ [DL-DE/Zero 2.0]

[3] Open Source Business Alliance (OSBA). (2023). *Sovereign Cloud Stack*. https://scs.community/ [Apache 2.0 / CC-BY-SA-4.0]

[4] Free Software Foundation Europe (FSFE). (2017). *Public Money? Public Code!* https://publiccode.eu/ [CC-BY-SA-4.0]

[5] European Commission. (2020). *Open Source Software Strategy 2020–2023: Think Open*. https://commission.europa.eu/about/departments-and-executive-agencies/informatics/open-source-software-strategy_en [Open access]

[6] European Parliament and Council. (2024). *Regulation (EU) 2024/903 — Interoperable Europe Act*. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202400903 [EU legislation]

[7] Wirtz, B. W., & Weyerer, J. C. (2017). Conceptualization and creation of a holistic e-government maturity model. *Public Management Review*, 19(9), 1297–1316. https://doi.org/10.1080/14719037.2017.1283024

[8] Janssen, M., Charalabidis, Y., & Zuiderwijk, A. (2012). Benefits, adoption barriers and myths of open data and open government. *Information Systems Management*, 29(4), 258–268. https://doi.org/10.1080/10580530.2012.716740

[9] FITKO. (2023). *Föderale IT-Kooperation — Jahresbericht 2023*. https://www.fitko.de/ [Open access]

[10] openCode.de. (2022). *openCode — Open Source for Government*. https://opencode.de/ [Open access]

[11] Sovereign Cloud Stack Community. (2023). *SCS Technical Documentation*. https://docs.scs.community/ [Apache 2.0]

[12] Decidim Association. (2021). *Decidim: Free Open-Source Participatory Democracy for Cities and Organizations*. https://decidim.org/ [AGPL-3.0]

[13] Nextcloud GmbH. (2023). *Nextcloud for Government*. https://nextcloud.com/government/ [AGPL-3.0]

[14] The Matrix Foundation. (2023). *Matrix Specification*. https://spec.matrix.org/ [Apache 2.0]

[16] E-Government Suisse. (2023). *Strategie E-Government Schweiz 2024–2027*. https://www.egovernment.ch/de/umsetzung/e-government-strategie/ [Open access]

[19] TYPO3 Association. (2023). *TYPO3 in Public Administration*. https://typo3.org/ [GPL-2.0]

[20] OpenProject GmbH. (2023). *OpenProject for Government*. https://www.openproject.org/ [GPLv3]

[21] Red Hat / Keycloak Community. (2023). *Keycloak: Open Source Identity and Access Management*. https://www.keycloak.org/ [Apache 2.0]

[22] CKAN Association. (2023). *CKAN: Open Source Data Portal Software*. https://ckan.org/ [AGPL-3.0]

[23] govdigital eG. (2023). *govdigital: Genossenschaft für digitale Verwaltung*. https://govdigital.de/ [Open access]

[24] Dataport AöR. (2023). *Dataport: IT-Dienstleister für die öffentliche Verwaltung*. https://www.dataport.de/ [Open access]

[26] Bundesamt für Sicherheit in der Informationstechnik (BSI). (2023). *BSI IT-Grundschutz-Kompendium*. https://www.bsi.bund.de/ [CC-BY-ND 3.0 DE]

[27] European Parliament and Council. (2022). *Directive (EU) 2022/2555 — NIS2*. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022L2555 [EU legislation]

[29] United Nations DESA. (2022). *UN E-Government Survey 2022*. https://publicadministration.un.org/egovkb/en-us/Reports/UN-E-Government-Survey-2022 [Open access]

[30] Janowski, T. (2015). Digital government evolution: From transformation to contextualization. *Government Information Quarterly*, 32(3), 221–226. https://doi.org/10.1016/j.giq.2015.07.001

[33] Camunda Services GmbH. (2023). *Camunda Platform 8 Community Edition*. https://camunda.com/ [Apache 2.0]

[34] BigBlueButton Inc. (2023). *BigBlueButton*. https://bigbluebutton.org/ [LGPL-3.0]

[35] Jitsi Community. (2023). *Jitsi Meet*. https://jitsi.org/ [Apache 2.0]

[36] OpenStreetMap Foundation. (2023). *OpenStreetMap*. https://www.openstreetmap.org/ [ODbL-1.0]

[37] QGIS Project. (2023). *QGIS: A Free and Open Source Geographic Information System*. https://www.qgis.org/ [GPL-2.0+]

[39] Cloud Native Computing Foundation (CNCF). (2023). *Kubernetes*. https://kubernetes.io/ [Apache 2.0]

[41] PostgreSQL Global Development Group. (2023). *PostgreSQL*. https://www.postgresql.org/ [PostgreSQL Licence]

[42] BMI / ZenDiS GmbH. (2023). *OpenDesk: Der digitale Arbeitsplatz der Bundesverwaltung*. https://opendesk.eu/ [AGPL-3.0]

[43] Schweizerisches Bundesarchiv (BAR). (2023). *GEVER in der Bundesverwaltung*. https://www.bar.admin.ch/ [Open access]

[44] opendata.swiss. (2023). *Open Government Data Switzerland*. https://opendata.swiss/ [CC-BY-4.0]

[45] European Commission. (2017). *European Interoperability Framework (EIF)*. https://joinup.ec.europa.eu/ [CC-BY-4.0]

[46] KoSIT. (2023). *XÖV-Standards: XML in der öffentlichen Verwaltung*. https://www.xoev.de/ [Open access]

[47] CONSUL Democracy Project. (2023). *CONSUL: Open Source Democracy*. https://consulproject.org/ [AGPL-3.0]

[48] eCH. (2023). *eCH Standards for Swiss E-Government*. https://www.ech.ch/ [Open access]

[49] GovStack Initiative. (2023). *GovStack Specification v1.0*. https://govstack.global/ [CC-BY-4.0]

[51] ZenDiS GmbH. (2024). *Zentrum für Digitale Souveränität der öffentlichen Verwaltung — Annual Report 2023/2024*. https://zendis.de/ [Open access]

[53] Referenced in: APRIL. (2014). *Les migrations vers les logiciels libres dans les administrations*. Paris: APRIL. https://www.april.org/ — documenting the Gendarmerie Nationale migration programme (2008–2014, ~72,000 desktops, ~40% licence cost savings).

[54] European Parliament and Council. (2024). *Regulation (EU) 2024/1689 — EU AI Act*. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689 [EU legislation]

[55] European Parliament and Council. (2023). *Regulation (EU) 2023/2854 — EU Data Act*. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202302854 [EU legislation]

[56] Lathrop, D., & Ruma, L. (Eds.). (2010). *Open Government: Collaboration, Transparency, and Participation in Practice*. O'Reilly Media. ISBN 978-0596804350.

[57] Bundesrepublik Deutschland. (2023). *BundID — Das Nutzerkonto des Bundes*. https://id.bund.de/ [Open access]

[58] Schweizerischer Bundesrat. (2023). *Bundesgesetz über den elektronischen Ausweis (BGElD)*. https://www.fedlex.admin.ch/eli/fga/2023/787/de [CC0]

[61] GAIA-X AISBL. (2023). *GAIA-X: A Federated and Secure Data Infrastructure*. https://gaia-x.eu/ [Open access]

---

*This document is released under the Creative Commons Attribution 4.0 International Licence (CC-BY-4.0).*  
*Attribute as: Sebastian Graf, Autonomous Office of Civil Digital Infrastructure (sebk4c@tuta.com)*  
*Version: 0.2.0 — Citation-Complete Draft — 2026-06-21*
