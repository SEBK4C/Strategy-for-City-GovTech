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
| [`Doc/`](Doc/) | Published documents (Markdown source of truth + generated HTML, DOCX, PDF) |
| [`Mem/`](Mem/) | Memory: source registry, literature-review state, research notes |
| [`Scripts/`](Scripts/) | Automation: document generation, translation, citation management, validation |
| [`.github/workflows/`](.github/workflows/) | CI: quarterly literature review, citation validation |

## Papers

| Paper | Languages | Latest version | Status |
|---|---|---|---|
| Sovereign by Design: Open-Source Technology Strategy for Municipal Governments | EN · DE | **v0.2.0** | Citation-complete draft |

Each paper follows a scientific structure: Abstract · Introduction · Methodology ·
Literature Review · Technology Stack Analysis · Implementation Roadmap · Stakeholder &
Procurement Strategy · Risk Analysis · Conclusion · References.

### v0.2.0 highlights (relative to v0.1.0)

- **56 references** [1]–[56] with full source registry metadata; all previously unverified citations resolved
- **New sections 3.6–3.11** covering GovStack, ZenDiS, eCH/Swiyu, TCO evidence, small-municipality mechanisms, and remaining literature gaps
- **Jurisdiction-specific implementation tracks** for Germany (Section 5.6: OZG 2.0, govdigital, ZenDiS, NIS2/NISG) and Switzerland (Section 5.7: EMBAG, eCH, Swiyu, ISDS)
- **Three appendices**: scoring methodology, implementation cost model (3 municipality sizes), CIO decision checklist

## Versioning

Documents use semantic versioning:

| Version | Meaning |
|---|---|
| `v0.1.0` | First structured draft (structure complete, some citations unverified) |
| `v0.2.0` | Citation-complete draft (all sources verified against primaries; critical gaps addressed) |
| `v0.3.0` | Small-municipality case studies; independent TCO data; AI Act implications |
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

This project is designed to improve on a recurring basis. A GitHub Actions workflow
(`.github/workflows/quarterly-review.yml`) runs automatically on the 21st of March,
June, September, and December. It creates a GitHub issue with a structured checklist
covering Swiss, German, and EU legislation updates; stack component releases; new
academic literature; and source registry maintenance.

The source registry (`Mem/source-registry.md`) and literature review state
(`Mem/literature-review-state.md`) are versioned alongside the papers and track
what is covered, what is missing, and what requires verification.

## Attribution

> **Sebastian Graf**
> Autonomous Office of Civil Digital Infrastructure
> Public requests and correspondence: [sebk4c@tuta.com](mailto:sebk4c@tuta.com)
