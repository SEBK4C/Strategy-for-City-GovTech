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
| [`Doc/`](Doc/) | Published documents (Markdown source of truth + generated DOCX, PDF, HTML) |
| [`Mem/`](Mem/) | Memory: source registry, literature-review state, research notes |
| [`Scripts/`](Scripts/) | Automation: document generation, translation, citation management, validation |

## Papers

| Paper | Languages | Status |
|---|---|---|
| Sovereign by Design: Open-Source Technology Strategy for Municipal Governments | EN · DE | v0.1.0 — first structured draft |

Each paper follows a scientific structure: Abstract · Introduction · Methodology ·
Literature Review · Technology Stack Analysis · Implementation Roadmap · Stakeholder &
Procurement Strategy · Risk Analysis · Conclusion · References.

## Versioning

Documents use semantic versioning:

| Version | Meaning |
|---|---|
| `v0.1.0` | First structured draft (structure complete, some citations unverified) |
| `v0.2.0` | Citation-complete draft (all sources verified against primaries) |
| `v1.0.0` | Externally shareable release |

## Languages

English is the **single source of truth**. German is a full translation derived from it.
The system is designed so additional languages can be added without rewriting the source
material — see [`Doc/README.md`](Doc/README.md) for the "add a language" procedure.

## Reproduce

```bash
pip install -r requirements.txt

# Build all documents (Markdown → DOCX → PDF → HTML)
python3 Scripts/build_govtech_docs.py

# Validate every citation against the source registry
python3 Scripts/validate_citations.py

# Generate the literature-review improvement agenda
python3 Scripts/update_literature_review.py

# Check translation parity between language versions
python3 Scripts/translate_document.py --check
```

## Continuous improvement

This project is designed to improve on a recurring basis. The source registry, literature
review, and implementation strategy are versioned and revisited on a quarterly cadence.
See [`Mem/README.md`](Mem/README.md) and [`Scripts/update_literature_review.py`](Scripts/update_literature_review.py).

## Attribution

> **Sebastian Graf**
> Autonomous Office of Civil Digital Infrastructure
> Public requests and correspondence: [sebk4c@tuta.com](mailto:sebk4c@tuta.com)
