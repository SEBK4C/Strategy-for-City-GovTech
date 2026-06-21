# Project Requirements and Plan

Reviewed: 2026-06-21
Branch: `consolidation/all-branches-20260621`

This document is the working plan for turning the consolidated branch into a coherent,
recurring, self-improving codebase. It is intentionally operational: every future loop
run should update this file when it changes scope, completes work, or discovers a new
gap.

## Product Goal

Build a reproducible publishing system for municipal GovTech strategy papers:

- The paper content has one canonical source of truth.
- Python automation builds publication formats from that source.
- The project can generate Markdown, HTML, DOCX, and PDF outputs.
- Research evidence, source verification, translations, and release state are tracked in
  the repo.
- Recurring improvement loops refine the paper without fragmenting the repository into
  many abandoned branches.

## Current Status Summary

The project has useful substance, but many features are only partially implemented.

| Area | Status | Current evidence | Main gap |
|---|---|---|---|
| Branch consolidation | Partial | Consolidation branch exists; all fetched branches archived under `Archive/branch-snapshots/`; audit exists | Not merged to `main`; old remote branches not deleted |
| Canonical content | Partial | Versioned Markdown papers exist for v0.1.0, v0.2.0, v0.3.0 in EN/DE | No manifest declares latest canonical source, generated outputs, and version lineage |
| Multi-format build | Partial | `Scripts/build_govtech_docs.py` builds DOCX and HTML locally; PDF path supports pandoc, LibreOffice CLI, or WeasyPrint | PDF depends on system tools; LibreOffice path is implemented but not locally/CI smoke-tested |
| Dependencies | Mostly done | `pyproject.toml`, `uv.lock`, uv-based workflows | Need keep all future tooling on `uv`/`uvx`; no ad hoc `pip install` |
| Citation validation | Mostly done | `uv run python Scripts/validate_citations.py` passes; active registry shows 51/51 verified | Historical branch registries conflict; German v0.3 has two reference entries not cited inline |
| Translation validation | Partial | Heading parity check passes for EN/DE | It only checks structure, not prose freshness, terminology consistency, or citation meaning |
| Smoke/sanity gates | Mostly done | `Scripts/smoke_check.py` checks source length, EN/DE word-count parity, and generated artifact word-count parity | PDF word-count gate runs only where PDF tooling is installed |
| Self-improvement loop | Partial | `update_literature_review.py` prints agenda; quarterly workflow creates an issue | Loop does not yet update this plan, write review reports, or implement research changes |
| TCO model | Prototype | `Scripts/tco_calculator.py` runs | Assumptions are hard-coded; no sensitivity tables, tests, or paper integration |
| Publishing/release | Partial | GitHub Actions workflow builds and uploads artifacts | Consolidated branch has not run in CI; release artifact path is not yet proven after consolidation |
| Governance | Partial | `AGENTS.md` says use one long-lived branch | Needs merge/branch cleanup decision and a repeatable loop playbook |

## Requirements Matrix

### R1. Single Repository State

Requirement: `main` is the only long-lived branch. Automated loops must not create a new
branch for every run.

Current implementation:

- `AGENTS.md` documents the one-branch rule.
- `Archive/branch-audit-2026-06-21.md` records what each fetched branch contained.
- Every fetched branch tree is preserved under `Archive/branch-snapshots/`.

Acceptance criteria:

- [ ] Consolidation branch reviewed and merged to `main`.
- [ ] Old remote loop branches deleted only after explicit approval.
- [ ] Future loop instructions mention `uv` commands and the one-branch rule.
- [ ] `PLAN.md` is updated by every recurring improvement cycle.

### R2. Canonical Source of Truth

Requirement: The content source must be unambiguous and versioned. Generated files must
be reproducible from that source.

Current implementation:

- Markdown files under `Doc/en/` are treated as source of truth.
- German files under `Doc/de/` are translations derived from English.
- HTML renderings are committed next to Markdown.
- DOCX/PDF are generated into `Doc/build/` and not committed.

Gaps:

- No machine-readable manifest declares latest version, translation relationships,
  generated artifacts, and release status.
- Committed HTML can drift from Markdown unless regenerated and checked.
- Appendices are v0.2.0 while the main paper is v0.3.0.

Acceptance criteria:

- [ ] Add `Doc/manifest.yml` or equivalent canonical manifest.
- [ ] Add a check that committed HTML matches Markdown generation, or move HTML fully to
      generated artifacts.
- [ ] Define whether appendices should be versioned to v0.3.0 or remain independent.
- [ ] Record every released version and language pair in one place.

### R3. Multi-Format Document Generation

Requirement: The repo must generate Markdown, HTML, DOCX, and PDF from the same source
using a Python/uv workflow, with LibreOffice CLI available as a supported conversion
path.

Current implementation:

- Markdown is the committed input format.
- `build_govtech_docs.py` generates DOCX, PDF, and HTML into `Doc/build/`.
- `generate_html.py` can regenerate same-directory HTML.
- PDF generation can use pandoc, LibreOffice CLI, or WeasyPrint if available.

Gaps:

- Local machine currently lacks `pandoc`, `soffice`/`libreoffice`, and WeasyPrint native
  libraries, so only DOCX/HTML were locally verified.
- CI installs pandoc and WeasyPrint libraries, but not LibreOffice.
- DOCX styling is functional but not yet publication-grade.
- PDF visual quality is not verified by screenshots or page rendering.

Acceptance criteria:

- [ ] CI proves PDF generation on Ubuntu.
- [ ] Add a LibreOffice smoke test in CI or a documented local command.
- [x] Add artifact checks: expected files exist for each language/version and are nonzero.
- [ ] Improve DOCX styles for headings, tables, code, references, and title metadata.
- [ ] Add a visual/render QA step for PDF when feasible.

### R4. Dependencies and Tooling

Requirement: Use `uv` for project dependencies and `uvx` for one-off Python CLIs.

Current implementation:

- `pyproject.toml` and `uv.lock` define Python dependencies.
- GitHub workflows use `uv`.
- Root `requirements.txt` has been removed.

Acceptance criteria:

- [ ] No active docs instruct `pip install` or `python3 Scripts/...`.
- [ ] Any future formatter, linter, or link checker is run through `uv run` or `uvx`.
- [ ] Optional system dependencies are documented separately from Python dependencies.

### R5. Evidence and Citation Integrity

Requirement: Every paper citation must resolve, and the active source registry must track
verification status and metadata.

Current implementation:

- `validate_citations.py` passes on the active tree.
- Active v0.3 registry coverage is 51/51 verified.
- Branch-era registries are archived because numeric IDs conflicted across branches.

Gaps:

- German v0.3.0 has reference entries `[39, 41]` not cited inline.
- No URL/link checker.
- No stable source identifier independent of visible citation number.
- No process for capturing/archiving primary source copies where legally permissible.

Acceptance criteria:

- [ ] Fix or intentionally document the uncited German references.
- [ ] Add stable registry IDs separate from paper-local citation numbers.
- [ ] Add a link-check or source freshness report, using cached results where possible.
- [ ] Define source archival policy and storage location.

### R6. Translation Quality

Requirement: Translations must remain structurally and substantively aligned with the
English source of truth.

Current implementation:

- `translate_document.py --check` verifies heading parity.
- EN/DE parity currently passes.

Gaps:

- No check for stale paragraphs after English updates.
- No glossary for recurring German terminology.
- No validation that citation numbers still refer to semantically matching sources.

Acceptance criteria:

- [ ] Add translation metadata with source checksum or source version.
- [x] Add EN/DE word-count sanity checks to catch truncated translations.
- [ ] Add a project glossary for German GovTech terms.
- [ ] Add a review checklist for translation updates after English source changes.

### R7. Self-Improvement Loop

Requirement: A scheduled loop should surface research gaps, update evidence, revise
papers, validate outputs, and leave an auditable trail.

Current implementation:

- `update_literature_review.py` prints open gaps and quarterly checklist items.
- `quarterly-review.yml` can create a GitHub issue and upload reports.
- `Mem/` stores research state, source registry, and notes.

Gaps:

- The loop currently creates an agenda but does not implement updates automatically.
- No durable report directory for completed review cycles.
- No rule that the loop updates this plan and closes completed items.
- No triage separation between content work, tooling work, and release work.

Acceptance criteria:

- [ ] Add `Reports/quarterly-review/YYYY-MM-DD.md` outputs or issue-to-report export.
- [ ] Quarterly loop updates `PLAN.md` status when work is completed or deferred.
- [ ] Review issue templates link to specific acceptance criteria.
- [x] Each loop has a quick smoke gate that exits nonzero on obvious output breakage.
- [ ] Each loop runs validation/build gates before any commit or PR.

### R8. TCO Model

Requirement: The TCO model should be transparent, configurable, cited, and reusable in
the strategy paper.

Current implementation:

- `Scripts/tco_calculator.py` prints a five-year proprietary vs open-source comparison.

Gaps:

- Assumptions are hard-coded.
- No tests or validation against known scenarios.
- Output is not integrated into the paper as generated tables.
- No sensitivity analysis.

Acceptance criteria:

- [ ] Move assumptions into `Data/tco-assumptions.yml`.
- [ ] Add tests for baseline scenarios.
- [ ] Generate Markdown tables for inclusion in the paper.
- [ ] Add sensitivity analysis for staff count, hosting cost, migration cost, and support
      subscriptions.

### R9. Publishing and Release

Requirement: The project should produce traceable, citable releases with generated
artifacts.

Current implementation:

- Build workflow uploads generated documents as artifacts.
- Versioning policy exists in `Doc/README.md`.
- `CITATION.cff` exists.

Gaps:

- Consolidated branch has not been run through remote CI.
- Release asset attachment path is not proven after consolidation.
- No changelog or release checklist.

Acceptance criteria:

- [ ] Add `CHANGELOG.md`.
- [ ] Add `RELEASE.md` checklist.
- [ ] Prove release artifact upload on a test tag or first post-consolidation release.
- [ ] Ensure `CITATION.cff`, document version, and tag version agree.

### R10. Smoke and Sanity Checks

Requirement: Every self-improvement loop must exit nonzero if the repository is
obviously incomplete, truncated, or unable to generate expected artifacts.

Quick loop gate:

```bash
uv run python Scripts/validate_citations.py
uv run python Scripts/translate_document.py --check
uv run python Scripts/build_govtech_docs.py --formats docx,html
uv run python Scripts/smoke_check.py
```

Release/CI gate:

```bash
uv run python Scripts/build_govtech_docs.py
uv run python Scripts/smoke_check.py --require-formats docx,html,pdf
```

The smoke check fails on:

- Missing, empty, or tiny Markdown sources.
- Missing H1 headings or merge-conflict markers.
- EN/DE word counts outside the rough translation band.
- Missing/empty generated artifacts.
- DOCX/HTML/PDF word counts far outside the Markdown source band.

## Open Decisions for Sebastian

1. Should Markdown remain the canonical content source, with Python enforcing and
   publishing it, or should the paper move into a more structured Python/YAML content
   model?
2. Should committed HTML remain in `Doc/<lang>/`, or should all generated HTML live only
   in `Doc/build/` and CI artifacts?
3. Should PDF generation prefer pandoc or LibreOffice in CI?
4. Should the full branch snapshots stay inside this repo long term, or move to an
   external archive after the consolidation is reviewed?
5. Should future loop runs commit directly to `main`, or open short-lived PRs that are
   reviewed and merged?

## Milestone Plan

### M0. Finish Consolidation

- [ ] Review this plan with Sebastian.
- [ ] Run the full uv verification suite.
- [ ] Commit the consolidation branch.
- [ ] Push and open a PR or merge to `main`, depending on governance choice.
- [ ] Delete old remote `claude/*` branches only after explicit approval.

### M1. Harden the Build System

- [ ] Add `Doc/manifest.yml`.
- [ ] Add artifact existence checks for all source documents.
- [ ] Add CI coverage for PDF generation and, if chosen, LibreOffice.
- [ ] Improve DOCX/PDF styling.
- [ ] Decide committed HTML policy and enforce it.

### M2. Prepare v0.4 Content Release

- [ ] Fix known German v0.3 reference/citation note.
- [ ] Version or reconcile appendices with v0.3.
- [ ] Integrate TCO output into the paper.
- [ ] Review archived branches for any remaining unique content worth promoting.
- [ ] Update `Mem/literature-review-state.md` after those decisions.

### M3. Make the Improvement Loop Real

- [ ] Add durable quarterly review reports.
- [ ] Make review issues reference this plan.
- [ ] Add stable source identifiers and source freshness reporting.
- [ ] Add loop rule: update `PLAN.md` in every cycle.

### M4. External Release Readiness

- [ ] Add changelog and release checklist.
- [ ] Run post-consolidation CI successfully.
- [ ] Produce release artifacts for EN/DE Markdown, HTML, DOCX, and PDF.
- [ ] Prepare v1.0 review path: external reviewers, citation audit, translation audit,
      and municipal implementation review.
