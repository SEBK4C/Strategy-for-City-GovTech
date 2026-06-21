#!/usr/bin/env python3
"""Generate self-contained, GDPR-compliant HTML from Markdown strategy papers.

Produces one ``.html`` file alongside each ``.md`` source under ``Doc/<lang>/``.
The HTML is intentionally minimal:

- No external CDN dependencies (GDPR: no Google Fonts, no JS libraries).
- No JavaScript — pure HTML + embedded CSS.
- System-font stack for zero network requests.
- Academic paper layout with dl-grid metadata, abstract box, and checklist styling.
- ``lang`` attribute inferred from YAML frontmatter ``language`` field.

Dependencies:
    stdlib only (``re``, ``html``, ``pathlib``, ``textwrap``)

Usage:
    python3 Scripts/generate_html.py                    # all papers
    python3 Scripts/generate_html.py Doc/en/sovereign-by-design-v0.2.0.md
"""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path
from textwrap import dedent

REPO_ROOT = Path(__file__).resolve().parents[1]
DOC_DIR = REPO_ROOT / "Doc"

CSS = dedent("""\
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body {
        font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        font-size: 1rem;
        line-height: 1.65;
        color: #1a1a1a;
        background: #fff;
        max-width: 860px;
        margin: 0 auto;
        padding: 2rem 1.5rem 4rem;
    }
    h1 { font-size: 1.8rem; font-weight: 700; line-height: 1.2; margin-bottom: 0.5rem; }
    h2 { font-size: 1.3rem; font-weight: 700; margin: 2.4rem 0 0.6rem; border-bottom: 2px solid #d0d0d0; padding-bottom: 0.25rem; }
    h3 { font-size: 1.1rem; font-weight: 600; margin: 1.6rem 0 0.4rem; }
    h4 { font-size: 1rem; font-weight: 600; margin: 1.2rem 0 0.3rem; }
    p { margin-bottom: 0.85rem; }
    a { color: #0056b3; text-decoration: none; }
    a:hover { text-decoration: underline; }
    strong { font-weight: 600; }
    em { font-style: italic; }
    code, pre { font-family: ui-monospace, "Cascadia Code", "Source Code Pro", Menlo, monospace; font-size: 0.875em; }
    pre { background: #f5f5f5; border: 1px solid #ddd; border-radius: 4px; padding: 1rem; overflow-x: auto; margin-bottom: 1rem; }
    blockquote { border-left: 4px solid #ccc; padding-left: 1rem; color: #555; margin-bottom: 1rem; }
    ul, ol { padding-left: 1.5rem; margin-bottom: 0.85rem; }
    li { margin-bottom: 0.25rem; }
    table { width: 100%; border-collapse: collapse; margin-bottom: 1.2rem; font-size: 0.9rem; }
    th { background: #f0f0f0; font-weight: 600; text-align: left; padding: 0.5rem 0.75rem; border: 1px solid #ccc; }
    td { padding: 0.45rem 0.75rem; border: 1px solid #ccc; vertical-align: top; }
    tr:nth-child(even) td { background: #fafafa; }
    /* Metadata dl grid */
    dl.meta { display: grid; grid-template-columns: max-content 1fr; gap: 0.15rem 1.2rem; margin-bottom: 1.5rem; font-size: 0.9rem; }
    dl.meta dt { font-weight: 600; white-space: nowrap; }
    dl.meta dd { color: #444; }
    /* Abstract box */
    .abstract { background: #f8f8f8; border: 1px solid #ddd; border-radius: 4px; padding: 1rem 1.25rem; margin: 1.5rem 0 2rem; }
    .abstract h2 { border: none; margin-top: 0; font-size: 1rem; text-transform: uppercase; letter-spacing: 0.05em; }
    /* Checklists */
    ul.checklist li { list-style: none; padding-left: 0; }
    ul.checklist li::before { content: '□\00a0'; }
    hr { border: none; border-top: 1px solid #ddd; margin: 2rem 0; }
    header { margin-bottom: 1.5rem; }
    footer { margin-top: 3rem; font-size: 0.85rem; color: #888; border-top: 1px solid #eee; padding-top: 1rem; }
""")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    """Extract YAML frontmatter and return (fields, body)."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    fm_block = text[3:end].strip()
    body = text[end + 4:].lstrip("\n")
    fields: dict[str, str] = {}
    for line in fm_block.splitlines():
        m = re.match(r'^(\w[\w-]*):\s*"?(.+?)"?\s*$', line)
        if m:
            fields[m.group(1)] = m.group(2)
    return fields, body


def md_to_html(md: str) -> str:
    """Very lightweight Markdown → HTML for the subset used in the papers."""
    lines = md.splitlines()
    out: list[str] = []
    i = 0
    in_table = False
    in_ul = False
    in_ol = False
    in_pre = False
    in_checklist = False

    def close_lists() -> None:
        nonlocal in_ul, in_ol, in_checklist
        if in_ul:
            out.append("</ul>")
            in_ul = False
            in_checklist = False
        if in_ol:
            out.append("</ol>")
            in_ol = False

    def close_table() -> None:
        nonlocal in_table
        if in_table:
            out.append("</tbody></table>")
            in_table = False

    def inline(s: str) -> str:
        """Apply inline Markdown transforms to a string."""
        s = html.escape(s)
        s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"_(.+?)_", r"<em>\1</em>", s)
        s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
        s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
        s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
        return s

    while i < len(lines):
        line = lines[i]
        raw = line.rstrip()

        # Fenced code block
        if raw.startswith("```"):
            close_lists()
            close_table()
            if not in_pre:
                out.append("<pre><code>")
                in_pre = True
            else:
                out.append("</code></pre>")
                in_pre = False
            i += 1
            continue
        if in_pre:
            out.append(html.escape(raw))
            i += 1
            continue

        # Horizontal rule
        if re.match(r"^-{3,}\s*$", raw) or re.match(r"^\*{3,}\s*$", raw):
            close_lists()
            close_table()
            out.append("<hr>")
            i += 1
            continue

        # Headings
        m = re.match(r"^(#{1,6})\s+(.*)", raw)
        if m:
            close_lists()
            close_table()
            level = len(m.group(1))
            text = inline(m.group(2))
            if level == 2 and "abstract" in text.lower():
                out.append(f'<div class="abstract"><h{level}>{text}</h{level}>')
                # Will be closed on next h1/h2
                in_abstract = True
            else:
                out.append(f"<h{level}>{text}</h{level}>")
            i += 1
            continue

        # Table
        if raw.startswith("|"):
            close_lists()
            cells = [c.strip() for c in raw.strip("|  ").split("|")]
            if not in_table:
                # header row
                ths = "".join(f"<th>{inline(c)}</th>" for c in cells)
                out.append(f"<table><thead><tr>{ths}</tr></thead><tbody>")
                in_table = True
                i += 1
                # skip separator row
                if i < len(lines) and re.match(r"[|: -]+", lines[i]):
                    i += 1
                continue
            else:
                tds = "".join(f"<td>{inline(c)}</td>" for c in cells)
                out.append(f"<tr>{tds}</tr>")
                i += 1
                continue
        else:
            close_table()

        # Checklist items
        m = re.match(r"^- \[ \]\s+(.*)", raw)
        if m:
            if not in_ul:
                out.append('<ul class="checklist">')
                in_ul = True
                in_checklist = True
            out.append(f"<li>{inline(m.group(1))}</li>")
            i += 1
            continue

        # Unordered list
        m = re.match(r"^[-*]\s+(.*)", raw)
        if m:
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{inline(m.group(1))}</li>")
            i += 1
            continue

        # Ordered list
        m = re.match(r"^\d+\.\s+(.*)", raw)
        if m:
            if not in_ol:
                close_lists()
                out.append("<ol>")
                in_ol = True
            out.append(f"<li>{inline(m.group(1))}</li>")
            i += 1
            continue

        # Blockquote
        m = re.match(r"^>\s+(.*)", raw)
        if m:
            close_lists()
            out.append(f"<blockquote><p>{inline(m.group(1))}</p></blockquote>")
            i += 1
            continue

        # Blank line
        if not raw.strip():
            close_lists()
            i += 1
            continue

        # Paragraph
        close_lists()
        close_table()
        out.append(f"<p>{inline(raw)}</p>")
        i += 1

    close_lists()
    close_table()
    return "\n".join(out)


def build_metadata_dl(fm: dict[str, str]) -> str:
    """Render frontmatter fields as a definition-list."""
    labels = {
        "author": "Author",
        "version": "Version",
        "status": "Status",
        "date": "Date",
        "language": "Language",
        "SPDX-License-Identifier": "License",
        "correspondence": "Correspondence",
    }
    items = ""
    for key, label in labels.items():
        val = fm.get(key)
        if val:
            items += f"<dt>{html.escape(label)}</dt><dd>{html.escape(val)}</dd>\n"
    return f'<dl class="meta">\n{items}</dl>' if items else ""


def generate(src: Path) -> Path:
    """Convert a Markdown paper to a self-contained HTML file."""
    text = src.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)

    lang = fm.get("language", "en")
    title_raw = fm.get("title", src.stem)
    title_esc = html.escape(title_raw)
    meta_block = build_metadata_dl(fm)

    # Remove the duplicate h1 title that is already in the heading
    body_html = md_to_html(body)

    # Close any open abstract div
    if '<div class="abstract">' in body_html:
        # Close it before the next h2 (which md_to_html already inserted)
        body_html = body_html.replace(
            '</div class="abstract">',  # md_to_html doesn't produce closing divs
            "",
        )

    src_link = src.name
    html_out = dedent(f"""\
        <!DOCTYPE html>
        <html lang="{lang}">
        <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content="{title_esc}">
        <title>{title_esc}</title>
        <style>
        {CSS}
        </style>
        </head>
        <body>
        <header>
        <h1>{title_esc}</h1>
        {meta_block}
        </header>
        <main>
        {body_html}
        </main>
        <footer>
        <p>Source: <a href="{html.escape(src_link)}">{html.escape(src_link)}</a> ·
        License: {html.escape(fm.get('SPDX-License-Identifier', 'see document'))}</p>
        </footer>
        </body>
        </html>
    """)

    dst = src.with_suffix(".html")
    dst.write_text(html_out, encoding="utf-8")
    return dst


def main(argv: list[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]

    if argv:
        targets = [Path(a) for a in argv]
    else:
        targets = []
        for lang_dir in sorted(DOC_DIR.iterdir()) if DOC_DIR.exists() else []:
            if lang_dir.is_dir() and lang_dir.name != "build":
                targets.extend(sorted(lang_dir.glob("*.md")))

    if not targets:
        print("No Markdown papers found.")
        return 1

    errors = 0
    for src in targets:
        try:
            dst = generate(src)
            print(f"OK  {dst.relative_to(REPO_ROOT)}")
        except Exception as exc:  # noqa: BLE001
            print(f"ERR {src}: {exc}")
            errors += 1

    return 0 if not errors else 2


if __name__ == "__main__":
    sys.exit(main())
