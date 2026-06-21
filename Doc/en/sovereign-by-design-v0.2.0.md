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
---

# Sovereign by Design: A State-of-the-Art Open-Source Technology Strategy for Municipal Governments

## Abstract

Municipal governments across Europe face a structural dependency on proprietary software whose licensing model, data-governance terms, and exit costs are fundamentally incompatible with the public-sector imperatives of digital sovereignty, transparency, and long-term fiscal sustainability. This paper presents a state-of-the-art, evidence-based technology strategy for migrating municipal IT estates to a coherent open-source stack, with concrete and parallel implementation tracks for German and Swiss municipalities. The strategy is grounded in a structured review of the European policy framework — including the EU Open Data Directive, Germany's Onlinezugangsgesetz (OZG), and Switzerland's pioneering "open-by-default" EMBAG mandate — and in an analysis of mature, production-grade open-source components.

The economic case is direct. Proprietary per-seat productivity and collaboration licences typically cost municipalities between €100 and €300 per user per year; open-source equivalents eliminate this recurring per-seat licence cost entirely, converting it into market-competitive, contestable service expenditure. A total cost of ownership (TCO) analysis spanning implementation, recurring licences, hosting, support, training, exit, and vendor lock-in risk premium consistently shows a 30–50% reduction over a five-year horizon when all cost categories are accounted for, corroborated by the French DGFiP LibreOffice migration and the City of Barcelona's Decidim deployment.

We evaluate nine functional layers of the municipal software estate — identity and access management, citizen participation and service delivery, document and collaboration, secure communication, open data, geospatial, workflow and case management, cloud infrastructure, and security and monitoring — against a transparent seven-criterion scoring matrix (licence openness, deployment maturity, community health, interoperability-standards compliance, security posture, total cost of ownership, and verified public-sector deployments). All nine functional requirements are met by mature open-source solutions that score competitively or superiorly across the matrix.

The paper translates this analysis into a phased 36-month implementation roadmap (Phases 0–5), with jurisdiction-specific tracks addressing OZG 2.0, BundID, XÖV, and BSI IT-Grundschutz in Germany, and EMBAG, eCH standards, opendata.swiss, and the forthcoming Swiyu eID in Switzerland. Stakeholder, procurement, and risk strategies — including EU procurement-law compliance, cooperative framework agreements, vendor-lobbying and FUD mitigation, and open-source supply-chain security — complete the operational guidance. We conclude that sovereign-by-design municipal IT is not only technically achievable today but economically advantageous, and that the principal barriers are organisational and political rather than technological.

**Keywords:** digital sovereignty; open source; GovTech; municipal transformation; interoperability; OZG; EMBAG; eCH; GovStack; ZenDiS.

---

## 1. Introduction

The digital infrastructure of municipal government is, in most European jurisdictions, built upon proprietary software supplied by a small number of large vendors. This concentration produces three structural risks for the public sector: fiscal exposure to unilateral licence-price changes; technical lock-in that raises the cost of change and entrenches incumbents; and a loss of sovereign control over the data and processes through which the state interacts with its citizens [2, 4]. The concept of *digital sovereignty* — a state's capacity to exercise autonomous control over its digital infrastructure, data, and the rules governing them — has accordingly moved from an academic concern to an explicit policy objective at EU, federal, and cantonal levels [2, 50].

Open-source software offers a credible and increasingly mandated answer. Where the source code is publicly available under an OSI-approved licence, the public sector gains the legal right to study, modify, run, and redistribute the software without per-seat licence fees and without dependence on a single vendor [4]. The principle has been crystallised politically in the Free Software Foundation Europe's "Public Money? Public Code!" campaign, which argues that software financed by public money should be released under a free and open-source licence [4], and legally in Switzerland's EMBAG, which mandates open-by-default publication of publicly developed software [1].

This paper synthesises the policy framework, the technology landscape, and the operational practice into a single, actionable strategy for municipal governments. It is written for the municipal Chief Information Officer (CIO), the procurement lead, and the political sponsor, and it is designed to be implementable by municipalities of widely differing sizes and capacities.

### 1.1 Scope

This paper addresses the IT estate of a typical European municipal government: citizen-facing digital services, internal productivity and collaboration tooling, identity management, open-data publication, geospatial services, workflow automation, and the underlying cloud and security infrastructure. It covers municipalities ranging from small (5,000–25,000 population) through medium (25,000–150,000) to large (150,000–500,000), and provides parallel, fully specified implementation tracks for the German and Swiss legal jurisdictions, which between them illustrate the two dominant regulatory models in German-speaking Europe.

The paper does not address specialist line-of-business systems (e.g. financial accounting or specialised registry software) in detail, except where interoperability standards bear on them. It assumes that the municipality retains, or can procure, baseline operational IT capacity.

### 1.2 Research Questions

This work is structured around four research questions:

- **RQ1.** Does a coherent, mature open-source stack exist that satisfies all nine functional requirements of a modern municipal IT estate?
- **RQ2.** What is the total cost of ownership of an open-source municipal stack relative to the proprietary status quo over a five-year horizon, and what evidence supports the estimate?
- **RQ3.** What is a realistic, risk-managed implementation roadmap for migrating a municipality of a given size to such a stack, and how does it differ between the German and Swiss jurisdictions?
- **RQ4.** What stakeholder, procurement, and risk-management strategies are required to make the transition durable against organisational resistance and vendor lobbying?

---

## 2. Methodology

This paper follows a structured, qualitative, multi-method approach combining a systematic literature review, a criteria-based technology evaluation, and comparative jurisdictional analysis.

The **literature review** (Section 3) draws on three classes of source: (a) peer-reviewed and grey-literature scholarship on digital sovereignty and e-government; (b) primary legal and policy instruments at EU, German federal, and Swiss federal levels; and (c) institutional reports and documentation from the relevant public-sector stewardship bodies (ZenDiS, OSOR, GovStack, eCH). Sources were identified through targeted search of academic databases, the EU Joinup/OSOR repository [51], and official government publication portals, and were selected for relevance, authority, and recency, with priority given to open-access and primary sources.

The **technology evaluation** (Section 4, Appendix A) applies a transparent seven-criterion scoring matrix to candidate open-source components for each of the nine functional layers. Criteria — licence openness, deployment maturity, community health, interoperability-standards compliance, security posture, total cost of ownership, and verified public-sector deployments — are each scored on a 0–5 ordinal scale and combined with equal weighting into a composite score. Candidate selection prioritised components with documented production use in European public administration.

The **TCO analysis** (Section 3.9, Appendix B) decomposes lifetime cost into seven categories and parameterises them for three municipality size bands, drawing on documented migration case studies where available. The methodology is explicitly presented as a framework to be validated against local procurement conditions rather than as a definitive figure, given the scarcity of independent comparative studies.

The **comparative jurisdictional analysis** (Sections 5.6, 5.7, 6.4) maps the generic roadmap onto the specific legal obligations of the German and Swiss jurisdictions. Limitations of the methodology are stated explicitly in Section 3.11.

---

## 3. Literature Review

### 3.1 Digital Sovereignty as a Policy Concept

Digital sovereignty denotes the capacity of a polity to determine, autonomously and accountably, the rules and infrastructure of its digital domain [2]. In the European public-sector discourse it has three intertwined dimensions: *technological* sovereignty (control over the software and hardware stack), *data* sovereignty (control over where and under what law data resides and is processed), and *operational* sovereignty (the ability to run, change, and exit systems without third-party permission) [2, 5]. The concept gained policy salience following the recognition that reliance on a handful of non-European hyperscale vendors exposed administrations to extraterritorial legal regimes and to unilateral commercial decisions [5]. Open-source software is widely identified as a necessary, though not sufficient, instrument of digital sovereignty, because it removes the legal and technical barriers to operational and exit control [4, 50].

### 3.2 Open-Source Software in Public Administration: Historical Overview

Public-sector adoption of open-source software has a two-decade history of high-profile successes and instructive reversals. Early municipal pioneers, most famously the City of Munich's LiMux programme, demonstrated both the feasibility of large-scale desktop migration and the political fragility of such transitions in the face of organisational inertia and vendor influence [55]. The literature distinguishes between transitions that were embedded in durable governance structures and political coalitions, which tended to persist, and those that depended on a single sponsor, which tended to be reversed [55]. The contemporary period is marked by a shift from individual heroic migrations toward shared, institutionally stewarded open-source infrastructure — the model embodied by ZenDiS in Germany [50] and codified in law by Switzerland's EMBAG [1].

### 3.3 The EU Policy Framework: PSI Directive, INSPIRE, and Open Data

The European Union has constructed a layered framework that increasingly favours openness and interoperability. The Open Data Directive (Directive (EU) 2019/1024), successor to the Public Sector Information (PSI) Directive, mandates that public-sector data be made available for reuse in machine-readable formats and via open APIs, and designates certain "high-value datasets" for mandatory open publication [44]. The INSPIRE Directive (2007/2/EC) establishes a pan-European spatial data infrastructure built on open geospatial standards, directly relevant to municipal GIS [42]. The European Interoperability Framework (EIF) provides the conceptual model — legal, organisational, semantic, and technical interoperability — within which national frameworks such as XÖV and eCH operate [43]. Together these instruments make open standards and open data a legal baseline rather than an aspiration.

### 3.4 Germany's OZG and the EfA Model

Germany's Onlinezugangsgesetz (OZG), enacted in 2017 and substantially revised as OZG 2.0, obliges federal, state, and municipal administrations to offer their services online [9]. The implementation model that emerged is *Einer für Alle* (EfA — "one for all"): a pioneer administration develops a digital service once, and other administrations reuse it rather than each building their own [9]. OZG 2.0 additionally strengthens the open-source dimension, with custom administrative software expected to be published on the public code repository openCode.de [10]. The EfA model is significant for small municipalities because it allows them to consume services developed and financed by larger pioneers, dramatically lowering the capacity barrier to digital service delivery [9].

### 3.5 Switzerland's EMBAG and the Open-by-Default Mandate

Switzerland has taken the most legally explicit position in the German-speaking region. The Federal Act on the Use of Electronic Means for the Fulfilment of Government Tasks (EMBAG), in force from 2024, establishes an "open-by-default" principle: software developed by or for the federal administration must, as a rule, be published as open source, with exceptions only for security or third-party-rights reasons [1]. EMBAG also provides a legal basis for the federal administration to offer digital services and to publish open government data [1]. While EMBAG binds the federal level directly, it sets a powerful normative precedent that cantonal and municipal administrations are increasingly choosing to follow, and it aligns Swiss practice with the FSFE's "Public Money? Public Code!" principle [4, 16].

### 3.6 The GovStack Initiative

GovStack is a joint initiative of the International Telecommunication Union (ITU), the Digital Impact Alliance (DIAL), the German Federal Government (BMZ/GIZ), and the Government of Estonia [49]. It defines a set of reusable digital "building blocks" for government services — including digital registration, consent management, an information mediator (based on the X-Road data-exchange layer), payments, scheduling, messaging, and e-signature — each specified as an interoperable, technology-neutral component [49]. GovStack's architecture is directly compatible with the open-source stack described in this paper: its information mediator maps onto interoperability middleware, its registration and identity blocks onto Keycloak, and its messaging block onto Matrix-based communication. For municipalities with limited IT capacity, GovStack provides a standardised, well-documented starting point and a vocabulary for specifying procurements in terms of composable building blocks rather than monolithic systems [49].

### 3.7 ZenDiS and the Centre for Digital Sovereignty

ZenDiS GmbH — the Zentrum für Digitale Souveränität der öffentlichen Verwaltung — was established by the German Federal Government in 2022 as a specialist agency for open-source stewardship in public administration [50]. Its core work comprises three strands: **OpenDesk**, a government open-source workplace suite integrating productivity, collaboration, and communication components into a coherent, sovereign alternative to proprietary office cloud suites; **openCode.de**, a public code repository that now hosts more than 300 repositories of publicly developed software; and an open-source component library supporting OZG digital services [50]. ZenDiS represents a new institutional model of public-sector open-source stewardship — a permanent, publicly owned body that curates, integrates, and supports a shared open-source estate. Crucially for this paper, ZenDiS is an entity that municipalities can partner with directly, obtaining implementation support for OpenDesk and access to vetted components rather than each negotiating bilaterally with the market [50].

### 3.8 Swiss eCH Standards and Digital Identity Infrastructure

eCH (E-Government Switzerland / E-Government Schweiz) publishes the XML and interoperability standards for Swiss e-government, functionally equivalent to Germany's XÖV framework [47]. Key standards include eCH-0010 (postal address), eCH-0011 (person data), eCH-0044 (electronic identity), eCH-0058 (interface for the communal register / message exchange), and eCH-0185 (open government data metadata) [47]. These standards are mandatory for Swiss cantonal and municipal systems that interoperate with federal services, and any open-source municipal stack must implement them at its data-exchange boundaries [47].

The Swiss electronic identity (eID) has a politically instructive history. The first eID proposal was rejected in the popular referendum of March 2021, primarily because it delegated identity issuance to private companies. The revised approach, enacted as the E-ID Act in 2023 and branded **Swiyu**, follows a state-issued, privacy-preserving architecture based on verifiable credentials, with launch planned for 2026 [16]. Municipal identity and access management systems built on Keycloak must therefore be configured to accept the new Swiss eID when it goes live, in the same way that German systems federate with BundID [16, 47].

### 3.9 Total Cost of Ownership — Evidence and Methodology

The total cost of ownership of open-source versus proprietary municipal software is the single most contested question in the field, and the absence of rigorous independent evidence is a critical gap that this version of the paper begins to address.

Two well-documented cases anchor the analysis. The French **DGFiP** (Direction Générale des Finances Publiques) migrated from Microsoft Office to LibreOffice across approximately 170,000 workstations, with an estimated saving of around €14 million over five years, alongside the strategic benefit of removing per-seat licence dependency [54]. The **City of Barcelona's** Decidim implementation reached TCO-neutrality relative to proprietary e-participation alternatives within roughly 18 months of deployment, after which the licence cost remained at €0 while the proprietary alternative would have continued to accrue per-seat or per-instance fees [12].

A defensible TCO framework decomposes lifetime cost into seven categories:

| Cost category | Open-source | Proprietary | Notes |
|---|---|---|---|
| (a) Implementation | Comparable | Comparable | Integration effort is similar for both models |
| (b) Recurring licence | €0 | €100–300/seat/year | The decisive structural difference |
| (c) Hosting | Comparable | Comparable | Same underlying compute/storage |
| (d) Support | Market-competitive | Vendor-controlled | Open-source support is contestable |
| (e) Training | Often higher (one-time) | Lower (incumbent familiarity) | A genuine migration cost |
| (f) Exit | Near-zero | High | Data and process lock-in |
| (g) Lock-in risk premium | Low | High | Exposure to unilateral price changes |

Over a five-year horizon, when all seven categories are included, the analysis consistently shows a **30–50% TCO reduction** for the open-source model, driven primarily by the elimination of recurring per-seat licence costs (b) and the near-elimination of exit and lock-in costs (f, g), partially offset by higher one-time training costs (e) [54, 12].

The principal caveat is methodological honesty: most publicly available TCO studies are vendor-commissioned and therefore systematically biased toward the commissioning party's product; genuinely independent comparative studies remain scarce. The framework proposed here must therefore be calibrated against local procurement conditions — local labour costs, existing licence terms, and the scope of migration — rather than applied as a universal constant.

### 3.10 Small-Municipality Case Studies

Municipalities under 50,000 population are severely underrepresented in the e-government and open-source literature, despite representing more than 95% of all EU municipalities [51]. This imbalance matters because the capacity constraints of small municipalities — limited or no in-house IT staff, small budgets, and weak procurement leverage — are qualitatively different from those of the large cities that dominate the case-study literature.

Three mechanisms specifically address small-municipality capacity constraints. First, the **cooperative model** — govdigital eG in Germany [23] and the cantonal IT cooperatives in Switzerland — pools demand, expertise, and procurement leverage across many small members, allowing each to consume professionally operated open-source infrastructure it could not build alone. Second, the **EU Open Source Observatory (OSOR)** maintains a case-study database documenting implementations from municipalities as small as 2,000 population, providing concrete, transferable precedents [51]. Third, Germany's **EfA model** explicitly socialises development cost: a small municipality benefits directly from a digital service financed and built by a larger pioneer municipality, consuming it as a shared service [23, 49]. Finally, the **GovStack** building-block architecture is designed for low-capacity deployments, allowing a small municipality to assemble services from documented, interoperable components rather than commissioning bespoke systems [49]. Together these mechanisms make the open-source strategy realistic for the long tail of small municipalities that the headline case studies tend to ignore [23, 51, 49].

### 3.11 Gaps Remaining at v0.2.0

Three evidence gaps persist and are targeted for resolution in version 1.0. First, **independent comparative TCO studies remain scarce**: the field still relies disproportionately on vendor-commissioned figures and a handful of large public migrations. Second, **user-experience research comparing citizen satisfaction** with open-source versus proprietary public services is essentially absent, leaving the quality-of-service dimension under-evidenced. Third, **longitudinal data on completed small-municipality transitions** is thin, so the durability of small-municipality migrations cannot yet be assessed empirically. Addressing these gaps requires primary, independent, multi-year field research.

---

## 4. Technology Stack Analysis

This section evaluates candidate open-source components for each of the nine functional layers, applying the seven-criterion scoring matrix described in Appendix A. The composite scores are summarised in Section 4.11.

### 4.1 Identity and Access Management: Keycloak

Identity and access management (IAM) is the foundation of the municipal stack: it provides single sign-on, federation with national identity systems, and centralised authorisation. **Keycloak** is the de facto open-source standard, implementing OpenID Connect (OIDC), OAuth 2.0, and SAML 2.0, with mature support for identity brokering and user federation [13]. For German municipalities, Keycloak federates with **BundID**, the national citizen identity system, via OIDC; for Swiss municipalities, it must be configured to accept the forthcoming **Swiyu** eID [13, 16]. Keycloak's maturity, strong standards compliance, active community, and extensive public-sector deployment make it the unambiguous choice for this layer.

### 4.2 Citizen Portal and Service Delivery: Decidim and CONSUL

Citizen participation and service delivery is served by two leading platforms. **Decidim**, originating in the City of Barcelona, is a comprehensive participatory-democracy framework supporting proposals, deliberation, participatory budgeting, and consultations, released under the AGPL-3.0 licence and deployed across dozens of European cities [12]. **CONSUL** (CONSUL Democracy), originating in the City of Madrid, provides comparable open-government and civic-participation functionality and has been adopted internationally [48]. For transactional service delivery, these platforms integrate with workflow engines (Section 4.7) and IAM (Section 4.1) to provide authenticated, auditable citizen interactions. Decidim's governance maturity and breadth give it a slight edge for municipalities prioritising deliberative participation.

### 4.3 Document and Collaboration Suite: Nextcloud and Collabora Online

The productivity and collaboration layer replaces proprietary office-cloud suites. **Nextcloud** provides file sync-and-share, groupware, and an application platform, and is the collaboration core of the ZenDiS OpenDesk suite [14, 50]. Integrated with **Collabora Online** (an enterprise-supported LibreOffice Online), it delivers in-browser collaborative editing of documents, spreadsheets, and presentations in open formats [15]. This pairing eliminates the €100–300/seat/year proprietary office-cloud licence while preserving the core collaborative workflows that staff depend upon, and it stores data on infrastructure the municipality controls [14, 15, 50].

### 4.4 Communication and Messaging: Matrix/Element

Secure, sovereign communication is provided by the **Matrix** protocol and its reference client **Element** [17]. Matrix is a decentralised, end-to-end-encrypted, federated messaging standard adopted by several national governments and armed forces for sovereign communication, precisely because federation allows each organisation to operate its own homeserver while still interoperating [17]. For municipalities this means internal and inter-agency messaging that is encrypted, self-hosted, and free of per-seat licence cost, and that maps directly onto the GovStack messaging building block [17, 49].

### 4.5 Open Data Infrastructure: CKAN

Open-data publication is dominated by **CKAN**, the open-source data-management platform that powers numerous national and municipal open-data portals [22]. CKAN supports dataset cataloguing, harvesting, APIs, and metadata standards, and natively satisfies the open-API and machine-readable-format obligations of the EU Open Data Directive [22, 44]. It implements the DCAT-AP metadata profile required for interoperability with national and EU data catalogues, and integrates with the Swiss opendata.swiss and German GovData ecosystems [22, 44, 47]. CKAN's role is extended substantially by the EU Data Act, discussed in Section 4.10.

### 4.6 Geographic Information Systems: GeoServer, QGIS, and MapLibre

Municipal geospatial services rest on a mature, fully open stack. **GeoServer** serves spatial data via the Open Geospatial Consortium (OGC) standards (WMS, WFS, WMTS) required by the INSPIRE Directive [42, 41]. **QGIS** provides professional desktop GIS for analysis and cartography, and **MapLibre** delivers performant, vendor-neutral web map rendering for citizen-facing applications [41]. This combination meets all common municipal geospatial requirements — cadastre, planning, utilities, environmental monitoring — with full INSPIRE and OGC compliance and no licence cost [42, 41].

### 4.7 Workflow and Case Management: Camunda and Formio

Administrative process automation is the layer where open-source maturity is sometimes questioned, but two components answer the requirement. **Camunda** is a BPMN 2.0-compliant workflow and decision engine widely used to orchestrate administrative processes, providing auditable, standards-based process automation [18]. **Form.io** (and comparable open form-builders) provides dynamic, schema-driven citizen forms that can be bound to XÖV or eCH data models and routed into Camunda processes [18, 46, 47]. Together they convert paper or proprietary-workflow processes into transparent, modifiable, standards-based digital services.

### 4.8 Cloud Infrastructure: Sovereign Cloud Stack and Kubernetes

The infrastructure layer must itself be sovereign. The **Sovereign Cloud Stack (SCS)** is a community-developed, standardised, fully open-source cloud stack combining OpenStack (IaaS) and Kubernetes (container orchestration) into a certified, federatable reference implementation explicitly designed for European digital sovereignty [3, 11]. SCS provides a curated, tested, security-patched component set, which materially reduces the operational and security burden on municipal teams [3, 11]. Municipalities can deploy SCS on their own hardware, procure it from a sovereign cloud provider, or consume it via a cooperative such as govdigital eG [3, 11, 23]. **Kubernetes** underpins the container orchestration layer across all deployment models.

### 4.9 Security and Monitoring: OpenZiti, Wazuh, and Grafana Stack

The security and observability layer combines several mature projects. **OpenZiti** provides zero-trust network access, replacing perimeter VPNs with identity-based, least-privilege connectivity [40]. **Wazuh** delivers open-source SIEM and XDR capabilities — intrusion detection, log analysis, and compliance monitoring — supporting the evidence requirements of BSI IT-Grundschutz and the Swiss ISDS framework [40, 26]. The **Grafana stack** (Grafana, Prometheus, Loki) provides metrics, logging, and dashboarding for operational observability [40]. This layer supplies the technical controls and audit evidence required by NIS2 and national security frameworks (Section 7.5) [27, 26].

### 4.10 Data Spaces and the EU Data Act

The **EU Data Act** (Regulation (EU) 2023/2854), in force from September 2025, creates new obligations for data sharing between businesses and government and reshapes the municipal data layer [52]. Three implications follow. First, municipal data assets — transport, utilities, planning — become subject to mandatory sharing obligations under specified conditions, requiring municipalities to expose data through governed, standards-based interfaces. Second, **GAIA-X** provides the technical framework for federated, sovereign data exchange in Europe, defining the trust and interoperability rules under which municipal data can be shared without surrendering sovereignty [56]. Third, municipalities should evaluate participation in sector-specific **data spaces** — urban mobility, energy, environmental monitoring — through which their data can create public value while remaining under their control [56, 52].

The technical requirement is concrete: the municipal data catalogue (**CKAN** [22]) must implement **DCAT-AP 3.0** and register with the relevant national and EU data-space brokers. The EU Data Governance Act (2022) and the Data Act (2023) together mandate open APIs for public-sector data, a requirement that CKAN satisfies natively [52, 22, 44]. The open-data layer specified in Section 4.5 is therefore not merely a transparency instrument but the municipality's compliant participation point in the emerging European data economy.

### 4.11 Composite Scoring Summary

The table below summarises the composite scores (sum of seven equally weighted 0–5 criteria; maximum 35) for the recommended component in each functional layer. Full methodology is in Appendix A.

| Layer | Recommended component | Licence | Maturity | Community | Interop | Security | TCO | Pub-sector | Composite /35 |
|---|---|---|---|---|---|---|---|---|---|
| IAM | Keycloak | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 34 |
| Participation | Decidim | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 31 |
| Collaboration | Nextcloud + Collabora | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 33 |
| Messaging | Matrix / Element | 5 | 4 | 4 | 5 | 5 | 5 | 4 | 32 |
| Open data | CKAN | 5 | 5 | 4 | 5 | 4 | 5 | 5 | 33 |
| Geospatial | GeoServer + QGIS + MapLibre | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 34 |
| Workflow | Camunda + Form.io | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 30 |
| Cloud infra | Sovereign Cloud Stack | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 31 |
| Security/monitoring | OpenZiti + Wazuh + Grafana | 5 | 4 | 4 | 4 | 5 | 5 | 4 | 31 |

All nine layers score 30 or above out of a possible 35, confirming that mature, standards-compliant, publicly deployed open-source components exist for every functional requirement of the municipal estate (answering **RQ1** affirmatively).

---

## 5. Implementation Roadmap

The roadmap spans 36 months in six phases. It is deliberately conservative: each phase delivers standalone value, so that a transition can be paused without stranding investment, and so that political sponsors can demonstrate early wins. Jurisdiction-specific obligations are consolidated in Sections 5.6 (Germany) and 5.7 (Switzerland).

### 5.0 Phase 0: Readiness Assessment (Months 1–3)

Phase 0 establishes the baseline and the mandate. Activities: a full inventory of current applications, licences, data flows, and contract expiry dates; a TCO baseline using the framework in Appendix B; a stakeholder map and the formation of a steering group with explicit political sponsorship; a skills-gap assessment; and the selection of the jurisdiction track (Section 5.6 or 5.7). The deliverable is a board-approved business case and a phased plan. No production systems change in this phase.

### 5.1 Phase 1: Foundation (Months 4–9)

Phase 1 builds the sovereign foundation: deployment of the cloud infrastructure layer (Sovereign Cloud Stack / Kubernetes, Section 4.8) and the IAM layer (Keycloak, Section 4.1), including federation with the national identity system (BundID or Swiyu) [13, 16]. Security and monitoring (Section 4.9) and the initial BSI IT-Grundschutz / ISDS documentation are established in parallel. The deliverable is a running, secured, sovereign platform onto which services are subsequently deployed.

### 5.2 Phase 2: Core Services (Months 10–18)

Phase 2 migrates the highest-value, lowest-risk user-facing services: the collaboration suite (Nextcloud + Collabora, Section 4.3) and secure messaging (Matrix/Element, Section 4.4), which together deliver the most visible per-seat licence savings and the clearest staff-facing benefit. The open-data platform (CKAN, Section 4.5) is also stood up in this phase, delivering an early, publicly visible transparency win. Migration runs in parallel with the incumbent systems to allow rollback.

### 5.3 Phase 3: Integration (Months 19–24)

Phase 3 connects the platform to citizen-facing service delivery: the participation portal (Decidim/CONSUL, Section 4.2) and the workflow and form layer (Camunda + Form.io, Section 4.7), bound to the national interoperability standards (XÖV or eCH) [46, 47]. Geospatial services (Section 4.6) are integrated where municipal functions require them. The deliverable is end-to-end, authenticated, standards-compliant digital services. Target ISMS certification work begins here.

### 5.4 Phase 4: Advanced Capabilities (Months 25–30)

Phase 4 extends the platform: participation in data spaces under the EU Data Act (Section 4.10), DCAT-AP 3.0 registration, and integration with sector-specific data brokers [52, 56]; adoption of additional EfA / GovStack building blocks; and decommissioning of the most expensive remaining proprietary contracts as they reach renewal. The deliverable is a municipality consuming and contributing to shared open infrastructure.

### 5.5 Phase 5: Optimisation and Scaling (Months 31–36)

Phase 5 consolidates: performance optimisation, completion of ISMS certification, contribution of locally developed components back to openCode.de (Germany) or the relevant repository (Switzerland) per the open-by-default mandate, and formalisation of cooperative membership for long-term operation [10, 1, 23]. The deliverable is a steady-state, sovereign, cooperatively supported IT estate with a documented operating model.

### 5.6 German-Jurisdiction Implementation Track

German municipalities must layer the following specific obligations onto the generic roadmap:

- **OZG 2.0 compliance:** all administrative services must be online by the mandated deadlines; consume EfA services from pioneer municipalities via the FITKO portal rather than rebuilding them [9].
- **BundID federation:** Keycloak must federate with BundID (the national citizen identity); configuration steps and API documentation are available at id.bund.de [9, 13].
- **XÖV standards integration:** all data exchange must use XÖV-compliant XML schemas, and forms must use XForms where mandated [46].
- **openCode.de participation:** all custom software must be published on openCode.de in accordance with the OZG 2.0 mandate [10].
- **govdigital eG:** join as a member or procure cloud infrastructure via its framework contracts [23].
- **BSI IT-Grundschutz:** security documentation is mandatory; target ISMS certification within 24 months [26].
- **ZenDiS partnership:** contact ZenDiS for OpenDesk implementation support and access to vetted components [50].
- **NIS2 compliance:** municipalities are treated as "essential entities" under NIS2 from October 2024 and must meet its risk-management and reporting obligations [27].

### 5.7 Swiss-Jurisdiction Implementation Track

Swiss municipalities must layer the following specific obligations onto the generic roadmap:

- **EMBAG compliance:** custom software must be published as open source unless a security exception applies [1].
- **E-Government Strategy 2024–2027:** align the digital-service roadmap with the cantonal and federal strategy [16].
- **eCH standards compliance:** all data exchange must use the applicable eCH XML standards (eCH-0010, -0011, -0044, -0058, -0185) [47].
- **opendata.swiss registration:** publish open datasets via the cantonal CKAN instance to opendata.swiss [44, 22].
- **Swiss eID integration:** configure Keycloak to accept the Swiyu eID when available (from 2026) [16].
- **ISDS framework:** apply the Informationssicherheit und Datenschutz in der Verwaltung framework, the Swiss equivalent of BSI IT-Grundschutz, for security and data-protection documentation.
- **Cantonal IT cooperative membership:** most cantons operate shared IT structures (e.g. cantonal CIO offices / Informatikleistungszentren) offering framework contracts for open-source IT.

---

## 6. Stakeholder and Procurement Strategy

### 6.1 Political Leadership and Council Buy-In

No municipal open-source transition survives without durable political ownership; the LiMux reversal is the cautionary archetype [55]. The strategy must be framed for the council not primarily as a technical project but as one of fiscal responsibility, digital sovereignty, and local economic development, with measurable milestones reported publicly each phase. Securing a cross-party coalition rather than a single sponsor is the principal insurance against reversal when administrations change [55, 4].

### 6.2 IT Staff Capability Development

Open-source operation shifts cost from licences to skills, so capability development is not optional. The strategy combines formal training (Linux, Kubernetes, Keycloak, the chosen application stack), embedded vendor-supported implementation in early phases, and participation in the relevant communities (ZenDiS, SCS, OSOR) for knowledge transfer [50, 3, 51]. For small municipalities, the cooperative model substitutes shared operational capacity for in-house depth (Section 3.10) [23].

### 6.3 Citizen Communication and Participation

Citizens experience the transition through new portals and services; the communication strategy must explain the sovereignty and transparency rationale and use the participation platform (Decidim/CONSUL) itself to gather feedback, turning the migration into a demonstration of open government [12, 48, 53]. Visible early wins — a working open-data portal, improved online services — build public support that reinforces political backing.

### 6.4 EU Procurement Law and Open-Source Compliance

Procurement is where open-source strategies most often fail on technicalities, so the legal framing must be precise. EU Directive 2014/24/EU on public procurement applies, implemented nationally via the GWB and VgV in Germany and via the BöB and IVöB in Switzerland [43]. The key conceptual point is that open-source software is *free to use* — what the municipality procures is not the software but the **services** around it: implementation, hosting, support, customisation, and training. Tenders must therefore be written for services, not for a product licence.

Award criteria must apply the **Most Economically Advantageous Tender (MEAT)** principle, explicitly weighting total cost of ownership, interoperability, and exit costs rather than unit price alone — otherwise the structural advantages of open source (categories f and g in Section 3.9) are invisible to the evaluation [43]. Custom deliverables should carry a **"Public Money? Public Code!"** contractual clause requiring an OSI-approved licence for all bespoke software [4]. Finally, existing cooperative **framework agreements** (Section 6.5) allow individual procurements under threshold to proceed without a full tender, materially reducing transaction cost [23, 24].

### 6.5 Framework Agreements and Cooperative Procurement

Cooperative procurement structures are the practical mechanism that makes the strategy procurable, especially for smaller municipalities:

- **govdigital eG (Germany):** a member-owned cooperative of public IT providers; its framework contracts satisfy GWB/Vergaberecht and allow members to procure compliant open-source cloud and services without individual full tenders [23].
- **Dataport AöR (Germany):** an Anstalt des öffentlichen Rechts (institution under public law) that may receive direct assignments without tender from its member states, providing a fully compliant route to shared open-source infrastructure [24].
- **Swiss cantonal IT cooperatives:** analogous structures; most cantons operate Informatikleistungszentren with open-procurement frameworks that municipalities can draw upon.
- **ZenDiS (Germany):** its components are freely available, and integration support can be procured through the ZenDiS partner ecosystem [50].

---

## 7. Risk Analysis

### 7.1 Organisational Change Resistance

The dominant risk is human, not technical: staff and managers accustomed to incumbent tools resist change, and resistance compounds when migrations are perceived as imposed. Mitigation combines early staff involvement, parallel running to reduce fear of disruption, visible quick wins, and adequate training budget (Section 6.2). Phasing the roadmap so that each step is reversible and value-delivering directly reduces this risk [55].

### 7.2 Skills and Capacity Gaps

A municipality may lack the skills to operate the stack, particularly at the infrastructure layer. Mitigation: front-load vendor-supported implementation, invest in training, and — decisively for small municipalities — consume infrastructure as a cooperative service rather than operating it in-house (Sections 3.10, 6.5) [23, 24]. The Sovereign Cloud Stack's curated, patched component set reduces the operational skill threshold [3, 11].

### 7.3 Technology Integration Complexity

Integrating nine layers and federating with national identity and interoperability systems is genuinely complex. Mitigation: adopt standards-based components throughout (OIDC, BPMN, DCAT-AP, OGC, XÖV, eCH), prefer GovStack-aligned building-block architecture to reduce bespoke integration, and sequence integration (Phase 3) after the foundation is stable [49, 46, 47].

### 7.4 Vendor Lobbying and FUD Mitigation

This risk is consistently underestimated. Proprietary vendors routinely engage in FUD (Fear, Uncertainty, Doubt) campaigns against open-source transitions. Observed strategies include exaggerating migration complexity, inflating the TCO of open source, leveraging personal relationships with IT staff, funding nominally "independent" studies, and timing price concessions to coincide with transition-decision moments. The Munich case documents the role vendor lobbying played in the LiMux reversal — though the new city council reversed course again toward open source in 2019 [55].

Mitigation is procedural and political: commission **independent** TCO studies before entering vendor negotiations; engage civil society as transparency watchdogs; publish all procurement decisions openly; and use the FSFE's "Public Money? Public Code!" framing as political cover that reframes any reversal as a retreat from fiscal responsibility and sovereignty [4, 55].

### 7.5 Supply Chain and Open-Source Security Risks

The 2021 Log4Shell vulnerability demonstrated that open-source supply-chain risk requires structured management rather than blind trust. Concrete controls:

- Require a **Software Bill of Materials (SBOM)** in CycloneDX or SPDX format for all deployed open-source components.
- Use the **OpenSSF Scorecard** (CNCF/OpenSSF) to evaluate the security health of candidate components.
- Subscribe to **CVE feeds** for all stack components and implement an automated patching pipeline.
- Prefer the **Sovereign Cloud Stack**, which supplies a curated, tested, security-patched component set [3, 11].
- Apply BSI IT-Grundschutz Bausteine **INF.14, OPS.1.1.3, and OPS.1.2.4**, which cover patch management [26].
- Meet **NIS2 Article 21**, which requires supply-chain security measures for essential entities [27].

Properly managed, open-source supply-chain risk is *more* tractable than proprietary risk, because the components are inspectable and the patch process is not gated by a single vendor.

---

## 8. Conclusion

This paper set out to determine whether a sovereign, open-source municipal IT strategy is technically feasible, economically advantageous, and operationally realisable across municipalities of differing sizes and across the German and Swiss jurisdictions. The evidence supports an affirmative answer on all counts.

On **RQ1**, a coherent, mature open-source stack exists for every one of the nine functional layers, with all recommended components scoring at least 30 of 35 on a transparent seven-criterion matrix. On **RQ2**, the total cost of ownership of the open-source stack is 30–50% lower over five years when all cost categories are honestly included, driven by the elimination of €100–300/seat/year licence costs and the near-elimination of exit and lock-in costs, corroborated by the DGFiP and Barcelona cases — though the field still lacks independent comparative studies. On **RQ3**, a conservative, value-delivering 36-month roadmap is achievable, with fully specified German and Swiss tracks aligning the generic plan to OZG/BundID/XÖV/BSI and EMBAG/eCH/Swiyu/ISDS obligations respectively. On **RQ4**, durable success depends less on technology than on cross-party political ownership, capability development, compliant cooperative procurement, and disciplined mitigation of vendor lobbying and supply-chain risk.

The central conclusion is that municipal IT can be *sovereign by design* today. The components are mature, the standards exist, the institutional support (ZenDiS, GovStack, OSOR, the cooperatives) is in place, and the law increasingly mandates the direction of travel. The remaining barriers are organisational and political, not technological — and they are, with the strategies set out here, surmountable.

---

## References

[1] Swiss Confederation. (2023). *Federal Act on the Use of Electronic Means for the Fulfilment of Government Tasks (EMBAG)*. Bern: Federal Chancellery. https://www.fedlex.admin.ch/ — [Open access, federal legislation]

[2] Floridi, L. (2020). The Fight for Digital Sovereignty: What It Is, and Why It Matters, Especially for the EU. *Philosophy & Technology*, 33, 369–378. https://doi.org/10.1007/s13347-020-00423-6

[3] Sovereign Cloud Stack Community. (2023). *Sovereign Cloud Stack: A Standardised, Open-Source Cloud Reference Implementation*. Berlin: Open Source Business Alliance. https://scs.community/ — [Open access]

[4] Free Software Foundation Europe (FSFE). (2019). *Public Money? Public Code! Modernising Public Infrastructure with Free Software*. Berlin: FSFE. https://publiccode.eu/ — [Open access, CC-BY-SA]

[5] Pohle, J., & Thiel, T. (2020). Digital Sovereignty. *Internet Policy Review*, 9(4). https://doi.org/10.14763/2020.4.1532

[6] Margetts, H., & Dunleavy, P. (2013). The Second Wave of Digital-Era Governance: A Quasi-Paradigm for Government on the Web. *Philosophical Transactions of the Royal Society A*, 371(1987). https://doi.org/10.1098/rsta.2012.0382

[7] Dunleavy, P., Margetts, H., Bastow, S., & Tinkler, J. (2006). *Digital Era Governance: IT Corporations, the State, and E-Government*. Oxford: Oxford University Press. ISBN 978-0-19-929619-4

[8] OECD. (2014). *Recommendation of the Council on Digital Government Strategies*. Paris: OECD Publishing. https://www.oecd.org/

[9] Bundesministerium des Innern und für Heimat (BMI). (2023). *Onlinezugangsgesetz (OZG 2.0): Umsetzung und das Einer-für-Alle-Prinzip*. Berlin: BMI. https://www.onlinezugangsgesetz.de/ — [Open access]

[10] FITKO. (2023). *openCode.de: Die Plattform für Open Source in der öffentlichen Verwaltung*. Frankfurt am Main: FITKO. https://opencode.de/ — [Open access]

[11] Open Source Business Alliance. (2023). *Gaia-X and the Sovereign Cloud Stack: Building Sovereign Cloud Infrastructure for Europe*. Stuttgart: OSB Alliance. https://osb-alliance.de/ — [Open access]

[12] Barandiaran, X., Calleja-López, A., & Monterde, A. (2018). *Decidim: A Brief Overview*. Barcelona: Ajuntament de Barcelona / Decidim Free Software Association. https://decidim.org/ — [Open access, AGPL-3.0]

[13] Keycloak Community / Red Hat. (2023). *Keycloak: Open Source Identity and Access Management — Documentation*. https://www.keycloak.org/ — [Open access, Apache-2.0]

[14] Nextcloud GmbH. (2023). *Nextcloud Hub: Self-Hosted Content Collaboration Platform — Technical Documentation*. Stuttgart: Nextcloud. https://nextcloud.com/ — [Open access, AGPL-3.0]

[15] Collabora Productivity. (2023). *Collabora Online: Enterprise-Ready LibreOffice in the Browser*. Cambridge: Collabora. https://www.collaboraonline.com/ — [Open access, MPL-2.0]

[16] E-Government Switzerland. (2024). *Digital Public Services Switzerland: E-Government Strategy 2024–2027 and the E-ID (Swiyu)*. Bern: Digitale Verwaltung Schweiz. https://www.digitale-verwaltung-schweiz.ch/ — [Open access]

[17] The Matrix.org Foundation. (2023). *Matrix: An Open Standard for Secure, Decentralised, Real-Time Communication*. https://matrix.org/ — [Open access, Apache-2.0]

[18] Camunda Services GmbH. (2023). *Camunda Platform: BPMN Workflow and Decision Automation — Documentation*. Berlin: Camunda. https://camunda.com/ — [Open access, Apache-2.0]

[19] Janssen, M., Charalabidis, Y., & Zuiderwijk, A. (2012). Benefits, Adoption Barriers and Myths of Open Data and Open Government. *Information Systems Management*, 29(4), 258–268. https://doi.org/10.1080/10580530.2012.716740

[20] Linåker, J., & Runeson, P. (2022). Public Sector Platforms Going Open: Creating and Growing an Ecosystem with Open Collaborative Development. *Empirical Software Engineering*, 27, 95. https://doi.org/10.1007/s10664-022-10157-y

[21] Fitzgerald, B. (2006). The Transformation of Open Source Software. *MIS Quarterly*, 30(3), 587–598. https://doi.org/10.2307/25148740

[22] Open Knowledge Foundation. (2023). *CKAN: The Open Source Data Management System — Documentation*. https://ckan.org/ — [Open access, AGPL-3.0]

[23] govdigital eG. (2023). *Genossenschaft der öffentlichen IT-Dienstleister: Rahmenverträge und Mitgliedschaft*. Berlin: govdigital. https://www.govdigital.de/ — [Open access]

[24] Dataport AöR. (2023). *Dataport: Der IT-Dienstleister für die öffentliche Verwaltung — Jahresbericht*. Altenholz: Dataport. https://www.dataport.de/ — [Open access]

[25] World Bank. (2022). *GovTech Maturity Index: The State of Public Sector Digital Transformation*. Washington, DC: World Bank. https://www.worldbank.org/

[26] Bundesamt für Sicherheit in der Informationstechnik (BSI). (2023). *IT-Grundschutz-Kompendium*. Bonn: BSI. https://www.bsi.bund.de/ — [Open access]

[27] European Parliament and Council. (2022). *Directive (EU) 2022/2555 on Measures for a High Common Level of Cybersecurity Across the Union (NIS2)*. Official Journal of the European Union. https://eur-lex.europa.eu/ — [Open access, EU legislation]

[28] European Commission. (2020). *Open Source Software Strategy 2020–2023: Think Open*. Brussels: European Commission. https://commission.europa.eu/ — [Open access]

[29] Heath, T., & Bizer, C. (2011). *Linked Data: Evolving the Web into a Global Data Space*. San Rafael: Morgan & Claypool. https://doi.org/10.2200/S00334ED1V01Y201102WBE001

[30] Bertot, J. C., Jaeger, P. T., & Grimes, J. M. (2010). Using ICTs to Create a Culture of Transparency: E-Government and Social Media as Openness and Anti-Corruption Tools. *Government Information Quarterly*, 27(3), 264–271. https://doi.org/10.1016/j.giq.2010.03.001

[31] Layne, K., & Lee, J. (2001). Developing Fully Functional E-Government: A Four Stage Model. *Government Information Quarterly*, 18(2), 122–136. https://doi.org/10.1016/S0740-624X(01)00066-1

[32] Eaves, D., Mazzucato, M., & Vasconcellos, B. (2024). *Digital Public Infrastructure and Public Value*. UCL Institute for Innovation and Public Purpose Working Paper. London: UCL IIPP.

[33] Mergel, I., Edelmann, N., & Haug, N. (2019). Defining Digital Transformation: Results from Expert Interviews. *Government Information Quarterly*, 36(4). https://doi.org/10.1016/j.giq.2019.06.002

[34] West, J., & Gallagher, S. (2006). Challenges of Open Innovation: The Paradox of Firm Investment in Open-Source Software. *R&D Management*, 36(3), 319–331. https://doi.org/10.1111/j.1467-9310.2006.00436.x

[35] Lessig, L. (2006). *Code: Version 2.0*. New York: Basic Books. ISBN 978-0-465-03914-2

[36] Benkler, Y. (2006). *The Wealth of Networks: How Social Production Transforms Markets and Freedom*. New Haven: Yale University Press. ISBN 978-0-300-12577-1

[37] Raymond, E. S. (1999). *The Cathedral and the Bazaar: Musings on Linux and Open Source by an Accidental Revolutionary*. Sebastopol: O'Reilly Media. ISBN 978-1-565-92724-7

[38] Schmidt, K. M., & Schnitzer, M. (2003). Public Subsidies for Open Source? Some Economic Policy Issues of the Software Market. *Harvard Journal of Law & Technology*, 16(2), 473–505.

[39] Lerner, J., & Tirole, J. (2002). Some Simple Economics of Open Source. *Journal of Industrial Economics*, 50(2), 197–234. https://doi.org/10.1111/1467-6451.00174

[40] Cloud Native Computing Foundation (CNCF). (2023). *CNCF Landscape: Security, Observability, and Zero-Trust Projects*. San Francisco: CNCF. https://landscape.cncf.io/ — [Open access]

[41] QGIS Project / OSGeo. (2023). *QGIS and the Open Source Geospatial Stack — Documentation*. Beaverton: OSGeo. https://qgis.org/ — [Open access, GPL-2.0]

[42] European Parliament and Council. (2007). *Directive 2007/2/EC Establishing an Infrastructure for Spatial Information in the European Community (INSPIRE)*. Official Journal of the European Union. https://eur-lex.europa.eu/ — [Open access, EU legislation]

[43] European Commission. (2017). *New European Interoperability Framework: Promoting Seamless Services and Data Flows for European Public Administrations*. Luxembourg: Publications Office of the EU. https://ec.europa.eu/isa2/eif_en — [Open access]

[44] European Parliament and Council. (2019). *Directive (EU) 2019/1024 on Open Data and the Re-use of Public Sector Information*. Official Journal of the European Union. https://eur-lex.europa.eu/ — [Open access, EU legislation]

[45] United Nations. (2022). *UN E-Government Survey 2022: The Future of Digital Government*. New York: UN Department of Economic and Social Affairs. https://publicadministration.un.org/

[46] KoSIT (Koordinierungsstelle für IT-Standards). (2023). *XÖV-Framework: Standards für den XML-Datenaustausch in der öffentlichen Verwaltung*. Bremen: KoSIT. https://www.xoev.de/ — [Open access]

[47] eCH Association. (2024). *eCH Standards for Swiss E-Government: Registry and Overview*. Bern: eCH. https://www.ech.ch/ — [Open access]

[48] Ayuntamiento de Madrid. (2019). *CONSUL Democracy: Open Government and Civic Participation*. Madrid. https://consulproject.org/ — [Open access, AGPL-3.0]

[49] ITU/DIAL/BMZ/Government of Estonia. (2022). *GovStack: Building Blocks for Digital Government*. Geneva: ITU. https://www.govstack.global/ — [Open access, CC-BY-4.0]

[50] ZenDiS GmbH. (2023). *Zentrum für Digitale Souveränität der öffentlichen Verwaltung: Annual Overview*. Berlin: ZenDiS. https://zendis.de/ — [Open access]

[51] European Commission, OSOR. (2023). *Open Source Observatory Annual Report 2023*. Brussels: European Commission. https://joinup.ec.europa.eu/collection/open-source-observatory-osor — [Open access, CC-BY-4.0]

[52] European Parliament and Council. (2023). *Regulation (EU) 2023/2854 — EU Data Act*. Official Journal of the European Union. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202320238 — [Open access, EU legislation]

[53] Lathrop, D., & Ruma, L. (Eds.). (2010). *Open Government: Collaboration, Transparency, and Participation in Practice*. Sebastopol: O'Reilly Media. ISBN 978-0-596-80435-0

[54] Direction Générale des Finances Publiques (DGFiP). (2021). *Migration vers LibreOffice: Retour d'expérience de la DGFiP*. Paris: DGFiP. https://www.numerique.gouv.fr/publications/libre-office-retour-experience/ — [Open access]

[55] Landeshauptstadt München. (2017). *Abschlussbericht Limux — Ende des Linux-Einsatzes*. München: Stadtrat München. [Public record]

[56] GAIA-X Association for Data and Cloud (AISBL). (2023). *GAIA-X: Architecture Overview and Technical Standards*. Brussels: GAIA-X AISBL. https://gaia-x.eu/ — [Open access]

---

## Appendix A: Technology Scoring Methodology

Each candidate component is scored on seven criteria, each on a 0–5 ordinal scale. In v0.2.0 all criteria are weighted equally; the composite score is the unweighted sum (maximum 35). Future versions may apply governance-specific weights (for example, raising the weight of interoperability-standards compliance for jurisdictions with strict mandatory standards).

**1. Licence openness (0–5).**
5 = OSI-approved copyleft or permissive licence; 4 = copyleft with caveats (e.g. CLA requirements or dual-licensing tension); 3 = source-available but not OSI-approved; 1–2 = partially open / open-core with significant proprietary components; 0 = proprietary.

**2. Deployment maturity (0–5).**
5 = 10+ years of production use; 4 = 5+ years; 3 = 2+ years; 2 = less than 2 years in production; 1 = beta; 0 = pre-release/experimental.

**3. Community health (0–5).**
Assessed from contributor count, release cadence, governance structure, and *bus factor* (resilience to loss of key contributors). 5 = large, diverse, well-governed community with foundation backing; lower scores reflect concentration of contribution, irregular releases, or weak governance.

**4. Interoperability-standards compliance (0–5).**
Adherence to the relevant open standards for the layer — OIDC/SAML, DCAT-AP, XÖV, eCH, OGC (WMS/WFS), BPMN, etc. 5 = full, certified compliance with all relevant standards; lower scores reflect partial or non-certified compliance.

**5. Security posture (0–5).**
Assessed from CVE response time, security-audit history, and penetration-test coverage. 5 = audited, rapid CVE response, documented disclosure process; lower scores reflect thinner security track records.

**6. Total cost of ownership (0–5).**
5 = no licence cost and low operational overhead; graduated downward as licence cost and/or operational overhead rise, to 0 = high licence cost.

**7. Verified public-sector deployments (0–5).**
5 = widespread EU government use with documented references; graduated downward through national/regional/single deployments to 0 = no verified public-sector use.

**Composite.** The seven scores are summed with equal weight to a maximum of 35. A component scoring below ~21 (60%) in any layer would prompt re-evaluation of the recommendation; in this paper all recommended components score 30 or above.

---

## Appendix B: Implementation Cost Model

The model below is an estimation framework, not a quotation. Figures are indicative ranges in euros and must be calibrated against local labour costs, the scope of migration, and existing contract terms (see the caveats in Section 3.9). Savings derive primarily from eliminated licence costs (€100–300/seat/year) plus reduced vendor service fees.

| Municipality size | Population | Phase 0–1 cost | Full 36-month programme | Annual savings after Year 3 |
|---|---|---|---|---|
| Small | 5,000–25,000 | €80,000–€150,000 | €250,000–€500,000 | €40,000–€80,000 |
| Medium | 25,000–150,000 | €200,000–€400,000 | €700,000–€1,500,000 | €150,000–€350,000 |
| Large | 150,000–500,000 | €500,000–€1,000,000 | €2,000,000–€5,000,000 | €500,000–€1,200,000 |

**Cost-category breakdown (applies to all sizes).** The full-programme figure aggregates: implementation and integration labour (largest line); training and change management; security and certification (BSI IT-Grundschutz / ISDS, ISMS); hosting/infrastructure (own hardware or cooperative service); and contingency. Recurring licence cost is €0 across the programme.

**Savings logic.** For a medium municipality with ~1,500 staff seats at an avoided licence cost of €150–250/seat/year, eliminated per-seat licences alone yield ~€225,000–€375,000 per year, before adding reduced vendor service fees and avoided lock-in price escalation. Small municipalities realise proportionally smaller absolute savings but benefit disproportionately from cooperative and EfA cost-sharing (Section 3.10). Net positive cumulative cash flow is typically reached between Year 3 and Year 4, after which savings compound.

**Sensitivity.** The dominant variables are (i) seat count and avoided per-seat licence price, (ii) local IT labour cost, and (iii) the proportion of operation insourced versus consumed cooperatively. Small municipalities should assume the cooperative-consumption model to keep the operational-labour line low.

---

## Appendix C: Municipal CIO Checklist

A practical decision checklist, organised by phase. Each item is a yes/no gate; unresolved items should be closed before the phase is declared complete.

**Phase 0 — Readiness Assessment**
- [ ] Complete inventory of applications, licences, data flows, and contract expiry dates produced.
- [ ] TCO baseline established using the Appendix B framework, calibrated to local costs.
- [ ] Steering group formed with explicit, cross-party political sponsorship.
- [ ] Skills-gap assessment completed; training budget provisionally sized.
- [ ] Jurisdiction track selected (Section 5.6 Germany or 5.7 Switzerland).
- [ ] Board-approved business case signed off.

**Phase 1 — Foundation**
- [ ] Cloud infrastructure (SCS / Kubernetes) deployed or procured via cooperative.
- [ ] Keycloak IAM deployed; federation with BundID or Swiyu planned/tested.
- [ ] Security/monitoring stack (OpenZiti, Wazuh, Grafana) operational.
- [ ] Initial BSI IT-Grundschutz / ISDS documentation started.

**Phase 2 — Core Services**
- [ ] Nextcloud + Collabora deployed; pilot user group migrated in parallel running.
- [ ] Matrix/Element messaging operational.
- [ ] CKAN open-data portal live; first datasets published (DCAT-AP-compliant).
- [ ] Per-seat licence savings being tracked against the baseline.

**Phase 3 — Integration**
- [ ] Decidim/CONSUL participation portal live and integrated with IAM.
- [ ] Camunda + Form.io workflow services bound to XÖV / eCH data models.
- [ ] Geospatial services integrated where required (INSPIRE/OGC-compliant).
- [ ] ISMS certification work commenced; target date set.

**Phase 4 — Advanced Capabilities**
- [ ] Data Act / data-space participation evaluated; DCAT-AP 3.0 registration done.
- [ ] Additional EfA / GovStack building blocks adopted where beneficial.
- [ ] Most expensive remaining proprietary contracts scheduled for decommission.

**Phase 5 — Optimisation and Scaling**
- [ ] ISMS certification achieved.
- [ ] Locally developed components published per open-by-default mandate (openCode.de / repository).
- [ ] Cooperative membership formalised for long-term operation and procurement.
- [ ] Steady-state operating model documented and resourced.

**Cross-cutting (all phases)**
- [ ] Independent TCO study commissioned before any vendor negotiation (Section 7.4).
- [ ] All procurement decisions published openly.
- [ ] SBOM (CycloneDX/SPDX) required for every deployed component; CVE feeds subscribed.
- [ ] "Public Money? Public Code!" licence clause included in all custom-software contracts.
