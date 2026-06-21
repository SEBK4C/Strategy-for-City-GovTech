# Research Notes — City GovTech Strategy

**Project:** Open-Source Municipal Government Technology Strategy  
**Version:** 0.2.0  
**Last updated:** 2026-06-21  

---

## Session: 2026-06-21 — v0.2.0 Research Sprint

### Key findings from deep research

**EMBAG (Switzerland):**
- In force January 1, 2024. Key articles: Art. 3 (digital by default), Art. 9 (OSS mandate), Art. 10 (open data), Arts. 12–15 (standards)
- Applies to all federal software developed with public funds; exceptions for security/third-party rights
- Places Switzerland among most progressive OSS-mandating jurisdictions globally
- Camptocamp (Swiss tech firm) has written analysis of EMBAG impact on OSS vendors

**OZG 2.0 (Germany):**
- In force July 24, 2024 (voted Bundestag February 2024)
- Key change: mandatory OSS preference for federal procurement; enhanced monitoring (3-year scientific review)
- By end 2023 only 81/581 services digitised — stark implementation lag
- DeutschlandID replacing/expanding BundID; citizens entitled to digital services from 2029
- OSOR article confirms: OZG 2.0 "favors open source solutions" with binding procurement language

**Sovereign Cloud Stack:**
- BMWK project funding ended December 2024
- R8 released April 9, 2025 — ScaleUp Technologies newest operator; 6+ production operators
- GovStack cloud spec integrated with SCS
- SLURP upgrade flexibility = skip-level update process (major operational improvement)

**Deutsche Verwaltungscloud:**
- Symbolically launched March 2025 at IT Planning Council conference
- Jointly led by govdigital eG and FITKO
- Enables cross-location application deployment and national sharing via openCode.de

**ZenDiS / OpenDesk:**
- Founded December 2022
- Three pillars: openCode (platform), openDesk (product), Sovereignty Check (advisory)
- OpenDesk v1.0: October 20, 2024
- OpenDesk v2.0 with mobile app: targeted September 2025
- 100,000+ users by June 2025
- BWI (Bundeswehr IT): 7-year contract April 2025
- Robert Koch Institute / Federal Ministry of Health (7,000 users): announced June 2025
- "Sovereignty Check" tool: evaluates IT solutions using transparent sovereignty criteria

**Deutschland-Stack:**
- Emerged from 2025 coalition agreement
- Federal Ministry for Digital Affairs and State Modernization responsible
- Full rollout target: 2028
- Integrates: OpenDesk + SCS + DVC + X-Road interoperability
- Nextcloud's "Impulspapier" from Schleswig-Holstein contributed to concept

**BundesMessenger:**
- BWI launched December 2023 (expansion of BwMessenger from 2021)
- Built on Matrix protocol + modified Element client
- Source code on openCode.de
- Features: E2E encryption, BYOD, built-in malware scanning, data on own servers
- Dataport planning Matrix deployment for 500,000 users in SH + Hamburg
- Referenced at Matrix Conference 2025 (talk: "The German BundesMessenger")

**Nextcloud:**
- 500,000+ server instances worldwide (2025 wrap-up)
- Customer interest tripled H1 2025 (attributed to US cloud concerns)
- Key 2025 deployments:
  - Austria Federal Ministry of Economy, Energy and Tourism (BMWET)
  - City of Stuttgart
  - Schleswig-Holstein ("Implementation Role Model" award)
  - Île-de-France: 550,000 students and staff on sovereign cloud platform
  - Denmark federal government (standard collaboration platform)
  - France: multiple 6-figure deployments
  - Netherlands: 8x increase in public sector inquiries in 2025
- Enterprise Days planned for Switzerland, Austria, Spain in 2026

**Schleswig-Holstein:**
- April 2024: announced 30,000 PC migration to Linux/LibreOffice/Nextcloud/Thunderbird
- October 2, 2025: completed email migration (40,000+ mailboxes, Exchange → Open-Xchange/Thunderbird)
- 6-month email migration process
- Dataport implementing Matrix for 500,000 users
- Model published: "Impulspapier" for Deutschland-Stack
- Recognized as Nextcloud "Implementation Role Model"

**Munich LiMux:**
- 2003–2017; 14,800 of 29,000 desktops migrated
- By 2012: >€10M savings documented (€4M by March 2012; cumulative including avoided hardware and licence costs)
- 2017 reversal: new mayor, political not technical failure
- Return to Windows: estimated €100M (The Register, 2018)
- OSOR has detailed historical documentation

**TYPO3:**
- >35% of German government websites on TYPO3
- GSB 11 (Government Site Builder 11) launched 2024: federal standard for ministerial and municipal websites
- 54%+ of German university websites on TYPO3
- Rwanda: 250+ government websites on TYPO3 since 2019

**Forgejo / Netherlands:**
- Netherlands OSPO (Ministry of Interior) selected Forgejo for code.overheid.nl
- Soft-launched 2026 as self-hosted sovereign alternative to GitHub/GitLab
- Explicit rationale: "public money, public code"
- MIT-licensed; community-governed fork of Gitea

**Interoperable Europe Act:**
- Regulation (EU) 2024/903
- Adopted March 4, 2024 (Council); in force April 11, 2024; substantive obligations from January 12, 2025
- €77M in Digital Europe Work Programme 2025–27 for implementation
- Establishes Interoperable Europe Board
- Explicitly supports FOSS for achieving interoperability

**AI Act:**
- Regulation (EU) 2024/1689; in force August 1, 2024
- High-risk provisions for public administration AI applicable August 2, 2026
- Public sector AI for citizen decisions: high-risk (conformity assessment, registration, human oversight)
- French "Albert" AI: open-source models on sovereign infrastructure = compliance-forward
- Open-source AI: code/weight auditability = structural compliance advantage

**BSI IT-Grundschutz++ / NIS2 Germany:**
- NIS2 Implementation Act (Germany): in force December 5, 2025
- BSI IT-Grundschutz++ catalogue: released January 1, 2026
- Mandatory for federal agencies and publicly organised IT service providers
- New methodology = "state of the art" as required by NIS2 Implementation Ordinance

**EU Funding:**
- Digital Europe Programme: €8.1B total
- NGI (Next Generation Internet) within Horizon Europe: €5K–50K grants for OSS code enhancement
- Every €1 in OSS = at least €4 economic value (European Commission estimate)
- Sovereign Tech Fund Germany: €17M/year; €23.5M cumulative in 60+ projects
- TSI (Technical Support Instrument): advisory support, no co-financing required

---

## Open questions for v0.3.0

1. What are the actual measured TCO figures from Schleswig-Holstein's migration? (Migration in progress; final figures expected 2026–2027)
2. Is there a peer-reviewed comparison of citizen satisfaction with Decidim vs. non-participatory processes?
3. What is the current state of Swiss eID rollout to cantonal/municipal level?
4. Are there published API compatibility guidelines for Keycloak ↔ Swiss eID integration?
5. What are the specific eCH standards for document management (eCH-0160 details)?
6. Which Swiss cantons have adopted EMBAG-aligned open-source policies?
7. What is the status of OZG 2.0 implementation as of Q2 2026 (target: find dashboard or report)?
