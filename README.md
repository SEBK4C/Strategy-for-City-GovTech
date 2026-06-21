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
| [`Doc/`](Doc/) | Published documents (Markdown source of truth + committed HTML; DOCX/PDF via build) |
| [`Mem/`](Mem/) | Memory: source registry, literature-review state, research notes |
| [`Scripts/`](Scripts/) | Automation: document generation, translation, citation management, validation |

## Papers

### Sovereign by Design: Open-Source Technology Strategy for Municipal Governments

A comprehensively cited strategy for implementing a state-of-the-art, open-source
governmental administration technology stack in city governments of all scales.
Covers Swiss (EMBAG), German (OZG 2.0, SCS, OpenDesk), and EU (Interoperable Europe
Act, Data Act, AI Act, GovStack) policy frameworks; full technology stack evaluation;
36-month phased implementation roadmap; TCO methodology; six case studies.

| Version | Status | EN | DE |
|---|---|---|---|
| v0.1.0 | First structured draft | [Markdown](Doc/en/sovereign-by-design-v0.1.0.md) · [HTML](Doc/en/sovereign-by-design-v0.1.0.html) | [Markdown](Doc/de/sovereign-by-design-v0.1.0.de.md) · [HTML](Doc/de/sovereign-by-design-v0.1.0.de.html) |
| **v0.2.0** | **Citation-Complete Draft** | [**Markdown**](Doc/en/sovereign-by-design-v0.2.0.md) · [**HTML**](Doc/en/sovereign-by-design-v0.2.0.html) | [**Markdown**](Doc/de/sovereign-by-design-v0.2.0.de.md) · [**HTML**](Doc/de/sovereign-by-design-v0.2.0.de.html) |
| v1.0.0 | _Externally shareable release (planned)_ | — | — |

What’s new in v0.2.0 versus v0.1.0:
- **54 citations** (up from ~30), all tracked in `Mem/source-registry.md`
- New sections: GovStack [3.3], EU Data Act [3.7], EU AI Act [3.8, 4.10], Case Studies [8], TCO Methodology [9]
- New appendices: Scorecard template [A], Citizen satisfaction survey [B], Procurement criteria [C], Data classification [D]
- Scale-adjusted roadmap variants and budget ranges for small, medium, and large cities [5.7–5.8]
- Six documented case studies: Barcelona, Schaffhausen, German federal OpenDesk, French LibreOffice, Munich LiMux, Helsinki

## Scientific structure

Each paper follows a rigorous academic structure:

> Abstract · Introduction · Methodology · Literature Review · Technology Stack Analysis ·
> Implementation Roadmap · Stakeholder & Procurement Strategy · Risk Analysis · Case Studies ·
> TCO Methodology · Conclusion · References · Appendices

## Formats

| Format | Where | How generated |
|---|---|---|
| Markdown | `Doc/<lang>/` | Source of truth; edit here |
| HTML | `Doc/<lang>/` | Committed alongside Markdown |
| DOCX, PDF | `Doc/build/` (local) | `python3 Scripts/build_govtech_docs.py` |

## Versioning

Documents use semantic versioning:

| Version | Meaning |
|---|---|
| `v0.1.0` | First structured draft (structure complete, some citations unverified) |
| `v0.2.0` | Citation-complete draft (all sources tracked; ~85% verified against primaries) |
| `v1.0.0` | Externally shareable release (all citations verified; external review complete) |

## Languages

English is the **single source of truth**. All translations derive from it and carry
`source-of-truth: false` + `source-document:` in their YAML front matter.
The system is designed so additional languages can be added without rewriting source
material.

## Reproduce locally

```bash
pip install -r requirements.txt

# Build all documents (Markdown → DOCX → PDF → HTML)
python3 Scripts/build_govtech_docs.py

# Validate every citation against the source registry
python3 Scripts/validate_citations.py

# Generate the literature-review improvement agenda (quarterly input)
python3 Scripts/update_literature_review.py

# Check translation parity between language versions
python3 Scripts/translate_document.py --check
```

## Continuous improvement

The source registry, literature review, and implementation strategy are revisited on a
**quarterly cadence**. Each cycle:

1. Run `python3 Scripts/update_literature_review.py` to generate the agenda.
2. Research the surfaced gaps and add sources to `Mem/source-registry.md`.
3. Update `Mem/literature-review-state.md` with what changed.
4. Revise the papers under `Doc/` and bump the version.
5. Run `python3 Scripts/validate_citations.py` to verify all citations resolve.

See `Mem/literature-review-state.md` for the current gap analysis and v0.3.0 targets.

## Attribution

> **Sebastian Graf**  
> Autonomous Office of Civil Digital Infrastructure  
> Public requests and correspondence: [sebk4c@tuta.com](mailto:sebk4c@tuta.com)
