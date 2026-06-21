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
| [`PLAN.md`](PLAN.md) | Requirements matrix, implementation status, open decisions, and milestone plan |
| [`Doc/`](Doc/) | Published documents (Markdown source of truth + committed HTML; DOCX/PDF via build) |
| [`Mem/`](Mem/) | Memory: source registry, literature-review state, research notes |
| [`Scripts/`](Scripts/) | Automation: document generation, translation, citation management, validation |
| [`Archive/`](Archive/) | Branch audit and full snapshots of the fetched loop-created branches |
| [`.github/workflows/`](.github/workflows/) | CI that builds & publishes DOCX/PDF/HTML on every push |

## Branching & loop workflow

**This project uses a single branch — `main` — for all work, including recurring
automated (“loop”) runs.** Earlier runs created a new per-session branch each time
(`claude/<name>-<id>`), which fragmented the work across many parallel branches. That is
no longer done:

- `main` is the **single source of truth** and the only long-lived branch.
- Recurring/automated runs commit their work to `main` (via short-lived PRs or directly).
- Historical per-session `claude/*` branches are **superseded by `main`** and may be
  deleted after review; their fetched contents are preserved under
  [`Archive/branch-snapshots/`](Archive/branch-snapshots/).

See [`AGENTS.md`](AGENTS.md) for the convention automated runs follow.
See [`Archive/branch-audit-2026-06-21.md`](Archive/branch-audit-2026-06-21.md) for the
branch-by-branch consolidation notes.

## Papers

| Paper | Version | Languages | Status | Source |
|---|---:|---|---|---|
| Sovereign by Design: Open-Source Technology Strategy for Municipal Governments | v0.3.0 | EN · DE | Extended draft | [`EN`](Doc/en/sovereign-by-design-v0.3.0.md) · [`DE`](Doc/de/sovereign-by-design-v0.3.0.de.md) |
| Sovereign by Design: Open-Source Technology Strategy for Municipal Governments | v0.2.0 | EN · DE | Citation-complete draft | [`EN`](Doc/en/sovereign-by-design-v0.2.0.md) · [`DE`](Doc/de/sovereign-by-design-v0.2.0.de.md) |
| Sovereign by Design: Open-Source Technology Strategy for Municipal Governments | v0.1.0 | EN · DE | First structured draft | [`EN`](Doc/en/sovereign-by-design-v0.1.0.md) · [`DE`](Doc/de/sovereign-by-design-v0.1.0.de.md) |
| Sovereign by Design appendices | v0.2.0 | EN · DE | Supporting material | [`EN`](Doc/en/appendices-v0.2.0.md) · [`DE`](Doc/de/appendices-v0.2.0.de.md) |

Each paper follows a scientific structure: Abstract · Introduction · Methodology ·
Literature Review · Technology Stack Analysis · Implementation Roadmap · Stakeholder &
Procurement Strategy · Risk Analysis · Conclusion · References.

## Formats

| Format | Where |
|---|---|
| Markdown | committed under `Doc/<lang>/` (source of truth) |
| HTML | committed under `Doc/<lang>/` (generated rendering) |
| DOCX, PDF | built by `Scripts/build_govtech_docs.py` into `Doc/build/`; published as CI artifacts on every push and as release assets on `vX.Y.Z` tags |

## Versioning

Documents use semantic versioning:

| Version | Meaning |
|---|---|
| `v0.1.0` | First structured draft (structure complete, some citations unverified) |
| `v0.2.0` | Citation-complete draft (all sources verified against primaries) |
| `v0.3.0` | Extended draft adding GovStack, EU AI Act, GAIA-X, OSOR, AKDB, and TCO material |
| `v1.0.0` | Externally shareable release |

## Languages

English is the **single source of truth**. German is a full translation derived from it.
The system is designed so additional languages can be added without rewriting the source
material — see [`Doc/README.md`](Doc/README.md) for the “add a language” procedure.

## Reproduce

```bash
uv sync

# Build all documents (Markdown → DOCX → PDF → HTML)
uv run python Scripts/build_govtech_docs.py

# Validate every citation against the source registry
uv run python Scripts/validate_citations.py

# Generate the literature-review improvement agenda
uv run python Scripts/update_literature_review.py

# Check translation parity between language versions
uv run python Scripts/translate_document.py --check

# Smoke-check source length, EN/DE length parity, and generated artifacts
uv run python Scripts/smoke_check.py
```

Use `uv` for project dependencies and `uvx` for one-off external Python CLIs. Do not use
`pip install` in the project root.

## Continuous improvement

This project is designed to improve on a recurring basis. The source registry, literature
review, and implementation strategy are versioned and revisited on a quarterly cadence.
See [`Mem/README.md`](Mem/README.md) and [`Scripts/update_literature_review.py`](Scripts/update_literature_review.py).

## Attribution

> **Sebastian Graf**
> Autonomous Office of Civil Digital Infrastructure
> Public requests and correspondence: [sebk4c@tuta.com](mailto:sebk4c@tuta.com)
