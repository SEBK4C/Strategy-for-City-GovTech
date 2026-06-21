# Scripts — Automation

Reproducible automation for document generation, citation management, literature-review
improvement, and translation validation. All scripts are pure Python 3.9+ and degrade
gracefully when optional dependencies (pandoc, weasyprint) are absent.

| Script | What it does | Key deps |
|---|---|---|
| [`build_govtech_docs.py`](build_govtech_docs.py) | Render Markdown → DOCX, PDF, HTML into `Doc/build/` | pandoc (preferred) or `markdown` + `python-docx` |
| [`generate_html.py`](generate_html.py) | Generate self-contained, GDPR-compliant HTML from Markdown papers (no pandoc, no CDN) | stdlib only |
| [`validate_citations.py`](validate_citations.py) | Check every inline `[N]` citation resolves to a reference and a registry entry; report verification coverage | stdlib only |
| [`update_literature_review.py`](update_literature_review.py) | Print the recurring literature-review agenda (gaps, open questions, due date) | stdlib only |
| [`translate_document.py`](translate_document.py) | Check section-heading parity between the English source of truth and each translation | stdlib only |

## Quick start

```bash
pip install -r requirements.txt   # optional: only needed for build_govtech_docs.py

python3 Scripts/validate_citations.py          # CI-friendly: non-zero exit on broken citations
python3 Scripts/generate_html.py               # generate HTML for all papers in Doc/<lang>/
python3 Scripts/build_govtech_docs.py          # build DOCX and PDF (requires pandoc)
python3 Scripts/update_literature_review.py    # print the improvement agenda
python3 Scripts/translate_document.py --check  # verify EN/DE structural parity
```

## generate_html.py in detail

`generate_html.py` converts each `Doc/<lang>/*.md` paper to a self-contained `.html` file
alongside the source:

- **No external CDN dependencies** — GDPR-safe from day one (no Google Fonts, no JS).
- **System-font stack** — zero network requests; works offline.
- **Lang attribute** — inferred from YAML frontmatter `language:` field.
- **Academic layout** — metadata dl-grid, abstract box, checklist styling.
- **Idempotent** — safe to re-run; overwrites existing HTML in place.

Run it after every paper revision to keep HTML versions in sync.

## Design notes

- **No network access required.** Scripts operate only on local repository files.
- **Idempotent.** Re-running produces the same outputs; build artefacts (DOCX, PDF) go to
  `Doc/build/` (git-ignored). HTML is written alongside the source file and is tracked.
- **CI-ready.** `validate_citations.py` and `translate_document.py --check` return a
  non-zero exit code on failure, so they can gate a release.

## The recurring improvement loop

These scripts implement the continuous-improvement workflow described in the Mem/ directory:

1. `update_literature_review.py` — surfaces what to work on
2. Research, then update `Mem/source-registry.md` and `Mem/literature-review-state.md`
3. Revise `Doc/` papers and bump the semantic version
4. `validate_citations.py` — gates the result before release
5. `generate_html.py` — regenerates HTML versions
6. `build_govtech_docs.py` — builds DOCX and PDF for release milestones
