# Agent & automation conventions

This repository is maintained partly by automated (“loop”) runs. To keep history clean,
those runs follow the conventions below. Humans are welcome to follow them too.

## One branch: `main`

**All work — including every recurring/automated run — happens on `main`.**

- Do **not** create a new per-session branch (e.g. `claude/<name>-<id>`) for routine work.
  Earlier runs did this and fragmented the work across many parallel branches; those have
  been consolidated into `main`.
- Commit directly to `main`, or open a short-lived pull request that is merged into `main`
  in the same run and then deleted. Either way, `main` is the only long-lived branch.
- If a genuinely experimental change needs isolation, use a clearly-named, short-lived
  branch and delete it once merged — never leave per-session branches lingering.

## Why

`main` is the single source of truth. A single branch keeps the literature review, source
registry, generated documents, and version history coherent across recurring runs, and
makes the “self-improving” loop (see `Mem/README.md`) easy to follow over time.

## Working agreement for each run

1. Pull `main`.
2. Do the work (update `Doc/`, `Mem/`, `Scripts/` as needed).
3. Run the gates before publishing:
   - `uv run python Scripts/validate_citations.py`
   - `uv run python Scripts/translate_document.py --check`
   - `uv run python Scripts/build_govtech_docs.py --formats docx,html`
   - `uv run python Scripts/smoke_check.py`
   - For release checks only: `uv run python Scripts/build_govtech_docs.py` and
     `uv run python Scripts/smoke_check.py --require-formats docx,html,pdf`
4. Commit to `main` with a clear, conventional message.
5. Bump the document version when the change warrants it (see `Doc/README.md`).

## Formats & binaries

Markdown and HTML are committed under `Doc/<lang>/`. DOCX and PDF are **not** committed
(they are binary); they are produced by `Scripts/build_govtech_docs.py` and published by
the `Build & Publish Documents` workflow as CI artifacts (every push) and release assets
(on `vX.Y.Z` tags).

## Attribution

Sebastian Graf · Autonomous Office of Civil Digital Infrastructure · sebk4c@tuta.com
