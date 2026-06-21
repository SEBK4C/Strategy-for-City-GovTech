---
title: "Sovereign by Design: A State-of-the-Art Open-Source Technology Strategy for Municipal Governments"
author: "Sebastian Graf, Autonomous Office of Civil Digital Infrastructure"
correspondence: "sebk4c@tuta.com"
version: "0.1.0"
status: "First Structured Draft"
date: "2026-06-20"
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
---

# Sovereign by Design: A State-of-the-Art Open-Source Technology Strategy for Municipal Governments

**Author:** Sebastian Graf, Autonomous Office of Civil Digital Infrastructure
**Correspondence:** sebk4c@tuta.com
**Version:** 0.1.0 — First Structured Draft
**Date:** 2026-06-20
**Languages:** English (source of truth) · Deutsch
**SPDX-License-Identifier:** CC-BY-4.0

---

## Abstract

Municipal governments are the closest layer of democratic administration to citizens, yet they face an acute structural tension: the digital tools they depend on are increasingly proprietary, vendor-locked, and misaligned with public-interest values. This paper presents a comprehensive strategy for implementing a state-of-the-art, open-source governmental administration technology stack in city governments. Drawing on exemplary practices from the Swiss federal administration’s EMBAG legislation, Germany’s OZG reform programme and Sovereign Cloud Stack initiative, and the wider European sovereign technology community, we derive a first-principles implementation roadmap, stakeholder engagement framework, and procurement strategy. We evaluate the core technology components — identity management, document management, workflow automation, citizen participation, secure communications, open data publication, and cloud infrastructure — against criteria of digital sovereignty, interoperability, total cost of ownership, and civic alignment. We conclude that open-source municipal technology stacks are not merely technically viable but fiscally superior, democratically necessary, and legally mandated in an increasing number of jurisdictions. The paper provides a phased 36-month implementation roadmap with concrete procurement guidance for city administrators, elected officials, IT teams, and civil-society stakeholders.

**Keywords:** digital sovereignty, open source government, GovTech, municipal digital transformation, interoperability, OZG, EMBAG, Sovereign Cloud Stack, e-government, civic technology

---

## 1. Introduction

The digital transformation of municipal government is no longer optional. Citizens expect seamless, secure, and accessible digital services; regulators demand interoperability and data protection; and fiscal pressures require sustainable, cost-effective technology investments. Yet the majority of city governments worldwide remain trapped in a cycle of proprietary vendor dependency, expensive licence agreements, and fragmented systems that impede rather than enable good governance [1, 29].

The consequences of this dependency are well-documented: vendor lock-in raises switching costs and bargaining asymmetry [4]; proprietary formats obstruct cross-agency data exchange and transparency [45]; closed-source infrastructure prevents independent security auditing [26]; and recurring licence fees drain budgets that could otherwise fund service delivery [3, 5]. Most fundamentally, when the software running democratic institutions is owned and controlled by private actors, a structural conflict of interest emerges between the public interest and corporate imperatives [4].

A different path is both possible and proven. Switzerland’s 2023 EMBAG legislation (Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben) mandates that federal software developed with public funds be released as open source by default [1]. Germany’s OZG reform programme, Sovereign Cloud Stack, and OpenDesk initiative represent the most ambitious open-source government technology programme in Europe [2, 3, 42]. The Free Software Foundation Europe’s “Public Money? Public Code!” campaign, now endorsed by over 200 organisations across 30 countries, articulates the democratic principle at stake: software paid for by the public should be available to the public [4].

This paper synthesises these developments into a practical strategy for municipal governments. It is addressed to all relevant stakeholders — city administrators, elected officials, public-sector IT teams, procurement offices, civil-society groups, open-source communities, and sovereign technology providers — and provides the evidence base, technology assessment, and implementation roadmap needed to make the transition.

### 1.1 Scope and Definitions

*Municipal government* refers to city and local government authorities, including Gemeinden, Kommunen, Städte, and equivalent structures in Swiss cantons. The strategy is designed to scale from small municipalities (population 5,000–50,000) to large cities (population 500,000+), with appropriate modulation.

*Open-source technology stack* refers to software components licensed under OSI-approved licences, deployed on infrastructure that the municipality controls or can migrate away from without undue cost or friction.

*Digital sovereignty* is the ability of a government to make independent decisions about its digital infrastructure, including the right to inspect, modify, audit, and migrate software without dependency on a single vendor [3].

### 1.2 Research Questions

1. What does a state-of-the-art open-source municipal technology stack look like in 2026?
2. What lessons can be drawn from the Swiss, German, and European sovereign technology communities?
3. What is the optimal phased implementation pathway for a city government of 50,000–500,000 population?
4. How should procurement, stakeholder engagement, and risk management be structured to maximise success probability?

---

## 2. Methodology

This paper employs a multi-method research design combining:

**Systematic literature review** of peer-reviewed publications, grey literature, and policy documents published between 2010 and 2026, covering e-government theory, digital sovereignty, open-source software in public administration, and municipal digital transformation.

**Comparative policy analysis** of technology legislation and strategies from Switzerland (EMBAG 2023, E-Government Strategy 2024–2027), Germany (OZG 2017/2024, Deutsche Verwaltungscloud-Strategie), and the European Union (Interoperable Europe Act 2024, EU Open Source Strategy 2020–2023).

**Technology stack evaluation** using a structured scoring matrix assessing each component on: (a) licence openness, (b) deployment maturity, (c) community health, (d) interoperability standards compliance, (e) security posture, (f) total cost of ownership, and (g) existing public-sector deployments.

**Stakeholder analysis** mapping the interests, influence, and engagement needs of each stakeholder group in the municipal digital transformation process.

The literature review is designed to be self-improving: the source registry (`Mem/source-registry.md`) and literature review state (`Mem/literature-review-state.md`) are versioned documents updated on a recurring basis. The `Scripts/update_literature_review.py` script provides structured prompts for reviewing and improving these files on a quarterly cadence.

### 2.1 Inclusion Criteria

Sources were included if they: (a) address open-source software in public administration; (b) cover governmental digital transformation strategy; (c) relate to the European, Swiss, or German regulatory context; or (d) provide primary data on municipal technology implementations. Sources published before 2010 were included only where they establish foundational theoretical frameworks.

### 2.2 Limitations

This paper is a first structured draft (v0.1.0). Some citations require verification against primary sources, noted in the source registry. Technology stack assessments reflect the state of publicly available information as of June 2026. Implementation cost estimates are indicative and must be validated against local procurement conditions.

---

## 3. Literature Review

### 3.1 Theoretical Foundations of E-Government

The academic literature on e-government has evolved through four broad phases [30]. First-generation e-government (1995–2005) focused on digitising existing processes and creating government websites [29]. Second-generation e-government (2005–2012) emphasised online service delivery, citizen portals, and back-office integration [7]. Third-generation e-government (2012–2020) introduced open data, participatory platforms, and mobile-first service design [8]. The current fourth generation (2020–present) is characterised by platform government, digital identity infrastructure, data spaces, and the sovereignty turn — a recognition that digital autonomy is a prerequisite for democratic self-governance [45].

Wirtz and Weyerer’s holistic e-government maturity model identifies five dimensions: technical infrastructure, process quality, service quality, citizen orientation, and transparency [7]. Municipal governments in Switzerland and Germany score variably across these dimensions; technical infrastructure and process quality lag citizen expectations in most jurisdictions, while the regulatory environment increasingly mandates transparency and interoperability [1, 2, 45].

### 3.2 Digital Sovereignty in Public Administration

The concept of digital sovereignty — the capacity of public institutions to make independent, auditable decisions about their digital infrastructure — has moved from academic concept to policy imperative in the European context [3, 5]. The EU Open Source Strategy 2020–2023 established “sharing and reuse” as a core principle, mandating that European institutions prefer open-source solutions in technology procurement [5]. The 2024 Interoperable Europe Act creates binding obligations for cross-border interoperability in public administrations [6].

Germany’s Sovereign Cloud Stack (SCS), developed by the Open Source Business Alliance (OSBA) and funded in part by the German Federal Ministry for Economic Affairs and Climate Action (BMWK), represents the most concrete realisation of digital sovereignty in cloud infrastructure. SCS provides a fully open-source, self-hostable cloud platform that enables public administrations to operate infrastructure that is technically and legally sovereign [3]. As of 2026, SCS underpins several German Länder cloud environments and is integrated with govdigital eG’s shared infrastructure [23].

Switzerland’s approach differs institutionally but converges on the same principles. The EMBAG legislation, which entered into force on 1 January 2024, requires all federal software developed with public funds to be released as open source unless compelling security reasons prevent it [1]. The law places Switzerland among the most progressive open-source mandating jurisdictions in the world.

### 3.3 The German OZG Ecosystem

The Onlinezugangsgesetz (OZG), enacted in 2017 and substantially reformed in 2024 (OZG 2.0), requires all German federal, Land, and municipal administrations to offer their administrative services online [2]. The OZG 2.0 reform addresses shortcomings of the first generation — including fragmented implementation, poor interoperability, and inconsistent user experience — through the “Once Only” principle, the “Einer für Alle” (EfA) approach to shared service development, and a federal platform architecture centred on BundID and FITKO [9, 10].

The openCode.de platform, launched in 2022, provides a centralised repository for government open-source software, enabling municipalities to discover, reuse, and contribute to shared solutions [10]. Dataport AöR and AKDB represent the cooperative model of public-sector IT delivery that the OZG ecosystem has reinforced [24].

### 3.4 Swiss Cantonal and Federal Digital Services

Switzerland’s federal structure creates both challenges and opportunities for municipal digital transformation. Key Swiss digital infrastructure includes:

- **Fedlex** (fedlex.admin.ch): the official platform for Swiss federal law, built on open standards and providing machine-readable legal data [1].
- **opendata.swiss**: the national open government data portal, built on CKAN and cataloguing thousands of datasets from federal, cantonal, and municipal authorities [44].
- **GEVER**: the standardised records management system for the federal administration, providing a template for cantonal and municipal implementations [43].
- **Swiss eID**: a decentralised, privacy-preserving digital identity system (post-2021 reform).

The E-Government Strategy Switzerland 2024–2027, co-authored by the Federal Council and the Conference of Cantonal Governments, sets out a collaborative framework for digital services that explicitly mandates open standards and interoperability [16].

### 3.5 Open Source Communities and Sovereign Technology

**Decidim** (Barcelona, 2016) is a participatory democracy platform used by over 400 organisations in 40 countries, including the cities of Barcelona, Helsinki, and the Swiss canton of Schaffhausen [12]. Its governance model — a multi-stakeholder association with a published social contract — is itself a model for open-source sovereignty.

**Matrix/Element** provides an open, decentralised, end-to-end-encrypted communication protocol increasingly adopted by European public administrations. The German federal BundesMessenger and the French government’s Tchap both operate on Matrix [14].

**Nextcloud** (Stuttgart, 2016) is the most widely deployed open-source file sync and collaboration platform in European public administration, used by thousands of German municipalities, the Swiss Federal Administration, and dozens of EU institutions [13].

**OpenDesk**, launched by the German Federal Government in 2023 and managed by ZenDiS GmbH, is a curated open-source desktop and collaboration suite built around Nextcloud, Cryptpad, OpenProject, Jitsi, and Element. It represents the first government-curated open-source workplace suite at scale [42].

### 3.6 Gaps in the Literature

1. **Total cost of ownership studies** comparing open-source and proprietary municipal stacks are sparse and methodologically inconsistent. Most available studies are vendor-commissioned.
2. **Longitudinal implementation data** from cities that have completed full open-source transitions is limited. Munich’s LiMux project (2003–2017) is frequently cited as a cautionary tale; post-mortems attribute its failure primarily to political, not technical, factors [30].
3. **Small-municipality perspectives** are underrepresented; most case studies focus on large cities or federal agencies.
4. **User experience research** comparing citizen satisfaction with open-source and proprietary municipal digital services is almost entirely absent.

See `Mem/literature-review-state.md` for the full gap analysis and improvement roadmap.

---

## 4. Technology Stack Analysis

A municipal technology stack can be decomposed into nine functional layers. The analysis below evaluates the leading open-source options for each layer against the scoring criteria defined in Section 2.

### 4.1 Digital Identity and Authentication

**Function:** Authenticate citizens and staff; federate identity across services; implement single sign-on (SSO).

**Recommended component: Keycloak** (Red Hat / CNCF) [21]

Keycloak is the de facto open-source identity and access management (IAM) platform for public administration. It implements OpenID Connect, OAuth 2.0, and SAML 2.0, enabling federation with national identity systems (BundID in Germany, eID in Switzerland). It is deployed by numerous European governments including the EU institutions, German Länder, and Swiss cantons.

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

For municipalities requiring full GEVER compliance (Switzerland), cantonal GEVER solutions (CMI, Fabasoft Community) provide the compliance layer with Nextcloud as the collaborative front-end. For German municipalities, AKDB’s BayernPortal and Dataport components provide the equivalent capability.

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Licence openness | 5 | AGPL-3.0 (Nextcloud) |
| Deployment maturity | 5 | 400,000+ organisations |
| Community health | 5 | Nextcloud GmbH + community |
| Interoperability | 4 | WebDAV, CalDAV, CardDAV, CMIS |
| Security posture | 5 | ISO 27001 certified offering |
| TCO | 5 | No per-seat licence (Community) |
| Public-sector deployments | 5 | Swiss federal, German states |

### 4.3 Workflow Automation and Business Process Management

**Function:** Automate administrative workflows; model, execute, and monitor BPMN processes.

**Recommended component: Camunda Platform 8 Community** [33]

Camunda provides a BPMN 2.0-native workflow engine with strong support for complex multi-step administrative processes and XÖV data standards integration [46]. **Flowable** (Apache 2.0) is a lighter-weight alternative if Camunda’s dual-licensing model creates procurement complications.

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Licence openness | 4 | Community: Apache 2.0; Enterprise: proprietary |
| Deployment maturity | 5 | Production-proven |
| Community health | 4 | Active; enterprise tier funds development |
| Interoperability | 5 | BPMN 2.0, REST API, event-driven |
| Security posture | 4 | Actively maintained |
| TCO | 3 | Community free; scale may need Enterprise |
| Public-sector deployments | 4 | Multiple German Länder |

### 4.4 Citizen Participation

**Function:** Consultation, participatory budgeting, initiative collection, deliberation platforms.

**Recommended component: Decidim** [12]

Decidim is the most mature and widely adopted open-source participation platform globally. Use by Barcelona, Helsinki, the canton of Schaffhausen, and the City of New York validates it across regulatory and linguistic contexts. The Decidim Association provides governance, a social contract, and a global community of practice.

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Licence openness | 5 | AGPL-3.0 |
| Deployment maturity | 5 | 400+ deployments globally |
| Community health | 5 | Active association and community |
| Interoperability | 4 | REST API, webhooks |
| Security posture | 4 | Actively maintained |
| TCO | 5 | No licence cost |
| Public-sector deployments | 5 | Cities, cantons, federal agencies |

**Alternative:** CONSUL Democracy (Madrid), also AGPL-3.0, strong in Spanish-speaking world and some European cities.

### 4.5 Communication and Collaboration

**Function:** Internal messaging, video conferencing, email, calendar; secure inter-agency communication.

**Recommended components:**
- **Matrix/Element** for messaging and inter-agency secure communication [14]
- **Jitsi Meet** or **BigBlueButton** for video conferencing [34, 35]
- **Nextcloud Talk** for integrated team communication

The German federal BundesMessenger (built on Matrix) provides a reference deployment applicable to municipal contexts.

| Component | Licence | Maturity | Key advantage |
|---|---|---|---|
| Matrix/Element | Apache 2.0 | Production | E2E encryption, federation |
| Jitsi Meet | Apache 2.0 | Production | Browser-based, self-hostable |
| BigBlueButton | LGPL-3.0 | Production | Council meeting focus |
| Nextcloud Talk | AGPL-3.0 | Production | Integrated with file management |

### 4.6 Open Data Publication

**Function:** Publish machine-readable datasets; catalogue data; provide API access; comply with PSI/Open Data directives.

**Recommended component: CKAN** [22]

CKAN is the world’s leading open-source open data portal software. It powers opendata.swiss, data.gov, data.gov.uk, and dozens of national and municipal open data portals. Its plugin architecture enables integration with DCAT-AP, DCAT-AP.de, and OGD Switzerland metadata standards, and harvesting from upstream catalogues.

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Licence openness | 5 | AGPL-3.0 |
| Deployment maturity | 5 | 10+ year production track record |
| Community health | 4 | CKAN Association; active |
| Interoperability | 5 | DCAT-AP, OAI-PMH, SPARQL |
| Security posture | 4 | Actively maintained |
| TCO | 4 | No licence cost; ops overhead |
| Public-sector deployments | 5 | Switzerland, Germany, EU |

### 4.7 Geographic Information Systems

**Function:** Map-based citizen services; urban planning; spatial data publication.

**Recommended components:**
- **QGIS** (desktop/server) for spatial data editing and analysis [37]
- **GeoServer** (GeoTools) for OGC-compliant spatial data publication
- **OpenStreetMap** as the base cartographic layer [36]

Switzerland’s swisstopo and Germany’s BKG (Bundesamt für Kartographie und Geodäsie) provide open, high-quality governmental base map data compatible with this stack.

### 4.8 Public Website and Content Management

**Function:** Public-facing website; news and announcements; service directory.

**Recommended components:**
- **TYPO3** (German-speaking world): dominant in Swiss and German public administration; the TYPO3 Association provides long-term support and public-sector extensions [19]
- **Drupal**: strong international track record; used by the European Commission

Both systems support accessibility standards (WCAG 2.1 AA / BITV 2.0), multilingualism, and integration with open data catalogues.

### 4.9 Cloud Infrastructure and Hosting

**Function:** Compute, storage, networking, container orchestration; digital sovereignty at the infrastructure layer.

**Recommended component: Sovereign Cloud Stack (SCS)** [3, 11]

SCS is the most strategically important infrastructure choice for European municipalities. It provides a fully open-source cloud stack (OpenStack + Kubernetes + Ceph) that can be self-hosted, operated by a cooperative provider (govdigital eG), or deployed by certified SCS cloud operators.

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Licence openness | 5 | Apache 2.0 / fully open |
| Deployment maturity | 4 | Production in multiple Länder |
| Community health | 5 | OSBA-backed, growing |
| Interoperability | 5 | Open APIs, OCI-compliant |
| Security posture | 5 | BSI IT-Grundschutz compatible |
| TCO | 4 | No licence; infrastructure cost |
| Public-sector deployments | 4 | German Länder, growing |

**For municipalities without in-house cloud operations capacity:** use certified SCS hosters (e.g., plusserver, OSISM) providing managed SCS with full data sovereignty guarantees.

### 4.10 Reference Architecture

```
+-------------------------------------------------------------+
|                     CITIZEN TOUCHPOINTS                     |
|         TYPO3/Drupal . Decidim . CKAN . Nextcloud          |
+-------------------------------------------------------------+
|                       SERVICE LAYER                        |
|     Camunda Workflows . XOEV Forms . GeoServer . QGIS      |
+-------------------------------------------------------------+
|                    COLLABORATION LAYER                     |
|     Nextcloud . Matrix/Element . Jitsi . OpenProject       |
+-------------------------------------------------------------+
|                      IDENTITY LAYER                        |
|            Keycloak <-> BundID / Swiss eID                 |
+-------------------------------------------------------------+
|                    INFRASTRUCTURE LAYER                    |
|   Sovereign Cloud Stack . Kubernetes . PostgreSQL . Ceph   |
+-------------------------------------------------------------+
```

All layers communicate via open APIs. Container orchestration across the stack is handled by Kubernetes [39], and relational persistence by PostgreSQL [41], both running on the Sovereign Cloud Stack. Data exchange uses XÖV standards (Germany) [46] or eCH standards (Switzerland). Security is governed by BSI IT-Grundschutz (Germany) [26] or the Swiss ISDS framework.

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

**Success criteria:**
- Political mandate secured (council resolution or executive decision)
- Budget envelope approved (indicative: €200,000–€500,000 for Phase 0–1 depending on city size)
- Project lead appointed

### Phase 1: Identity and Infrastructure (Months 4–12)

**Objective:** Stand up the foundational layers that everything else depends on.

**Deliverables:**
- Sovereign Cloud Stack environment operational (own or hosted)
- Keycloak identity provider deployed and federated with national identity system
- Nextcloud baseline deployment for internal collaboration
- Matrix/Element messaging for staff
- BSI IT-Grundschutz baseline documentation complete

**Success criteria:**
- 100% of IT staff can authenticate via Keycloak SSO
- File storage migrated from proprietary cloud to Nextcloud
- Basic encrypted messaging operational
- Security baseline documented and approved

### Phase 2: Services and Workflows (Months 10–18)

**Objective:** Migrate or build the first five citizen-facing services on open infrastructure.

**Deliverables:**
- Five highest-volume administrative services deployed on Camunda/XÖV stack
- TYPO3 or Drupal CMS migration complete
- Open data portal (CKAN) launched with first 20 datasets
- Decidim instance deployed for the first participatory process

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

**Success criteria:**
- End-to-end service delivery without paper for 80% of transaction types
- Data quality metrics established and tracked
- First annual open data report published

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
- Total cost of ownership report published

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
| Civil society / NGOs | Transparency, access, participation | Decidim platform, public roadmaps |
| Open-source communities | Contribution, reuse | openCode.de participation, upstream contributions |
| Sovereign technology providers | Partnership, deployment | Certified partner agreements |
| Data protection officer | GDPR compliance | Privacy-by-design review at each phase |

### 6.2 Procurement Framework

Open-source procurement requires a different framework from proprietary licence purchasing. Key principles:

**1. Procure services, not licences.** Open-source software is free to use; municipalities pay for implementation, hosting, support, customisation, and training. Procurement documents must be structured around these services.

**2. Use cooperative procurement structures.** Germany’s govdigital eG and Swiss cantonal IT cooperatives provide framework agreements for open-source municipal IT that satisfy public procurement law (GWB/Vergaberecht in Germany; BöB in Switzerland) [23].

**3. Apply the “Public Money? Public Code!” principle.** All custom software developed under contract must be released under an OSI-approved open-source licence and published on openCode.de or an equivalent public repository. This should be a contract condition [4].

**4. Evaluate total cost of ownership.** Procurement scoring must include a 5-year TCO model covering implementation, hosting, training, support, and exit costs. Proprietary alternatives typically understate long-term costs by omitting vendor lock-in risk and licence escalation.

**5. Require interoperability standards.** All procured systems must implement: XÖV (Germany), eCH (Switzerland), DCAT-AP (EU open data) [46]. Non-compliance should be a disqualifying criterion.

**6. Prefer certified cooperative providers.** For infrastructure, prefer SCS-certified cloud operators or members of govdigital eG, who are bound by collective data sovereignty agreements [23].

### 6.3 Change Management

Open-source transitions frequently fail not on technical grounds but on human factors: end-user resistance, insufficient training, middle-management inertia, and political backsliding under vendor lobbying.

**Recommendations:**
- Appoint a **Digital Transformation Champion** at senior political level with explicit mandate
- Establish **open-source champions** in each department with advanced training and peer support role
- Run **parallel operations** for a minimum of three months before cutting over critical systems
- Document and celebrate **early wins** (cost savings, new capabilities, citizen feedback)
- Publish a **public transparency dashboard** showing migration progress, costs, and service quality metrics

---

## 7. Risk Analysis

### 7.1 Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Political reversal after election | Medium | High | Embed in legislation/ordinance; build cross-party consensus |
| Vendor lobbying / FUD campaigns | High | Medium | Document TCO evidence; engage civil society; publicise mandate |
| Skill gap in IT team | High | Medium | Training programme; cooperative IT provider; community of practice |
| Integration failure between layers | Medium | High | Phased rollout with decision gates; reference architecture adherence |
| Data loss during migration | Low | Critical | Full backup protocol; parallel operation; staged migration |
| GDPR / data protection violation | Low | High | Privacy-by-design; DPO engagement; data mapping |
| User adoption failure | Medium | High | Change management; UX testing; training; parallel systems |
| Security incident | Low | Critical | BSI IT-Grundschutz; penetration testing; incident response plan |
| Community fragmentation | Low | Medium | Contribute upstream; align with openCode.de; join govdigital eG |
| Cost overrun | Medium | Medium | Phase-gated budget; independent project office; open TCO accounting |

### 7.2 The Munich Cautionary Case

The City of Munich’s LiMux project (2003–2017) is the most-cited case of a large-scale municipal open-source transition that was reversed. Post-mortem analysis identifies the reversal was driven primarily by: (a) a change in political leadership with closer ties to Microsoft; (b) inadequate change management and user training; (c) compatibility issues with state-level systems that had not been updated to support open standards [30]. The technical implementation itself was broadly successful.

The Munich case confirms that political risk management — building cross-party support and embedding digital sovereignty as a constitutional value, not merely a procurement preference — is as important as technical planning.

### 7.3 Security Considerations

The BSI’s IT-Grundschutz framework provides a comprehensive security baseline applicable regardless of licence model [26]. Key requirements:

- All server components must receive regular security updates with a documented patch management process
- Authentication must meet BSI Authenticator Assurance Level 2 (AAL2) for citizen-facing services
- Data in transit encrypted (TLS 1.3 minimum); data at rest encrypted for sensitive categories
- Penetration testing at each phase gate
- Incident response plan aligned with NIS2 obligations [27]
- Software Bill of Materials (SBOM) maintained for all open-source dependencies

---

## 8. Conclusion

The evidence reviewed in this paper converges on four findings:

**1. Open-source municipal technology stacks are technically mature and production-proven.** Every functional requirement of a modern municipal government can be met by open-source software with documented deployments at peer municipalities.

**2. The regulatory environment increasingly mandates open-source and interoperability.** EMBAG (Switzerland), OZG 2.0 (Germany), and the Interoperable Europe Act (EU) create legal obligations that proprietary, vendor-locked systems cannot sustainably satisfy. Municipalities that begin the transition now are building compliance capital; those that delay are accumulating regulatory debt.

**3. The economic case is compelling when total costs are counted correctly.** Open-source stacks eliminate per-seat licence costs — often €100–300 per user per year for productivity software alone — and reduce vendor lock-in risk. Cooperative procurement models spread implementation costs across many municipalities.

**4. Success requires as much political and organisational investment as technical investment.** Clear political mandate, skilled change management, and sustained stakeholder engagement are the binding constraints. The Munich case and successful transitions in Barcelona, Stuttgart, and Swiss cantons alike confirm this.

Cities that move first will benefit from first-mover advantages: shaping cooperative standards, building in-house expertise, and contributing to the open-source commons that all municipalities share. The invitation is open.

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

[14] The Matrix Foundation. (2023). *Matrix Specification*. https://spec.matrix.org/ — [Open access, Apache 2.0]

[16] E-Government Suisse. (2023). *Strategie E-Government Schweiz 2024–2027*. Bern: Schweizerische Bundeskanzlei. https://www.egovernment.ch/de/umsetzung/e-government-strategie/ — [Open access]

[19] TYPO3 Association. (2023). *TYPO3 in Public Administration*. Düsseldorf: TYPO3 Association. https://typo3.org/project/association — [Open access]

[20] OpenProject GmbH. (2023). *OpenProject for Government: Open Source Project Management*. Berlin: OpenProject GmbH. https://www.openproject.org/ — [Open access, GPLv3]

[21] Red Hat / Keycloak Community. (2023). *Keycloak: Open Source Identity and Access Management*. https://www.keycloak.org/ — [Open access, Apache 2.0]

[22] CKAN Association. (2023). *CKAN: Open Source Data Portal Software*. https://ckan.org/ — [Open access, AGPL-3.0]

[23] govdigital eG. (2023). *govdigital: Genossenschaft für digitale Verwaltung*. Berlin: govdigital eG. https://govdigital.de/ — [Open access]

[24] Dataport AöR. (2023). *Dataport: IT-Dienstleister für die öffentliche Verwaltung*. Hamburg: Dataport AöR. https://www.dataport.de/ — [Open access]

[26] Bundesamt für Sicherheit in der Informationstechnik (BSI). (2023). *BSI IT-Grundschutz-Kompendium*. Bonn: BSI. https://www.bsi.bund.de/ — [Open access, CC-BY-ND 3.0 DE]

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

[42] BMI / ZenDiS GmbH. (2023). *OpenDesk: Der digitale Arbeitsplatz der Bundesverwaltung*. https://opendesk.eu/ — [Open access, AGPL-3.0]

[43] Schweizerisches Bundesarchiv (BAR). (2023). *Geschäftsverwaltung (GEVER) in der Bundesverwaltung*. Bern: BAR. https://www.bar.admin.ch/ — [Open access]

[44] opendata.swiss. (2023). *Open Government Data Switzerland*. Bern: Schweizerische Bundeskanzlei. https://opendata.swiss/ — [Open access, CC-BY-4.0]

[45] European Commission. (2017). *European Interoperability Framework — Implementation Strategy (EIF)*. Brussels: European Commission. https://joinup.ec.europa.eu/collection/nifo-national-interoperability-framework-observatory — [Open access, CC-BY-4.0]

[46] KoSIT. (2023). *XÖV-Standards: XML in der öffentlichen Verwaltung*. Bremen: KoSIT. https://www.xoev.de/ — [Open access]

---

*This document is released under the Creative Commons Attribution 4.0 International Licence (CC-BY-4.0).*
*Attribute as: Sebastian Graf, Autonomous Office of Civil Digital Infrastructure (sebk4c@tuta.com)*
