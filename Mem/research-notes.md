# Research Notes — City GovTech Strategy

**Version:** 0.2.0  
**Last updated:** 2026-06-20

Append-only working document for findings, open questions, hypotheses, and leads. Add new
entries at the top.

---

## 2026-06-20 — v0.2.0 research round

### Key findings

**1. CONSUL adds important geographic diversity to the participatory democracy stack.**
CONSUL Democracy (Madrid) and Decidim (Barcelona) represent complementary traditions:
CONSUL emphasises participatory budgeting and direct democracy mechanisms; Decidim
emphases participatory processes and multi-stakeholder governance. Both are AGPL-3.0 and
have 40+ country deployments. Municipalities should evaluate both and choose based on
primary use case. CONSUL: https://consuldemocracy.org

**2. CryptPad fills the high-security collaboration niche.** For documents containing
schützenswerte Daten (protected data under nDSG/DSGVO), CryptPad’s E2E encryption
architecture provides structural guarantees that standard Nextcloud/Collabora cannot.
NGI0-funded; XWiki SAS provides commercial support. Key for medical data, social services,
legal affairs. Score: 30/35.

**3. OpenSlides has a clear governance niche with no strong open-source alternative.**
No other mature OSS product targets the specific workflow of council/parliament management
(Tagesordnung, Anträge, Redelisten, Abstimmungen, Protokolle). OpenSlides is
community-funded via Intevation GmbH; municipalities should consider contributing upstream.
Bundestag committee use is a significant credibility signal.

**4. Forgejo’s community-first governance model is the key differentiator from GitLab CE.**
Forked from Gitea after governance concerns; Codeberg e.V. provides the foundation.
For municipalities committed to full open governance, Forgejo’s governance structure is
more transparent than GitLab CE’s dual-licensing model. GitLab CE is better for large
CI/CD pipelines. Functional equivalence for most municipal use cases.

**5. The Swiss eID architecture (SSI + W3C VC) is forward-compatible with EU eIDAS 2.0.**
BGEID implements a self-sovereign identity model using W3C Verifiable Credentials and
OpenID4VP, which aligns with the EU European Digital Identity Wallet (EUDI Wallet)
architecture. Municipalities implementing Keycloak with OIDC support will be
eID/EUDI-ready by design. Timeline: Swiss eID expected ca. 2026–2027; EUDI Wallet 2024+.

**6. eCH standards are more ‘voluntary’ in letter but mandatory in practice.**
eCH standards are formally voluntary (not statutory), but cantonal IT regulations
frequently reference them as binding technical norms. eCH-0059 (accessibility) and
eCH-0229 (document management) are the most relevant for municipalities. eCH.ch
publishes quarterly updates; changes are retroactively incorporated into cantonal law.

**7. EU Data Act 2023 creates new switching rights relevant to cloud procurement.**
Art. 23–35 EU Data Act establish mandatory data portability and cloud-switching rights,
enforceable from September 2025. Municipal cloud contracts signed after this date must
include data portability clauses. OSS stacks self-hosted on SCS are structurally compliant
because the municipality retains full data control.

**8. TCO evidence strengthens but needs a DACH-specific study.**
Blind et al. (EC 2021) [8] provides the strongest large-sample evidence (14 EU agencies,
32–57 % savings). The French Gendarmerie migration (72,000 desktops, ~40% saving) is
the most cited real-world data point. No equivalent DACH-specific municipal study exists.
This is the most valuable missing piece for political arguments at the municipal level.

### Open questions (updated)

- **Q1:** BundesMessenger deployment count in German federal agencies as of mid-2026?
  Any Bundesländer extending Matrix to municipal services?
- **Q2:** Swiss eID timeline: when will cantonal services accept it? Keycloak federation
  roadmap?
- **Q3 (resolved):** eCH standards catalogue confirmed. eCH-0059, eCH-0229 most relevant.
- **Q4:** Current SCS-certified cloud operators and their municipal pricing?
- **Q5:** ZenDiS/OpenDesk framework agreement — can non-federal entities (Bundesländer,
  municipalities) access OpenDesk directly, or only via Länder procurement?
- **Q6 (resolved):** Interoperable Europe Act applies to all Member State public bodies,
  including municipalities, for digital services provided to public bodies and citizens.
- **Q7 (resolved):** GAIA-X — primarily a policy/certification framework as of 2026;
  SCS is the operational implementation. Municipalities should select SCS-certified
  hosters, not engage directly with GAIA-X.
- **Q8 (new):** OpenDesk v2.x deployment statistics — how many German federal users?
  Timeline for Bundesländer onboarding?
- **Q9 (new):** What municipal-size threshold triggers NIS2 critical infrastructure
  obligations? Is water/energy supply IT in scope for all municipalities or only above
  a population threshold?

### Leads to follow up

- [ ] Contact Decidim Association re: Schaffhausen case study (ongoing from v0.1.0)
- [ ] Pull openCode.de stats: repo count, most-reused OZG components
- [ ] Commission or identify DACH-specific municipal TCO study
- [ ] Locate OSOR Annual Report 2024 PDF; update [5] in source registry
- [ ] Verify BSI guidance on NIS2 municipal scope (Q9 above)
- [ ] Contact ZenDiS re: OpenDesk municipal access framework (Q5 above)
- [ ] Identify 3 municipalities <50,000 with completed OSS transitions for v0.3.0 case studies
- [ ] Contact Intevation GmbH re: OpenSlides adoption statistics and roadmap
- [ ] Confirm DVS (Digitale Verwaltung Schweiz) URL and 2024–2027 strategy document [64]
- [ ] Locate specific BfDI cloud guidance publication [60]

### Working hypotheses (updated)

- **H1 (confirmed):** The binding constraint for municipal OSS adoption is political
  sustainability, not technical maturity. LiMux confirms (political reversal despite
  technical success). The Munich case is the clearest evidence.
- **H2 (confirmed):** Cooperative IT structures (govdigital eG, AKDB, Dataport) are
  the most efficient delivery vehicle for municipalities < 100,000.
- **H3 (confirmed):** Phased approach starting with IAM (Keycloak) + DMS (Nextcloud)
  gives fastest path to demonstrable wins at lowest disruption risk. Supported by
  OpenDesk architecture (same starting stack).
- **H4 (strengthened):** EU regulatory environment makes vendor-locked municipal IT
  legally problematic within 5–7 years. EU Data Act switching rights (2025),
  Interoperable Europe Act (2024), EMBAG (2024), OZG 2.0 (2024), NIS2 (2024 impl.)
  form a coherent regulatory tide toward open, interoperable infrastructure.
- **H5 (new):** The SSI/W3C VC architecture of the Swiss eID and EU EUDI Wallet creates
  a medium-term forcing function: municipalities that implement Keycloak with OIDC today
  will be able to integrate the eID/EUDI Wallet with minimal rework; those locked into
  proprietary IAM will face significant integration costs.

---

## 2026-06-20 — Initial research round (v0.1.0)

### Key findings

**1. EMBAG is the strongest legislative mandate globally.** Switzerland’s EMBAG (SR
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

**4. BundID adoption is the key bottleneck for German OZG progress.** Citizen adoption
is growing but still low relative to target. Municipalities should design Keycloak
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

### Open questions (v0.1.0)

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

### Leads (v0.1.0)

- [ ] Contact Decidim Association re: Schaffhausen case study
- [ ] Pull openCode.de stats: repo count, most-reused components
- [ ] Find an independent (non-vendor) government-software TCO methodology
- [ ] Locate OSOR Annual Report 2023 PDF; add to source registry
- [ ] Check status of Interoperable Europe Act implementing acts
- [ ] Contact KoSIT re: XÖV relevance for small municipalities
- [ ] Identify 3 municipalities <50,000 with completed OS transitions

### Working hypotheses (v0.1.0)

- **H1:** The binding constraint for municipal OSS adoption is political sustainability.
- **H2:** Cooperative IT structures are the most efficient delivery vehicle for
  municipalities < 100,000.
- **H3:** Phased approach starting with identity + files gives fastest demonstrable wins.
- **H4:** EU regulatory environment will make proprietary, vendor-locked municipal IT
  legally problematic within 5–7 years.
