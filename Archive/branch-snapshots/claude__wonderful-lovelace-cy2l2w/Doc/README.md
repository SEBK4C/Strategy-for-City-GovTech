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
│  └─ sovereign-by-design-v0.1.0.md
├─ de/                 Deutsch (full translation)
│  └─ sovereign-by-design-v0.1.0.de.md
└─ build/              Generated artefacts (DOCX/PDF/HTML) — git-ignored
```

## Documents

| Title | Version | EN | DE | Status |
|---|---|---|---|---|
| Sovereign by Design | v0.1.0 | [md](en/sovereign-by-design-v0.1.0.md) | [md](de/sovereign-by-design-v0.1.0.de.md) | First structured draft |

## Version scheme (semantic versioning)

| Version | Meaning |
|---|---|
| `v0.1.x` | First structured draft — structure complete, some citations unverified |
| `v0.2.x` | Citation-complete draft — all sources verified against primaries |
| `v1.0.0` | Externally shareable release |

When a document changes version, copy it to a new filename carrying the new version, so
prior releases remain immutable and citable.

## Build (Markdown → DOCX → PDF → HTML)

```bash
pip install -r requirements.txt
python3 Scripts/build_govtech_docs.py                    # build everything
python3 Scripts/build_govtech_docs.py Doc/en/sovereign-by-design-v0.1.0.md   # one file
```

## Adding a language

The English version under `en/` is the single source of truth. To add a language:

1. Create `Doc/<lang-code>/` (ISO 639-1, e.g. `fr`, `it`).
2. Copy the English source into it, renaming with the language suffix:
   `cp en/sovereign-by-design-v0.1.0.md <lang>/sovereign-by-design-v0.1.0.<lang>.md`
3. Translate the copy; keep the YAML front-matter keys identical, set `language:` and
   `translated-from:`.
4. Register the language in `Scripts/translate_document.py` (`LANGUAGES`).
5. Add a column/row to the table above.

Structural changes (new sections, reference renumbering) are made to the **English source
first**, then propagated to translations. `Scripts/translate_document.py --check` reports
sections that have drifted out of parity.

## Licence

Documents are released under **CC-BY-4.0**.
Attribute as: *Sebastian Graf, Autonomous Office of Civil Digital Infrastructure (sebk4c@tuta.com)*
