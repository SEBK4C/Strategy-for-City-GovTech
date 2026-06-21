# Research Notes — City GovTech Strategy

**Version:** 0.2.0
**Last updated:** 2026-06-21

Append-only working document for findings, open questions, hypotheses, and leads. Add new
entries at the top.

---

## 2026-06-21 — Citation verification and v0.2.0 gap-fill

### Research decisions made

**1. CELEX number for Interoperable Europe Act confirmed as 32024R0903.**
The regulation's official CELEX in the EUR-Lex system is 32024R0903. This is the binding
identifier used in citations [6] across the paper.

**2. FITKO URL corrected to https://www.fitko.de/fitko.**
The earlier draft used a stale URL. The canonical homepage is fitko.de/fitko.

**3. E-Government Strategy Switzerland URL corrected.**
Canonical URL is https://www.egovernment.ch/de/umsetzung/e-government-strategie-2024-2027/.
The earlier draft used a different path on the same domain.

**4. BAR (Swiss Federal Archives) URL verified.**
Source [43] confirmed at https://www.bar.admin.ch/bar/de/home/recherche/suchen/hilfsmittel-findbuecher/gever-bundesverwaltung.html.

**5. eIDAS 2.0 CELEX confirmed as 32024R1183.**
The amending regulation (EU 2024/1183) has CELEX 32024R1183. Added as new source [40]
alongside the original eIDAS Regulation [1a/existing].

**6. Economic analysis approach for Section 3.6.**
In the absence of an independent municipal TCO study, the analysis synthesises:
- French Gendarmerie Ubuntu/LibreOffice migration (~40% cost savings, 72,000 desktops)
- Microsoft 365 Business Standard licence cost benchmark (€12.50/user/month)
- Swiss federal GEVER procurement as a reference point
- Vendor lock-in quantification: 15–40% licence renewal premium as proxy metric
The 5-year TCO model (€560K–€1.47M open-source vs. >€1.5M proprietary for a 500-person
municipality over 36 months) is an indicative range, not a peer-reviewed study.
This must be flagged as such in v0.3.0 and replaced with an independent methodology.

**7. GovStack framing adopted for Section 3.7.**
GovStack (ITU/DIAL) provides the cleanest globally applicable framing for government
digital building blocks. Added as source [28]. The Decidim €75M Barcelona figure comes
from Decidim Association reporting (verify against primary for v0.3.0).

**8. Technology scoring rubric formalised.**
7 criteria × 5-point scale = max 35 points. Minimum procurement threshold set at 27/35
(= 77%), derived from a minimum acceptable score of 3/5 on every criterion.
Scorecard results: Keycloak 34/35, Nextcloud 34/35, Decidim 33/35, Matrix/Element 32/35,
CKAN 32/35, SCS 32/35, TYPO3 32/35, OpenProject 29/35, Camunda Community 29/35.
All nine components exceed the 27/35 threshold.

**9. Appendix B procurement clauses are illustrative, not legal advice.**
The four verbatim clauses (open-source release obligation, interoperability, data
sovereignty, exit rights) are model language inspired by German public procurement
practice and the FSFE "Public Money? Public Code!" campaign. They must be reviewed
by legal counsel before use in actual contracts.

### Open questions for v0.3.0

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
- **Q8:** Decidim €75M Barcelona figure — verify against primary source (Decidim
  Association annual report or Barcelona City Council budget documents).
- **Q9:** French Gendarmerie cost savings — locate original primary source (DINSIC/ANSSI
  report or peer-reviewed citation).

### Leads to follow up

- [x] Pull CELEX for Interoperable Europe Act — confirmed 32024R0903
- [x] Verify FITKO URL — corrected
- [x] Verify E-Government Strategy Switzerland URL — corrected
- [x] Locate OSOR Annual Report 2023 — added as source [18]
- [x] Add eCH standards to source registry — added as [15]
- [x] Add ZenDiS to source registry — added as [17]
- [x] Add GovStack to source registry — added as [28]
- [x] Add CONSUL Democracy to source registry — added as [31]
- [x] Add Lathrop & Ruma (2010) to source registry — added as [32]
- [x] Add OpenTofu to source registry — added as [38]
- [x] Add eIDAS 2.0 to source registry — added as [40]
- [ ] Contact Decidim Association re: Schaffhausen case study (primary data)
- [ ] Find an independent (non-vendor) government-software TCO methodology
- [ ] Check status of Interoperable Europe Act implementing acts (2025/2026)
- [ ] Contact KoSIT re: XÖV relevance for small municipalities
- [ ] Identify 3 municipalities <50,000 with completed OS transitions
- [ ] Locate French Gendarmerie cost savings primary source
- [ ] Locate Decidim €75M Barcelona primary source
- [ ] Pull openCode.de stats: repo count, most-reused components (as of Q3 2026)

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
large-scale data points for economic analysis.

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
