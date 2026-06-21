# Archive

This directory preserves branch-era work from the automated loop runs.

The canonical codebase remains the repository root:

- `Doc/` contains the publishable Markdown sources and committed HTML renders.
- `Mem/` contains the active source registry and review memory.
- `Scripts/` contains the active build, validation, translation, and research helpers.

`Archive/branch-snapshots/` contains full tree snapshots of every remote branch that was
available during the 2026-06-21 consolidation. These snapshots are intentionally outside
`Doc/` so the build and validation scripts do not treat branch-only variants as published
papers.

Start with `branch-audit-2026-06-21.md` for the branch-by-branch summary.
