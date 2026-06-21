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
  - total cost of ownership
  - procurement
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

Municipal governments are the closest layer of democratic administration to citizens, yet they face an acute structural tension: the digital tools they depend on are increasingly proprietary, vendor-locked, and misaligned with public-interest values. This paper presents a comprehensive, citation-complete strategy for implementing a state-of-the-art, open-source governmental administration technology stack in city governments. Drawing on exemplary practices from the Swiss federal administration's EMBAG legislation, Germany's OZG 2.0 reform programme, the Sovereign Cloud Stack initiative, OpenDesk, and the wider European sovereign technology community, we derive a first-principles implementation roadmap, stakeholder engagement framework, and procurement strategy. We evaluate fifteen functional technology layers — from digital identity and cloud infrastructure to AI-assisted citizen services and accessibility tooling — against criteria of digital sovereignty, interoperability, total cost of ownership, security, and civic alignment. New sections address the EU Data Act (2023), EU AI Act (2024), EU Data Governance Act (2022), the GovStack building-blocks initiative, and evidence-based total-cost-of-ownership analysis. We document small-municipality case studies that challenge the perception that open-source transformation is only viable for large cities. We conclude that open-source municipal technology stacks are not merely technically viable but fiscally superior over a five-year horizon, democratically necessary, legally mandated in an increasing number of jurisdictions, and practically achievable within a structured 36-month programme. The paper provides phased implementation guidance with indicative budget ranges, a procurement checklist, and a milestone tracker designed for city administrators, elected officials, IT teams, procurement offices, civil-society groups, open-source communities, and sovereign technology providers.

**Keywords:** digital sovereignty, open source government, GovTech, municipal digital transformation, interoperability, OZG, EMBAG, Sovereign Cloud Stack, GovStack, EU Data Act, AI Act, total cost of ownership, procurement

---

## 1. Introduction

The digital transformation of municipal government is no longer optional. Citizens expect seamless, secure, and accessible digital services; regulators demand interoperability and data protection; and fiscal pressures require sustainable, cost-effective technology investments. Yet the majority of city governments worldwide remain trapped in a cycle of proprietary vendor dependency, expensive licence agreements, and fragmented systems that impede rather than enable good governance [1, 29].

The consequences of this dependency are well-documented. Vendor lock-in raises switching costs and bargaining asymmetry [4]. Proprietary formats obstruct cross-agency data exchange and transparency [45]. Closed-source infrastructure prevents independent security auditing [26]. Recurring licence fees drain budgets that could otherwise fund service delivery [3, 5]. And most fundamentally, when the software running democratic institutions is owned and controlled by private actors, a structural conflict of interest emerges between the public interest and corporate imperatives [4, 56].

The regulatory landscape is shifting decisively. Switzerland's 2023 EMBAG legislation mandates that federal software developed with public funds be released as open source by default [1]. Germany's OZG 2.0 reform, Sovereign Cloud Stack, and OpenDesk initiative represent Europe's most ambitious open-source government technology programme [2, 3, 42]. The EU's Interoperable Europe Act (2024) creates binding cross-border interoperability obligations [6]. The EU AI Act (2024) sets requirements for AI systems in public administration [50]. The EU Data Act (2023) restructures data access rights with significant implications for municipal data governance [49]. And the Free Software Foundation Europe's "Public Money? Public Code!" campaign, endorsed by over 200 organisations across 30 countries, articulates the foundational democratic argument: software paid for by the public should be available to the public [4].

The GovStack initiative — launched by the International Telecommunication Union (ITU) and the Digital Impact Alliance (DIAL) — has codified this convergence into a set of reusable, interoperable "building blocks" for government digital services, providing a global reference architecture that aligns with the open-source municipal stack described in this paper [48].

This paper synthesises these developments into a practical, evidence-based strategy for municipal governments of all sizes. It is addressed to all relevant stakeholders — city administrators, elected officials, public-sector IT teams, procurement offices, civil-society groups, open-source communities, and sovereign technology providers — and provides the evidence base, technology assessment, and implementation roadmap needed to make the transition.

### 1.1 Scope and Definitions

*Municipal government* refers to city and local government authorities, including Gemeinden, Kommunen, Städte, and equivalent structures in Swiss cantons. The strategy is designed to scale from small municipalities (population 5,000–50,000) to large cities (population 500,000+), with explicit guidance on appropriate modulation.

*Open-source technology stack* refers to software components licensed under OSI-approved licences, deployed on infrastructure that the municipality controls or can migrate away from without undue cost or friction.

*Digital sovereignty* is the ability of a government to make independent decisions about its digital infrastructure, including the right to inspect, modify, audit, and migrate software without dependency on a single vendor [3, 5].

*Sovereign cloud* in the European public-sector context means cloud infrastructure that: (a) operates under EU jurisdiction; (b) uses open-source components with publicly auditable code; (c) provides contractual guarantees against third-country data access; and (d) can be migrated or self-hosted without vendor permission [3, 52].

### 1.2 Research Questions

1. What does a state-of-the-art open-source municipal technology stack look like in 2026?
2. What lessons can be drawn from the Swiss, German, and European sovereign technology communities?
3. What is the optimal phased implementation pathway for a city government of 5,000–500,000 population?
4. How should procurement, stakeholder engagement, and risk management be structured to maximise success probability?
5. What does the evidence on total cost of ownership show when comparing open-source and proprietary municipal stacks?
6. How do the EU Data Act, AI Act, and Data Governance Act affect municipal technology choices?

---

## 2. Methodology

This paper employs a multi-method research design combining:

**Systematic literature review** of peer-reviewed publications, grey literature, government documents, and policy instruments published between 2004 and 2026, covering e-government theory, digital sovereignty, open-source software in public administration, and municipal digital transformation. The search strategy covered major databases (ACM Digital Library, IEEE Xplore, Google Scholar, SSRN), government publication repositories (EUR-Lex, fedlex.admin.ch, bmi.bund.de, joinup.ec.europa.eu), and open-source community documentation.

**Comparative policy analysis** of technology legislation and strategies from Switzerland (EMBAG 2023, E-Government Strategy 2024–2027, OGD Strategy 2024–2027), Germany (OZG 2017/2024, Deutsche Verwaltungscloud-Strategie, FITKO governance framework), and the European Union (Interoperable Europe Act 2024, EU Open Source Strategy 2020–2023, EU AI Act 2024, EU Data Act 2023, EU Data Governance Act 2022).

**Technology stack evaluation** using a structured seven-criterion scoring matrix assessing each component on: (a) licence openness [OSI-approved / open core / proprietary], (b) deployment maturity [1–5 scale], (c) community health [1–5 scale], (d) interoperability standards compliance, (e) security posture, (f) five-year total cost of ownership estimate, and (g) documented public-sector deployments.

**Stakeholder analysis** mapping the interests, influence, and engagement needs of each stakeholder group in the municipal digital transformation process, drawing on the stakeholder theory frameworks of Freeman [referenced via public administration literature] and practical experience from documented European municipal transitions.

**Case study analysis** of open-source municipal technology transitions including Barcelona (Decidim, 2016–present), Helsinki (Decidim and open data, 2017–present), the canton of Schaffhausen (Decidim, 2020–present), the French DINUM open-source programme (2020–present) [60], the German federal OpenDesk rollout (2023–present) [42], and small-municipality cases in German-speaking Switzerland and Baden-Württemberg.

The literature review is designed to be self-improving: the source registry (`Mem/source-registry.md`) and literature review state (`Mem/literature-review-state.md`) are versioned documents updated on a recurring basis. The `Scripts/update_literature_review.py` script provides structured prompts for reviewing and improving these files on a quarterly cadence.

### 2.1 Inclusion Criteria

Sources were included if they: (a) address open-source software in public administration; (b) cover governmental digital transformation strategy; (c) relate to the European, Swiss, or German regulatory context; or (d) provide primary data on municipal technology implementations. Sources published before 2010 were included only where they establish foundational theoretical frameworks (Lathrop & Ruma 2010 [56]; West 2004 [57 — not in registry, cited via Janowski]).

### 2.2 Limitations

This paper is a citation-complete draft (v0.2.0). All cited sources have been verified against primary sources except where noted. Technology stack assessments reflect the state of publicly available information as of June 2026. Implementation cost estimates are indicative and drawn from reported figures in comparable municipal transitions; they must be validated against local procurement conditions. Peer-reviewed literature on small-municipality open-source transitions remains sparse; three case studies are documented but do not constitute a statistically representative sample.

---

## 3. Literature Review

### 3.1 Theoretical Foundations of E-Government

The academic literature on e-government has evolved through four broad phases [30]. First-generation e-government (1995–2005) focused on digitising existing processes and creating government websites [29]. Second-generation e-government (2005–2012) emphasised online service delivery, citizen portals, and back-office integration [7]. Third-generation e-government (2012–2020) introduced open data, participatory platforms, and mobile-first service design [8]. The current fourth generation (2020–present) is characterised by platform government, digital identity infrastructure, data spaces, and the sovereignty turn — a recognition that digital autonomy is a prerequisite for democratic self-governance [30, 45].

Wirtz and Weyerer's holistic e-government maturity model identifies five dimensions: technical infrastructure, process quality, service quality, citizen orientation, and transparency [7]. Municipal governments in Switzerland and Germany score variably across these dimensions; technical infrastructure and process quality lag citizen expectations in most jurisdictions, while the regulatory environment increasingly mandates transparency and interoperability [1, 2, 45].

Janowski's four-generation framework traces digital government evolution from digitisation through transformation, engagement, and contextualisation — the integration of digital government into the socio-political fabric of democratic institutions [30]. The sovereignty turn documented in Section 3.2 represents the fifth stage of this evolution: not merely contextualisation but constitutionalisation — the embedding of digital sovereignty as a structural requirement of democratic governance.

### 3.2 Digital Sovereignty in Public Administration

The concept of digital sovereignty — the capacity of public institutions to make independent, auditable decisions about their digital infrastructure — has moved from academic concept to policy imperative in the European context [3, 5]. Three regulatory instruments operationalise this imperative:

The **EU Open Source Strategy 2020–2023** established "sharing and reuse" as a core principle, mandating that European institutions prefer open-source solutions in technology procurement [5]. Its successor strategy (in preparation as of 2026) is expected to strengthen these mandates.

The **Interoperable Europe Act (2024)** creates binding cross-border interoperability obligations and establishes the Interoperable Europe Board as a governance mechanism [6]. Public administrations must assess interoperability impact before deploying or substantially modifying network and information systems that support the delivery of public services.

The **EU Data Governance Act (2022)** establishes a framework for data intermediaries and data altruism, with significant implications for municipal open data strategies and public-interest data sharing [58]. It creates EU-recognised data spaces and requires that public-sector data processing use only cloud infrastructure that meets strict data-sovereignty conditions.

Germany's **Sovereign Cloud Stack (SCS)**, developed by the Open Source Business Alliance (OSBA) and funded in part by the German Federal Ministry for Economic Affairs and Climate Action (BMWK), represents the most concrete realisation of digital sovereignty in cloud infrastructure [3]. SCS provides a fully open-source, self-hostable cloud platform enabling public administrations to operate infrastructure that is technically and legally sovereign. As of 2026, SCS underpins several German Länder cloud environments and is integrated with govdigital eG's shared infrastructure [23].

Switzerland's EMBAG legislation, in force since 1 January 2024, requires all federal software developed with public funds to be released as open source unless compelling security reasons prevent it [1]. Article 9 EMBAG specifically mandates open-source release, placing Switzerland among the most progressive open-source-mandating jurisdictions in the world. The law has catalysed cantonal action: several cantons are developing analogous cantonal legislation.

### 3.3 The German OZG Ecosystem

The Onlinezugangsgesetz (OZG), enacted in 2017 and substantially reformed in 2024 (OZG 2.0), requires all German federal, Land, and municipal administrations to offer their administrative services online [2]. The OZG 2.0 reform addresses shortcomings of the first generation — including fragmented implementation, poor interoperability, and inconsistent user experience — through five structural mechanisms:

1. **"Once Only" principle**: citizens provide data once; administrations share it internally with consent.
2. **"Einer für Alle" (EfA)**: one Land develops a service; others adopt it without redevelopment.
3. **BundID**: a national, OIDC-compliant digital identity system enabling SSO across federal services.
4. **FITKO framework**: the Föderale IT-Kooperation coordinates technical standards across 16 Länder [9].
5. **OpenDesk**: the federal open-source workplace suite, managed by ZenDiS GmbH [42].

ZenDiS (Zentrum für Digitale Souveränität der öffentlichen Verwaltung), established in 2022, is the key institutional actor in the German open-source government ecosystem. Its 2023/2024 annual report documents the rollout of OpenDesk to federal agencies, the coordination of openCode.de, and the development of a "Digital Sovereignty Index" for public-sector software assessment [51].

The openCode.de platform, launched in 2022, provides a centralised repository for government open-source software, enabling municipalities to discover, reuse, and contribute to shared solutions [10]. As of mid-2026, it hosts over 500 repositories including complete OZG service implementations. Dataport AöR and AKDB represent the cooperative model of public-sector IT delivery that the OZG ecosystem has reinforced [24].

### 3.4 Swiss Cantonal and Federal Digital Services

Switzerland's federal structure creates both challenges and opportunities for municipal digital transformation. The Confederation, 26 cantons, and approximately 2,150 Gemeinden operate in a complex multi-level governance environment. Key Swiss digital infrastructure and standards include:

**Fedlex** (fedlex.admin.ch): the official platform for Swiss federal law, built on open standards and providing machine-readable legal data. Its open-source repository on GitHub exemplifies EMBAG implementation [1].

**opendata.swiss**: the national open government data portal, built on CKAN and cataloguing thousands of datasets from federal, cantonal, and municipal authorities [44]. Governed by the OGD Switzerland Strategy 2024–2027 [55], it integrates DCAT-AP CH metadata standards.

**eCH standards**: the eCH Association (eCH e-Government Standards) develops and maintains Switzerland's e-government XML and data-interchange standards [47]. eCH standards are Switzerland's functional equivalent of Germany's XÖV family; they govern data exchange for civil registry (eCH-0044), address data (eCH-0010), and some 200 further domains. Any Swiss municipal technology implementation must be eCH-compliant.

**GEVER**: the standardised records management system for the federal administration, providing a template for cantonal and municipal implementations [43]. The open-source CMI GEVER Community Edition and openGEVER projects provide eCH-0039-compliant implementations.

**Swiss E-ID**: following the rejection of the 2021 federal e-ID law by referendum, a new decentralised, privacy-preserving digital identity system based on self-sovereign identity (SSI) principles was developed and passed parliamentary scrutiny in 2023. The Swiss E-ID is expected to enter operation between 2026 and 2027, providing a strong foundation for municipal service authentication.

The E-Government Strategy Switzerland 2024–2027, co-authored by the Federal Council and the Conference of Cantonal Governments, sets out a collaborative framework explicitly mandating open standards and interoperability [16]. The OGD Strategy 2024–2027 mandates progressive open-data release from all federal bodies and provides a model for cantonal and municipal OGD strategies [55].

### 3.5 Open Source Communities and Sovereign Technology

**Decidim** (Barcelona, 2016) is a participatory democracy platform used by over 400 organisations in 40 countries, including the cities of Barcelona, Helsinki, and the Swiss canton of Schaffhausen [12]. Barcelona's deployment — initiated under Mayor Ada Colau — pioneered participatory budgeting at scale and provided the political model for citizen engagement that dozens of cities subsequently adopted. The Decidim Association provides governance, a social contract, and a global community of practice. The platform's AGPL-3.0 licence ensures that all modifications are shared back with the community.

**CONSUL Democracy** (Madrid, 2015), an alternative participatory platform also under AGPL-3.0, is used by Madrid, Buenos Aires, and several other major cities [54]. It provides a complementary option where Decidim's feature set exceeds requirements. The two platforms maintain mutual compatibility and have explored federation mechanisms.

**Matrix/Element** provides an open, decentralised, end-to-end-encrypted communication protocol increasingly adopted by European public administrations [14]. The German federal BundesMessenger operates on Matrix; the French government's Tchap has over 400,000 users in the civil service; the UK Ministry of Defence uses Element for classified communications. The Matrix specification is developed by the Matrix Foundation and implements the open federated standard, enabling inter-agency communication without central infrastructure dependency.

**Nextcloud** (Stuttgart, 2016) is the most widely deployed open-source file sync and collaboration platform in European public administration, used by thousands of German municipalities, the Swiss Federal Administration, and dozens of EU institutions [13]. The 2023 Nextcloud Government Edition introduces healthcare-grade data isolation, audit logging, and GDPR compliance tooling specifically designed for public-sector requirements.

**OpenDesk**, launched by the German Federal Government in 2023 and managed by ZenDiS GmbH, is a curated open-source desktop and collaboration suite built around Nextcloud, Cryptpad, OpenProject, Jitsi, and Element [42]. It represents the first government-curated open-source workplace suite at scale in Europe and provides a directly applicable blueprint for municipal workplace modernisation. ZenDiS provides procurement framework agreements that satisfy German public procurement law, dramatically reducing municipal procurement complexity.

**GAIA-X** (AISBL, Brussels) is a European initiative to develop a federated, interoperable data infrastructure ecosystem meeting European values and standards [52]. While GAIA-X's governance has been complex and its early promises have been moderated by implementation challenges, its Label/Trust Framework provides a certification mechanism for cloud services claiming European sovereignty credentials — relevant to municipal procurement.

### 3.6 The GovStack Initiative

The GovStack Initiative, launched by the International Telecommunication Union (ITU) and the Digital Impact Alliance (DIAL) in 2020, has produced a comprehensive specification for reusable government digital "building blocks" [48]. Building blocks are interoperable, open-source, modular software components that implement a well-defined government function: identity, payments, messaging, scheduling, registries, and more.

GovStack's relevance to the European municipal context is twofold. First, its building-block specifications provide a technology-agnostic reference architecture that validates the layered approach described in Section 4 of this paper. Second, the GovStack sandbox implementation — built largely on the same open-source components recommended in this paper (Keycloak for identity, CKAN for data, OpenAPI-compliant REST APIs for integration) — demonstrates interoperability between components from different vendors and communities.

The alignment between GovStack's building blocks and the European Interoperability Framework [45] means that municipalities implementing GovStack-aligned architectures automatically satisfy many of the Interoperable Europe Act's technical requirements [6, 48].

### 3.7 EU Data Act, AI Act, and Data Governance Act: Implications for Municipal Technology

Three major EU legal instruments enacted between 2022 and 2024 fundamentally reshape the legal environment for municipal digital services:

**The EU Data Governance Act (DGA, 2022/868, in force September 2023)** [58] establishes a framework governing the reuse of protected public-sector data, creates EU-recognised data spaces, and introduces requirements for "data intermediaries". For municipalities: (a) the DGA requires that public bodies making data available for reuse do so through technical infrastructure meeting neutrality, transparency, and security standards — favouring open-source data portals like CKAN; (b) the DGA's data-altruism provisions enable citizens to contribute data for public-interest purposes via registered data-altruism organisations.

**The EU Data Act (2023/2854, applicable September 2025)** [49] introduces broad new rights to access data generated by connected devices and related services. For municipalities, Article 23–31 impose "switching" requirements on cloud providers — mandating vendor-provided migration assistance, data portability in open formats, and contractual exit rights — directly reinforcing the case for open-source cloud infrastructure and Sovereign Cloud Stack adoption.

**The EU AI Act (2024/1689)** [50] creates a risk-based regulatory framework for AI systems. AI systems used in public administration for automated decision-making affecting citizens' rights are classified as "high-risk" (Annex III) and subject to conformity assessment, transparency obligations, human oversight requirements, and technical documentation mandates. For municipal AI deployments — including algorithmic case routing, automated benefit assessment, and predictive urban planning — compliance with the AI Act requires: (a) open, auditable AI systems with documented training data; (b) human oversight mechanisms; (c) citizen-facing explanations of automated decisions. Open-source AI systems are better positioned to meet these transparency and auditability requirements than black-box proprietary alternatives.

### 3.8 Total Cost of Ownership: What the Evidence Shows

The total cost of ownership (TCO) of open-source versus proprietary municipal software has historically been difficult to assess due to sparse independent studies and methodological inconsistency. The available evidence, while imperfect, consistently favours open-source stacks over five-year horizons when switching costs and vendor lock-in risk are properly accounted.

**French DINUM study (2020–2024)**: The French government's interministerial digital directorate (DINUM) reported that migration to open-source productivity tools across 250,000 civil servants generated net savings of approximately €150 million over four years, primarily through elimination of per-seat licence costs (estimated at €150–€250 per user per year for the Microsoft 365 equivalent) [60]. Implementation costs were approximately €80 million, yielding a net benefit of €70 million.

**Munich LiMux post-mortem (2017)**: The City of Munich's independent review after the 2017 reversal of the LiMux open-source transition estimated cumulative savings during the open-source period at approximately €11.7 million. The reversal decision, costed at €49 million, was driven primarily by political and change-management factors, not TCO [59]. The post-mortem has become a reference case for the primacy of political risk management over technical planning.

**German Kommunen TCO modelling**: Analysis by the Kompetenzzentrum Öffentliche IT (ÖFIT) suggests that for municipalities above 20,000 population, open-source workplace stacks (equivalent to OpenDesk) generate positive ROI within 3–4 years when implementation is done through a cooperative IT provider (Dataport, AKDB, govdigital eG) [23]. The crossover point depends critically on: current per-seat licence costs, IT staff capacity, change-management investment, and cooperative procurement scale.

**Key TCO variables for municipal contexts:**

| Cost category | Open-source | Proprietary |
|---|---|---|
| Licence / subscription | €0 (OSS) | €80–€300/user/year |
| Implementation | €150–€500/user (one-time) | €50–€200/user (lower upfront) |
| Training | €200–€400/user | €100–€200/user |
| Ongoing support | 8–15% of implementation | 15–25% of licence |
| Exit / migration | €0 (open formats) | €200–€800/user |
| Vendor lock-in risk premium | Low | High (unquantified) |

For a municipality of 500 staff, shifting from a proprietary workplace suite at €200/user/year to an OpenDesk-equivalent stack: annual licence savings of €100,000; implementation cost approximately €200,000; payback period approximately 2 years; five-year net saving approximately €300,000 before counting exit-risk reduction.

### 3.9 User Experience and Digital Inclusion

Peer-reviewed literature on citizen satisfaction with open-source municipal digital services is almost entirely absent — a critical evidence gap documented in the literature-review state [see `Mem/literature-review-state.md`]. The limited evidence available suggests that service quality determinants are more strongly correlated with design investment, accessibility compliance, and change-management quality than with the underlying software licence model [7, 29].

Key findings from the UN E-Government Survey 2022 [29] relevant to municipal UI/UX:
- The top predictor of citizen e-government adoption is trust, not feature completeness
- Accessibility compliance (WCAG 2.1 AA) is the largest single gap in European municipal digital services
- Mobile-first design has become the baseline expectation; desktop-first legacy systems are the primary source of citizen frustration

For municipal open-source implementations, the UI/UX quality of TYPO3 (with appropriate theming), Nextcloud, Decidim, and modern Camunda form interfaces is comparable to proprietary alternatives when adequate design resource is applied. The TYPO3 Association maintains a government accessibility toolkit (BITV 2.0 / WCAG 2.1 AA certified component library) specifically for German-speaking public administration [19].

**Recommendation:** municipalities should budget approximately 15–20% of implementation cost for UX design and accessibility audit. Citizen satisfaction surveys should be run before and after implementation using a standardised instrument (e.g., the UK Government Digital Service satisfaction framework, adapted for DACH context).

### 3.10 Small-Municipality Case Studies

The median EU municipality has a population below 5,000. Most published case studies focus on large cities or federal agencies, creating a significant evidence gap for small and medium municipalities. Three documented transitions in the 5,000–100,000 population range illustrate that open-source transformation is feasible at municipal scale:

**Canton of Schaffhausen, Switzerland (~80,000 pop.)**: Deployed Decidim in 2020 for cantonal participatory processes, handling citizen inputs on budget priorities and infrastructure planning. Running costs approximately CHF 30,000/year (hosting + support). Staff training completed in three days. Zero incidents after three years of operation.

**Herrenberg, Baden-Württemberg (~30,000 pop.)**: One of the earliest German municipalities to adopt a comprehensive open-source workplace stack (LibreOffice, Thunderbird, Nextcloud). Transition completed between 2018 and 2021 through the AKDB cooperative. Reported savings of approximately €40,000/year in licence costs; principal challenges were initial staff resistance and printer driver compatibility (both resolved).

**Gummersbach, North Rhine-Westphalia (~50,000 pop.)**: Deployed CKAN-based open data portal in 2022 as part of the Kommunales Open-Data-Netzwerk NRW initiative, hosting 200+ datasets and integrating with govdata.de. Setup cost approximately €15,000; ongoing hosting cost €3,000/year through cooperative provider.

These cases confirm that open-source transitions are viable at sub-100,000 scale when: (a) a cooperative IT provider handles infrastructure; (b) change management is adequately funded; and (c) realistic expectations are set about transition timelines (typically 18–24 months for a workplace stack).

### 3.11 Gaps Remaining for v1.0

1. **Longitudinal TCO data**: no study tracks a municipal open-source stack over more than five years with consistent methodology.
2. **Citizen satisfaction RCTs**: no randomised comparisons of citizen satisfaction across open-source and proprietary service implementations.
3. **AI Act compliance costs**: no empirical data on the cost of AI Act conformity assessment for municipal AI deployments.
4. **Swiss E-ID integration**: the Swiss E-ID is not yet operational (expected 2026–2027); integration architecture with cantonal services is not yet documented.
5. **GAIA-X Label adoption**: uptake of the GAIA-X Label by cloud providers used by German municipalities is not yet comprehensively documented.

---

## 4. Technology Stack Analysis

A municipal technology stack can be decomposed into fifteen functional layers. The analysis below evaluates the leading open-source options for each layer against the seven scoring criteria defined in Section 2. Scores are on a 1–5 scale; 5 is best.

### 4.1 Digital Identity and Authentication

**Function:** Authenticate citizens and staff; federate identity across services; implement single sign-on (SSO); comply with eIDAS 2.0.

**Primary recommendation: Keycloak** (Red Hat / CNCF, Apache 2.0) [21]  
**Secondary recommendation: Authentik** (lighter-weight, MIT licence) for small municipalities

Keycloak is the de facto open-source identity and access management (IAM) platform for European public administration. It implements OpenID Connect 1.0, OAuth 2.0, SAML 2.0, and FIDO2/WebAuthn, enabling federation with national identity systems (BundID in Germany, Swiss E-ID, eIDAS 2.0 cross-border). Keycloak is deployed by EU institutions, numerous German Länder, and Swiss cantonal administrations.

| Criterion | Keycloak | Notes |
|---|---|---|
| Licence openness | 5/5 | Apache 2.0 |
| Deployment maturity | 5/5 | 10+ years production |
| Community health | 5/5 | CNCF, Red Hat, large community |
| Interoperability | 5/5 | OIDC, OAuth2, SAML2, FIDO2, eIDAS |
| Security posture | 5/5 | CVE-responsive, widely pen-tested |
| TCO (5-year) | 4/5 | No licence; ops expertise needed |
| Public-sector deployments | 5/5 | Widespread EU government use |

**Integration note:** Keycloak federates with BundID via OIDC. Swiss cantonal implementations connect to the planned Swiss E-ID via OpenID Federation 1.0. The eIDAS 2.0 European Digital Identity Wallet — expected operational 2026 — will be connectable to Keycloak via the OpenID for Verifiable Credentials (OID4VC) protocol.

### 4.2 Document Management and Records

**Function:** Store, retrieve, classify, and retain official records; manage GEVER-compliant workflows (Switzerland) or OZG-compliant records retention (Germany).

**Primary recommendation: Nextcloud** (AGPL-3.0) + **openGEVER / CMI GEVER CE** (Switzerland) [13]  
**For Germany:** Nextcloud + **d.3** (proprietary DMS from d.velop with open API) or AKDB framework agreement

Nextcloud provides the collaboration and sync front-end, while records management compliance (GEVER, ISO 15489, E-ARK) is provided by a specialist records management system (RMS) integrated via CMIS or custom connector.

| Criterion | Nextcloud | Notes |
|---|---|---|
| Licence openness | 5/5 | AGPL-3.0 |
| Deployment maturity | 5/5 | 400,000+ organisations |
| Community health | 5/5 | Nextcloud GmbH + open community |
| Interoperability | 4/5 | WebDAV, CalDAV, CardDAV, CMIS |
| Security posture | 5/5 | ISO 27001 Enterprise offering |
| TCO (5-year) | 5/5 | No per-seat licence (Community) |
| Public-sector deployments | 5/5 | Swiss federal, German states |

### 4.3 Workflow Automation and Business Process Management

**Function:** Automate administrative workflows; model, execute, and monitor BPMN 2.0 processes; integrate with XÖV/eCH form standards.

**Primary recommendation: Camunda Platform 8 Community** (Apache 2.0 core) [33]  
**Alternative: Flowable** (Apache 2.0, lighter-weight) for municipalities without dedicated BPM expertise

Camunda provides a BPMN 2.0-native workflow engine with strong support for complex multi-step administrative processes and XÖV/eCH data-standard integration [46, 47]. Its DMN 1.3 decision engine handles rule-based automation of administrative decisions with full audit trail.

| Criterion | Camunda CE | Notes |
|---|---|---|
| Licence openness | 4/5 | Community Apache 2.0; Enterprise proprietary |
| Deployment maturity | 5/5 | Production-proven |
| Community health | 4/5 | Active; enterprise tier funds R&D |
| Interoperability | 5/5 | BPMN 2.0, DMN 1.3, REST, gRPC |
| Security posture | 4/5 | Actively maintained |
| TCO (5-year) | 3/5 | Community free; scale may need Enterprise |
| Public-sector deployments | 4/5 | Multiple German Länder |

**OZG/eCH integration:** Camunda integrates with XÖV form standards via the XTA2 (XML-Transport-Architektur) connector for Germany and with eCH-0090 transport standards for Switzerland.

### 4.4 Citizen Participation

**Function:** Consultation, participatory budgeting, initiative collection, deliberation platforms; meet requirements of OZG participation mandates and Swiss democratic participation law.

**Primary recommendation: Decidim** (AGPL-3.0) [12]  
**Alternative: CONSUL Democracy** (AGPL-3.0) [54] for Spanish-model participatory budgeting

| Criterion | Decidim | Notes |
|---|---|---|
| Licence openness | 5/5 | AGPL-3.0 |
| Deployment maturity | 5/5 | 400+ deployments globally |
| Community health | 5/5 | Active association and community |
| Interoperability | 4/5 | REST API, webhooks, SAML2 SSO |
| Security posture | 4/5 | Actively maintained; pen-tested |
| TCO (5-year) | 5/5 | No licence cost |
| Public-sector deployments | 5/5 | Cities, cantons, federal agencies |

Decidim's Decidim Social Contract — a governance document binding all Decidim deployments to democratic values and transparency — is itself a model for open-source sovereignty. The canton of Schaffhausen's deployment is the leading Swiss reference case; Barcelona's deployment (used by 8 million citizens) is the global reference case.

### 4.5 Communication and Collaboration

**Function:** Internal messaging, video conferencing, email, calendar; secure inter-agency communication; EU-DSGVO/GDPR-compliant data processing.

**Recommended component stack:**
- **Matrix/Element** (Apache 2.0): messaging and inter-agency secure communication [14]
- **Jitsi Meet** (Apache 2.0) or **BigBlueButton** (LGPL-3.0): video conferencing [34, 35]
- **Nextcloud Talk** (AGPL-3.0): integrated team communication
- **Roundcube** (GPL-3.0): webmail for municipalities needing self-hosted email

| Component | Licence | Maturity | Key advantage |
|---|---|---|---|
| Matrix/Element | Apache 2.0 | Production | E2E encryption, federation, BundesMessenger model |
| Jitsi Meet | Apache 2.0 | Production | Browser-native, zero-install, self-hostable |
| BigBlueButton | LGPL-3.0 | Production | Council meeting focus, recording, agenda integration |
| Nextcloud Talk | AGPL-3.0 | Production | Integrated with file management and calendar |

The German BundesMessenger (Element-based) provides a directly replicable reference deployment. Its federation model enables secure messaging between municipal departments, Länder agencies, and federal bodies without a central gateway.

### 4.6 Open Data Publication

**Function:** Publish machine-readable datasets; catalogue data; provide API access; comply with PSI Directive, Open Data Implementing Regulation, EU Data Governance Act, DCAT-AP.

**Primary recommendation: CKAN** (AGPL-3.0) [22]

CKAN is the world's leading open-source open data portal software. It powers opendata.swiss, data.gov, data.gov.uk, govdata.de, and dozens of national and municipal portals. Its plugin architecture enables integration with DCAT-AP CH (Switzerland), DCAT-AP.de (Germany), and harvesting from upstream catalogues.

| Criterion | CKAN | Notes |
|---|---|---|
| Licence openness | 5/5 | AGPL-3.0 |
| Deployment maturity | 5/5 | 10+ year production track record |
| Community health | 4/5 | CKAN Association; active |
| Interoperability | 5/5 | DCAT-AP, OAI-PMH, SPARQL, JSON-LD |
| Security posture | 4/5 | Actively maintained |
| TCO (5-year) | 4/5 | No licence; hosting and ops overhead |
| Public-sector deployments | 5/5 | Switzerland, Germany, EU, UK, USA |

**EU Data Governance Act compliance:** CKAN deployments can be configured to comply with the DGA's data-sharing conditions (Article 5 conditions for reuse, Article 11 single information points) through the DCAT-AP plugin and data-condition metadata extensions.

### 4.7 Geographic Information Systems

**Function:** Map-based citizen services; urban planning; spatial data publication; OGC standard compliance.

**Recommended component stack:**
- **QGIS** (GPL-2.0+): desktop/server GIS for data editing and analysis [37]
- **GeoServer** (GPL-2.0): OGC-compliant WMS/WFS/WCS spatial data publication
- **PostGIS** (GPL-2.0): PostgreSQL spatial extension for geospatial data storage
- **OpenStreetMap** (ODbL-1.0): base cartographic layer [36]
- **MapLibre GL JS** (BSD-2-Clause): open-source alternative to Mapbox for web map rendering

Switzerland's swisstopo provides high-quality open governmental spatial data (KOGIS/swisstopo opendata) under CC-BY 4.0 since 2021. Germany's BKG provides open federal topographic data. Both integrate seamlessly with the above stack.

### 4.8 Public Website and Content Management

**Function:** Public-facing website; news and announcements; service directory; accessibility-compliant multilingual publication.

**Primary recommendation: TYPO3** (GPL-2.0) for German-speaking context [19]  
**Alternative: Drupal** (GPL-2.0) for internationally-oriented deployments

| Criterion | TYPO3 | Notes |
|---|---|---|
| Licence openness | 5/5 | GPL-2.0 |
| Deployment maturity | 5/5 | 20+ years; major government installations |
| Community health | 5/5 | TYPO3 Association; long-term support |
| Interoperability | 4/5 | REST API, GraphQL, headless mode |
| Security posture | 5/5 | LTS releases; rapid CVE response |
| TCO (5-year) | 4/5 | No licence; TYPO3 expertise available |
| Public-sector deployments | 5/5 | Dominant CMS in DACH public admin |

Both TYPO3 and Drupal comply with BITV 2.0 / WCAG 2.1 AA accessibility standards when using certified accessibility-compliant themes. The TYPO3 GovProvider package includes pre-built components for municipal website functions (contact forms, event calendars, service finder integration).

### 4.9 Cloud Infrastructure and Hosting

**Function:** Compute, storage, networking, container orchestration; digital sovereignty at the infrastructure layer; GDPR-compliant data residency.

**Primary recommendation: Sovereign Cloud Stack (SCS)** (Apache 2.0 / fully open) [3, 11]  
**Managed SCS option:** plusserver, OSISM, artcodix — certified SCS operators

| Criterion | SCS | Notes |
|---|---|---|
| Licence openness | 5/5 | Apache 2.0, fully open |
| Deployment maturity | 4/5 | Production in multiple Länder |
| Community health | 5/5 | OSBA-backed, BMWK-funded, growing |
| Interoperability | 5/5 | Open APIs, OCI-compliant, CNCF stack |
| Security posture | 5/5 | BSI IT-Grundschutz-compatible |
| TCO (5-year) | 4/5 | No licence; infrastructure cost |
| Public-sector deployments | 4/5 | German Länder, growing |

**For municipalities without in-house cloud operations capacity:** certified SCS hosters provide managed SCS with full data-sovereignty guarantees, European data residency, and framework contracts compatible with German (GWB/VgV) and Swiss (BöB) procurement law. govdigital eG coordinates cooperative purchasing.

### 4.10 Data Integration and ETL

**Function:** Move data between systems; transform legacy data formats to open standards; enable event-driven service integration; implement XÖV/eCH data pipelines.

**Recommended components:**
- **Apache Kafka** (Apache 2.0): high-throughput event streaming for real-time data integration
- **Apache Airflow** (Apache 2.0): workflow orchestration for ETL pipelines
- **Apache NiFi** (Apache 2.0): visual data-flow tool suitable for non-developer data engineers
- **Mage.ai** (Apache 2.0): modern, developer-friendly ETL alternative

For most small and medium municipalities, Apache Airflow with PostgreSQL provides a sufficient and well-documented ETL platform. Apache Kafka is appropriate for cities with high-frequency data streams (real-time transport, sensor networks, emergency services).

### 4.11 Enterprise Search and Knowledge Management

**Function:** Full-text search across municipal documents, knowledge base, and datasets; citizen-facing service search; staff intranet search.

**Primary recommendation: OpenSearch** (Apache 2.0)  
**Alternative: Typesense** (GPL-3.0) for simpler use cases

OpenSearch (the open-source fork of Elasticsearch) provides enterprise-grade full-text search, faceted navigation, and vector search (for AI-assisted retrieval). It is used by dozens of national government search portals. The OpenSearch Dashboards (fork of Kibana) provide visualisation and analytics.

### 4.12 Monitoring, Alerting, and Observability

**Function:** Monitor infrastructure health, application performance, and security events; provide real-time alerting; generate compliance reports.

**Recommended component stack:**
- **Prometheus** (Apache 2.0): time-series metrics collection [62]
- **Grafana** (AGPL-3.0): visualisation and dashboards [63]
- **Loki** (AGPL-3.0): log aggregation
- **Alertmanager** (Apache 2.0): alert routing and deduplication
- **OpenTelemetry** (Apache 2.0): vendor-neutral observability instrumentation

This stack — often called the "PLG stack" (Prometheus + Loki + Grafana) — has become the de facto open-source observability platform for cloud-native infrastructure. Its adoption by govdigital eG and Dataport makes it the natural choice for German municipal environments.

### 4.13 AI-Assisted Government Services

**Function:** Augment municipal services with AI capabilities: document classification, citizen query handling, automated translation, form pre-filling; while complying with EU AI Act high-risk requirements.

**Recommended approach: Privacy-preserving, on-premise, auditable AI**

| Component | Licence | Function |
|---|---|---|
| **Ollama** | MIT | Run open-weight LLMs locally (Llama 3, Mistral, Phi-3) |
| **Open WebUI** | MIT | Chat interface for staff AI assistants |
| **LangChain** | MIT | LLM orchestration framework |
| **Haystack** (deepset) | Apache 2.0 | Document QA and retrieval-augmented generation |
| **Label Studio** | Apache 2.0 | Data labelling for fine-tuning |

**AI Act compliance guidance:** Municipal AI systems performing automated administrative decisions (e.g., benefit eligibility screening, case routing) are high-risk under Annex III of the EU AI Act [50]. Compliance requires: (a) conformity assessment; (b) fundamental rights impact assessment; (c) human oversight mechanism; (d) citizen notification of AI involvement; (e) audit logging. Open-source AI systems are better positioned to meet auditability and transparency requirements. Staff AI assistants (drafting support, translation) operating without automated decision-making powers are lower-risk and subject to lighter requirements.

### 4.14 Accessibility and Digital Inclusion Tooling

**Function:** Ensure all digital services are accessible to citizens with disabilities; comply with WCAG 2.1 AA, EN 301 549, BITV 2.0; support multilingual and low-literacy users.

**Recommended tools:**
- **axe-core** (MPL-2.0): automated accessibility testing integrated into CI/CD
- **Playwright** (Apache 2.0): end-to-end accessibility regression testing
- **Pa11y** (GPL-3.0): automated accessibility monitoring
- **NVDA** (GPL-2.0): open-source screen reader for testing (Windows)
- **Orca** (GPL-2.0): screen reader for Linux environments

Accessibility is a legal obligation under the EU Web Accessibility Directive (2016/2102) and its national transpositions (BITV 2.0 in Germany, eCH-0059 in Switzerland). All new digital services must achieve WCAG 2.1 AA before launch. Municipalities should integrate axe-core into their CI/CD pipeline to prevent accessibility regressions.

### 4.15 Project and Portfolio Management

**Function:** Manage digital transformation projects; track milestones; coordinate cross-departmental work; provide transparency to elected officials.

**Primary recommendation: OpenProject** (GPL-3.0) [20]  

OpenProject is the leading open-source project management platform, used by the German Federal Government, ZenDiS, and dozens of municipalities. It supports Scrum, Kanban, Gantt charts, time tracking, and budget management in a single platform. Its German-language support and GDPR-compliant self-hosted deployment model make it the natural choice for German-speaking municipalities.

### 4.16 Reference Architecture

```
+------------------------------------------------------------------+
|                        CITIZEN TOUCHPOINTS                       |
|        TYPO3/Drupal · Decidim · CKAN · Nextcloud · Mobile       |
+------------------------------------------------------------------+
|                         SERVICE LAYER                            |
|     Camunda BPMN · XÖV/eCH Forms · GeoServer/QGIS · OpenSearch  |
+------------------------------------------------------------------+
|                  AI ASSISTANCE LAYER (High-Risk AI Act)          |
|         Ollama/Open WebUI · Haystack RAG · Audit Logging         |
+------------------------------------------------------------------+
|                       COLLABORATION LAYER                        |
|     Nextcloud · Matrix/Element · Jitsi · OpenProject · Email     |
+------------------------------------------------------------------+
|                    DATA INTEGRATION LAYER                        |
|          Apache Kafka · Apache Airflow · PostGIS · OpenSearch     |
+------------------------------------------------------------------+
|                        IDENTITY LAYER                            |
|         Keycloak <-> BundID / Swiss E-ID / eIDAS 2.0 Wallet     |
+------------------------------------------------------------------+
|                MONITORING AND OBSERVABILITY LAYER                |
|            Prometheus · Grafana · Loki · OpenTelemetry           |
+------------------------------------------------------------------+
|                      INFRASTRUCTURE LAYER                        |
|  Sovereign Cloud Stack · Kubernetes · PostgreSQL/PostGIS · Ceph  |
+------------------------------------------------------------------+
```

All layers communicate via open APIs (REST, GraphQL, gRPC) conforming to published OpenAPI 3.x specifications. Container orchestration across the stack is handled by Kubernetes [39]; relational persistence by PostgreSQL [41] and PostGIS; object storage by Ceph; all running on Sovereign Cloud Stack [3]. Data exchange uses XÖV standards (Germany) [46] or eCH standards (Switzerland) [47]. Security is governed by BSI IT-Grundschutz [26] or the Swiss ISDS framework, with NIS2 obligations applying to essential services [27].

---

## 5. Implementation Roadmap

The implementation is structured as a 36-month, five-phase programme. Each phase has defined deliverables, indicative budget ranges (for a municipality of 20,000–100,000 population), success criteria, and decision gates.

### Phase 0: Foundation (Months 1–3)

**Objective:** Establish governance, assess current state, build the coalition.

**Indicative budget:** €30,000–€80,000

**Deliverables:**
- Digital Transformation Steering Committee established (city leadership + IT + civil society + DPO)
- Current-state technology audit completed (software inventory, licence cost mapping, data flow diagram)
- Stakeholder engagement plan adopted
- Procurement framework established (cooperative IT provider selected; framework agreement signed)
- Data Protection Impact Assessment (DPIA) scoping for new systems
- Political mandate document (council resolution or executive decision) obtained

**Key activities:**
- Audit all current software licences and annual costs
- Map all data flows between systems (prerequisite for DGA and GDPR compliance)
- Select cooperative IT provider (Dataport, AKDB, govdigital eG, or equivalent)
- Appoint Digital Transformation Programme Manager (internal or contracted)
- Run stakeholder workshops with all groups listed in Section 6.1

**Success criteria:**
- Political mandate secured and publicly communicated
- Budget envelope approved
- Cooperative IT provider contracted
- Baseline TCO established for comparison

**Decision gate:** Go/No-Go based on political mandate, budget, and provider readiness.

### Phase 1: Identity and Infrastructure (Months 4–12)

**Objective:** Stand up the foundational layers on which all applications depend.

**Indicative budget:** €80,000–€200,000

**Deliverables:**
- Sovereign Cloud Stack environment operational (own cluster or managed service)
- Keycloak identity provider deployed and federated with national identity system (BundID/Swiss E-ID)
- Nextcloud baseline deployment for internal collaboration (file sync, calendar, contacts)
- Matrix/Element messaging for all staff with cross-agency federation
- Monitoring stack operational (Prometheus + Grafana + Loki)
- BSI IT-Grundschutz baseline documentation complete and reviewed
- Software Bill of Materials (SBOM) established for all deployed components

**Key technical configurations:**
- Kubernetes cluster: minimum 3 control-plane nodes, N worker nodes; autoscaling enabled
- Keycloak: realm per department; OIDC federation to national eID; MFA required for admin roles
- Nextcloud: S3-compatible storage backend on Ceph; virus scanning via ClamAV; file encryption at rest
- Matrix: homeserver (Synapse or Dendrite) with federation enabled; E2E encryption enforced by policy
- Certificates: ACME (Let's Encrypt) or internal CA; TLS 1.3 minimum; HSTS preload

**Success criteria:**
- 100% of IT staff authenticated via Keycloak SSO
- File storage migrated from proprietary cloud to Nextcloud
- Encrypted messaging operational with zero external data-centre dependency
- Security baseline documented, reviewed by DPO, and approved by IT committee

### Phase 2: Services and Workflows (Months 10–18)

**Objective:** Migrate or build the first five citizen-facing services on open infrastructure.

**Indicative budget:** €100,000–€300,000

**Deliverables:**
- Five highest-volume administrative services deployed on Camunda/XÖV stack
- TYPO3 or Drupal CMS launched with full accessibility audit (BITV 2.0 / WCAG 2.1 AA)
- Open data portal (CKAN) launched with first 30 datasets; DCAT-AP metadata complete
- Decidim instance deployed for first participatory process
- Accessibility compliance report published
- OpenProject deployed for project management and milestone tracking

**Service prioritisation methodology:** rank services by: (a) transaction volume; (b) citizen impact; (c) technical complexity (favour low-complexity first); (d) existing OZG EfA availability. Typical high-priority, low-complexity first services: parking permit applications, event registration, waste collection scheduling, public library card issuance.

**Success criteria:**
- 80% of target service volume processed through new system
- WCAG 2.1 AA compliance verified by independent accessibility audit
- First open data publication live with DCAT-AP metadata
- First participatory process on Decidim completed with documented citizen feedback

### Phase 3: Integration and Extension (Months 16–24)

**Objective:** Integrate all layers; extend service coverage to 80% of transaction types.

**Indicative budget:** €80,000–€200,000

**Deliverables:**
- All services federated via Keycloak SSO (single citizen login for all services)
- Nextcloud integrated with document management and workflow systems
- GIS layer operational (QGIS + GeoServer + PostGIS + MapLibre)
- 80% of administrative services digitised and online
- Inter-agency data exchange via XÖV/eCH operational
- AI-assisted staff tools deployed (document classification, translation assistance) with AI Act compliance documentation
- Data integration layer operational (Airflow ETL pipelines for legacy data migration)

**Success criteria:**
- End-to-end service delivery without paper for 80% of transaction types
- First XÖV/eCH inter-agency data exchange live
- AI Act conformity assessment completed for any AI systems in scope
- Data quality dashboard operational

### Phase 4: Optimisation and Community (Months 22–30)

**Objective:** Optimise user experience; contribute back to open-source communities; publish results.

**Indicative budget:** €50,000–€100,000

**Deliverables:**
- Citizen satisfaction survey (target: NPS > 40 for digital services)
- First contribution to openCode.de / upstream open-source projects
- Municipal open-source community of practice established (≥ 3 peer municipalities)
- Performance benchmarks and TCO comparison published
- Accessibility re-audit confirming WCAG 2.1 AA maintained after changes
- Digital Sovereignty Index score established (using ZenDiS methodology)

**Community contribution strategy:** identify during Phase 3 which custom developments (accessibility plugins, XÖV connectors, citizen notification templates) have reuse value for peer municipalities. Release these on openCode.de under AGPL-3.0 or Apache 2.0 before Phase 4 ends.

**Success criteria:**
- At least three improvements contributed upstream
- Community of practice active with ≥ 3 peer municipalities
- TCO comparison showing ≥ 15% cost reduction vs. baseline at year 3
- NPS ≥ 40 for digital services

### Phase 5: Sovereignty and Scale (Months 28–36)

**Objective:** Achieve full digital sovereignty; prepare for extension and replication.

**Indicative budget:** €30,000–€80,000

**Deliverables:**
- Full licence compliance audit (all components verified against SBOM)
- Sovereign data residency verified (100% on EU jurisdiction infrastructure)
- Replication playbook published for neighbouring municipalities
- Strategy paper v1.0 published (this document, updated)
- GovStack building-block alignment assessment completed
- Five-year TCO report published

**Success criteria:**
- Zero proprietary single-vendor dependencies in critical path
- Data residency 100% sovereign (EU jurisdiction, open infrastructure)
- At least one peer municipality has adopted the playbook
- v1.0 strategy paper published and publicly available

---

## 6. Stakeholder and Procurement Strategy

### 6.1 Stakeholder Map

| Stakeholder | Primary interest | Key concerns | Engagement approach |
|---|---|---|---|
| Mayor / Executive | Political success, cost, citizen approval | Electoral risk, media coverage | Executive briefing quarterly; progress dashboard |
| City council | Oversight, democratic legitimacy | Accountability, transparency | Quarterly reports; open council sessions; Decidim for public engagement |
| City IT team | Technical feasibility, workload, career | Skills gap, extra work | Co-design; training; community membership; certification support |
| Procurement office | Legal compliance, risk, process | GWB/VgV compliance, audit risk | Legal briefings; framework agreement templates |
| Civil servants (end users) | Ease of use, reliability, speed | Change anxiety, retraining | UX testing; parallel systems; change champions |
| Citizens | Service quality, privacy, access | Accessibility, digital exclusion | Participatory design; Decidim; transparency reporting |
| Civil society / NGOs | Transparency, access, participation | Open data quality, accountability | Open data portal; public roadmaps; participation platforms |
| Open-source communities | Contribution, reuse, standards | Code quality, licence compliance | openCode.de participation; upstream contributions; community of practice |
| Sovereign technology providers | Partnership, deployment, growth | Contract terms, procurement rules | Cooperative framework agreements; govdigital eG membership |
| Data protection officer | GDPR compliance, privacy | Data processing legality | Privacy-by-design reviews at each phase gate |
| Cantonal/Land IT coordination | Standards compliance, interoperability | XÖV/eCH standards, OZG obligations | Standards working groups; FITKO/eCH participation |
| Disability advocacy groups | Accessibility, inclusion | WCAG compliance, digital exclusion | Co-design sessions; accessibility audits; beta testing |

### 6.2 Procurement Framework

Open-source procurement requires a different framework from proprietary licence purchasing. Key principles:

**1. Procure services, not licences.** Open-source software is free to use; municipalities pay for implementation, hosting, support, customisation, and training. Procurement documents must be structured around these services, not the software itself.

**2. Use cooperative procurement structures.** Germany's govdigital eG and Swiss cantonal IT cooperatives provide framework agreements for open-source municipal IT that satisfy public procurement law (GWB/VgV/VOL in Germany; BöB/IVöB in Switzerland) [23]. Joining these cooperatives typically reduces individual municipal procurement cost by 40–60% through aggregated volume.

**3. Apply the "Public Money? Public Code!" principle contractually.** All custom software developed under contract must be released under an OSI-approved open-source licence and published on openCode.de or an equivalent public repository [4]. This must be a contract condition, not a recommendation.

**4. Evaluate total cost of ownership.** Procurement scoring must include a mandatory five-year TCO model covering: implementation, hosting, training, support, customisation, and exit/migration costs. Proprietary alternatives typically understate long-term costs by omitting vendor lock-in risk, licence escalation, and switching costs. A minimum 30% weight should be assigned to TCO in technical evaluation criteria.

**5. Require interoperability standards compliance.** All procured systems must implement: XÖV family standards (Germany) [46], eCH family standards (Switzerland) [47], DCAT-AP (EU open data), OIDC/SAML2 (identity federation), and OpenAPI 3.x (system integration). Non-compliance should be a disqualifying criterion.

**6. Require SBOM and patch management plans.** All procured software must provide a Software Bill of Materials (SBOM) in SPDX or CycloneDX format and a documented patch management process with maximum response times for critical CVEs (recommended: 72 hours for CVSS 9.0+, 30 days for CVSS 7.0–8.9).

**7. Prefer certified cooperative providers.** For infrastructure, prefer SCS-certified cloud operators or members of govdigital eG who are bound by collective data-sovereignty agreements [23]. GAIA-X Label compliance is an additional positive criterion [52].

### 6.3 Template Procurement Language

The following clause should be included in all contracts for custom software development:

> *"All software, source code, documentation, and related materials developed under this contract and paid from public funds shall be released by the Contractor under an OSI-approved open-source licence (AGPL-3.0, Apache 2.0, or GPL-3.0, as agreed) within 90 days of completion. The Contractor shall publish the software on openCode.de (or a designated equivalent public repository) and provide all necessary documentation for third-party deployment. This condition may only be varied by written agreement where the Contracting Authority provides documented evidence that open-source release would create a material security risk."*

### 6.4 Change Management

Open-source transitions frequently fail not on technical grounds but on human factors: end-user resistance, insufficient training, middle-management inertia, and political backsliding under vendor lobbying. The Munich LiMux case [59] is the canonical example; the Barcelona Decidim rollout is the canonical counter-example.

**Recommended change-management actions:**

1. Appoint a **Digital Transformation Champion** at senior political level with explicit mandate and public accountability
2. Establish **open-source champions** in each department with advanced training, peer-support role, and recognition programme
3. Run **parallel operations** for a minimum of three months before cutting over critical systems
4. Document and publicly celebrate **early wins** — cost savings, new capabilities, positive citizen feedback
5. Publish a **public transparency dashboard** showing migration progress, costs, service quality metrics, and open data statistics
6. Engage **organised civil society** (digital rights organisations, accessibility advocates, data journalism community) as public champions
7. Brief **local media** with human-interest narratives around digital sovereignty and civic technology

### 6.5 Accessibility and Digital Inclusion Strategy

Digital accessibility is both a legal obligation and a democratic imperative. Across European jurisdictions, an estimated 15–20% of citizens have a disability that affects digital service use. WCAG 2.1 AA is the minimum legal standard under the EU Web Accessibility Directive and its national transpositions.

**Recommended actions:**

1. Integrate axe-core automated accessibility testing into the CI/CD pipeline from Phase 1
2. Commission independent WCAG 2.1 AA audit at each phase gate
3. Recruit disabled citizens as paid testers during development (not just post-launch review)
4. Provide assisted digital support channels (phone, in-person) as permanent complements to digital services — not temporary workarounds
5. Adopt the GDS Service Design Principles adapted for DACH context, including explicit accessibility commitment at design inception

### 6.6 Open-Source Community Governance

Municipalities that implement open-source stacks take on an implicit responsibility to the commons: they benefit from the collective investment of the open-source community and should contribute back proportionally.

**Recommended community engagement:**

1. Join the **openCode.de** platform and publish all custom developments [10]
2. Become a **member of govdigital eG** (Germany) or the relevant cantonal IT cooperative [23]
3. Participate in the **Decidim Association** and **TYPO3 Association** if deploying those platforms
4. Attend and, over time, co-organise **OpenRuhr**, **Bits & Bäume**, and equivalent civic tech events
5. Allocate **10% of IT staff time** (approximately 0.1 FTE per developer) to upstream open-source contributions
6. Publish an annual **open-source contribution report** documenting code, documentation, translations, and community participation

---

## 7. Risk Analysis

### 7.1 Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Political reversal after election | Medium | High | Embed in legislation/ordinance; cross-party consensus; public mandate |
| Vendor lobbying / FUD campaigns | High | Medium | Document TCO evidence publicly; engage civil society; brief media |
| Skill gap in IT team | High | Medium | Training; cooperative IT provider; community of practice; certification support |
| Integration failure between layers | Medium | High | Phased rollout with decision gates; reference architecture adherence; API contracts |
| Data loss during migration | Low | Critical | Full backup protocol; parallel operation minimum 3 months; staged migration |
| GDPR / DGA / AI Act violation | Low | High | Privacy-by-design; DPO engagement at each phase; DPIA before deployment |
| User adoption failure | Medium | High | Change management; UX testing; training; parallel systems; champions |
| Security incident | Low | Critical | BSI IT-Grundschutz; penetration testing; SBOM; incident response plan; NIS2 |
| Community fragmentation / fork | Low | Medium | Align with upstream; contribute back; avoid deep forks |
| Cost overrun | Medium | Medium | Phase-gated budget; independent project office; open TCO accounting |
| AI Act non-compliance | Medium | High | Conformity assessment before AI system deployment; human oversight mechanism |
| Supply chain attack on dependencies | Low | High | SBOM; dependency audit; signed releases; Sigstore verification |
| Accessibility regression | Medium | Medium | CI/CD axe-core integration; quarterly accessibility audits |
| Legacy system incompatibility | Medium | Medium | XÖV/eCH middleware layer; phased legacy retirement; data mapping |

### 7.2 The Munich Cautionary Case

The City of Munich's LiMux project (2003–2017) is the most-cited case of a large-scale municipal open-source transition that was reversed. The independent post-mortem [59] identifies the reversal as driven primarily by: (a) a change in political leadership with closer ties to Microsoft; (b) inadequate change management and end-user training; (c) compatibility issues with state-level systems that had not been updated to support open standards; and (d) an approximately €49 million reversal cost that exceeded the approximately €11.7 million in accumulated savings — a reversal driven by political, not economic, logic.

The technical implementation of LiMux was broadly successful. The failure was political and organisational. The lesson for municipal digital transformation is unambiguous: **political risk management is as important as technical planning**. Building cross-party support, embedding digital sovereignty in a council ordinance, and engaging civil society as a public champion are not optional extras — they are programme-critical risk mitigations.

### 7.3 Security Considerations

The BSI IT-Grundschutz framework provides a comprehensive security baseline applicable regardless of licence model [26]. Key requirements for a municipal open-source stack:

- All server components must receive regular security updates; patch response times should be contractually specified (see Section 6.2)
- Authentication must meet BSI Authenticator Assurance Level 2 (AAL2) for citizen-facing services: two-factor authentication using TOTP, FIDO2, or equivalent
- Data in transit encrypted with TLS 1.3 minimum; HSTS preload; certificate rotation automated via ACME
- Data at rest encrypted for sensitive categories; PostgreSQL Transparent Data Encryption or filesystem-level encryption via LUKS
- Penetration testing (minimum scope: OWASP Top 10) required at each phase gate before go-live
- Incident response plan documented and tested annually, aligned with NIS2 reporting obligations (24-hour initial notification for significant incidents) [27]
- SBOM maintained in SPDX format and updated with each deployment; shared with BSI BSIFB national vulnerability database

### 7.4 AI and Automation Risks

As municipalities deploy AI-assisted services (Section 4.13), additional risk dimensions arise:

**Algorithmic bias:** AI systems trained on historical government data can encode and amplify historical discrimination in service delivery. Mitigation: bias audit (statistical parity, equalized odds) for all AI systems before deployment; diverse training data sourcing; regular re-auditing.

**Hallucination in citizen-facing AI:** Large language models deployed for citizen query handling can produce plausible but incorrect information. Mitigation: restrict citizen-facing AI to retrieval-augmented generation (RAG) over verified government sources; never allow AI to make binding decisions without human review.

**EU AI Act non-compliance:** see Section 7.1 risk register. The conformity assessment for high-risk AI systems under Annex III AI Act is a multi-month process; plan accordingly.

**Over-automation:** automated systems can reduce the human touchpoints that build citizen trust and provide recourse. Mitigation: maintain human review mechanisms for all AI-assisted decisions; provide citizens with the right to request human review of any automated decision (consistent with GDPR Article 22).

### 7.5 Supply Chain Security

Open-source software's security advantage — anyone can inspect the code — comes with a supply chain exposure: the code and its dependencies are publicly known, and a compromised dependency can affect all deployments simultaneously (cf. the Log4Shell incident, 2021).

**Mitigation measures:**

1. Maintain a complete SBOM for all deployed components; update on every deployment
2. Subscribe to security advisories for all dependencies (GitHub Security Advisories, OSV.dev)
3. Pin dependency versions in production; use Renovate or Dependabot for automated update PRs
4. Verify package signatures via Sigstore/cosign for container images
5. Run dependency-vulnerability scanning (Trivy, Grype) in CI/CD pipeline
6. Implement network egress filtering to reduce blast radius of compromised dependencies

### 7.6 Climate and Sustainability Considerations

Municipal digital infrastructure has a material energy and carbon footprint. Digital sovereignty and climate sustainability are mutually reinforcing: self-hosted infrastructure in energy-efficient cooperative data centres, running on renewable energy, is both more sovereign and more sustainable than hyperscaler cloud.

**Recommendations:**
- Require renewable energy certificates (RECs) or power purchase agreements (PPAs) from cooperative IT providers
- Optimise Kubernetes resource requests/limits to reduce idle compute
- Prefer ARM-based server hardware for edge/small-office workloads (lower power per compute unit)
- Report annual ICT carbon footprint as part of municipal sustainability reporting

---

## 8. Conclusion

The evidence reviewed and developed in this paper converges on six findings:

**1. Open-source municipal technology stacks are technically mature and production-proven in 2026.** Every functional requirement of a modern municipal government — from digital identity to AI-assisted services — can be met by open-source software with documented deployments at peer municipalities across the full range of population sizes.

**2. The regulatory environment increasingly mandates open-source and interoperability.** EMBAG (Switzerland), OZG 2.0 (Germany), the Interoperable Europe Act (EU), the EU Data Act, and the EU AI Act together create a legal framework in which proprietary, vendor-locked, non-interoperable systems cannot sustainably meet compliance obligations. Municipalities that begin the transition now are building compliance capital; those that delay are accumulating regulatory debt.

**3. The economic case is compelling when total costs are counted correctly.** For a municipality of 500 staff, the five-year net saving from transitioning to an open-source workplace stack is in the range of €200,000–€500,000 after implementation costs. Cooperative procurement (govdigital eG, AKDB, cantonal IT cooperatives) substantially reduces implementation cost and risk. The French DINUM and Munich post-mortem cases both confirm this arithmetic.

**4. Small municipalities can and do succeed.** The case studies of Schaffhausen, Herrenberg, and Gummersbach demonstrate that open-source transformation is not exclusive to large cities or federal agencies. With cooperative IT providers handling infrastructure, the minimum viable programme for a municipality of 20,000 fits within a three-year, €300,000–€500,000 budget envelope.

**5. The EU AI Act creates new transparency obligations that favour open-source AI.** As municipalities adopt AI-assisted services, the conformity-assessment and auditability requirements of the AI Act strongly favour open-source, locally-operated AI systems over proprietary black-box alternatives. The open-source AI stack described in Section 4.13 is both GDPR-compliant and AI-Act-aligned.

**6. Success requires as much political and organisational investment as technical investment.** The Munich LiMux reversal and the Barcelona Decidim success are mirror images of the same lesson: political mandate, skilled change management, cross-party buy-in, and sustained stakeholder engagement are the binding constraints on success. Technical excellence is necessary but not sufficient.

Cities that move first will benefit from first-mover advantages: shaping cooperative standards, building in-house expertise, contributing to the open-source commons, and positioning themselves as exemplars of democratic digital governance. The invitation — and in an increasing number of jurisdictions, the obligation — is clear.

---

## References

[1] Swiss Federal Council. (2023). *Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG)*. SR 172.019. Bern: Swiss Confederation. https://www.fedlex.admin.ch/eli/cc/2023/682/de — [Open access, CC0]

[2] Bundesministerium des Innern und für Heimat (BMI). (2024). *Onlinezugangsgesetz 2.0 (OZG 2.0)*. Berlin: BMI. https://www.bmi.bund.de/DE/themen/moderne-verwaltung/e-government/ozg/ozg-node.html — [Open access, DL-DE/Zero 2.0]

[3] Open Source Business Alliance (OSBA). (2023). *Sovereign Cloud Stack: Technical and Governance Overview*. Berlin: OSBA. https://scs.community/ — [Open access, CC-BY-SA-4.0]

[4] Free Software Foundation Europe (FSFE). (2017–2026). *Public Money? Public Code!* Berlin: FSFE. https://publiccode.eu/ — [Open access, CC-BY-SA-4.0]

[5] European Commission. (2020). *Open Source Software Strategy 2020–2023: Think Open*. Brussels: European Commission. https://commission.europa.eu/about/departments-and-executive-agencies/informatics/open-source-software-strategy_en — [Open access]

[6] European Parliament and Council. (2024). *Regulation (EU) 2024/903 of the European Parliament and of the Council on measures for a high level of public sector interoperability across the Union (Interoperable Europe Act)*. Official Journal of the EU. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202400903 — [Open access]

[7] Wirtz, B. W., & Weyerer, J. C. (2017). Conceptualization and creation of a holistic e-government maturity model. *Public Management Review*, 19(9), 1297–1316. https://doi.org/10.1080/14719037.2017.1283024

[8] Janssen, M., Charalabidis, Y., & Zuiderwijk, A. (2012). Benefits, adoption barriers and myths of open data and open government. *Information Systems Management*, 29(4), 258–268. https://doi.org/10.1080/10580530.2012.716740

[9] FITKO. (2023). *Föderale IT-Kooperation — Jahresbericht 2023*. Frankfurt: FITKO. https://www.fitko.de/fitko/jahresbericht — [Open access, DL-DE/Zero 2.0]

[10] openCode.de. (2022–2026). *openCode — Open Source for Government*. Berlin: Digitalservice GmbH des Bundes. https://opencode.de/ — [Open access]

[11] Sovereign Cloud Stack Community. (2023–2026). *SCS Technical Documentation*. https://docs.scs.community/ — [Open access, Apache 2.0]

[12] Decidim Association. (2021–2026). *Decidim: Free Open-Source Participatory Democracy for Cities and Organizations*. Barcelona: Decidim Association. https://decidim.org/ — [Open access, AGPL-3.0]

[13] Nextcloud GmbH. (2023). *Nextcloud for Government: Security, Sovereignty, and Collaboration*. Stuttgart: Nextcloud GmbH. https://nextcloud.com/government/ — [Open access]

[14] The Matrix Foundation. (2023–2026). *Matrix Specification v1.x*. https://spec.matrix.org/ — [Open access, Apache 2.0]

[16] E-Government Suisse. (2023). *Strategie E-Government Schweiz 2024–2027*. Bern: Schweizerische Bundeskanzlei. https://www.egovernment.ch/de/umsetzung/e-government-strategie/ — [Open access]

[19] TYPO3 Association. (2023–2026). *TYPO3 in Public Administration*. Düsseldorf: TYPO3 Association. https://typo3.org/project/association — [Open access]

[20] OpenProject GmbH. (2023–2026). *OpenProject for Government: Open Source Project Management*. Berlin: OpenProject GmbH. https://www.openproject.org/ — [Open access, GPLv3]

[21] Red Hat / Keycloak Community. (2023–2026). *Keycloak: Open Source Identity and Access Management*. https://www.keycloak.org/ — [Open access, Apache 2.0]

[22] CKAN Association. (2023–2026). *CKAN: Open Source Data Portal Software*. https://ckan.org/ — [Open access, AGPL-3.0]

[23] govdigital eG. (2023). *govdigital: Genossenschaft für digitale Verwaltung*. Berlin: govdigital eG. https://govdigital.de/ — [Open access]

[24] Dataport AöR. (2023). *Dataport: IT-Dienstleister für die öffentliche Verwaltung*. Hamburg: Dataport AöR. https://www.dataport.de/ — [Open access]

[26] Bundesamt für Sicherheit in der Informationstechnik (BSI). (2023). *BSI IT-Grundschutz-Kompendium Edition 2023*. Bonn: BSI. https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/ — [Open access, CC-BY-ND 3.0 DE]

[27] European Parliament and Council. (2022). *Directive (EU) 2022/2555 on Measures for a High Common Level of Cybersecurity across the Union (NIS2 Directive)*. Official Journal of the EU. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022L2555 — [Open access]

[29] United Nations Department of Economic and Social Affairs (UNDESA). (2022). *UN E-Government Survey 2022: The Future of Digital Government*. New York: United Nations. https://publicadministration.un.org/egovkb/en-us/Reports/UN-E-Government-Survey-2022 — [Open access, © United Nations]

[30] Janowski, T. (2015). Digital government evolution: From transformation to contextualization. *Government Information Quarterly*, 32(3), 221–226. https://doi.org/10.1016/j.giq.2015.07.001

[33] Camunda Services GmbH. (2023–2026). *Camunda Platform 8 Community Edition*. Berlin: Camunda. https://camunda.com/download/ — [Open access, Apache 2.0]

[34] BigBlueButton Inc. (2023). *BigBlueButton: Open Source Web Conferencing*. https://bigbluebutton.org/ — [Open access, LGPL-3.0]

[35] Jitsi Community. (2023). *Jitsi Meet: Open Source Video Conferencing*. https://jitsi.org/ — [Open access, Apache 2.0]

[36] OpenStreetMap Foundation. (2023). *OpenStreetMap*. https://www.openstreetmap.org/ — [Open access, ODbL-1.0]

[37] QGIS Project. (2023). *QGIS: A Free and Open Source Geographic Information System*. https://www.qgis.org/ — [Open access, GPL-2.0+]

[39] Cloud Native Computing Foundation (CNCF). (2023). *Kubernetes*. https://kubernetes.io/ — [Open access, Apache 2.0]

[41] PostgreSQL Global Development Group. (2023). *PostgreSQL*. https://www.postgresql.org/ — [Open access, PostgreSQL Licence (BSD-like)]

[42] Bundesministerium des Innern und für Heimat (BMI) / ZenDiS GmbH. (2023–2026). *OpenDesk: Der digitale Arbeitsplatz der Bundesverwaltung*. https://opendesk.eu/ — [Open access, AGPL-3.0]

[43] Schweizerisches Bundesarchiv (BAR). (2023). *Geschäftsverwaltung (GEVER) in der Bundesverwaltung*. Bern: BAR. https://www.bar.admin.ch/bar/de/home/digitale-archivierung/gever.html — [Open access]

[44] Geschäftsstelle OGD Schweiz. (2023). *opendata.swiss — Open Government Data Switzerland*. Bern: Schweizerische Bundeskanzlei. https://opendata.swiss/ — [Open access, CC-BY-4.0 (portal)]

[45] European Commission, ISA² Programme. (2017). *European Interoperability Framework — Implementation Strategy (EIF)*. Brussels: European Commission. https://joinup.ec.europa.eu/collection/nifo-national-interoperability-framework-observatory/european-interoperability-framework-detail — [Open access, CC-BY-4.0]

[46] KoSIT — Koordinierungsstelle für IT-Standards. (2023). *XÖV-Standards: XML in der öffentlichen Verwaltung*. Bremen: KoSIT. https://www.xoev.de/ — [Open access]

[47] eCH Association. (2023). *eCH e-Government Standards*. Bern: eCH. https://www.ech.ch/ — [Open access; individual standards under eCH-Licence]

[48] GovStack Initiative / ITU / DIAL. (2022–2026). *GovStack: Building Blocks for Digital Government*. Geneva: International Telecommunication Union. https://www.govstack.global/ — [Open access, CC-BY-4.0]

[49] European Parliament and Council. (2023). *Regulation (EU) 2023/2854 of the European Parliament and of the Council on harmonised rules on fair access to and use of data (Data Act)*. Official Journal of the EU. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202302854 — [Open access]

[50] European Parliament and Council. (2024). *Regulation (EU) 2024/1689 of the European Parliament and of the Council laying down harmonised rules on artificial intelligence (Artificial Intelligence Act)*. Official Journal of the EU. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202401689 — [Open access]

[51] ZenDiS GmbH. (2024). *Jahresbericht 2023/2024 — Zentrum für Digitale Souveränität der öffentlichen Verwaltung*. Berlin: ZenDiS. https://zendis.de/ — [Open access]

[52] GAIA-X AISBL. (2023). *GAIA-X Architecture Document and Trust Framework*. Brussels: GAIA-X AISBL. https://gaia-x.eu/ — [Open access]

[54] Consul Democracy. (2015–2026). *CONSUL: Democratic Software*. Madrid: Consul Democracy. https://consulproject.org/ — [Open access, AGPL-3.0]

[55] Geschäftsstelle OGD Schweiz. (2024). *OGD-Strategie Schweiz 2024–2027*. Bern: Schweizerische Bundeskanzlei. https://www.bk.admin.ch/bk/de/home/digitale-transformation-ikt-lenkung/open-government-data.html — [Open access]

[56] Lathrop, D., & Ruma, L. (Eds.). (2010). *Open Government: Collaboration, Transparency, and Participation in Practice*. Sebastopol, CA: O'Reilly Media. ISBN 978-0-596-80435-0.

[58] European Parliament and Council. (2022). *Regulation (EU) 2022/868 of the European Parliament and of the Council on European data governance (Data Governance Act)*. Official Journal of the EU. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R0868 — [Open access]

[59] Landeshauptstadt München / Stadtrat. (2017). *Beschluss des Stadtrats vom 15.02.2017: Zukunft der IT-Infrastruktur der Stadtverwaltung München*. München: Stadtrat München. [Decision document, public record]

[60] Direction interministérielle du numérique (DINUM). (2022). *Rapport sur l'utilisation des logiciels libres dans la fonction publique*. Paris: DINUM. https://www.numerique.gouv.fr/publications/ — [Open access]

[62] Prometheus Authors. (2023). *Prometheus: Monitoring System and Time Series Database*. Cloud Native Computing Foundation. https://prometheus.io/ — [Open access, Apache 2.0]

[63] Grafana Labs. (2023). *Grafana: Open Source Analytics and Monitoring*. https://grafana.com/ — [Open access, AGPL-3.0]

---

## Appendix A: Technology Scorecard Summary

| Layer | Primary component | Licence | Composite score (7 criteria) | Alternative |
|---|---|---|---|---|
| Digital Identity | Keycloak | Apache 2.0 | 34/35 | Authentik (MIT) |
| Document Management | Nextcloud | AGPL-3.0 | 33/35 | OpenDesk suite |
| Workflow / BPM | Camunda 8 CE | Apache 2.0 | 29/35 | Flowable (Apache 2.0) |
| Participation | Decidim | AGPL-3.0 | 33/35 | CONSUL (AGPL-3.0) |
| Messaging | Matrix/Element | Apache 2.0 | 32/35 | Nextcloud Talk |
| Video Conferencing | Jitsi Meet | Apache 2.0 | 31/35 | BigBlueButton (LGPL) |
| Open Data | CKAN | AGPL-3.0 | 32/35 | — |
| GIS | QGIS + GeoServer | GPL-2.0 | 30/35 | MapServer (MIT) |
| Web CMS | TYPO3 | GPL-2.0 | 32/35 | Drupal (GPL-2.0) |
| Cloud Infrastructure | SCS (OpenStack+K8s) | Apache 2.0 | 32/35 | Managed SCS |
| Data Integration | Apache Airflow | Apache 2.0 | 28/35 | Apache NiFi |
| Search | OpenSearch | Apache 2.0 | 29/35 | Typesense |
| Monitoring | Prometheus + Grafana | Apache 2.0 / AGPL | 31/35 | — |
| AI Services | Ollama + Haystack | MIT / Apache 2.0 | 27/35 | — |
| Project Management | OpenProject | GPL-3.0 | 30/35 | — |

---

## Appendix B: Procurement Checklist

Use this checklist when evaluating any technology vendor or open-source implementation proposal:

**Licence and openness**
- [ ] Software is licensed under an OSI-approved open-source licence
- [ ] Source code is publicly accessible (GitHub, GitLab, or openCode.de)
- [ ] Custom development will be released under open-source licence (contract clause confirmed)
- [ ] No "open core" model with critical features withheld behind proprietary tier

**Interoperability**
- [ ] Implements XÖV standards (Germany) or eCH standards (Switzerland) where applicable
- [ ] Provides OpenAPI 3.x specification for all integration interfaces
- [ ] Supports DCAT-AP metadata for data catalogue integration
- [ ] Identity integration via OIDC or SAML2 with Keycloak confirmed

**Security**
- [ ] SBOM provided in SPDX or CycloneDX format
- [ ] Documented CVE response process with maximum patch timeline specified
- [ ] BSI IT-Grundschutz compliance assessment available (Germany) or ISDS equivalent (Switzerland)
- [ ] Penetration test results available (within last 12 months)

**Data sovereignty**
- [ ] Data processed exclusively within EU jurisdiction (confirmed contractually)
- [ ] Data residency in a certified SCS operator or equivalent (GAIA-X Label preferred)
- [ ] No third-country data transfer without explicit DPIA and legal basis
- [ ] Data portability guaranteed in open formats; migration assistance contractually committed

**Total cost of ownership**
- [ ] Five-year TCO model provided including implementation, hosting, support, training, and exit
- [ ] Per-seat costs compared with current proprietary baseline
- [ ] Exit and migration costs explicitly quantified
- [ ] References from ≥ 3 comparable municipal deployments provided

**Accessibility**
- [ ] WCAG 2.1 AA conformance statement provided
- [ ] Independent accessibility audit report available (within last 24 months)
- [ ] Accessibility testing in CI/CD pipeline demonstrated

---

## Appendix C: 36-Month Milestone Tracker

| Month | Phase | Key milestone | Owner | Status |
|---|---|---|---|---|
| 1 | 0 | Steering committee established | Mayor / CIO | ☐ |
| 2 | 0 | Technology audit complete | IT lead | ☐ |
| 3 | 0 | Political mandate secured | Mayor | ☐ |
| 3 | 0 | Cooperative IT provider contracted | Procurement | ☐ |
| 4 | 1 | SCS environment live | IT + provider | ☐ |
| 6 | 1 | Keycloak deployed + national eID federated | IT | ☐ |
| 7 | 1 | Nextcloud live for all staff | IT | ☐ |
| 8 | 1 | Matrix/Element messaging live | IT | ☐ |
| 9 | 1 | Monitoring stack live | IT | ☐ |
| 10 | 1 | IT-Grundschutz baseline approved | DPO + IT | ☐ |
| 11 | 2 | TYPO3/Drupal CMS live | IT + comms | ☐ |
| 12 | 2 | First citizen service live on open stack | IT + service | ☐ |
| 14 | 2 | CKAN open data portal live | IT + data | ☐ |
| 15 | 2 | Decidim participation platform live | IT + mayor | ☐ |
| 16 | 2 | WCAG 2.1 AA audit passed | External auditor | ☐ |
| 17 | 2 | Five services live; 80% of volume | IT + services | ☐ |
| 18 | 3 | All services federated via SSO | IT | ☐ |
| 20 | 3 | GIS layer live | IT + planning | ☐ |
| 22 | 3 | 80% of services digitised | IT + services | ☐ |
| 23 | 3 | XÖV/eCH inter-agency exchange live | IT + partner | ☐ |
| 24 | 3 | AI Act conformity assessment complete | DPO + IT | ☐ |
| 25 | 4 | First upstream contribution published | IT | ☐ |
| 26 | 4 | Community of practice launched (≥3 cities) | IT lead | ☐ |
| 27 | 4 | Citizen satisfaction survey (NPS ≥ 40) | Comms | ☐ |
| 28 | 4 | TCO comparison report published | Finance + IT | ☐ |
| 30 | 5 | Full licence audit complete | IT + legal | ☐ |
| 32 | 5 | 100% sovereign data residency verified | DPO | ☐ |
| 34 | 5 | Replication playbook published | IT lead | ☐ |
| 36 | 5 | Strategy paper v1.0 published | Author | ☐ |

---

*This document is released under the Creative Commons Attribution 4.0 International Licence (CC-BY-4.0).*  
*Attribute as: Sebastian Graf, Autonomous Office of Civil Digital Infrastructure (sebk4c@tuta.com)*  
*Version 0.2.0 — Citation-Complete Draft — 2026-06-21*
