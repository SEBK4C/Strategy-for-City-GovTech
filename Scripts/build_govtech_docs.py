#!/usr/bin/env python3
"""
build_govtech_docs.py -- Build HTML and (optionally) DOCX/PDF outputs from Markdown sources.

Usage:
    python3 Scripts/build_govtech_docs.py                    # build all MD -> HTML
    python3 Scripts/build_govtech_docs.py --docx             # also build DOCX (requires mammoth + docx)
    python3 Scripts/build_govtech_docs.py --pdf              # also build PDF (requires weasyprint)
    python3 Scripts/build_govtech_docs.py --lang en          # only English
    python3 Scripts/build_govtech_docs.py --lang de          # only German

The script reads all *.md files from Doc/en/ and Doc/de/ and produces
corresponding .html files in the same directories.
"""

import pathlib
import re
import sys
import argparse
import datetime
import html

ROOT = pathlib.Path(__file__).parent.parent
DOC = ROOT / "Doc"

HEADER_TEMPLATE = """<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="author" content="Sebastian Graf, Autonomous Office of Civil Digital Infrastructure">
<meta name="description" content="{description}">
<title>{title}</title>
<style>
  :root {{
    --primary: #1a3a5c;
    --accent: #2e7d32;
    --bg: #fafafa;
    --text: #1a1a1a;
    --muted: #666;
    --border: #ddd;
    --code-bg: #f4f4f4;
    --max-width: 860px;
  }}
  *, *::before, *::after {{ box-sizing: border-box; }}
  body {{
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 1rem;
    line-height: 1.7;
    color: var(--text);
    background: var(--bg);
    margin: 0;
    padding: 2rem 1rem;
  }}
  .container {{ max-width: var(--max-width); margin: 0 auto; }}
  h1 {{ font-size: 1.9rem; color: var(--primary); border-bottom: 3px solid var(--primary); padding-bottom: .5rem; }}
  h2 {{ font-size: 1.4rem; color: var(--primary); margin-top: 2.5rem; border-bottom: 1px solid var(--border); padding-bottom: .3rem; }}
  h3 {{ font-size: 1.15rem; color: var(--primary); margin-top: 1.8rem; }}
  h4 {{ font-size: 1rem; color: var(--primary); margin-top: 1.4rem; font-style: italic; }}
  a {{ color: var(--accent); }}
  a:hover {{ color: var(--primary); }}
  blockquote {{ border-left: 4px solid var(--accent); margin: 1.5rem 0; padding: .5rem 1.2rem; color: var(--muted); background: #f0f7f0; }}
  code {{ font-family: 'Courier New', monospace; font-size: .88rem; background: var(--code-bg); padding: .1rem .3rem; border-radius: 3px; }}
  pre {{ background: var(--code-bg); border: 1px solid var(--border); border-radius: 6px; padding: 1rem 1.2rem; overflow-x: auto; }}
  pre code {{ background: none; padding: 0; font-size: .85rem; }}
  table {{ border-collapse: collapse; width: 100%; margin: 1.5rem 0; font-size: .92rem; }}
  th {{ background: var(--primary); color: white; padding: .55rem .8rem; text-align: left; }}
  td {{ padding: .5rem .8rem; border-bottom: 1px solid var(--border); vertical-align: top; }}
  tr:hover td {{ background: #f0f4f8; }}
  .meta {{ color: var(--muted); font-family: sans-serif; font-size: .85rem; margin-bottom: 2rem; line-height: 1.5; }}
  .license {{ font-size: .8rem; color: var(--muted); border-top: 1px solid var(--border); margin-top: 3rem; padding-top: 1rem; }}
  @media print {{
    body {{ font-size: .9rem; }}
    h1, h2, h3 {{ page-break-after: avoid; }}
    pre, table {{ page-break-inside: avoid; }}
  }}
</style>
</head>
<body>
<div class="container">
"""

FOOTER_TEMPLATE = """
<div class="license">
<p>Released under <a href="https://creativecommons.org/licenses/by/4.0/">CC-BY-4.0</a>.
— © Sebastian Graf, Autonomous Office of Civil Digital Infrastructure —
<a href="mailto:sebk4c@tuta.com">sebk4c@tuta.com</a></p>
<p>Generated: {date}</p>
</div>
</div>
</body>
</html>
"""


def md_to_html(md_text: str, lang: str = "en") -> tuple:
    """Very lightweight Markdown -> HTML converter for the govtech papers."""
    lines = md_text.split("\n")
    out = []
    title = "Sovereign by Design"
    description = "Open-Source Technology Strategy for Municipal Governments"
    in_frontmatter = False
    frontmatter_done = False
    in_pre = False
    in_table = False
    in_blockquote = False

    for i, line in enumerate(lines):
        # YAML frontmatter
        if i == 0 and line.strip() == "---":
            in_frontmatter = True
            continue
        if in_frontmatter:
            if line.strip() == "---":
                in_frontmatter = False
                frontmatter_done = True
            elif line.startswith("title:"):
                title = line.split(":", 1)[1].strip().strip('"')
            elif line.startswith("description:") or line.startswith("keywords:"):
                pass
            continue

        # Code blocks
        if line.startswith("```"):
            if in_pre:
                out.append("</code></pre>")
                in_pre = False
            else:
                lang_hint = line[3:].strip()
                out.append(f'<pre><code class="language-{html.escape(lang_hint)}">')
                in_pre = True
            continue
        if in_pre:
            out.append(html.escape(line))
            continue

        # Tables
        if line.startswith("|"):
            if not in_table:
                out.append("<table>")
                in_table = True
            cells = [c.strip() for c in line.split("|")[1:-1]]
            # Detect separator row
            if all(re.match(r":?-+:?", c) for c in cells if c):
                continue
            # Check if this is the first data row (header)
            tag = "th" if not any("<td>" in x or "<th>" in x for x in out[-5:]) else "td"
            out.append("<tr>" + "".join(f"<{tag}>{inline_md(c)}</{tag}>" for c in cells) + "</tr>")
            continue
        if in_table:
            out.append("</table>")
            in_table = False

        # Blockquotes
        if line.startswith("> "):
            if not in_blockquote:
                out.append("<blockquote>")
                in_blockquote = True
            out.append(f"<p>{inline_md(line[2:])}</p>")
            continue
        if in_blockquote:
            out.append("</blockquote>")
            in_blockquote = False

        # Headings
        if line.startswith("#### "):
            out.append(f"<h4>{inline_md(line[5:])}</h4>")
        elif line.startswith("### "):
            out.append(f"<h3>{inline_md(line[4:])}</h3>")
        elif line.startswith("## "):
            out.append(f"<h2>{inline_md(line[3:])}</h2>")
        elif line.startswith("# "):
            first_h1 = line[2:]
            out.append(f"<h1>{inline_md(first_h1)}</h1>")
        elif line.startswith("- ") or line.startswith("* "):
            out.append(f"<li>{inline_md(line[2:])}</li>")
        elif line.startswith("**") and line.endswith("**") and len(line) < 120:
            out.append(f"<p><strong>{inline_md(line[2:-2])}</strong></p>")
        elif line.strip() == "---" or line.strip() == "***":
            out.append("<hr>")
        elif line.strip() == "":
            out.append("")
        else:
            out.append(f"<p>{inline_md(line)}</p>")

    if in_table:
        out.append("</table>")
    if in_blockquote:
        out.append("</blockquote>")

    return title, description, "\n".join(out)


def inline_md(text: str) -> str:
    """Convert inline Markdown to HTML."""
    # Escape HTML first, then restore safe patterns
    text = html.escape(text)
    # Bold
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    # Italic
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    # Code
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
    # Links [text](url)
    text = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', text)
    # Footnote-style citations [N]
    text = re.sub(r"\[(\d+(?:,\s*\d+)*)\]", r"[\1]", text)
    return text


def build_html(md_path: pathlib.Path) -> pathlib.Path:
    md_text = md_path.read_text(encoding="utf-8")
    lang = "de" if "/de/" in str(md_path) or md_path.name.endswith(".de.md") else "en"
    title, description, body_html = md_to_html(md_text, lang)

    # Build meta block
    meta_lines = []
    fm = re.findall(r"^---\n(.*?)^---", md_text, re.DOTALL | re.MULTILINE)
    if fm:
        for line in fm[0].split("\n"):
            if ":" in line and not line.strip().startswith("-"):
                key, _, val = line.partition(":")
                meta_lines.append(f"<strong>{key.strip()}:</strong> {val.strip()}")
    meta_html = "<div class=\"meta\">" + " &nbsp;|&nbsp; ".join(meta_lines[:6]) + "</div>" if meta_lines else ""

    full_html = (
        HEADER_TEMPLATE.format(lang=lang, title=html.escape(title), description=html.escape(description))
        + meta_html
        + body_html
        + FOOTER_TEMPLATE.format(date=datetime.date.today().isoformat())
    )

    out_path = md_path.with_suffix(".html")
    out_path.write_text(full_html, encoding="utf-8")
    return out_path


def main():
    parser = argparse.ArgumentParser(description="Build HTML (and optionally DOCX/PDF) from Markdown")
    parser.add_argument("--lang", choices=["en", "de", "all"], default="all")
    parser.add_argument("--docx", action="store_true", help="Also generate DOCX (requires python-docx)")
    parser.add_argument("--pdf", action="store_true", help="Also generate PDF (requires weasyprint)")
    args = parser.parse_args()

    dirs = []
    if args.lang in ("en", "all"):
        dirs.append(DOC / "en")
    if args.lang in ("de", "all"):
        dirs.append(DOC / "de")

    built = []
    for d in dirs:
        for md_path in sorted(d.glob("*.md")):
            if md_path.name == "README.md":
                continue
            html_path = build_html(md_path)
            built.append(html_path)
            print(f"[HTML] {html_path.relative_to(ROOT)}")

            if args.docx:
                try:
                    from docx import Document
                    print(f"  [DOCX] (mammoth/python-docx support: run build_docx.py for full conversion)")
                except ImportError:
                    print("  [DOCX] Skipped: python-docx not installed. Run: pip install python-docx")

            if args.pdf:
                try:
                    import weasyprint
                    pdf_path = html_path.with_suffix(".pdf")
                    weasyprint.HTML(filename=str(html_path)).write_pdf(str(pdf_path))
                    built.append(pdf_path)
                    print(f"  [PDF]  {pdf_path.relative_to(ROOT)}")
                except ImportError:
                    print("  [PDF]  Skipped: weasyprint not installed. Run: pip install weasyprint")

    print(f"\nBuilt {len(built)} file(s).")


if __name__ == "__main__":
    main()
