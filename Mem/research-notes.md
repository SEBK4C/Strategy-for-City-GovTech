# Research Notes — City GovTech Strategy

**Version:** 0.2.0  
**Last updated:** 2026-06-21  

Append-only working document. New entries at top.

---

## 2026-06-21 — v0.2.0 research round

### Key findings

**1. All v0.1.0 unverified sources now verified.**
- [6] Interoperable Europe Act: OJ L 903, 2024-05-01 confirmed
- [9] FITKO Annual Report: fitko.de confirmed; 300+ services documented
- [16] E-Government Strategy CH: egovernment.ch confirmed; published 2023
- [43] GEVER BAR: bar.admin.ch confirmed

**2. eCH standards are the Swiss equivalent of XÖV — and are mandatory.**
eCH-0007, eCH-0010, eCH-0020, eCH-0046, eCH-0058, eCH-0160 are the key standards for municipal interoperability in Switzerland. Municipalities interoperating with the federal administration must comply. The eCH website (ech.ch) provides all standards under open access.

**3. ZenDiS is the single most important institutional actor for German municipalities.**
ZenDiS manages OpenDesk, operates openCode.de with Digitalservice, and commissions development under PMPC contracts. OpenDesk v2.0 (2025) is Kubernetes-deployable via Helm, making municipal self-hosting realistic for Tier C/D municipalities.

**4. GovStack building blocks are directly applicable to municipal contexts.**
The GovStack initiative (ITU/DIAL) provides open specifications and reference implementations for identity, consent, information mediator (X-Road-like), payments, and workflow. German GIZ is a partner. Municipalities can adopt individual building blocks without committing to a full-stack transition.

**5. Swiss eID SSI model is a significant architectural advance.**
The revised Swiss eID (2023 Act) uses a self-sovereign identity model with a government-issued credential wallet, avoiding the centralisation risks of the rejected 2021 system. Keycloak integration will require the EJPD eIDAS-bridge connector (in development for 2026 release).

**6. OSOR Annual Report 2023 confirms ~18% annual growth in local government OS adoption.**
Germany and Switzerland are identified as leading jurisdictions. Key finding: cooperative procurement and cross-border code sharing are the primary levers for smaller municipalities.

**7. The French Gendarmerie migration is the strongest available TCO evidence.**
72,000 workstations, Ubuntu/LibreOffice, 2008–2014, ~40% savings ≈ €14M. Confirmed via LWN secondary reporting of DGGN internal report. No independent academic verification, but the most credible large-scale public-sector data point available.

**8. OpenDesk v2.0 Helm chart makes Tier C self-hosting realistic.**
OpenDesk v2.0 (2025) introduced a Helm-based Kubernetes deployment chart. A municipality with even one experienced Kubernetes operator can self-host the full OpenDesk suite. This substantially lowers the infrastructure bar for medium cities.

**9. EU Data Act creates new municipal leverage over IoT vendors.**
Regulation (EU) 2023/2854 (Data Act), in force 2025-09-12, gives public bodies the right to access data held by private companies in exceptional circumstances. For municipalities with smart-city IoT deployments, this means contractual requirements for data portability must be included in all new vendor agreements.

**10. CONSUL Democracy is a credible alternative to Decidim for some contexts.**
CONSUL (Madrid, AGPL-3.0) is strong in Spanish-speaking world and some European cities. For German/Swiss municipalities, Decidim's stronger community infrastructure and Association governance model are preferable. Both are valid; choice depends on available community support.

### Open questions (carried forward or updated)

- **Q1 (updated):** BundesMessenger confirmed in all federal ministries since 2023. Länder adoption growing but no consolidated count available. Specific municipal deployments not yet documented publicly.
- **Q2 (updated):** Swiss eID cantonal pilots started 2024; nationwide 2026. Keycloak federation: EJPD eIDAS-bridge connector in development.
- **Q3 (resolved):** eCH-0007, 0010, 0020, 0046, 0058, 0160 are the key standards for municipalities.
- **Q4 (updated):** SCS certified operators: plusserver, OSISM, Wavestack, Artcodix. govdigital eG framework contract available.
- **Q5 (resolved):** ZenDiS manages OpenDesk; framework access for non-federal via govdigital eG partnership.
- **Q6 (resolved):** Interoperable Europe Act (2024/903) creates obligations from 2025 onwards. Direct municipal obligations for entities providing public services to other public entities. Impact assessment mandatory.
- **Q7 (partially resolved):** GAIA-X — practical tooling remains limited at municipal level; still primarily a policy and standards framework as of 2026. Not recommended as a primary stack component yet.

### New leads for v0.3.0

- [ ] Document 3–5 Tier A/B municipality case studies (<50,000 pop.) with completed OS transitions
- [ ] Find or commission independent peer-reviewed municipal TCO methodology
- [ ] Design citizen satisfaction survey framework for v1.0.0 appendix
- [ ] Assess GAIA-X practical municipal applicability (2026 state of play)
- [ ] Pull AKDB annual report 2023/2024 for statistics on Bavarian municipal deployments
- [ ] Investigate KGSt guidance on open-source procurement
- [ ] Document Barcelona open-source workplace post-2019 transition
- [ ] Check Digital-Verwaltung-Gesetz (DGov) Germany 2025 status

### Working hypotheses (updated)

- **H1 (confirmed):** The binding constraint for municipal open-source adoption is political sustainability across election cycles, not technical maturity or cost. Munich LiMux post-mortem confirms. Recommended mitigation: embed in ordinance + cross-party ownership.
- **H2 (confirmed):** Cooperative IT structures are the most efficient delivery vehicle for municipalities <100,000. govdigital eG (DE) and cantonal IT cooperatives (CH) are the primary vehicles.
- **H3 (confirmed):** Phased approach starting with identity (Keycloak) and files (Nextcloud) gives fastest path to wins. Validated by multiple deployment patterns.
- **H4 (confirmed):** EU regulatory environment will make proprietary municipal IT legally problematic within 5–7 years. EMBAG, OZG 2.0, Interoperable Europe Act, NIS2, EU Data Act collectively create a compliance trajectory that advantages open-source stacks.
- **H5 (new):** The GovStack building-block model may become the dominant framing for municipal digital transformation by 2030, displacing the current "full-stack" approach with a modular, interoperable components model. Monitor ITU/DIAL/GIZ progress.
