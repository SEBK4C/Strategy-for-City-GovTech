# Research Notes — City GovTech Strategy

**Version:** 0.2.0
**Last updated:** 2026-06-21

Append-only working document for findings, open questions, hypotheses, and leads. Add new
entries at the top.

---

## 2026-06-21 — v0.2.0 research round

### Key findings

**1. EU AI Act creates concrete obligations for municipal technology procurement.** The
AI Act (in force August 2024, phased application) classifies several common municipal AI
applications as high-risk (Annex III), including AI systems used to make or support
individual citizen decisions on benefits, services, or administrative processes. Practical
implication: municipalities cannot deploy open-source LLM-based systems for individual
citizen decisions without a fundamental rights impact assessment (FRIA) and human
oversight. Municipalities should inventory all AI applications — including AI features
built into procurement software — before Phase 3 deployment.

**2. ZenDiS is the key actor for German municipal open-source access.** ZenDiS (founded
2022) has emerged as the critical intermediary between the federal open-source mandate
and municipal implementation capacity. OpenDesk v2.x (2025) bundles the full stack
(Nextcloud + Collabora + Element + BigBlueButton + OpenProject + Cryptpad) in a single,
professionally maintained deployment. The ZenDiS framework contract provides legal
procurement cover for municipalities without independent EU-threshold tender capacity.

**3. The Swiss E-ID is now operational.** The E-ID-Gesetz (SR 161.5), following the
successful 2023 parliamentary approval after the failed 2021 referendum, entered
progressive operation from 2025. The new system is state-issued (unlike the rejected
private-provider model), based on SSI/verifiable credentials principles, and integrates
with Keycloak via OpenID Connect. Swiss municipalities should plan E-ID federation in
Phase 1 identity deployment.

**4. eCH standards are the Swiss integration prerequisite.** Unlike XÖV in Germany
(which is mandatory for OZG), eCH compliance is a de facto requirement for Swiss
municipal system integration with cantonal and federal platforms. Key standards:
eCH-0007 (Gemeinderegister), eCH-0011 (Meldewesen), eCH-0020 (Ereignismeldung),
eCH-0058 (Schnittstellendefinition). Swiss municipalities should add eCH compliance as
a mandatory evaluation criterion in all IT procurement.

**5. TCO evidence is stronger than previously assessed.** The French Gendarmerie (40%
workstation cost reduction, 85,000 desktops) and City of Paris (€5M savings over 5 years)
provide the most credible large-scale TCO evidence. Together with the Jena cooperative
model (40% lower than standalone procurement) and the indicative per-user cost model in
the paper, the economic case for open-source transition is now better evidenced. The
remaining gap is a rigorous 10-year longitudinal study.

**6. Cooperative IT structures are the most efficient delivery vehicle for municipalities
under 100,000.** The evidence from Dataport (Hamburg/SH/HB), AKDB (Bavaria), TIT
(Thuringia), and govdigital eG consistently shows: cooperative IT reduces implementation
cost by 40–70% for small/medium municipalities while maintaining data sovereignty.
Swiss cantonal IT cooperatives (e.g., kkt, VRSG, IT St.Gallen) provide equivalent
structures.

**7. The Cyber Resilience Act changes procurement due diligence.** From 2027, all
software products must meet CRA security requirements. For open-source: projects not
"placed on the market" in a commercial context (i.e., purely volunteer/non-commercial)
have limited obligations; however, municipalities procuring commercially managed
open-source services should verify CRA compliance of their service providers.

**8. LibreOffice is now the dominant evidence-based productivity choice for European
public administration.** Beyond the Gendarmerie and Paris cases, the BVA (German Federal
Administration Office) and the Spanish national administration both run LibreOffice at
scale. Collabora Online CODE, integrated with OpenDesk and Nextcloud, removes the last
practical barrier (lack of real-time collaborative editing) that previously required
Microsoft Office.

### Open questions (v0.2.0)

- **Q1:** What is the current BundID citizen registration rate and adoption velocity?
  Municipal Keycloak implementations should design for gradual BundID adoption with
  low-assurance fallback flows.
- **Q2:** How does the EU Digital Identity Wallet (EUDIW / ARF) interact with Swiss E-ID
  and BundID? Timeline for convergence? This will affect Phase 1 identity architecture.
- **Q3:** What is the exact ZenDiS pricing structure for municipalities via OpenDesk
  framework contract? Is it publicly available?
- **Q4:** Current state of GAIA-X for municipalities — are there practical tools (not
  just policy frameworks) available in 2026?
- **Q5:** Which Swiss municipalities under 20,000 have completed or are in active
  progress on a full open-source transition? Case study candidates needed.
- **Q6:** Have any German municipalities deployed EU-AI-Act-classified high-risk AI
  systems with documented FRIA and human oversight mechanisms?

### Leads to follow up

- [ ] Locate ZenDiS Open-Source-Beschaffungs-Leitfaden (2023) full PDF; add as [53]
- [ ] Check EU Digital Identity Wallet (EUDIW) ARF compatibility with eCH-based Swiss E-ID
- [ ] Find 3 Swiss municipalities (<20,000) with documented open-source transitions
- [ ] Locate published BundID uptake statistics (BMI quarterly report)
- [ ] Identify academic AI fairness literature applicable to Annex III EU AI Act cases
- [ ] Check OSOR Annual Report 2024 when published (expected Q1 2027)
- [ ] Locate GAIA-X 2026 implementation review — practical tools vs. policy
- [ ] Review Collabora Online CODE technical documentation for Section 4.3 expansion
- [ ] Contact AKDB re: municipal case study for paper v1.0

### Working hypotheses (updated v0.2.0)

- **H1 (confirmed):** The binding constraint for municipal open-source adoption is not
  technical maturity (sufficient as of 2026) nor cost (favourable on 5-year TCO) but
  political sustainability across election cycles.
- **H2 (confirmed):** Cooperative IT structures (govdigital eG, AKDB, Dataport, TIT,
  Swiss cantonal IT cooperatives) are the most efficient delivery vehicle for
  municipalities under 100,000. Jena (TIT) and the indicative cost model support this.
- **H3 (confirmed):** A phased approach starting with identity (Keycloak) and files
  (Nextcloud + LibreOffice) gives the fastest path to demonstrable wins at lowest
  disruption risk.
- **H4 (updated):** The EU regulatory environment (EMBAG, OZG 2.0, Interoperable Europe
  Act, NIS2, EU Data Act, EU AI Act, CRA) will make proprietary, vendor-locked municipal
  IT legally problematic within 3–5 years — shorter than originally estimated in v0.1.0.
  The AI Act's high-risk classification of citizen-affecting AI systems creates an
  additional compliance imperative favouring auditable open-source systems.
- **H5 (new):** Open-source AI (Ollama + AnythingLLM + OpenWebUI) will become a standard
  layer of the municipal technology stack by 2028, primarily driven by EU AI Act
  compliance pressure (need for auditable, transparent systems) rather than pure
  cost-efficiency arguments.

---

## 2026-06-20 — Initial research round

### Key findings

**1. EMBAG is the strongest legislative mandate globally.** Switzerland's EMBAG (SR
172.019, in force 2024-01-01) requires open-source release *by default* with a narrow
security exception — stronger than comparable French, Italian, or German federal law.
Municipal implementation guidance is still being developed by cantons.

**2. OpenDesk is the reference implementation for German municipalities.** Managed by
ZenDiS GmbH des Bundes, OpenDesk bundles Nextcloud + Cryptpad + OpenProject + Jitsi +
Element + Collabora. It is the most operationally complete reference for German
municipalities. Need current version number and deployment statistics.

**3. Sovereign Cloud Stack is production-ready but adoption is early.** SCS is technically
mature (OpenStack + Kubernetes + Ceph). Most German Länder are in pilot/evaluation as of
mid-2026. Municipalities should plan on SCS-certified hosters first, not self-hosting.

**4. BundID adoption is the key bottleneck for German OZG progress.** Citizen adoption is
growing but still low relative to target. Municipalities should design Keycloak
federations supporting both BundID and simpler fallback flows with upgrade paths.

**5. Decidim governance is a transferable pattern.** A multi-stakeholder association with
a published social contract is itself a model for municipal open-source communities. The
Canton of Schaffhausen deployment merits a case study.

**6. Munich LiMux failure was political, not technical.** Post-mortems consistently cite
(a) 2014 political shift; (b) insufficient end-user training; (c) state-level
interoperability problems (ODF support). The software worked. Validates political risk as
the primary concern.

**7. French Gendarmerie/state migration provides TCO evidence.** The Gendarmerie
Nationale migrated ~85,000 desktops to Ubuntu/LibreOffice (2008–2014), reporting ~40%
cost savings; the French state runs Tchap (Matrix) for government communication. Real,
large-scale data points confirmed and integrated in v0.2.0.

### Open questions (from v0.1.0 — now partially resolved)

- **Q1 (resolved):** BundesMessenger is on Matrix; specific deployment statistics still
  unavailable from public sources. Federal agencies participating, some Länder piloting.
- **Q2 (resolved):** Swiss eID now operational. New system based on SSI. Integration with
  Keycloak via OpenID Connect confirmed.
- **Q3 (resolved):** eCH standards exist and are documented (eCH-0007, eCH-0011,
  eCH-0020, eCH-0058). Added as [15].
- **Q4 (open):** SCS-certified cloud operators and pricing — not publicly documented;
  requires direct inquiry to plusserver, OSISM, govdigital eG.
- **Q5 (resolved):** ZenDiS framework contract for OpenDesk accessible to municipalities
  via coordinating state authority.
- **Q6 (resolved):** Interoperable Europe Act creates direct obligations for all EU
  public administrations including municipalities, with interoperability assessments
  required for new IT systems.
- **Q7 (open):** GAIA-X — still primarily policy and architecture; practical tools for
  municipalities remain limited in 2026.
