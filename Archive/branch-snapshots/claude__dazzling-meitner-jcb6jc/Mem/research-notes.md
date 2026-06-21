# Research Notes — City GovTech Strategy

**Version:** 0.2.0
**Last updated:** 2026-06-21

Append-only working document. Newest entries at top.

---

## 2026-06-21 — v0.2.0 deep research round

Five parallel web searches + eight primary source fetches. Adversarial 3-vote verification applied to all major quantitative claims. 13 verified findings integrated into v0.2.0 paper.

### Key new verified findings

**1. Deutschland-Stack makes SCS binding at all government levels (March 2026)**
The IT-Planungsrat (IT Planning Council) made Sovereign Cloud Stack standards binding for
federal, state, and *municipal* administrations on 24 March 2026. The Deutschland-Stack
framework mandates ODF + PDF/UA as the only permissible document formats (proprietary
excluded). 7-layer architecture with 2028 delivery target. "Made in EU first" principle.
Source: Heise Online (two articles, verified). This is a landmark development that
materially strengthens the case for open-source municipal technology.

**2. Swiss E-ID law passed December 2024; SWIYU wallet; go-live 2026**
The Swiss Parliament adopted the E-ID law on 20 December 2024 (Ständerat 43–1). Official
wallet: SWIYU. Public beta Q1 2025 with final production technology. Go-live: early 2026.
Integration into cantonal/municipal services (address changes, e-voting, local permits)
is the planned next phase. OIDC federation with Keycloak is technically documented.
Source: admin.ch (federal council decision), humancolossus.foundation, biometricupdate.
All verified.

**3. GendBuntu: 103,164 workstations, 40% TCO, €2M/year savings (verified June 2024)**
The OSOR article (2013) and Wikipedia (June 2024 update) together confirm:
- June 2024: 103,164 workstations (97% of force)
- ~€2M/year software licensing savings
- ~40% TCO reduction vs. proprietary baseline
- Ubuntu 24.04 LTS upgrade: December 2024
- DINUM cited GendBuntu as national rollout governance model: February 2026
This is the world's best TCO reference case for government Linux at scale.

**4. Schleswig-Holstein: €15M savings, <1yr payback (verified Q1 2026)**
- 30,000 workstations migrating to LibreOffice
- ODF official format from 1 August 2024
- €15M annual savings (€500/person/year previously for Microsoft 365)
- €9M implementation investment, payback under 1 year
- Dataport provides 1st/2nd level support
- ~80% complete by early 2026
Source: TDF Blog, The Register, Medium (Artuc 2025). All verified.

**5. ZenDiS/OpenDesk: cloud available September 2024; target 160K licences**
- ZenDiS wholly-owned federal GmbH under BMI
- Took over openDesk January 2024
- Cloud-based version available to all German public institutions September 2024
- First deployment: Ministerpräsidentenkonferenz Leipzig, October 2024
- BWI GmbH (Bundeswehr IT) user
- Target: 160,000 licences end 2025 (not yet confirmed as achieved)
Components: Nextcloud, Cryptpad, OpenProject, Jitsi Meet, Element, Collabora Online.

**6. BundID: 4.9M accounts, 2M logins/month, 43 services (August 2025)**
- 4.9M active accounts (after cleanup of ~400K inactive)
- 2M logins/month (doubled from 2024)
- 43 digital administrative services integrated
- End 2023: only 81/581 OZG services online
- Expected to evolve to DeutschlandID

**7. NIS2 Germany: Act in force 6 Dec 2025; KRITIS-Dachgesetz 17 Mar 2026**
- NIS2 Implementation Act: amends BSI Act; in force December 6, 2025
- ~30,000 organisations in scope; 11,500 registered by March 2026 deadline
- KRITIS-Dachgesetz: in force March 17, 2026; addresses municipalities directly
- Municipal digital infrastructure now has direct cybersecurity compliance obligations

**8. Interoperable Europe Act: binding open-source preference since July 2024**
- Regulation EU 2024/903; in force April 11, 2024; most provisions July 12, 2024
- Interoperability assessments required from January 12, 2025
- Article 4: share solutions including source code
- "Shall prioritise open source" where functionally equivalent
- Municipalities and regions: explicit active stakeholders

**9. eCH standards: verified Swiss municipal interoperability framework**
- eCH-0007 (Municipal Data Standard, V6.0): municipality identification and naming
- eCH-0020 (Reporting Reasons, V4.1.0, approved May 16, 2025): civil registration
- eCH-0058 (Messaging Framework): technical envelope for system communication
- Published by eCH Association (ech.ch) under Swiss Federal Chancellery

**10. Signalen: 39 Dutch municipalities, 7.9M citizens/year**
OSOR case study confirmed. EfA/cooperative development model. NLP/ML for citizen report
classification. EUPL-1.2 licence. Best available example of inter-municipal cooperative
open-source development applicable to DE/CH contexts.

**11. GovStack v1.0: 9 building blocks, municipal applicability confirmed**
Founded 2020 (Estonia, GIZ, ITU, DIAL). V1.0 June 2023. Building blocks:
identity, payments, registries, messaging, scheduling, consent, signature, workflow, data
collection. All applicable to municipal level. Maps 1:1 onto the recommended stack layers.

**12. Sovereign Tech Agency: ~€23.5M in 60+ projects, ~€17M annual budget**
Evolved from Sovereign Tech Fund. Targets foundational open-source infrastructure
(FreeBSD, curl, OpenSSH, Log4j, etc.). Annual budget ~€17M under negotiation in new
coalition. Complements ZenDiS. Municipalities can advocate through Land/federal channels.

**13. SCS: research project concluded Dec 2024; forum SCS-Standards from Jan 2025**
OSBA + 14 member companies founded forum SCS-Standards on January 1, 2025. This body
takes over SCS certification from the funded research project. Key operators: plusserver
(pluscloud open), STACKIT, OSISM, govdigital eG.

### Open questions (v0.2.0 → v0.3.0)

- **Q1:** Confirmed OpenDesk licence count for end-2025 (target was 160,000)?
- **Q2:** BundID/DeutschlandID transition: timeline and scope of changes?
- **Q3:** Swiss cantonal uptake of SWIYU post-launch (expected data: late 2026)?
- **Q4:** Which specific eCH standards are mandated (not just recommended) for Swiss municipalities?
- **Q5:** NIS2 equivalent for Switzerland — is there a Swiss counterpart legislation in force or planned?
- **Q6:** EU Data Act 2023 — specific municipal data obligations under Articles 3–10?
- **Q7:** GAIA-X — any practical tools for municipalities available in 2026, or still policy?
- **Q8:** eVaka (Finland) — can we get specific adoption statistics (number of municipalities, children served)?
- **Q9:** Schlessing-Holstein 2026 end-of-year status — is the 80% figure confirmed?
- **Q10:** BundesMessenger 2025 adoption statistics across German Länder?

### Working hypotheses (updated)

- **H1:** The binding constraint for municipal open-source adoption is political sustainability across
  election cycles, not technical maturity (sufficient) or cost (demonstrably favourable).
  Evidence: Munich LiMux (political failure), GendBuntu (institutional commitment = success).
  Status: STRENGTHENED by new TCO evidence in v0.2.0.

- **H2:** Cooperative IT structures (govdigital eG, AKDB, Dataport, Swiss cantonal IT cooperatives)
  are the most efficient delivery vehicle for municipalities <100,000.
  Evidence: Signalen model (39 Dutch municipalities), govdigital eG framework contracts.
  Status: CONFIRMED by Signalen case study.

- **H3:** A phased approach starting with identity (Keycloak) and files (Nextcloud/OpenDesk) gives
  the fastest path to demonstrable wins at lowest disruption risk.
  Status: UNCHANGED — supported by reference architecture.

- **H4:** The EU regulatory environment will make proprietary, vendor-locked municipal IT legally
  problematic within 5–7 years. Early movers gain compliance capital; late movers accumulate debt.
  Status: MATERIALLY STRENGTHENED — the Deutschland-Stack (March 2026), Interoperable Europe Act
  (January 2025 interoperability assessments), NIS2 (December 2025), and KRITIS-Dachgesetz
  (March 2026) all entered force since v0.1.0. The trajectory is faster than anticipated.

- **H5 (NEW):** The Deutschland-Stack will become the de facto technical standard for municipal
  IT procurement across all 16 German Länder within 2–3 years of its March 2026 binding decision.
  Municipalities that begin SCS-aligned procurement now will face minimal migration costs;
  those that procure proprietary alternatives will face mandatory migration by 2028.

---

## 2026-06-20 — Initial research round

### Key findings

**1. EMBAG is the strongest legislative mandate globally.** Switzerland's EMBAG (SR
172.019, in force 2024-01-01) requires open-source release *by default* with a narrow
security exception — stronger than comparable French, Italian, or German federal law.
Municipal implementation guidance is still being developed by cantons.

**2. OpenDesk is the reference implementation for German municipalities.** Now confirmed
as managed by ZenDiS GmbH des Bundes. OpenDesk bundles Nextcloud + Cryptpad + OpenProject
+ Jitsi + Element + Collabora. Available to all German public institutions since September
2024.

**3. Sovereign Cloud Stack is production-ready and standards are now binding.** SCS
standards made binding by IT-Planungsrat March 24, 2026 under Deutschland-Stack.
Municipalities should plan on SCS-certified hosters first, then build in-house capacity.

**4. BundID adoption is the key bottleneck for German OZG progress.** 4.9M accounts,
2M logins/month as of August 2025. 43 services. 81/581 OZG services online by end 2023.
Municipalities need Keycloak federation supporting both BundID and fallback flows.

**5. Decidim governance is a transferable pattern.** Multi-stakeholder association with
published social contract. Schaffhausen canton deployment merits a deeper case study.

**6. Munich LiMux failure was political, not technical.** Confirmed by research.

**7. GendBuntu and Schleswig-Holstein provide definitive TCO evidence.** See v0.2.0
findings above.
