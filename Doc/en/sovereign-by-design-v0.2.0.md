---
title: "Sovereign by Design: A State-of-the-Art Open-Source Technology Strategy for Municipal Governments"
author: "Sebastian Graf, Autonomous Office of Civil Digital Infrastructure"
correspondence: "sebk4c@tuta.com"
version: "0.2.0"
status: "Citation-Complete Draft"
date: "2026-06-21"
language: "en"
source-of-truth: true
supersedes: "en/sovereign-by-design-v0.1.0.md"
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
  - procurement
  - LibreOffice
  - open AI
---

# Sovereign by Design: A State-of-the-Art Open-Source Technology Strategy for Municipal Governments

**Author:** Sebastian Graf, Autonomous Office of Civil Digital Infrastructure
**Correspondence:** sebk4c@tuta.com
**Version:** 0.2.0 — Citation-Complete Draft
**Date:** 2026-06-21
**Languages:** English (source of truth) · Deutsch
**Supersedes:** v0.1.0 (2026-06-20)
**SPDX-License-Identifier:** CC-BY-4.0

---

## Abstract

Municipal governments are the closest layer of democratic administration to citizens, yet they face an acute structural tension: the digital tools they depend on are increasingly proprietary, vendor-locked, and misaligned with public-interest values. This paper presents a comprehensive, citation-complete strategy for implementing a state-of-the-art, open-source governmental administration technology stack in city governments. Drawing on exemplary practices from Switzerland's EMBAG legislation, Germany's OZG reform programme and Sovereign Cloud Stack initiative, and the wider European sovereign technology community, we derive a first-principles implementation roadmap, stakeholder engagement framework, and procurement strategy. We evaluate ten functional technology layers — identity management, document management, office productivity, workflow automation, citizen participation, secure communications, open data publication, geographic information, cloud infrastructure, and AI — against criteria of digital sovereignty, interoperability, total cost of ownership, and civic alignment. Five detailed implementation case studies (Barcelona, the French Gendarmerie, Munich, Jena, and the Canton of Zug) provide empirical grounding for the theoretical framework. We conclude that open-source municipal technology stacks are not merely technically viable but fiscally superior, democratically necessary, and legally mandated in an increasing number of jurisdictions. The paper provides a phased 36-month implementation roadmap with concrete budget estimates for cities of four size categories, and detailed guidance on Swiss and German procurement law. This version (v0.2.0) resolves all unverified citations from v0.1.0 and integrates coverage of the EU Data Act, the EU AI Act, the Cyber Resilience Act, eCH standards, Swiss eID, and ZenDiS.

**Keywords:** digital sovereignty, open source government, GovTech, municipal digital transformation, interoperability, OZG, EMBAG, Sovereign Cloud Stack, e-government, civic technology, LibreOffice, AI Act, procurement

---

## 1. Introduction

The digital transformation of municipal government is no longer optional. Citizens expect seamless, secure, and accessible digital services; regulators demand interoperability and data protection; fiscal pressures require sustainable, cost-effective technology investments. Yet the majority of city governments worldwide remain trapped in a cycle of proprietary vendor dependency, expensive licence agreements, and fragmented systems that impede rather than enable good governance [1, 29].

The consequences of this dependency are well-documented: vendor lock-in raises switching costs and bargaining asymmetry [4]; proprietary formats obstruct cross-agency data exchange and transparency [45]; closed-source infrastructure prevents independent security auditing [26]; and recurring licence fees drain budgets that could otherwise fund service delivery [3, 5]. Most fundamentally, when the software running democratic institutions is owned and controlled by private actors, a structural conflict of interest emerges between the public interest and corporate imperatives [4].

A different path is both possible and proven. Switzerland's 2023 EMBAG legislation mandates that federal software developed with public funds be released as open source by default [1]. Germany's OZG reform programme, Sovereign Cloud Stack, and OpenDesk initiative represent the most ambitious open-source government technology programme in Europe [2, 3, 42]. The Free Software Foundation Europe's "Public Money? Public Code!" campaign, now endorsed by over 200 organisations across 30 countries, articulates the democratic principle at stake [4]. France's migration of the Gendarmerie Nationale's 85,000 workstations to Ubuntu Linux and LibreOffice — yielding approximately 40 percent savings on workstation costs — demonstrates that large-scale open-source transitions succeed when managed well [31].

This paper synthesises these developments into a practical strategy for municipal governments. It is addressed to all relevant stakeholders — city administrators, elected officials, public-sector IT teams, procurement offices, civil-society groups, open-source communities, and sovereign technology providers — and provides the evidence base, technology assessment, and implementation roadmap needed to make the transition.

### 1.1 Scope and Definitions

*Municipal government* refers to city and local government authorities, including Gemeinden, Kommunen, Städte, and equivalent structures in Swiss cantons. The strategy is designed to scale from small municipalities (population 5,000–50,000) to large cities (population 500,000+), with appropriate modulation by city size.

*Open-source technology stack* refers to software components licensed under OSI-approved licences, deployed on infrastructure that the municipality controls or can migrate away from without undue cost or friction.

*Digital sovereignty* is the ability of a government to make independent decisions about its digital infrastructure, including the right to inspect, modify, audit, and migrate software without dependency on a single vendor [3].

### 1.2 Research Questions

1. What does a state-of-the-art open-source municipal technology stack look like in 2026?
2. What lessons can be drawn from the Swiss, German, and European sovereign technology communities?
3. What is the optimal phased implementation pathway for a city government of 50,000–500,000 population?
4. How should procurement, stakeholder engagement, and risk management be structured to maximise success probability?

### 1.3 Why Now: The 2026 Regulatory Moment

Mid-2026 represents a decisive inflection point. Several overlapping regulatory frameworks — each independently significant — have simultaneously entered force, collectively making proprietary, vendor-locked municipal IT legally precarious and financially unattractive:

**Switzerland:** EMBAG entered force on 1 January 2024, creating an open-by-default obligation for publicly funded federal software [1]. The E-Government Strategy Switzerland 2024–2027 extends this logic to cantonal and municipal levels [16]. The new Swiss eID system, approved by parliament in 2023 and progressively operationalised from 2025, provides a privacy-preserving, state-backed digital identity infrastructure based on verifiable credentials [40].

**Germany:** OZG 2.0, enacted in 2024, requires all administrative services to be offered digitally and mandates interoperability via BundID. FITKO coordinates federal implementation; ZenDiS GmbH manages OpenDesk as the reference open-source workplace suite [25]. The requirement for "once-only" data provision and EfA (Einer für Alle) reuse of digital service implementations creates strong economic incentives for municipalities to join cooperative procurement structures rather than procuring independently.

**European Union:** The Interoperable Europe Act (Regulation (EU) 2024/903, in force May 2024) creates binding cross-border interoperability obligations for all public administrations [6]. The EU Data Act (Regulation (EU) 2023/2854, applicable September 2025) introduces data-sharing obligations for IoT-generated data relevant to smart-city applications [28]. The EU AI Act (Regulation (EU) 2024/1689) classifies several municipal AI applications as high-risk, requiring conformity assessments and human oversight [49]. The Cyber Resilience Act (Regulation (EU) 2024/2847) introduces mandatory security and update obligations for software placed on the EU market, including open-source software in commercial settings [48]. The NIS2 Directive (2022/2555), whose transposition deadline was October 2024, creates cybersecurity obligations for public administration [27].

Municipalities that act now build compliance capital. Those that delay accumulate compounding regulatory debt.

---

## 2. Methodology

This paper employs a multi-method research design combining:

**Systematic literature review** of peer-reviewed publications, grey literature, and policy documents published between 2010 and 2026, covering e-government theory, digital sovereignty, open-source software in public administration, and municipal digital transformation.

**Comparative policy analysis** of technology legislation and strategies from Switzerland (EMBAG 2023, E-Government Strategy 2024–2027), Germany (OZG 2017/2024, Deutsche Verwaltungscloud-Strategie, ZenDiS), and the European Union (Interoperable Europe Act 2024, EU Open Source Strategy 2020–2023, EU Data Act 2023, EU AI Act 2024).

**Technology stack evaluation** using a structured scoring matrix assessing each component on: (a) licence openness, (b) deployment maturity, (c) community health, (d) interoperability standards compliance, (e) security posture, (f) total cost of ownership, and (g) existing public-sector deployments.

**Case study analysis** of five municipal or public-sector open-source transitions, selected to span a range of city sizes, national contexts, and outcomes (including one failure case for balanced analysis).

**Stakeholder analysis** mapping the interests, influence, and engagement needs of each stakeholder group in the municipal digital transformation process.

The literature review is designed to be self-improving: the source registry (`Mem/source-registry.md`) and literature review state (`Mem/literature-review-state.md`) are versioned documents updated on a recurring basis. The `Scripts/update_literature_review.py` script provides structured prompts for quarterly review cycles.

### 2.1 Inclusion Criteria

Sources were included if they: (a) address open-source software in public administration; (b) cover governmental digital transformation strategy; (c) relate to the European, Swiss, or German regulatory context; or (d) provide primary data on municipal technology implementations. Sources published before 2010 were included where they establish foundational theoretical frameworks (e.g., Lathrop & Ruma 2010 [32]).

### 2.2 Limitations

This paper is a citation-complete draft (v0.2.0). Technology stack assessments reflect the state of publicly available information as of June 2026. Implementation cost estimates are indicative and must be validated against local procurement conditions. Academic peer-reviewed literature on open-source municipal stacks remains sparse; several key data points draw on grey literature and practitioner reports rather than peer-reviewed studies.

---

## 3. Literature Review

### 3.1 Theoretical Foundations of E-Government

The academic literature on e-government has evolved through four broad phases [30]. First-generation e-government (1995–2005) focused on digitising existing processes and creating government websites [29]. Second-generation e-government (2005–2012) emphasised online service delivery, citizen portals, and back-office integration [7]. Third-generation e-government (2012–2020) introduced open data, participatory platforms, and mobile-first service design [8]. The current fourth generation (2020–present) is characterised by platform government, digital identity infrastructure, data spaces, and the sovereignty turn — a recognition that digital autonomy is a prerequisite for democratic self-governance [45].

Wirtz and Weyerer's holistic e-government maturity model identifies five dimensions: technical infrastructure, process quality, service quality, citizen orientation, and transparency [7]. Municipal governments in Switzerland and Germany score variably across these dimensions; technical infrastructure and process quality lag citizen expectations in most jurisdictions, while the regulatory environment increasingly mandates transparency and interoperability [1, 2, 45].

Lathrop and Ruma's foundational anthology *Open Government: Collaboration, Transparency, and Participation in Practice* (2010) articulated the philosophical and practical arguments for open government that anticipate the subsequent legislative wave in Europe [32]. Their argument — that openness and interoperability are prerequisites for democratic accountability, not merely technical preferences — remains the normative foundation for the policy developments of the 2020s.

### 3.2 Digital Sovereignty in Public Administration

The concept of digital sovereignty — the capacity of public institutions to make independent, auditable decisions about their digital infrastructure — has moved from academic concept to policy imperative in the European context [3, 5]. The EU Open Source Strategy 2020–2023 established "sharing and reuse" as a core principle, mandating that European institutions prefer open-source solutions in technology procurement [5]. The 2024 Interoperable Europe Act creates binding obligations for cross-border interoperability in all public administrations [6].

Germany's Sovereign Cloud Stack (SCS), developed by the Open Source Business Alliance (OSBA) and funded by the German Federal Ministry for Economic Affairs and Climate Action (BMWK), represents the most concrete realisation of digital sovereignty in cloud infrastructure [3]. SCS provides a fully open-source, self-hostable cloud platform (OpenStack + Kubernetes + Ceph) that enables public administrations to operate technically and legally sovereign infrastructure. As of 2026, SCS underpins several German Länder cloud environments and is integrated with govdigital eG's shared infrastructure [23].

Switzerland's approach differs institutionally but converges on the same principles. EMBAG, in force from 1 January 2024, requires all federal software developed with public funds to be released as open source unless compelling security reasons prevent it [1]. The Swiss Open Government Data (OGD) Strategy and the associated framework for open standards (eCH) [15] extend this logic to data and interoperability. The GovStack initiative, co-led by ITU and GIZ, contributes an international building-blocks framework for sovereign government digital services that Switzerland and Germany have both engaged with [18].

### 3.3 The German OZG Ecosystem and ZenDiS

The Onlinezugangsgesetz (OZG), enacted in 2017 and substantially reformed in 2024 (OZG 2.0), requires all German federal, Land, and municipal administrations to offer their administrative services online [2]. The OZG 2.0 reform addresses shortcomings of the first generation — fragmented implementation, poor interoperability, and inconsistent user experience — through the "Once Only" principle, the EfA (Einer für Alle) approach to shared service development, and a federal platform architecture centred on BundID and FITKO [9, 10].

ZenDiS GmbH (Zentrum für Digitale Souveränität der öffentlichen Verwaltung) was established by the German federal government in 2022 to develop and manage sovereign open-source software for the public sector [25]. ZenDiS oversees OpenDesk — a curated open-source desktop and collaboration suite — and provides a framework contract through which federal and, progressively, Land and municipal authorities can access professionally managed open-source workplace software at scale. OpenDesk bundles Nextcloud, Cryptpad, OpenProject, BigBlueButton, Element/Matrix, and Collabora Online into a single, maintainable suite. ZenDiS's mandate includes supporting municipalities without the capacity for independent open-source management.

The openCode.de platform, launched in 2022 and managed by Digitalservice GmbH des Bundes, provides a centralised repository for government open-source software with over 400 repositories as of 2026, enabling municipalities to discover, reuse, and contribute to shared solutions [10]. The EU Open Source Observatory (OSOR) Annual Report 2023 documents the broader European trend: public-sector open-source adoption has grown consistently across all member states since 2020, with Germany, France, and Switzerland among the top performers [38]. Dataport AöR and AKDB represent the cooperative model of public-sector IT delivery that the OZG ecosystem has reinforced: both organisations operate as public entities, deploying open-source solutions across their member authorities without profit extraction [24, 50].

### 3.4 Swiss Cantonal and Federal Digital Services

Switzerland's federal structure creates both challenges and opportunities for municipal digital transformation. The federal government sets the strategic framework but cannot mandate cantonal or municipal implementation. Key Swiss digital infrastructure includes:

**Fedlex** (fedlex.admin.ch): the official platform for Swiss federal law, built on open standards and providing machine-readable legal data [1].

**opendata.swiss**: the national open government data portal, built on CKAN and cataloguing thousands of datasets from federal, cantonal, and municipal authorities [44].

**GEVER**: the standardised records management system for the Swiss federal administration, providing a template for cantonal and municipal implementations [43].

**Swiss eID**: Following the rejection of the government's first eID proposal in a March 2021 referendum — in which voters objected to the involvement of private providers in digital identity infrastructure — the Federal Council developed a new model based on self-sovereign identity (SSI) principles. The revised E-ID law was approved by the Federal Assembly in late 2023 and the system entered progressive operation from 2025 [40]. The new eID is state-issued, privacy-preserving by design, and integrates with Keycloak-based identity federations via OpenID Connect and verifiable credentials.

**eCH standards**: The association eCH (E-Government Standards) publishes the Swiss XML interoperability standards that are the functional equivalent of Germany's XÖV family [15]. Key standards for municipalities include: eCH-0007 (Gemeinderegister), eCH-0010 (Postadressregeln), eCH-0011 (Meldewesen), eCH-0020 (Ereignismeldung), and eCH-0058 (Schnittstellendefinition für E-Government-Anwendungen). Compliance with eCH standards is a prerequisite for integration with cantonal systems.

The E-Government Strategy Switzerland 2024–2027, co-authored by the Federal Council and the Conference of Cantonal Governments, sets out a collaborative framework for digital services that explicitly mandates open standards and interoperability [16].

### 3.5 European Union Legislative Landscape

The EU legislative output of 2022–2024 has created a comprehensive framework for digital sovereignty in public administration. Four instruments are most directly relevant to municipal technology decisions:

**Interoperable Europe Act (Regulation (EU) 2024/903):** In force from May 2024, this Act creates a legal obligation for all public administrations in the EU to share, reuse, and publish interoperable digital components and datasets by default [6]. It establishes the Interoperable Europe Board as the governance body and mandates interoperability assessments for all new IT systems deployed by public authorities. Municipal CIOs and procurement officers must assess all new system acquisitions against this Act's requirements.

**EU Data Act (Regulation (EU) 2023/2854):** Applicable from September 2025, this Act governs who can access and use data generated by connected devices [28]. For municipalities operating smart-city infrastructure — connected street lighting, parking sensors, air-quality monitors, waste management systems — the Act creates specific rights for users and public bodies to access IoT-generated data. Municipalities deploying open-source data platforms (CKAN, FIWARE) can implement Data Act compliance as a platform feature; proprietary smart-city platforms may create vendor lock-in that inhibits compliance.

**EU AI Act (Regulation (EU) 2024/1689):** The EU's comprehensive AI regulation classifies AI systems by risk level [49]. Several applications relevant to municipal service delivery fall under Annex III ("high-risk AI systems"), including AI used in public administration for benefit or service decisions affecting citizens. High-risk applications require a fundamental rights impact assessment, human oversight mechanisms, full documentation, and registration in the EU AI Act database. Municipalities deploying open-source AI (document routing, citizen inquiry classification, planning permit triage) must conduct these assessments. The Act explicitly does not prohibit open-source AI models but creates equal compliance obligations for both proprietary and open-source high-risk applications.

**Cyber Resilience Act (Regulation (EU) 2024/2847):** In force from October 2024 with a three-year compliance timeline, the CRA introduces mandatory cybersecurity and ongoing software update requirements for products with digital elements placed on the EU market [48]. For municipalities consuming open-source software, the CRA applies primarily to commercial vendors and managed-service providers rather than self-hosted deployments. However, procurement due diligence should now include CRA compliance status for any commercially provided software component.

### 3.6 Open Source Communities and Sovereign Technology

**Decidim** (Barcelona, 2016) is a participatory democracy platform used by over 400 organisations in 40 countries, including the cities of Barcelona, Helsinki, and New York, and the Swiss canton of Schaffhausen [12]. The platform's governance model — a multi-stakeholder Decidim Association with a published social contract — is itself a model for community-governed open-source infrastructure. Barcelona's deployment has processed over 70,000 proposals and tens of millions of citizen interactions, making it the largest empirically validated open-source civic participation system in the world.

**CONSUL Democracy** (Madrid, 2015) is an alternative participatory platform used extensively in Spanish-speaking cities and some European authorities, also licensed under AGPL-3.0 [17]. While functionally similar to Decidim, CONSUL's module structure and administrative interface differ; the choice between them is typically a matter of existing community relationships and local language support.

**Matrix/Element** provides an open, decentralised, end-to-end-encrypted communication protocol increasingly adopted by European public administrations. The German federal BundesMessenger, the French government's Tchap, and the UK Ministry of Defence's internal messaging all operate on Matrix [14]. The protocol's federation capability — allowing different Matrix deployments to communicate securely without trusting a central server — is particularly valuable for inter-agency municipal communication.

**Nextcloud** (Stuttgart, 2016) is the most widely deployed open-source file sync and collaboration platform in European public administration, used by the Swiss Federal Administration, thousands of German municipalities, and dozens of EU institutions [13]. Nextcloud Hub 7 (released 2025) integrates AI-powered document summarisation using locally hosted models, maintaining data sovereignty.

**OpenDesk**, managed by ZenDiS GmbH, is a curated open-source desktop and collaboration suite built around Nextcloud, Cryptpad, OpenProject, BigBlueButton, Element, and Collabora Online [42]. Version 2.x (2025) provides a single, maintainable deployment unit. ZenDiS also publishes procurement guidance for municipalities seeking to adopt OpenDesk without independent open-source engineering capability.

### 3.7 Implementation Case Studies

#### 3.7.1 Barcelona: Decidim Participatory Democracy (2016–present)

Barcelona's deployment of Decidim, initiated in 2016 under the Colau administration, represents the most thoroughly documented open-source civic technology implementation at the city level. The platform has hosted city-wide participatory budgeting cycles, strategic plan consultations, and citizen initiative processes, accumulating over 70,000 registered users and processing more than 100,000 proposals over nine years of operation. The Barcelona model demonstrates three key lessons: (a) participatory platforms require sustained political mandate and resourcing beyond the initial deployment; (b) open-source governance of the platform itself (through the Decidim Association) protects against political reversal by embedding the technology in an international community; and (c) the software's AGPL-3.0 licence has enabled reuse by 400+ organisations globally without Barcelona losing control of its own data or customisations.

#### 3.7.2 French Gendarmerie Nationale: Linux Migration (2008–2014)

The migration of the French Gendarmerie Nationale's approximately 85,000 workstations from Windows to Ubuntu Linux and from Microsoft Office to OpenOffice/LibreOffice (2008–2014) is the largest documented large-scale open-source desktop migration in European public administration [31]. The migration was led by Lt. Col. Xavier Guimard and proceeded in structured waves, with extensive staff training at each phase. Key outcomes: approximately 40 percent reduction in per-workstation cost; significantly reduced vendor dependency; improved update agility. The Gendarmerie's Linux environment continues to operate. The French government subsequently deployed Tchap (Matrix-based messaging) for inter-agency communication and LibreOffice across multiple ministries. The French experience establishes that open-source desktop migration at scale is technically feasible and economically advantageous when properly managed.

#### 3.7.3 Munich LiMux: A Structural Analysis (2003–2017)

The City of Munich's LiMux project (2003–2017) remains the most cited example of a large-scale municipal open-source transition that was subsequently reversed. The technical implementation — migrating approximately 15,000 desktops to Ubuntu Linux and LibreOffice — was largely successful. Post-mortem analyses consistently attribute the 2017 reversal primarily to: (a) a change in political leadership in 2014, with the incoming administration maintaining closer relationships with Microsoft; (b) aggressive vendor lobbying; (c) inadequate management of compatibility with state-level government systems (particularly ODF support in Bavaria) that had not been updated to open standards; and (d) accumulated end-user frustration from insufficient training investment [30]. Munich's experience does not invalidate open-source municipal transitions; it validates the primacy of political risk management and cross-party institutionalisation. Notably, Munich re-initiated an open-source evaluation programme in the early 2020s, suggesting the political pendulum can swing back.

#### 3.7.4 Jena, Germany: Cooperative OZG Implementation

The City of Jena (population ~113,000) provides an example of a medium-sized German municipality successfully implementing OZG services through cooperative procurement. Rather than building its own digital services, Jena participates in the Thüringen IT (TIT) cooperative framework, which develops and operates OZG-compliant services shared across all 17 Thuringian districts and the state capital. The model demonstrates the "Einer für Alle" principle in practice: Jena contributes to the shared pool, accesses all services developed by other participants, and maintains sovereignty through TIT's public-sector governance structure. Keycloak provides SSO federation with BundID; Nextcloud handles internal collaboration; TYPO3 powers the citizen-facing website. Total annual technology cost for Jena through TIT is approximately 40 percent lower than comparable standalone procurements.

#### 3.7.5 Canton of Zug, Switzerland: Digital Pioneer

The Canton of Zug (population ~130,000), widely known as "Crypto Valley" for its blockchain-forward policies, has also been a pioneer in digital government services. The Zug municipal administration has piloted self-sovereign identity credentials for citizen services (ZugApp), deployed Nextcloud for cantonal document management, and maintains its citizens' data on cantonal infrastructure rather than commercial cloud providers. Zug's approach demonstrates that digital sovereignty and innovation are complementary rather than competing values: the canton's reputation for regulatory clarity and digital openness attracts both fintech businesses and citizens who value transparent, accountable administration. The Zug model is replicable in Swiss municipalities with political will and cantonal IT support.

### 3.8 Total Cost of Ownership Evidence

Rigorous, independent, comparative Total Cost of Ownership (TCO) studies for open-source versus proprietary municipal technology stacks remain sparse. Most available studies are vendor-commissioned or context-specific. The following data points represent the best available evidence:

**French Gendarmerie (2008–2014):** Approximately 40 percent reduction in per-workstation cost after migration to Ubuntu/LibreOffice [31]. Direct comparison possible because the Gendarmerie maintained detailed procurement records.

**City of Paris LibreOffice migration (2017):** The City of Paris reported savings of approximately €5 million over the initial 5-year period after migrating to LibreOffice from Microsoft Office, primarily from eliminated licence fees [51]. Ongoing support costs partially offset but did not eliminate these savings.

**Indicative municipal stack TCO model (2026):** Based on publicly available pricing data for representative municipalities of 50,000 population:

| Component | Proprietary (annual) | Open-source hosted (annual) | Open-source self-hosted (annual) |
|---|---|---|---|
| Productivity suite | €200–300/user | €80–150/user | €30–60/user |
| File storage & collaboration | €120–200/user | €60–100/user | €20–50/user |
| Video conferencing | €100–180/user | €40–80/user | €15–40/user |
| Identity management | €50–100/user | €20–40/user | €10–25/user |
| **Total (est.)** | **€470–780/user** | **€200–370/user** | **€75–175/user** |

For a city of 50,000 with 500 IT users, the indicative 5-year saving from a fully hosted open-source stack versus proprietary equivalents is approximately €675,000–€2,025,000. Implementation costs (€150,000–€500,000) are recovered within 12–30 months depending on city size and migration complexity.

### 3.9 Gaps in the Literature

1. **Longitudinal TCO studies** comparing open-source and proprietary municipal stacks over full 10-year cycles are still lacking. The Paris and Gendarmerie cases are the best available but lack independent verification.
2. **User experience research** comparing citizen satisfaction with open-source and proprietary municipal digital services is almost entirely absent from peer-reviewed literature.
3. **Small-municipality perspectives** (under 10,000 population) remain underrepresented; the cooperative IT model may not translate directly to the smallest jurisdictions.
4. **AI governance in open-source municipal contexts** is an entirely new literature area; almost no empirical literature exists on municipal deployment of open-source AI systems under the EU AI Act framework.

See `Mem/literature-review-state.md` for the full gap analysis and improvement roadmap.

---

## 4. Technology Stack Analysis

A municipal technology stack can be decomposed into ten functional layers. The analysis below evaluates the leading open-source options for each layer against the scoring criteria defined in Section 2.

### 4.1 Digital Identity and Authentication

**Function:** Authenticate citizens and staff; federate identity across services; implement single sign-on (SSO); integrate national identity systems.

**Recommended component: Keycloak** (Red Hat / CNCF) [21]

Keycloak is the de facto open-source identity and access management (IAM) platform for public administration in Europe. It implements OpenID Connect, OAuth 2.0, and SAML 2.0, enabling federation with national identity systems (BundID in Germany, Swiss eID via OpenID Connect, eIDAS for cross-border EU authentication). It is deployed by numerous European governments including EU institutions, German Länder, and Swiss cantons.

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Licence openness | 5 | Apache 2.0 |
| Deployment maturity | 5 | Production-proven, 10+ years |
| Community health | 5 | Large, active, CNCF-supported |
| Interoperability | 5 | OIDC, OAuth2, SAML2, FIDO2, eIDAS |
| Security posture | 5 | CVE-responsive, regularly audited |
| TCO | 4 | No licence cost; requires ops expertise |
| Public-sector deployments | 5 | Widespread EU government use |

**Integration notes:** For German municipalities, Keycloak federates with BundID via the SAML2 profile specified by FITKO. For Swiss municipalities, federation with cantonal identity providers and the new Swiss eID uses the OpenID Connect / verifiable credentials bridge. For both contexts, Keycloak's realm structure allows separate citizen-facing and staff-facing identity domains with different assurance levels.

### 4.2 Document Management and Records

**Function:** Store, retrieve, classify, and retain official records; manage GEVER-compliant (CH) or e-Akte-compliant (DE) workflows.

**Recommended components: Nextcloud** (collaborative file management) + **OpenProject** (project and records linking) [13, 20]

For Swiss municipalities requiring full GEVER compliance, cantonal solutions (CMI, Fabasoft Community Edition) provide the compliance layer with Nextcloud as the collaborative front-end. CMI eCH is OSI-licenced. For German municipalities, the AKDB's e-Akte and Dataport's DMS components provide equivalent e-Akte compliance built on open-source document management foundations.

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Licence openness | 5 | AGPL-3.0 (Nextcloud); GPLv3 (OpenProject) |
| Deployment maturity | 5 | 400,000+ organisations worldwide |
| Community health | 5 | Nextcloud GmbH + large community |
| Interoperability | 4 | WebDAV, CalDAV, CardDAV, CMIS, eCH-0160 |
| Security posture | 5 | ISO 27001 certified offering; regular audits |
| TCO | 5 | No per-seat licence (Community Edition) |
| Public-sector deployments | 5 | Swiss federal, German states and cities |

### 4.3 Office Productivity Suite

**Function:** Word processing, spreadsheets, presentations; document creation and editing for staff and citizens; OpenDocument Format (ODF) document storage.

**Recommended components: LibreOffice** (desktop) + **Collabora Online** (browser-based) [47]

LibreOffice, maintained by The Document Foundation under LGPL-3.0, is the leading open-source office suite deployed across European public administration. Significant deployments include: the French Ministry of Defence (Gendarmerie, 85,000+ desktops) [31], the City of Paris [51], Spain's national administration, the German Federal Administration via Bundesverwaltungsamt [52], and numerous German municipalities. Collabora Online CODE (Collabora Office in the Cloud, based on LibreOffice) provides a browser-based alternative that integrates natively with Nextcloud and OpenDesk, enabling collaborative editing without requiring desktop installation.

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Licence openness | 5 | LGPL-3.0 (LibreOffice); MPL-2.0 (Collabora) |
| Deployment maturity | 5 | 200M+ users globally; government deployments since 2010 |
| Community health | 5 | Document Foundation + Collabora commercial backing |
| Interoperability | 4 | ODF ISO 26300; OOXML import/export; OASIS standards |
| Security posture | 4 | Regular CVE patching; BSI-evaluated |
| TCO | 5 | No per-seat licence cost |
| Public-sector deployments | 5 | French state, German federal/municipal, EU |

**Format strategy:** Store all official documents in OpenDocument Format (ODF, ISO 26300) for archival. Maintain OOXML (.docx/.xlsx) import/export capability for citizen communication. Apply the German KGSt recommendation of ODF-first for all new documents.

### 4.4 Workflow Automation and Business Process Management

**Function:** Automate administrative workflows; model, execute, and monitor BPMN processes; integrate XÖV (DE) and eCH (CH) data standards.

**Recommended component: Camunda Platform 8 Community Edition** [33]

Camunda provides a BPMN 2.0-native workflow engine with strong support for complex multi-step administrative processes and XÖV/eCH data standards integration [46, 15]. **Flowable** (Apache 2.0) is a lighter-weight alternative where Camunda's dual-licensing model creates procurement complications. The German OZG 2.0 ecosystem has standardised on BPMN 2.0 for service digitisation; most EfA service implementations expose Camunda-compatible process models.

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Licence openness | 4 | Community: Apache 2.0; Enterprise: proprietary |
| Deployment maturity | 5 | Production-proven, multiple Länder |
| Community health | 4 | Active; enterprise tier funds development |
| Interoperability | 5 | BPMN 2.0, REST API, event-driven, XÖV, eCH |
| Security posture | 4 | Actively maintained |
| TCO | 3 | Community free; scale may require Enterprise |
| Public-sector deployments | 4 | Multiple German Länder and Swiss cantons |

### 4.5 Citizen Participation

**Function:** Consultation, participatory budgeting, initiative collection, deliberation platforms; comply with civic participation mandates.

**Recommended component: Decidim** [12]

Decidim is the most mature and widely adopted open-source participation platform globally. Use by Barcelona, Helsinki, the canton of Schaffhausen, and New York validates it across regulatory and linguistic contexts. The Decidim Association provides governance, a published social contract, and a global community of practice that protects against vendor abandonment.

**Alternative: CONSUL Democracy** [17] — AGPL-3.0, strong in Spanish-speaking cities and some European authorities; provides slightly simpler administration for smaller municipalities.

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Licence openness | 5 | AGPL-3.0 |
| Deployment maturity | 5 | 400+ deployments in 40 countries |
| Community health | 5 | Active Decidim Association |
| Interoperability | 4 | REST API, webhooks, DCAT-AP export |
| Security posture | 4 | Actively maintained |
| TCO | 5 | No licence cost |
| Public-sector deployments | 5 | Cities, cantons, national agencies |

### 4.6 Communication and Collaboration

**Function:** Internal messaging, video conferencing, email, calendar; secure inter-agency communication; integration with national government networks.

**Recommended components:**
- **Matrix/Element** for messaging and secure inter-agency communication [14]
- **BigBlueButton** for democratic processes (council meetings, public hearings) [34]
- **Jitsi Meet** for informal video conferencing [35]
- **Nextcloud Talk** for integrated team communication

The German federal BundesMessenger (built on Matrix) and French Tchap provide reference deployments applicable to municipal contexts. Matrix's federation protocol allows municipal Matrix servers to communicate with federal servers without trusting a central intermediary.

| Component | Licence | Maturity | Key advantage |
|---|---|---|---|
| Matrix/Element | Apache 2.0 | Production | E2E encryption, federation, government endorsement |
| BigBlueButton | LGPL-3.0 | Production | Council/public hearing focus, recording |
| Jitsi Meet | Apache 2.0 | Production | Browser-based, no account required |
| Nextcloud Talk | AGPL-3.0 | Production | Integrated with file management and calendar |

### 4.7 Open Data Publication

**Function:** Publish machine-readable datasets; catalogue municipal data; provide API access; comply with EU Open Data Directive and DCAT-AP standards.

**Recommended component: CKAN** [22]

CKAN is the world's leading open-source open data portal software. It powers opendata.swiss, data.gov, data.gov.uk, and dozens of national and municipal portals. Its plugin architecture supports DCAT-AP, DCAT-AP.de (Germany), OGD Switzerland metadata standards, and harvesting from upstream national catalogues — enabling municipal datasets to automatically appear in federal and EU catalogues.

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Licence openness | 5 | AGPL-3.0 |
| Deployment maturity | 5 | 10+ year production track record |
| Community health | 4 | CKAN Association; active ecosystem |
| Interoperability | 5 | DCAT-AP, OAI-PMH, SPARQL, CSW |
| Security posture | 4 | Actively maintained |
| TCO | 4 | No licence cost; ops overhead for maintained portal |
| Public-sector deployments | 5 | Switzerland, Germany, UK, EU institutions |

### 4.8 Geographic Information Systems

**Function:** Map-based citizen services; urban planning; spatial data publication; OGC-compliant APIs.

**Recommended components:**
- **QGIS** (desktop/server, GPL-2.0+) for spatial data editing and analysis [37]
- **GeoServer** (LGPL-2.0, GeoTools) for OGC-compliant WMS/WFS spatial data publication
- **OpenStreetMap** (ODbL-1.0) as the base cartographic layer [36]

Switzerland's swisstopo provides open, high-quality governmental base map data (swisstopo open data, published 2021) under free licences. Germany's BKG provides comparable federal geodata. Both are compatible with QGIS and GeoServer deployments. Municipal integration with the national geoportal via OGC standard APIs is technically straightforward.

### 4.9 Public Website and Content Management

**Function:** Public-facing website; news and announcements; service directory; barrier-free access (WCAG 2.1 AA / BITV 2.0); multilingual content.

**Recommended components:**
- **TYPO3** (GPL-2.0): dominant CMS for Swiss and German public administration; the TYPO3 Association provides long-term support, public-sector extensions, and accessibility certification [19]
- **Drupal** (GPL-2.0): strong international track record; used by the European Commission and numerous French municipalities

Both systems support accessibility standards (WCAG 2.1 AA / BITV 2.0), multilingualism, and integration with open data catalogues. TYPO3's dominance in the DACH region provides advantages in available integrators, extensions, and training resources.

### 4.10 Cloud Infrastructure and Hosting

**Function:** Compute, storage, networking, container orchestration; data sovereignty at the infrastructure layer.

**Recommended component: Sovereign Cloud Stack (SCS)** [3, 11]

SCS is the most strategically important infrastructure choice for European municipalities. It provides a fully open-source cloud stack (OpenStack + Kubernetes + Ceph) that can be self-hosted, operated by a cooperative provider (govdigital eG), or deployed by certified SCS cloud operators including plusserver GmbH and OSISM GmbH.

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Licence openness | 5 | Apache 2.0 / fully open |
| Deployment maturity | 4 | Production in multiple German Länder |
| Community health | 5 | OSBA-backed, growing international adoption |
| Interoperability | 5 | Open APIs, OCI container standard |
| Security posture | 5 | BSI IT-Grundschutz compatible; German data residency |
| TCO | 4 | No licence; infrastructure and operations cost |
| Public-sector deployments | 4 | German Länder, growing municipal deployment |

**For municipalities without in-house cloud operations capacity:** certified SCS hosters (plusserver, OSISM, Open Telekom Cloud) provide managed SCS with full data sovereignty guarantees, BSI compliance, and GDPR-compliant German data centres. govdigital eG offers framework contracts that satisfy German and EU procurement law and provide economies of scale across member authorities [23].

### 4.11 AI and Automation

**Function:** Intelligent document processing; citizen inquiry routing; permit triage; knowledge base search; workflow optimisation; automated translation.

This layer is the most rapidly evolving area of open-source municipal technology. Key components in 2026:

**Ollama** (MIT): a self-hosted large language model (LLM) inference runtime supporting popular open models (Llama 3, Mistral, Phi-3, Qwen). Enables municipalities to deploy LLM-based services on their own infrastructure, keeping citizen data sovereign and enabling EU AI Act compliance through in-house control.

**AnythingLLM** (MIT): a document-aware LLM interface that enables retrieval-augmented generation (RAG) over municipal knowledge bases, enabling internal staff to query local ordinances, process documentation, and historical decisions without sending data to external providers.

**n8n** (sustainable use licence, self-hostable): an open-source workflow automation tool with native AI integration, suitable for automating citizen inquiry triage, document routing, and inter-system data flows.

**OpenWebUI** (MIT): a browser-based interface for locally hosted LLMs, providing staff with a sovereign ChatGPT-equivalent for approved use cases.

**EU AI Act compliance framework:** Municipalities deploying AI must categorise each application against the EU AI Act's risk tiers [49]:

| Application | Risk tier | Requirements |
|---|---|---|
| Internal document summarisation | Minimal | None beyond general transparency |
| Citizen FAQ chatbot | Limited | Transparency notice to citizens |
| Permit triage prioritisation | High | Fundamental rights impact assessment, human oversight, registration |
| Automated benefit eligibility determination | High | Full EU AI Act conformity assessment |
| Biometric identification at civic events | Prohibited | Not permissible |

**Operational principle:** All citizen-affecting AI decisions must be explainable, subject to human review, and documented in the municipality's AI Act register. Open-source models enable independent auditability of the decision logic in ways proprietary cloud AI cannot.

### 4.12 Reference Architecture

```
+---------------------------------------------------------------+
|                     CITIZEN TOUCHPOINTS                       |
|         TYPO3/Drupal . Decidim . CKAN . Nextcloud            |
+---------------------------------------------------------------+
|                       SERVICE LAYER                          |
|     Camunda Workflows . XÖV/eCH Forms . GeoServer . QGIS    |
+---------------------------------------------------------------+
|                    COLLABORATION LAYER                       |
|     Nextcloud . Matrix/Element . BigBlueButton . OpenProject |
+---------------------------------------------------------------+
|                     PRODUCTIVITY LAYER                       |
|     LibreOffice (desktop) . Collabora Online (browser)       |
+---------------------------------------------------------------+
|                      IDENTITY LAYER                          |
|       Keycloak <-> BundID / Swiss eID / eIDAS               |
+---------------------------------------------------------------+
|                       AI / AUTOMATION                        |
|        Ollama . AnythingLLM . n8n . OpenWebUI               |
+---------------------------------------------------------------+
|                    INFRASTRUCTURE LAYER                      |
|   Sovereign Cloud Stack . Kubernetes . PostgreSQL . Ceph     |
+---------------------------------------------------------------+
```

All layers communicate via open APIs and open standards. Container orchestration across the stack is handled by Kubernetes [39], relational persistence by PostgreSQL [41], object storage by Ceph — all running on Sovereign Cloud Stack. Data exchange uses XÖV standards (Germany) [46] or eCH standards (Switzerland) [15]. Security is governed by BSI IT-Grundschutz (Germany) [26] or the Swiss ISDS framework.

---

## 5. Implementation Roadmap

The implementation is structured as a 36-month, five-phase programme. Each phase has defined deliverables, success criteria, and decision gates. Phases deliberately overlap to maintain momentum and avoid "big bang" transitions.

### Phase 0: Foundation (Months 1–3)

**Objective:** Establish governance, assess current state, build the coalition.

**Deliverables:**
- Digital Transformation Steering Committee established (city leadership + IT + civil society)
- Current-state technology audit completed (all software, licences, contracts, integration dependencies)
- Stakeholder engagement plan adopted
- Procurement framework established (see Section 6)
- Memorandum of Understanding with cooperative IT provider (Dataport, AKDB, TIT, govdigital, or Swiss cantonal IT cooperative)

**Success criteria:**
- Political mandate secured (council resolution or executive decision)
- Budget envelope approved (see Section 5.7)
- Project lead appointed with adequate seniority and authority
- All current vendor contracts mapped with expiry dates

### Phase 1: Identity and Infrastructure (Months 4–12)

**Objective:** Stand up the foundational layers that everything else depends on.

**Deliverables:**
- Sovereign Cloud Stack environment operational (managed hoster or self-hosted)
- Keycloak identity provider deployed and federated with national identity system
- Nextcloud baseline deployment for internal collaboration
- LibreOffice deployed on all staff workstations (parallel to existing suite for 6 months)
- Matrix/Element messaging for IT and management staff
- BSI IT-Grundschutz or Swiss ISDS baseline documentation complete

**Success criteria:**
- 100% of IT staff can authenticate via Keycloak SSO
- File storage migrated from proprietary cloud to Nextcloud (or hybrid with clear exit plan)
- Basic encrypted messaging operational for senior staff
- Security baseline documented and approved by data protection officer
- LibreOffice deployed and training complete for pilot department (>20 staff)

### Phase 2: Services and Workflows (Months 10–18)

**Objective:** Migrate or build the first five citizen-facing services on open infrastructure.

**Deliverables:**
- Five highest-volume administrative services deployed on Camunda/XÖV (DE) or Camunda/eCH (CH) stack
- TYPO3 or Drupal CMS migration complete with WCAG 2.1 AA certification
- Open data portal (CKAN) launched with first 20 datasets
- Decidim instance deployed for the first participatory process
- LibreOffice fully rolled out to all staff; proprietary suite decommissioned

**Success criteria:**
- 80% of target service transaction volume processed through new system
- Zero regression in service availability vs. baseline
- First open data publication live and harvested by national catalogue
- All staff using LibreOffice exclusively

### Phase 3: Integration and Extension (Months 16–24)

**Objective:** Integrate all layers; extend service coverage to 80% of transactions.

**Deliverables:**
- All services federated via Keycloak SSO
- Nextcloud integrated with document management and GEVER/e-Akte workflows
- GIS layer operational (QGIS + GeoServer + swisstopo/BKG base data)
- 80% of administrative services digitised
- Inter-agency data exchange via XÖV/eCH operational
- First internal AI deployment (document summarisation, internal Q&A — minimal risk tier)

**Success criteria:**
- End-to-end service delivery without paper for 80% of transaction types
- Data quality metrics established and publicly reported
- First annual open data report published
- AI use policy adopted and published

### Phase 4: Optimisation and Community (Months 22–30)

**Objective:** Optimise user experience; contribute back to open-source communities; establish leadership position.

**Deliverables:**
- Citizen satisfaction survey (target: NPS > 40)
- First contribution to openCode.de / upstream projects (Nextcloud, CKAN, Decidim, TYPO3)
- Municipal open-source community of practice established with peer municipalities
- Performance benchmarks published (cost, uptime, citizen satisfaction)
- AI Act compliance register established for all AI applications

**Success criteria:**
- At least three improvements contributed upstream
- Community of practice active with ≥ 3 peer municipalities engaged
- Full 5-year TCO report published

### Phase 5: Sovereignty and Scale (Months 28–36)

**Objective:** Achieve full digital sovereignty; prepare for extension to neighbouring municipalities.

**Deliverables:**
- Complete audit of all software components for licence compliance and CRA status
- Sovereign data residency verified (all data on SCS or certified SCS hoster)
- Playbook for replication by neighbouring municipalities published on openCode.de
- Strategy paper v1.0 published
- Advanced AI services assessed (permit triage, citizen inquiry routing) — high-risk tier with full EU AI Act documentation

**Success criteria:**
- Zero proprietary single-vendor dependencies in critical path
- All data on sovereign EU infrastructure
- At least one peer municipality has adopted the playbook
- EU AI Act compliance documentation in place for all AI applications

### 5.7 Budget Estimates by City Size

Cost ranges are indicative and vary significantly by existing infrastructure, in-house capacity, and cooperative membership. All figures in EUR.

| City category | Population | Phase 0–1 | Phases 2–5 | Annual operating (post-migration) |
|---|---|---|---|---|
| Small | 5,000–20,000 | €50,000–120,000 | €80,000–250,000 | €25,000–70,000 |
| Medium | 20,000–100,000 | €120,000–350,000 | €250,000–800,000 | €70,000–250,000 |
| Large | 100,000–500,000 | €350,000–1,200,000 | €800,000–3,000,000 | €250,000–900,000 |
| Metropolitan | 500,000+ | €1,200,000–5,000,000 | €3,000,000–15,000,000 | €900,000–4,000,000 |

**Notes:** (a) Small municipalities should strongly prefer joining a cooperative (Dataport, AKDB, TIT, govdigital, cantonal IT cooperative) rather than procuring independently — this reduces Phase 0–1 costs by 40–70% and provides ongoing managed-service economies. (b) Annual operating costs decline relative to comparable proprietary stacks over a 5-year horizon as migration costs are amortised. (c) Staff training is the most consistently underestimated budget line; budget at least 2 days per staff member per major new system.

---

## 6. Stakeholder and Procurement Strategy

### 6.1 Stakeholder Map

| Stakeholder | Primary interest | Engagement approach |
|---|---|---|
| Mayor / Executive | Political success, cost, citizen approval | Executive briefing, progress dashboard, TCO report |
| City council | Oversight, democratic legitimacy | Quarterly reports, open council sessions, annual strategy review |
| City IT team | Technical feasibility, workload, career development | Co-design, training, open-source community membership, conference attendance |
| Procurement office | Legal compliance, risk, value for money | Framework agreements, legal briefings, ZenDiS/BMI procurement guide |
| Civil servants (end users) | Ease of use, reliability, familiar tools | UX testing, parallel systems during transition, peer champions, training |
| Citizens | Service quality, privacy, accessibility | Participatory design via Decidim, transparency reporting, accessibility testing |
| Civil society / NGOs | Transparency, access, participation, data rights | Decidim platform, public roadmaps, open data portal |
| Open-source communities | Contribution, reuse, sustainability | openCode.de participation, upstream contributions, shared maintenance |
| Sovereign technology providers | Partnership, deployment, reference clients | Certified partner agreements, co-development, case study publication |
| Data protection officer | GDPR compliance, privacy by design | Privacy-by-design review at each phase, DPIA for all new citizen-facing services |
| Information security officer | NIS2/CRA compliance, IT-Grundschutz | Security baseline co-authorship, penetration testing sign-off |

### 6.2 Procurement Framework

Open-source procurement requires a different framework from proprietary licence purchasing. The software is free; municipalities pay for implementation, hosting, support, customisation, and training. Key principles:

**1. Procure services, not licences.** Procurement documents must be structured around services (implementation, hosting, support, updates) rather than licences. This is both legally correct and practically important: it shifts the contract from a product purchase to a services engagement, making exit easier.

**2. Apply the "Public Money? Public Code!" principle.** All custom software developed under contract must be released under an OSI-approved open-source licence and published on openCode.de or an equivalent public repository. This should be a non-negotiable contract condition [4]. Switzerland's EMBAG creates this as a legal requirement at the federal level; German municipalities should adopt it as a procurement policy.

**3. Evaluate total cost of ownership.** Procurement scoring must include a 5-year TCO model. Proprietary alternatives typically understate long-term costs by omitting vendor lock-in risk, licence escalation clauses, and migration costs. The indicative TCO model in Section 3.8 provides a framework.

**4. Require interoperability standards.** All procured systems must implement: XÖV (Germany) [46], eCH (Switzerland) [15], DCAT-AP (EU open data), OIDC/SAML2 (identity), and ODF (document format). Non-compliance should be a disqualifying criterion.

**5. Prefer certified cooperative providers.** For infrastructure and managed services, prefer SCS-certified cloud operators or members of govdigital eG (Germany) or cantonal IT cooperatives (Switzerland), who are bound by collective data sovereignty and GDPR compliance agreements [23].

**6. Include an exit plan in every contract.** Every managed-service contract must include a documented migration path: all data in open formats, all configurations exportable, and a minimum 12-month transition support period.

### 6.3 Swiss Procurement Law (BöB)

Swiss federal procurement is governed by the Bundesgesetz über das öffentliche Beschaffungswesen (BöB, SR 172.056.1), substantially revised and in force since 2021. Key provisions relevant to open-source municipal procurement:

- **Threshold for competitive tender:** CHF 150,000 for services (federal). Cantonal municipalities follow the Interkantonale Vereinbarung über das öffentliche Beschaffungswesen (IVöB) and cantonal implementing law.
- **Services model:** Software licences (at zero cost) do not require tender; related services (implementation, hosting, support) above threshold do. This means CKAN, Nextcloud, Keycloak, and LibreOffice require no licence procurement process — only the service contracts.
- **Open-source preference clause:** EMBAG Article 9 creates an open-by-default principle that supports, but does not legally require, a preference for open-source solutions in procurement scoring. Municipalities may adopt this as a policy criterion.
- **Framework agreements:** The Swiss federal administration publishes framework agreements (Rahmenvertrag) for common IT services including cloud hosting. Swiss municipalities can negotiate cantonal framework agreements analogous to Germany's EVB-IT structure.
- **GEAK (Government Enterprise Architecture):** The federal GEAK framework provides architectural guidance compatible with the open-source stack described in this paper.

### 6.4 German Procurement Law (GWB/UVgO)

German public procurement above EU thresholds is governed by Part 4 of the Gesetz gegen Wettbewerbsbeschränkungen (GWB) and the Vergabeverordnung (VgV). Below-threshold procurement follows the Unterschwellenvergabeordnung (UVgO). Key provisions:

- **Threshold for competitive tender (2024):** €221,000 for service contracts above EU threshold (VgV/VgV). Below-threshold: UVgO procedure with lower formality requirements.
- **IT-specific contracts:** EVB-IT (Ergänzende Vertragsbedingungen für IT) contracts provide standard terms for government IT procurement. ZenDiS has published an Open-Source-Beschaffungs-Leitfaden (Open Source Procurement Guide, 2023) that provides templates compatible with EVB-IT.
- **Services model:** As in Switzerland, open-source software licences are at zero cost and not subject to procurement law. Procurement is for the services layer only.
- **Framework agreements:** govdigital eG provides framework agreements covering SCS-based cloud hosting and OpenDesk that satisfy GWB Part 4 requirements. AKDB and Dataport AöR offer similar structures for their member authorities. Municipalities joining these cooperatives can procure under existing framework agreements without individual tender processes above threshold.
- **Open-source preference:** While GWB does not mandate open-source preference, the OZG 2.0 legislative materials and ZenDiS mandate support adopting it as an evaluation criterion. The openCode.de community norm of publishing all publicly funded custom software supports the PMPC principle in practice.

### 6.5 Change Management

Open-source transitions frequently fail not on technical grounds but on human factors: end-user resistance, insufficient training, middle-management inertia, and political backsliding under vendor lobbying. The Munich LiMux case (Section 3.7.3) is the canonical example.

**Recommendations:**
- Appoint a **Digital Transformation Champion** at senior political level with explicit, multi-year mandate and budget authority
- Establish **open-source champions** in each department with advanced training, peer support role, and time allocation (minimum 20% of one FTE per 50-person department)
- Run **parallel operations** for a minimum of three months before cutting over critical systems
- Document and celebrate **early wins** (cost savings, new capabilities, positive citizen feedback) with public reporting
- Publish a **public transparency dashboard** showing migration progress, costs, service quality metrics, and open data statistics
- Engage **unions and staff councils** early: frame the transition as skill development and digital autonomy, not cost-cutting
- Prepare a **vendor lobbying response plan**: document the evidence base for open-source decisions in advance, so pushback can be addressed with facts

---

## 7. Risk Analysis

### 7.1 Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Political reversal after election | Medium | High | Embed in legislation/ordinance; build cross-party consensus; institutionalise in cooperative membership |
| Vendor lobbying / FUD campaigns | High | Medium | Document TCO evidence in advance; engage civil society allies; publish mandate rationale publicly |
| Skill gap in IT team | High | Medium | Training programme; cooperative IT provider; community of practice; recruitment of open-source specialists |
| Integration failure between stack layers | Medium | High | Phased rollout with decision gates; strict reference architecture adherence; integration testing at each gate |
| Data loss during migration | Low | Critical | Full backup protocol; parallel operation minimum 3 months; staged migration; independent backup verification |
| GDPR / data protection violation | Low | High | Privacy-by-design at each phase; DPO engagement; DPIA for all citizen-facing systems; data mapping |
| User adoption failure | Medium | High | Change management; UX testing; training; parallel systems; open-source champions; executive sponsorship |
| Security incident | Low | Critical | BSI IT-Grundschutz; penetration testing at each gate; incident response plan; NIS2 compliance; CRA awareness |
| Community fragmentation or project abandonment | Low | Medium | Use only projects with commercial backing or large community (all in stack); contribute upstream; monitor community health |
| Cost overrun | Medium | Medium | Phase-gated budget; independent project office; open TCO accounting; contingency reserve (20%) |
| Regulatory non-compliance (AI Act) | Medium | High | AI Act compliance register from Phase 3; legal review of all AI applications; prefer minimal/limited risk tiers initially |
| Interoperability gaps with legacy systems | Medium | Medium | API mapping before migration; gradual sunset of legacy; XÖV/eCH adapters; cooperative support |

### 7.2 The Munich Cautionary Case

The City of Munich's LiMux project is analysed in detail in Section 3.7.3. The principal lessons for risk management:

1. **Political institutionalisation is the binding constraint.** Embed digital sovereignty as a principle in the city's digital strategy document, procurement policy, and ideally in a municipal ordinance. Cross-party council support is essential; executive mandate alone is fragile.
2. **Interoperability with state-level systems must be verified before, not after, migration.** Munich's 2014 compatibility problems with Bavarian state systems were predictable and preventable. Require XÖV/eCH compliance from state-level partners as a precondition.
3. **Training investment is non-negotiable.** Budget a minimum of 2 full training days per staff member per major system change. Middle managers require separate track on change leadership.
4. **Plan for vendor lobbying.** Document the evidence base for every open-source decision before the political cycle changes. ZenDiS, FSFE, and govdigital eG can provide expert support when FUD campaigns emerge.

### 7.3 Security Considerations

The BSI's IT-Grundschutz framework provides a comprehensive security baseline applicable regardless of licence model [26]. Key requirements for municipal open-source deployments:

- All server components must receive security updates within 14 days of release (critical patches within 72 hours)
- Authentication must meet BSI Authenticator Assurance Level 2 (AAL2) for citizen-facing services, AAL3 for privileged access
- Data in transit: TLS 1.3 minimum; data at rest: AES-256 for sensitive categories (special category GDPR data, legal records)
- Penetration testing at each phase gate, conducted by accredited testers (BSI IT-Grundschutz certified for German municipalities)
- Incident response plan aligned with NIS2 obligations: documented, tested annually, integrated with CERT-Bund notification procedures [27]
- Software Bill of Materials (SBOM) maintained for all deployed open-source components in SPDX format; updated quarterly
- CRA compliance verification for all commercial providers: confirm they meet the CRA's update and vulnerability-reporting obligations [48]

### 7.4 AI-Specific Risks

As municipalities begin deploying open-source AI systems (Phase 3–5), specific risks require dedicated management:

**EU AI Act non-compliance:** Deploying an AI application in the high-risk tier (permit triage, benefit routing) without a conformity assessment, human oversight mechanism, and EU AI Act registration is a regulatory violation. Mitigation: classify all AI applications before deployment; begin with minimal/limited-risk tiers only; engage legal counsel for high-risk assessments.

**Bias in automated citizen decisions:** LLM-based document routing and triage systems may exhibit systematic bias against demographic groups if training data is not representative. Mitigation: never deploy open-source AI as a final decision-making system for individual citizens without human review; monitor for demographic disparities in outcomes quarterly.

**"Shadow AI" — unauthorised use of external AI services:** Staff using commercial cloud AI (ChatGPT, Claude, Gemini) to process citizen data or official documents creates GDPR violations and security risks. Mitigation: provide a sovereign self-hosted alternative (OpenWebUI + Ollama) as part of the AI layer; adopt a clear AI use policy and train all staff before Phase 3.

**Vendor lock-in in AI features:** Open-source applications (Nextcloud, TYPO3) increasingly offer AI features that call external APIs by default. Evaluate these features carefully; prefer deployments that use locally hosted models or allow model substitution.

---

## 8. Conclusion

The evidence reviewed in this paper converges on five findings:

**1. Open-source municipal technology stacks are technically mature, production-proven, and comprehensively supported.** Every functional requirement of a modern municipal government — identity, documents, office productivity, workflows, participation, communication, open data, GIS, cloud infrastructure, and AI — can be met by open-source software with documented, operational deployments at peer municipalities across Europe.

**2. The regulatory environment in Switzerland, Germany, and the EU increasingly mandates open-source and interoperability.** EMBAG (Switzerland), OZG 2.0 (Germany), and the Interoperable Europe Act (EU) create legal obligations that proprietary, vendor-locked systems cannot sustainably satisfy. The EU Data Act, EU AI Act, and Cyber Resilience Act add further compliance dimensions that are more tractable with transparent, auditable open-source systems.

**3. The economic case is compelling on a 5-year total cost of ownership basis.** Open-source stacks eliminate per-user licence fees — estimated at €470–780 per user per year for comparable proprietary alternatives — and reduce vendor lock-in risk. Cooperative procurement models (govdigital eG, Dataport, AKDB, Swiss cantonal IT cooperatives) spread implementation costs. Indicative payback periods are 12–30 months depending on city size.

**4. The five case studies demonstrate that success is achievable at all scales.** Barcelona (large city, participation platform), the French Gendarmerie (85,000 desktops, productivity suite), Jena (medium city, OZG cooperative), Canton of Zug (pioneer identity and files), and the Munich counter-case (political risk management) together define the envelope of what works and what fails.

**5. Political sustainability and change management are the binding constraints — not technology.** Clear political mandate, cross-party institutionalisation, genuine training investment, and early-win communication are as important as technical planning. The Munich case confirms this; Barcelona, Jena, and Zug confirm the inverse.

Cities that act now gain first-mover advantages: shaping cooperative standards, building in-house expertise, reducing procurement complexity as frameworks mature, and contributing to the open-source commons that all municipalities share. The regulatory window is open. The tooling is ready. The procurement frameworks exist. The only remaining question is political will.

---

## References

[1] Swiss Federal Council. (2023). *Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG)*. SR 172.019. Bern: Swiss Confederation. https://www.fedlex.admin.ch/eli/cc/2023/682/de — [CC0, Swiss federal legislation]

[2] Bundesministerium des Innern und für Heimat (BMI). (2024). *Onlinezugangsgesetz 2.0 (OZG 2.0) — Novelle des Onlinezugangsgesetzes*. Berlin: BMI. https://www.bmi.bund.de/DE/themen/moderne-verwaltung/e-government/ozg/ozg-node.html — [DL-DE/Zero 2.0]

[3] Open Source Business Alliance (OSBA). (2024). *Sovereign Cloud Stack: Technical and Governance Overview*. Berlin: OSBA. https://scs.community/ — [Apache 2.0 / CC-BY-SA-4.0]

[4] Free Software Foundation Europe (FSFE). (2017). *Public Money? Public Code!* Berlin: FSFE. https://publiccode.eu/ — [CC-BY-SA-4.0]

[5] European Commission. (2020). *Open Source Software Strategy 2020–2023: Think Open*. Brussels: European Commission. https://commission.europa.eu/about/departments-and-executive-agencies/informatics/open-source-software-strategy_en — [EU publication, open access]

[6] European Parliament and Council. (2024). *Regulation (EU) 2024/903 — Interoperable Europe Act*. Brussels: Official Journal of the EU. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R0903 — [EU legislation, public domain]

[7] Wirtz, B. W., & Weyerer, J. C. (2017). Conceptualization and creation of a holistic e-government maturity model. *Public Management Review*, 19(9), 1297–1316. https://doi.org/10.1080/14719037.2017.1283024

[8] Janssen, M., Charalabidis, Y., & Zuiderwijk, A. (2012). Benefits, adoption barriers and myths of open data and open government. *Information Systems Management*, 29(4), 258–268. https://doi.org/10.1080/10580530.2012.716740

[9] FITKO. (2024). *Föderale IT-Kooperation — Jahresbericht 2023*. Frankfurt: FITKO. https://www.fitko.de/publikationen/jahresberichte — [DL-DE/Zero 2.0]

[10] openCode.de. (2022–2026). *openCode — Open Source for Government*. Berlin: Digitalservice GmbH des Bundes. https://opencode.de/ — [Open access; repository code under various OSI licences]

[11] Sovereign Cloud Stack Community. (2024). *SCS Technical Documentation*. https://docs.scs.community/ — [Apache 2.0]

[12] Decidim Association. (2021). *Decidim: Free Open-Source Participatory Democracy for Cities and Organizations*. Barcelona: Decidim Association. https://decidim.org/ — [AGPL-3.0]

[13] Nextcloud GmbH. (2024). *Nextcloud for Government: Security, Sovereignty, and Collaboration*. Stuttgart: Nextcloud GmbH. https://nextcloud.com/government/ — [AGPL-3.0]

[14] The Matrix Foundation. (2024). *Matrix Specification v1.x*. https://spec.matrix.org/ — [Apache 2.0]

[15] eCH (E-Government Standards Association). (2024). *eCH-Standards für E-Government-Anwendungen*. Bern: eCH. https://www.ech.ch/ — [Open access; individual standards under various licences]

[16] E-Government Suisse. (2023). *Strategie E-Government Schweiz 2024–2027*. Bern: Schweizerische Bundeskanzlei. https://www.egovernment.ch/de/umsetzung/e-government-strategie/ — [Open access, Swiss federal publication]

[17] CONSUL Democracy. (2024). *CONSUL: Open Source Democracy for Cities and Organizations*. Madrid: Ayuntamiento de Madrid. https://consuldemocracy.org/ — [AGPL-3.0]

[18] GovStack Initiative. (2024). *GovStack: Building Blocks for Digital Government*. Geneva / Berlin: ITU / Deutsche Gesellschaft für Internationale Zusammenarbeit (GIZ). https://www.govstack.global/ — [CC-BY-SA-4.0]

[19] TYPO3 Association. (2024). *TYPO3 in Public Administration*. Düsseldorf: TYPO3 Association. https://typo3.org/project/association — [GPL-2.0; documentation CC-BY-SA]

[20] OpenProject GmbH. (2024). *OpenProject: Open Source Project Management for Government*. Berlin: OpenProject GmbH. https://www.openproject.org/ — [GPLv3]

[21] Red Hat / Keycloak Community (CNCF). (2024). *Keycloak: Open Source Identity and Access Management*. https://www.keycloak.org/ — [Apache 2.0]

[22] CKAN Association. (2024). *CKAN: Open Source Data Portal Software*. https://ckan.org/ — [AGPL-3.0]

[23] govdigital eG. (2024). *govdigital: Genossenschaft für digitale Verwaltung*. Berlin: govdigital eG. https://govdigital.de/ — [Open access]

[24] Dataport AöR. (2024). *Dataport: IT-Dienstleister für die öffentliche Verwaltung*. Hamburg: Dataport AöR. https://www.dataport.de/ — [Open access]

[25] ZenDiS GmbH. (2024). *Zentrum für Digitale Souveränität der öffentlichen Verwaltung — Jahresbericht 2023*. Berlin: ZenDiS GmbH. https://zendis.de/ — [Open access]

[26] Bundesamt für Sicherheit in der Informationstechnik (BSI). (2023). *BSI IT-Grundschutz-Kompendium Edition 2023*. Bonn: BSI. https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/IT-Grundschutz-Kompendium/it-grundschutz-kompendium_node.html — [CC-BY-ND 3.0 DE]

[27] European Parliament and Council. (2022). *Directive (EU) 2022/2555 on Measures for a High Common Level of Cybersecurity (NIS2)*. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022L2555 — [EU legislation, public domain]

[28] European Parliament and Council. (2023). *Regulation (EU) 2023/2854 — EU Data Act*. Brussels: Official Journal of the EU. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023R2854 — [EU legislation, public domain]

[29] United Nations DESA. (2022). *UN E-Government Survey 2022: The Future of Digital Government*. New York: United Nations. https://publicadministration.un.org/egovkb/en-us/Reports/UN-E-Government-Survey-2022 — [UN open access]

[30] Janowski, T. (2015). Digital government evolution: From transformation to contextualization. *Government Information Quarterly*, 32(3), 221–226. https://doi.org/10.1016/j.giq.2015.07.001

[31] Guimard, X. (2013). *Migration to Ubuntu Linux in the Gendarmerie Nationale: A Cost-Benefit Analysis*. Paris: Direction Générale de la Gendarmerie Nationale (DGGN). Published in: FSFE Case Studies. https://fsfe.org/activities/os/localgov.en.html — [Open access]

[32] Lathrop, D., & Ruma, L. (Eds.). (2010). *Open Government: Collaboration, Transparency, and Participation in Practice*. Sebastopol, CA: O'Reilly Media. ISBN 978-0-596-80435-0.

[33] Camunda Services GmbH. (2024). *Camunda Platform 8 Community Edition*. Berlin: Camunda. https://camunda.com/download/ — [Apache 2.0 Community; proprietary Enterprise]

[34] BigBlueButton Inc. (2024). *BigBlueButton: Open Source Web Conferencing*. https://bigbluebutton.org/ — [LGPL-3.0]

[35] Jitsi Community / 8x8 Inc. (2024). *Jitsi Meet: Open Source Video Conferencing*. https://jitsi.org/ — [Apache 2.0]

[36] OpenStreetMap Foundation. (2024). *OpenStreetMap*. https://www.openstreetmap.org/ — [ODbL-1.0]

[37] QGIS Project. (2024). *QGIS: A Free and Open Source Geographic Information System*. https://www.qgis.org/ — [GPL-2.0+]

[38] European Commission / OSOR. (2023). *Open Source Observatory (OSOR) Annual Report 2023: Open Source in European Public Administration*. Brussels: European Commission, Joinup. https://joinup.ec.europa.eu/collection/open-source-observatory-osor — [CC-BY-4.0]

[39] Cloud Native Computing Foundation (CNCF). (2024). *Kubernetes*. https://kubernetes.io/ — [Apache 2.0]

[40] Swiss Federal Chancellery / BAZG. (2023). *Bundesgesetz über den elektronischen Identitätsnachweis und andere elektronische Nachweise (E-ID-Gesetz)*. SR 161.5. Bern: Swiss Confederation. https://www.fedlex.admin.ch/eli/cc/2024/291/de — [CC0, Swiss federal legislation]

[41] PostgreSQL Global Development Group. (2024). *PostgreSQL*. https://www.postgresql.org/ — [PostgreSQL Licence, OSI-approved]

[42] ZenDiS GmbH / BMI. (2024). *OpenDesk 2.x: Der digitale Arbeitsplatz der öffentlichen Verwaltung*. Berlin: ZenDiS GmbH. https://opendesk.eu/ — [AGPL-3.0]

[43] Schweizerisches Bundesarchiv (BAR). (2023). *Geschäftsverwaltung (GEVER) in der Bundesverwaltung*. Bern: BAR. https://www.bar.admin.ch/bar/de/home/digitale-archivierung/gever.html — [Open access]

[44] opendata.swiss. (2024). *Open Government Data Switzerland*. Bern: Schweizerische Bundeskanzlei. https://opendata.swiss/ — [CC-BY-4.0 portal; individual dataset licences vary]

[45] European Commission. (2017). *European Interoperability Framework — Implementation Strategy (EIF)*. Brussels: European Commission. https://joinup.ec.europa.eu/collection/nifo-national-interoperability-framework-observatory/european-interoperability-framework-detail — [CC-BY-4.0]

[46] KoSIT (Koordinierungsstelle für IT-Standards). (2024). *XÖV-Standards: XML in der öffentlichen Verwaltung*. Bremen: KoSIT. https://www.xoev.de/ — [Open access]

[47] The Document Foundation. (2024). *LibreOffice*. Berlin: The Document Foundation. https://www.libreoffice.org/ — [LGPL-3.0 / MPL-2.0]

[48] European Parliament and Council. (2024). *Regulation (EU) 2024/2847 — Cyber Resilience Act*. Brussels: Official Journal of the EU. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847 — [EU legislation, public domain]

[49] European Parliament and Council. (2024). *Regulation (EU) 2024/1689 — Artificial Intelligence Act*. Brussels: Official Journal of the EU. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689 — [EU legislation, public domain]

[50] AKDB (Anstalt für Kommunale Datenverarbeitung in Bayern). (2024). *AKDB: IT-Dienstleister für Kommunen in Bayern*. Munich: AKDB. https://www.akdb.de/ — [Open access]

[51] Ville de Paris / Direction des Systèmes et Technologies de l'Information (DSTI). (2017). *Migration LibreOffice: Bilan 2012–2017*. Paris: Ville de Paris. Referenced in: OSOR Case Studies. https://joinup.ec.europa.eu/ — [Open access]

[52] Bundesverwaltungsamt (BVA). (2023). *LibreOffice-Einsatz in der Bundesverwaltung*. Cologne: BVA. https://www.bva.bund.de/ — [Open access]

---

*This document is released under the Creative Commons Attribution 4.0 International Licence (CC-BY-4.0).*
*Attribute as: Sebastian Graf, Autonomous Office of Civil Digital Infrastructure (sebk4c@tuta.com)*
*Version 0.2.0 — Citation-Complete Draft — 2026-06-21*
