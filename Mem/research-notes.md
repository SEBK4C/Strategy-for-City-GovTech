# Research Notes — City GovTech Strategy

**Maintainer:** Sebastian Graf, Autonomous Office of Civil Digital Infrastructure
**Last updated:** 2026-06-20

Working notes, findings, and decisions made during the drafting of the strategy papers.
These notes inform future versions and the quarterly self-improvement cycle.

---

## v0.2.0 Research Session — 2026-06-20

### Task
Upgrade from v0.1.0 (structured draft) to v0.2.0 (citation-complete draft) of the
English strategy paper, produce a complete German translation, and generate HTML versions
of both. Update all Mem/ files.

### Key research findings

#### EU legislative landscape
The EU regulatory frame for open-source GovTech is now tighter than the v0.1.0 paper
reflected. Three regulations deserve equal prominence:

1. **Interoperable Europe Act (2024/903)** [6] — already in v0.1.0
2. **Data Governance Act (2022/868)** [48] — added in v0.2.0; creates non-exclusive data
   sharing obligations for public sector; voluntary but well-incentivised
3. **Data Act (2023/2854)** [55] — added in v0.2.0; hardest hitting for vendor lock-in;
   mandates cloud switching assistance and interoperability; applies to smart-city IoT data

Together these three create what could be called a "digital sovereignty floor" for EU
public-sector IT: open standards mandated, switching costs legislated away, interoperability
cross-border binding.

#### Case study selection rationale
Four case studies selected for v0.2.0 (§3.8):

- **Barcelona** [54]: Best documented large-city open-source commitment with measurable
  outcomes (Decidim, open-source preference policy). Plans were ambitious; some
  back-sliding under subsequent administrations is worth noting for v1.0.0.
- **Schleswig-Holstein** [47]: Most significant German Land commitment; 25,000 workstations;
  directly replicable by German municipalities. Progress tracking needed for v1.0.0.
- **Helsinki** [56]: Pioneer Nordic open data; strong participatory democracy platform
  (Decidim). Good counterpoint to Iberian case studies.
- **Swiss Federal** (EMBAG, Nextcloud): Regulatory mandate case; shows top-down legislative
  driver working alongside bottom-up community adoption.

Note: Munich LiMux (2003–2017 migration followed by 2017 regression to Microsoft) was
not included as a main case study but referenced in risk analysis. It is valuable for
the change-management section in v1.0.0 — the political economy of proprietary regression
needs dedicated treatment.

#### Technology stack completeness assessment
v0.1.0 had 11 components across 7 layers. v0.2.0 adds:
- **LibreOffice + Collabora** (§4.10): Document format sovereignty; crucial in German
  context where ODF vs. OOXML is politically live
- **Matomo** (§4.11): GDPR-mandatory analytics; DSK ruling [57] makes this non-optional
  for German public websites
- **Forgejo + Woodpecker CI** (§4.12): Code hosting sovereignty; currently most municipalities
  use GitHub (Microsoft) — this closes the self-hosting gap
- **Municipal ERP advisory** (§4.13): Advisory note only; no adequate open-source ERP for
  municipal finance/HR exists yet at the v0.2.0 review. Odoo is possible for small
  municipalities but not enterprise-grade for cities >50k. Flag for v0.3.0 review.

#### GovStack integration opportunity
GovStack [50] provides a technology-neutral building-block specification that aligns well
with the European open-source stack. The key insight is that GovStack's building blocks
map onto the tech stack in this paper:
- Identity BB → Keycloak + BundID/E-ID
- Information Mediator BB → X-Road-style API gateway
- Payments BB → not in scope for this paper
- Registration BB → Decidim / CONSUL
- GIS BB → QGIS + OpenStreetMap

The GovStack angle strengthens the paper's relevance for international audiences beyond
CH/DE/EU. Recommended for deeper treatment in v1.0.0.

#### German translation decisions
Some terminology choices required judgement calls:
- "Digital sovereignty" → "Digitale Souveränität" (standard German term)
- "Total cost of ownership" → "Gesamtbetriebskosten (TCO)"; acronym retained in parentheses
  since TCO is widely used in German IT procurement
- "Procurement" → "Beschaffung" (not "Ankauf" or "Einkauf", both too informal)
- "Steering committee" → "Lenkungsausschuss" (standard project governance term)
- "Change management" → kept as "Change-Management" (anglicism standard in German IT)
- "Data Protection Impact Assessment" → "Datenschutz-Folgenabschätzung (DSFA)" per DSGVO
- "Once Only" → kept as "Once-Only-Prinzip" (EU/BMI official terminology)
- "Building block" → "Baustein" for BSI Grundschutz context; "Building Block" retained
  where referring specifically to GovStack terminology

#### HTML design decisions
Both HTML files are self-contained (no external CDN dependencies):
- Fonts: system-ui stack (no Google Fonts — GDPR compliance)
- Styling: embedded `<style>` block; academic paper aesthetic
- No JavaScript (accessibility, performance, security)
- `lang` attribute set correctly (`lang="en"` / `lang="de"`)
- Meta description for web indexing
- Self-links to corresponding .md source

### Open questions for v0.3.0 / v1.0.0

1. **Munich LiMux regression**: What specifically caused the 2017 decision to return to
   Microsoft? Political economy analysis needed. Is the Schleswig-Holstein commitment
   structurally more resilient?

2. **Matomo vs. Plausible Analytics**: Matomo is GDPR-compliant and self-hosted; Plausible
   is a newer open-source alternative (AGPL-3.0, simpler UI). Should the paper recommend
   one or present both?

3. **Forgejo vs. GitLab CE**: Forgejo is lighter and fully open; GitLab CE is more
   feature-complete. For large municipalities with complex CI/CD needs, GitLab CE may be
   preferable. The paper should present both in v1.0.0.

4. **ERP gap**: No adequate open-source municipal ERP. Odoo 17 (LGPL-3.0) covers SME
   finance well but lacks German GemHVO-compliant accounting modules. Monitor for v0.3.0.

5. **Barcelona regression**: The post-2017 administrations rolled back some open-source
   commitments. This is important nuance for the case study — "exemplary deployment" needs
   honest treatment of reversals.

6. **Accessibility tooling**: TYPO3 is BITV 2.0 compliant, but how well do Decidim and
   CONSUL meet WCAG 2.1 AA in practice? German municipalities face legal liability for
   inaccessible public websites. Needs empirical check.

7. **Federated identity for cross-municipality services**: BundID (Germany), E-ID
   (Switzerland), and eIDAS 2.0 wallet (EU) all target the same user need but use
   different technical architectures. The paper should map interoperability paths.

---

## v0.1.0 Research Session — 2026-06-20 (initial)

Initial paper created with 46 citation slots across 8 sections. Identified the following
gap categories requiring v0.2.0 treatment:

- Missing: case studies section, EU Data Act, GovStack, LibreOffice, Matomo, Forgejo
- Missing: KPI framework, RFP template, GDPR analysis, vendor exit strategy
- Missing: glossary, regulatory appendix
- Source numbering gaps [15], [17], [18], [25], [28], [31], [32], [38], [40] are
  intentional — these IDs were used in early drafts and removed in consolidation
