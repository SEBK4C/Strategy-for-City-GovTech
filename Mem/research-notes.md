# Research Notes — City GovTech Strategy

**Version:** 0.2.0  
**Last updated:** 2026-06-21  
**Maintainer:** Sebastian Graf, Autonomous Office of Civil Digital Infrastructure  

This document contains working notes, leads, and observations accumulated during
research. It feeds into the source registry and literature review state. Notes here
are informal and may not be fully verified.

---

## Session: 2026-06-21 (v0.2.0 research sprint)

### Key decisions made

1. **Version bump to 0.2.0** (citation-complete draft): all unverified sources from v0.1.0
   have been resolved. Four previously flagged as "unverified" (IDs 6, 9, 16, 43) are now
   confirmed against primary sources.

2. **EU AI Act treatment**: The AI Act is directly cited (as [50]) and receives a dedicated
   subsection in the literature review (Section 3.7). The Annex III high-risk classification
   for automated public administration decisions is central to Section 4.13 (AI Services)
   and Section 7.4 (AI risks).

3. **GovStack added**: The GovStack initiative (ITU/DIAL, [48]) is important because it
   provides a global reference architecture that validates the layered stack approach and
   aligns with the EIF. Its building-block definitions are technology-agnostic but largely
   map 1:1 to the components recommended in Section 4.

4. **TCO evidence**: The two primary sources are the Munich LiMux post-mortem [59] and the
   French DINUM report [60]. Both support the open-source case but neither is a
   methodologically rigorous comparative TCO study. The v0.2.0 TCO section (3.8) is honest
   about this limitation and provides an indicative cost matrix instead.

5. **Small municipality cases**: Three cases documented (Schaffhausen, Herrenberg,
   Gummersbach). All confirmed via public sources. No longitudinal data available beyond
   initial reporting. Need to expand to 5+ cases for v1.0.

### Sources investigated but not yet registered

| Source | Status | Notes |
|---|---|---|
| EU Cyber Resilience Act (CRA) | Investigated; not yet registered [64] | CRA applies to products with digital elements; SBOM mandates directly relevant. Final text adopted 2024. Add to v1.0. |
| EUCS (ENISA cloud scheme) | Investigated; not yet registered [65] | EUCS high-assurance level relevant to SCS certification. Delayed; target 2026. Monitor. |
| eIDAS 2.0 ARF (Architecture Reference Framework) | Investigated; not yet registered [67] | EC published ARF v1.4 in 2024. EUDI Wallet pilots ongoing. Add when pilots complete. |
| OpenDesk v2.x release notes | Investigated | OpenDesk v2 announced mid-2025. ZenDiS has not yet published full technical specs. Monitor. |
| Austrian Gemeinde open-source initiatives | Investigated | Austria has no national OZG equivalent; digital government fragmented. No significant open-source municipal cases found. |
| OSOR Annual Report 2023 | Searched | Report exists on joinup.ec.europa.eu; not individually registered yet. Add as [68]. |

### Technical notes

**Keycloak / BundID federation:** The BundID OIDC interface is documented at
https://id.bund.de but access requires government registration. The public documentation
confirms OIDC 1.0 and confirms compatibility with Keycloak federation. Relevant for
Section 4.1.

**SCS operator list:** Certified SCS operators as of mid-2026: plusserver, OSISM,
artcodix. The SCS certification programme (managed by OSBA/SCS Community) maintains the
official list at scs.community/de/cloud. Relevant for Section 4.9.

**Decidim canton of Schaffhausen:** The deployment is documented in a public press
release from the Kanton Schaffhausen (2020) and referenced in Decidim Association
communications. CHF 30,000/year figure from cantonal IT budget information. Needs
confirmation via direct contact with cantonal IT department for v1.0.

**Herrenberg open-source transition:** Referenced in multiple German-language
newsources (Heise Online, Golem, kommunalwiki.de) 2018-2021. The €40,000/year savings
figure is from a 2021 Heise Online interview with the IT lead. Needs primary source
confirmation for v1.0.

**DINUM TCO figures:** The €150 million savings figure over 4 years and €80 million
implementation cost appear in multiple secondary sources (ZDNet France, LeMonde
Informatique) citing DINUM presentations. The primary DINUM publication URL
(numerique.gouv.fr/publications) hosts multiple documents; the specific report needs
identification and archival for v1.0.

### Architecture notes

**Reference architecture (v0.2.0)** adds three new layers vs. v0.1.0:
- AI Assistance Layer (between Service and Collaboration layers)
- Data Integration Layer (between Collaboration and Identity layers)
- Monitoring and Observability Layer (between Identity and Infrastructure layers)

This 8-layer architecture better reflects the operational complexity of a production
municipal stack and provides clearer separation of concerns for procurement and
operations documentation.

**OpenSearch vs. Elasticsearch:** OpenSearch is the recommended choice over
Elasticsearch because (a) OpenSearch is Apache 2.0 licensed; (b) Elasticsearch changed
to SSPL in 2021, which is not an OSI-approved licence; (c) AWS-managed OpenSearch
providers exist as alternatives to self-hosting.

### Language notes (German translation)

Key terminology decisions for the German translation (v0.2.0):

| English term | German rendering | Rationale |
|---|---|---|
| Digital sovereignty | Digitale Souveränität | Established German policy term |
| Sovereign cloud | Souveräne Cloud | Follows BMI/SCS usage |
| Total cost of ownership | Gesamtbetriebskosten (TCO) | Standard German IT term |
| Software Bill of Materials | Software-Stückliste (SBOM) | BSI uses both terms |
| Single sign-on | Single Sign-On (SSO) | Untranslated; universal in German IT |
| Building blocks (GovStack) | Bausteine | Established translation in German GovStack docs |
| Open-source champions | Open-Source-Meister | Used by ZenDiS documentation |
| Change management | Change Management | Adopted as loanword in German public sector |

---

## Open questions for v1.0

1. **Swiss E-ID integration architecture**: How will cantonal services integrate with the
   Swiss E-ID once it enters operation? Is a Keycloak-to-E-ID OIDC bridge planned? Contact:
   Bundesamt für Justiz (EJPD) or Schweizerische Post (E-ID implementer).

2. **AI Act conformity assessment timeline for municipalities**: What is the expected
   timeline and cost of an AI Act Annex III conformity assessment for a typical municipal
   AI deployment? Who conducts assessments? Are notified bodies designated yet?

3. **GAIA-X Label adoption**: How many SCS-certified operators have also obtained the
   GAIA-X Label? Is the Label required or just desirable for municipal procurement?

4. **Herrenberg primary source**: Can we obtain the original 2021 Heise Online interview
   or a direct statement from the Herrenberg IT department confirming the €40,000/year
   savings figure?

5. **Decidim Schaffhausen CHF 30,000 figure**: Primary source confirmation needed.
   Contact: Staatskanzlei Kanton Schaffhausen (staatskanzlei@ktsh.ch).

---

## Quarterly review schedule

| Review date | Version target | Status |
|---|---|---|
| 2026-06-20 | v0.1.0 | ✅ Completed |
| 2026-06-21 | v0.2.0 | ✅ Completed |
| 2026-09-21 | v0.3.0 | Scheduled |
| 2026-12-21 | v0.4.0 | Planned |
| 2027-03-21 | v1.0.0 | Target |
