# Mem — Memory, Research State & Source Registry

This directory is the project's durable memory. It holds the source registry, the
literature-review state, and the running research notes that make the literature review
**self-improving** across recurring cycles.

## Files

| File | Purpose |
|---|---|
| [`source-registry.md`](source-registry.md) | Canonical registry of every cited source, with full metadata (language, jurisdiction, issuer, date, title, URL, licence/reuse status, verification status) |
| [`literature-review-state.md`](literature-review-state.md) | Coverage map, gap analysis, and improvement log for the literature review |
| [`research-notes.md`](research-notes.md) | Append-only findings, open questions, leads, and working hypotheses |

## The improvement loop

This project is designed to get better every cycle. The recurring loop is:

```
  ┌─▶ 1. update_literature_review.py prints the quarterly review agenda
  │   2. Research the open questions in research-notes.md
  │   3. Add/verify sources in source-registry.md (update verification status)
  │   4. Update coverage map + gaps in literature-review-state.md
  │   5. Revise the papers in /Doc; bump the semantic version
  └─── 6. validate_citations.py must pass before release
```

Each pass should raise the citation-completeness and coverage of the review, moving the
papers from `v0.1.0` (structured draft) → `v0.2.0` (citation-complete) → `v1.0.0`
(externally shareable).

## Verification status vocabulary

| Status | Meaning |
|---|---|
| `unverified` | Cited from secondary knowledge; primary not yet confirmed |
| `verified` | Confirmed against the primary source |
| `archived` | Primary captured/archived where legally permissible |

## Attribution

Sebastian Graf · Autonomous Office of Civil Digital Infrastructure · sebk4c@tuta.com
