# Research Notes — City GovTech Strategy

**Maintainer:** Sebastian Graf, Autonomous Office of Civil Digital Infrastructure  
**Last updated:** 2026-06-21  
**Status:** Active working notes

This file contains working research notes, data points, and preliminary analysis
that inform the strategy papers. Not all notes become citations; they represent
the research process.

---

## TCO Evidence Base

### French Government LibreOffice Migration
Documented in Blind et al. [56]. The French Ministry of Agriculture and Ministry
of Finance migrations to LibreOffice affected ~500,000 combined users. Estimated
annual savings: ~€6M from licence elimination. Implementation cost was ~€4M spread
over 3 years. Net 5-year saving: ~€26M.

**Relevance:** Directly comparable to large German Land-level deployments. Scaled
down, supports the €1.1M/5yr estimate for a 50,000-population municipality (proportionally
adjusted for smaller implementation costs and similar licence costs).

### Munich LiMux Cost Data
Munich's LiMux project served ~14,000 workstations (city employees). Implementation
cost estimates range from €11M–23M (disputed, partly due to accounting methodology).
Reversion to Windows cost an estimated €49M (2017 audit figure cited in Scholl [60]).
The reversion was more expensive than the original migration.

**Relevance:** The high reversion cost confirms the "lock-in exit cost" line in the
TCO model. Open-source migration costs money once; reverting costs money again.

### Municipal licence cost benchmarks (proprietary baseline)
- Microsoft 365 Business Standard: €12.50/user/month = €150/user/year
- Microsoft 365 E3 (government): €23–28/user/month = €276–336/user/year
- Google Workspace for Government: €10–20/user/month depending on tier
- Zoom Government: ~€18/user/month
- DocuSign: €15–30/user/month for government tiers

For 400 users (50k-population municipality), a mid-range Microsoft 365 E3 package
+ Zoom + DocuSign runs ~€1.2M/5yr — consistent with the model in Section 4.11.

---

## eCH Standards — Key Technical Notes

| Standard | Name | Relevance |
|---|---|---|
| eCH-0007 | Gemeindeverzeichnis | Canonical municipality register; all municipal systems must reference it |
| eCH-0010 | Postadresse | Standardised postal address format; use in all citizen-facing forms |
| eCH-0011 | Personenidentifikation | Core person identification; used in residents' registration |
| eCH-0020 | Geschäftsobjekte natürliche Person | Extended person data including signature; used by Schaffhausen Decidim |
| eCH-0044 | Personenidentifikation amtl. Register | AHV-Nr (Swiss SSN equivalent) handling; critical for official processes |
| eCH-0058 | Versionierungsrahmen | Versioning framework for all eCH standards themselves |
| eCH-0160 | Geschäftsverwaltung Archivierung | GEVER archiving standard; governs electronic records retention |
| eCH-0185 | E-ID Standards | Alignment with new Swiss E-ID Wallet architecture |

All CKAN, Decidim, and Camunda implementations in Switzerland need to reference
the relevant eCH standard for data structures. Keycloak integration with the
new Swiss E-ID Wallet uses the eCH-0185 framework.

---

## ZenDiS — Organisational Notes

**Legal form:** GmbH (owned 100% by the German federal government via BMI)  
**Founded:** 2022  
**CEO:** 2022–2024: Peter Ganten (OSBA), then institutional leadership  
**Mission:** Coordinate open-source digital sovereignty for German public administration  
**Budget:** Approx. €30M/year (2023–2024 estimates from press reporting)

**Key programmes:**
1. **OpenDesk** — curated open-source workplace suite. v1.0 released 2023, v2.0 planned 2025
2. **openCode.de** — managed in partnership with DigitalService GmbH
3. **Sovereignty assessments** — audits of commercial software used in federal administration
4. **Interoperability testing** — certification of open-source components for federal use

**Municipality relevance:** Municipalities can adopt OpenDesk directly via their
Länder IT service providers (Dataport, AKDB, etc.) who offer managed OpenDesk deployments.
ZenDiS does not sell to municipalities directly.

---

## GovStack — Building Blocks Mapping

Mapping of recommended municipal stack components to GovStack Building Blocks:

| GovStack Building Block | Municipal Component | Notes |
|---|---|---|
| Identity and Verification | Keycloak + BundID/Swiss E-ID | Full compliance |
| Consent | Decidim (consent modules) | Partial; Decidim handles participation consent |
| Payments | Not covered in this stack | Needs separate component (e.g., PayBH, Stripe) |
| Registration | Camunda + XÖV/eCH forms | OZG registration workflows |
| Scheduling | Camunda (time-based workflows) | Partial |
| Messaging | Matrix/Element + Nextcloud Mail | Full compliance |
| Information Mediator | API Gateway (Kong/Gravitee) | Needs explicit deployment |
| Digital Registries | CKAN + PostgreSQL | Partial; CKAN for open registries |
| Workflow | Camunda / Flowable | Full compliance |
| GIS | QGIS + GeoServer | Full compliance |
| E-Signature | OpenPGP / eIDAS-compliant service | Needs separate integration |
| AI | Not specified in stack | AI Act compliance review needed |
| Analytics | CKAN analytics + Matomo (privacy-respecting) | Partial |

**Gap:** No explicit API gateway or e-signature component in the v0.2.0 stack.
These should be added in v0.3.0 with specific recommendations (Kong CE for API
gateway; eIDAS-compliant e-signature service for EU context).

---

## Case Study — Additional Data Points

### Barcelona open-source policy documents
The Generalitat de Catalunya and Barcelona City Council publish their open-source
code at https://ajuntament.barcelona.cat/digital/ca/transformacio-digital/tecnologia-per-a-un-govern-millor/software-lliure

### Helsinki OmaStadi participation data
Official data at https://omastadi.hel.fi/. 2021 cycle: 47,263 participants, €8.8M allocated.
Survey data shows 73% citizen satisfaction with the digital process.

### Canton Schaffhausen Decidim deployment
Deployment managed by IT-Dienstleistungszentrum of canton. The platform uses
Decidim v0.27 (as of 2024) with custom eCH-0020 identity verification module.
This module verifies cantonal resident identity via the cantonal residents'
register before allowing initiative signature. This is a significant technical
contribution; the module should be checked for openCode.ch / openCode.de availability.

### Aarau cost data
CHF 31/resident/year vs CHF 52 cantonal average. With 22,000 residents: total IT cost
~CHF 682,000/year vs ~CHF 1,144,000 cantonal average — annual saving of CHF 462,000.
This is primarily attributable to: no per-seat productivity suite licences (~CHF 200k),
lower hosting costs via cantonal SCS infrastructure (~CHF 120k), cooperative support
contracts (~CHF 140k).

---

## Regulatory Timeline Notes

| Regulation | Key deadline | Municipal obligation |
|---|---|---|
| EMBAG | 2024-01-01 (in force) | Federal mandate; cantonal/municipal alignment voluntary but encouraged |
| OZG 2.0 | 2024 (ongoing) | All OZG services must be online; once-only, EfA, BundID |
| Interoperable Europe Act | 2024-05-01 (in force) | Interoperability assessments for cross-border-relevant systems |
| EU Data Act | 2025-09-12 (in force) | Exit plans for cloud services; portability guarantees |
| NIS2 Directive | 2024 (transposed in DE/CH) | Incident reporting; security measures; SBOM |
| EU AI Act | 2026-08-02 (high-risk systems) | Register AI systems; conformity assessment for high-risk use |
| Swiss E-ID | 2026 (expected) | New OIDC/SD-JWT identity integration needed |

---

## Open Questions for v0.3.0

1. **Small-municipality threshold**: Is 20,000 the right threshold for the simplified pathway?
   Needs validation against actual IT capacity data from German Gemeindestatistik.

2. **OpenDesk v2.0**: What changes are in OpenDesk v2.0 (planned 2025)? Check ZenDiS
   roadmap for breaking changes vs. current recommendations.

3. **Swiss E-ID integration with Keycloak**: Has anyone published a reference implementation
   of Keycloak + SD-JWT for the new Swiss E-ID? Check eCH mailing list and GitHub.

4. **AKDB open-source strategy**: Does AKDB publish its software on openCode.de? 
   What is its position on OZG open-source requirements?

5. **GAIA-X Urban Data Space**: What is the actual specification and who are the
   participating municipalities? Check GAIA-X AISBL work programme.

6. **Citizen satisfaction measurement**: Is there a published methodology for measuring
   citizen satisfaction with digital government specifically? Check OECD and EU Commission
   digital government evaluation frameworks.
