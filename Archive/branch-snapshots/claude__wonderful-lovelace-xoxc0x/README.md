# Strategy for City GovTech

**Open-source strategy papers for city governments implementing a state-of-the-art,
sovereign, open-source governmental administration technology stack.**

Author: **Sebastian Graf**, Autonomous Office of Civil Digital Infrastructure  
Public correspondence: [sebk4c@tuta.com](mailto:sebk4c@tuta.com)  
License: [CC-BY-4.0](LICENSE) (documents) · MIT (scripts)

---

## What this is

A continuously improving body of strategy papers, a self-improving literature review,
and a reproducible document-generation pipeline that together help municipal governments
plan and execute a transition to an open-source, digitally sovereign technology stack.

The work evaluates digital GovTech offerings from the **Swiss government** (EMBAG, eCH,
E-Government Strategy 2024–2027), **German governments** (OZG 2.0, Sovereign Cloud Stack,
OpenDesk/ZenDiS, govdigital eG), and the wider **European sovereign technology community**
(Decidim, Matrix, Nextcloud, CKAN, GovStack, GAIA-X). It provides a step-by-step
implementation roadmap, stakeholder engagement framework, procurement strategy, and
total cost of ownership analysis.

It is written for **all stakeholders** in municipal digital transformation: city
administrators, elected officials, public-sector IT teams, procurement offices,
civil-society groups, open-source communities, and sovereign technology providers.

## Repository structure

| Path | Purpose |
|---|---|
| [`Doc/en/`](Doc/en/) | English papers (source of truth) — Markdown + HTML |
| [`Doc/de/`](Doc/de/) | German translations — Markdown + HTML |
| [`Mem/`](Mem/) | Memory: source registry, literature-review state, research notes |
| [`Scripts/`](Scripts/) | Automation: document generation, citation validation, translation workflow |

## Papers

| Paper | Languages | Version | Status |
|---|---|---|---|
| Sovereign by Design: Open-Source Technology Strategy for Municipal Governments | EN · DE | **v0.2.0** | Citation-complete draft |
| Sovereign by Design (v0.1.0 archive) | EN · DE | v0.1.0 | Superseded |

### v0.2.0 additions over v0.1.0
- Expanded literature review: eCH standards, GovStack (ITU/DIAL), GAIA-X, EU AI Act implications
- Case studies: Barcelona, Helsinki, Canton Schaffhausen, OpenDesk (federal), Munich LiMux
- New TCO analysis section (35% saving for reference municipality; 55–65% cooperative)
- ZenDiS and OpenDesk deep dive
- 65+ verified registry entries (all citations traced to primary sources)
- Interoperability standards matrix (XÖV/eCH/DCAT-AP/OIDC/WCAG)

## Scientific structure

Each paper follows a scientific structure:

> Abstract · Introduction · Methodology · Literature Review · Technology Stack Analysis · Implementation Roadmap · Stakeholder & Procurement Strategy · Risk Analysis · Total Cost of Ownership · Conclusion · References

## Versioning

| Version | Meaning |
|---|---|
| `v0.1.0` | First structured draft (structure complete, some citations unverified) |
| `v0.2.0` | Citation-complete draft (all sources verified against primaries) |
| `v1.0.0` | Externally shareable release |

## Languages

English is the **single source of truth**. German is a full translation derived from it.
The system is designed so additional languages (French, Italian, Romansh) can be added
without rewriting the source material.

| Language | Code | Status |
|---|---|---|
| English | `en` | Source of truth |
| Deutsch | `de` | v0.2.0 complete |
| Français | `fr` | Planned for v1.0.0 |
| Italiano | `it` | Planned for v1.0.0 |

See [`Scripts/translate_document.py --add-language fr`](Scripts/translate_document.py) for the procedure to add a language.

## Reproduce

```bash
pip install -r requirements.txt

# Build all documents (Markdown → DOCX → PDF → HTML)
python3 Scripts/build_govtech_docs.py --version 0.2.0

# Validate all citations against source registry
python3 Scripts/validate_citations.py --strict

# Generate the quarterly literature-review checklist
python3 Scripts/update_literature_review.py

# Check translation parity (EN vs DE)
python3 Scripts/translate_document.py --check --lang de

# Add a new language (e.g. French)
python3 Scripts/translate_document.py --add-language fr
```

## Continuous improvement

This project improves on a quarterly basis. The source registry, literature review, and
implementation strategy are versioned and updated every quarter. See
[`Mem/literature-review-state.md`](Mem/literature-review-state.md) for the full gap analysis
and improvement roadmap.

The working structure (research notes, source registry drafts, progress log) lives in
the [Thinking-Deeply](https://github.com/SEBK4C/Thinking-Deeply) repository under
`Mem/govtech/` and `Scripts/govtech/`.

## Attribution

> **Sebastian Graf**  
> Autonomous Office of Civil Digital Infrastructure  
> Public requests and correspondence: [sebk4c@tuta.com](mailto:sebk4c@tuta.com)
