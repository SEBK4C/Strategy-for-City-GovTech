# Scripts — Automation

Reproducible automation for document generation, citation management, literature-review
improvement, and translation validation. All scripts are pure Python 3.9+ and degrade
gracefully when optional dependencies (pandoc, weasyprint) are absent.

| Script | What it does | Key deps |
|---|---|---|
| [`build_govtech_docs.py`](build_govtech_docs.py) | Render Markdown → DOCX, PDF, HTML into `Doc/build/` | pandoc (preferred) or `markdown` + `python-docx` |
| [`validate_citations.py`](validate_citations.py) | Check every inline `[N]` citation resolves to a reference and a registry entry; report verification coverage | stdlib only |
| [`update_literature_review.py`](update_literature_review.py) | Print the recurring literature-review agenda (gaps, open questions, due date) | stdlib only |
| [`translate_document.py`](translate_document.py) | Check section-heading parity between the English source of truth and each translation | stdlib only |

## Quick start

```bash
pip install -r requirements.txt

python3 Scripts/validate_citations.py          # CI-friendly: non-zero exit on broken citations
python3 Scripts/build_govtech_docs.py          # build all four formats for every paper
python3 Scripts/update_literature_review.py    # print the improvement agenda
python3 Scripts/translate_document.py --check   # verify EN/DE structural parity
```

## Design notes

- **No network access required.** Scripts operate only on local repository files.
- **Idempotent.** Re-running produces the same outputs; generated artefacts go to
  `Doc/build/` (git-ignored).
- **CI-ready.** `validate_citations.py` and `translate_document.py --check` return a
  non-zero exit code on failure, so they can gate a release.

## The recurring improvement loop

These scripts implement the continuous-improvement workflow described in `Mem/README.md`:
`update_literature_review.py` surfaces what to work on, the registry and review state in
`Mem/` are updated, the papers in `Doc/` are revised and re-versioned, and
`validate_citations.py` gates the result before it is built and released.
