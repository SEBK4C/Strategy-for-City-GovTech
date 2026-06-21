# Branch Audit and Consolidation Notes

Date: 2026-06-21

## Summary

`git fetch --all --prune --tags` found 24 remote branch refs:

- `origin/main`
- 23 `origin/claude/*` branches

The earlier reported count of 28 branches was not present on the remote at fetch time.
The likely explanation is that the earlier number counted deleted/pruned refs, duplicate
local/remote branch names, or branches that no longer exist on GitHub.

The branch set was mostly produced by an hourly coding loop. The branches are not 23
independent strategies; they are overlapping attempts to advance the same repository from
v0.1.0 to v0.2.0, with one branch advancing to v0.3.0.

## What Actually Got Done

The loop did produce useful work:

- A v0.1.0 English and German structured strategy paper.
- A v0.2.0 citation-complete draft in English and German, with many competing variants.
- A v0.3.0 extended draft adding GovStack mapping, EU AI Act coverage, GAIA-X, OSOR, and
  AKDB material.
- A source registry and literature-review memory system.
- Python validation/build scripts.
- A document build workflow for DOCX, PDF, and HTML artifacts.
- A quarterly review workflow concept.
- A TCO calculator script.
- Appendix material for procurement, evaluation, and review workflows.
- Several generated HTML renderings.

The main problem was not absence of work. It was fragmentation: the loop repeatedly
branched before reconciling previous outputs, causing parallel variants of the same
document, registry, and scripts.

## Consolidation Decisions

Promoted into the canonical tree:

| Area | Source branch | Reason |
|---|---|---|
| v0.2.0 EN/DE papers and HTML | `origin/claude/dazzling-meitner-n9i8bj` | Best v0.2.0 pair with passing EN/DE heading parity |
| v0.3.0 EN/DE papers and HTML | `origin/claude/wonderful-lovelace-ozwrds` | Only v0.3.0 branch; adds GovStack, AI Act, GAIA-X, OSOR, AKDB |
| Active `Mem/` files | `origin/claude/wonderful-lovelace-ozwrds` | Most recent v0.3.0 memory state |
| v0.2.0 appendices | `origin/claude/wonderful-lovelace-9j666k` | Only branch with appendix documents |
| `Scripts/tco_calculator.py` | `origin/claude/wonderful-lovelace-ozwrds` | Only branch with a TCO calculator |
| `Scripts/generate_html.py` | `origin/claude/wonderful-lovelace-1ena50` | Standalone same-directory HTML helper |
| `.github/workflows/quarterly-review.yml` | `origin/claude/wonderful-lovelace-9wpquq`, then fixed | Only branch with a scheduled review workflow |
| `CITATION.cff` | `origin/claude/wonderful-lovelace-fgrdfs`, then version-adjusted | Most developed citation metadata |

Preserved but not promoted as canonical:

- Every fetched branch tree is stored under `Archive/branch-snapshots/<branch-name>/`.
- Branch-specific source registries remain in those snapshots because registry IDs were
  not stable across all branches.
- Rich but structurally drifting v0.2.0 drafts remain archived rather than being treated
  as the current source of truth.
- Generated HTML variants are preserved in snapshots, but canonical publication should
  regenerate from Markdown.

## Branch Groups

### Baseline / Existing Main

| Branch | What it contained |
|---|---|
| `main` | v0.1.0 EN/DE papers, build workflow, AGENTS.md, single-branch convention |
| `claude/serene-pascal-f4dm3m` | v0.1.0 EN/DE HTML and CI build workflow; also `origin/HEAD` |

### Early v0.1.0 / Setup Branches

| Branch | What it contained |
|---|---|
| `claude/wonderful-lovelace-cy2l2w` | Early cleanup branch; no committed HTML/workflow |
| `claude/wonderful-lovelace-naeg7w` | German v0.1.0 alternative filename and source-registry expansion |
| `claude/wonderful-lovelace-uruolz` | Early `generate_html.py` and alternate German v0.1.0 filename |

### v0.2.0 Draft / HTML / Memory Variants

| Branch | What it contained |
|---|---|
| `claude/wonderful-lovelace-jlou9h` | Early v0.2.0 EN/DE Markdown |
| `claude/wonderful-lovelace-9j666k` | v0.2.0 appendices and memory updates |
| `claude/wonderful-lovelace-xoxc0x` | v0.2.0 scripts and README updates |
| `claude/wonderful-lovelace-2qef5n` | v0.2.0 EN/DE HTML with embedded CSS |
| `claude/wonderful-lovelace-1bda4x` | v0.2.0 EN/DE pair with heading parity |
| `claude/wonderful-lovelace-91yvss` | v0.2.0 EN/DE pair with heading parity and memory updates |
| `claude/wonderful-lovelace-molc56` | Accessible v0.2.0 HTML outputs |
| `claude/wonderful-lovelace-y76u9x` | README inventory and v0.2.0 availability updates |
| `claude/wonderful-lovelace-2cvfoi` | CI workflow variant and v0.2.0 Markdown |
| `claude/wonderful-lovelace-fgrdfs` | CITATION/Doc README updates and a larger v0.2.0 registry variant |
| `claude/wonderful-lovelace-qu9zam` | README/Doc README updates and alternate German v0.2.0 filename |
| `claude/wonderful-lovelace-7akm8l` | Rich v0.2.0 content and script improvements, but EN/DE outline drift |
| `claude/wonderful-lovelace-1ena50` | `generate_html.py` and v0.2.0 README/table updates |
| `claude/wonderful-lovelace-9wpquq` | German v0.2.0 and quarterly-review workflow |
| `claude/dazzling-meitner-jcb6jc` | v0.2.0 citation-complete EN/DE papers |
| `claude/dazzling-meitner-n9i8bj` | v0.2.0 EN/DE pair with parity; v0.3.0 leads surfaced |
| `claude/wonderful-lovelace-a3kbea` | Late German markdown repair attempt; not canonical because heading structure was broken |
| `claude/wonderful-lovelace-03xyj1` | Milestone references updated toward v0.3.0 |

### v0.3.0 Branch

| Branch | What it contained |
|---|---|
| `claude/wonderful-lovelace-ozwrds` | v0.3.0 EN/DE papers and HTML, v0.3.0 memory files, TCO calculator, new sections for OSOR, GovStack, EU AI Act, GAIA-X, and AKDB |

## Current Canonical Document Set

| Version | English | German |
|---|---|---|
| v0.1.0 | `Doc/en/sovereign-by-design-v0.1.0.md` | `Doc/de/sovereign-by-design-v0.1.0.de.md` |
| v0.2.0 | `Doc/en/sovereign-by-design-v0.2.0.md` | `Doc/de/sovereign-by-design-v0.2.0.de.md` |
| v0.3.0 | `Doc/en/sovereign-by-design-v0.3.0.md` | `Doc/de/sovereign-by-design-v0.3.0.de.md` |

## Caution

Older versioned papers contain their own reference sections. The active source registry
tracks the latest v0.3.0 line; branch-era registries are preserved in branch snapshots
because their numeric IDs sometimes conflict across branches.
