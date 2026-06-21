#!/usr/bin/env python3
"""generate_html.py — Convert GovTech strategy Markdown papers to standalone HTML.

Usage:
    python Scripts/generate_html.py                   # process all papers
    python Scripts/generate_html.py Doc/en/foo.md     # single file

Requires: mistune>=3.0 (pip install mistune)
Outputs:  same directory as input, .html extension.
License:  MIT
"""

import sys
import re
from pathlib import Path

HTML_TEMPLATE = """\
<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="author" content="{author}">
  <meta name="description" content="{description}">
  <meta name="version" content="{version}">
  <meta name="date" content="{date}">
  <style>
    :root {{
      --ink: #1a1a2e;
      --muted: #555;
      --accent: #2c4a7c;
      --bg: #fdfdfd;
      --rule: #dde;
      --code-bg: #f3f4f8;
      --max-w: 780px;
      --font: system-ui, -apple-system, "Segoe UI", Helvetica, Arial, sans-serif;
      --mono: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
    }}
    *, *::before, *::after {{ box-sizing: border-box; }}
    html {{ font-size: 17px; scroll-behavior: smooth; }}
    body {{
      font-family: var(--font);
      color: var(--ink);
      background: var(--bg);
      line-height: 1.7;
      margin: 0;
      padding: 2rem 1rem 4rem;
    }}
    .paper {{
      max-width: var(--max-w);
      margin: 0 auto;
    }}
    /* --- header / meta block --- */
    .paper-header {{
      border-bottom: 3px solid var(--accent);
      margin-bottom: 2.5rem;
      padding-bottom: 1.5rem;
    }}
    .paper-header h1 {{
      font-size: 1.85rem;
      line-height: 1.25;
      color: var(--accent);
      margin: 0 0 0.5rem;
    }}
    .paper-meta {{
      font-size: 0.82rem;
      color: var(--muted);
      display: flex;
      flex-wrap: wrap;
      gap: 0.4rem 1.2rem;
    }}
    .paper-meta span {{ white-space: nowrap; }}
    .badge {{
      display: inline-block;
      padding: 0.1rem 0.55rem;
      border-radius: 3px;
      font-size: 0.75rem;
      font-weight: 600;
      background: var(--accent);
      color: #fff;
      vertical-align: middle;
    }}
    /* --- typography --- */
    h1, h2, h3, h4, h5 {{
      color: var(--accent);
      font-weight: 700;
      margin-top: 2.2rem;
      margin-bottom: 0.6rem;
    }}
    h2 {{ font-size: 1.35rem; border-bottom: 1px solid var(--rule); padding-bottom: 0.3rem; }}
    h3 {{ font-size: 1.1rem; }}
    h4 {{ font-size: 0.98rem; color: var(--ink); }}
    p {{ margin: 0 0 1rem; }}
    a {{ color: var(--accent); }}
    a:hover {{ text-decoration: none; }}
    blockquote {{
      border-left: 4px solid var(--accent);
      margin: 1.2rem 0;
      padding: 0.6rem 1.2rem;
      background: var(--code-bg);
      color: var(--muted);
    }}
    /* --- tables --- */
    table {{
      border-collapse: collapse;
      width: 100%;
      margin: 1.2rem 0 1.5rem;
      font-size: 0.88rem;
    }}
    th {{
      background: var(--accent);
      color: #fff;
      font-weight: 600;
      text-align: left;
      padding: 0.5rem 0.75rem;
    }}
    td {{
      padding: 0.45rem 0.75rem;
      border-bottom: 1px solid var(--rule);
    }}
    tr:nth-child(even) td {{ background: var(--code-bg); }}
    /* --- code --- */
    pre, code {{
      font-family: var(--mono);
      background: var(--code-bg);
      border-radius: 4px;
    }}
    code {{ font-size: 0.85em; padding: 0.1em 0.35em; }}
    pre {{
      padding: 1rem;
      overflow-x: auto;
      margin: 1rem 0;
    }}
    pre code {{ background: none; padding: 0; }}
    /* --- lists --- */
    ul, ol {{ padding-left: 1.6rem; margin: 0 0 1rem; }}
    li {{ margin-bottom: 0.3rem; }}
    /* --- footer --- */
    footer {{
      margin-top: 3rem;
      padding-top: 1rem;
      border-top: 1px solid var(--rule);
      font-size: 0.8rem;
      color: var(--muted);
    }}
    /* --- print --- */
    @media print {{
      body {{ font-size: 11pt; padding: 0; }}
      .paper {{ max-width: 100%; }}
      a[href]::after {{ content: " (" attr(href) ")"; font-size: 0.75em; }}
    }}
    /* --- responsive --- */
    @media (max-width: 600px) {{
      html {{ font-size: 15px; }}
      .paper-header h1 {{ font-size: 1.4rem; }}
    }}
  </style>
</head>
<body>
  <article class="paper">
    <header class="paper-header">
      <h1>{title}</h1>
      <div class="paper-meta">
        <span>✏️ {author}</span>
        <span>📅 {date}</span>
        <span><span class="badge">v{version}</span></span>
        <span>{status}</span>
        <span>📌 {lang_label}</span>
        <span>📄 {license}</span>
      </div>
    </header>
    <main>
{body}
    </main>
    <footer>
      <p>{license_footer}</p>
    </footer>
  </article>
</body>
</html>
"""


def extract_frontmatter(text: str) -> tuple[dict, str]:
    """Parse YAML frontmatter and return (meta, body)."""
    meta: dict = {}
    if not text.startswith("---"):
        return meta, text
    end = text.find("\n---", 3)
    if end == -1:
        return meta, text
    block = text[3:end].strip()
    for line in block.splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            meta[k.strip()] = v.strip().strip('"\'')
    return meta, text[end + 4:].strip()


def md_to_html_body(md: str) -> str:
    """Convert Markdown to HTML body using mistune if available, else regex fallback."""
    try:
        import mistune
        return mistune.html(md)
    except ImportError:
        pass
    # Minimal regex fallback
    html = md
    html = re.sub(r"^#{6}\s+(.+)$", r"<h6>\1</h6>", html, flags=re.M)
    html = re.sub(r"^#{5}\s+(.+)$", r"<h5>\1</h5>", html, flags=re.M)
    html = re.sub(r"^#{4}\s+(.+)$", r"<h4>\1</h4>", html, flags=re.M)
    html = re.sub(r"^#{3}\s+(.+)$", r"<h3>\1</h3>", html, flags=re.M)
    html = re.sub(r"^#{2}\s+(.+)$", r"<h2>\1</h2>", html, flags=re.M)
    html = re.sub(r"^#{1}\s+(.+)$", r"<h1>\1</h1>", html, flags=re.M)
    html = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", html)
    html = re.sub(r"\*(.+?)\*", r"<em>\1</em>", html)
    html = re.sub(r"`(.+?)`", r"<code>\1</code>", html)
    html = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', html)
    lines = html.split("\n")
    out, in_ul, in_ol, in_pre, para = [], False, False, False, []

    def flush_para():
        if para:
            content = " ".join(para).strip()
            if content:
                out.append(f"<p>{content}</p>")
            para.clear()

    for line in lines:
        if line.startswith("```"):
            flush_para()
            if in_pre:
                out.append("</code></pre>")
                in_pre = False
            else:
                out.append("<pre><code>")
                in_pre = True
            continue
        if in_pre:
            out.append(line)
            continue
        if line.startswith("- ") or line.startswith("* "):
            flush_para()
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{line[2:]}</li>")
            continue
        if in_ul and not (line.startswith("- ") or line.startswith("* ")):
            out.append("</ul>")
            in_ul = False
        m = re.match(r"^\d+\.\s+(.+)$", line)
        if m:
            flush_para()
            if not in_ol:
                out.append("<ol>")
                in_ol = True
            out.append(f"<li>{m.group(1)}</li>")
            continue
        if in_ol and not re.match(r"^\d+\.\s+", line):
            out.append("</ol>")
            in_ol = False
        if line.startswith("<h") or line.startswith("<hr"):
            flush_para()
            out.append(line)
        elif line.strip() == "":
            flush_para()
        else:
            para.append(line)
    flush_para()
    return "\n".join(out)


def build_html(md_path: Path) -> Path:
    text = md_path.read_text(encoding="utf-8")
    meta, body_md = extract_frontmatter(text)

    lang = meta.get("language", "en")
    lang_labels = {"en": "English (source of truth)", "de": "German (translation)"}
    lang_label = lang_labels.get(lang, lang)

    title = meta.get("title", md_path.stem)
    author = meta.get("author", "Unknown")
    version = meta.get("version", "0.0.0")
    date = meta.get("date", "")
    status = meta.get("status", "")
    license_ = meta.get("SPDX-License-Identifier", "CC-BY-4.0")
    description = meta.get("description", title)

    license_footer = (
        f'This document is licensed under <a href="https://creativecommons.org/licenses/by/4.0/">'
        f"{license_}</a>. "
        f"Attribution: {author}. "
        f'Published by the <a href="mailto:sebk4c@tuta.com">Autonomous Office of Civil Digital Infrastructure</a>.'
    )

    body_html = md_to_html_body(body_md)
    # Indent body lines for readability
    body_indented = "\n".join("      " + l if l.strip() else l for l in body_html.splitlines())

    html = HTML_TEMPLATE.format(
        lang=lang,
        lang_label=lang_label,
        title=title,
        author=author,
        version=version,
        date=date,
        status=status,
        license=license_,
        description=description,
        body=body_indented,
        license_footer=license_footer,
    )

    out_path = md_path.with_suffix(".html")
    out_path.write_text(html, encoding="utf-8")
    print(f"  Written: {out_path}")
    return out_path


def main(argv: list[str] | None = None) -> None:
    args = argv if argv is not None else sys.argv[1:]
    if args:
        targets = [Path(a) for a in args]
    else:
        root = Path(__file__).parent.parent
        targets = sorted(root.glob("Doc/**/*.md"))

    if not targets:
        print("No Markdown files found.")
        return

    print(f"Processing {len(targets)} file(s)...")
    for p in targets:
        if not p.exists():
            print(f"  SKIP (not found): {p}")
            continue
        try:
            build_html(p)
        except Exception as exc:
            print(f"  ERROR {p}: {exc}")
    print("Done.")


if __name__ == "__main__":
    main()
