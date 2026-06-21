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

The work evaluates digital GovTech offerings from the **Swiss government**, **German
governments** (federal and Länder), and the wider **European sovereign technology
community**, examines the overall technology stack from first principles, and provides a
step-by-step implementation plan.

It is written for **all stakeholders** in municipal digital transformation: city
administrators, elected officials, public-sector IT teams, procurement offices,
civil-society groups, open-source communities, and sovereign technology providers.

## Repository structure

| Path | Purpose |
|---|---|
| [`Doc/`](Doc/) | Published documents (Markdown source of truth + HTML) |
| [`Mem/`](Mem/) | Memory: source registry, literature-review state, research notes |
| [`Scripts/`](Scripts/) | Automation: document generation, translation, citation management, validation |

## Papers

| Paper | Version | Languages | Status | Formats |
|---|---|---|---|---|
| **Sovereign by Design**: Open-Source Municipal GovTech Strategy | **v0.2.0** | EN · DE | Citation-Complete Draft | [EN ℹ️](Doc/en/sovereign-by-design-v0.2.0.md) · [EN HTML](Doc/en/sovereign-by-design-v0.2.0.html) · [DE ℹ️](Doc/de/sovereign-by-design-v0.2.0.de.md) · [DE HTML](Doc/de/sovereign-by-design-v0.2.0.de.html) |
| Sovereign by Design | v0.1.0 | EN · DE | First structured draft (archived) | [EN ℹ️](Doc/en/sovereign-by-design-v0.1.0.md) · [DE ℹ️](Doc/de/sovereign-by-design-v0.1.0.de.md) |

Each paper follows a scientific structure: Abstract · Introduction · Methodology ·
Literature Review · Technology Stack Analysis · Implementation Roadmap · Stakeholder &
Procurement Strategy · Data Governance & Privacy · Risk Analysis · Conclusion · References.

### v0.2.0 highlights (2026-06-21)

- **61 cited sources** (up from 46 at v0.1.0), all documented in [`Mem/source-registry.md`](Mem/source-registry.md)
- New Section 3.6: TCO evidence (French Gendarmerie ~40% savings; 5-year comparison table)
- New Section 3.7: EU regulatory context (AI Act, Data Act, NIS2)
- New Section 3.8: Small-municipality case studies (Schaffhausen CH, Vitoria-Gasteiz ES, Bolzano IT, Rennes FR)
- New Section 4.10: AI services layer (Ollama + Nextcloud AI, EU AI Act compliance)
- New Section 7: Data Governance and Privacy (GDPR architecture, data residency, OGD policy)
- Updated reference architecture with AI layer
- Readiness assessment and cost estimation frameworks

## Versioning

Documents use semantic versioning:

| Version | Meaning |
|---|---|
| `v0.1.0` | First structured draft (structure complete, some citations unverified) |
| `v0.2.0` | Citation-complete draft (all sources verified against primaries) |
| `v1.0.0` | Externally shareable release (after peer review and stakeholder consultation) |

## Languages

English is the **single source of truth**. German is a full translation derived from it.
The system is designed so additional languages can be added without rewriting the source
material.

## Reproduce

```bash
pip install mistune  # optional, for higher-quality HTML output

# Generate HTML from Markdown
python3 Scripts/generate_html.py

# Validate every citation against the source registry
python3 Scripts/validate_citations.py

# Generate the literature-review improvement agenda
python3 Scripts/update_literature_review.py
```

## Continuous improvement

This project is designed to improve on a recurring basis. The source registry, literature
review, and implementation strategy are versioned and revisited on a **quarterly cadence**.
See [`Mem/literature-review-state.md`](Mem/literature-review-state.md) for the current
coverage map, critical gaps, and next-review date.

Next review due: **2026-09-21**.

## Attribution

> **Sebastian Graf**
> Autonomous Office of Civil Digital Infrastructure
> Public requests and correspondence: [sebk4c@tuta.com](mailto:sebk4c@tuta.com)
