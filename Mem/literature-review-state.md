# Literature Review State — City GovTech Strategy

**Project:** Open-Source Municipal Government Technology Strategy
**Maintainer:** Sebastian Graf, Autonomous Office of Civil Digital Infrastructure
**Last updated:** 2026-06-20
**Current version:** v0.1.1 (cycle after v0.1.0 paper release)
**Next review due:** 2026-09-20 (Q3 2026)

This file tracks the state of the literature review: what has been covered, what gaps
remain, what sources need verification, and what the improvement agenda is for the next
quarterly cycle. It feeds the `Scripts/update_literature_review.py` automation.

---

## Current coverage summary (v0.1.0)

| Domain | Coverage | Quality | Priority gaps |
|---|---|---|---|
| E-government theory | Good | Peer-reviewed | Post-2020 platform-government literature thin |
| Digital sovereignty (EU) | Good | Policy + academic | Legal implementation studies missing |
| Swiss EMBAG/eID | Good | Primary source | BGEID implementation details unverified |
| German OZG ecosystem | Good | Policy + grey lit | Municipal-level TCO data absent |
| Open-source municipal stacks | Moderate | Mixed | Small-municipality case studies missing |
| Participatory democracy platforms | Good | Grey lit dominant | Decidim Schaffhausen case study missing |
| Secure communications | Moderate | Grey lit | BundesMessenger technical evaluation missing |
| Cloud infrastructure (SCS) | Good | Technical docs | Commercial SCS operator comparison missing |
| GIS / spatial data | Thin | Grey lit only | No academic treatment |
| Procurement frameworks | Thin | Policy only | Legal comparative analysis missing |
| Change management / org factors | Thin | Case study only | Munich LiMux post-mortem needs update |
| Security (BSI, NIS2) | Good | Primary source | NIS2 transposition status by country missing |
| User experience research | Very thin | Almost none | Critical gap — no comparative UX data exists |

---

## Sources verified since last cycle

All 46 sources in `Mem/source-registry.md` v0.1.0 were reviewed. 4 required
verification (marked in registry). 7 new sources added ([47]–[53]):
- [47] CONSUL Democracy — verified
- [48] eCH Standards — verified
- [49] ZenDiS — verified
- [50] OSOR Annual Report — unverified (URL needed)
- [51] Swiss BGEID — unverified (Fedlex URL to confirm)
- [52] Lathrop & Ruma — verified
- [53] GovStack/ITU — verified

---

## Improvement agenda — v0.2.0 cycle (Q3 2026)

### High priority

1. **Locate and verify OSOR Annual Report 2023 PDF** — this is the primary source for
   comparative open-source adoption data across EU administrations. Without it, the
   deployment-frequency claims in Section 4 rest on grey literature only.

2. **Verify Swiss BGEID Fedlex URL and confirm in-force date** — eID section of the
   paper uses this as a reference. The 2021 referendum result is confirmed, but the
   implementing legislation URL needs checking.

3. **Add Decidim Schaffhausen case study** — this is the primary Swiss cantonal Decidim
   deployment and should be cited in Section 3.5. Search: "Decidim Schaffhausen Kanton"
   or contact the Decidim Association for a case study reference.

4. **TCO comparative data** — the economic argument in Section 8 (finding 3) makes
   quantitative claims (€100–300/user/year licence cost) that need primary source
   backing. Priority: find at least one government-commissioned TCO study or audit.

5. **Add GovStack [53] to main paper** — the ITU/DIAL building-blocks framework is
   directly relevant to Section 4 (technology stack analysis) as it provides an
   internationally recognised component taxonomy. Add a subsection reference in v0.2.0.

### Medium priority

6. **eCH standards [48] integration** — eCH should be cited alongside XÖV in Section
   4.10 (reference architecture) and Section 6.2 (procurement framework, interoperability
   requirements). Add a paragraph on eCH in Section 3.4 (Swiss digital services).

7. **BundesMessenger technical evaluation** — the German BundesMessenger is cited as
   a reference deployment in Section 4.5 but without a primary technical source.
   Search for BSI or BMI evaluation reports.

8. **Munich LiMux post-mortem update** — the [30] Janowski citation is used to
   contextualise Munich but does not specifically address LiMux. Find the 2019 Munich
   city council investigation report or Sirius/Gartner post-mortem.

9. **EUCS (EU Cloud Certification Scheme)** — relevant to Section 4.9 (cloud
   infrastructure). The ENISA EUCS Level High requirements for cloud sovereignty are
   directly applicable to SCS certification.

10. **NIS2 transposition tracker** — cite a current transposition-status source to
    support the regulatory pressure argument in the conclusion.

### Low priority

11. **CONSUL vs Decidim comparative evaluation** — now that [47] CONSUL is in the
    registry, add a paragraph comparing the two in Section 4.4.

12. **Add small-municipality case study** — find one example of a municipality under
    50,000 inhabitants that has completed or is executing an open-source transition.
    Swiss Gemeinden or German Kleinstädte are the target.

13. **Add academic treatment of GIS in e-government** — Section 4.7 has no academic
    citations. Search Government Information Quarterly for GIS/spatial data articles.

---

## Self-improvement process

This literature review improves on a quarterly cadence via this process:

1. **Run** `Scripts/update_literature_review.py` — generates a structured checklist of
   the items above, ordered by priority.
2. **Search** for each high-priority gap using academic databases (Google Scholar,
   Semantic Scholar), grey literature (EU Joinup, FITKO, BSI, Swiss Federal Chancellery),
   and community sources (openCode.de, SCS community blog).
3. **Add** verified sources to `Mem/source-registry.md` with full metadata.
4. **Update** the paper (English source of truth) to incorporate new citations.
5. **Regenerate** the German translation where sections change.
6. **Bump** the document version (patch version for citation additions, minor for new
   sections, major for externally shareable release).
7. **Update** this file with new coverage summary and next cycle's agenda.

---

## Known permanent gaps (not addressable by literature search)

- **User experience comparative data**: No published research compares citizen
  satisfaction with open-source vs proprietary municipal digital services. This gap
  is structural in the field, not just in this review.
- **Small-municipality cost data**: Disaggregated cost data for municipalities under
  10,000 inhabitants is almost entirely absent from published literature.
- **Real-time vendor lobbying documentation**: The influence of proprietary vendors on
  municipal IT decisions is documented anecdotally but rarely in peer-reviewed literature.
