# Research Notes — City GovTech Strategy

**Project:** Open-Source Municipal Government Technology Strategy
**Maintainer:** Sebastian Graf, Autonomous Office of Civil Digital Infrastructure
**Last updated:** 2026-06-20

This file is an append-only working log of research decisions, open questions,
and observations accumulated during the strategy development process. It supplements
the structured coverage map in `literature-review-state.md`.

---

## 2026-06-20 — v0.2.0 Research Session

### New sections added

**Section 3.5 — ZenDiS and OpenDesk**
ZenDiS deserves much more prominent treatment than it received in v0.1.0. It represents
a genuinely new institutional model: a publicly funded, government-owned GmbH with an
explicit mandate to maintain open-source workplace software as a public good. This is
different from both (a) proprietary outsourcing and (b) community-maintained software with
no guaranteed support. The model should be studied and potentially replicated at cantonal/
Länder level for municipalities too small to fund it independently. Tracked under [48].

**Section 3.6 — eCH Standards**
The eCH/XÖV parallel is important for Swiss municipalities. Both are XML-based government
interoperability standards; both are mandatory at federal level; both enable competitive
procurement by preventing data-format lock-in. The key difference: eCH standards are
maintained by an association (voluntary coordination); XÖV by KoSIT (mandatory coordination
via federal/Länder coordination body). Neither is inherently superior — the governance model
reflects the different federalism of CH vs. DE.

Key eCH standards relevant to the municipal stack:
- eCH-0014: Framework (the "master standard") — cites and governs all others
- eCH-0011: Person data (Personendaten) — governs how names, birth dates, addresses
             are represented in data exchange. Keycloak must implement this for Swiss eID
             integration.
- eCH-0010: Physical address — governs address data exchange
- eCH-0058: GEVER / records management — governs document lifecycle, retention, archival
- eCH-0046: Electronic communications standard

**Section 3.7 — EU Data Act**
The Data Act is not yet well understood in municipal IT circles. Key insight: it changes the
balance of power in vendor negotiations. Before the Data Act, a municipality wanting to
migrate from a proprietary system had to negotiate data export terms ad hoc. After September
2025, they have a legal right to data portability (Art. 5), cloud switching support (Art. 30),
and open interoperability (Art. 35). Procurement teams should be briefed on these rights.

However, enforcement is still unclear — the regulation is new and no case law exists.
Municipal legal departments should be consulted on how to operationalise Data Act rights
in standard IT contracts.

**Section 3.8 — GovStack**
GovStack's significance is primarily as a normative alignment framework. If the SCS +
Keycloak + CKAN stack is GovStack-compatible, it becomes interoperable with systems
deployed in other countries following GovStack (Estonia, Rwanda, Bangladesh). This matters
for Swiss municipalities with international partnerships and for German federal systems
increasingly referenced by GovStack.

Alignment status (assessed June 2026):
- Keycloak → GovStack Identity BB: HIGH alignment (OIDC + FIDO2)
- CKAN → GovStack Digital Registries BB: MEDIUM alignment (REST API, not full compliance)
- Matrix → GovStack Messaging BB: HIGH alignment (federated, E2E encrypted)
- Camunda → GovStack Workflow BB: MEDIUM alignment (BPMN 2.0 compatible)

### Open research questions

1. What are the actual cost savings documented by the first OpenDesk federal ministry
   deployments? ZenDiS has published some data but I could not verify the exact figures.
   **Action:** Attempt to obtain ZenDiS annual report or press releases with cost data.

2. How does the Swiss eID v2 (relaunched 2024) handle the delegation of attribute
   assertion to cantons? If each canton controls the identity attributes for its residents,
   cantonal systems (including municipal Keycloak deployments) need to implement per-canton
   federation — not just a single federal federation point. This has architecture implications.
   **Action:** Read the e-id.ch technical specification document.

3. What is the current status of BundesMessenger adoption in German federal ministries?
   The 2023 launch was widely reported; 2024/2025 adoption data is less clear.
   **Action:** Check FITKO and ZenDiS publications for BundesMessenger statistics.

4. The Munich LiMux failure is universally cited but I have not found a primary academic
   study (peer-reviewed) that independently analyses the failure. Most references are to
   journalist and blog accounts (including Heise, Golem, and the LiMux Wikipedia article).
   **Action:** Search GIQ and ISM for peer-reviewed analysis of the Munich case.
   If no primary academic source exists, this should be noted in the citation.

5. Is there a public-sector equivalent of the Standish CHAOS Report that tracks
   success/failure rates of open-source vs. proprietary government IT projects?
   If not, this is a significant research gap worth naming explicitly.
   **Action:** Search OSOR archives and academic databases. Note gap explicitly in v0.3.0.

### Technology notes

**Camunda dual-licensing concern:** Camunda shifted to a proprietary licence for Camunda 8
Enterprise features in 2022. The community edition (Apache 2.0) is still fully functional
for most municipal use cases. However, municipalities should be aware that contributions to
Camunda 8 are under CLA and may not flow back as community-licensed features. Flowable
(Apache 2.0 for all features) avoids this concern entirely. For strict open-source
procurement environments, Flowable may be preferable. Both are BPMN 2.0 compliant and
largely compatible at the process model level. This deserves a note in the procurement
template.

**TYPO3 vs. Drupal for Swiss multilingual municipalities:** Swiss municipalities with
German, French, or Italian as official languages (e.g., bilingual cities in cantons BE,
FR, VS) need excellent multilingual CMS support. TYPO3's multilingual architecture
(content inheritance across language trees) is mature and well-tested in DACH environments.
Drupal's multilingual support is also strong but requires more configuration. For purely
German-language Swiss municipalities, TYPO3 is the clear recommendation. For multilingual
municipalities, both are viable — the decisive factor may be available local support.

**SCS for small municipalities:** The Sovereign Cloud Stack is primarily designed for
medium-to-large deployments. A municipality with 10,000 inhabitants is unlikely to run
its own SCS cluster — the minimum reasonable scale is probably a cantonal or Kreis-level
deployment serving dozens of municipalities. This reinforces the cooperative hosting model.
The upcoming SCS "Small Operator" profile may change this calculus.

---

## Pre-v0.1.0 Notes (prior to 2026-06-20)

*[These notes predate the current version structure and have been incorporated into
the main paper where relevant.]*
