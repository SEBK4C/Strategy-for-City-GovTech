# Research Notes — City GovTech Strategy

**Maintainer:** Sebastian Graf, Autonomous Office of Civil Digital Infrastructure
**Last updated:** 2026-06-21
**Version:** 0.2.0

Working notes, open questions, and leads for improving the strategy papers.
For verified sources, see `Mem/source-registry.md`. For the literature coverage
map, see `Mem/literature-review-state.md`.

---

## Key findings (v0.2.0)

### The regulatory momentum is now structural
EMBAG (CH, 2024), OZG 2.0 (DE, 2024), Interoperable Europe Act (EU, 2024), and
NIS2 (EU transposition 2024) create overlapping legal obligations that push
municipalities toward open standards and auditable infrastructure. This is no longer
a procurement preference — it is compliance. Municipalities delaying transition are
accumulating regulatory risk, not caution.

### The ecosystem has reached critical mass
Three developments converged in 2022–2024 that did not exist when Munich's LiMux
failed (2017):
1. SCS provides a production-ready, fully open cloud substrate.
2. ZenDiS and OpenDesk provide a government-curated office suite.
3. openCode.de provides a commons for sharing and reusing government code.

The "build vs. buy" question is no longer the right frame. The correct question is
"adopt from the commons + contribute back" vs. "licence from vendor."

### The Munich failure was political, not technical
Post-mortem analyses (Burkhard, 2017; Landeshauptstadt München, 2017) confirm:
- Technical transition was largely successful (18,000 workstations migrated)
- Reversal was triggered by incoming city council with Microsoft ties (2014)
- Specific trigger: Bavarian state government systems not updated to open standards,
  creating compatibility pressure on municipal departments
- Cost argument was contested: city commissioned report (2013) showed savings
  of ~€10M; Microsoft-commissioned counter-report disputed methodology
Lesson: Cross-party mandate and open-standards adoption at Länder level are
prerequisites for sustainable municipal transitions.

### Cost picture is clearer than critics claim
Available evidence suggests:
- German federal LibreOffice migration (BSI estimate, 2021): licence savings
  €20M/year for ~100,000 seats
- French state migration to LibreOffice (Gendarmerie Nationale, 2006–2014):
  savings of €50M over 8 years vs. continued Microsoft licences
- Schleswig-Holstein Linux plan (2021–present): projected savings €13M/year
  (Ministerium für Digitalisierung, 2021 press release)
- Per-seat TCO for M365: €150–400/user/year (enterprise) for productivity alone;
  open-source stack: €0 licence + €60–120/user/year ops and support

### eCH and XÖV are structural prerequisites
Switzerland (eCH) and Germany (XÖV) have different XML standard families that
cannot be ignored: any municipal procurement must specify compliance with the
relevant national standard family as a mandatory criterion. Open-source tools
generally support these better than proprietary ones (vendor lock-in discourages
standards implementation).

---

## Open questions to research for v0.3.0

### Leads to follow up
- [ ] Schleswig-Holstein Linux migration: outcome data 2024–2026 (IT-Ministerium SH)
- [ ] Barcelona Decidim: post-2020 usage data, citizen satisfaction scores
- [ ] Frankfurt/Main digital transformation: early OZG EfA adoption outcomes
- [ ] Swiss eID wallet (BGEID implementation): timeline for municipal integration
- [ ] EU AI Act Art. 6–7 implications for municipal decision-support systems
- [ ] EU Data Act Art. 14–21: public sector data sharing obligations for municipalities
- [ ] GAIA-X minimum viable ecosystem 2025: which services are actually available?
- [ ] LocalAI/Ollama deployment in Swiss/German municipal context: any case studies?
- [ ] openCode.de contribution metrics: how many municipalities contributing vs. consuming?
- [ ] GovStack implementation: which countries have adopted building blocks?
- [ ] Flowable vs. Camunda for German OZG workflows: independent comparison
- [ ] ZenDiS OpenDesk v2: timeline and feature set

### Design questions for v1.0
- How should citizen satisfaction metrics be standardised across municipalities
  to enable benchmarking? (Propose a framework based on UN EGDI + SUS score)
- What is the minimum viable open-source stack for a municipality of 5,000–10,000?
  (Likely: hosted SCS + Nextcloud + TYPO3/Drupal + Keycloak)
- How should shared IT cooperatives (Zweckverband) be structured legally in
  Switzerland vs. Germany for municipal open-source operations?
- What procurement language should be included verbatim in RFPs?

---

## Source candidates (not yet assessed)

| Source | Type | Priority | Notes |
|---|---|---|---|
| EU AI Act (Reg. 2024/1689) | Legislation | HIGH | High-risk AI in municipal services |
| EU Data Act (Reg. 2023/2854) | Legislation | HIGH | Municipal data sharing |
| eIDAS 2.0 (Reg. 2024/1183) | Legislation | HIGH | EU Digital Identity wallet |
| GAIA-X docs 2025 | Policy | MEDIUM | Data space infrastructure |
| Schleswig-Holstein Linux report 2024 | Case study | HIGH | German Land Linux migration |
| Bourgogne-Franche-Comté LibreOffice eval | Case study | HIGH | French TCO data |
| Helsinki open-source strategy 2022 | Policy | MEDIUM | Nordic peer municipality |
| GeoServer docs (OSGeo) | Technical | LOW | Add to GIS section |
| Flowable docs (Activiti fork) | Technical | MEDIUM | Camunda alternative |
| Swiss P028 accessibility standard | Standard | MEDIUM | Web accessibility (CH) |
| IT-Planungsrat Beschlüsse 2023–2024 | Policy | MEDIUM | German IT planning resolutions |
| ZenDiS OpenDesk roadmap 2025 | Technical | HIGH | Product direction |

---

## Case study shortlist for v0.3.0

| Municipality | Country | Population | Stack focus | Data availability |
|---|---|---|---|---|
| Schaffhausen (canton) | CH | 85,000 | Decidim participation | Case study published |
| Heidekreis | DE | 140,000 | OZG EfA early adopter | FITKO case study |
| Schleswig-Holstein (Land) | DE | 2.9M | Linux migration 2021+ | Ongoing; partial data |
| Barcelona | ES | 1.6M | Decidim + open data | Multiple papers |
| Helsinki | FI | 660,000 | Open-source city stack | HEL strategy doc |
| Bourgogne-Franche-Comté | FR | 2.8M | LibreOffice migration | French gov't report |
| Dortmund | DE | 600,000 | Nextcloud + OZG | Dataport case study |
| Solothurn | CH | 17,000 | Small city model | To be researched |
