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

The work evaluates digital GovTech offerings from the **Swiss government** (EMBAG, eCH
standards, Swiss E-ID), **German governments** (OZG 2.0, Sovereign Cloud Stack, OpenDesk,
ZenDiS), and the wider **European sovereign technology community** (Interoperable Europe
Act, EU Data Act, GovStack, GAIA-X), examines the overall technology stack from first
principles, and provides a step-by-step implementation plan.

It is written for **all stakeholders** in municipal digital transformation: city
administrators, elected officials, public-sector IT teams, procurement offices,
civil-society groups, open-source communities, and sovereign technology providers.

## Repository structure

| Path | Purpose |
|---|---|
| [`Doc/`](Doc/) | Published documents (Markdown source of truth + HTML; DOCX/PDF via build) |
| [`Mem/`](Mem/) | Memory: source registry, literature-review state, research notes |
| [`Scripts/`](Scripts/) | Automation: document generation, citation validation, translation |
| [`.github/workflows/`](.github/workflows/) | CI that builds & publishes outputs on every push |

## Papers

| Paper | Version | Languages | Status | Files |
|---|---|---|---|---|
| Sovereign by Design: Open-Source Technology Strategy for Municipal Governments | **v0.2.0** | EN · DE | Citation-complete draft | [EN MD](Doc/en/sovereign-by-design-v0.2.0.md) · [EN HTML](Doc/en/sovereign-by-design-v0.2.0.html) · [DE MD](Doc/de/sovereign-by-design-v0.2.0.de.md) · [DE HTML](Doc/de/sovereign-by-design-v0.2.0.de.html) |
| Sovereign by Design: Open-Source Technology Strategy for Municipal Governments | v0.1.0 | EN · DE | First structured draft (superseded) | [EN MD](Doc/en/sovereign-by-design-v0.1.0.md) · [DE MD](Doc/de/sovereign-by-design-v0.1.0.de.md) |

Each paper follows a scientific structure: Abstract · Introduction · Methodology ·
Literature Review · Technology Stack Analysis · Implementation Roadmap · Stakeholder &
Procurement Strategy · Risk Analysis · Conclusion · References.

## v0.2.0 Highlights (2026-06-21)

- **60 verified sources** (up from 30): added eCH standards, GovStack, ZenDiS, EU Data Act,
  Swiss E-ID, GAIA-X v2024, CONSUL Democracy, Blind et al. 2021 open-source TCO study
- **New sections**: §4.11 Total Cost of Ownership Analysis (5-year model, 3 municipality tiers),
  §4.12 Case Studies (Barcelona, Helsinki, Schaffhausen, Bühl, Kirchheim, Aarau),
  §5.6 Small-Municipality Pathway (<20,000 pop, 18-month, €40k–120k), §7.4 EU AI Act Implications
- **Complete German translation** (v0.1.0.de was truncated; v0.2.0.de is full)
- **Self-contained HTML** in English and German (responsive, print-friendly, no external dependencies)

## Key finding (TCO)

A municipality of **50,000 inhabitants** switching to the recommended open-source stack
saves approximately **€1.14 million net over 5 years** vs. a comparable proprietary stack.
A small municipality of 8,000 inhabitants saves **€120,000–180,000** — enough to fund a
part-time digital transformation coordinator throughout the transition.
Source: §4.11 of `Doc/en/sovereign-by-design-v0.2.0.md`.

## Formats

| Format | Where |
|---|---|
| Markdown | `Doc/<lang>/` — source of truth; edit here |
| HTML | `Doc/<lang>/` — committed alongside Markdown; self-contained |
| DOCX, PDF | built by `Scripts/build_govtech_docs.py`; requires pandoc |

## Versioning

Documents use semantic versioning:

| Version | Meaning |
|---|---|
| `v0.1.0` | First structured draft (structure complete, some citations unverified) |
| `v0.2.0` | Citation-complete draft (all sources verified, TCO + case studies added) |
| `v0.3.0` | Planned Q3 2026: UX research, longitudinal data, procurement templates |
| `v1.0.0` | Externally shareable release (peer-reviewed, all formats, all languages) |

## Languages

English is the **single source of truth** (`source-of-truth: true` in frontmatter).
German is a full translation (`source-of-truth: false`, `source-language: en`).
On conflicts, the English version governs.

## Reproduce

```bash
pip install -r requirements.txt

# Build all documents (Markdown → HTML; DOCX/PDF with pandoc)
python3 Scripts/build_govtech_docs.py --version 0.2.0 --lang all --format all

# Validate every citation against the source registry
python3 Scripts/validate_citations.py --paper Doc/en/sovereign-by-design-v0.2.0.md \
                                       --registry Mem/source-registry.md

# Generate the literature-review improvement agenda
python3 Scripts/update_literature_review.py

# Check translation parity between language versions
python3 Scripts/translate_document.py --check
```

## Continuous improvement

The source registry (`Mem/source-registry.md`), literature review state
(`Mem/literature-review-state.md`), and implementation strategy are versioned and
revisited on a **quarterly cadence** (Q3 2026, Q4 2026, Q1 2027…).

Working notes, session logs, open questions, and automation scripts are maintained in
the companion repository: [`sebk4c/thinking-deeply`](https://github.com/SEBK4C/Thinking-Deeply).

## Attribution

> **Sebastian Graf**
> Autonomous Office of Civil Digital Infrastructure
> Public requests and correspondence: [sebk4c@tuta.com](mailto:sebk4c@tuta.com)
