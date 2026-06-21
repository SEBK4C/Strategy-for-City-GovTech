# Scripts — Automation

Reproducible automation for document generation, citation management, literature-review
improvement, and translation validation. All scripts are pure Python and run through
`uv`. They degrade gracefully when optional system tools (pandoc, LibreOffice CLI, or
WeasyPrint native libraries) are absent.

| Script | What it does | Key deps |
|---|---|---|
| [`build_govtech_docs.py`](build_govtech_docs.py) | Render Markdown → DOCX, PDF, HTML into `Doc/build/` | pandoc (preferred), LibreOffice CLI for PDF, or `markdown` + `python-docx` |
| [`generate_html.py`](generate_html.py) | Render standalone HTML next to each Markdown source when same-directory HTML is desired | `mistune` optional |
| [`tco_calculator.py`](tco_calculator.py) | Estimate proprietary vs open-source five-year total cost of ownership scenarios | stdlib only |
| [`validate_citations.py`](validate_citations.py) | Check every inline `[N]` citation resolves to that paper's references; check latest EN source against the active registry; report verification coverage | stdlib only |
| [`smoke_check.py`](smoke_check.py) | Check source completeness, EN/DE word-count sanity, and generated DOCX/HTML/PDF artifacts | `python-docx`, `pypdf` |
| [`update_literature_review.py`](update_literature_review.py) | Print the recurring literature-review agenda (gaps, open questions, due date) | stdlib only |
| [`translate_document.py`](translate_document.py) | Check section-heading parity between the English source of truth and each translation | stdlib only |

## Quick start

```bash
uv sync

uv run python Scripts/validate_citations.py          # CI-friendly: non-zero exit on broken citations
uv run python Scripts/build_govtech_docs.py --formats docx,html
uv run python Scripts/smoke_check.py                 # quick loop smoke gate
uv run python Scripts/tco_calculator.py              # print a sample 5-year TCO comparison
uv run python Scripts/generate_html.py               # optional same-directory HTML render
uv run python Scripts/update_literature_review.py    # print the improvement agenda
uv run python Scripts/translate_document.py --check  # verify EN/DE structural parity
```

For release/CI checks with PDF tooling installed:

```bash
uv run python Scripts/build_govtech_docs.py
uv run python Scripts/smoke_check.py --require-formats docx,html,pdf
```

## Design notes

- **No network access required after `uv sync`.** Scripts operate only on local repository files.
- **Idempotent.** Re-running produces the same outputs; generated artefacts go to
  `Doc/build/` (git-ignored).
- **CI-ready.** `validate_citations.py` and `translate_document.py --check` return a
  non-zero exit code on failure, so they can gate a release.

## The recurring improvement loop

These scripts implement the continuous-improvement workflow described in `Mem/README.md`:
`update_literature_review.py` surfaces what to work on, the registry and review state in
`Mem/` are updated, the papers in `Doc/` are revised and re-versioned, and
`validate_citations.py` gates the result before it is built and released.
