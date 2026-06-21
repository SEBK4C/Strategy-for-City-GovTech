# Research Notes — City GovTech Strategy

**Project:** Open-Source Municipal Government Technology Strategy  
**Maintainer:** Sebastian Graf, Autonomous Office of Civil Digital Infrastructure  
**Last updated:** 2026-06-21

This file captures research findings, open questions, and hypotheses that inform
the strategy paper but are not directly cited. It is a working document, not a
publication. Findings here feed into future paper revisions and literature review
updates.

---

## Research Round 1 — v0.1.0 (June 2026-06-20)

### Key findings

1. **EMBAG is the strongest single legislative driver in Europe.** Unlike the OZG (which creates service delivery obligations) or the Interoperable Europe Act (which creates interoperability obligations), EMBAG directly mandates open-source publication. This is qualitatively different and stronger.

2. **SCS is production-ready but adoption is concentrated.** As of mid-2026, SCS deployments are real but primarily in Germany. The Swiss public-sector cloud market is still fragmented between proprietary hyperscalers and cantonal IT bodies. No Swiss canton has formally adopted SCS, though OSBA has Swiss members.

3. **The cooperative model (govdigital, Dataport) is the key procurement unlock.** The reason most municipalities cite procurement complexity as a barrier is that they're trying to run individual tenders. Cooperative procurement eliminates this for most stack components.

4. **Decidim community management is as important as the software.** Multiple deployment reports emphasise that citizen engagement quality depends heavily on the facilitation process, not just the platform.

5. **Munich LiMux is widely cited but poorly understood.** The primary post-mortem documents are in German city council archives and not easy to access in English. Most English-language accounts are secondary. This is a source quality issue.

### Open questions (v0.1.0)

- What is the current state of Swiss cantonal SCS adoption discussions?
- Is there a systematic comparison of eCH and XÖV compliance requirements for cross-border municipalities?
- How many German municipalities have successfully completed a full proprietary-to-OSS transition vs. partial/hybrid?
- What percentage of openCode.de repositories are actively maintained vs. archived?

---

## Research Round 2 — v0.2.0 (2026-06-21)

### Key findings

1. **GovStack provides the best internationally recognised classification framework.** The GovStack building-blocks taxonomy is well-aligned with EU interoperability frameworks and gives municipal procurement teams a vendor-neutral vocabulary for specifying requirements. Citing it also future-proofs the paper against international applicability questions.

2. **EU AI Act risk classification is more nuanced for municipalities than first appears.** Most obvious municipal AI use cases (chatbots for citizen inquiry routing, form pre-population) are arguably NOT high-risk under the current Act text — they do not evaluate persons for access to public services. However, AI-assisted benefits decisions or social service eligibility assessments DO fall in high-risk Annex III. The key municipal compliance action is running a formal classification exercise before any deployment, not blanket avoidance.

3. **The French LibreOffice migration is the best available TCO evidence.** It is the only documented large-scale migration with publicly stated cost savings. The €20M/3yr figure comes from French government communications and is widely cited in FSFE materials, but the primary government document URL needs to be tracked down and verified. The figure should be treated as indicative, not audited.

4. **DCAT-AP 3.0 matters more than usually acknowledged.** Many municipalities underestimate that contributing to national open data portals (opendata.swiss, GovData.de) requires specific metadata schemas. Implementing DCAT-AP 3.0 from the start in CKAN is far easier than retrofitting it later. The GAIA-X angle is also real: GAIA-X data space participants need DCAT-AP-compatible catalogue entries.

5. **ZenDiS is the institutional model to watch.** The OpenDesk programme has demonstrated that a dedicated public body managing the curation layer (selecting, integrating, and quality-assuring open-source components) while leaving upstream maintenance to communities is viable. This is the key institutional design pattern for large-city or Länder-level programmes.

6. **The AI Act open-source provisions (Arts. 53, 102) are genuinely helpful for municipalities.** Open-weight models used in higher-risk contexts (but below the high-risk threshold) benefit from reduced documentation requirements. This creates a concrete advantage for open-source AI over proprietary AI in public administration — proprietary LLMs are black boxes from a compliance perspective.

7. **Case study asymmetry is a real problem.** Successes are reported (Barcelona, Helsinki, French LibreOffice); partial failures or reversals (Munich) are documented but hard to find primary sources for. We have almost no data on projects that were started and abandoned without political fanfare, which is likely the most common outcome. The proposed citizen satisfaction survey (Appendix B) and the community of practice (Section 6.5) are the right mechanisms to build this evidence base.

### Open questions (v0.2.0)

- Has any academic paper formally evaluated GovStack building block compliance for European municipal procurement contexts?
- Is there a systematic registry of CONSUL vs. Decidim municipal deployments in German-speaking countries?
- What is the current status of the Schaffhausen Decidim deployment post-Richtplan consultation?
- Has any municipality run a formally validated TCO comparison using a published methodology? (Distinct from the French Ministry of Interior cost claim, which is a government communication, not an audited cost study)
- What are the FITKO's published targets for BundID adoption rates among German municipalities by 2026?
- Are there documented cases of Swiss cantonal governments migrating away from a major proprietary vendor stack? The Swiss federal EMBAG mandate is well-documented but cantonal implementation varies widely.

### Hypotheses to test (priority order)

1. **H1:** Municipalities that join cooperative IT providers (govdigital, Dataport, cantonal cooperatives) before beginning their open-source transition have significantly higher completion rates than those attempting the transition independently.
   - *Testable by:* Survey of municipalities with >2 years of programme history.

2. **H2:** The 15–20% change management budget recommendation (Section 6.4) is systematically under-funded in actual municipal OSS transition programmes, and this under-funding is a primary predictor of failure or reversal.
   - *Testable by:* Budget analysis of documented transitions (Munich, Barcelona, Helsinki, French state).

3. **H3:** Municipalities contributing upstream code or documentation have lower 5-year TCO than those maintaining private forks, even after accounting for the contribution effort.
   - *Testable by:* Cost accounting study comparing Barcelona (active contributor) with municipalities that forked and diverged.

4. **H4:** Open-source municipal digital services achieve equivalent or higher citizen satisfaction scores compared to proprietary alternatives, when service design quality is controlled for.
   - *Testable by:* Controlled survey study comparing Helsinki (open-source first) with peer municipalities using proprietary stacks.

---

## Methodological notes

### On the scoring matrix (Appendix A)
The seven-criterion weighted scoring matrix is a synthesis of criteria from prior e-government maturity frameworks (Wirtz & Weyerer [7]) and OSS evaluation frameworks (OpenSSF Scorecard, CHAOSS metrics). The weights (licence 20%, deployment maturity 15%, community health 15%, interoperability 15%, security 20%, TCO 10%, public deployments 5%) are informed by the primary failure modes identified in the case studies: licence risk, abandoned projects, poor interoperability, and security incidents. These weights should be treated as illustrative and validated against expert consultation in v0.3.0.

### On TCO estimates (Section 9.4)
All TCO benchmark figures are derived from secondary sources (published case studies, vendor pricing, and the OSOR evidence base). They have not been independently audited. The order-of-magnitude estimates are robust; the exact figures are illustrative. Any municipality using these figures for a procurement business case must run its own validated TCO calculation using local cost data.

### On AI Act compliance (Section 3.8, 4.10)
The AI Act analysis reflects the legislative text as of June 2026 and Commission guidance available at that date. The Act's implementing acts (for high-risk system registration, conformity assessment procedures, etc.) are still being developed by the AI Office. Municipal practitioners should monitor the AI Office guidance portal at https://digital-strategy.ec.europa.eu/en/policies/european-approach-artificial-intelligence for updates.
