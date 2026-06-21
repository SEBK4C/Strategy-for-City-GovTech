# Literature Review State — City GovTech Strategy

**Project:** Open-Source Municipal Government Technology Strategy  
**Version:** 0.2.0  
**Last updated:** 2026-06-21  
**Next scheduled review:** 2026-09-21 (quarterly cadence)

This file tracks the state of the literature review, identifies gaps, and documents
the improvement roadmap. It is the input document for `Scripts/update_literature_review.py`.

---

## Current coverage (v0.2.0)

### Well-covered areas

| Area | Coverage | Key sources |
|---|---|---|
| Swiss EMBAG legislation | Comprehensive | [1], [16], [47] |
| German OZG ecosystem | Comprehensive | [2], [9], [10], [23], [24], [46] |
| Sovereign Cloud Stack | Comprehensive | [3], [11], [55] |
| ZenDiS / OpenDesk | Comprehensive | [42], [50] |
| BundesMessenger / Matrix | Comprehensive | [14], [59] |
| Nextcloud government deployments | Comprehensive | [13], [58] |
| Decidim / citizen participation | Good | [12], [48] |
| CKAN / open data | Good | [22], [44] |
| EU regulatory framework | Comprehensive | [5], [6], [27], [45], [64] |
| Economic evidence | Good | [49], [56], [62] |
| Munich LiMux case | Comprehensive | [30], [56] |
| Schleswig-Holstein migration | Comprehensive | [51], [58] |
| TYPO3 / web publishing | Good | [19], [61] |
| BSI IT-Grundschutz / NIS2 | Comprehensive | [26], [27], [57] |
| Forgejo / code hosting | Adequate | [60] |
| LibreOffice / office suite | Adequate | [63] |
| GovStack | Adequate | [53] |
| Deutschland-Stack | Adequate | [54] |

### Gap analysis

| Gap | Priority | Action for v0.3.0 |
|---|---|---|
| Long-term TCO studies for small municipalities (<50,000 pop) | High | Search academic databases for 2020–2026 studies; commission if none found |
| User experience / citizen satisfaction research comparing OS vs proprietary | High | Search HCI/CSCW literature; contact Barcelona and Schleswig-Holstein for data |
| Longitudinal contribution-back economics | Medium | Search OSS economics literature; contact FSFE for data |
| Barcelona Digital Plan 2017 (primary source) | Medium | Fetch from ajuntament.barcelona.cat |
| Decidim Social Contract (primary source) | Medium | Fetch from meta.decidim.org |
| AI Act implementing regulations for public sector | Medium | Monitor EUR-Lex; expected 2025–2026 |
| OZG 2.0 first scientific evaluation report | Low | Due 2027; flag for future review |
| AKDB specific technology stack and services | Low | Request from AKDB directly |
| Open-Xchange technical documentation | Low | Fetch from open-xchange.com |
| Swiss E-ID Act implementation details | Medium | Fetch from fedlex.admin.ch |
| eCH-0160 digital archiving standard specifics | Low | Fetch from ech.ch |
| Horizon Europe NGI specific active calls 2026 | Medium | Check ec.europa.eu/info/funding-tenders |

---

## Literature review improvement roadmap

### v0.3.0 (target: 2026-09-21)

1. **Close TCO gap:** Commission or locate 2020–2026 comparative TCO studies for small municipalities. If none available, draft a model TCO calculation based on Schleswig-Holstein and Munich data, clearly marked as indicative.
2. **Add primary sources:** Barcelona Digital Plan 2017, Decidim Social Contract, Swiss E-ID Act.
3. **Expand AI Act section:** Add implementing regulations once published; include French "Albert" AI assistant as case study.
4. **Add AKDB profile:** Request technology stack documentation from AKDB for Bavaria-specific implementation guidance.
5. **Update OZG metrics:** Track OZG 2.0 implementation dashboard for 2025 data (target: services online count).

### v1.0.0 (target: 2027-01-21)

1. **Commission user satisfaction study:** Design and propose a comparative study of citizen satisfaction with open-source vs. proprietary municipal digital services across at least three municipalities.
2. **Full regulatory update:** Include NIS2 implementing acts, AI Act delegated regulations, updated EU Open Source Strategy (expected 2024+).
3. **Economic model:** Publish a reproducible economic model for open-source municipal TCO, covering municipalities of 10,000 / 50,000 / 250,000 population.
4. **Case study expansion:** Add at least two more city-level case studies (suggested: Zurich, Vienna, or Tallinn).

---

## Recurring improvement workflow

Run quarterly:

```bash
python3 Scripts/update_literature_review.py
```

This script:
1. Loads this file and the source registry
2. Checks each source URL for availability and changed content
3. Prompts for review of each gap item
4. Generates a structured agenda for the next literature review cycle
5. Updates the `Last updated` date and `Next scheduled review` date

---

## Change log

| Version | Date | Changes |
|---|---|---|
| 0.1.0 | 2026-06-20 | Initial literature review state |
| 0.2.0 | 2026-06-21 | Added 18 new sources [47]–[64]; fixed all unverified citations; added economic evidence section; updated gap analysis |
