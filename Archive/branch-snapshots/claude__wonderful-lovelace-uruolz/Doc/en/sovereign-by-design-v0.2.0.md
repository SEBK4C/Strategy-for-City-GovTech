---
title: "Sovereign by Design: A State-of-the-Art Open-Source Technology Strategy for Municipal Governments"
author: "Sebastian Graf, Autonomous Office of Civil Digital Infrastructure"
correspondence: "sebk4c@tuta.com"
version: "0.2.0"
status: "Citation-Complete Draft"
date: "2026-06-20"
language: "en"
source-of-truth: true
SPDX-License-Identifier: "CC-BY-4.0"
previous-version: "0.1.0"
changelog: "v0.1.0→v0.2.0: Expanded literature review (§3.7–3.9), four new technology components (§4.10–4.13), detailed phase checklists (§5), TCO methodology and KPI framework (§6), GDPR and exit-strategy analysis (§7), glossary (§9), regulatory appendix. References [47]–[57] added."
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
  - EU Data Act
  - GovStack
  - total cost of ownership
---

# Sovereign by Design: A State-of-the-Art Open-Source Technology Strategy for Municipal Governments

**Author:** Sebastian Graf, Autonomous Office of Civil Digital Infrastructure  
**Correspondence:** sebk4c@tuta.com  
**Version:** 0.2.0 — Citation-Complete Draft  
**Previous version:** [v0.1.0](sovereign-by-design-v0.1.0.md)  
**Date:** 2026-06-20  
**Languages:** English (source of truth) · [Deutsch](../de/sovereign-by-design-v0.2.0.de.md)  
**SPDX-License-Identifier:** CC-BY-4.0  

---

## Abstract

Municipal governments are the closest layer of democratic administration to citizens, yet they face an acute structural tension: the digital tools they depend on are increasingly proprietary, vendor-locked, and misaligned with public-interest values. Recurring software licence costs consume public budgets that could fund services; vendor dependencies create structural barriers to transparency and democratic accountability; and closed-source infrastructure prevents independent security auditing essential for public trust.

This paper presents a comprehensive, citation-complete strategy for implementing a state-of-the-art, open-source governmental administration technology stack in city governments. Drawing on landmark legislation — Switzerland's EMBAG Act (2024), Germany's OZG 2.0 reform, the European Union's Interoperable Europe Act (2024) and Data Governance Act (2022) — as well as exemplary deployments from Barcelona, Helsinki, the German federal administration's OpenDesk initiative, and multiple Swiss cantons, we derive a first-principles implementation roadmap suitable for municipalities from 5,000 to 500,000 population.

We evaluate fourteen technology components across seven functional layers against criteria of digital sovereignty, interoperability, security posture, total cost of ownership, and civic alignment. We present a phased 36-month implementation roadmap with phase-gated checklists, a procurement framework adapted to German and Swiss public-procurement law, a total cost of ownership methodology, and a key performance indicator framework for measuring success.

We conclude that: (1) open-source municipal technology stacks are technically mature and production-proven across every functional requirement; (2) the regulatory environment in Switzerland, Germany, and the EU increasingly mandates open standards and open-source defaults; (3) the economic case, when total costs including vendor lock-in risk are correctly modelled, systematically favours open-source; and (4) success depends as much on political mandate, change management, and community engagement as on technical implementation.

**Keywords:** digital sovereignty, open source government, GovTech, municipal digital transformation, interoperability, OZG, EMBAG, Sovereign Cloud Stack, e-government, civic technology, EU Data Act, GovStack, total cost of ownership

---

## 1. Introduction

The digital transformation of municipal government is no longer optional. Citizens expect seamless, secure, and accessible digital services; regulators demand interoperability and data protection; and fiscal pressures require sustainable, cost-effective technology investments. Yet the majority of city governments remain trapped in a cycle of proprietary vendor dependency, expensive licence agreements, and fragmented systems that impede rather than enable good governance [1, 29].

The consequences of this dependency are well-documented: vendor lock-in raises switching costs and bargaining asymmetry [4]; proprietary formats obstruct cross-agency data exchange and transparency [45]; closed-source infrastructure prevents independent security auditing [26]; and recurring licence fees drain budgets that could otherwise fund service delivery [3, 5]. Most fundamentally, when the software running democratic institutions is owned and controlled by private actors, a structural conflict of interest emerges between the public interest and corporate imperatives [4].

A different path is both possible and proven. The evidence from pioneering jurisdictions is now substantial:

- Switzerland's 2023 **EMBAG** legislation mandates that federal software developed with public funds be released as open source by default [1].
- The German federal government's **OpenDesk** initiative demonstrates that a complete, curated open-source workplace suite can be deployed at scale [42].
- The **Sovereign Cloud Stack** (SCS), backed by the German Federal Ministry, provides a fully auditable, self-hostable cloud infrastructure meeting the highest European sovereignty standards [3].
- The Free Software Foundation Europe's **"Public Money? Public Code!"** campaign has secured endorsements from over 200 organisations across 30 countries [4].
- **Schleswig-Holstein** announced in 2021 a systematic migration of 25,000 civil-servant workstations from Microsoft Office to LibreOffice — the largest such migration in a German Land [47].
- The EU's **Interoperable Europe Act** (2024) and **Data Governance Act** (2022) create binding obligations that proprietary, closed-format systems cannot sustainably satisfy [6, 48].

This paper synthesises these developments into a practical, evidence-based strategy for municipal governments, addressing all relevant stakeholders: city administrators, elected officials, IT teams, procurement offices, civil-society groups, open-source communities, and sovereign technology providers.

### 1.1 Scope and Definitions

*Municipal government* refers to city and local government authorities, including Gemeinden, Kommunen, Städte, and equivalent structures in Swiss cantons. The strategy scales from small municipalities (5,000–50,000 population) to large cities (500,000+).

*Open-source technology stack* refers to software components licensed under OSI-approved licences, deployed on infrastructure that the municipality controls or can migrate away from without undue cost or friction.

*Digital sovereignty* is the ability of a government to make independent decisions about its digital infrastructure, including the right to inspect, modify, audit, and migrate software without dependency on a single vendor [3].

*Total cost of ownership (TCO)* includes all costs over a defined lifecycle: software licences, implementation, hosting, maintenance, training, support, and exit costs, including the risk-adjusted cost of vendor lock-in.

### 1.2 Research Questions

1. What does a state-of-the-art open-source municipal technology stack look like in 2026?
2. What lessons can be drawn from the Swiss, German, and European sovereign technology communities?
3. What is the optimal phased implementation pathway for a city of 50,000–500,000 population?
4. How should procurement, stakeholder engagement, and risk management be structured to maximise success?
5. What quantitative metrics best capture progress toward digital sovereignty?

---

## 2. Methodology

This paper employs a multi-method research design combining:

**Systematic literature review** of peer-reviewed publications, grey literature, and policy documents published 2010–2026, covering e-government theory, digital sovereignty, open-source software in public administration, and municipal digital transformation.

**Comparative policy analysis** of technology legislation and strategies from Switzerland (EMBAG 2023, E-Government Strategy 2024–2027, E-ID-Gesetz 2023), Germany (OZG 2017/2024, Schleswig-Holstein open-source plan), and the EU (Interoperable Europe Act 2024, Data Governance Act 2022, EU Open Source Strategy 2020–2023).

**Technology stack evaluation** using a structured scoring matrix (7 criteria, 1–5 per criterion, maximum composite 35): (a) licence openness, (b) deployment maturity, (c) community health, (d) interoperability standards compliance, (e) security posture, (f) TCO, (g) existing public-sector deployments.

**Stakeholder analysis** using the Power–Interest Grid.

**Case study analysis** of five municipal implementations: Barcelona, German Federal Government (OpenDesk), Schleswig-Holstein, Helsinki, and the Swiss Federal Administration.

The literature review is self-improving: `Mem/source-registry.md` and `Mem/literature-review-state.md` are versioned and updated quarterly via `Scripts/update_literature_review.py`.

### 2.1 Inclusion Criteria

Sources included if they: (a) address open-source software in public administration; (b) cover governmental digital transformation; (c) relate to the European, Swiss, or German regulatory context; or (d) provide primary data on municipal technology implementations.

### 2.2 Limitations

Technology assessments reflect publicly available information as of June 2026. Implementation cost estimates are indicative and require local validation. Case studies rely on published accounts.

---

## 3. Literature Review

### 3.1 Theoretical Foundations of E-Government

The academic literature on e-government has evolved through four broad phases [30]. First-generation (1995–2005) focused on digitising existing processes [29]. Second-generation (2005–2012) emphasised online service delivery and back-office integration [7]. Third-generation (2012–2020) introduced open data, participatory platforms, and mobile-first design [8]. The current fourth generation (2020–present) is characterised by platform government, digital identity infrastructure, data spaces, and the sovereignty turn [45].

Wirtz and Weyerer's holistic e-government maturity model identifies five dimensions: technical infrastructure, process quality, service quality, citizen orientation, and transparency [7]. The GovStack initiative (ITU/DIAL) operationalises digital government transformation through modular, interoperable "building blocks" — standardised digital components composable into country-specific implementations [50].

### 3.2 Digital Sovereignty in Public Administration

Digital sovereignty has moved from academic concept to policy imperative in the European context [3, 5]. The EU Open Source Strategy 2020–2023 established "sharing and reuse" as a core principle [5]. The 2024 Interoperable Europe Act creates binding cross-border interoperability obligations [6].

Germany's Sovereign Cloud Stack (SCS), developed by the Open Source Business Alliance (OSBA) and funded in part by BMWK, provides a fully open-source, self-hostable cloud platform (OpenStack + Kubernetes + Ceph) enabling technical and legal sovereignty [3, 11].

Switzerland's EMBAG, in force since 1 January 2024, requires all federally funded software to be released as open source by default — placing Switzerland among the most progressive jurisdictions globally [1].

### 3.3 The German OZG Ecosystem

The Onlinezugangsgesetz (OZG, 2017/2024) requires all German administrations to offer services online [2]. OZG 2.0 introduces the "Once Only" principle, EfA (Einer für Alle) shared service development, BundID, and FITKO coordination [9, 10].

**Schleswig-Holstein** (2021) committed to migrating 25,000 workstations from proprietary software to LibreOffice, Nextcloud, and Thunderbird — the most ambitious Land-level open-source programme in Germany [47].

**ZenDiS GmbH** (est. 2022) coordinates OpenDesk and the federal open-source portfolio. Its 2023 annual report documents OpenDesk deployment to 10,000+ federal civil servants [49].

The openCode.de platform provides a centralised government open-source repository, enabling discovery and reuse [10].

### 3.4 Swiss Cantonal and Federal Digital Services

**eCH standards** (maintained by the Swiss e-government standards organisation eCH) define data formats and interfaces for Swiss public administration at all levels — the Swiss equivalent of Germany's XÖV [51]. Key standards: eCH-0010 (address), eCH-0044 (persons), eCH-0261 (cloud for government).

**Swiss eID** (E-ID-Gesetz 2023): after the 2021 referendum rejected the first eID law, a new law was enacted in 2023 establishing a state-issued, privacy-preserving digital identity using selective disclosure principles [52].

**opendata.swiss** — CKAN-based national open data portal cataloguing datasets from federal, cantonal, and municipal authorities [44].

**GEVER** — standardised records management framework for the federal administration, with cantonal implementations [43].

### 3.5 Open-Source Communities and Sovereign Technology

**Decidim** (Barcelona, 2016) is deployed by 400+ organisations in 40 countries — Barcelona, Helsinki, the Swiss canton of Schaffhausen, New York City [12]. Barcelona's 2016 participatory budgeting exercise engaged 70,000+ participants [54].

**CONSUL Democracy** (Madrid, 2015) is an alternative participatory platform emphasising direct democracy mechanisms — citizen initiatives, referendums [53].

**Matrix/Element** — the German BundesMessenger and French Tchap both operate on Matrix, validating its public-sector suitability [14].

**Nextcloud** (Stuttgart, 2016) serves the Swiss Federal Administration (~40,000 civil servants), thousands of German municipalities, and EU institutions [13].

**OpenDesk** (Germany, 2023), managed by ZenDiS GmbH, is the first government-curated open-source workplace suite at scale: Nextcloud + Cryptpad + OpenProject + Jitsi + Element + Collabora [42, 49].

### 3.6 The EU Data Governance Act and Data Act

The **Data Governance Act** (Regulation (EU) 2022/868, applicable from September 2023) requires public bodies to make data available on non-exclusive, fair terms — creating structural pull toward open data architectures and against proprietary data silos [48].

The **Data Act** (Regulation (EU) 2023/2854, applicable from September 2025) grants governments emergency access to private-sector data, establishes cloud switching rights, and strengthens data portability — making vendor lock-in legally more fragile [55].

Together, these regulations structurally advantage open-source, standards-based architectures.

### 3.7 GovStack and the Building-Block Approach

The **GovStack** initiative (ITU/DIAL, 2021) provides an international framework implementing digital government through modular "building blocks": identity, payments, registration, messaging, scheduling, consent, workflow [50]. The building-block specifications align with EU interoperability requirements and map directly to the technology stack in Section 4.

### 3.8 Case Studies

**Barcelona:** The 2016–2023 Digital City Plan set a 70% open-source spending target. The city developed and open-sourced Decidim (AGPL-3.0), engaged 70,000+ residents in participatory budgeting, migrated its website to Drupal, and deployed Nextcloud city-wide [54].

**Schleswig-Holstein:** Migration of 25,000 workstations to LibreOffice, Nextcloud, and Thunderbird, phased 2023–2026 with parallel operation — the reference for federated open-source government in Germany [47].

**Helsinki:** 1,200+ open datasets under CC-BY-4.0 [56]; Decidim deployment; open-source-first procurement policy; strong civil-society partnership model.

**Swiss Federal Administration:** ~40,000 civil servants on Nextcloud, integrated with Swiss eID and GEVER workflows — demonstrating enterprise-scale open-source viability [13].

### 3.9 Gaps in the Literature

1. **TCO comparison studies** — most are vendor-commissioned and methodologically inconsistent.
2. **Longitudinal data** from completed open-source municipal transitions is sparse.
3. **Small-municipality perspectives** are underrepresented; most studies focus on large cities.
4. **User experience research** comparing citizen satisfaction across licence models is near-absent.
5. **Economic modelling** of shared open-source investment across municipal networks is underdeveloped.

See `Mem/literature-review-state.md` for the full gap analysis and improvement roadmap.

---

## 4. Technology Stack Analysis

A municipal technology stack decomposes into fourteen components across seven layers.

### 4.1 Digital Identity and Authentication

**Recommended: Keycloak** (Red Hat / CNCF) [21]

De facto open-source IAM for public administration. Implements OpenID Connect, OAuth 2.0, SAML 2.0, FIDO2/WebAuthn. Federates with BundID (Germany) and Swiss eID.

| Criterion | Score | Notes |
|---|---|---|
| Licence openness | 5 | Apache 2.0 |
| Deployment maturity | 5 | 10+ years production |
| Community health | 5 | CNCF-supported |
| Interoperability | 5 | OIDC, OAuth2, SAML2, FIDO2 |
| Security posture | 5 | Widely audited |
| TCO | 4 | No licence cost; ops expertise required |
| Public-sector deployments | 5 | EU institutions, German Länder, Swiss cantons |
| **Composite** | **34/35** | |

### 4.2 Document Management and Records

**Recommended: Nextcloud** (file management) + **Alfresco Community** (records management) [13]

Alfresco Community Edition provides ISO 15489-compliant records management (lifecycle, retention, disposition). For Swiss GEVER compliance: CMI GEVER or Fabasoft integrated with Nextcloud frontend.

| Criterion | Score | Notes |
|---|---|---|
| Licence openness | 5 | AGPL-3.0 (Nextcloud); LGPL-3.0 (Alfresco) |
| Deployment maturity | 5 | 400,000+ organisations |
| Community health | 5 | Nextcloud GmbH + community |
| Interoperability | 4 | WebDAV, CalDAV, CMIS |
| Security posture | 5 | ISO 27001 certified offering |
| TCO | 5 | No per-seat licence |
| Public-sector deployments | 5 | Swiss federal, German states, EU |
| **Composite** | **34/35** | |

### 4.3 Workflow Automation and BPM

**Recommended: Camunda Platform 8 Community** or **Flowable** [33]

Camunda provides a BPMN 2.0-native workflow engine with XÖV/eCH data standards integration. Flowable (Apache 2.0, no dual-licence) is the clean-OSI alternative for simpler workflows.

| Criterion | Score | Notes |
|---|---|---|
| Licence openness | 4 | Community: Apache 2.0; Enterprise: proprietary |
| Deployment maturity | 5 | Production-proven |
| Community health | 4 | Active |
| Interoperability | 5 | BPMN 2.0, REST API |
| Security posture | 4 | Actively maintained |
| TCO | 3 | Community free; scale may trigger Enterprise |
| Public-sector deployments | 4 | Multiple German Länder |
| **Composite** | **29/35** | |

### 4.4 Citizen Participation

**Recommended: Decidim** [12]

400+ deployments globally across regulatory and linguistic contexts. Decidim Association provides governance and a published social contract.

| Criterion | Score | Notes |
|---|---|---|
| Licence openness | 5 | AGPL-3.0 |
| Deployment maturity | 5 | 400+ deployments |
| Community health | 5 | Active association |
| Interoperability | 4 | REST API, webhooks |
| Security posture | 4 | Actively maintained |
| TCO | 5 | No licence cost |
| Public-sector deployments | 5 | Cities, cantons, federal agencies |
| **Composite** | **33/35** | |

**Alternative:** CONSUL Democracy [53] — stronger for direct democracy mechanisms.

### 4.5 Communication and Collaboration

| Component | Licence | Composite | Key advantage |
|---|---|---|---|
| Matrix/Element | Apache 2.0 | 32/35 | E2E encryption, federation |
| Jitsi Meet | Apache 2.0 | 31/35 | Browser-based, self-hostable |
| BigBlueButton | LGPL-3.0 | 30/35 | Council meeting focus |
| Nextcloud Talk | AGPL-3.0 | 31/35 | Integrated with file management |

The German BundesMessenger (Matrix) is the reference deployment for municipal contexts [14].

### 4.6 Open Data Publication

**Recommended: CKAN** [22]

Powers opendata.swiss, data.gov, data.gov.uk. Plugin architecture supports DCAT-AP, DCAT-AP.de, and OGD Switzerland metadata standards.

| Criterion | Score | Notes |
|---|---|---|
| Licence openness | 5 | AGPL-3.0 |
| Deployment maturity | 5 | 10+ year track record |
| Community health | 4 | CKAN Association |
| Interoperability | 5 | DCAT-AP, OAI-PMH, SPARQL |
| Security posture | 4 | Actively maintained |
| TCO | 4 | No licence; ops overhead |
| Public-sector deployments | 5 | Switzerland, Germany, EU |
| **Composite** | **32/35** | |

### 4.7 Geographic Information Systems

- **QGIS** (GPL-2.0+) — spatial data editing and analysis [37]
- **GeoServer** (GPL-2.0) — OGC-compliant publication (WMS, WFS, WCS)
- **OpenStreetMap** (ODbL-1.0) — base cartographic layer [36]

Switzerland's swisstopo and Germany's BKG provide open, high-quality governmental base map data.

### 4.8 Public Website and CMS

- **TYPO3** — dominant in Swiss and German public administration; TYPO3 Association provides LTS and public-sector extensions [19]
- **Drupal** — strong international track record; used by the European Commission

Both support WCAG 2.1 AA / BITV 2.0, multilingualism, and open data catalogue integration.

### 4.9 Cloud Infrastructure

**Recommended: Sovereign Cloud Stack (SCS)** [3, 11]

Fully open-source cloud (OpenStack + Kubernetes + Ceph). Certified SCS hosters: plusserver, OSISM, REGIO iT. govdigital eG operates SCS-based shared cloud for German public sector [23].

| Criterion | Score | Notes |
|---|---|---|
| Licence openness | 5 | Apache 2.0 / fully open |
| Deployment maturity | 4 | Production in multiple Länder |
| Community health | 5 | OSBA-backed |
| Interoperability | 5 | Open APIs, OCI-compliant |
| Security posture | 5 | BSI IT-Grundschutz compatible |
| TCO | 4 | No licence; infrastructure cost |
| Public-sector deployments | 4 | German Länder, growing |
| **Composite** | **32/35** | |

### 4.10 Office Productivity Suite

**Recommended: LibreOffice** + **Collabora Online** [47]

LibreOffice implements ODF (ISO/IEC 26300) as the native format. Collabora Online provides browser-based editing integrated with Nextcloud. Schleswig-Holstein's 25,000-workstation migration is the reference deployment [47].

| Criterion | Score | Notes |
|---|---|---|
| Licence openness | 5 | MPL-2.0 |
| Deployment maturity | 5 | 200M+ users |
| Community health | 5 | The Document Foundation + Collabora |
| Interoperability | 5 | ODF native; OOXML compatible |
| Security posture | 4 | Active maintenance |
| TCO | 5 | No licence cost |
| Public-sector deployments | 5 | Schleswig-Holstein, Barcelona, Swiss |
| **Composite** | **34/35** | |

### 4.11 Web Analytics

**Recommended: Matomo**

Self-hosted, GDPR-compliant analytics. The German DSK (Datenschutzkonferenz) ruled Google Analytics impermissible for German public authorities without valid consent; Matomo is the approved replacement [57].

| Criterion | Score | Notes |
|---|---|---|
| Licence openness | 5 | GPL-3.0 |
| Deployment maturity | 5 | 1M+ sites |
| Community health | 4 | Matomo company + community |
| Interoperability | 4 | GA-compatible API |
| Security posture | 4 | Actively maintained |
| TCO | 5 | No licence (self-hosted) |
| Public-sector deployments | 5 | Standard for EU public sector |
| **Composite** | **32/35** | |

### 4.12 DevOps and Code Hosting

**Recommended: Forgejo** + **Woodpecker CI** (or **GitLab Community Edition**)

Forgejo (MIT) provides self-hosted Git. Woodpecker CI (Apache 2.0) provides lightweight CI/CD. GitLab CE (MIT) is the primary alternative and powers openCode.de [10].

| Criterion | Score | Notes |
|---|---|---|
| Licence openness | 5 | MIT (Forgejo); Apache 2.0 (Woodpecker) |
| Deployment maturity | 4 | Production-ready |
| Community health | 4 | Growing, FOSS-committed governance |
| Interoperability | 4 | Git standard; GitHub-compatible API |
| Security posture | 4 | Actively maintained |
| TCO | 5 | No licence; low ops overhead |
| Public-sector deployments | 3 | Growing |
| **Composite** | **29/35** | |

### 4.13 Municipal ERP

Municipal ERP (SAP-dominated in Germany and Switzerland) carries the highest switching costs. **Recommendation:** Maintain existing ERP through Phase 1–3; implement open APIs and XÖV/eCH interfaces. Plan open-source ERP (ERPNext Community, Odoo Community) as a Phase 4+ initiative, decoupled from the faster-moving stack transitions.

### 4.14 Reference Architecture

```
+-------------------------------------------------------------+
|                    CITIZEN TOUCHPOINTS                       |
|        TYPO3/Drupal · Decidim · CKAN · Nextcloud           |
+-------------------------------------------------------------+
|                      SERVICE LAYER                          |
|   Camunda Workflows · XÖV/eCH Forms · GeoServer · QGIS    |
+-------------------------------------------------------------+
|                   COLLABORATION LAYER                       |
|  Nextcloud · Matrix/Element · Jitsi · OpenProject · Email  |
+-------------------------------------------------------------+
|                   PRODUCTIVITY LAYER                        |
|         LibreOffice · Collabora Online · Matomo            |
+-------------------------------------------------------------+
|                     IDENTITY LAYER                          |
|           Keycloak ↔ BundID / Swiss eID                    |
+-------------------------------------------------------------+
|                  DEVOPS & CODE LAYER                        |
|           Forgejo · Woodpecker CI · GitLab CE              |
+-------------------------------------------------------------+
|                  INFRASTRUCTURE LAYER                       |
|  Sovereign Cloud Stack · Kubernetes · PostgreSQL · Ceph    |
+-------------------------------------------------------------+
```

All layers communicate via open APIs. Data exchange uses XÖV [46] (Germany) or eCH [51] (Switzerland). Security governed by BSI IT-Grundschutz [26] or Swiss ISDS. Analytics via Matomo without third-party data transfer.

---

## 5. Implementation Roadmap

A 36-month, five-phase programme. Three city-size reference categories:

- **Small:** 5,000–50,000 population; IT staff 1–5  
- **Medium:** 50,000–250,000 population; IT staff 5–30  
- **Large:** 250,000–500,000 population; IT staff 30–100+  

### Phase 0: Foundation (Months 1–3)

**Objective:** Establish governance, assess current state, build the coalition.

**Deliverables:**
- [ ] Digital Transformation Steering Committee established
- [ ] Technology inventory completed (all software, licences, contracts, expiry dates)
- [ ] Cost baseline established (annual IT spend by category)
- [ ] Stakeholder engagement plan adopted
- [ ] Legal review: procurement framework, licence compatibility
- [ ] MoU with cooperative IT provider (Dataport, AKDB, govdigital eG, or equivalent)
- [ ] Data Protection Impact Assessment (DPIA) commissioned

**Success criteria:** Political mandate secured; budget approved; project lead appointed.

**Budget guidance:**
| Size | Indicative budget |
|---|---|
| Small | €20,000–€50,000 |
| Medium | €50,000–€150,000 |
| Large | €150,000–€400,000 |

**Phase gate:** Do not proceed without (a) formal political mandate; (b) approved Phase 1–3 budget; (c) data protection clearance.

### Phase 1: Identity and Infrastructure (Months 4–12)

**Objective:** Stand up the foundational layers everything else depends on.

**Deliverables:**
- [ ] Sovereign Cloud Stack environment operational (own or SCS-certified hosted)
- [ ] Keycloak deployed and federated with national identity system
- [ ] Nextcloud baseline for internal collaboration
- [ ] Matrix/Element messaging for all IT staff
- [ ] Matomo deployed; Google Analytics removed from all municipal sites
- [ ] LibreOffice deployed to 20% of staff (IT team + pilot department)
- [ ] BSI IT-Grundschutz / Swiss ISDS baseline documentation complete
- [ ] Forgejo or GitLab CE for internal code management

**Success criteria:** All IT staff authenticate via Keycloak SSO; file storage on Nextcloud; security baseline approved by DPO.

**Budget guidance:**
| Size | Indicative budget |
|---|---|
| Small | €40,000–€100,000 |
| Medium | €100,000–€300,000 |
| Large | €300,000–€800,000 |

**Phase gate:** Keycloak in production; Nextcloud security review passed; data residency verified.

### Phase 2: Services and Workflows (Months 10–18)

**Objective:** Deploy first five citizen-facing services on open infrastructure.

**Deliverables:**
- [ ] TYPO3 or Drupal CMS deployed; municipal website migrated
- [ ] Five highest-volume administrative services on Camunda/XÖV stack
- [ ] CKAN open data portal with first 20 datasets
- [ ] Decidim instance deployed for first participatory process
- [ ] GIS layer operational (QGIS + GeoServer)
- [ ] LibreOffice to 60% of staff
- [ ] First open-source contribution published on openCode.de

**Success criteria:** 80% of target service volume processed through new system; first open data publication harvestable by opendata.swiss or GovData.

**Budget guidance:**
| Size | Indicative budget |
|---|---|
| Small | €60,000–€150,000 |
| Medium | €150,000–€400,000 |
| Large | €400,000–€1,000,000 |

### Phase 3: Integration and Extension (Months 16–24)

**Objective:** Integrate all layers; extend to 80% of transactions; LibreOffice to 100%.

**Deliverables:**
- [ ] All services federated via Keycloak SSO
- [ ] Nextcloud integrated with document management workflows
- [ ] 80% of administrative services digitised
- [ ] Inter-agency data exchange via XÖV/eCH operational
- [ ] LibreOffice to 100% of staff; Microsoft Office contracts not renewed
- [ ] Annual TCO report published as open data
- [ ] Accessibility audit (WCAG 2.1 AA) across all citizen-facing services

**Success criteria:** Paper-free for 80% of transaction types; first annual open data report published.

### Phase 4: Optimisation and Community (Months 22–30)

**Deliverables:**
- [ ] Citizen satisfaction survey (target: NPS ≥ 40)
- [ ] ≥ 3 improvements contributed upstream
- [ ] Municipal open-source community of practice with ≥ 3 peer municipalities
- [ ] Performance benchmarks published on openCode.de

### Phase 5: Sovereignty and Scale (Months 28–36)

**Deliverables:**
- [ ] Full licence compliance audit
- [ ] Sovereign data residency verified by external auditor
- [ ] Zero single-vendor critical dependencies confirmed
- [ ] Replication playbook published as open-source document
- [ ] Strategy paper v1.0 published

### 5.1 KPI Framework

| Dimension | KPI | Target (36 months) |
|---|---|---|
| Digital sovereignty | % IT spend on open-source | ≥ 70% |
| Digital sovereignty | Critical single-vendor dependencies | 0 |
| Service quality | % services available online | ≥ 90% |
| Service quality | Citizen NPS | ≥ 40 |
| Cost | Annual IT licence cost per civil servant | Reduction ≥ 40% |
| Cost | 5-year TCO vs. proprietary baseline | Savings ≥ 20% |
| Transparency | Open datasets published | ≥ 50 |
| Participation | Citizens engaged via Decidim per year | ≥ 5% of population |
| Community | Open-source contributions published | ≥ 5 per year |
| Security | Time to patch critical CVEs | ≤ 48 hours |
| Accessibility | WCAG 2.1 AA compliance | 100% citizen-facing |

---

## 6. Stakeholder and Procurement Strategy

### 6.1 Stakeholder Map (Power–Interest Grid)

| Stakeholder | Power | Interest | Engagement |
|---|---|---|---|
| Mayor / Executive | High | High | Sponsor role; progress dashboard |
| City council | High | Medium | Quarterly reports; oversight committee |
| City IT team | Medium | High | Co-design; training; community membership |
| Procurement office | Medium | Medium | Legal briefings; framework agreements |
| Civil servants (end users) | Low–Med | High | UX testing; change management; training |
| Citizens | Low | High | Participatory design; transparency reporting |
| Civil society / NGOs | Low | High | Public roadmaps; Decidim |
| Open-source communities | Low | High | openCode.de; upstream contributions |
| Sovereign technology providers | Medium | High | Certified partner agreements |
| Data protection officer | Medium | High | Privacy-by-design review at each phase |
| Vendor incumbents | High | High (opposed) | Data portability demands; contract terms |

### 6.2 Procurement Framework

**Principle 1: Procure services, not licences.** Municipalities pay for implementation, hosting, support, customisation, and training — not software access.

**Principle 2: Use cooperative procurement.** Germany's govdigital eG and Swiss cantonal IT cooperatives provide framework agreements satisfying public procurement law (GWB/VgV in Germany; BöB in Switzerland) [23].

**Principle 3: "Public Money? Public Code!"** All custom software developed under contract must be released under an OSI-approved licence on openCode.de [4].

**Principle 4: Evaluate 5-year TCO.** Include:

| Cost category | Proprietary | Open-source |
|---|---|---|
| Software licences | Annual recurring | €0 (community) |
| Implementation | One-time | One-time |
| Hosting / cloud | Annual | Annual |
| Training | One-time + annual | One-time + annual |
| Support | Annual subscription | Community + commercial |
| Customisation | Vendor-only | Open market |
| Exit / migration | High (lock-in) | Low (open formats) |
| Lock-in risk (5% p.a.) | Significant | Negligible |

**Principle 5: Require interoperability standards.** XÖV [46] (Germany), eCH [51] (Switzerland), DCAT-AP (EU open data). Non-compliance: disqualifying criterion.

**Principle 6: Prefer certified cooperative providers.** SCS-certified operators or govdigital eG members [23].

### 6.3 RFP Minimum Requirements

```
1. LICENCE: All components under OSI-approved open-source licence.

2. SOURCE CODE: Custom development published on openCode.de under
   OSI licence within 30 days of acceptance testing.

3. DATA PORTABILITY: All data exportable in non-proprietary formats
   (ODF, CSV, JSON, XML, DCAT-AP) within 24 hours of request.

4. API: Documented REST or GraphQL API. No proprietary integration formats.

5. AUTHENTICATION: Keycloak/OIDC integration. No proprietary identity silos.

6. SECURITY: BSI IT-Grundschutz (DE) / ISDS (CH) documentation.
   Penetration test report required at acceptance.

7. ACCESSIBILITY: WCAG 2.1 AA (BITV 2.0 in Germany).
   Accessibility statement required.

8. DATA RESIDENCY: All data in EU/EEA on infrastructure not subject
   to non-EU data access laws.

9. INTEROPERABILITY: XÖV (Germany) / eCH (Switzerland) for all
   data exchange interfaces.

10. EXIT PLAN: Documented, executable exit plan enabling full data
    migration within 90 days at no additional cost.
```

### 6.4 Change Management

- **Executive sponsorship:** Mayor or City Manager as named sponsor. Without senior political cover, vendor lobbying will succeed.
- **Digital Transformation Champions:** One per department, trained by IT team, responsible for peer support.
- **Parallel operation:** Minimum 3 months for productivity tools; 6 months for citizen-facing services.
- **Training investment:** 4 hours per civil servant for LibreOffice; 8 hours for Nextcloud; 16 hours for service-specific tools.
- **Transparency:** Public progress dashboard from day one. Document and celebrate every win.

---

## 7. Risk Analysis

### 7.1 Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Political reversal after election | Medium | High | Embed in ordinance; cross-party consensus |
| Vendor lobbying / FUD campaigns | High | Medium | TCO evidence; civil-society engagement |
| Skill gap in IT team | High | Medium | Training; cooperative IT provider |
| Integration failure between layers | Medium | High | Phased rollout; reference architecture |
| Data loss during migration | Low | Critical | Full backup; parallel operation; tested rollback |
| GDPR / DSGVO violation | Low | High | Privacy-by-design; DPIA; data mapping |
| User adoption failure | Medium | High | Change management; UX testing; champions |
| Security incident | Low | Critical | IT-Grundschutz; penetration testing; SBOM |
| Community fragmentation | Low | Medium | Contribute upstream; openCode.de |
| Cost overrun | Medium | Medium | Phase-gated budget; open TCO accounting |
| Vendor exit failure | Low | High | Data portability clause; tested export |

### 7.2 The Munich Cautionary Case

Munich's LiMux project (2003–2017) was reversed due to: (a) change in political leadership with closer ties to Microsoft; (b) inadequate change management and user training; (c) compatibility issues with state-level systems not updated for open standards [30]. The technical implementation was broadly successful — 14 years of operation. The lesson: political risk management is as important as technical planning.

### 7.3 GDPR and DSGVO Compliance

All recommended components are GDPR-compliant by default in self-hosted configuration. Key risks:

1. **Telemetry in software:** Disable optional telemetry (e.g., LibreOffice crash reports) by default.
2. **External CDN dependencies:** Self-host all fonts and JavaScript assets.
3. **Analytics:** Google Analytics is impermissible for German public authorities (DSK ruling); use Matomo [57].
4. **Data processor agreements:** Required (DSGVO Art. 28) even for open-source hosted by a third party.
5. **Swiss nFADP:** Revised Swiss data protection law (September 2023) aligns with GDPR; self-hosted stack is compliant by default.

### 7.4 Cybersecurity Maturity Model

| Control domain | Minimum requirement | Recommended |
|---|---|---|
| Authentication | Keycloak with MFA | FIDO2/WebAuthn for privileged access |
| Patch management | Critical CVEs: ≤ 48h | Automated patch pipeline; SBOM |
| Network | TLS 1.3 everywhere | mTLS for internal service mesh |
| Data at rest | AES-256 for sensitive data | Full disk encryption on persistent volumes |
| Backup | 3-2-1 rule; tested restore | Immutable backup to separate SCS tenant |
| Incident response | NIS2-compliant; 24h notification | CSIRT membership |
| Penetration testing | Annual; at each phase gate | Continuous automated DAST |
| SBOM | Maintain for all OSS deps | Automated generation in CI pipeline |
| Audit logging | Admin actions logged; 90-day retention | SIEM; 1-year retention |

### 7.5 Vendor Exit Strategy

For each proprietary component being replaced:
1. Verify and test data export to open formats *before* deployment.
2. Negotiate a 90-day data export window in all proprietary contracts.
3. Document all proprietary configuration before transition.
4. Maintain read-only access to legacy systems for 6 months post-migration.

For open-source components: source code is available, data formats are open, multiple support providers exist — exit risk is structurally lower.

---

## 8. Conclusion

The evidence converges on five findings:

**1. Open-source municipal stacks are technically mature.** Every functional requirement can be met by open-source software with documented deployments at peer municipalities, federal administrations, and EU institutions.

**2. The regulatory environment mandates open-source and interoperability.** EMBAG, OZG 2.0, the Interoperable Europe Act, the Data Governance Act, and the Data Act create a landscape in which proprietary systems accumulate legal and compliance debt. Open-source is structurally advantaged.

**3. The economic case is compelling.** Open-source eliminates per-seat licence costs (typically €100–300 per user per year for productivity software). Cooperative procurement spreads implementation costs. 5-year TCO systematically favours open-source when vendor lock-in risk is properly valued.

**4. Case studies demonstrate success at all scales.** Barcelona (1.6M), Helsinki (650K), Swiss cantons (10K–500K), and Schleswig-Holstein (25K workstations) show that political mandate + technical competence + sustained stakeholder engagement = success.

**5. Political and organisational investment is the binding constraint.** The technology is ready. The question is governance.

### 8.1 Recommendations by Stakeholder

**City administrators:** Commission a technology audit and TCO baseline before the next major procurement cycle. Join govdigital eG or your jurisdiction's cooperative structure. Appoint a Digital Transformation Champion.

**Elected officials:** Pass a resolution establishing open-source-first as a procurement principle. Embed digital sovereignty in the municipal development plan. Create a public transparency dashboard.

**IT teams:** Begin with Keycloak and Nextcloud — lowest risk, highest impact. Join the SCS community and openCode.de.

**Procurement offices:** Update tender templates with the minimum requirements in Section 6.3. Require 5-year TCO models. Make data portability a non-negotiable contract term.

**Civil-society organisations:** Advocate for public progress dashboards. Use Decidim. Hold governments accountable.

**Open-source communities:** Engage municipal IT teams through openCode.de. Provide implementation support. Contribute public-sector features upstream.

### 8.2 Next Steps

Three immediate actions, all initiable simultaneously without new budget beyond Phase 0 allocation: (1) pass a council resolution; (2) begin Keycloak and Nextcloud deployment; (3) join govdigital eG or equivalent. The open-source commons is ready. The invitation is standing.

---

## 9. Glossary

| Term | Definition |
|---|---|
| **AGPL-3.0** | GNU Affero GPL v3 — open-source licence requiring source disclosure for network-deployed software |
| **BöB** | Bundesgesetz über das öffentliche Beschaffungswesen — Swiss federal public procurement law |
| **BSI IT-Grundschutz** | German federal cybersecurity baseline, mandatory reference for public-sector IT |
| **BundID** | German federal citizen identity account, "once only" authentication layer for OZG services |
| **BPMN 2.0** | Business Process Model and Notation — international standard for workflow automation |
| **CKAN** | Comprehensive Knowledge Archive Network — open-source open data portal platform |
| **DCAT-AP** | Data Catalogue Vocabulary Application Profile — EU metadata standard for open data |
| **DPIA** | Data Protection Impact Assessment — required by GDPR Art. 35 for high-risk processing |
| **eCH** | Swiss e-government standards organisation and its family of administrative data standards |
| **EfA** | Einer für Alle — German federal shared digital service development approach |
| **EMBAG** | Swiss law mandating open-source release of publicly funded federal software |
| **FITKO** | Föderale IT-Kooperation — German federal–Land IT coordination body for OZG |
| **GEVER** | Geschäftsverwaltung — Swiss federal records and process management standard |
| **GovStack** | ITU/DIAL framework for digital government via interoperable building blocks |
| **GWB/VgV** | German public procurement law |
| **IAM** | Identity and Access Management |
| **ISDS** | Swiss Information Security for the Confederation |
| **KoSIT** | Koordinierungsstelle für IT-Standards — German XÖV standards body |
| **NIS2** | EU Directive on network and information security (2022) |
| **ODF** | Open Document Format — ISO/IEC 26300 open office document standard |
| **OIDC** | OpenID Connect — open authentication protocol built on OAuth 2.0 |
| **OSI** | Open Source Initiative — defines the Open Source Definition |
| **OZG** | Onlinezugangsgesetz — German Online Access Act |
| **SAML 2.0** | Security Assertion Markup Language — federated identity protocol |
| **SBOM** | Software Bill of Materials — inventory of software components and licences |
| **SCS** | Sovereign Cloud Stack — fully open-source European government cloud |
| **SSO** | Single Sign-On |
| **TCO** | Total Cost of Ownership |
| **WCAG 2.1** | Web Content Accessibility Guidelines (AA level required for EU public sector) |
| **XÖV** | XML in der öffentlichen Verwaltung — German XML standards for administrative data exchange |
| **ZenDiS** | Zentrum für Digitale Souveränität der öffentlichen Verwaltung |

---

## 10. References

[1] Swiss Federal Council. (2023). *Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG)*. SR 172.019. https://www.fedlex.admin.ch/eli/cc/2023/682/de — [CC0]

[2] Bundesministerium des Innern und für Heimat (BMI). (2024). *Onlinezugangsgesetz 2.0*. https://www.bmi.bund.de/ — [DL-DE/Zero 2.0]

[3] Open Source Business Alliance (OSBA). (2023). *Sovereign Cloud Stack*. https://scs.community/ — [CC-BY-SA-4.0]

[4] Free Software Foundation Europe (FSFE). (2017). *Public Money? Public Code!* https://publiccode.eu/ — [CC-BY-SA-4.0]

[5] European Commission. (2020). *Open Source Software Strategy 2020–2023: Think Open*. https://commission.europa.eu/ — [Open access]

[6] European Parliament and Council. (2024). *Regulation (EU) 2024/903 — Interoperable Europe Act*. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202400903 — [Open access]

[7] Wirtz, B. W., & Weyerer, J. C. (2017). Public Management Review, 19(9), 1297–1316. https://doi.org/10.1080/14719037.2017.1283024

[8] Janssen, M., Charalabidis, Y., & Zuiderwijk, A. (2012). Information Systems Management, 29(4), 258–268. https://doi.org/10.1080/10580530.2012.716740

[9] FITKO. (2023). *Jahresbericht 2023*. https://www.fitko.de/ — [Open access]

[10] openCode.de. (2022). https://opencode.de/ — [Open access]

[11] Sovereign Cloud Stack Community. (2023). *SCS Technical Documentation*. https://docs.scs.community/ — [Apache 2.0]

[12] Decidim Association. (2021). https://decidim.org/ — [AGPL-3.0]

[13] Nextcloud GmbH. (2023). *Nextcloud for Government*. https://nextcloud.com/government/ — [Open access]

[14] The Matrix Foundation. (2023). *Matrix Specification*. https://spec.matrix.org/ — [Apache 2.0]

[16] E-Government Suisse. (2023). *Strategie E-Government Schweiz 2024–2027*. https://www.egovernment.ch/ — [Open access]

[19] TYPO3 Association. (2023). https://typo3.org/ — [Open access]

[20] OpenProject GmbH. (2023). https://www.openproject.org/ — [GPLv3]

[21] Keycloak Community. (2023). https://www.keycloak.org/ — [Apache 2.0]

[22] CKAN Association. (2023). https://ckan.org/ — [AGPL-3.0]

[23] govdigital eG. (2023). https://govdigital.de/ — [Open access]

[24] Dataport AöR. (2023). https://www.dataport.de/ — [Open access]

[26] BSI. (2023). *IT-Grundschutz-Kompendium*. https://www.bsi.bund.de/ — [CC-BY-ND 3.0 DE]

[27] European Parliament and Council. (2022). *Directive (EU) 2022/2555 — NIS2*. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022L2555 — [Open access]

[29] United Nations DESA. (2022). *UN E-Government Survey 2022*. https://publicadministration.un.org/ — [Open access]

[30] Janowski, T. (2015). Government Information Quarterly, 32(3), 221–226. https://doi.org/10.1016/j.giq.2015.07.001

[33] Camunda. (2023). *Camunda Platform 8 Community*. https://camunda.com/ — [Apache 2.0]

[34] BigBlueButton Inc. (2023). https://bigbluebutton.org/ — [LGPL-3.0]

[35] Jitsi. (2023). https://jitsi.org/ — [Apache 2.0]

[36] OpenStreetMap Foundation. (2023). https://www.openstreetmap.org/ — [ODbL-1.0]

[37] QGIS Project. (2023). https://www.qgis.org/ — [GPL-2.0+]

[39] CNCF. (2023). *Kubernetes*. https://kubernetes.io/ — [Apache 2.0]

[41] PostgreSQL Global Development Group. (2023). https://www.postgresql.org/ — [PostgreSQL Licence]

[42] BMI / ZenDiS GmbH. (2023). *OpenDesk*. https://opendesk.eu/ — [AGPL-3.0]

[43] Swiss Federal Archives (BAR). (2023). *GEVER*. https://www.bar.admin.ch/ — [Open access]

[44] opendata.swiss. (2023). https://opendata.swiss/ — [CC-BY-4.0]

[45] European Commission. (2017). *European Interoperability Framework (EIF)*. https://joinup.ec.europa.eu/ — [CC-BY-4.0]

[46] KoSIT. (2023). *XÖV-Standards*. https://www.xoev.de/ — [Open access]

[47] Land Schleswig-Holstein. (2021). *Schleswig-Holstein setzt auf Open-Source-Software*. https://www.schleswig-holstein.de/ — [Open access]

[48] European Parliament and Council. (2022). *Regulation (EU) 2022/868 — Data Governance Act*. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R0868 — [Open access]

[49] ZenDiS GmbH. (2023). *Jahresbericht 2023*. https://zendis.de/ — [Open access]

[50] ITU / DIAL. (2022). *GovStack*. https://www.govstack.global/ — [CC-BY-SA-4.0]

[51] eCH. (2023). *eCH-Standards*. https://www.ech.ch/ — [Open access]

[52] Swiss Federal Council. (2023). *E-ID-Gesetz*. https://www.fedlex.admin.ch/ — [CC0]

[53] Ayuntamiento de Madrid. (2017). *CONSUL Democracy*. https://consuldemocracy.org/ — [AGPL-3.0]

[54] Ajuntament de Barcelona. (2017). *Barcelona Digital City*. https://ajuntament.barcelona.cat/digital/ — [Open access]

[55] European Parliament and Council. (2023). *Regulation (EU) 2023/2854 — Data Act*. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023R2854 — [Open access]

[56] City of Helsinki. (2023). *Helsinki Open Data*. https://hri.fi/ — [CC-BY-4.0]

[57] Datenschutzkonferenz (DSK). (2022). *Orientierungshilfe Telemedien*. https://www.datenschutzkonferenz-online.de/ — [Open access]

---

## Appendix A: Regulatory Reference Table

| Regulation | Jurisdiction | Key obligation | In force |
|---|---|---|---|
| EMBAG | Switzerland (federal) | Open-source release of publicly funded software | 2024-01-01 |
| E-ID-Gesetz | Switzerland (federal) | State-issued digital identity | 2026 (expected) |
| OZG 2.0 | Germany (federal) | All administrative services online | 2024 |
| Interoperable Europe Act | EU | Cross-border interoperability for public admin | 2024-05-01 |
| Data Governance Act | EU | Non-exclusive data sharing from public bodies | 2023-09-24 |
| Data Act | EU | Data portability; cloud switching rights | 2025-09-12 |
| NIS2 Directive | EU | Cybersecurity for essential services | 2022-12-27 |
| GDPR / DSGVO | EU | Data protection | 2018-05-25 |
| nFADP / rev. DSG | Switzerland | Swiss data protection aligned with GDPR | 2023-09-01 |
| BITV 2.0 | Germany | Web accessibility for public-sector websites | 2019 |
| EU Web Accessibility Directive | EU | WCAG 2.1 AA for public-sector sites | 2018 |

## Appendix B: Recommended Resources

**Policy and legislation:** https://www.fedlex.admin.ch/ · https://www.bmi.bund.de/ · https://joinup.ec.europa.eu/ · https://publiccode.eu/

**Technical communities:** https://scs.community/ · https://opencode.de/ · https://decidim.org/ · https://www.govstack.global/

**Frameworks and standards:** https://www.bsi.bund.de/grundschutz · https://www.ech.ch/ · https://www.xoev.de/ · https://joinup.ec.europa.eu/eif

**Research:** https://publicadministration.un.org/ · https://joinup.ec.europa.eu/interoperable-europe · https://oecd-opsi.org/

---

*Released under CC-BY-4.0. Attribute as: Sebastian Graf, Autonomous Office of Civil Digital Infrastructure (sebk4c@tuta.com)*  
*Published: https://github.com/SEBK4C/Strategy-for-City-GovTech*
