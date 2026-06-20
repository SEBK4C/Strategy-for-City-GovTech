# Research Notes — City GovTech Strategy

**Version:** 0.1.0
**Last updated:** 2026-06-20

Append-only working document for findings, open questions, hypotheses, and leads. Add new
entries at the top.

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
Nationale migrated ~72,000 desktops to Ubuntu/LibreOffice (2008–2014), reporting ~40%
cost savings; the French state runs Tchap (Matrix) for government communication. Real,
large-scale data points for v0.2.0.

### Open questions

- **Q1:** Current deployment count for BundesMessenger (Matrix) across German federal
  agencies? Any Länder using it for municipal services?
- **Q2:** Exact status of the Swiss eID as of mid-2026? Which cantonal services accept
  it? How does it federate with Keycloak?
- **Q3:** Is there a formal eCH standard equivalent to XÖV (eCH-0058, eCH-0020,
  eCH-0007)? Which matter most for municipalities?
- **Q4:** Current SCS-certified cloud operators, their SLAs and municipal pricing?
- **Q5:** ZenDiS mandate re: municipal access to OpenDesk — is there a framework
  agreement non-federal entities can use?
- **Q6:** Does the Interoperable Europe Act (2024) create direct obligations for
  municipalities or only national/federal bodies? Implementation timeline?
- **Q7:** Current state of GAIA-X — practical tools for municipalities, or policy only?

### Leads to follow up

- [ ] Contact Decidim Association re: Schaffhausen case study
- [ ] Pull openCode.de stats: repo count, most-reused components
- [ ] Find an independent (non-vendor) government-software TCO methodology
- [ ] Locate OSOR Annual Report 2023 PDF; add to source registry
- [ ] Check status of Interoperable Europe Act implementing acts
- [ ] Contact KoSIT re: XÖV relevance for small municipalities
- [ ] Identify 3 municipalities <50,000 with completed OS transitions

### Working hypotheses

- **H1:** The binding constraint for municipal open-source adoption is not technical
  maturity (sufficient) nor cost (favourable) but political sustainability across
  election cycles.
- **H2:** Cooperative IT structures (govdigital eG, AKDB, Dataport, Swiss cantonal IT
  cooperatives) are the most efficient delivery vehicle for municipalities <100,000.
- **H3:** A phased approach starting with identity (Keycloak) and files (Nextcloud) gives
  the fastest path to demonstrable wins at lowest disruption risk.
- **H4:** The EU regulatory environment (EMBAG, OZG 2.0, Interoperable Europe Act, NIS2)
  will make proprietary, vendor-locked municipal IT legally problematic within 5–7 years.
  Early movers gain compliance capital; late movers accumulate regulatory debt.
