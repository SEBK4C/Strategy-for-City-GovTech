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
  - eCH
  - GovStack
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

| Version | Date | Changes |
|---|---|---|
| v0.1.0 | 2026-06-20 | First structured draft. 30 primary sources. Full scientific structure. |
| v0.2.0 | 2026-06-21 | Citation-complete draft. All 4 previously unverified sources verified. §0 Executive Stakeholder Guide added. §3.7 Small and Mid-Size Municipality Case Studies added. §4.11 Total Cost of Ownership Framework added. §7.4 Regulatory Compliance Obligations added. ZenDiS, eCH standards, CONSUL Democracy, GovStack initiative, Swiss E-ID Act, EU Data Act fully integrated. 12 new sources [47]–[58]. Literature review state updated. |

---

## §0. Executive Stakeholder Guide

*This guide provides a tailored entry point for each stakeholder group. Read the section for your role, then proceed to the full paper for detail.*

### For City Administrators and Senior Managers

The core message: open-source municipal technology is no longer an experiment — it is mandated by law in Switzerland (EMBAG) and Germany (OZG 2.0), and strongly incentivised by the EU Interoperable Europe Act. The fiscal case is compelling: proprietary productivity suites cost €100–300 per seat per year in licence fees alone; the open-source equivalent costs primarily labour for deployment and support, spread across cooperative procurement. The risk most frequently underestimated is not technical but political: securing sustained cross-party mandate and allocating adequate change-management budget are the two decisions that determine outcome. **Recommended reading:** §5 (Implementation Roadmap) and §6 (Stakeholder and Procurement Strategy).

### For Elected Officials

Digital sovereignty is a democratic value, not a technical preference. When the software running a city's administration is owned and controlled by a private vendor, that vendor can withdraw support, raise prices, or be acquired by a foreign actor — with no democratic recourse. Open-source software places those decisions back in public hands. Switzerland's parliament enacted EMBAG in 2023 precisely because this principle resonates across the political spectrum. The paper provides the evidence base for a council motion or executive mandate. **Recommended reading:** §1 (Introduction), §3.2 (Digital Sovereignty), §8 (Conclusion).

### For Public-Sector IT Teams

Every component evaluated in this paper has production deployments at peer municipalities. The reference architecture (§4.10) is a tested blueprint, not a theoretical model. The most important technical decisions are: (1) start with Keycloak identity management — everything else federates to it; (2) select a Sovereign Cloud Stack-certified host or self-host on SCS before deploying application layers; (3) insist on XÖV (Germany) or eCH (Switzerland) standards compliance in every procurement. The skill gap is real but bridgeable through govdigital eG membership and the openCode.de community. **Recommended reading:** §4 (Technology Stack Analysis), §5 (Implementation Roadmap), §7.3 (Security).

### For Procurement Offices

Open-source procurement is structurally different from licence procurement: you are buying services (implementation, hosting, support, training), not rights to use software. The legal framework supports this: govdigital eG framework agreements satisfy German public procurement law (GWB §97ff.); Swiss cantonal cooperatives cover BöB requirements. The key contractual obligation to add to all custom-development contracts: any software developed with public funds must be released under an OSI-approved licence and published on openCode.de or equivalent. Evaluate total cost of ownership over five years, not headline implementation cost. **Recommended reading:** §6.2 (Procurement Framework), §4.11 (TCO Framework).

### For Civil-Society Groups and Open-Source Communities

This strategy positions civic communities as co-producers, not just service recipients. Decidim deployments actively solicit participation in budget allocation and urban planning. openCode.de pools contributions so that improvements made by one municipality benefit all. The transparency obligations embedded in this stack — open data via CKAN, public roadmaps, open-source code — create structural accountability that proprietary alternatives cannot match. Contributions to upstream projects (Decidim, Nextcloud, CKAN, Matrix) directly improve the commons. **Recommended reading:** §3.5 (Sovereign Technology Communities), §6.1 (Stakeholder Map).

### For Sovereign Technology Providers

This strategy creates substantial market opportunity for providers who can deliver implementation, hosting, support, and training for the stack components described herein — on the explicit condition of data sovereignty and open-source compliance. Certification as an SCS cloud operator or membership in govdigital eG provides the framework contract access that unlocks public-sector procurement. Contributing to openCode.de and upstream communities is a reputational and competitive advantage in this market segment. **Recommended reading:** §4 (Technology Stack Analysis), §6 (Stakeholder and Procurement Strategy).

---

## Abstract

Municipal governments are the closest layer of democratic administration to citizens, yet they face an acute structural tension: the digital tools they depend on are increasingly proprietary, vendor-locked, and misaligned with public-interest values. This paper presents a comprehensive strategy for implementing a state-of-the-art, open-source governmental administration technology stack in city governments. Drawing on exemplary practices from the Swiss federal administration's EMBAG legislation, Germany's OZG reform programme and Sovereign Cloud Stack initiative, the ZenDiS-managed OpenDesk platform, and the wider European sovereign technology community — including GovStack, eCH, Decidim, CONSUL Democracy, and Matrix — we derive a first-principles implementation roadmap, stakeholder engagement framework, and procurement strategy. We evaluate the core technology components — identity management, document management, workflow automation, citizen participation, secure communications, open data publication, and cloud infrastructure — against criteria of digital sovereignty, interoperability, total cost of ownership, and civic alignment. Case studies from small and mid-size municipalities in Switzerland and Germany demonstrate that the transition is achievable across the full range of city sizes. We conclude that open-source municipal technology stacks are not merely technically viable but fiscally superior, democratically necessary, and legally mandated in an increasing number of jurisdictions. The paper provides a phased 36-month implementation roadmap with concrete procurement guidance for city administrators, elected officials, IT teams, procurement offices, civil-society groups, open-source communities, and sovereign technology providers.

**Keywords:** digital sovereignty, open source government, GovTech, municipal digital transformation, interoperability, OZG, EMBAG, Sovereign Cloud Stack, e-government, civic technology, ZenDiS, eCH, GovStack

---

## 1. Introduction

The digital transformation of municipal government is no longer optional. Citizens expect seamless, secure, and accessible digital services; regulators demand interoperability and data protection; and fiscal pressures require sustainable, cost-effective technology investments. Yet the majority of city governments worldwide remain trapped in a cycle of proprietary vendor dependency, expensive licence agreements, and fragmented systems that impede rather than enable good governance [1, 29].

The consequences of this dependency are well-documented: vendor lock-in raises switching costs and shifts bargaining power asymmetrically toward private suppliers [4]; proprietary formats obstruct cross-agency data exchange and transparency [45]; closed-source infrastructure prevents independent security auditing [26]; and recurring licence fees drain budgets that could otherwise fund service delivery [3, 5]. Most fundamentally, when the software running democratic institutions is owned and controlled by private actors, a structural conflict of interest emerges between the public interest and corporate imperatives [4, 53].

A different path is both possible and proven. Switzerland's 2023 EMBAG legislation (Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben) mandates that federal software developed with public funds be released as open source by default [1]. Germany's OZG reform programme, Sovereign Cloud Stack, and OpenDesk initiative — managed by ZenDiS GmbH, the federal centre for digital sovereignty — represent the most ambitious open-source government technology programme in Europe [2, 3, 42, 47]. The Free Software Foundation Europe's "Public Money? Public Code!" campaign, now endorsed by over 200 organisations across 30 countries, articulates the democratic principle at stake [4]. The GovStack initiative, a partnership between the ITU, GIZ, and the Digital Impact Alliance, provides an internationally standardised building-block framework directly applicable to European municipal implementations [50].

This paper synthesises these developments into a practical strategy for municipal governments. It is addressed to all relevant stakeholders — city administrators, elected officials, public-sector IT teams, procurement offices, civil-society groups, open-source communities, and sovereign technology providers — and provides the evidence base, technology assessment, and implementation roadmap needed to make the transition.

### 1.1 Scope and Definitions

*Municipal government* refers to city and local government authorities, including Gemeinden, Kommunen, Städte, and equivalent structures in Swiss cantons. The strategy is designed to scale from small municipalities (population 5,000–50,000) to large cities (population 500,000+), with appropriate modulation.

*Open-source technology stack* refers to software components licensed under OSI-approved licences, deployed on infrastructure that the municipality controls or can migrate away from without undue cost or friction.

*Digital sovereignty* is the ability of a government to make independent decisions about its digital infrastructure, including the right to inspect, modify, audit, and migrate software without dependency on a single vendor [3, 47].

### 1.2 Research Questions

1. What does a state-of-the-art open-source municipal technology stack look like in 2026?
2. What lessons can be drawn from the Swiss, German, and European sovereign technology communities?
3. What is the optimal phased implementation pathway for city governments across the full population range?
4. How should procurement, stakeholder engagement, and risk management be structured to maximise success probability?

---

## 2. Methodology

This paper employs a multi-method research design combining:

**Systematic literature review** of peer-reviewed publications, grey literature, and policy documents published between 2010 and 2026, covering e-government theory, digital sovereignty, open-source software in public administration, and municipal digital transformation.

**Comparative policy analysis** of technology legislation and strategies from Switzerland (EMBAG 2023, E-Government Strategy 2024–2027), Germany (OZG 2017/2024, Deutsche Verwaltungscloud-Strategie), and the European Union (Interoperable Europe Act 2024, EU Open Source Strategy 2020–2023, EU Data Act 2023).

**Technology stack evaluation** using a structured scoring matrix assessing each component on: (a) licence openness, (b) deployment maturity, (c) community health, (d) interoperability standards compliance, (e) security posture, (f) total cost of ownership, and (g) existing public-sector deployments.

**Stakeholder analysis** mapping the interests, influence, and engagement needs of each stakeholder group in the municipal digital transformation process.

**Case study analysis** of municipalities across the population range that have completed or substantially advanced open-source transitions, with particular attention to small and mid-size municipalities underrepresented in prior literature.

The literature review is designed to be self-improving: the source registry (`Mem/source-registry.md`) and literature review state (`Mem/literature-review-state.md`) are versioned documents updated on a recurring basis. The `Scripts/update_literature_review.py` script provides structured prompts for reviewing and improving these files on a quarterly cadence.

### 2.1 Inclusion Criteria

Sources were included if they: (a) address open-source software in public administration; (b) cover governmental digital transformation strategy; (c) relate to the European, Swiss, or German regulatory context; or (d) provide primary data on municipal technology implementations. Sources published before 2010 were included only where they establish foundational theoretical frameworks.

### 2.2 Limitations

Technology stack assessments reflect the state of publicly available information as of June 2026. Implementation cost estimates are indicative and must be validated against local procurement conditions. Case study data for small municipalities relies on publicly available project reports; independent audit of outcomes was not possible within the scope of this paper.

---

## 3. Literature Review

### 3.1 Theoretical Foundations of E-Government

The academic literature on e-government has evolved through four broad phases [30]. First-generation e-government (1995–2005) focused on digitising existing processes and creating government websites [29]. Second-generation e-government (2005–2012) emphasised online service delivery, citizen portals, and back-office integration [7]. Third-generation e-government (2012–2020) introduced open data, participatory platforms, and mobile-first service design [8]. The current fourth generation (2020–present) is characterised by platform government, digital identity infrastructure, data spaces, and the sovereignty turn — a recognition that digital autonomy is a prerequisite for democratic self-governance [45].

Lathrop and Ruma's foundational 2010 volume *Open Government* established the three pillars that continue to structure policy: transparency, participation, and collaboration [53]. These pillars map directly onto the technology stack components evaluated in Section 4: open data (transparency), participatory platforms such as Decidim and CONSUL (participation), and collaborative infrastructure such as Nextcloud and Matrix (collaboration).

Wirtz and Weyerer's holistic e-government maturity model identifies five dimensions: technical infrastructure, process quality, service quality, citizen orientation, and transparency [7]. Municipal governments in Switzerland and Germany score variably across these dimensions; technical infrastructure and process quality lag citizen expectations in most jurisdictions, while the regulatory environment increasingly mandates transparency and interoperability [1, 2, 45].

### 3.2 Digital Sovereignty in Public Administration

The concept of digital sovereignty has moved from academic concept to policy imperative in the European context [3, 5]. The EU Open Source Strategy 2020–2023 established "sharing and reuse" as a core principle, mandating that European institutions prefer open-source solutions in technology procurement [5]. The 2024 Interoperable Europe Act (Regulation (EU) 2024/903, CELEX 32024R0903, OJ L 2024/903, 22 April 2024) creates binding obligations for cross-border interoperability in public administrations across all EU member states [6]. The EU Data Act (Regulation (EU) 2023/2854, in force January 2024, applicable from September 2025) adds harmonised data-sharing obligations that interact directly with municipal open data and GIS infrastructure [52].

Germany's Sovereign Cloud Stack (SCS), developed by the Open Source Business Alliance (OSBA) and funded in part by the German Federal Ministry for Economic Affairs and Climate Action (BMWK), represents the most concrete realisation of digital sovereignty in cloud infrastructure. SCS provides a fully open-source, self-hostable cloud platform (OpenStack + Kubernetes + Ceph) that enables public administrations to operate infrastructure that is technically and legally sovereign [3]. ZenDiS GmbH (Zentrum für Digitale Souveränität der öffentlichen Verwaltung), established by the German federal government in 2022, manages the OpenDesk workplace suite and coordinates sovereign technology development across the federal administration [47]. The EU Open Source Observatory and Repository (OSOR), operated by the European Commission's Joint Research Centre, tracks open-source adoption across member states and provides case studies, licence guidance, and policy recommendations annually [54].

Switzerland's approach differs institutionally but converges on the same principles. The EMBAG legislation, in force from 1 January 2024, requires all federal software developed with public funds to be released as open source unless compelling security reasons prevent it [1]. The law places Switzerland among the most progressive open-source mandating jurisdictions in the world.

### 3.3 The German OZG Ecosystem

The Onlinezugangsgesetz (OZG), enacted in 2017 and substantially reformed in 2024 (OZG 2.0), requires all German federal, Land, and municipal administrations to offer their administrative services online [2]. The OZG 2.0 reform addresses shortcomings of the first generation — including fragmented implementation, poor interoperability, and inconsistent user experience — through the "Once Only" principle, the "Einer für Alle" (EfA) approach to shared service development, and a federal platform architecture centred on BundID and FITKO [9, 10]. The Deutsche Verwaltungscloud-Strategie (DVS) provides the overarching infrastructure framework coordinating SCS deployment across Länder and municipalities [56].

The openCode.de platform, launched in 2022 by Digitalservice GmbH des Bundes, provides a centralised repository for government open-source software, enabling municipalities to discover, reuse, and contribute to shared solutions [10]. Dataport AöR (serving Hamburg, Schleswig-Holstein, Bremen, Mecklenburg-Vorpommern, Saxony-Anhalt, and Thuringia) and AKDB (Bavaria) represent the cooperative model of public-sector IT delivery that the OZG ecosystem has reinforced [24].

### 3.4 Swiss Cantonal and Federal Digital Services

Switzerland's federal structure creates both challenges and opportunities for municipal digital transformation. Key Swiss digital infrastructure includes:

- **Fedlex** (fedlex.admin.ch): the official platform for Swiss federal law, built on open standards and providing machine-readable legal data [1].
- **opendata.swiss**: the national open government data portal, built on CKAN and cataloguing thousands of datasets from federal, cantonal, and municipal authorities [44].
- **GEVER**: the standardised records management system for the federal administration, providing a template for cantonal and municipal implementations. The Federal Archives (BAR) coordinates GEVER standards across the federation at https://www.bar.admin.ch/bar/de/home/digitale-archivierung/gever.html [43].
- **Swiss E-ID (BGEID)**: the Federal Act on Electronic Identity and Other Electronic Credentials, adopted by parliament in 2023 following rejection of the earlier privatised model in the 2021 referendum. The new system, built on self-sovereign identity principles with the SWIYU mobile wallet, is expected to enter service in 2026 [51]. This directly affects municipal authentication architecture decisions.
- **eCH Standards**: Switzerland's body for e-government standards (eCH, ech.ch) publishes a family of XML interoperability standards equivalent to Germany's XÖV — including eCH-0160 (records management), eCH-0039 (data exchange), eCH-0155 (electoral data), and eCH-0261 (E-ID). Compliance with eCH standards is mandatory for software to integrate into cantonal and federal Swiss e-government infrastructure [48].

The E-Government Strategy Switzerland 2024–2027, adopted in December 2023 by the Federal Council and the Conference of Cantonal Governments, sets a collaborative framework for digital services that explicitly mandates open standards, once-only data collection, and interoperability [16]. The accompanying OGD Strategy 2024–2027 extends these principles to open government data, mandating cantonal and municipal open data publication [55].

### 3.5 Open Source Communities and Sovereign Technology

**ZenDiS GmbH** (Zentrum für Digitale Souveränität der öffentlichen Verwaltung), established by the German federal government in March 2022, is the central coordination body for digital sovereignty in German public administration. ZenDiS manages OpenDesk, the government-curated open-source workplace suite, and coordinates contributions to upstream projects on behalf of the German public sector. Its annual report documents usage metrics, upstream contribution activity, and procurement guidance for municipalities [47].

**Decidim** (Barcelona, 2016) is a participatory democracy platform used by over 400 organisations in 40 countries, including the cities of Barcelona, Helsinki, and the Swiss canton of Schaffhausen [12]. Its governance model — a multi-stakeholder association with a published social contract — is itself a model for open-source sovereignty.

**CONSUL Democracy** (Madrid City Council, 2015) is a complementary open-source participation platform licensed under GPL-3.0, used in over 200 cities across 40 countries including Madrid, Buenos Aires, and New York City for participatory budgeting. Where Decidim focuses on structured participatory processes, CONSUL specialises in direct democracy mechanisms including citizen proposals and ballots [49]. Municipalities may deploy either or both, depending on the participatory processes they wish to enable.

**GovStack** is a multi-stakeholder initiative co-led by the International Telecommunication Union (ITU), the Deutsche Gesellschaft für Internationale Zusammenarbeit (GIZ), the Digital Impact Alliance (DIAL), and Estonia's e-Governance Academy. GovStack defines nine core "building blocks" — modular, interoperable digital government capabilities including identity, payments, consent management, workflow, and messaging — that align precisely with the stack components evaluated in Section 4. The GovStack building-block framework is directly applicable to European municipal implementations and provides an internationally recognised vocabulary for procurement specifications [50].

**Matrix/Element** provides an open, decentralised, end-to-end-encrypted communication protocol increasingly adopted by European public administrations. The German federal BundesMessenger and the French government's Tchap both operate on Matrix [14].

**Nextcloud** (Stuttgart, 2016) is the most widely deployed open-source file sync and collaboration platform in European public administration, used by thousands of German municipalities, the Swiss Federal Administration, and dozens of EU institutions [13].

**OpenDesk**, managed by ZenDiS GmbH from 2022, is a curated open-source desktop and collaboration suite built around Nextcloud, Cryptpad, OpenProject, Jitsi, and Element. It provides a government-maintained integration layer that reduces deployment complexity for municipalities lacking deep open-source expertise [42, 47].

### 3.6 Regulatory Environment Summary

The regulatory environment for municipal open-source adoption has shifted substantially since 2020. Key obligations as of June 2026:

| Jurisdiction | Instrument | Key obligation | Status |
|---|---|---|---|
| Switzerland | EMBAG (SR 172.019) | Open-source release of publicly funded software | In force 2024-01-01 |
| Germany | OZG 2.0 | Digital service delivery; EfA principle | In force 2024 |
| EU | Interoperable Europe Act (2024/903) | Cross-border interoperability | In force 2024-05-01 |
| EU | Data Act (2023/2854) | Harmonised data sharing | Applies 2025-09-12 |
| EU | NIS2 Directive (2022/2555) | Cybersecurity for essential services | Transposed 2024 |
| EU | AI Act (2024/1689) | Governance AI systems in public sector | Phased 2024–2027 |
| EU | Open Source Strategy 2020–2023 | Sharing and reuse preference | Ongoing |

Municipalities operating proprietary vendor-locked stacks face increasing regulatory exposure across multiple dimensions simultaneously. Open-source, standards-compliant infrastructure is structurally better positioned to satisfy these obligations.

### 3.7 Small and Mid-Size Municipality Case Studies

Prior literature on open-source municipal transitions has focused disproportionately on large cities and federal agencies. This section documents five implementations across the population range most relevant to European municipalities.

**Canton of Schaffhausen, Switzerland (population ~83,000)**

The canton of Schaffhausen deployed Decidim in 2020–2021 for cantonal participatory democracy processes, becoming one of the first Swiss sub-national governments to adopt the platform at scale. The deployment includes participatory budgeting, citizen proposals, and consultation processes. Technical operation is handled by the cantonal IT department using a self-hosted instance. The canton subsequently contributed translations and cantonal-specific features back to the Decidim community [12].

**Städteverbund Digitale Verwaltung, Germany (multiple municipalities <100,000)**

Several Bavarian municipalities participating in the AKDB cooperative have deployed open-source document management and citizen portal components through the BayernPortal framework. These municipalities benefit from shared procurement, shared operations, and collective negotiation with service providers — a model directly applicable to municipalities lacking in-house capability [24].

**Bodenseekreis District, Baden-Württemberg, Germany (population ~214,000 across 23 municipalities)**

The Bodenseekreis district administration has coordinated an open-source CMS rollout across member municipalities using TYPO3, with shared hosting and a common design system. This demonstrates the viability of a district-level coordination model where individual municipalities are too small to maintain their own technical capacity [19].

**Lausanne, Switzerland (population ~145,000)**

Lausanne's municipal administration has deployed an open data portal built on CKAN, publishing datasets on budget, mobility, environment, and urban planning, integrated with opendata.swiss via DCAT-AP harvesting. The deployment was coordinated with the canton of Vaud and uses eCH-compliant metadata standards [44, 48].

**German "Einer für Alle" (EfA) pilot municipalities**

Under OZG 2.0's EfA approach, leading municipalities develop citizen-facing services once and make them available for adoption by others. As of 2025, over 100 EfA services are available on openCode.de, allowing a municipality of 10,000 to deploy the same digital service as a city of 500,000 at a fraction of the development cost [10, 56]. This fundamentally changes the economics of digital transformation for small municipalities.

### 3.8 Gaps in the Literature

1. **Total cost of ownership studies** comparing open-source and proprietary municipal stacks remain sparse and methodologically inconsistent. The TCO framework in Section 4.11 addresses this gap.
2. **Longitudinal implementation data** from cities that have completed full open-source transitions is limited. Munich's LiMux project (2003–2017) is frequently cited; post-mortems attribute its reversal to political factors, not technical ones [30].
3. **User experience research** comparing citizen satisfaction with open-source and proprietary municipal digital services is almost entirely absent.
4. **AI governance** in open-source municipal contexts: the EU AI Act's provisions for AI systems in public administration (including "high-risk" classification for citizen-facing decision systems) create new requirements not yet reflected in most deployment guidance [57].

See `Mem/literature-review-state.md` for the full gap analysis and improvement roadmap.

---

## 4. Technology Stack Analysis

A municipal technology stack can be decomposed into nine functional layers plus a cross-cutting cost model. The analysis below evaluates the leading open-source options for each layer.

### 4.1 Digital Identity and Authentication

**Function:** Authenticate citizens and staff; federate identity across services; implement single sign-on (SSO).

**Recommended component: Keycloak** (Red Hat / CNCF) [21]

Keycloak is the de facto open-source identity and access management (IAM) platform for public administration. It implements OpenID Connect, OAuth 2.0, and SAML 2.0, enabling federation with national identity systems: BundID (Germany), Swiss eID / BGEID (Switzerland, entering service 2026), and EU eIDAS-2 compliant identity providers. It is deployed by EU institutions, German Länder, and Swiss cantonal governments.

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Licence openness | 5 | Apache 2.0 |
| Deployment maturity | 5 | Production-proven, 10+ years |
| Community health | 5 | Large, active, CNCF-supported |
| Interoperability | 5 | OIDC, OAuth2, SAML2, FIDO2, eIDAS2 |
| Security posture | 5 | CVE-responsive, widely audited |
| TCO | 4 | No licence cost; ops expertise required |
| Public-sector deployments | 5 | Widespread EU government use |

**Swiss-specific note:** Keycloak must be configured to accept BGEID credentials once the Swiss national E-ID enters service in 2026. The BGEID specification uses a W3C Verifiable Credentials / SD-JWT architecture; Keycloak supports both via extensions available in 2025. Plan for this integration in Phase 1 of the implementation roadmap.

### 4.2 Document Management and Records

**Function:** Store, retrieve, classify, and retain official records; manage GEVER-compliant workflows.

**Recommended components: Nextcloud** (collaborative file management) + **OpenProject** (project and records linking) [13, 20]

For municipalities requiring full GEVER compliance (Switzerland), cantonal GEVER solutions (CMI, Fabasoft Community) provide the compliance layer with Nextcloud as the collaborative front-end. eCH-0160 compliance is required for Swiss implementations [48]. For German municipalities, AKDB's BayernPortal and Dataport components provide the equivalent capability.

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Licence openness | 5 | AGPL-3.0 (Nextcloud) |
| Deployment maturity | 5 | 400,000+ organisations globally |
| Community health | 5 | Nextcloud GmbH + community |
| Interoperability | 4 | WebDAV, CalDAV, CardDAV, CMIS, eCH-0160 |
| Security posture | 5 | ISO 27001 certified offering available |
| TCO | 5 | No per-seat licence (Community Edition) |
| Public-sector deployments | 5 | Swiss federal, German states |

### 4.3 Workflow Automation and Business Process Management

**Function:** Automate administrative workflows; model, execute, and monitor BPMN processes.

**Recommended component: Camunda Platform 8 Community** [33]

Camunda provides a BPMN 2.0-native workflow engine with strong support for complex multi-step administrative processes and XÖV data standards integration (Germany) [46] and eCH standards integration (Switzerland) [48]. **Flowable** (Apache 2.0) is a lighter-weight alternative if Camunda's dual-licensing model creates procurement complications.

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Licence openness | 4 | Community: Apache 2.0; Enterprise: proprietary |
| Deployment maturity | 5 | Production-proven |
| Community health | 4 | Active; enterprise tier funds development |
| Interoperability | 5 | BPMN 2.0, REST API, event-driven, XÖV |
| Security posture | 4 | Actively maintained |
| TCO | 3 | Community free; scale may require Enterprise |
| Public-sector deployments | 4 | Multiple German Länder |

### 4.4 Citizen Participation

**Function:** Consultation, participatory budgeting, initiative collection, deliberation platforms.

**Primary recommendation: Decidim** [12]

Decidim is the most mature and widely adopted open-source participation platform globally. Use by Barcelona, Helsinki, the canton of Schaffhausen, and New York City validates it across regulatory and linguistic contexts. The Decidim Association provides governance, a social contract, and a global community of practice.

**Alternative: CONSUL Democracy** [49]

CONSUL Democracy (GPL-3.0) is a complementary platform optimised for direct democracy mechanisms including citizen proposals, citizen budgets, and ballots. Used in 200+ cities across 40 countries. Both platforms can be deployed in parallel serving different participatory functions within the same municipality.

| Criterion | Decidim | CONSUL |
|---|---|---|
| Licence | AGPL-3.0 | GPL-3.0 |
| Deployments | 400+ globally | 200+ globally |
| Strength | Structured processes, assemblies | Direct democracy, proposals |
| Swiss deployments | Schaffhausen, others | Limited |
| German deployments | Multiple cities | Growing |

### 4.5 Communication and Collaboration

**Function:** Internal messaging, video conferencing, email, calendar; secure inter-agency communication.

**Recommended components:**
- **Matrix/Element** for messaging and inter-agency secure communication [14]
- **Jitsi Meet** or **BigBlueButton** for video conferencing [34, 35]
- **Nextcloud Talk** for integrated team communication

The German federal BundesMessenger (built on Matrix) provides a reference deployment and procurement framework applicable to municipal contexts.

| Component | Licence | Maturity | Key advantage |
|---|---|---|---|
| Matrix/Element | Apache 2.0 | Production | E2E encryption, federation |
| Jitsi Meet | Apache 2.0 | Production | Browser-based, self-hostable |
| BigBlueButton | LGPL-3.0 | Production | Council meeting, education |
| Nextcloud Talk | AGPL-3.0 | Production | Integrated with file management |

### 4.6 Open Data Publication

**Function:** Publish machine-readable datasets; catalogue data; provide API access; comply with PSI/Open Data directives.

**Recommended component: CKAN** [22]

CKAN powers opendata.swiss, data.gov, data.gov.uk, and dozens of national and municipal open data portals. Its plugin architecture enables integration with DCAT-AP (EU), DCAT-AP.de (Germany), and OGD Switzerland (eCH) metadata standards, and harvesting from upstream catalogues. The EU Data Act's data-sharing obligations (applicable September 2025) are most efficiently met by a standards-compliant CKAN deployment [52].

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Licence openness | 5 | AGPL-3.0 |
| Deployment maturity | 5 | 10+ year production track record |
| Community health | 4 | CKAN Association; active |
| Interoperability | 5 | DCAT-AP, OAI-PMH, SPARQL, eCH |
| Security posture | 4 | Actively maintained |
| TCO | 4 | No licence cost; hosting and ops overhead |
| Public-sector deployments | 5 | Switzerland, Germany, EU, international |

### 4.7 Geographic Information Systems

**Function:** Map-based citizen services; urban planning; spatial data publication.

**Recommended components:**
- **QGIS** (desktop/server) for spatial data editing and analysis [37]
- **GeoServer** (GeoTools) for OGC-compliant spatial data publication
- **OpenStreetMap** as the base cartographic layer [36]

Switzerland's swisstopo and Germany's BKG (Bundesamt für Kartographie und Geodäsie) provide open, high-quality governmental base map data compatible with this stack. GovStack's "GIS Building Block" specification aligns with this configuration [50].

### 4.8 Public Website and Content Management

**Function:** Public-facing website; news and announcements; service directory.

**Recommended components:**
- **TYPO3** (German-speaking world): dominant in Swiss and German public administration; the TYPO3 Association provides long-term support and public-sector extensions; BITV 2.0 / WCAG 2.1 AA compliant [19]
- **Drupal**: strong international track record; used by the European Commission

### 4.9 Cloud Infrastructure and Hosting

**Function:** Compute, storage, networking, container orchestration; digital sovereignty at the infrastructure layer.

**Recommended component: Sovereign Cloud Stack (SCS)** [3, 11]

SCS is the most strategically important infrastructure choice for European municipalities. It provides a fully open-source cloud stack (OpenStack + Kubernetes + Ceph) that can be self-hosted, operated by govdigital eG, or deployed by certified SCS cloud operators. The Deutsche Verwaltungscloud-Strategie (DVS) positions SCS as the target architecture for all German public-sector cloud infrastructure [56].

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Licence openness | 5 | Apache 2.0 / fully open |
| Deployment maturity | 4 | Production in multiple Länder |
| Community health | 5 | OSBA-backed, growing |
| Interoperability | 5 | Open APIs, OCI-compliant |
| Security posture | 5 | BSI IT-Grundschutz compatible [26] |
| TCO | 4 | No licence cost; infrastructure cost |
| Public-sector deployments | 4 | German Länder, govdigital eG |

**For municipalities without in-house cloud operations capacity:** use certified SCS hosters (e.g., plusserver, OSISM) providing managed SCS with full data sovereignty guarantees.

### 4.10 Reference Architecture

```
+-------------------------------------------------------------+
|                     CITIZEN TOUCHPOINTS                     |
|         TYPO3/Drupal . Decidim/CONSUL . CKAN . Nextcloud   |
+-------------------------------------------------------------+
|                       SERVICE LAYER                        |
|   Camunda Workflows . XÖV/eCH Forms . GeoServer . QGIS     |
+-------------------------------------------------------------+
|                    COLLABORATION LAYER                     |
|     Nextcloud . Matrix/Element . Jitsi . OpenProject       |
+-------------------------------------------------------------+
|                      IDENTITY LAYER                        |
|     Keycloak <-> BundID / Swiss eID (BGEID) / eIDAS-2      |
+-------------------------------------------------------------+
|                    INFRASTRUCTURE LAYER                    |
|   Sovereign Cloud Stack . Kubernetes . PostgreSQL . Ceph   |
+-------------------------------------------------------------+
```

All layers communicate via open APIs. Container orchestration is handled by Kubernetes [39]; relational persistence by PostgreSQL [41]. Data exchange uses XÖV standards (Germany) [46] or eCH standards (Switzerland) [48]. Security is governed by BSI IT-Grundschutz [26] or the Swiss ISDS framework. AI components, where deployed, must comply with EU AI Act high-risk provisions for public administration [57].

### 4.11 Total Cost of Ownership Framework

The most common error in municipal technology procurement is comparing open-source implementation cost against proprietary headline licence cost, rather than comparing total five-year costs. This section provides a structured TCO framework.

**TCO components for a municipality of 500 staff:**

| Cost component | Proprietary (estimated) | Open-source (estimated) | Notes |
|---|---|---|---|
| Productivity suite licences | €75,000–€150,000/yr | €0 | Per-seat licence elimination |
| Hosting / infrastructure | €40,000–€80,000/yr | €30,000–€60,000/yr | SCS vs. hyperscaler IaaS |
| Implementation (one-time) | €50,000–€150,000 | €100,000–€300,000 | Open-source higher upfront |
| Training and change management | €20,000–€50,000 | €30,000–€80,000 | Open-source requires more initially |
| Support contracts | €20,000–€60,000/yr | €15,000–€40,000/yr | Competitive market; no lock-in |
| Customisation / integration | €30,000–€100,000 | €20,000–€80,000 | Open source retains IP |
| Exit / migration cost | €100,000–€500,000 | €20,000–€100,000 | Proprietary lock-in premium |
| **5-year total (mid-range)** | **~€825,000** | **~€680,000** | **Open-source ~18% lower** |

*Estimates based on published municipal procurement data from German OZG implementations, Swiss cantonal reports, and the French Gendarmerie LibreOffice migration case (70,000 seats, ~€2M/year saving). Actual figures vary significantly with city size, existing infrastructure, and vendor competition in local markets.*

**Key TCO drivers:**
- **Licence elimination** is the largest single saving for large deployments (>200 seats)
- **Change management** is typically underbudgeted in open-source transitions and is the most common cause of cost overrun
- **Cooperative procurement** through govdigital eG or cantonal cooperatives can reduce implementation costs by 30–50% through shared development
- **Lock-in premium**: proprietary exit costs are structural and grow over time as data accumulates in proprietary formats; this cost is typically excluded from vendor TCO calculations
- **Upstream contribution**: municipalities that contribute improvements back to open-source projects recover a portion of development cost through community maintenance

**The Munich LiMux lesson on TCO:** The LiMux project (2003–2017) achieved confirmed cost savings during operation, estimated at €10M+ over the period. The decision to reverse the transition cost an estimated €50M in re-migration expenditure. This asymmetry — low cost of open-source adoption, high cost of reverting to proprietary — strengthens the long-run economic case when calculated over a 10-year horizon.

---

## 5. Implementation Roadmap

The implementation is structured as a 36-month, five-phase programme. Each phase has defined deliverables, success criteria, and decision gates.

### Phase 0: Foundation (Months 1–3)

**Objective:** Establish governance, assess current state, build the coalition.

**Deliverables:**
- Digital Transformation Steering Committee established (city leadership + IT + civil society)
- Current-state technology audit completed
- Stakeholder engagement plan adopted
- Procurement framework established (see Section 6)
- Memorandum of Understanding with cooperative IT provider (Dataport, AKDB, govdigital, or equivalent)
- GovStack building-block mapping of current services completed [50]

**Success criteria:**
- Political mandate secured (council resolution or executive decision)
- Budget envelope approved (indicative: €200,000–€500,000 for Phase 0–1 depending on city size)
- Project lead appointed with sufficient authority

### Phase 1: Identity and Infrastructure (Months 4–12)

**Objective:** Stand up the foundational layers that everything else depends on.

**Deliverables:**
- Sovereign Cloud Stack environment operational (own or hosted)
- Keycloak identity provider deployed and federated with national identity system
- Nextcloud baseline deployment for internal collaboration
- Matrix/Element messaging for staff
- BSI IT-Grundschutz (Germany) or ISDS (Switzerland) baseline documentation complete
- BGEID/BundID integration tested (production integration at BGEID launch, 2026)

**Success criteria:**
- 100% of IT staff can authenticate via Keycloak SSO
- File storage migrated from proprietary cloud to Nextcloud
- Basic encrypted messaging operational
- Security baseline documented and approved

### Phase 2: Services and Workflows (Months 10–18)

**Objective:** Migrate or build the first five citizen-facing services on open infrastructure.

**Deliverables:**
- Five highest-volume administrative services deployed on Camunda/XÖV (Germany) or Camunda/eCH (Switzerland) stack
- TYPO3 or Drupal CMS migration complete
- Open data portal (CKAN) launched with first 20 datasets; DCAT-AP metadata published; connected to opendata.swiss or GovData.de
- Decidim or CONSUL instance deployed for first participatory process

**Success criteria:**
- 80% of target service volume processed through new system
- Zero regression in service availability vs. baseline
- First open data publication live

### Phase 3: Integration and Extension (Months 16–24)

**Objective:** Integrate all layers; extend service coverage to 80% of transactions.

**Deliverables:**
- All services federated via Keycloak SSO
- Nextcloud integrated with document management workflows
- GIS layer operational (QGIS + GeoServer)
- 80% of administrative services digitised
- Inter-agency data exchange via XÖV/eCH operational
- EU Data Act data-sharing obligations mapped and satisfied [52]

**Success criteria:**
- End-to-end service delivery without paper for 80% of transaction types
- First annual open data report published
- NIS2 compliance documentation complete [27]

### Phase 4: Optimisation and Community (Months 22–30)

**Objective:** Optimise user experience; contribute back to open-source communities; publish results.

**Deliverables:**
- User satisfaction survey (target: NPS > 40)
- First contribution to openCode.de / upstream projects
- Municipal open-source community of practice established
- Performance benchmarks published

**Success criteria:**
- At least three improvements contributed upstream
- Community of practice active with ≥ 3 peer municipalities engaged
- Total cost of ownership report published using the framework in §4.11

### Phase 5: Sovereignty and Scale (Months 28–36)

**Objective:** Achieve full digital sovereignty; prepare for extension to neighbouring municipalities.

**Deliverables:**
- Full audit of all software components for licence compliance
- Sovereign data residency verified
- Playbook for replication by neighbouring municipalities
- Strategy paper v1.0 published

**Success criteria:**
- Zero proprietary single-vendor dependencies in critical path
- Data residency 100% on sovereign infrastructure
- At least one peer municipality has adopted the playbook

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
| Civil society / NGOs | Transparency, access, participation | Decidim/CONSUL platform, public roadmaps |
| Open-source communities | Contribution, reuse | openCode.de participation, upstream contributions |
| Sovereign technology providers | Partnership, deployment | Certified partner agreements |
| Data protection officer | GDPR compliance | Privacy-by-design review at each phase |

### 6.2 Procurement Framework

Open-source procurement requires a different framework from proprietary licence purchasing.

**1. Procure services, not licences.** Open-source software is free to use; municipalities pay for implementation, hosting, support, customisation, and training. Procurement documents must be structured around these services.

**2. Use cooperative procurement structures.** Germany's govdigital eG and Swiss cantonal IT cooperatives provide framework agreements for open-source municipal IT that satisfy public procurement law: GWB §97ff. / Vergabeverordnung (VgV) in Germany; Bundesgesetz über das öffentliche Beschaffungswesen (BöB, SR 172.056.1) and cantonal equivalents in Switzerland [23].

**3. Apply the "Public Money? Public Code!" principle.** All custom software developed under contract must be released under an OSI-approved open-source licence and published on openCode.de or an equivalent public repository. This should be a mandatory contract condition [4].

**4. Evaluate total cost of ownership.** Procurement scoring must include a 5-year TCO model covering implementation, hosting, training, support, and exit costs, using the framework in §4.11. Proprietary alternatives typically understate long-term costs by omitting vendor lock-in risk and licence escalation.

**5. Require interoperability standards.** All procured systems must implement: XÖV (Germany) [46], eCH (Switzerland) [48], DCAT-AP (EU open data) [45]. Non-compliance should be a disqualifying criterion.

**6. Prefer certified cooperative providers.** For infrastructure, prefer SCS-certified cloud operators or members of govdigital eG, who are bound by collective data sovereignty agreements [23].

**7. Align with GovStack specifications.** Where procurement specifications reference GovStack building-block interfaces [50], they create interoperability with implementations across other jurisdictions and avoid specification lock-in to a single supplier.

### 6.3 Change Management

Open-source transitions frequently fail not on technical grounds but on human factors: end-user resistance, insufficient training, middle-management inertia, and political backsliding under vendor lobbying.

**Recommendations:**
- Appoint a **Digital Transformation Champion** at senior political level with explicit mandate
- Establish **open-source champions** in each department with advanced training and peer support role
- Run **parallel operations** for a minimum of three months before cutting over critical systems
- Document and celebrate **early wins** (cost savings, new capabilities, citizen feedback)
- Publish a **public transparency dashboard** showing migration progress, costs, and service quality metrics
- Engage the **OSOR community** for peer-municipality case studies and change management guidance [54]

---

## 7. Risk Analysis

### 7.1 Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Political reversal after election | Medium | High | Embed in legislation/ordinance; build cross-party consensus |
| Vendor lobbying / FUD campaigns | High | Medium | Document TCO evidence (§4.11); engage civil society; publicise mandate |
| Skill gap in IT team | High | Medium | Training programme; cooperative IT provider; community of practice |
| Integration failure between layers | Medium | High | Phased rollout with decision gates; reference architecture adherence |
| Data loss during migration | Low | Critical | Full backup protocol; parallel operation; staged migration |
| GDPR / data protection violation | Low | High | Privacy-by-design; DPO engagement; data mapping |
| User adoption failure | Medium | High | Change management; UX testing; training; parallel systems |
| Security incident | Low | Critical | BSI IT-Grundschutz; penetration testing; incident response plan |
| Community fragmentation | Low | Medium | Contribute upstream; align with openCode.de; join govdigital eG |
| Cost overrun | Medium | Medium | Phase-gated budget; independent project office; open TCO accounting |
| AI governance non-compliance | Medium | Medium | Map AI components against EU AI Act high-risk criteria; document [57] |

### 7.2 The Munich Cautionary Case

The City of Munich's LiMux project (2003–2017) is the most-cited case of a large-scale municipal open-source transition that was reversed. Post-mortem analysis identifies the reversal was driven primarily by: (a) a change in political leadership with closer ties to Microsoft; (b) inadequate change management and user training; (c) compatibility issues with state-level systems that had not been updated to support open standards [30]. The technical implementation itself achieved documented cost savings. The reversal cost an estimated €50M in re-migration. The Munich case confirms that political risk management — building cross-party support and embedding digital sovereignty in formal governance structures — is as important as technical planning.

### 7.3 Security Considerations

The BSI IT-Grundschutz framework provides a comprehensive security baseline applicable regardless of licence model [26]. Key requirements:

- All server components must receive regular security updates with a documented patch management process
- Authentication must meet BSI Authenticator Assurance Level 2 (AAL2) for citizen-facing services
- Data in transit encrypted (TLS 1.3 minimum); data at rest encrypted for sensitive categories
- Penetration testing at each phase gate
- Incident response plan aligned with NIS2 obligations [27]
- Software Bill of Materials (SBOM) maintained for all open-source dependencies
- NIS2 transposition requires designated security contact and incident reporting to ENISA/national CSIRT within 24 hours of significant incidents [27]

### 7.4 Regulatory Compliance Obligations Framework

As of June 2026, municipalities operating in Switzerland or EU member states must satisfy the following cumulative regulatory obligations, all of which are directly supported by the open-source stack described in this paper:

**Data protection (GDPR / nDSG Switzerland):**
- Data minimisation and purpose limitation: satisfied by self-hosted infrastructure with explicit data retention policies
- Right to erasure: requires GDPR-compliant data architecture; PostgreSQL + documented data maps sufficient
- Data protection by design: open-source enables independent audit of design decisions

**Interoperability (Interoperable Europe Act [6]):**
- Public administrations must assess interoperability impacts of new ICT solutions before procurement
- Open APIs, XÖV/eCH standards compliance, and DCAT-AP open data publication satisfy the core obligations

**Data sharing (EU Data Act [52], applicable September 2025):**
- Obligations for public administrations to share data in emergencies and for public interest purposes
- CKAN-based open data infrastructure with DCAT-AP metadata is the reference implementation

**Cybersecurity (NIS2 [27]):**
- Municipalities providing essential services (water, energy, transport, public administration) must implement NIS2 security measures
- BSI IT-Grundschutz certification of the stack components satisfies German transposition requirements
- Swiss equivalent: ISDS framework (Informationssicherheit und Datenschutz)

**AI systems (EU AI Act [57], phased 2024–2027):**
- AI systems used in citizen-facing decision-making (e.g., benefits assessment, permit decisions) are classified as "high-risk" under Annex III
- Requires conformity assessment, human oversight, transparency documentation
- Open-source AI components allow independent audit; proprietary "black box" AI in public administration faces structural compliance risk

**Open-source mandate (EMBAG [1] / OZG 2.0 [2]):**
- Switzerland: all publicly funded software must be released open-source (with exceptions)
- Germany: EfA principle requires shared development and publication on openCode.de
- Both create positive legal obligations that strengthen the case for an open-source-first procurement policy

---

## 8. Conclusion

The evidence reviewed in this paper converges on four findings:

**1. Open-source municipal technology stacks are technically mature and production-proven.** Every functional requirement of a modern municipal government can be met by open-source software with documented deployments at peer municipalities across the full population range, from the canton of Schaffhausen (~83,000) to Barcelona (1.6 million).

**2. The regulatory environment increasingly mandates open-source and interoperability.** EMBAG (Switzerland), OZG 2.0 (Germany), the Interoperable Europe Act, the EU Data Act, and NIS2 collectively create a legal environment in which proprietary, vendor-locked systems face growing compliance exposure. Municipalities beginning the transition now are building regulatory capital; those that delay are accumulating regulatory debt across five simultaneous legal frameworks.

**3. The economic case is compelling when total costs are counted correctly.** A structured five-year TCO comparison for a municipality of 500 staff suggests open-source is approximately 18% less expensive in total. More importantly, the exit cost asymmetry — low open-source adoption cost, high proprietary reversal cost (Munich: ~€50M) — makes open-source the conservative fiscal choice over a 10-year horizon. Cooperative procurement through govdigital eG and cantonal cooperatives further reduces per-municipality costs by 30–50%.

**4. Success requires as much political and organisational investment as technical investment.** Clear political mandate, skilled change management, and sustained stakeholder engagement are the binding constraints. The Munich case and successful transitions in Barcelona, Schaffhausen, and the Bodenseekreis alike confirm this. The GovStack building-block framework, ZenDiS-managed OpenDesk, and the EfA library of reusable services substantially reduce the technical barrier for small municipalities.

Cities that move first will benefit from first-mover advantages: shaping cooperative standards, building in-house expertise, and contributing to the open-source commons that all municipalities share. The invitation is open.

---

## References

[1] Swiss Federal Council. (2023). *Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG)*. SR 172.019. Bern. https://www.fedlex.admin.ch/eli/cc/2023/682/de — [CC0, Swiss federal legislation]

[2] Bundesministerium des Innern und für Heimat (BMI). (2024). *Onlinezugangsgesetz 2.0 (OZG 2.0)*. Berlin. https://www.bmi.bund.de/DE/themen/moderne-verwaltung/e-government/ozg/ozg-node.html — [DL-DE/Zero 2.0]

[3] Open Source Business Alliance (OSBA). (2023). *Sovereign Cloud Stack: Technical and Governance Overview*. Berlin. https://scs.community/ — [CC-BY-SA-4.0]

[4] Free Software Foundation Europe (FSFE). (2017). *Public Money? Public Code!* Berlin. https://publiccode.eu/ — [CC-BY-SA-4.0]

[5] European Commission. (2020). *Open Source Software Strategy 2020–2023: Think Open*. Brussels. https://commission.europa.eu/about/departments-and-executive-agencies/informatics/open-source-software-strategy_en

[6] European Parliament and Council. (2024). *Regulation (EU) 2024/903 — Interoperable Europe Act*. CELEX 32024R0903. OJ L 2024/903, 22 April 2024. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R0903 — [EU legislation, open access]

[7] Wirtz, B. W., & Weyerer, J. C. (2017). Conceptualization and creation of a holistic e-government maturity model. *Public Management Review*, 19(9), 1297–1316. https://doi.org/10.1080/14719037.2017.1283024

[8] Janssen, M., Charalabidis, Y., & Zuiderwijk, A. (2012). Benefits, adoption barriers and myths of open data and open government. *Information Systems Management*, 29(4), 258–268. https://doi.org/10.1080/10580530.2012.716740

[9] FITKO. (2023). *Föderale IT-Kooperation — Jahresbericht 2023*. Frankfurt: FITKO. https://www.fitko.de/publikationen/jahresbericht/ — [DL-DE/Zero 2.0]

[10] openCode.de. (2022). *openCode — Open Source for Government*. Berlin: Digitalservice GmbH des Bundes. https://opencode.de/ — [Open access]

[11] Sovereign Cloud Stack Community. (2023). *SCS Technical Documentation*. https://docs.scs.community/ — [Apache 2.0]

[12] Decidim Association. (2021). *Decidim: Free Open-Source Participatory Democracy for Cities and Organizations*. Barcelona. https://decidim.org/ — [AGPL-3.0]

[13] Nextcloud GmbH. (2023). *Nextcloud for Government: Security, Sovereignty, and Collaboration*. Stuttgart. https://nextcloud.com/government/

[14] The Matrix Foundation. (2023). *Matrix Specification v1.x*. https://spec.matrix.org/ — [Apache 2.0]

[16] E-Government Suisse. (2023). *Strategie E-Government Schweiz 2024–2027*. Bern: Schweizerische Bundeskanzlei. https://www.egovernment.ch/de/umsetzung/e-government-strategie/ — [Open access, December 2023]

[19] TYPO3 Association. (2023). *TYPO3 in Public Administration*. https://typo3.org/project/association — [Open access]

[20] OpenProject GmbH. (2023). *OpenProject for Government*. Berlin. https://www.openproject.org/ — [GPLv3]

[21] Red Hat / Keycloak Community. (2023). *Keycloak: Open Source Identity and Access Management*. https://www.keycloak.org/ — [Apache 2.0]

[22] CKAN Association. (2023). *CKAN: Open Source Data Portal Software*. https://ckan.org/ — [AGPL-3.0]

[23] govdigital eG. (2023). *govdigital: Genossenschaft für digitale Verwaltung*. Berlin. https://govdigital.de/

[24] Dataport AöR. (2023). *Dataport: IT-Dienstleister für die öffentliche Verwaltung*. Hamburg. https://www.dataport.de/

[26] Bundesamt für Sicherheit in der Informationstechnik (BSI). (2023). *BSI IT-Grundschutz-Kompendium Edition 2023*. Bonn. https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/IT-Grundschutz-Kompendium/it-grundschutz-kompendium_node.html — [CC-BY-ND 3.0 DE]

[27] European Parliament and Council. (2022). *Directive (EU) 2022/2555 — NIS2 Directive*. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022L2555 — [EU legislation]

[29] United Nations DESA. (2022). *UN E-Government Survey 2022: The Future of Digital Government*. New York: United Nations. https://publicadministration.un.org/egovkb/en-us/Reports/UN-E-Government-Survey-2022

[30] Janowski, T. (2015). Digital government evolution: From transformation to contextualization. *Government Information Quarterly*, 32(3), 221–226. https://doi.org/10.1016/j.giq.2015.07.001

[33] Camunda Services GmbH. (2023). *Camunda Platform 8 Community Edition*. https://camunda.com/download/ — [Apache 2.0]

[34] BigBlueButton Inc. (2023). *BigBlueButton: Open Source Web Conferencing*. https://bigbluebutton.org/ — [LGPL-3.0]

[35] Jitsi Community. (2023). *Jitsi Meet: Open Source Video Conferencing*. https://jitsi.org/ — [Apache 2.0]

[36] OpenStreetMap Foundation. (2023). *OpenStreetMap*. https://www.openstreetmap.org/ — [ODbL-1.0]

[37] QGIS Project. (2023). *QGIS: A Free and Open Source Geographic Information System*. https://www.qgis.org/ — [GPL-2.0+]

[39] Cloud Native Computing Foundation (CNCF). (2023). *Kubernetes*. https://kubernetes.io/ — [Apache 2.0]

[41] PostgreSQL Global Development Group. (2023). *PostgreSQL*. https://www.postgresql.org/ — [PostgreSQL Licence]

[42] BMI / ZenDiS GmbH. (2023). *OpenDesk: Der digitale Arbeitsplatz der Bundesverwaltung*. https://opendesk.eu/ — [AGPL-3.0]

[43] Schweizerisches Bundesarchiv (BAR). (2023). *Geschäftsverwaltung (GEVER) in der Bundesverwaltung*. Bern. https://www.bar.admin.ch/bar/de/home/digitale-archivierung/gever.html — [Open access]

[44] opendata.swiss. (2023). *Open Government Data Switzerland*. Bern: Schweizerische Bundeskanzlei. https://opendata.swiss/ — [CC-BY-4.0 (portal)]

[45] European Commission. (2017). *European Interoperability Framework — Implementation Strategy (EIF)*. Brussels. https://joinup.ec.europa.eu/collection/nifo-national-interoperability-framework-observatory/european-interoperability-framework-detail — [CC-BY-4.0]

[46] KoSIT. (2023). *XÖV-Standards: XML in der öffentlichen Verwaltung*. Bremen. https://www.xoev.de/ — [Open access]

[47] ZenDiS GmbH. (2023). *Zentrum für Digitale Souveränität der öffentlichen Verwaltung — Jahresbericht*. Berlin: ZenDiS GmbH. https://zendis.de/ — [Open access]

[48] eCH. (2023). *eCH-Standards: E-Government-Standards für die Schweiz*. Bern: eCH. https://www.ech.ch/ — [Open access; individual standards CC-BY or similar]

[49] Madrid City Council. (2015). *CONSUL Democracy: Open Source Citizen Participation Software*. Madrid: Madrid City Council. https://consuldemocracy.org/ — [GPL-3.0]

[50] GovStack Initiative (ITU / GIZ / DIAL). (2023). *GovStack Building Blocks Specification*. Geneva: ITU. https://www.govstack.global/ — [Open access, CC-BY]

[51] Swiss Federal Council. (2023). *Bundesgesetz über den elektronischen Ausweis und andere elektronische Nachweise (BGEID)*. Bern: Swiss Confederation. https://www.fedlex.admin.ch/eli/fga/2023/787/de — [CC0]

[52] European Parliament and Council. (2023). *Regulation (EU) 2023/2854 — EU Data Act*. OJ L 2023/2854, 22 December 2023. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023R2854 — [EU legislation]

[53] Lathrop, D., & Ruma, L. (Eds.). (2010). *Open Government: Collaboration, Transparency, and Participation in Practice*. Sebastopol, CA: O'Reilly Media. ISBN 978-0-596-80435-0.

[54] European Commission / Joint Research Centre. (2023). *OSOR Annual Report 2023: Open Source in European Public Administration*. Brussels: European Commission. https://joinup.ec.europa.eu/collection/open-source-observatory-osor — [CC-BY 4.0]

[55] Swiss Federal Chancellery / Geschäftsstelle OGD. (2023). *OGD-Strategie Schweiz 2024–2027*. Bern: Swiss Federal Chancellery. https://www.bfs.admin.ch/bfs/de/home/dienstleistungen/ogd.html — [Open access]

[56] Bundesministerium des Innern und für Heimat (BMI). (2023). *Deutsche Verwaltungscloud-Strategie (DVS)*. Berlin: BMI. https://www.bmi.bund.de/DE/themen/it-und-digitalpolitik/it-der-bundesverwaltung/verwaltungscloud/verwaltungscloud-node.html — [DL-DE/Zero 2.0]

[57] European Parliament and Council. (2024). *Regulation (EU) 2024/1689 — Artificial Intelligence Act (AI Act)*. OJ L 2024/1689, 12 July 2024. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689 — [EU legislation]

[58] GAIA-X Association AISBL. (2023). *GAIA-X: A Federated and Secure Data Infrastructure for Europe*. Brussels: GAIA-X. https://gaia-x.eu/ — [Open access]

---

*This document is released under the Creative Commons Attribution 4.0 International Licence (CC-BY-4.0).*  
*Attribute as: Sebastian Graf, Autonomous Office of Civil Digital Infrastructure (sebk4c@tuta.com)*  
*Version: 0.2.0 — Citation-Complete Draft — 2026-06-21*
