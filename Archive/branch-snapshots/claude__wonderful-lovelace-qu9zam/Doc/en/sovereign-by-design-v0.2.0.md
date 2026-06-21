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
  - Deutschland-Stack
  - OpenDesk
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

Municipal governments are the closest layer of democratic administration to citizens, yet they face an acute structural tension: the digital tools they depend on are increasingly proprietary, vendor-locked, and misaligned with public-interest values. This paper presents a comprehensive strategy for implementing a state-of-the-art, open-source governmental administration technology stack in city governments. Drawing on exemplary practices from the Swiss federal administration's EMBAG legislation (SR 172.019, in force 2024), Germany's OZG 2.0 reform programme, the Sovereign Cloud Stack (SCS), ZenDiS and OpenDesk initiatives, and the wider European sovereign technology community, we derive a first-principles implementation roadmap, stakeholder engagement framework, and procurement strategy. We evaluate ten core technology components — identity management, document management, workflow automation, citizen participation, secure communications, open data publication, geographic information, web publishing, code hosting, and cloud infrastructure — against criteria of digital sovereignty, interoperability, total cost of ownership, and civic alignment. Economic evidence from the Schleswig-Holstein Linux migration (30,000 seats), the Munich LiMux post-mortem, and the EU's finding that every €1 invested in open source generates at least €4 in economic value confirms the fiscal case. The EU Interoperable Europe Act (Regulation (EU) 2024/903, in force April 2024) and Germany's NIS2 Implementation Act (in force December 2025) create binding legal obligations that proprietary stacks cannot sustainably satisfy. The paper provides a phased 36-month implementation roadmap with concrete procurement guidance and EU funding pathways for all relevant stakeholders.

**Keywords:** digital sovereignty, open source government, GovTech, municipal digital transformation, interoperability, OZG 2.0, EMBAG, Sovereign Cloud Stack, OpenDesk, Deutschland-Stack, e-government, civic technology

---

## 1. Introduction

The digital transformation of municipal government is no longer optional. Citizens expect seamless, secure, and accessible digital services; regulators demand interoperability and data protection; and fiscal pressures require sustainable, cost-effective technology investments. Yet the majority of city governments remain trapped in a cycle of proprietary vendor dependency, expensive licence agreements, and fragmented systems that impede rather than enable good governance [1, 29].

The consequences are well-documented: vendor lock-in raises switching costs and bargaining asymmetry [4]; proprietary formats obstruct cross-agency data exchange and transparency [45]; closed-source infrastructure prevents independent security auditing [26]; and recurring licence fees drain budgets that could fund service delivery [3, 5]. Most fundamentally, when the software running democratic institutions is owned by private actors, a structural conflict of interest emerges between the public interest and corporate imperatives [4].

A different path is both possible and proven. Switzerland's EMBAG legislation (SR 172.019, in force January 2024) mandates that federal software developed with public funds be released as open source by default [1]. Germany's OZG 2.0 reform (in force July 2024) requires that public administrators prioritise open-source solutions in procurement [2]. Germany's Sovereign Cloud Stack reached Release 8 in April 2025 [55], and the OpenDesk office suite — managed by ZenDiS GmbH — surpassed 100,000 users including the Bundeswehr IT provider BWI and several Länder administrations [42, 50]. The state of Schleswig-Holstein is migrating 30,000 workplaces to Linux, LibreOffice, Nextcloud, and open standards [51]. The EU Interoperable Europe Act (April 2024) creates binding cross-border interoperability obligations [6].

Meanwhile, the economic evidence is compelling: the EU calculates that every €1 invested in open source generates at least €4 in economic value across Europe through reuse, reduced duplication, and innovation [62]. The return to Windows after Munich's LiMux project cost an estimated €100 million [56] — a figure that concentrates the mind when evaluating the cost of inaction.

This paper synthesises these developments into a practical strategy for municipal governments. It is addressed to all relevant stakeholders — city administrators, elected officials, public-sector IT teams, procurement offices, civil-society groups, open-source communities, and sovereign technology providers — and provides the evidence base, technology assessment, implementation roadmap, and EU funding pathways needed to make the transition.

### 1.1 Scope and Definitions

*Municipal government* refers to city and local government authorities, including Gemeinden, Kommunen, Städte, and equivalent structures in Swiss cantons. The strategy scales from small municipalities (population 5,000–50,000) to large cities (population 500,000+), with appropriate modulation.

*Open-source technology stack* refers to software components licensed under OSI-approved licences, deployed on infrastructure that the municipality controls or can migrate away from without undue cost or friction.

*Digital sovereignty* is the ability of a government to make independent decisions about its digital infrastructure, including the right to inspect, modify, audit, and migrate software without dependency on a single vendor [3]. In the European context, digital sovereignty has become a policy imperative endorsed by the European Commission, the German Federal Government, and the Swiss Federal Council alike.

### 1.2 Research Questions

1. What does a state-of-the-art open-source municipal technology stack look like in 2026?
2. What lessons can be drawn from the Swiss, German, and European sovereign technology communities?
3. What is the optimal phased implementation pathway for a city government of 50,000–500,000 population?
4. How should procurement, stakeholder engagement, risk management, and EU funding access be structured to maximise success probability?

---

## 2. Methodology

This paper employs a multi-method research design combining:

**Systematic literature review** of peer-reviewed publications, grey literature, and policy documents published between 2010 and 2026, covering e-government theory, digital sovereignty, open-source software in public administration, and municipal digital transformation.

**Comparative policy analysis** of technology legislation and strategies from Switzerland (EMBAG 2023, E-Government Strategy 2024–2027, eCH standards), Germany (OZG 2.0 2024, Deutsche Verwaltungscloud-Strategie, Deutschland-Stack 2025), and the European Union (Interoperable Europe Act 2024, AI Act 2024, NIS2 2022/2025, Digital Europe Programme 2021–2027).

**Technology stack evaluation** using a structured scoring matrix assessing each component on: (a) licence openness, (b) deployment maturity, (c) community health, (d) interoperability standards compliance, (e) security posture, (f) total cost of ownership, and (g) existing public-sector deployments.

**Economic analysis** drawing on published cost data from Munich (LiMux), Schleswig-Holstein, and EU-level open-source economic impact assessments.

**Stakeholder analysis** mapping the interests, influence, and engagement needs of each stakeholder group in the municipal digital transformation process.

The literature review is designed to be self-improving: the source registry (`Mem/source-registry.md`) and literature review state (`Mem/literature-review-state.md`) are versioned documents updated on a recurring basis. The `Scripts/update_literature_review.py` script provides structured prompts for reviewing and improving these files on a quarterly cadence.

### 2.1 Inclusion Criteria

Sources were included if they: (a) address open-source software in public administration; (b) cover governmental digital transformation strategy; (c) relate to the European, Swiss, or German regulatory context; or (d) provide primary data on municipal technology implementations. Sources published before 2010 were included only where they establish foundational theoretical frameworks.

### 2.2 Limitations

This is a citation-complete draft (v0.2.0). All citations have been verified against primary sources or clearly marked where verification remains outstanding. Technology stack assessments reflect publicly available information as of June 2026. Implementation cost estimates are indicative and must be validated against local procurement conditions. The literature on long-term open-source TCO in small municipalities remains sparse; this gap is documented in the literature review state.

---

## 3. Literature Review

### 3.1 Theoretical Foundations of E-Government

The academic literature on e-government has evolved through four broad phases [30]. First-generation e-government (1995–2005) focused on digitising existing processes and creating government websites [29]. Second-generation e-government (2005–2012) emphasised online service delivery, citizen portals, and back-office integration [7]. Third-generation e-government (2012–2020) introduced open data, participatory platforms, and mobile-first service design [8]. The current fourth generation (2020–present) is characterised by platform government, digital identity infrastructure, data spaces, and the sovereignty turn — a recognition that digital autonomy is a prerequisite for democratic self-governance [45].

Wirtz and Weyerer's holistic e-government maturity model identifies five dimensions: technical infrastructure, process quality, service quality, citizen orientation, and transparency [7]. Municipal governments in Switzerland and Germany score variably across these dimensions; technical infrastructure and process quality lag citizen expectations in most jurisdictions, while the regulatory environment increasingly mandates transparency and interoperability [1, 2, 45].

The GovStack initiative, a joint effort of the International Telecommunication Union (ITU) and the Digital Impact Alliance (DIAL), provides a building-block framework for digital government that maps closely to the open-source stack presented in Section 4 [53]. GovStack's specification for cloud infrastructure building blocks has been formally integrated with the Sovereign Cloud Stack community [55], providing a globally interoperable reference for municipal implementation.

### 3.2 Digital Sovereignty in Public Administration

The concept of digital sovereignty has moved from academic concept to policy imperative [3, 5]. The EU Open Source Strategy 2020–2023 established "sharing and reuse" as a core principle, mandating that European institutions prefer open-source solutions in technology procurement [5]. The 2024 Interoperable Europe Act (Regulation (EU) 2024/903), which entered into force on 11 April 2024 with substantive obligations applying from 12 January 2025, creates binding obligations for cross-border interoperability in public administrations and explicitly supports free and open-source software as a vehicle for achieving it [6]. The European Parliament and Council have earmarked €77 million in the Digital Europe Work Programme 2025–2027 to support implementation [6, 62].

The **Sovereign Tech Fund** (Sovereign Tech Fund GmbH), a German federal government initiative, has by late 2024 invested approximately €23.5 million in over 60 critical open-source projects, with an annual budget of €17 million [49]. This mechanism demonstrates that government can act not only as a consumer of open source but as a strategic funder of the digital commons it depends on.

Germany's **Sovereign Cloud Stack (SCS)**, developed by the Open Source Business Alliance (OSBA) and originally co-funded by the German Federal Ministry for Economic Affairs and Climate Action (BMWK), reached Release 8 on April 9, 2025 [55]. Although BMWK project funding concluded in December 2024, engaged companies and organisations continue maintenance and evolution of SCS standards. More than half a dozen providers — including ScaleUp Technologies (the newest operator as of R8), plusserver, and OSISM — operate production clouds using SCS, providing municipalities with certified sovereign infrastructure options [55].

The **AI Act** (Regulation (EU) 2024/1689, in force August 2024) and **NIS2 Directive** transposition create new obligations for public administrations deploying AI and critical digital infrastructure. AI systems used in public administration for citizen-facing decisions are classified as high-risk, requiring conformity assessments, explainability, and human oversight [64]. Open-source AI components may satisfy these requirements more readily than opaque proprietary systems, since source code inspection is a precondition for meaningful conformity assessment. Germany's NIS2 Implementation Act entered into force on 5 December 2025, making IT-Grundschutz-based risk management mandatory for federal agencies and publicly organised IT service providers [57].

### 3.3 The German OZG Ecosystem

The Onlinezugangsgesetz (OZG), enacted in 2017 and substantially reformed in 2024 (OZG 2.0), requires all German federal, Land, and municipal administrations to digitise their administrative services [2]. OZG 2.0 (in force July 24, 2024) introduces a legal entitlement for citizens to receive digital administrative services from 2029, strengthens open standards requirements, and mandates that federal and state administrators "prioritise open-source solutions and open standards when providing IT components" and that federal authorities "prioritise open source software over proprietary solutions during procurement" [2, 47].

Progress under the original OZG has been slower than anticipated: by the end of 2023, only 81 out of 581 designated services had been fully digitised [2]. OZG 2.0 responds to this by strengthening monitoring mechanisms (an independent scientific evaluation every three years) and introducing the "DeutschlandID" as a nationwide digital identity built on BundID and eID [2].

The **openCode.de** platform, managed by Digitalservice GmbH des Bundes, provides the central repository for government open-source software in Germany, now hosting hundreds of repositories [10]. The **Deutsche Verwaltungscloud (DVC)** was symbolically launched at the IT Planning Council's expert conference in March 2025, enabling applications to run across cloud locations and be shared nationally via openCode.de [2, 23].

The **Deutschland-Stack**, emerging from the 2025 German coalition agreement, sets out Germany's national vision for digital sovereignty with a target of full rollout by 2028. It frames openDesk, Sovereign Cloud Stack, Deutsche Verwaltungscloud, and interoperability with Estonia's X-Road as integrated building blocks of a unified national digital infrastructure [54].

Cooperative IT providers — **Dataport AöR** (serving Hamburg, Schleswig-Holstein, Bremen, Mecklenburg-Vorpommern, Saxony-Anhalt, Thuringia) and **AKDB** (serving Bavaria) — provide the shared IT infrastructure used by most German municipal governments. Both are transitioning services toward open-source components aligned with OZG 2.0 mandates. Dataport has committed to deploying a Matrix-based solution for up to 500,000 users in public offices and educational institutions in Schleswig-Holstein and Hamburg [59].

### 3.4 Swiss Cantonal and Federal Digital Services

Switzerland's EMBAG (SR 172.019, in force 1 January 2024) is landmark open-source legislation. Its key articles are: Art. 3 (digital by default); Art. 9 (open-source publication obligation for federally funded software, subject only to security or third-party rights exceptions); Art. 10 (open data by default); and Arts. 12–15 (standards, interfaces, interoperability, and pilot programmes) [1]. This places Switzerland among the most progressive open-source mandating jurisdictions globally.

The **eCH association** publishes Swiss e-government standards (eCH standards), which define data formats, interfaces, and processes for cantonal and municipal digital administration — the Swiss equivalent of Germany's XÖV standards [47]. Key standards include eCH-0058 (web services), eCH-0097 (UID — company identification), and eCH-0160 (digital archiving). Compliance with eCH standards is a practical requirement for any technology deployed in Swiss public administration.

The **Swiss eID** (AHV-Nummer-basiertes System, post-2021 referendum reform) provides a state-backed digital identity operated on a privacy-preserving, decentralised architecture. The Confederation issued a revised eID Act (E-ID-Gesetz) creating the legal basis for a government-operated e-ID that will progressively replace cantonal solutions and integrate with European eIDAS 2.0 [16].

Key Swiss digital infrastructure includes: **Fedlex** (machine-readable federal law, open standards), **opendata.swiss** (national open government data portal, CKAN-based, cataloguing thousands of datasets from federal, cantonal, and municipal authorities) [44], **GEVER** (standardised records management, BAR-mandated for federal administration with cantonal variants such as CMI GEVER and Fabasoft eGov) [43], and the **E-Government Strategy 2024–2027** co-authored by the Federal Council and Conference of Cantonal Governments [16].

### 3.5 Case Studies in Open-Source Municipal Transformation

#### 3.5.1 Schleswig-Holstein: System-Wide Migration

Schleswig-Holstein represents the most ambitious current public-sector open-source migration in Europe. In April 2024, the state announced migration of 30,000 civil servant workplaces from Windows/Microsoft Office to Linux, LibreOffice, Nextcloud, and Thunderbird [51]. In October 2025, the state completed the email infrastructure migration: more than 40,000 mailboxes switched from Microsoft Exchange and Outlook to Open-Xchange and Thunderbird in a six-month process [51]. Nextcloud has recognised Schleswig-Holstein as an "Implementation Role Model" for digital sovereignty [58].

The state is also deploying a Matrix-based messaging infrastructure via Dataport for 500,000 users in public offices and educational institutions [59]. Schleswig-Holstein's "Deutschland-Stack" impulse paper, published in collaboration with Nextcloud, provides a reference architecture for other German Länder and municipalities [58].

#### 3.5.2 Barcelona: Decidim and Open Data

Barcelona's digital sovereignty strategy, launched under the 2017 Digital Plan (Pla Digital), combines the Decidim participatory democracy platform (which Barcelona co-created and open-sourced) with open data publication and a preference for open-source procurement [12]. The city's approach demonstrates that a large urban government can pursue digital sovereignty across multiple domains simultaneously. Decidim now has an international deployment census tracking instances globally, with confirmed deployments in Helsinki, Barcelona, New York, and the Swiss canton of Schaffhausen, among many others [12].

#### 3.5.3 France: Île-de-France and National Initiatives

France's public sector demonstrates the scale achievable with open-source collaboration platforms. The Île-de-France region deployed a Nextcloud-based sovereign cloud platform for 550,000 students and staff [58]. France's Tchap messaging application, built on Matrix, serves government employees. The French government has also deployed an AI assistant ("Albert") using open-source models on sovereign infrastructure, demonstrating that even emerging AI workloads can run on open infrastructure [64].

#### 3.5.4 Munich LiMux: Lessons from Reversal

Munich's LiMux project (2003–2017) migrated approximately 14,800 of its 29,000 workplace computers to Linux and LibreOffice. The project generated documented savings exceeding €10 million before political reversal [56]. The 2017 decision to return to Microsoft was driven by a new mayor with closer ties to the proprietary vendor, not by technical failure [30]. The return to Windows was subsequently estimated to cost the city approximately €100 million [56], making it one of the most expensive political reversals in municipal IT history and a powerful argument for embedding digital sovereignty in legislation rather than relying on administrative preference.

### 3.6 Open-Source Communities and Sovereign Technology Providers

**Decidim** (Barcelona, 2016) is a participatory democracy platform used across multiple continents. Its Decidim Census project tracks active deployments worldwide [12]. The Decidim Association's Social Contract — a governance document committing to democratic values, transparency, and open participation — is itself a model for open-source governance.

**Matrix/Element** provides an open, decentralised, E2E-encrypted communications protocol adopted at scale by European public administrations. The German BundesMessenger (launched December 2023 by BWI GmbH as an expansion of the Bundeswehr's BwMessenger from 2021) stores all data on government-controlled servers and makes its source code available on the openCode.de repository [59]. Dataport will deploy a Matrix-based solution for up to 500,000 users in Schleswig-Holstein and Hamburg [59].

**Nextcloud** (Stuttgart, 2016) reported over 500,000 server instances worldwide in 2025, with customer interest tripling in the first five months of 2025 amid rising concerns about US cloud provider dependency [58]. Public-sector deployments span Austria's Federal Ministry of Economy, Energy and Tourism; the City of Stuttgart; Schleswig-Holstein; Île-de-France (550,000 users); Danish federal government; and numerous French public bodies [58].

**OpenDesk** (ZenDiS GmbH, Berlin, launched 2022; v1.0 released October 20, 2024) is the German government's curated open-source workplace suite: Nextcloud (files and collaboration), Collabora Online (office documents), OpenProject (project management), Jitsi (video), Element (messaging), CryptPad (end-to-end encrypted editing), and additional components [42, 50]. By June 2025, OpenDesk served more than 100,000 users, including the Robert Koch Institute and several state administrations. In April 2025, BWI signed a seven-year agreement for Bundeswehr use [50]. ZenDiS also manages **openCode.de** as a platform for collaborative development of administration-related open-source software [10, 50].

**Forgejo**, a community-governed fork of Gitea, has emerged as the European sovereign alternative for code hosting. The Netherlands government's Open Source Programme Office (OSPO) selected Forgejo as the foundation for **code.overheid.nl** — a self-hosted platform for government open-source software — explicitly citing the "public money, public code" principle and the need to reduce dependency on GitHub and GitLab [60].

**TYPO3** powers over 35% of German government websites [19]. The new **Government Site Builder (GSB) 11**, launched in 2024, is the federal standard for German ministerial and municipal websites, built on TYPO3 and offering WCAG 2.1 AA / BITV 2.0 accessibility compliance, multilingualism, and integration with open data systems [19].

### 3.7 Economic Evidence

The economic case for open-source municipal technology is supported by multiple lines of evidence:

**EU-level multiplier:** The European Commission finds that every €1 invested in open source generates at least €4 in economic value across Europe through code reuse, reduced duplication, and innovation spillovers [62]. This multiplier is particularly powerful for municipal governments that can share implementations via openCode.de or the Swiss public repositories.

**Licence cost displacement:** Proprietary productivity software costs €100–300 per user per year in licence fees alone [3]. A municipality of 500 employees replacing Microsoft 365 with OpenDesk/Nextcloud/LibreOffice eliminates €50,000–150,000 in annual licence costs, providing a compelling break-even case for a one-time migration investment.

**The Munich reversal benchmark:** The €100 million estimated cost of Munich's return to Windows [56] — for a city of ~29,000 civil servant workstations — illustrates the true cost of proprietary dependency when political winds shift. For a medium-sized municipality of 500 workstations, the proportional risk is approximately €1.7 million.

**Schleswig-Holstein data:** The state's migration of email infrastructure (40,000+ mailboxes) from Microsoft Exchange to Open-Xchange was completed on schedule [51], validating that large-scale enterprise migrations to open alternatives are operationally feasible.

**Sovereign Tech Fund ROI:** The German Sovereign Tech Fund's investment of €23.5 million in critical open-source infrastructure [49] functions as a public insurance premium: it maintains the open-source commons that all public administrations draw upon, at a fraction of the cost of proprietary alternatives.

### 3.8 Gaps in the Literature

1. **Long-term TCO studies for small municipalities** remain sparse. Most available data covers large cities or federal agencies.
2. **User experience research** comparing citizen satisfaction with open-source and proprietary municipal services is almost entirely absent.
3. **Longitudinal studies on contribution-back economics** — the value municipalities generate by contributing improvements upstream — are not yet available.
4. **Small-municipality perspectives** are underrepresented; most case studies focus on large cities or federal agencies.
5. **AI Act compliance cost studies** for open-source vs. proprietary AI in public administration are an emerging gap as the Act's requirements take effect.

See `Mem/literature-review-state.md` for the full gap analysis and improvement roadmap.

---

## 4. Technology Stack Analysis

A municipal technology stack can be decomposed into ten functional layers. The analysis below evaluates the leading open-source options for each layer against the scoring criteria defined in Section 2. All components are assessed as of June 2026.

### 4.1 Digital Identity and Authentication

**Function:** Authenticate citizens and staff; federate identity across services; implement single sign-on (SSO).

**Recommended component: Keycloak** (Red Hat / CNCF) [21]

Keycloak is the de facto open-source identity and access management (IAM) platform for public administration. It implements OpenID Connect (OIDC), OAuth 2.0, SAML 2.0, and FIDO2/WebAuthn, enabling federation with national identity systems (DeutschlandID/BundID in Germany, eID in Switzerland, eIDAS 2.0 for EU cross-border services). Deployed by EU institutions, German Länder, Swiss cantons, and French national services.

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Licence openness | 5 | Apache 2.0 |
| Deployment maturity | 5 | Production-proven, 10+ years |
| Community health | 5 | Large, active, CNCF-supported |
| Interoperability | 5 | OIDC, OAuth2, SAML2, FIDO2 |
| Security posture | 5 | CVE-responsive, widely audited |
| TCO | 4 | No licence cost; ops expertise required |
| Public-sector deployments | 5 | Widespread EU government use |

### 4.2 Document Management and Records

**Function:** Store, retrieve, classify, and retain official records; manage GEVER-compliant workflows.

**Recommended components: Nextcloud** (collaborative file management) + **OpenProject** (project and records linking) [13, 20]

For Swiss municipalities requiring GEVER compliance, cantonal GEVER solutions (CMI GEVER, Fabasoft eGov Community) provide the compliance layer, with Nextcloud as the collaborative front-end [43]. For German municipalities, the OpenDesk suite integrates Nextcloud and OpenProject within a government-curated stack [42]. Nextcloud's 500,000+ server deployments globally and specific government deployments at the scale of Austria's BMWET, Stuttgart, and Île-de-France (550,000 users) confirm enterprise-grade maturity [58].

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Licence openness | 5 | AGPL-3.0 (Nextcloud) |
| Deployment maturity | 5 | 500,000+ server instances |
| Community health | 5 | Nextcloud GmbH + community |
| Interoperability | 4 | WebDAV, CalDAV, CardDAV, CMIS |
| Security posture | 5 | ISO 27001 certified offering |
| TCO | 5 | No per-seat licence (Community) |
| Public-sector deployments | 5 | Swiss federal, German Länder, French regions |

### 4.3 Office Suite

**Function:** Word processing, spreadsheets, presentations, real-time collaborative editing.

**Recommended components: LibreOffice** (desktop) + **Collabora Online** (browser-based, WOPI-compatible) [63]

LibreOffice, developed by The Document Foundation, is the leading open-source office suite with full ODF (Open Document Format) support and strong Microsoft Office compatibility. Collabora Online, the enterprise-grade browser-based version of LibreOffice, is integrated directly into OpenDesk [42] and deployed across Schleswig-Holstein's 30,000-seat migration [51]. Both support German BITV 2.0 and international WCAG 2.1 accessibility standards.

**Open-Xchange** provides open-source email, calendar, and contacts (groupware), forming part of Schleswig-Holstein's migration from Microsoft Exchange completed October 2025 [51]. It is available as App Suite for enterprise deployments.

| Component | Licence | Maturity | Key advantage |
|---|---|---|---|
| LibreOffice | MPL-2.0 | Production | Full ODF, wide hardware compatibility |
| Collabora Online | MPL-2.0 | Production | Browser-based, OpenDesk-integrated |
| Open-Xchange | AGPL-3.0 | Production | Enterprise email/groupware, Exchange replacement |

### 4.4 Workflow Automation and Business Process Management

**Function:** Automate administrative workflows; model, execute, and monitor BPMN processes.

**Recommended component: Camunda Platform Community** [33]

Camunda provides a BPMN 2.0-native workflow engine with strong support for complex multi-step administrative processes and XÖV / eCH data standards integration [46, 47]. **Flowable** (Apache 2.0) is a lighter-weight alternative if Camunda's dual-licensing model creates procurement complications. Both support the FIM (Form and Information Management) approach central to OZG 2.0 implementation [2].

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Licence openness | 4 | Community: Apache 2.0; Enterprise: proprietary |
| Deployment maturity | 5 | Production-proven |
| Community health | 4 | Active; enterprise tier funds development |
| Interoperability | 5 | BPMN 2.0, REST API, event-driven |
| Security posture | 4 | Actively maintained |
| TCO | 3 | Community free; scale may need Enterprise |
| Public-sector deployments | 4 | Multiple German Länder, Swiss cantons |

### 4.5 Citizen Participation

**Function:** Consultation, participatory budgeting, initiative collection, deliberation platforms.

**Recommended component: Decidim** [12]

Decidem is the most mature and widely adopted open-source participation platform globally. The Decidim Association's Social Contract commits the platform to democratic values, transparency, and inclusivity. Confirmed deployments include Barcelona, Helsinki, New York, and the Swiss canton of Schaffhausen. The Decidim Census project tracks active instances worldwide [12]. Its modular architecture supports participatory budgeting, public consultations, citizen initiatives, and deliberative assemblies.

**Alternative:** CONSUL Democracy (Madrid), also AGPL-3.0, strong in Spanish-speaking contexts [48].

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Licence openness | 5 | AGPL-3.0 |
| Deployment maturity | 5 | Hundreds of deployments globally |
| Community health | 5 | Active association and community |
| Interoperability | 4 | REST API, GraphQL, webhooks |
| Security posture | 4 | Actively maintained |
| TCO | 5 | No licence cost |
| Public-sector deployments | 5 | Cities, cantons, federal agencies |

### 4.6 Communication and Collaboration

**Function:** Internal messaging, video conferencing, email; secure inter-agency communication.

**Recommended components:**
- **Matrix/Element** for messaging and inter-agency secure communication [14]
- **BundesMessenger** reference deployment for German municipalities [59]
- **Jitsi Meet** or **BigBlueButton** for video conferencing [34, 35]
- **Open-Xchange** for email/groupware
- **Nextcloud Talk** for integrated team communication [13]

The BundesMessenger (BWI, December 2023), built on Matrix and Element, stores all data on government-controlled servers and provides E2E encryption, BYOD support, and built-in malware scanning [59]. Dataport's planned Matrix deployment for 500,000 users in Schleswig-Holstein and Hamburg provides a reference scale for state-level implementations [59].

| Component | Licence | Maturity | Key advantage |
|---|---|---|---|
| Matrix/Element | Apache 2.0 | Production | E2E encryption, federation |
| Jitsi Meet | Apache 2.0 | Production | Browser-based, self-hostable |
| BigBlueButton | LGPL-3.0 | Production | Council meeting focus |
| Nextcloud Talk | AGPL-3.0 | Production | Integrated with file management |
| Open-Xchange | AGPL-3.0 | Production | Enterprise email, Exchange replacement |

### 4.7 Open Data Publication

**Function:** Publish machine-readable datasets; catalogue data; provide API access; comply with PSI/Open Data directives.

**Recommended component: CKAN** [22]

CKAN powers opendata.swiss (Switzerland), govdata.de (Germany), data.europa.eu (EU), data.gov (USA), and data.gov.uk, among many others [22]. Its plugin architecture enables full compliance with DCAT-AP (EU), DCAT-AP.de (Germany), and OGD Switzerland metadata standards, and supports harvesting from and to upstream catalogues.

### 4.8 Geographic Information Systems

**Function:** Map-based citizen services; urban planning; spatial data publication.

**Recommended components:**
- **QGIS** (desktop/server) for spatial data editing and analysis [37]
- **GeoServer** for OGC-compliant spatial data publication
- **OpenStreetMap** as base cartographic layer [36]

Switzerland's swisstopo and Germany's BKG provide open, high-quality governmental base map data compatible with this stack. Both publish under open government data licences.

### 4.9 Web Publishing and Content Management

**Function:** Public-facing website; news; service directory.

**Recommended components:**
- **TYPO3** + **Government Site Builder (GSB) 11** (German-speaking world): TYPO3 powers over 35% of German government websites [19]; GSB 11, launched in 2024, is the federal standard for ministerial and municipal websites
- **Drupal**: strong international track record; used by the European Commission

### 4.10 Code Hosting and Inner Source

**Function:** Version-control government software; enable inner-source collaboration across agencies; publish open-source code per EMBAG/OZG obligations.

**Recommended components:**
- **Forgejo** (sovereign self-hosted Git platform) [60]
- **openCode.de** (German government platform, ZenDiS, Forgejo-compatible) [10]
- Cantonal/municipal instances publishing to opendata portals

Forgejo, chosen by the Netherlands' OSPO for code.overheid.nl [60], provides a fully open-source (MIT-licensed), self-hostable alternative to GitHub and GitLab. Swiss municipalities with EMBAG obligations and German municipalities under OZG 2.0 can use a Forgejo instance or contribute directly to openCode.de to satisfy open-source publication requirements.

### 4.11 Cloud Infrastructure and Hosting

**Function:** Compute, storage, networking, container orchestration; digital sovereignty at the infrastructure layer.

**Recommended component: Sovereign Cloud Stack (SCS)** [3, 11, 55]

SCS provides a fully open-source cloud stack (OpenStack + Kubernetes + Ceph) that can be self-hosted, operated by a cooperative provider (govdigital eG), or deployed by certified SCS cloud operators including ScaleUp Technologies, plusserver, and OSISM [55]. SCS Release 8 (April 2025) introduces upgrade flexibility via SLURP (skip-level update release process), updated Ubuntu 24.04 LTS base, OpenStack 2024.2, and current Kubernetes versions [55]. The GovStack initiative has formally integrated SCS into its cloud infrastructure specification [55].

The **Deutsche Verwaltungscloud (DVC)**, launched March 2025, enables applications to run across multiple SCS-based cloud locations and be shared nationally [2].

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Licence openness | 5 | Apache 2.0 / fully open |
| Deployment maturity | 4 | Production in multiple Länder; R8 released |
| Community health | 5 | OSBA-backed, growing post-BMWK |
| Interoperability | 5 | Open APIs, OCI-compliant, GovStack-integrated |
| Security posture | 5 | BSI IT-Grundschutz compatible |
| TCO | 4 | No licence; infrastructure cost |
| Public-sector deployments | 4 | German Länder, UN projects |

**For municipalities without in-house cloud operations capacity:** use certified SCS hosters (plusserver, ScaleUp Technologies, OSISM) providing managed SCS with full data sovereignty guarantees, or join govdigital eG for cooperative procurement.

### 4.12 Reference Architecture

```
+---------------------------------------------------------------------+
|                       CITIZEN TOUCHPOINTS                           |
|   TYPO3/GSB11 . Decidim . CKAN . Nextcloud . Forgejo (public)     |
+---------------------------------------------------------------------+
|                         SERVICE LAYER                              |
|   Camunda Workflows . XÖV/eCH Forms . GeoServer . QGIS Server     |
+---------------------------------------------------------------------+
|                      COLLABORATION LAYER                           |
|   OpenDesk (Nextcloud + Collabora + OpenProject + Jitsi + Element) |
|   Open-Xchange (email/calendar) . Forgejo (inner source)          |
+---------------------------------------------------------------------+
|                        IDENTITY LAYER                              |
|         Keycloak <-> DeutschlandID/BundID / Swiss eID / eIDAS 2.0 |
+---------------------------------------------------------------------+
|                    INFRASTRUCTURE LAYER                            |
|  Sovereign Cloud Stack R8 . Kubernetes . PostgreSQL . Ceph . MinIO |
+---------------------------------------------------------------------+
```

All layers communicate via open APIs. Container orchestration is handled by Kubernetes [39], relational persistence by PostgreSQL [41], object storage by MinIO (S3-compatible), all running on the Sovereign Cloud Stack. Data exchange uses XÖV standards (Germany) [46] or eCH standards (Switzerland) [47]. Security governance follows BSI IT-Grundschutz++ (Germany, mandatory from January 2026) [57] or the Swiss ISDS framework. Open-source publication of custom code uses Forgejo instances connected to openCode.de or Swiss public repositories.

---

## 5. Implementation Roadmap

The implementation is structured as a 36-month, five-phase programme. Each phase has defined deliverables, success criteria, and decision gates. Budget figures are indicative for a municipality with 200–500 IT-using staff; scale linearly for larger cities.

### Phase 0: Foundation (Months 1–3)

**Objective:** Establish governance, assess current state, build the coalition.

**Deliverables:**
- Digital Transformation Steering Committee established (city leadership + IT + civil society + data protection officer)
- Current-state technology audit and dependency mapping completed
- Stakeholder engagement plan adopted
- Procurement framework established (Section 6)
- MoU with cooperative IT provider (Dataport, AKDB, govdigital eG, or equivalent)
- Initial contact with openCode.de / opendata.swiss for code publication pathway

**Success criteria:**
- Political mandate secured (council resolution or executive decision)
- Budget envelope approved (indicative: €200,000–€500,000 for Phases 0–1)
- Project lead appointed with sufficient seniority and mandate
- Data protection officer engaged from day one

**EU funding pathway:** Apply to Digital Europe Programme calls for digital public services and interoperability; engage Technical Support Instrument (TSI) for public service modernisation advisory [62].

### Phase 1: Identity and Infrastructure (Months 4–12)

**Objective:** Stand up the foundational layers that everything else depends on.

**Deliverables:**
- SCS environment operational (own or certified hoster: plusserver, ScaleUp, govdigital eG)
- Keycloak identity provider deployed and federated with national identity (DeutschlandID / Swiss eID)
- OpenDesk baseline deployment for internal collaboration (Nextcloud + Collabora + Element)
- Open-Xchange or Thunderbird migration plan drafted
- Forgejo instance deployed for inner-source code management
- BSI IT-Grundschutz++ baseline documentation initiated

**Success criteria:**
- 100% of IT staff authenticate via Keycloak SSO
- File storage migrated from proprietary cloud to Nextcloud/OpenDesk
- Basic encrypted messaging (Matrix/Element) operational
- Zero proprietary US-cloud dependencies for internal communications

### Phase 2: Services and Workflows (Months 10–18)

**Objective:** Migrate or build the first citizen-facing services on open infrastructure.

**Deliverables:**
- Five highest-volume administrative services deployed on Camunda/XÖV (or Flowable/eCH) stack
- TYPO3 GSB 11 (Germany) or TYPO3/Drupal (Switzerland) CMS migration complete
- CKAN open data portal launched with minimum 20 datasets; DCAT-AP/OGD metadata compliant
- Decidim instance deployed for first participatory process
- Open-source code published on openCode.de or Swiss public repository per EMBAG/OZG obligations

**Success criteria:**
- 80% of target service volume through new system
- Zero regression in service availability vs. baseline
- First open data publication live
- First upstream contribution to an open-source project used by the municipality

### Phase 3: Integration and Extension (Months 16–24)

**Objective:** Integrate all layers; extend service coverage to 80% of transactions.

**Deliverables:**
- All services federated via Keycloak SSO
- Nextcloud integrated with document management workflows
- GIS layer operational (QGIS + GeoServer) with open base maps
- 80% of administrative services digitised per OZG 2.0 / cantonal requirements
- Inter-agency data exchange via XÖV/eCH operational
- Email infrastructure migrated to Open-Xchange + Thunderbird
- AI Act compliance assessment for any AI components

**Success criteria:**
- End-to-end service delivery without paper for 80% of transaction types
- Data quality metrics established and tracked
- First annual open data report published
- NIS2 / BSI IT-Grundschutz++ documentation complete

### Phase 4: Optimisation and Community (Months 22–30)

**Objective:** Optimise user experience; contribute back to open-source communities; publish results.

**Deliverables:**
- User satisfaction survey (target: NPS > 40)
- Minimum three contributions to openCode.de / upstream projects
- Municipal open-source community of practice established with ≥ 3 peer municipalities
- TCO report published (open access)
- Sovereign Tech Fund partnership explored for critical dependencies

**Success criteria:**
- Community of practice active
- Total cost of ownership report published openly
- First applications submitted to Sovereign Tech Fund or Digital Europe Programme for co-funding

### Phase 5: Sovereignty and Scale (Months 28–36)

**Objective:** Achieve full digital sovereignty; prepare extension to neighbouring municipalities.

**Deliverables:**
- Full audit: all software components licence-compliant, SBOM maintained
- Sovereign data residency verified on SCS-based infrastructure
- Playbook for replication by neighbouring municipalities published on openCode.de
- Strategy paper v1.0 published
- Annual open-source contribution report

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
| Civil society / NGOs | Transparency, access, participation | Decidim platform, public roadmaps |
| Open-source communities | Contribution, reuse | openCode.de / Swiss repos, upstream contributions |
| Sovereign technology providers | Partnership, deployment | Certified partner agreements |
| Data protection officer | GDPR / nDSG compliance | Privacy-by-design review at each phase |
| AI Act compliance officer | High-risk AI conformity | AI inventory, conformity assessments |

### 6.2 Procurement Framework

**1. Procure services, not licences.** Open-source software is free to use; municipalities pay for implementation, hosting, support, customisation, and training. Procurement documents must be structured around these services.

**2. Use cooperative procurement structures.** Germany's **govdigital eG** and Swiss cantonal IT cooperatives provide framework agreements for open-source municipal IT that satisfy public procurement law (GWB/Vergaberecht in Germany; BöB/VöB in Switzerland) [23]. Joining govdigital eG or an equivalent cooperative distributes costs and provides collective bargaining power.

**3. Apply the "Public Money? Public Code!" principle.** All custom software developed under contract must be released under an OSI-approved licence and published on openCode.de (Germany), a cantonal public repository (Switzerland), or the EU's Interoperable Europe Portal. This must be a binding contract condition [4].

**4. Evaluate total cost of ownership over five years.** Procurement scoring must include a 5-year TCO model covering implementation, hosting, training, support, and exit costs. The Munich case (€100M reversal cost) [56] and Schleswig-Holstein email migration demonstrate that both the cost of migration and the cost of lock-in must be quantified. The EU multiplier of €4 economic value per €1 open-source investment [62] should be included in the business case.

**5. Require interoperability standards.** All procured systems must implement: XÖV (Germany) [46], eCH (Switzerland) [47], DCAT-AP (EU open data) [45], eIDAS 2.0 (EU digital identity) [16], and NIS2/BSI IT-Grundschutz++ security standards [57]. Non-compliance should be a disqualifying criterion.

**6. Prefer certified cooperative providers.** For infrastructure, prefer SCS-certified cloud operators or members of govdigital eG, who are bound by collective data sovereignty agreements [23].

### 6.3 EU Funding Pathways

Municipalities have access to multiple EU funding mechanisms for open-source digital transformation:

**Digital Europe Programme (DIGITAL, 2021–2027):** €8.1 billion total; supports digital public services, interoperability, and cybersecurity. The Interoperable Europe Board earmarks €77 million in the 2025–2027 Work Programme specifically for cross-border interoperability and digital government collaboration [6, 62].

**Horizon Europe (2021–2027):** €93.5 billion total; the Next Generation Internet (NGI) programme within Horizon funds open-source projects with grants of €5,000–€50,000 for code enhancement. Consortia combining public agencies, industry, and researchers have strong competitive positions [62].

**Sovereign Tech Fund (Germany):** €17 million annual budget; funds critical open-source infrastructure that municipalities and federal agencies depend on. Municipalities can nominate dependencies for STF consideration or contribute co-funding [49].

**Interreg and Cohesion Funds:** Support cross-border digital transformation; particularly relevant for border municipalities in CH/DE/AT/FR regions.

**Technical Support Instrument (TSI):** EU-funded advisory support for public service modernisation; does not require co-financing and is suitable for smaller municipalities.

### 6.4 Change Management

Open-source transitions frequently fail not on technical grounds but on human factors: end-user resistance, insufficient training, middle-management inertia, and political backsliding under vendor lobbying. The Munich LiMux case confirms that political risk management is as important as technical planning [30, 56].

**Recommendations:**
- Appoint a **Digital Transformation Champion** at senior political level with explicit mandate and cross-party endorsement
- Establish **open-source champions** in each department with advanced training and peer support role
- Run **parallel operations** for minimum three months before cutting over critical systems
- Document and celebrate **early wins** (cost savings, new capabilities, citizen feedback) publicly
- Publish a **public transparency dashboard** showing migration progress, costs, and service quality
- Embed digital sovereignty preference in municipal ordinance or statute — not merely in administrative policy — to survive political transitions

---

## 7. Risk Analysis

### 7.1 Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Political reversal after election | Medium | High | Embed in legislation/ordinance; build cross-party consensus; public transparency dashboard |
| Vendor lobbying / FUD campaigns | High | Medium | Document TCO evidence; engage civil society; publicise mandate; cite Munich reversal cost |
| Skill gap in IT team | High | Medium | Training programme; cooperative IT provider; community of practice; Sovereign Tech Fund |
| Integration failure between layers | Medium | High | Phased rollout with decision gates; reference architecture adherence |
| Data loss during migration | Low | Critical | Full backup protocol; parallel operation; staged migration |
| GDPR / nDSG data protection violation | Low | High | Privacy-by-design; DPO engagement from Phase 0; data mapping |
| User adoption failure | Medium | High | Change management; UX testing; training; parallel systems; open-source champions |
| Security incident | Low | Critical | BSI IT-Grundschutz++; penetration testing; incident response plan; NIS2 compliance |
| AI Act non-compliance | Medium | High | AI inventory at Phase 0; conformity assessments; prefer open-source AI with auditable weights |
| Community fragmentation | Low | Medium | Contribute upstream; align with openCode.de; join govdigital eG |
| Cost overrun | Medium | Medium | Phase-gated budget; independent project office; open TCO accounting |
| Supply chain attack on open-source dependency | Low | High | SBOM maintenance; Sovereign Tech Fund investment in critical deps; dependency audit |

### 7.2 The Munich Cautionary Case

The City of Munich's LiMux project (2003–2017) migrated approximately 14,800 workplaces to Linux and LibreOffice. The project generated documented savings exceeding €10 million. The 2017 decision to revert to Microsoft was driven primarily by a change in political leadership, inadequate change management, and compatibility issues with state-level systems that had not adopted open standards [30]. The technical implementation was broadly successful. The return to Windows cost an estimated €100 million [56] — demonstrating that the true cost of vendor dependency is only visible at the moment of maximum lock-in. The lesson is institutional: digital sovereignty must be embedded in legislation, not merely in administrative preference.

### 7.3 AI Act Compliance

The EU AI Act (Regulation (EU) 2024/1689, fully applicable from August 2026) classifies AI systems used in public administration for citizen-facing decisions — including automated benefit assessments, risk scoring, and eligibility determinations — as **high-risk AI systems** subject to mandatory conformity assessment, registration in the EU AI database, human oversight, and explainability requirements [64]. Open-source AI systems offer structural advantages for compliance: source code availability enables the technical documentation required for conformity assessment; model weights can be audited; and deployment on sovereign infrastructure avoids cross-border data transfer risks. Municipalities should maintain an AI inventory from Phase 0, assess each system under the Act's risk classification, and prefer open-source AI components where high-risk classification applies.

### 7.4 Security Considerations

The BSI's IT-Grundschutz++ framework (catalogue released January 1, 2026, mandatory for German public administrations under the NIS2 Implementation Act in force December 5, 2025) provides a comprehensive security baseline [57]. For Swiss municipalities, the ISDS framework serves the equivalent function. Key requirements for both:

- Server components must receive security updates within defined SLA; a documented patch management process is required
- Authentication must meet BSI AAL2 (or equivalent) for citizen-facing services; FIDO2/WebAuthn preferred
- Data in transit: TLS 1.3 minimum; data at rest: encrypted for sensitive categories
- Software Bill of Materials (SBOM) maintained for all open-source dependencies
- Penetration testing at each phase gate
- Incident response plan aligned with NIS2 obligations
- AI systems deployed in public administration require additional security review per AI Act Art. 9

---

## 8. Conclusion

The evidence reviewed in this paper converges on five findings:

**1. Open-source municipal technology stacks are technically mature and production-proven at scale.** Every functional requirement of a modern municipal government can be met by open-source software with documented deployments at peer municipalities, from Schleswig-Holstein's 30,000-seat migration to Île-de-France's 550,000-user Nextcloud deployment to Barcelona's Decidim platform and the German federal BundesMessenger.

**2. The regulatory environment increasingly mandates open-source and interoperability.** EMBAG Art. 9 (Switzerland, 2024), OZG 2.0's open-source preference mandate (Germany, July 2024), the Interoperable Europe Act's binding obligations (EU, April 2024), and Germany's NIS2 Implementation Act (December 2025) collectively create a legal environment where proprietary, vendor-locked systems generate regulatory risk and compliance debt. The Deutschland-Stack vision (2025 coalition agreement, 2028 target) signals Germany's long-term direction unambiguously.

**3. The economic case is compelling when total costs are counted correctly.** The EU finding of €4 economic value per €1 open-source investment [62], Munich's €100 million reversal cost [56], and the Sovereign Tech Fund's €23.5 million investment in 60+ critical open-source projects [49] together frame the fiscal argument. Open-source stacks eliminate per-seat licence costs and reduce vendor lock-in risk; cooperative procurement via govdigital eG or Swiss cantonal IT cooperatives spreads implementation costs.

**4. EU and national funding mechanisms reduce the financial barrier to entry.** The Digital Europe Programme (€77 million earmarked for interoperability 2025–27), the Sovereign Tech Fund (€17 million annually), and Horizon Europe's NGI programme provide structured co-funding pathways that municipalities should access from Phase 0.

**5. Success requires as much political and organisational investment as technical investment.** Munich's cautionary tale and Schleswig-Holstein's ongoing success both confirm that clear political mandate, cross-party consensus, skilled change management, and sustained stakeholder engagement are the binding constraints. Embedding digital sovereignty preference in municipal ordinance — not merely administrative policy — is the single most important risk mitigation available.

Cities that move first will shape cooperative standards, build in-house expertise, and contribute to the open-source commons that all municipalities share. The regulatory, economic, and democratic arguments have converged. The invitation — and increasingly the obligation — is open.

---

## References

[1] Swiss Federal Council. (2023). *Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG)*. SR 172.019. In force 2024-01-01. Bern: Swiss Confederation. https://www.fedlex.admin.ch/eli/cc/2023/682/de — [CC0]

[2] Bundesministerium des Innern und für Heimat (BMI). (2024). *Onlinezugangsgesetz 2.0 — OZG-Änderungsgesetz, in force 2024-07-24*. Berlin: BMI. https://www.digitale-verwaltung.de/Webs/DV/DE/onlinezugangsgesetz/das-gesetz/ozg-aenderungsgesetz/ozg-aenderungsgesetz-node.html — [DL-DE/Zero 2.0]

[3] Open Source Business Alliance (OSBA). (2025). *Sovereign Cloud Stack: Community and Governance Overview*. Berlin: OSBA. https://scs.community/ — [CC-BY-SA-4.0]

[4] Free Software Foundation Europe (FSFE). (2017). *Public Money? Public Code!* Berlin: FSFE. https://publiccode.eu/ — [CC-BY-SA-4.0]

[5] European Commission. (2020). *Open Source Software Strategy 2020–2023: Think Open*. Brussels. https://commission.europa.eu/about/departments-and-executive-agencies/informatics/open-source-software-strategy_en — [© EU, open access]

[6] Council of the EU. (2024). *Regulation (EU) 2024/903 — Interoperable Europe Act, in force 2024-04-11, substantive obligations from 2025-01-12*. Brussels: Council of the EU. https://www.consilium.europa.eu/en/press/press-releases/2024/03/04/interoperable-europe-act-council-adopts-new-law-for-more-efficient-digital-public-services-across-the-eu/ — [EU legislation, public domain]

[7] Wirtz, B. W., & Weyerer, J. C. (2017). Conceptualization and creation of a holistic e-government maturity model. *Public Management Review*, 19(9), 1297–1316. https://doi.org/10.1080/14719037.2017.1283024

[8] Janssen, M., Charalabidis, Y., & Zuiderwijk, A. (2012). Benefits, adoption barriers and myths of open data and open government. *Information Systems Management*, 29(4), 258–268. https://doi.org/10.1080/10580530.2012.716740

[9] FITKO. (2024). *Föderale IT-Kooperation — Jahresbericht 2024*. Frankfurt: FITKO. https://www.fitko.de/ — [DL-DE/Zero 2.0]

[10] ZenDiS GmbH. (2025). *openCode — Open Source for Government*. Berlin: ZenDiS. https://opencode.de/ — [Open access; repository code under various OSI licences]

[11] Sovereign Cloud Stack Community. (2025). *SCS Technical Documentation*. https://docs.scs.community/ — [Apache 2.0]

[12] Decidim Association. (2025). *Decidim: Free Open-Source Participatory Democracy for Cities and Organizations. Decidim Census.* Barcelona: Decidim Association. https://decidim.org/ | https://decidim-census.digidemlab.org/ — [AGPL-3.0]

[13] Nextcloud GmbH. (2025). *Nextcloud for Government: Security, Sovereignty, and Collaboration*. Stuttgart. https://nextcloud.com/government/ — [AGPL-3.0]

[14] The Matrix Foundation. (2025). *Matrix Specification v1.x*. https://spec.matrix.org/ — [Apache 2.0]

[16] E-Government Suisse / Swiss Federal Chancellery. (2023). *Strategie E-Government Schweiz 2024–2027*. Bern. https://www.egovernment.ch/de/umsetzung/e-government-strategie/ — [Open access]

[19] TYPO3 Association / TYPO3 GmbH. (2024). *Government Site Builder 11 powered by TYPO3*. Düsseldorf. https://typo3.com/solutions/industries/public-sector | https://typo3.com/solutions/industries/public-sector/government-site-builder — [GPL-2.0]

[20] OpenProject GmbH. (2025). *OpenProject: Open Source Project Management*. Berlin. https://www.openproject.org/ — [GPLv3]

[21] Keycloak Community / CNCF. (2025). *Keycloak: Open Source Identity and Access Management*. https://www.keycloak.org/ — [Apache 2.0]

[22] CKAN Association. (2025). *CKAN: Open Source Data Portal Software*. https://ckan.org/ — [AGPL-3.0]

[23] govdigital eG. (2025). *govdigital: Genossenschaft für digitale Verwaltung*. Berlin. https://govdigital.de/ — [Open access]

[24] Dataport AöR. (2025). *Dataport: IT-Dienstleister für die öffentliche Verwaltung*. Hamburg. https://www.dataport.de/ — [Open access]

[26] Bundesamt für Sicherheit in der Informationstechnik (BSI). (2023). *BSI IT-Grundschutz-Kompendium Edition 2023*. Bonn: BSI. https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/IT-Grundschutz-Kompendium/it-grundschutz-kompendium_node.html — [CC-BY-ND 3.0 DE]

[27] European Parliament and Council. (2022). *Directive (EU) 2022/2555 — NIS2 Directive*. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022L2555 — [EU legislation, public domain]

[29] United Nations DESA. (2022). *UN E-Government Survey 2022: The Future of Digital Government*. New York: UN. https://publicadministration.un.org/egovkb/en-us/Reports/UN-E-Government-Survey-2022 — [© UN, open access]

[30] Janowski, T. (2015). Digital government evolution: From transformation to contextualization. *Government Information Quarterly*, 32(3), 221–226. https://doi.org/10.1016/j.giq.2015.07.001

[33] Camunda Services GmbH. (2025). *Camunda Platform Community Edition*. https://camunda.com/download/ — [Apache 2.0 / proprietary Enterprise]

[34] BigBlueButton Inc. (2025). *BigBlueButton: Open Source Web Conferencing*. https://bigbluebutton.org/ — [LGPL-3.0]

[35] Jitsi Community / 8x8. (2025). *Jitsi Meet: Open Source Video Conferencing*. https://jitsi.org/ — [Apache 2.0]

[36] OpenStreetMap Foundation. (2025). *OpenStreetMap*. https://www.openstreetmap.org/ — [ODbL-1.0]

[37] QGIS Project. (2025). *QGIS: A Free and Open Source Geographic Information System*. https://www.qgis.org/ — [GPL-2.0+]

[39] Cloud Native Computing Foundation (CNCF). (2025). *Kubernetes*. https://kubernetes.io/ — [Apache 2.0]

[41] PostgreSQL Global Development Group. (2025). *PostgreSQL*. https://www.postgresql.org/ — [PostgreSQL Licence (BSD-like, OSI-approved)]

[42] ZenDiS GmbH / BMI. (2024). *openDesk v1.0: Der digitale Arbeitsplatz der öffentlichen Verwaltung*. Released 2024-10-20. https://opendesk.eu/en/about — [AGPL-3.0]

[43] Schweizerisches Bundesarchiv (BAR). (2024). *Geschäftsverwaltung (GEVER) in der Bundesverwaltung*. Bern: BAR. https://www.bar.admin.ch/bar/de/home/digitale-archivierung/gever.html — [Open access]

[44] opendata.swiss. (2025). *Open Government Data Switzerland*. Bern: Swiss Federal Chancellery. https://opendata.swiss/ — [CC-BY-4.0 for portal; individual dataset licences vary]

[45] European Commission. (2017). *European Interoperability Framework — Implementation Strategy (EIF)*. Brussels. https://joinup.ec.europa.eu/collection/nifo-national-interoperability-framework-observatory/european-interoperability-framework-detail — [CC-BY-4.0]

[46] KoSIT. (2025). *XÖV-Standards: XML in der öffentlichen Verwaltung*. Bremen: KoSIT. https://www.xoev.de/ — [Open access]

[47] eCH Association. (2025). *eCH-Standards für E-Government Schweiz*. Bern: eCH. https://www.ech.ch/ — [Open access; standards freely downloadable]

[48] CONSUL Democracy Foundation. (2025). *CONSUL Democracy: Free Citizen Participation Platform*. Madrid. https://consulproject.org/ — [AGPL-3.0]

[49] Sovereign Tech Fund GmbH. (2024). *Sovereign Tech Fund: Investing in Digital Infrastructure*. Berlin: STF. https://www.sovereigntechfund.de/ — [Open access]

[50] ZenDiS GmbH. (2025). *ZenDiS: Co-creating Digital Sovereignty. Annual overview 2024–2025*. Berlin: ZenDiS. https://www.zendis.de/en — [Open access]

[51] Staatskanzlei Schleswig-Holstein. (2024–2025). *Linux-Migration Schleswig-Holstein: 30,000 Arbeitsplätze auf Open Source (April 2024); E-Mail-Migration abgeschlossen (October 2025)*. Kiel. https://www.schleswig-holstein.de/DE/landesregierung/themen/digitalisierung/linux-plus1/Projekt — [Open access]

[52] Open Source Observatory (OSOR). (2024). *OSOR Handbook, updated edition*. Brussels: European Commission / Interoperable Europe Portal. https://interoperable-europe.ec.europa.eu/collection/open-source-observatory-osor — [© European Union, open access]

[53] ITU / DIAL. (2023). *GovStack: Building Block Specifications for Digital Government*. Geneva: ITU. https://www.govstack.global/ — [Open access]

[54] German Federal Government. (2025). *Koalitionsvertrag 2025: Deutschland-Stack und digitale Souveränität*. Berlin: Bundesregierung. https://www.bundesregierung.de/ — [DL-DE/Zero 2.0]

[55] Sovereign Cloud Stack Community / OSBA. (2025). *Sovereign Cloud Stack Release 8 — April 9, 2025*. Berlin: OSBA. https://sovereigncloudstack.org/announcements/release8/ — [Apache 2.0]

[56] OSOR / The Register. (2018). *Munich's return to Windows: €100 million cost estimate*. Sources: https://interoperable-europe.ec.europa.eu/collection/open-source-observatory-osor/document/munichs-long-history-open-source-public-administration | https://theregister.com/2018/01/04/munich_linux_costs_ownership — [Open access]

[57] Bundesamt für Sicherheit in der Informationstechnik (BSI). (2025). *NIS-2-Umsetzungsgesetz in Kraft (2025-12-05); BSI IT-Grundschutz++ Katalog ab 2026-01-01*. Bonn: BSI. https://www.bsi.bund.de/DE/Service-Navi/Presse/Pressemitteilungen/Presse2025/251205_NIS-2-Umsetzungsgesetz_in_Kraft.html — [Open access]

[58] Nextcloud GmbH. (2025). *Nextcloud 2025 Wrap-Up: 500,000 servers, government adoptions*. Stuttgart: Nextcloud. https://nextcloud.com/blog/nextcloud-2025-wrap-up/ — [Open access]

[59] BWI GmbH / Element / OSOR. (2023–2025). *BundesMessenger: Matrix-based messaging for German public administration. Launched December 2023; Dataport deployment 500,000 users planned.* https://interoperable-europe.ec.europa.eu/collection/open-source-observatory-osor/news/bundesmessenger-shared-reused-and-interoperable | https://element.io/matrix-in-germany/projects/bundesmessenger — [Open access; code: Apache 2.0]

[60] Netherlands Ministry of the Interior / OSPO. (2026). *code.overheid.nl: Sovereign Forgejo-based code forge for Dutch government open source*. The Hague. https://www.opensourceforu.com/2026/04/dutch-government-backs-forgejo-for-sovereign-open-source-github-alternative/ — [Open access; Forgejo: MIT]

[61] TYPO3 GmbH. (2024). *TYPO3 for the Public Sector: Government Site Builder 11. 35% of German government websites on TYPO3.* https://typo3.com/solutions/industries/public-sector — [GPL-2.0]

[62] European Commission / Interoperable Europe Portal. (2024). *Funding Opportunities for Open Source Software Projects in the Public Sector. Digital Europe Programme 2021–2027: €8.1bn; €1 OSS investment = €4 economic value.* https://interoperable-europe.ec.europa.eu/collection/open-source-observatory-osor/funding-opportunities-open-source-software-projects-public-sector — [© EU, open access]

[63] The Document Foundation. (2025). *LibreOffice*. https://www.libreoffice.org/ — [MPL-2.0]; Collabora Online: https://www.collaboraonline.com/ — [MPL-2.0]

[64] European Parliament and Council. (2024). *Regulation (EU) 2024/1689 — Artificial Intelligence Act, in force 2024-08-01, high-risk provisions applicable from 2026-08-02*. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689 — [EU legislation, public domain]

---

*This document is released under the Creative Commons Attribution 4.0 International Licence (CC-BY-4.0).*  
*Attribute as: Sebastian Graf, Autonomous Office of Civil Digital Infrastructure (sebk4c@tuta.com)*  
*Published at: https://github.com/SEBK4C/Strategy-for-City-GovTech*
