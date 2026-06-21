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
  - OpenDesk
  - eCH standards
  - GovStack
  - total cost of ownership
changelog:
  - version: "0.2.0"
    date: "2026-06-21"
    changes:
      - "Added Section 3.6 — Total Cost of Ownership Evidence (critical gap addressed)"
      - "Added Section 3.7 — Small Municipality Case Studies (critical gap addressed)"
      - "Added Section 3.8 — ZenDiS and Institutional Architecture"
      - "Added coverage of eCH standards, CONSUL Democracy, GovStack, Swiss e-ID (v0.2)"
      - "Added EU Data Act [51] and Data Governance Act [52]"
      - "Added Section 4.11 — Cross-border Interoperability Standards"
      - "Added Section 5.6 — Small Municipality Implementation Track"
      - "Expanded risk register with EU Data Act and smart city compliance"
      - "16 new sources added to registry (47–62); total 62 verified sources"
      - "All previously-unverified citations reviewed; 4 remain partially verified"
  - version: "0.1.0"
    date: "2026-06-20"
    changes:
      - "First structured draft — complete structure, 46 sources"
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

Municipal governments are the closest layer of democratic administration to citizens, yet they face an acute structural tension: the digital tools they depend on are increasingly proprietary, vendor-locked, and misaligned with public-interest values. This paper presents a comprehensive strategy for implementing a state-of-the-art, open-source governmental administration technology stack in city governments. Drawing on exemplary practices from the Swiss federal administration's EMBAG legislation, Germany's OZG reform programme, ZenDiS and the Sovereign Cloud Stack initiative, and the wider European sovereign technology community — including the GovStack building-block framework, CONSUL Democracy, and the eVaka shared-resource model — we derive a first-principles implementation roadmap, stakeholder engagement framework, and procurement strategy applicable to municipalities of all sizes.

We evaluate the core technology components — identity management, document management, workflow automation, citizen participation, secure communications, open data publication, geographic information systems, public websites, and cloud infrastructure — against criteria of digital sovereignty, interoperability, total cost of ownership, and civic alignment. We also survey the evolving EU regulatory landscape, including the Interoperable Europe Act (2024), the EU Data Act (2023, applies September 2025), and the Data Governance Act (2022), which together create binding obligations that render proprietary, vendor-locked infrastructure increasingly costly to maintain.

We present empirical total cost of ownership evidence: the French Gendarmerie's GendBuntu project achieved a 40% TCO reduction and €2 million in annual licence savings across 103,164 workstations; the City of Toulouse documented €1.8 million in savings over three years following open-source desktop migration. We conclude that open-source municipal technology stacks are not merely technically viable but fiscally superior, democratically necessary, legally mandated in an increasing number of jurisdictions, and now supported by a mature institutional ecosystem including ZenDiS, govdigital eG, and the GovStack initiative. The paper provides a phased 36-month implementation roadmap with a small-municipality track and concrete procurement guidance for city administrators, elected officials, IT teams, and civil-society stakeholders.

**Keywords:** digital sovereignty, open source government, GovTech, municipal digital transformation, interoperability, OZG, EMBAG, Sovereign Cloud Stack, e-government, civic technology, ZenDiS, OpenDesk, eCH standards, GovStack, total cost of ownership

---

## 1. Introduction

The digital transformation of municipal government is no longer optional. Citizens expect seamless, secure, and accessible digital services; regulators demand interoperability and data protection; and fiscal pressures require sustainable, cost-effective technology investments. Yet the majority of city governments worldwide remain trapped in a cycle of proprietary vendor dependency, expensive licence agreements, and fragmented systems that impede rather than enable good governance [1, 29].

The consequences of this dependency are well-documented: vendor lock-in raises switching costs and bargaining asymmetry [4]; proprietary formats obstruct cross-agency data exchange and transparency [45]; closed-source infrastructure prevents independent security auditing [26]; and recurring licence fees drain budgets that could otherwise fund service delivery [3, 5]. Most fundamentally, when the software running democratic institutions is owned and controlled by private actors, a structural conflict of interest emerges between the public interest and corporate imperatives [4]. The foundational argument, articulated most clearly by Lathrop and Ruma in *Open Government* (2010), is that the data generated by democratic processes and the software that governs those processes should, as a default, be available to the public that pays for them [60].

A different path is both possible and proven. Switzerland's 2023 EMBAG legislation mandates that federal software developed with public funds be released as open source by default [1]. Germany's OZG reform programme, ZenDiS and its OpenDesk initiative, the Sovereign Cloud Stack, and the openCode.de platform represent the most ambitious coordinated open-source government technology programme in Europe [2, 3, 42, 47]. The Free Software Foundation Europe's "Public Money? Public Code!" campaign, now endorsed by over 200 organisations across 30 countries, articulates the democratic principle at stake: software paid for by the public should be available to the public [4]. And the 2024 Interoperable Europe Act creates binding cross-border interoperability obligations that proprietary, closed stacks will find increasingly difficult to satisfy [6].

This paper synthesises these developments into a practical strategy for municipal governments. It is addressed to all relevant stakeholders — city administrators, elected officials, public-sector IT teams, procurement offices, civil-society groups, open-source communities, and sovereign technology providers — and provides the evidence base, technology assessment, and implementation roadmap needed to make the transition.

### 1.1 Scope and Definitions

*Municipal government* refers to city and local government authorities, including Gemeinden, Kommunen, Städte, and equivalent structures in Swiss cantons. The strategy is designed to scale from small municipalities (population 5,000–50,000) to large cities (population 500,000+), with modulation provided in the small-municipality track in Section 5.6.

*Open-source technology stack* refers to software components licensed under OSI-approved licences, deployed on infrastructure that the municipality controls or can migrate away from without undue cost or friction.

*Digital sovereignty* is the ability of a government to make independent decisions about its digital infrastructure, including the right to inspect, modify, audit, and migrate software without dependency on a single vendor [3, 59].

### 1.2 Research Questions

1. What does a state-of-the-art open-source municipal technology stack look like in 2026?
2. What lessons can be drawn from the Swiss, German, and European sovereign technology communities?
3. What is the optimal phased implementation pathway for city governments of varying sizes?
4. How should procurement, stakeholder engagement, and risk management be structured to maximise success probability?

---

## 2. Methodology

This paper employs a multi-method research design combining:

**Systematic literature review** of peer-reviewed publications, grey literature, and policy documents published between 2010 and 2026, covering e-government theory, digital sovereignty, open-source software in public administration, and municipal digital transformation. The literature review is designed to be self-improving: the source registry (`Mem/source-registry.md`) and literature review state (`Mem/literature-review-state.md`) are versioned documents updated on a recurring basis, and `Scripts/update_literature_review.py` provides structured prompts for reviewing and improving these files on a quarterly cadence.

**Comparative policy analysis** of technology legislation and strategies from Switzerland (EMBAG 2023 [1], E-Government Strategy 2024–2027 [16], Digital Switzerland Strategy 2025 [61], e-ID Act 2024 [56]), Germany (OZG 2017/2024 [2], ZenDiS mandate [47], openCode.de [10]), and the European Union (Interoperable Europe Act 2024 [6], EU Open Source Strategy 2020–2023 [5], EU Data Act 2023 [51], Data Governance Act 2022 [52]).

**Technology stack evaluation** using a structured scoring matrix assessing each component on: (a) licence openness, (b) deployment maturity, (c) community health, (d) interoperability standards compliance, (e) security posture, (f) total cost of ownership, and (g) existing public-sector deployments.

**Stakeholder analysis** mapping the interests, influence, and engagement needs of each stakeholder group in the municipal digital transformation process.

**Total cost of ownership analysis** drawing on available empirical case studies from France, Italy, and Czech Republic to provide quantitative reference points for municipal budget planning.

### 2.1 Inclusion Criteria

Sources were included if they: (a) address open-source software in public administration; (b) cover governmental digital transformation strategy; (c) relate to the European, Swiss, or German regulatory context; or (d) provide primary data on municipal technology implementations. Sources published before 2010 were included only where they establish foundational theoretical frameworks.

### 2.2 Limitations

This paper is a citation-complete draft (v0.2.0). Four citations remain partially verified against primary sources; these are noted in the source registry. Technology stack assessments reflect publicly available information as of June 2026. Implementation cost estimates are indicative and must be validated against local procurement conditions. The total cost of ownership analysis draws on desktop/productivity suite migration data; a comprehensive full-stack TCO study covering the complete municipal administration stack does not yet exist in the peer-reviewed literature — this is documented as a gap for v1.0.

---

## 3. Literature Review

### 3.1 Theoretical Foundations of E-Government

The academic literature on e-government has evolved through four broad phases [30]. First-generation e-government (1995–2005) focused on digitising existing processes and creating government websites [29]. Second-generation e-government (2005–2012) emphasised online service delivery, citizen portals, and back-office integration [7]. Third-generation e-government (2012–2020) introduced open data, participatory platforms, and mobile-first service design [8]. The current fourth generation (2020–present) is characterised by platform government, digital identity infrastructure, data spaces, and the sovereignty turn — a recognition that digital autonomy is a prerequisite for democratic self-governance [45].

Wirtz and Weyerer's holistic e-government maturity model identifies five dimensions: technical infrastructure, process quality, service quality, citizen orientation, and transparency [7]. Municipal governments in Switzerland and Germany score variably across these dimensions; technical infrastructure and process quality lag citizen expectations in most jurisdictions, while the regulatory environment increasingly mandates transparency and interoperability [1, 2, 45].

The philosophical foundations of this shift were articulated prescriptively by Lathrop and Ruma in *Open Government* (2010), which argued that government data, generated through public processes and funded by public money, should be open by default [60]. The book's central argument — that openness is not merely a technical choice but a democratic obligation — has been progressively codified into law, from the EU's Open Data Directive to EMBAG and OZG 2.0.

The UN E-Government Survey 2022 found that digital government services are increasingly central to citizen trust in public institutions [29]. Countries and cities that offer seamless, inclusive, and rights-respecting digital services are not merely more efficient; they are more legitimate in the eyes of their citizens.

The European Parliamentary Research Service's 2023 study on digital sovereignty in public administration [59] consolidates the academic consensus: digital sovereignty is not achievable through policy statements but only through concrete infrastructure choices — primarily open-source software, sovereign cloud infrastructure, and open standards. The EPRS study explicitly endorses the Sovereign Cloud Stack approach as a model for EU public administration.

### 3.2 Digital Sovereignty in Public Administration

The concept of digital sovereignty — the capacity of public institutions to make independent, auditable decisions about their digital infrastructure — has moved from academic concept to policy imperative in the European context [3, 5, 59]. The EU Open Source Strategy 2020–2023 established "sharing and reuse" as a core principle, mandating that European institutions prefer open-source solutions in technology procurement [5]. The 2024 Interoperable Europe Act creates binding obligations for cross-border interoperability in public administrations [6].

Germany's Sovereign Cloud Stack (SCS), developed by the Open Source Business Alliance (OSBA) and funded in part by the German Federal Ministry for Economic Affairs and Climate Action (BMWK), represents the most concrete realisation of digital sovereignty in cloud infrastructure [3]. SCS provides a fully open-source, self-hostable cloud platform (OpenStack + Kubernetes + Ceph) that enables public administrations to operate infrastructure that is technically and legally sovereign [11]. SCS-certified cloud operators including plusserver and OSISM provide managed hosting for municipalities that lack in-house cloud operations capacity. The govdigital eG cooperative offers SCS-based shared infrastructure under framework agreements that satisfy German public procurement law [23].

Switzerland's approach differs institutionally but converges on the same principles. The EMBAG legislation (Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben), which entered into force on 1 January 2024, requires all federal software developed with public funds to be released as open source unless compelling security reasons prevent it [1]. The law places Switzerland among the most progressive open-source mandating jurisdictions in the world, ahead of France, Italy, and Germany in the strength of its mandate.

The 2025 Digital Switzerland Strategy identifies digital sovereignty as a cross-cutting priority, closely linked to the deployment of the Swiss e-ID and open data infrastructure [61]. The strategy sets out a collaborative framework for digital services that explicitly mandates open standards, interoperability via eCH standards, and public availability of government-funded software.

The EU Data Act (Regulation EU 2023/2854), in force from January 2024 and applying from September 2025, extends digital sovereignty obligations in a new direction [51]. Municipalities deploying smart city infrastructure — sensors, smart meters, connected public transport, public WiFi networks — must ensure that data generated by these connected devices is accessible and portable under the Data Act's provisions. This creates a new compliance requirement favouring open protocols and sovereign data management.

The Data Governance Act (Regulation EU 2022/868), applying from September 2023, creates an enabling framework for European common data spaces and recognises "data altruism" as a legitimate organisational form [52]. Municipalities can register as data altruism organisations, enabling structured civic data sharing and participation in European data spaces for health, mobility, energy, and other domains relevant to municipal services.

### 3.3 The German OZG Ecosystem

The Onlinezugangsgesetz (OZG), enacted in 2017 and substantially reformed in 2024 (OZG 2.0), requires all German federal, Land, and municipal administrations to offer their administrative services online [2]. The OZG 2.0 reform addresses shortcomings of the first generation — including fragmented implementation, poor interoperability, and inconsistent user experience — through the "Once Only" principle, the "Einer für Alle" (EfA) approach to shared service development, and a federal platform architecture centred on BundID and FITKO [9, 10].

**Implementation progress** as of early 2025 is mixed [62]. The federal government had digitalized its 115 prioritized OZG services by end 2024. However, only 196 of the 575 state-level administrative services were available nationwide by early 2025 — less than 34% of the target. Municipal services lag state services significantly. The OZG implementation demonstrates that political mandate alone is insufficient without a supporting institutional infrastructure to carry municipalities across the capability threshold.

**BundID**, Germany's central digital identity service, had approximately 5.3 million active accounts at the end of 2024, rising to approximately 6 million by March 2025, with 154,000 new accounts added monthly since May 2025 [62]. Monthly login volume doubled from approximately 1 million to 2 million between 2024 and 2025. These are encouraging trends, but at 7.5% of 72 million eligible citizens, BundID remains far from the adoption levels needed for digital-first municipal services. Municipalities should design Keycloak identity federations that support BundID as the high-assurance pathway while offering accessible fallback authentication flows with clear upgrade paths.

**ZenDiS GmbH** (Zentrum Digitale Souveränität der Öffentlichen Verwaltung) is the institutional actor that connects the federal OZG mandate with practical municipal implementation [47]. Founded in December 2022 by the Federal Ministry of the Interior (BMI), ZenDiS manages OpenDesk and co-manages openCode.de. OpenDesk — a curated open-source workplace suite built around Nextcloud, Cryptpad, OpenProject, Jitsi, Element, and Collabora Office — was officially launched as a SaaS offering at the end of 2024. ZenDiS also targeted tenders for marketing licences in Q1 2026, making OpenDesk available to municipalities through a structured procurement pathway. ZenDiS represents the most important institutional partner for German municipalities pursuing open-source digital transformation.

**The openCode.de platform** [10], hosted by Digitalservice GmbH des Bundes and coordinated with ZenDiS, provides a centralised repository for government open-source software with over 300 repositories. The EfA principle — building one high-quality service once and making it available to all municipalities — is the operational logic of openCode.de and the cooperative procurement approach.

Fraunhofer IESE's 2024 research on municipalities and open-source software [58] confirms the primary findings of this paper: the barriers to municipal OSS adoption are not technical (software maturity is sufficient) but organisational and political. Personnel resistance to change, lack of internal OSS expertise, and interoperability challenges with Länder systems are the binding constraints. This validates the emphasis in the implementation roadmap (Section 5) on change management, training, and cooperative IT provision over technical depth.

### 3.4 Swiss Cantonal and Federal Digital Services

Switzerland's federal structure creates both challenges and opportunities for municipal digital transformation. Key Swiss digital infrastructure includes:

- **Fedlex** (fedlex.admin.ch): the official platform for Swiss federal law, built on open standards and providing machine-readable legal data [1].
- **opendata.swiss**: the national open government data portal, built on CKAN and cataloguing thousands of datasets from federal, cantonal, and municipal authorities [44].
- **GEVER**: the standardised records management system for the federal administration, providing a template for cantonal and municipal implementations [43].

The E-Government Strategy Switzerland 2024–2027 sets out a collaborative framework for digital services that explicitly mandates open standards and interoperability [16]. The 2025 Digital Switzerland Strategy [61] reinforces this with specific emphasis on the e-ID as a foundational digital infrastructure element.

**eCH Standards** [49] provide the Swiss equivalent of Germany's XÖV/KoSIT family of interoperability standards. The eCH association promotes, develops, and adopts e-government standards for Switzerland, enabling electronic cooperation between government bodies (G2G), and between government bodies and citizens (G2C), businesses (G2B), and organisations. Standards have the formal status of recommendations but can be declared binding by federal, cantonal, or municipal authorities. The Swiss Federal Chancellery publishes eCH standards as a mandatory reference framework for Swiss e-government.

Key eCH standards for municipal digital transformation include:
- **eCH-0007**: Historicised municipal directory — canonical source of Swiss Gemeinde identifiers
- **eCH-0010**: Postal address format — standard for address data exchange
- **eCH-0044**: Person identification — standard for citizen identifiers
- **eCH-0058**: Delivery interface — standard for secure document delivery between authorities
- **eCH-0211**: Building application — enables data exchange between municipalities and cantons while preserving autonomous local business processes (canton of Zurich implementation reference)

The **Swiss e-ID** represents a transformative development for Swiss municipal digital services [56]. The Federal Act on Electronic Identification Services (BGEID) was passed by the Swiss Parliament on 20 December 2024 and approved by Swiss voters in a referendum on 28 September 2025, with 50.39% voting in favour. The narrow margin reflects lingering concerns about digital identity systems, but the approval establishes a clear legal mandate. The system is entirely state-managed, with no central data storage — a deliberate design choice informed by the 2021 referendum rejection of a private-company-issued e-ID (64.4% against). The budget for development and operation is CHF 182 million for 2023–2028. A public beta opened in early 2025, and the e-ID is targeted for summer 2026 rollout. Following the e-ID launch, cantons will offer the digital driving licence (mDL-Suisse) via the federal wallet. Municipal deployments should plan Keycloak federation with the Swiss e-ID system as the primary authentication pathway for high-assurance citizen services.

### 3.5 Open-Source Communities and Sovereign Technology

**Decidim** (Barcelona, 2016) is a participatory democracy platform used by over 400 organisations in 40 countries, including the cities of Barcelona, Helsinki, and the Swiss canton of Schaffhausen [12]. Its governance model — a multi-stakeholder association with a published social contract — is itself a model for open-source sovereignty in public administration. Decidim's strength is greatest in Northern and Western Europe; its multilingual support for German, French, and Italian makes it particularly well-suited to Swiss and German municipal deployments.

**CONSUL Democracy** (Madrid, 2015) is a complementary participatory platform with a distinct geographic reach [50]. Originally developed by the Madrid City Council for the Decide Madrid platform, CONSUL has 250+ deployments globally, supports 45 languages, and enables over 100 million citizens worldwide to participate in civic decision-making through CONSUL-powered platforms. Its features include proposals, participatory budgeting, debates, crowd laws, and consultations. The CONSUL Democracy Foundation, established in 2019, ensures continued open-source maintenance following the decline of political support from the Madrid City Council after elections — itself a cautionary parallel to the Munich LiMux case. The EU Open Source Observatory has published a case study of CONSUL as a reference implementation [55]. For Swiss and German municipalities: Decidim is the primary recommendation due to its stronger Northern European community and German-language support; CONSUL is the recommended alternative for cities with trans-national participation programmes or Southern European partnerships.

**Matrix/Element** provides an open, decentralised, end-to-end-encrypted communication protocol increasingly adopted by European public administrations [14]. The German federal BundesMessenger and the French government's Tchap both operate on Matrix. E2E encryption by default makes Matrix the appropriate standard for inter-agency secure communications.

**Nextcloud** (Stuttgart, 2016) is the most widely deployed open-source file sync and collaboration platform in European public administration, used by thousands of German municipalities, the Swiss Federal Administration, and dozens of EU institutions [13]. Its integration with Keycloak (SSO), OpenProject (project management), and Collabora Office (document editing) makes it the connective tissue of a modern open-source municipal workplace.

**OpenDesk** [42], launched at end of 2024 by ZenDiS GmbH, is a curated open-source workplace suite built around Nextcloud, Cryptpad, OpenProject, Jitsi, Element, and Collabora Office, available as SaaS. It represents the first government-curated open-source workplace suite at scale and is the reference implementation for German municipalities. German municipalities can access OpenDesk through the ZenDiS service offering without procuring individual components separately.

**GovStack** [48] is a multi-stakeholder initiative led by the International Telecommunication Union (ITU), the Digital Impact Alliance (DIAL), Germany's Federal Ministry for Economic Cooperation (BMZ), and Estonia. GovStack provides nine digital "building block" specifications — covering payments, registries, identification, digital messaging, information mediation, consent, e-signature, geographic information systems, and scheduling — which governments can use to build interoperable digital services from modular, vendor-neutral components. GovStack has been applied in Montenegro (December 2024, covering 25 local self-governments), Rwanda, Kenya, and Ethiopia. For Swiss and German municipalities, GovStack provides a procurement and architecture reference framework that complements the specific component recommendations in Section 4: using GovStack's specifications in tender documents ensures international interoperability and avoids specifying proprietary solutions. The ITU Academy offers training on GovStack implementation.

### 3.6 Total Cost of Ownership Evidence

One of the most significant gaps in the v0.1.0 draft was the absence of rigorous TCO data. This section documents the available empirical evidence.

**French Gendarmerie GendBuntu** [53]: The French National Gendarmerie began migrating its computing estate to Linux (Ubuntu) and LibreOffice in 2004. By June 2024, 103,164 workstations — representing 97% of the Gendarmerie's entire computing estate — were running the open-source stack. Documented outcomes: approximately 40% reduction in total cost of ownership and approximately €2 million in annual savings on software licences alone. This is the largest and longest-running documented open-source government desktop migration and provides the most robust TCO baseline.

**City of Toulouse** [54]: The City of Toulouse documented savings of €1.8 million over three years following migration of 90% of its municipal desktops to open-source solutions. This is a municipal-scale reference point directly comparable to the municipalities targeted by this strategy.

**French state (ministries)** [53]: Eleven French ministries have installed LibreOffice on 500,000 workstations. The Occitanie region launched a digital independence strategy in 2023 following a significant increase in its Microsoft contract costs, opting pragmatically for open-source alternatives — illustrating the escalating cost risk of proprietary dependency.

**Province of Bolzano-Bozen, Italy**: A transition to open-source desktop software (OpenOffice suite) across municipalities in the Province of Bolzano-Bozen provided a documented learning: "tackling correctly personnel resistance to change may be the most important factor for a successful transition." Technical implementation was smooth; human change management was the binding constraint — consistent with the Munich LiMux experience and Fraunhofer IESE's findings [58].

**Methodological note**: No rigorous independent comparative TCO study covering the full open-source vs. proprietary *municipal administration* stack (identity management, document management, workflow automation, citizen portal, open data portal, and cloud infrastructure together) exists in the peer-reviewed or grey literature. The available evidence focuses on desktop/productivity suite migration. A five-year TCO model for the full stack should include: (a) licence costs eliminated (typically €100–300/user/year for productivity software; significantly higher for enterprise platforms); (b) implementation and migration costs (one-time); (c) hosting on sovereign infrastructure vs. proprietary cloud; (d) support contracts; (e) training and change management; (f) exit costs (zero for open-source vs. significant lock-in premium for proprietary); and (g) opportunity value of feature development owned by the municipality vs. roadmap dependency on a single vendor. This TCO methodology is documented in the source registry for future municipal cost-benefit analyses.

**TCO summary**: The available evidence consistently shows 30–40% cost reductions achievable through open-source desktop migration at scale. For full-stack municipal transformation, the cost profile shifts: implementation costs are higher upfront (due to integration work and change management), but long-term operational costs are lower due to eliminated licence fees, and exit costs are essentially zero. Cooperative procurement structures (govdigital eG, cantonal IT cooperatives) spread implementation costs across many municipalities, improving the economic case for smaller Gemeinden.

### 3.7 Small Municipality Case Studies

The majority of documented open-source government technology case studies involve large cities (Barcelona, Helsinki, Munich) or federal agencies. The median European municipality has a population under 10,000, and the strategies and economics for small municipalities are substantially different. This section documents available evidence for smaller contexts.

**eVaka — Espoo, Finland** [57]: The City of Espoo developed eVaka as an open-source early education management platform, handling everything from applications to daily operations for childcare and preschool services. A critical success factor was the *shared resource model*: multiple Finnish municipalities pool resources for training, system maintenance, and feature updates. This is the Finnish equivalent of Germany's EfA (Einer für Alle) approach. Result: reduced costs for all participating municipalities, accelerated feature improvements, and a platform that is now available on GitHub under LGPL-2.1 for any municipality globally. The eVaka model demonstrates that small municipalities can achieve the benefits of high-quality digital services through cooperation rather than individual capability.

**Cityvizor — Czech Republic**: Cityvizor is an open-source municipal budget transparency platform that transforms complex financial information into an accessible, searchable public interface. Its modular design enables adoption by multiple municipalities with minimal customisation. The shared governance model — where participating municipalities collectively shape the roadmap — ensures the platform remains responsive to local needs without any single municipality bearing the full development cost. This model is analogous to the Decidim Association's governance structure.

**Province of Bolzano-Bozen, Italy**: As noted in Section 3.6, the desktop migration across municipalities in this alpine province provides direct evidence from a small-municipality context. The province's linguistic complexity (German, Italian, and Ladin) adds an additional layer of relevance for Swiss municipalities with multilingual obligations.

**EfA services for small German municipalities**: The OZG EfA (Einer für Alle) approach specifically addresses the challenge that most German municipalities are too small to develop their own digital services independently. Under EfA, one Land or consortium develops a high-quality digital service and makes it available to all municipalities through openCode.de and the shared infrastructure provided by Dataport, AKDB, and equivalent cooperative IT providers [24]. This approach is the most economically efficient model for municipalities below approximately 50,000 population and should be the default starting point for small-municipality digital transformation in Germany.

**Key insight**: The binding constraint for small municipalities is not technical capability but *cooperative participation*. Municipalities that join govdigital eG, participate in EfA consortia, adopt OpenDesk from ZenDiS, or share resources through cantonal IT cooperatives gain access to enterprise-grade open-source capabilities at a fraction of the cost of individual implementation. The implementation roadmap in Section 5.6 reflects this principle.

### 3.8 ZenDiS and the Institutional Architecture for German Municipal Digital Sovereignty

ZenDiS GmbH (Zentrum Digitale Souveränität der Öffentlichen Verwaltung) [47] deserves dedicated treatment as a pivotal institutional actor that was under-covered in the v0.1.0 draft. Founded in December 2022 by the Federal Ministry of the Interior (BMI), ZenDiS operates at the intersection of federal policy and municipal implementation. Its mandate is to reduce digital dependency across German public administration and to coordinate the open-source strategy that makes digital sovereignty operational rather than rhetorical.

ZenDiS manages two key products: **OpenDesk** [42] — the government open-source workplace suite officially launched end of 2024 as a SaaS for public administrations — and **openCode.de** [10] — the central repository for government open-source software. The significance of ZenDiS for municipal procurement is twofold: first, it provides a pre-vetted, government-curated open-source stack that municipalities can adopt without conducting their own independent software evaluation; second, it represents a contractual partner whose mandate includes serving the entire public administration, not only federal agencies.

The relationship between ZenDiS, govdigital eG [23], and the Sovereign Cloud Stack [3] creates an integrated institutional ecosystem for digital sovereignty: ZenDiS curates and manages the application stack; govdigital eG provides cooperative cloud infrastructure (SCS-based); and openCode.de serves as the shared code repository. Together, these three institutions provide German municipalities with a complete, sovereign digital infrastructure pathway that no individual municipality needs to assemble from scratch.

### 3.9 Gaps in the Literature

As of v0.2.0, the following gaps remain:

1. **Post-2022 e-government theory**: The literature review theory section relies primarily on Wirtz/Weyerer (2017) and Janowski (2015). Academic literature on fourth-generation e-government, platform government, and AI in public services published 2022–2026 has not yet been systematically reviewed.
2. **Full-stack TCO studies**: No rigorous independent study covers the complete municipal administration stack (identity + document management + workflow + portal + open data + cloud).
3. **User experience research**: Almost no peer-reviewed literature exists on citizen satisfaction comparing open-source and proprietary municipal digital services.
4. **BundesMessenger adoption data**: Precise deployment statistics for the German federal BundesMessenger and Länder-level expansions are not publicly available.
5. **GAIA-X for municipalities**: The practical tools available to municipalities through GAIA-X (as distinct from the SCS) remain unclear as of June 2026.

See `Mem/literature-review-state.md` for the full gap analysis and improvement roadmap.

---

## 4. Technology Stack Analysis

A municipal technology stack can be decomposed into nine functional layers plus a cross-cutting interoperability framework. The analysis below evaluates the leading open-source options for each layer against the scoring criteria defined in Section 2.

### 4.1 Digital Identity and Authentication

**Function:** Authenticate citizens and staff; federate identity across services; implement single sign-on (SSO).

**Recommended component: Keycloak** (Red Hat / CNCF) [21]

Keycloak is the de facto open-source identity and access management (IAM) platform for European public administration. It implements OpenID Connect, OAuth 2.0, SAML 2.0, and FIDO2, enabling federation with national identity systems (BundID in Germany [62], Swiss e-ID in Switzerland [56]). It is deployed by numerous European governments including EU institutions, German Länder, and Swiss cantons.

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Licence openness | 5 | Apache 2.0 |
| Deployment maturity | 5 | Production-proven, 10+ years |
| Community health | 5 | Large, active, CNCF-supported |
| Interoperability | 5 | OIDC, OAuth2, SAML2, FIDO2 |
| Security posture | 5 | CVE-responsive, widely audited |
| TCO | 4 | No licence cost; ops expertise required |
| Public-sector deployments | 5 | Widespread EU government use |

**Integration note (Germany):** Configure BundID as external IdP via OIDC. Design fallback flows for users without BundID, with clear upgrade path. Map AAL (Authenticator Assurance Levels) to service risk tiers.

**Integration note (Switzerland):** Plan OIDC federation with Swiss e-ID wallet (available summer 2026). eCH-0044 person identifiers provide the canonical citizen identifier across Keycloak and downstream systems [49, 56].

### 4.2 Document Management and Records

**Function:** Store, retrieve, classify, and retain official records; manage GEVER-compliant workflows.

**Recommended components: Nextcloud** [13] + **OpenProject** [20]

Nextcloud provides the collaborative file management layer; OpenProject handles project and records linking. For Swiss municipalities requiring full GEVER compliance, cantonal GEVER solutions (CMI, Fabasoft Community) provide the compliance layer with Nextcloud as the collaborative front-end. File exchange with cantonal authorities uses eCH-0058 (delivery interface) for secure document delivery [49].

For German municipalities, AKDB's BayernPortal and Dataport components provide equivalent capability within OZG/XÖV [46] compliance frameworks.

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Licence openness | 5 | AGPL-3.0 (Nextcloud) |
| Deployment maturity | 5 | 400,000+ organisations |
| Community health | 5 | Nextcloud GmbH + community |
| Interoperability | 4 | WebDAV, CalDAV, CardDAV, CMIS, eCH-0058 |
| Security posture | 5 | ISO 27001 certified offering |
| TCO | 5 | No per-seat licence (Community) |
| Public-sector deployments | 5 | Swiss federal, German states |

### 4.3 Workflow Automation and Business Process Management

**Function:** Automate administrative workflows; model, execute, and monitor BPMN processes.

**Recommended component: Camunda Platform 8 Community** [33]

Camunda provides a BPMN 2.0-native workflow engine with strong support for complex multi-step administrative processes and XÖV data standards integration [46]. **Flowable** (Apache 2.0) is a lighter-weight alternative for municipalities where Camunda's dual-licensing model creates procurement complications. For Switzerland, eCH-0058 and eCH-0044 compliance in workflow data exchange is essential [49].

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Licence openness | 4 | Community: Apache 2.0; Enterprise: proprietary |
| Deployment maturity | 5 | Production-proven |
| Community health | 4 | Active; enterprise tier funds development |
| Interoperability | 5 | BPMN 2.0, REST API, event-driven, XÖV/eCH |
| Security posture | 4 | Actively maintained |
| TCO | 3 | Community free; scale may need Enterprise |
| Public-sector deployments | 4 | Multiple German Länder |

### 4.4 Citizen Participation

**Function:** Consultation, participatory budgeting, initiative collection, deliberation platforms.

**Primary recommendation: Decidim** [12]

Decidim is the most mature and widely adopted open-source participation platform in Northern and Western Europe. Use by Barcelona, Helsinki, the canton of Schaffhausen, and the City of New York validates it across regulatory and linguistic contexts. The Decidim Association provides governance, a social contract, and a global community of practice. Strong German-language support and active Swiss and German municipal deployments make Decidim the primary recommendation for this strategy's target audience.

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Licence openness | 5 | AGPL-3.0 |
| Deployment maturity | 5 | 400+ deployments globally |
| Community health | 5 | Active association and community |
| Interoperability | 4 | REST API, webhooks |
| Security posture | 4 | Actively maintained |
| TCO | 5 | No licence cost |
| Public-sector deployments | 5 | Cities, cantons, federal agencies |

**Alternative: CONSUL Democracy** [50]

CONSUL Democracy (Madrid, 2015; CONSUL Democracy Foundation, 2019) is the leading alternative, with 250+ global deployments, 45 languages, and over 100 million citizens served. CONSUL is particularly strong in Spanish-speaking municipalities and cities with trans-national participation programmes.

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Licence openness | 5 | AGPL-3.0 |
| Deployment maturity | 5 | 250+ deployments, 100M+ citizens |
| Community health | 4 | Foundation-maintained, active |
| Interoperability | 4 | REST API |
| Security posture | 4 | Actively maintained |
| TCO | 5 | No licence cost |
| Public-sector deployments | 5 | Cities globally; OSOR case study [55] |

**Selection guidance:** For Swiss/German municipalities with primarily German-speaking participation processes, Decidim is recommended. For cities with significant Southern European diaspora populations or international participation partnerships, CONSUL Democracy is a valid equal alternative. Both platforms can be run simultaneously for different participation processes if needed.

### 4.5 Communication and Collaboration

**Function:** Internal messaging, video conferencing, email, calendar; secure inter-agency communication.

**Recommended components:**
- **Matrix/Element** for messaging and inter-agency secure communication [14]
- **Jitsi Meet** or **BigBlueButton** for video conferencing [34, 35]
- **Nextcloud Talk** for integrated team communication [13]

The German federal BundesMessenger (built on Matrix) and the French government's Tchap provide reference deployments applicable to municipal contexts. E2E encryption by default makes Matrix the appropriate standard for sensitive inter-agency communications.

| Component | Licence | Maturity | Key advantage |
|---|---|---|---|
| Matrix/Element | Apache 2.0 | Production | E2E encryption, federation |
| Jitsi Meet | Apache 2.0 | Production | Browser-based, self-hostable |
| BigBlueButton | LGPL-3.0 | Production | Council meeting focus |
| Nextcloud Talk | AGPL-3.0 | Production | Integrated with file management |

**OpenDesk integration note (Germany):** All communication components (Jitsi, Element) are included in OpenDesk [42]. German municipalities using OpenDesk receive these as part of the integrated SaaS offering from ZenDiS [47].

### 4.6 Open Data Publication

**Function:** Publish machine-readable datasets; catalogue data; provide API access; comply with PSI/Open Data directives and DCAT-AP standards.

**Recommended component: CKAN** [22]

CKAN is the world's leading open-source open data portal software. It powers opendata.swiss, data.gov, data.gov.uk, and dozens of national and municipal open data portals. Its plugin architecture enables integration with DCAT-AP, DCAT-AP.de, and OGD Switzerland metadata standards, and harvesting from upstream catalogues. Municipalities publishing open data via CKAN can contribute directly to national catalogues (opendata.swiss for Switzerland, GovData.de for Germany) through automated harvesting.

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Licence openness | 5 | AGPL-3.0 |
| Deployment maturity | 5 | 10+ year production track record |
| Community health | 4 | CKAN Association; active |
| Interoperability | 5 | DCAT-AP, DCAT-AP.de, OAI-PMH, SPARQL |
| Security posture | 4 | Actively maintained |
| TCO | 4 | No licence cost; ops overhead |
| Public-sector deployments | 5 | Switzerland, Germany, EU, global |

**Data Governance Act [52] note:** Municipalities publishing open data via CKAN can register as data altruism organisations under the Data Governance Act, enabling participation in European common data spaces. DCAT-AP metadata already satisfies the DGA's machine-readable catalogue requirements.

### 4.7 Geographic Information Systems

**Function:** Map-based citizen services; urban planning; spatial data publication; OGC-compliant data services.

**Recommended components:**
- **QGIS** (desktop/server) for spatial data editing and analysis [37]
- **GeoServer** (GeoTools) for OGC-compliant spatial data publication (WMS, WFS, WCS)
- **OpenStreetMap** as the base cartographic layer [36]

Switzerland's swisstopo (Bundesamt für Landestopografie) provides open, high-quality governmental base map data available under OGD licence. Germany's BKG (Bundesamt für Kartographie und Geodäsie) provides equivalent coverage. Both are compatible with the QGIS/GeoServer stack and reduce the need for expensive proprietary cartographic licences.

**INSPIRE Directive compliance:** European municipalities must comply with the EU INSPIRE Directive for spatial data publication. GeoServer's native WMS/WFS support satisfies INSPIRE technical requirements, and QGIS's INSPIRE plugin assists with metadata management.

### 4.8 Public Website and Content Management

**Function:** Public-facing website; news and announcements; service directory; accessibility compliance.

**Recommended components:**
- **TYPO3** (German-speaking world): dominant in Swiss and German public administration; the TYPO3 Association provides long-term support and public-sector extensions [19]
- **Drupal**: strong international track record; used by the European Commission

Both systems support accessibility standards (WCAG 2.1 AA / BITV 2.0 for Germany; P028 / WCAG 2.1 for Switzerland), multilingualism, and integration with open data catalogues and citizen participation platforms. TYPO3's extension ecosystem includes dedicated public administration components built and maintained by the German-speaking community.

**Accessibility obligation:** Germany's BITV 2.0 (Barrierefreie-Informationstechnik-Verordnung) and Switzerland's P028 standard both require public sector websites to meet WCAG 2.1 AA. Both TYPO3 and Drupal satisfy these requirements when correctly configured and styled.

### 4.9 Cloud Infrastructure and Hosting

**Function:** Compute, storage, networking, container orchestration; digital sovereignty at the infrastructure layer.

**Recommended component: Sovereign Cloud Stack (SCS)** [3, 11]

SCS is the most strategically important infrastructure choice for European municipalities. It provides a fully open-source cloud stack (OpenStack + Kubernetes + Ceph) that can be self-hosted, operated by a cooperative provider (govdigital eG [23]), or deployed by certified SCS cloud operators (plusserver, OSISM).

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Licence openness | 5 | Apache 2.0 / fully open |
| Deployment maturity | 4 | Production in multiple Länder |
| Community health | 5 | OSBA-backed, growing |
| Interoperability | 5 | Open APIs, OCI-compliant |
| Security posture | 5 | BSI IT-Grundschutz compatible |
| TCO | 4 | No licence; infrastructure cost |
| Public-sector deployments | 4 | German Länder, growing |

**Procurement options for municipalities:**
1. **Self-hosted SCS** (municipalities >500,000 with in-house ops capacity)
2. **SCS-certified commercial hoster** (plusserver, OSISM) — managed, sovereign
3. **govdigital eG shared infrastructure** [23] — cooperative, framework-agreement-compliant
4. **ZenDiS OpenDesk SaaS** [47] — application layer on sovereign infrastructure (Germany only)
5. **Cantonal IT cooperative** (Switzerland) — shared cantonal cloud infrastructure

**For municipalities without in-house cloud operations capacity:** options 3 or 4 (Germany) or 5 (Switzerland) are the recommended starting points. Self-hosting should be deferred to Phase 5 or later.

### 4.10 Reference Architecture

The following diagram shows the relationships between the recommended components:

```
+----------------------------------------------------------------+
|                      CITIZEN TOUCHPOINTS                       |
|    TYPO3/Drupal . Decidim/CONSUL . CKAN . Nextcloud Portal    |
+----------------------------------------------------------------+
|                        SERVICE LAYER                          |
|     Camunda Workflows . XÖV/eCH Forms . GeoServer . QGIS     |
+----------------------------------------------------------------+
|                     COLLABORATION LAYER                       |
|     Nextcloud/OpenDesk . Matrix/Element . Jitsi . OpenProject |
+----------------------------------------------------------------+
|                       IDENTITY LAYER                          |
|         Keycloak ←→ BundID (DE) / Swiss e-ID (CH)            |
+----------------------------------------------------------------+
|                     DATA & OPEN DATA                          |
|     CKAN . PostgreSQL . DCAT-AP . eCH/XÖV Data Standards     |
+----------------------------------------------------------------+
|                   INFRASTRUCTURE LAYER                        |
|  Sovereign Cloud Stack . Kubernetes . PostgreSQL . Ceph . OSM |
+----------------------------------------------------------------+

Horizontal: GovStack building blocks as architecture reference [48]
Security: BSI IT-Grundschutz (DE) [26] / Swiss ISDS framework (CH)
Interoperability: XÖV [46] (DE) | eCH [49] (CH) | EU EIF [45] | DCAT-AP
```

All layers communicate via open APIs. Container orchestration across the stack is handled by Kubernetes [39], and relational persistence by PostgreSQL [41], both running on the Sovereign Cloud Stack. Data exchange uses XÖV standards in Germany [46] and eCH standards in Switzerland [49]. Security is governed by BSI IT-Grundschutz (Germany) [26] and the Swiss ISDS framework, both aligned with NIS2 obligations [27].

### 4.11 Cross-border Interoperability Standards

Cross-border and cross-agency interoperability is not automatic even within a municipality. This section summarises the key standards that must be implemented in any compliant municipal technology stack.

| Standard | Jurisdiction | Function | Layer |
|---|---|---|---|
| XÖV (XPersonenstand, XMeld, XKfz, etc.) [46] | Germany | XML data exchange | Service, data |
| eCH-0007, -0010, -0044, -0058, -0211 [49] | Switzerland | Data exchange, delivery | Service, data |
| DCAT-AP / DCAT-AP.de [22] | EU / Germany | Open data metadata | Open data |
| EU EIF [45] | European Union | Interoperability framework | All layers |
| INSPIRE Directive | EU | Spatial data services | GIS |
| OIDC / SAML2 [21] | International | Identity federation | Identity |
| BPMN 2.0 [33] | International | Workflow modelling | Service |
| Matrix protocol [14] | International | Secure messaging | Communication |
| GovStack building blocks [48] | International | Architecture reference | All layers |
| OCI / Kubernetes APIs [39] | International | Container interoperability | Infrastructure |

Municipalities that implement this full interoperability stack are not merely compliant with current regulations — they are positioned to participate in the emerging European data spaces, contribute to the GovStack community, and collaborate with peer municipalities across national boundaries.

---

## 5. Implementation Roadmap

The implementation is structured as a 36-month, five-phase programme, followed by a small-municipality track variant in Section 5.6.

### Phase 0: Foundation (Months 1–3)

**Objective:** Establish governance, assess current state, build the coalition.

**Deliverables:**
- Digital Transformation Steering Committee established (city leadership + IT + civil society)
- Current-state technology audit completed (software inventory, licence costs, data map)
- Stakeholder engagement plan adopted
- Procurement framework established (see Section 6)
- Memorandum of Understanding with cooperative IT provider (Dataport, AKDB, govdigital eG, ZenDiS, or cantonal IT cooperative)
- Data protection impact assessment initiated

**Success criteria:**
- Political mandate secured (council resolution or executive decision)
- Budget envelope approved (indicative: €200,000–€500,000 for Phase 0–1 depending on city size)
- Project lead with explicit mandate appointed
- Privacy-by-design principle adopted as policy

**Key decision gate:** Confirm political mandate and budget before Phase 1 begins.

### Phase 1: Identity and Infrastructure (Months 4–12)

**Objective:** Stand up the foundational layers that everything else depends on.

**Deliverables:**
- Sovereign Cloud Stack environment operational (own, SCS-certified hoster, or govdigital eG / ZenDiS)
- Keycloak identity provider deployed and federated with national identity system (BundID / Swiss e-ID)
- Nextcloud baseline deployment for internal collaboration (or OpenDesk SaaS for German municipalities)
- Matrix/Element messaging for staff
- BSI IT-Grundschutz / Swiss ISDS baseline documentation complete
- Software Bill of Materials (SBOM) initiated for all open-source components

**Success criteria:**
- 100% of IT staff can authenticate via Keycloak SSO
- File storage migrated from proprietary cloud to Nextcloud/OpenDesk
- Basic encrypted messaging operational
- Security baseline documented and approved by data protection officer

### Phase 2: Services and Workflows (Months 10–18)

**Objective:** Migrate or build the first five citizen-facing services on open infrastructure.

**Deliverables:**
- Five highest-volume administrative services deployed on Camunda/XÖV (Germany) or Camunda/eCH (Switzerland) stack
- TYPO3 or Drupal CMS migration complete
- Open data portal (CKAN) launched with first 20 datasets, including DCAT-AP metadata
- Decidim or CONSUL Democracy instance deployed for the first participatory process
- GIS layer operational (QGIS + GeoServer + swisstopo/BKG base data)

**Success criteria:**
- 80% of target service volume processed through new system
- Zero regression in service availability vs. baseline
- First open data publication live and harvested by national catalogue (opendata.swiss / GovData.de)
- First citizen participation process completed on open platform

### Phase 3: Integration and Extension (Months 16–24)

**Objective:** Integrate all layers; extend service coverage to 80% of transactions.

**Deliverables:**
- All services federated via Keycloak SSO
- Nextcloud integrated with document management workflows and records classification
- 80% of administrative services digitised
- Inter-agency data exchange via XÖV/eCH operational
- Smart city IoT data management aligned with EU Data Act requirements [51]
- Data Governance Act registration (if appropriate) [52]

**Success criteria:**
- End-to-end service delivery without paper for 80% of transaction types
- Data quality metrics established and tracked
- First annual open data report published
- Data Act compliance gap analysis completed

### Phase 4: Optimisation and Community (Months 22–30)

**Objective:** Optimise user experience; contribute back to open-source communities; publish results.

**Deliverables:**
- User satisfaction survey (target: NPS > 40)
- First contribution to openCode.de / upstream projects
- Municipal open-source community of practice established (≥ 3 peer municipalities)
- Performance benchmarks published
- Total cost of ownership report (initial) published
- Accessibility audit completed (WCAG 2.1 AA / BITV 2.0)

**Success criteria:**
- At least three improvements contributed upstream to openCode.de or component projects
- Community of practice active with ≥ 3 peer municipalities engaged
- TCO report published with methodology for replication

### Phase 5: Sovereignty and Scale (Months 28–36)

**Objective:** Achieve full digital sovereignty; prepare for extension to neighbouring municipalities.

**Deliverables:**
- Full audit of all software components for licence compliance and SBOM completeness
- Sovereign data residency verified (all data on sovereign infrastructure)
- Playbook for replication by neighbouring municipalities
- Strategy paper v1.0 published
- Contribution to GovStack building-block community (if applicable) [48]

**Success criteria:**
- Zero proprietary single-vendor dependencies in critical path
- Data residency 100% on sovereign infrastructure
- At least one peer municipality has adopted the playbook
- Strategy paper v1.0 released publicly under CC-BY-4.0

### 5.6 Small Municipality Implementation Track

For municipalities with populations below 20,000 population (the majority of European municipalities), a simplified track is recommended:

**Guiding principle:** Participate in shared platforms rather than build individual implementations. The cooperative model consistently outperforms solo deployment for small municipalities.

**Track 0 (Months 1–2):** Join govdigital eG cooperative (Germany) or cantonal IT cooperative (Switzerland). This single step provides immediate access to SCS-based cloud infrastructure, framework contracts, and procurement support.

**Track 1 (Months 2–6):** Adopt OpenDesk SaaS from ZenDiS [47] (Germany) or equivalent cantonal offering (Switzerland). This provides Nextcloud + Cryptpad + OpenProject + Jitsi + Element + Collabora in a single managed service, eliminating the need to deploy each component separately.

**Track 2 (Months 4–9):** Adopt EfA services from openCode.de [10] for citizen-facing processes (Germany) or eCH-compliant cantonal services (Switzerland). Catalogue the five highest-volume administrative interactions and check whether EfA equivalents exist before building bespoke solutions.

**Track 3 (Months 6–18):** Deploy Decidim or CONSUL Democracy for the first participatory process; launch a CKAN instance (or contribute data to the cantonal/national portal via a harvested feed); integrate Keycloak with BundID or Swiss e-ID.

**Key difference from full track:** Small municipalities should defer self-hosted SCS and bespoke workflow development until Track 5 (Year 3+), if at all. The cooperative infrastructure pathway achieves digital sovereignty without the operational overhead of self-hosting.

---

## 6. Stakeholder and Procurement Strategy

### 6.1 Stakeholder Map

| Stakeholder | Primary interest | Engagement approach |
|---|---|---|
| Mayor / Executive | Political success, cost, citizen approval | Executive briefing, progress dashboard, TCO report |
| City council | Oversight, democratic legitimacy | Quarterly reports, open council sessions |
| City IT team | Technical feasibility, workload | Co-design, training, community of practice membership |
| Procurement office | Legal compliance, risk | Framework agreements, legal briefings, GWB/BöB guidance |
| Civil servants (end users) | Ease of use, reliability | UX testing, change management, parallel operations period |
| Citizens | Service quality, privacy, participation | Participatory design via Decidim/CONSUL, transparency reports |
| Civil society / NGOs | Transparency, access, participation | Open platform access, published roadmaps |
| Open-source communities | Contribution, reuse | openCode.de participation, upstream contributions |
| ZenDiS / govdigital eG | Partnership, deployment | Framework agreement, service contract |
| Sovereign technology providers | Partnership | Certified partner agreements (SCS operators) |
| Data protection officer | GDPR, NIS2, Data Act compliance | Privacy-by-design review at each phase; Data Act gap analysis |
| Cantonal / Land IT authority | Interoperability, compliance | XÖV/eCH standard adoption; EfA coordination |

### 6.2 Procurement Framework

Open-source procurement requires a different framework from proprietary licence purchasing. Key principles:

**1. Procure services, not licences.** Open-source software is free to use; municipalities pay for implementation, hosting, support, customisation, and training. Procurement documents must be structured around these service components.

**2. Use cooperative procurement structures.** Germany's govdigital eG [23] and Swiss cantonal IT cooperatives provide framework agreements that satisfy public procurement law (GWB/Vergaberecht in Germany; BöB in Switzerland). ZenDiS provides a direct SaaS pathway for OpenDesk [47].

**3. Apply the "Public Money? Public Code!" principle [4].** All custom software developed under contract must be released under an OSI-approved open-source licence and published on openCode.de or an equivalent public repository. This should be a mandatory contract condition, not merely a preference.

**4. Evaluate total cost of ownership.** Procurement scoring must include a 5-year TCO model covering implementation, hosting, training, support, and exit costs. Proprietary alternatives typically understate long-term costs by omitting vendor lock-in risk and licence escalation. Reference the French Gendarmerie (40% TCO reduction) [53] and Toulouse (€1.8M savings) [54] data in procurement justification documents.

**5. Require interoperability standards.** All procured systems must implement: XÖV [46] (Germany), eCH [49] (Switzerland), DCAT-AP [22] (EU open data), and GovStack building-block specifications [48] where applicable. Non-compliance should be a disqualifying criterion, not merely a preference.

**6. Prefer certified cooperative providers.** For infrastructure, prefer SCS-certified cloud operators or members of govdigital eG [23], who are bound by collective data sovereignty agreements.

**7. EU Data Act and Data Governance Act compliance.** Procurement of smart city infrastructure must include explicit Data Act compliance requirements [51]. DCAT-AP-compliant open data infrastructure should reference DGA data altruism registration [52] as a desirable future capability.

### 6.3 Change Management

Open-source transitions frequently fail not on technical grounds but on human factors: end-user resistance, insufficient training, middle-management inertia, and political backsliding under vendor lobbying. Fraunhofer IESE's 2024 research [58] and the Bolzano-Bozen municipal experience confirm: personnel resistance to change is the most important factor, not technical issues.

**Recommendations:**
- Appoint a **Digital Transformation Champion** at senior political level with explicit mandate and cross-election-cycle continuity plan
- Establish **open-source champions** in each department with advanced training and peer support role
- Run **parallel operations** for a minimum of three months before cutting over critical systems
- Document and celebrate **early wins** (cost savings, new capabilities, citizen feedback on Decidim/CONSUL)
- Publish a **public transparency dashboard** showing migration progress, costs, and service quality metrics
- Ensure **training budget** is at least 15% of total project budget — underinvestment in training is the most common cause of user adoption failure

---

## 7. Risk Analysis

### 7.1 Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Political reversal after election | Medium | High | Embed in legislation/ordinance; build cross-party consensus; create institutional inertia (govdigital eG membership, ZenDiS SaaS contract) |
| Vendor lobbying / FUD campaigns | High | Medium | Document TCO evidence (Gendarmerie, Toulouse); engage civil society; publicise mandate; publish FSFE endorsement |
| Skill gap in IT team | High | Medium | Training programme (15%+ of budget); cooperative IT provider; community of practice; Fraunhofer IESE resources [58] |
| Integration failure between layers | Medium | High | Phased rollout with decision gates; reference architecture adherence; XÖV/eCH compliance testing |
| Data loss during migration | Low | Critical | Full backup protocol; parallel operation; staged migration; SBOM tracking |
| GDPR / data protection violation | Low | High | Privacy-by-design; DPO engagement at each phase; data mapping; eCH-0044/XÖV person identifier compliance |
| EU Data Act non-compliance (smart city) | Medium | Medium | Audit smart city IoT deployments; require open protocols in procurement; Data Act gap analysis in Phase 3 |
| User adoption failure | Medium | High | Change management (Section 6.3); UX testing; training; parallel systems; champion network |
| Security incident | Low | Critical | BSI IT-Grundschutz; NIS2 compliance [27]; penetration testing at each phase gate; incident response plan; SBOM maintenance |
| Community fragmentation | Low | Medium | Contribute upstream; align with openCode.de; join govdigital eG; participate in GovStack community |
| Cost overrun | Medium | Medium | Phase-gated budget; independent project office; open TCO accounting; cooperative procurement spreads risk |
| BundID / Swiss e-ID adoption lag | Medium | Low | Design fallback auth flows; monitor adoption statistics [62]; e-ID timeline (summer 2026) is now firm |
| ZenDiS service availability | Low | Medium | For critical systems, maintain option to self-host; OpenDesk is open-source so exit is always possible |

### 7.2 The Munich Cautionary Case

The City of Munich's LiMux project (2003–2017) is the most-cited case of a large-scale municipal open-source transition that was subsequently reversed. Post-mortem analysis identifies three primary causes of reversal: (a) a change in political leadership in 2014 with closer ties to the proprietary vendor; (b) inadequate change management and end-user training; (c) compatibility issues with state-level systems that had not been updated to support open standards [30]. The technical implementation itself was broadly successful.

The Munich case confirms that political risk management — building cross-party support, embedding digital sovereignty as a legislative value rather than merely a procurement preference, and creating institutional dependencies (cooperative memberships, shared infrastructure) that outlast individual political cycles — is as important as technical planning.

The CONSUL Democracy Foundation's 2019 establishment offers a positive counterpoint: when political support for Decide Madrid declined after elections, the Foundation ensured the platform's continued maintenance through a community governance structure. Municipalities should similarly plan for governance structures that survive political change.

### 7.3 Security Considerations

The BSI's IT-Grundschutz framework provides a comprehensive security baseline applicable regardless of licence model [26]. Key requirements for the open-source municipal stack:

- All server components must receive regular security updates with a documented patch management process
- Authentication must meet BSI Authenticator Assurance Level 2 (AAL2) for citizen-facing services (FIDO2/passkeys are the recommended implementation via Keycloak)
- Data in transit encrypted (TLS 1.3 minimum); data at rest encrypted for sensitive categories (using open encryption libraries, not proprietary implementations)
- Penetration testing at each phase gate, with findings published in the transparency dashboard
- Software Bill of Materials (SBOM) maintained for all open-source dependencies, updated quarterly
- Incident response plan aligned with NIS2 obligations [27]
- Annual security training for all staff with access to citizen data

**NIS2 compliance note:** The NIS2 Directive [27] requires municipalities classified as "essential entities" to implement comprehensive cybersecurity measures and incident reporting. An open-source stack, with its auditable code and community-maintained security patches, provides better security posture in this framework than closed-source alternatives where vulnerabilities may not be publicly disclosed.

---

## 8. Conclusion

The evidence reviewed in this paper converges on five findings:

**1. Open-source municipal technology stacks are technically mature and production-proven.** Every functional requirement of a modern municipal government can be met by open-source software with documented deployments at peer municipalities, from Keycloak for identity to CKAN for open data, and from Decidim for participation to the Sovereign Cloud Stack for infrastructure.

**2. The regulatory environment increasingly mandates open-source and interoperability.** EMBAG (Switzerland), OZG 2.0 (Germany), the Interoperable Europe Act (EU), the EU Data Act (applies September 2025), and NIS2 create a dense regulatory fabric that makes proprietary, vendor-locked systems not merely suboptimal but progressively harder to keep compliant. Municipalities that begin the transition now are building compliance capital; those that delay are accumulating regulatory debt within a shortening window.

**3. The economic case is compelling when total costs are counted correctly.** The French Gendarmerie's 40% TCO reduction across 103,164 workstations, the City of Toulouse's €1.8 million in three-year savings, and the consistent pattern of 30–40% cost reductions across European government open-source migrations provide robust benchmarks. Cooperative procurement models — govdigital eG, cantonal IT cooperatives, the EfA approach — spread implementation costs across many municipalities, making the economics accessible even to small Gemeinden.

**4. Success requires as much political and organisational investment as technical investment.** Fraunhofer IESE's 2024 research, the Munich LiMux post-mortems, and the Bolzano-Bozen municipal experience converge on the same finding: personnel resistance to change, not technical failure, is the primary risk. Clear political mandate, skilled change management, and sustained stakeholder engagement are the binding constraints. The implementation roadmap reflects this: change management, training, and cooperative IT provider relationships receive as much attention as technical architecture.

**5. The institutional ecosystem is now mature enough to support municipal implementation at scale.** ZenDiS's OpenDesk (launched end of 2024), govdigital eG's SCS-based cooperative cloud, openCode.de's 300+ repositories, and the GovStack building-block framework together provide German municipalities with a complete, sovereign digital infrastructure pathway they do not need to assemble alone. Swiss municipalities have the analogous support from the e-ID Act (summer 2026 rollout), eCH standards, opendata.swiss, and cantonal IT cooperatives.

Cities that move first will benefit from first-mover advantages: shaping cooperative standards, building in-house expertise, contributing to the open-source commons that all municipalities share, and acquiring compliance capital that later movers will pay more to obtain. The invitation is open.

---

## References

[1] Swiss Federal Council. (2023). *Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG)*. SR 172.019. Bern: Swiss Confederation. https://www.fedlex.admin.ch/eli/cc/2023/682/de — [Open access, CC0]

[2] Bundesministerium des Innern und für Heimat (BMI). (2024). *Onlinezugangsgesetz 2.0 (OZG 2.0)*. Berlin: BMI. https://www.bmi.bund.de/DE/themen/moderne-verwaltung/e-government/ozg/ozg-node.html — [Open access, DL-DE/Zero 2.0]

[3] Open Source Business Alliance (OSBA). (2023). *Sovereign Cloud Stack: Technical and Governance Overview*. Berlin: OSBA. https://scs.community/ — [Open access, CC-BY-SA-4.0]

[4] Free Software Foundation Europe (FSFE). (2017). *Public Money? Public Code!* Berlin: FSFE. https://publiccode.eu/ — [Open access, CC-BY-SA-4.0]

[5] European Commission. (2020). *Open Source Software Strategy 2020–2023: Think Open*. Brussels: European Commission. https://commission.europa.eu/about/departments-and-executive-agencies/informatics/open-source-software-strategy_en — [Open access]

[6] European Parliament and Council. (2024). *Regulation (EU) 2024/903 — Interoperable Europe Act*. Brussels: Official Journal of the EU. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202400903 — [Open access, EU legislation]

[7] Wirtz, B. W., & Weyerer, J. C. (2017). Conceptualization and creation of a holistic e-government maturity model. *Public Management Review*, 19(9), 1297–1316. https://doi.org/10.1080/14719037.2017.1283024

[8] Janssen, M., Charalabidis, Y., & Zuiderwijk, A. (2012). Benefits, adoption barriers and myths of open data and open government. *Information Systems Management*, 29(4), 258–268. https://doi.org/10.1080/10580530.2012.716740

[9] FITKO. (2023). *Föderale IT-Kooperation — Jahresbericht 2023*. Frankfurt: FITKO. https://www.fitko.de/ — [Open access]

[10] openCode.de. (2022). *openCode — Open Source for Government*. Berlin: Digitalservice GmbH des Bundes. https://opencode.de/ — [Open access]

[11] Sovereign Cloud Stack Community. (2023). *SCS Technical Documentation*. https://docs.scs.community/ — [Open access, Apache 2.0]

[12] Decidim Association. (2021). *Decidim: Free Open-Source Participatory Democracy for Cities and Organizations*. Barcelona: Decidim Association. https://decidim.org/ — [Open access, AGPL-3.0]

[13] Nextcloud GmbH. (2023). *Nextcloud for Government: Security, Sovereignty, and Collaboration*. Stuttgart: Nextcloud GmbH. https://nextcloud.com/government/ — [Open access]

[14] The Matrix Foundation. (2023). *Matrix Specification v1.x*. https://spec.matrix.org/ — [Open access, Apache 2.0]

[16] E-Government Suisse. (2023). *Strategie E-Government Schweiz 2024–2027*. Bern: Schweizerische Bundeskanzlei. https://www.egovernment.ch/de/umsetzung/e-government-strategie/ — [Open access]

[19] TYPO3 Association. (2023). *TYPO3 in Public Administration*. Düsseldorf: TYPO3 Association. https://typo3.org/project/association — [Open access]

[20] OpenProject GmbH. (2023). *OpenProject for Government: Open Source Project Management*. Berlin: OpenProject GmbH. https://www.openproject.org/ — [Open access, GPLv3]

[21] Red Hat / Keycloak Community. (2023). *Keycloak: Open Source Identity and Access Management*. https://www.keycloak.org/ — [Open access, Apache 2.0]

[22] CKAN Association. (2023). *CKAN: Open Source Data Portal Software*. https://ckan.org/ — [Open access, AGPL-3.0]

[23] govdigital eG. (2023). *govdigital: Genossenschaft für digitale Verwaltung*. Berlin: govdigital eG. https://govdigital.de/ — [Open access]

[24] Dataport AöR. (2023). *Dataport: IT-Dienstleister für die öffentliche Verwaltung*. Hamburg: Dataport AöR. https://www.dataport.de/ — [Open access]

[26] Bundesamt für Sicherheit in der Informationstechnik (BSI). (2023). *BSI IT-Grundschutz-Kompendium Edition 2023*. Bonn: BSI. https://www.bsi.bund.de/ — [Open access, CC-BY-ND 3.0 DE]

[27] European Parliament and Council. (2022). *Directive (EU) 2022/2555 — NIS2 Directive*. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022L2555 — [Open access]

[29] United Nations DESA. (2022). *UN E-Government Survey 2022: The Future of Digital Government*. New York: United Nations. https://publicadministration.un.org/egovkb/en-us/Reports/UN-E-Government-Survey-2022 — [Open access]

[30] Janowski, T. (2015). Digital government evolution: From transformation to contextualization. *Government Information Quarterly*, 32(3), 221–226. https://doi.org/10.1016/j.giq.2015.07.001

[33] Camunda Services GmbH. (2023). *Camunda Platform 8 Community Edition*. https://camunda.com/download/ — [Open access, Apache 2.0]

[34] BigBlueButton Inc. (2023). *BigBlueButton: Open Source Web Conferencing*. https://bigbluebutton.org/ — [Open access, LGPL-3.0]

[35] Jitsi Community. (2023). *Jitsi Meet: Open Source Video Conferencing*. https://jitsi.org/ — [Open access, Apache 2.0]

[36] OpenStreetMap Foundation. (2023). *OpenStreetMap*. https://www.openstreetmap.org/ — [Open access, ODbL-1.0]

[37] QGIS Project. (2023). *QGIS: A Free and Open Source Geographic Information System*. https://www.qgis.org/ — [Open access, GPL-2.0+]

[39] Cloud Native Computing Foundation (CNCF). (2023). *Kubernetes*. https://kubernetes.io/ — [Open access, Apache 2.0]

[41] PostgreSQL Global Development Group. (2023). *PostgreSQL*. https://www.postgresql.org/ — [Open access, PostgreSQL Licence]

[42] ZenDiS GmbH / BMI. (2024). *OpenDesk: Der digitale Arbeitsplatz der Bundesverwaltung*. Berlin: ZenDiS GmbH. https://opendesk.eu/ — [Open access, AGPL-3.0]

[43] Schweizerisches Bundesarchiv (BAR). (2023). *Geschäftsverwaltung (GEVER) in der Bundesverwaltung*. Bern: BAR. https://www.bar.admin.ch/ — [Open access]

[44] opendata.swiss. (2023). *Open Government Data Switzerland*. Bern: Schweizerische Bundeskanzlei. https://opendata.swiss/ — [Open access, CC-BY-4.0]

[45] European Commission. (2017). *European Interoperability Framework — Implementation Strategy (EIF)*. Brussels: European Commission. https://joinup.ec.europa.eu/collection/nifo-national-interoperability-framework-observatory — [Open access, CC-BY-4.0]

[46] KoSIT. (2023). *XÖV-Standards: XML in der öffentlichen Verwaltung*. Bremen: KoSIT. https://www.xoev.de/ — [Open access]

[47] ZenDiS GmbH. (2024). *ZenDiS: Co-creating Digital Sovereignty*. Berlin: Zentrum Digitale Souveränität der Öffentlichen Verwaltung GmbH. https://www.zendis.de/ — [Open access]

[48] GovStack Initiative / ITU. (2024). *GovStack: Digital Building Blocks for E-Government*. Geneva: International Telecommunication Union / Digital Impact Alliance. https://www.govstack.global/ — [Open access, CC-BY-4.0]

[49] eCH Association. (2024). *eCH E-Government Standards*. Zurich: eCH. https://www.ech.ch/ — [Open access; see also Swiss Federal Chancellery: https://www.bk.admin.ch/bk/de/home/digitale-transformation-ikt-lenkung/vorgaben/ech-standards.html]

[50] CONSUL Democracy Foundation. (2024). *CONSUL Democracy: Open Government and E-Participation Web Software*. Madrid: CONSUL Democracy Foundation. https://consuldemocracy.org/ — [Open access, AGPL-3.0]

[51] European Parliament and Council. (2023). *Regulation (EU) 2023/2854 on harmonised rules on fair access to and use of data (Data Act)*. In force: 2024-01-11; Applies: 2025-09-12. Brussels: Official Journal of the EU. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023R2854 — [Open access, EU legislation]

[52] European Parliament and Council. (2022). *Regulation (EU) 2022/868 on European data governance (Data Governance Act)*. Applied from September 2023. Brussels: Official Journal of the EU. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R0868 — [Open access, EU legislation]

[53] French National Gendarmerie. (2024). *GendBuntu: Open Source Desktop Migration Case Study*. France: Gendarmerie Nationale. Cited via secondary source: https://yeandel.co.uk/21-migration-case-studies/france-gendarmerie.html — [Open access]

[54] Ville de Toulouse. (2023). *Migration open source — Bilan de la ville de Toulouse*. Toulouse: Direction des Systèmes d'Information. — [Grey literature; cited via secondary reporting; €1.8M savings over 3 years, 90% desktop migration]

[55] Open Source Observatory (OSOR) / Interoperable Europe. (2023). *Case Study: CONSUL Democracy*. Brussels: Interoperable Europe Portal. https://interoperable-europe.ec.europa.eu/collection/open-source-observatory-osor/document/case-study-consul-democracy — [Open access, CC-BY-4.0]

[56] Swiss Federal Council. (2024). *Bundesgesetz über den elektronischen Ausweis und andere elektronische Nachweise (BGEID)*. Bern: Swiss Federal Chancellery. https://www.eid.admin.ch/ — [Open access] — Parliament: 2024-12-20; Referendum: 2025-09-28 (50.39% yes); Rollout: summer 2026

[57] City of Espoo. (2023). *eVaka: Open Source Early Education Management*. Espoo: City of Espoo Digital Services. https://github.com/espoon-voltti/evaka — [Open access, LGPL-2.1]

[58] Fraunhofer IESE. (2024). *The Key to Digital Sovereignty: How Municipalities Can Establish Open Source Software*. Kaiserslautern: Fraunhofer Institut für Experimentelles Software Engineering. https://www.iese.fraunhofer.de/en/media/press/pm-2024-01-24-open-source-software.html — [Open access]

[59] European Parliamentary Research Service. (2023). *Digital Sovereignty — Panel for the Future of Science and Technology (STOA)*. Brussels: European Parliament. https://www.europarl.europa.eu/RegData/etudes/STUD/2023/737128/EPRS_STU(2023)737128_EN.pdf — [Open access]

[60] Lathrop, D., & Ruma, L. (Eds.). (2010). *Open Government: Collaboration, Transparency, and Participation in Practice*. Sebastopol: O'Reilly Media. Open-access edition: https://github.com/oreillymedia/open_government — [CC-BY]

[61] Swiss Federal Council. (2025). *Strategie Digitale Schweiz 2025*. Bern: Swiss Federal Chancellery. https://www.bk.admin.ch/bk/en/home/digitale-transformation-ikt-lenkung/strategie-digitale-schweiz.html — [Open access]

[62] KOMMUNAL / FITKO. (2025). *Behörden-Digimeter 2025: Aktueller Stand der OZG-Umsetzung in Deutschland*. Frankfurt: FITKO / KOMMUNAL. https://kommunal.de/behoerden-digimeter-2025-so-weit-ist-das-ozg — [Open access]

---

*This document is released under the Creative Commons Attribution 4.0 International Licence (CC-BY-4.0).*
*Attribute as: Sebastian Graf, Autonomous Office of Civil Digital Infrastructure (sebk4c@tuta.com)*
*Version 0.2.0 — Citation-Complete Draft — 2026-06-21*
*Source of truth: English. German translation: Doc/de/sovereign-by-design-v0.2.0.de.md*
