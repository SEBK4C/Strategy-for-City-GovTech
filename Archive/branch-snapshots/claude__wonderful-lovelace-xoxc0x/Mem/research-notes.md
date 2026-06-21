# Research Notes — City GovTech Strategy

**Version:** 0.2.0  
**Last updated:** 2026-06-21  

Working notes on sources, debates, and open questions. Not for citation without verification against primary sources.

---

## Key debates in the literature

### 1. TCO: Open source vs. proprietary

The most contested empirical question. Vendor-commissioned studies systematically undercount open-source TCO by including implementation and training costs while excluding proprietary licence escalation, lock-in risk, and migration costs. The most credible independent analysis remains the French government’s LibreOffice migration report (2018, DINUM), which found net savings of €10M over five years for 220,000 workstations.

The Munich LiMux reversal is often cited as evidence of higher TCO for open source, but the Accenture study that triggered the reversal (2015) has been widely criticised as methodologically flawed and conflict-of-interest-tainted. Post-mortems (Grassmuck 2017 [62]) confirm the migration was broadly cost-effective; the reversal was political.

**Open question:** What is the empirically validated per-workstation annual cost differential in the 2024–2026 context, controlling for municipality size, existing IT capacity, and cooperative membership?

### 2. The governance question: platform vs. solution

Decidim’s model — an independent association governing a platform used by hundreds of municipalities — contrasts with city-owned deployments where the city is both operator and primary contributor. The Decidim Association model is more resilient but requires surrender of unilateral control.

Analogously, the Sovereign Cloud Stack’s community governance model (OSBA + operators) differs from proprietary cloud where governance is entirely vendor-controlled.

**Implication for municipalities:** Joining a governed community platform (Decidim Association, SCS community, govdigital eG) provides resilience in exchange for accepting shared governance constraints. This is generally the right tradeoff for municipalities lacking dedicated platform staff.

### 3. The Swiss-German interoperability gap

Swiss eCH standards and German XÖV standards serve equivalent functions but are technically distinct. There is no automatic translation layer. Municipalities near the Swiss-German border (e.g., Constance, Freiburg, Basel-region) face a genuine interoperability challenge when providing cross-border services.

**Opportunity:** This gap is a research and standards gap, not a fundamental technical barrier. A Swiss-German eCH-XÖV mapping project would be a high-value community contribution.

### 4. eIDAS 2.0 / EUDI Wallet implementation uncertainty

The EU Digital Identity Wallet (EUDI) is mandated by the revised eIDAS Regulation (2024), but implementation is proceeding at different speeds across member states. Switzerland is not an EU member but participates in some electronic identification mutual recognition arrangements.

For municipalities: Keycloak’s extensibility means it can be adapted to federate with EUDI Wallets as they become available. The recommended architecture is EUDI-ready without being EUDI-dependent.

### 5. AI in municipal government: the compliance-capability tension

The EU AI Act creates significant compliance overhead for high-risk AI applications in municipal government. However, AI tools that are genuinely useful — document classification, service routing, translation, planning support — are in many cases low-risk or limited-risk under the Act’s classification.

The practical guidance for municipalities: start with low-risk AI tools (chatbots with mandatory AI disclosure, document translation), build compliance infrastructure, and defer high-risk AI deployment until the EU’s standardisation framework (CEN/CENELEC standards referenced in the Act) is mature.

---

## Notable practitioners and community contacts

- **FSFE Brussels office**: campaigns on Public Money? Public Code! policy
- **Joinup (EU)**: maintains OSOR and catalogue of government open-source
- **openCode.de team** (Digitalservice): platform for German government OS
- **ZenDiS communications**: OpenDesk deployment support
- **Decidim Association**: governance, localisation, community
- **OSBA SCS team**: technical support for SCS deployments
- **govdigital eG**: framework contracts and cooperative hosting
- **AKDB (Munich)**: Bavarian municipal IT cooperative
- **Dataport (Hamburg)**: Northern German municipal IT cooperative
- **swisstopo**: Swiss geodata and API access
- **eCH secretariat (Bern)**: standards access and participation

---

## Open questions for v0.3.0

1. What does a full eCH-to-XÖV connector architecture look like? Which open-source projects have built this?
2. Are there documented cases of municipalities using GovStack building blocks in a European context?
3. What is the actual BundesMessenger (Matrix) adoption rate within the German federal administration as of 2026?
4. Has any Swiss canton published post-EMBAG open-source release statistics?
5. What GAIA-X credential certifications do SCS-certified hosters currently hold?
6. Which municipal AI systems have been registered in EU AI Act Article 49 national databases?
7. How does the Flowable BPMN engine compare to Camunda in OZG service implementations?

---

## Methodology notes

- Sources rated “unverified” in the registry should not be cited in the main paper. When upgrading a source to “verified”, confirm: (a) URL resolves to the stated document, (b) publication date is accurate, (c) licence is correctly stated.
- The translation to German is derived from the English source of truth. All German-language technical terms follow the authoritative usage in the BSI IT-Grundschutz Kompendium and the OZG documentation. Swiss-specific terms follow eCH and E-Government Suisse publications.
- The TCO model (Section 8 of the paper) should be treated as indicative until validated against actual municipal procurement data. The methodology is documented in `Scripts/build_govtech_docs.py`.
