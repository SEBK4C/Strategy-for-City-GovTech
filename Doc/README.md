# Doc — Published Documents

**Project:** Open-Source Municipal Government Technology Strategy
**Author:** Sebastian Graf, Autonomous Office of Civil Digital Infrastructure
**Correspondence:** sebk4c@tuta.com

This directory holds the published strategy papers. The Markdown files are the **source of
truth**; DOCX, PDF, and HTML are generated from them by `Scripts/build_govtech_docs.py`.

## Layout

```
Doc/
├─ en/                 English (single source of truth)
│  ├─ sovereign-by-design-v0.1.0.md
│  ├─ sovereign-by-design-v0.2.0.md
│  ├─ sovereign-by-design-v0.3.0.md     # latest source of truth
│  └─ appendices-v0.2.0.md
├─ de/                 Deutsch (full translation)
│  ├─ sovereign-by-design-v0.1.0.de.md
│  ├─ sovereign-by-design-v0.2.0.de.md
│  ├─ sovereign-by-design-v0.3.0.de.md  # latest translation
│  └─ appendices-v0.2.0.de.md
└─ build/              DOCX + PDF + HTML, regenerated locally (git-ignored)
```

## Documents & formats

| Title | Version | Markdown | HTML | DOCX | PDF |
|---|---|---|---|---|---|
| Sovereign by Design (EN) | v0.3.0 | [md](en/sovereign-by-design-v0.3.0.md) | [html](en/sovereign-by-design-v0.3.0.html) | build / CI | build / CI |
| Sovereign by Design (DE) | v0.3.0 | [md](de/sovereign-by-design-v0.3.0.de.md) | [html](de/sovereign-by-design-v0.3.0.de.html) | build / CI | build / CI |
| Sovereign by Design (EN) | v0.2.0 | [md](en/sovereign-by-design-v0.2.0.md) | [html](en/sovereign-by-design-v0.2.0.html) | build / CI | build / CI |
| Sovereign by Design (DE) | v0.2.0 | [md](de/sovereign-by-design-v0.2.0.de.md) | [html](de/sovereign-by-design-v0.2.0.de.html) | build / CI | build / CI |
| Sovereign by Design (EN) | v0.1.0 | [md](en/sovereign-by-design-v0.1.0.md) | [html](en/sovereign-by-design-v0.1.0.html) | build / CI | build / CI |
| Sovereign by Design (DE) | v0.1.0 | [md](de/sovereign-by-design-v0.1.0.de.md) | [html](de/sovereign-by-design-v0.1.0.de.html) | build / CI | build / CI |
| Appendices (EN) | v0.2.0 | [md](en/appendices-v0.2.0.md) | build / CI | build / CI | build / CI |
| Appendices (DE) | v0.2.0 | [md](de/appendices-v0.2.0.de.md) | build / CI | build / CI | build / CI |

### Where each format lives

- **Markdown** — committed here, the source of truth, in `en/` and `de/`.
- **HTML** — committed here next to the Markdown (a generated rendering).
- **DOCX & PDF** — binary artefacts. They are **not committed** (the automation that
  authors this repo can only write text through the GitHub API, and binary blobs cannot
  be carried that way). Get them in any of three equivalent ways:
  1. **Build locally:** `uv run python Scripts/build_govtech_docs.py` writes all four formats
     into `Doc/build/<lang>/`.
  2. **CI artefacts:** the *Build & Publish Documents* GitHub Actions workflow
     (`.github/workflows/build-docs.yml`) builds every format on each push and uploads
     them as a downloadable artefact.
  3. **Release assets:** pushing a `vX.Y.Z` tag attaches the DOCX/PDF/HTML to a GitHub
     Release.

  All three regenerate byte-for-byte from the committed Markdown, so the binaries are
  fully reproducible and never drift from the source.

## Version scheme (semantic versioning)

| Version | Meaning |
|---|---|
| `v0.1.x` | First structured draft — structure complete, some citations unverified |
| `v0.2.x` | Citation-complete draft — all sources verified against primaries |
| `v0.3.x` | Extended draft — GovStack, EU AI Act, GAIA-X, OSOR, AKDB, TCO additions |
| `v1.0.0` | Externally shareable release |

When a document changes version, copy it to a new filename carrying the new version, so
prior releases remain immutable and citable.

## Build (Markdown → DOCX → PDF → HTML)

```bash
uv sync
uv run python Scripts/build_govtech_docs.py                    # build everything
uv run python Scripts/build_govtech_docs.py Doc/en/sovereign-by-design-v0.3.0.md   # one file
```

The script prefers `pandoc` (highest fidelity for all four formats), can use
LibreOffice CLI (`soffice`/`libreoffice`) for PDF conversion from generated DOCX, and
falls back to pure-Python renderers (`markdown`, `python-docx`, `weasyprint`) when
system tools are absent.

## Adding a language

The English version under `en/` is the single source of truth. To add a language:

1. `uv run python Scripts/translate_document.py --scaffold <lang>` creates a skeleton copy.
2. Translate the prose; keep all headings, section numbers, tables, and `[N]` citation
   markers intact.
3. Register the language in `Scripts/translate_document.py` (`LANGUAGES`).
4. `uv run python Scripts/translate_document.py --check` verifies structural parity with the
   English source.

Structural changes are made to the **English source first**, then propagated.

## Licence

Documents are released under **CC-BY-4.0**.
Attribute as: *Sebastian Graf, Autonomous Office of Civil Digital Infrastructure (sebk4c@tuta.com)*
