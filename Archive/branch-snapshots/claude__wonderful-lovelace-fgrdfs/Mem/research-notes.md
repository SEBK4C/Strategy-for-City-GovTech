# Research Notes — City GovTech Strategy

**Version:** 0.2.0
**Last updated:** 2026-06-21

Append-only working document for findings, open questions, hypotheses, and leads. Add new
entries at the top.

---

## 2026-06-21 — v0.2.0 research round (quarterly update Q1)

### Key findings

**1. ZenDiS is now the central actor for German municipal digital sovereignty.**
Founded December 2022 by BMI. Manages OpenDesk (officially launched end of 2024) and
openCode.de. OpenDesk available as SaaS from ZenDiS for public administrations.
Targeting marketing licence tenders Q1 2026. Represents the institutional bridge between
federal policy (BMI) and municipal implementation. Key for any German municipality
procurement strategy.

**2. BundID stats are better than the narrative suggests — but still early.**
~5.3M active accounts by end 2024; ~6M by March 2025; 154k new accounts/month since May 2025.
Monthly logins doubled 2024→2025 to 2M/month. But: only 7.5% of 72M eligible citizens registered.
OZG progress: only 196/575 state services nationwide by early 2025 (<34%). Federal completed
its 115 prioritized services by end 2024. Municipal services lag state services significantly.
Design: municipalities should federate Keycloak with BundID AND provide simpler fallback flows.

**3. Swiss eID is now law and rolling out.**
E-ID Act passed Parliament December 20, 2024. Approved by Swiss voters September 28, 2025
(50.39% in favour — close vote, unlike 2021 rejection at 64.4%). Key difference from 2021:
state-managed, no central data storage. Budget: CHF 182M (2023–2028). Public beta started
early 2025. Target: summer 2026 rollout. E-ID federation target for Keycloak Swiss
municipality deployments. Cantons will offer digital driving licence (mDL-Suisse) via
federal wallet after e-ID launch.

**4. eCH standards are the Swiss equivalent of XÖV — and they matter for municipalities.**
eCH-0007 (municipal directory), eCH-0010 (postal address), eCH-0044 (person identification),
eCH-0058 (delivery interface), eCH-0211 (building application). Canton of Zurich uses
eCH-0211 to enable data exchange between municipalities and canton, preserving autonomous
business processes. Standards are recommendations by default but can be declared binding by
authorities. Federal Chancellery references eCH standards as mandatory framework for
Swiss e-government.

**5. CONSUL Democracy complements Decidim with different geographic reach.**
250+ deployments, 45 languages, 100M+ citizens. CONSUL stronger in Spanish-speaking world
and South America; Decidim stronger in Northern Europe. Both AGPL-3.0. CONSUL Democracy
Foundation (2019) ensures maintenance after Madrid City Council support declined. EU OSOR
has a case study. For Swiss/German municipalities: Decidim is the primary recommendation
(better i18n for German, Finnish, French), CONSUL is a valid alternative especially for
trans-national collaboration with Southern European partners.

**6. GovStack provides a building-block reference architecture for procurement.**
ITU/DIAL/BMZ/Estonia initiative. 9 building block specifications: payments, registries,
identification, digital messaging, information mediation, consent, e-signature, GIS,
scheduling. Applied in Montenegro (Dec 2024: 25 local self-governments), Rwanda, Kenya,
Ethiopia. For Swiss/German municipalities: GovStack provides a procurement reference
framework even if the primary stack recommendations remain SCS + Keycloak + Nextcloud + etc.

**7. TCO evidence is now solid for desktop/productivity — still weak for full stack.**
French Gendarmerie GendBuntu: 40% TCO reduction, €2M/year (103,164 workstations by June 2024).
Toulouse: €1.8M over 3 years (90% desktops to OSS). 11 French ministries: LibreOffice on
500,000 workstations. Bolzano-Bozen (Italy) desktop migration: main lesson was change
management, not technology. STILL NEEDED: independent TCO study for full municipal
administration stack (identity, document management, workflow, portal, open data). The
desktop TCO data is a starting point but does not cover the full picture.

**8. EU Data Act is in application from September 2025 — smart city implications.**
Regulation EU 2023/2854. Municipalities deploying IoT/smart city infrastructure (sensors,
smart meters, connected vehicles, public WiFi) must design data sharing obligations into
those systems. This is distinct from open data obligations (PSI Directive) and adds a
NEW compliance requirement for smart city deployments. Design principle: use open
protocols for IoT data collection from the start to avoid lock-in and simplify Data Act
compliance.

**9. EU Data Governance Act enables data altruism — municipal opportunity.**
Regulation EU 2022/868, applies since September 2023. Municipalities can register as
"data altruism organisations" to enable civic data sharing. European common data spaces
(health, mobility, agriculture, energy, finance) offer data-sharing opportunities for
municipal services. A municipality with CKAN + DCAT-AP infrastructure is well-positioned
to participate.

**10. Fraunhofer IESE confirms municipality-specific OSS barriers.**
2024 research specifically on municipalities. Confirms: political sustainability, skill
gaps, interoperability with Länder systems, and change management are the binding
constraints. Technical maturity is not a barrier. Validates H1 and H2 from v0.1.0.

### Answers to open questions from v0.1.0

**Q1 (BundesMessenger):** Adoption data not publicly quantified in search results.
Known: German federal agencies use it; expanding. Länder pilots known. Exact count TBC.

**Q2 (Swiss eID mid-2026):** E-ID Act now law. Summer 2026 rollout target. Cantons
adopting via federal wallet. Keycloak OIDC federation will be the integration point.

**Q3 (eCH standards):** Answered above. eCH-0007, -0010, -0044, -0058, -0211 are the
most relevant for municipalities.

**Q4 (SCS-certified operators):** Plusserver and OSISM confirmed as SCS-certified.
govdigital eG operates SCS-based cloud. Specific SLAs and municipal pricing TBC via
direct procurement inquiry.

**Q5 (ZenDiS/OpenDesk for non-federal entities):** OpenDesk officially launched as SaaS
end of 2024. Marketing licence tenders targeted Q1 2026. Framework agreement for
municipal access: check ZenDiS directly for current status.

**Q6 (Interoperable Europe Act for municipalities):** Primary obligation falls on
national/federal bodies. Municipalities are affected through national implementation
requirements. Monitoring: check implementing acts in 2026.

**Q7 (GAIA-X for municipalities):** Still primarily policy framework. Practical tools
for municipalities limited. Focus remains on SCS as the concrete implementation.

### New open questions (v0.3.0 targets)

- **Q8:** What is the status of the BundesMessenger deployment across German Länder and
  municipalities as of 2026? Any framework agreement for municipal adoption?
- **Q9:** Current deployment count for OpenDesk among German municipalities? Any case
  studies from early adopters?
- **Q10:** Swiss cantonal e-government strategies — which cantons have explicit open-source
  mandates? (Bern, Basel, Zurich, Geneva?)
- **Q11:** What are the specific eCH standards that are mandatory (not just
  recommendations) for Swiss municipalities by 2026?
- **Q12:** Academic post-2022 literature on "platform government" and "data spaces" in
  municipal context — what's the state of the field?
- **Q13:** Is there an EU-level procurement framework for open-source municipal IT?
  (The ISA² programme and Joinup may offer resources.)

### Leads to follow up (v0.3.0)

- [ ] Contact ZenDiS re: OpenDesk municipal pricing and framework agreements
- [ ] Retrieve OSOR Annual Report 2024 when published
- [ ] Systematic search GIQ/ISM/EJEG for post-2022 e-government theory
- [ ] Contact Fraunhofer IESE for full report on municipal OSS adoption
- [ ] Find 2–3 German Gemeinden <20,000 with OpenDesk or Nextcloud case studies
- [ ] Check BSI IT-Grundschutz 2024 edition for any SCS-specific profiles
- [ ] Locate Swiss cantonal e-government strategy documents (especially Bern, Zurich)
- [ ] Find academic literature on GovStack adoption/outcomes
- [ ] Verify Swiss e-ID summer 2026 timeline and municipal integration guide
- [ ] Find CONSUL Democracy Foundation 2024 community statistics

### Working hypotheses (updated)

- **H1 (CONFIRMED):** Fraunhofer IESE 2024 confirms political sustainability is the
  binding constraint. "Personnel resistance to change is the most important factor"
  confirmed by Bolzano-Bozen and Munich cases.
- **H2 (CONFIRMED):** Cooperative IT (govdigital eG, AKDB, Dataport, Finnish shared
  resource model in eVaka) is the efficient vehicle for small municipalities.
- **H3 (CONFIRMED):** Keycloak + Nextcloud first approach validated by Phase 1 structure.
- **H4 (STRENGTHENED):** EU Data Act (Sept 2025 application), NIS2, Interoperable Europe
  Act, Swiss eID (summer 2026), and OZG 2.0 create a dense regulatory fabric that makes
  vendor-locked proprietary stacks increasingly costly to maintain compliance. The 5-year
  window is likely 3–4 years given 2025 application dates.
- **H5 (NEW):** The EfA (Einer für Alle) principle and its Finnish analogue (eVaka's
  shared resource model) represent the optimal architecture for small municipalities:
  participate in shared platforms rather than build own implementations.

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
municipalities. Updated: officially launched end of 2024 as SaaS.

**3. Sovereign Cloud Stack is production-ready but adoption is early.** SCS is technically
mature (OpenStack + Kubernetes + Ceph). Most German Länder are in pilot/evaluation as of
mid-2026. Municipalities should plan on SCS-certified hosters first, not self-hosting.

**4. BundID adoption is the key bottleneck for German OZG progress.** Updated: ~6M
accounts March 2025 but still only 7.5% of eligible citizens. Growth is accelerating.

**5. Decidim governance is a transferable pattern.** A multi-stakeholder association with
a published social contract is itself a model for municipal open-source communities. The
Canton of Schaffhausen deployment merits a case study.

**6. Munich LiMux failure was political, not technical.** Post-mortems consistently cite
(a) 2014 political shift; (b) insufficient end-user training; (c) state-level
interoperability problems (ODF support). The software worked. Validates political risk as
the primary concern.

**7. French Gendarmerie/state migration provides TCO evidence.** GendBuntu: 103,164
workstations by June 2024, 40% TCO reduction, €2M/year savings. Toulouse: €1.8M over
3 years. French state: LibreOffice on 500,000 workstations across 11 ministries.
