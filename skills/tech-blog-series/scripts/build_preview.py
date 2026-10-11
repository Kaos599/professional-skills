#!/usr/bin/env python3
"""Render a series post (post.md) into a single preview HTML page.

Usage: python3 build_preview.py <post-dir>   (run from the series root; writes <post-dir>/preview.html)

Front matter keys: title, short (tab title, 2-4 words), dek, series, part, status.
Restyle the PAGE tokens to match the author's own site before the first publish.

Handles the Markdown subset the series uses: front matter, headings, paragraphs,
**bold**, `code`, [links](url), - and 1. lists, pipe tables, and figures written as
![FIG n.m](../figures/<file>.svg) followed by an *italic caption* line. Figures are
inlined so the page's CSS variables theme them. Standard library only.
"""
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent


def inline(text: str) -> str:
    out = html.escape(text, quote=False)
    out = re.sub(r"`([^`]+)`", r"<code>\1</code>", out)
    out = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"(?<![*\w])\*([^*]+)\*(?![*\w])", r"<em>\1</em>", out)
    out = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', out)
    return out


def render(md: str, post_dir: Path) -> tuple[str, dict]:
    meta = {}
    if md.startswith("---"):
        _, fm, md = md.split("---", 2)
        for line in fm.strip().splitlines():
            k, _, v = line.partition(":")
            meta[k.strip()] = v.strip().strip('"')
    lines = md.strip().splitlines()
    out, i = [], 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.startswith("# "):
            i += 1  # title rendered in the header
            continue
        m = re.match(r"!\[([^\]]*)\]\(([^)]+)\)", line)
        if m:
            svg = (post_dir / m.group(2)).resolve().read_text()
            svg = re.sub(r"<\?xml[^>]*>\s*", "", svg)
            cap = ""
            if i + 1 < len(lines) and lines[i + 1].startswith("*"):
                cap = lines[i + 1].strip().strip("*")
                i += 1
            out.append(f'<figure class="fig"><div class="fig-scroll">{svg}</div><figcaption>{inline(cap)}</figcaption></figure>')
            i += 1
            continue
        if line.startswith("> "):
            block = []
            while i < len(lines) and lines[i].startswith(">"):
                block.append(lines[i][1:].strip())
                i += 1
            paras = " ".join(block).split("  ")
            out.append('<aside class="eng">' + "".join(f"<p>{inline(x)}</p>" for x in paras if x) + "</aside>")
            continue
        if line.startswith("## "):
            out.append(f"<h2>{inline(line[3:])}</h2>")
            i += 1
            continue
        if line.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
                    rows.append(cells)
                i += 1
            head, body = rows[0], rows[1:]
            t = "<div class=\"table\"><table><thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead><tbody>"
            t += "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in body)
            out.append(t + "</tbody></table></div>")
            continue
        if re.match(r"^(- |\d+\. )", line):
            ordered = bool(re.match(r"^\d+\. ", line))
            items = []
            while i < len(lines) and re.match(r"^(- |\d+\. )", lines[i]):
                items.append(re.sub(r"^(- |\d+\. )", "", lines[i]))
                i += 1
            tag = "ol" if ordered else "ul"
            out.append(f"<{tag}>" + "".join(f"<li>{inline(x)}</li>" for x in items) + f"</{tag}>")
            continue
        para = [line]
        i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#|!\[|\||- |\d+\. |> )", lines[i]):
            para.append(lines[i])
            i += 1
        joined = ' '.join(para)
        cls = ' class="pull"' if re.fullmatch(r"\*\*[^*]+\*\*", joined.strip()) else ""
        out.append(f"<p{cls}>{inline(joined)}</p>")
    return "\n".join(out), meta


PAGE = """<title>{short}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;600;700&family=Martian+Mono:wght@400;500&family=DM+Mono&display=swap">
<style>
/* Layout: one 68ch reading column, figures break out to 760px, like the author's own blog.
   Tokens follow the site's deep-nord (dark) and blueprint (light) palettes. Dark-first. */
:root {{
  --bg: #111213; --bg-elev: #181a1c; --fg: #dde1e4; --muted: #a4a9ac; --hair: #262b2e;
  --accent: #8eaab6; --hot: #ff6450; --text: #c3c8cb;
  --fig-bg: #181a1c; --fig-ink: #dde1e4; --fig-muted: #a4a9ac; --fig-hair: #2e3438;
  --fig-accent: #8eaab6; --fig-hazard: #ff6450;
  --body: "Hanken Grotesk", system-ui, -apple-system, "Segoe UI", sans-serif;
  --mono: "Martian Mono", "DM Mono", ui-monospace, Menlo, monospace;
  --code: "DM Mono", ui-monospace, Menlo, monospace;
  color-scheme: dark;
}}
@media (prefers-color-scheme: light) {{ :root:not([data-theme="dark"]) {{
  --bg: #e4f7f6; --bg-elev: #eef9f8; --fg: #131519; --muted: #3d4750; --hair: #b7cac9;
  --accent: #2b6c8f; --hot: #d9432f; --text: #262d33;
  --fig-bg: #eef9f8; --fig-ink: #131519; --fig-muted: #4a5560; --fig-hair: #b7cac9;
  --fig-accent: #2b6c8f; --fig-hazard: #d9432f; color-scheme: light; }} }}
:root[data-theme="light"] {{
  --bg: #e4f7f6; --bg-elev: #eef9f8; --fg: #131519; --muted: #3d4750; --hair: #b7cac9;
  --accent: #2b6c8f; --hot: #d9432f; --text: #262d33;
  --fig-bg: #eef9f8; --fig-ink: #131519; --fig-muted: #4a5560; --fig-hair: #b7cac9;
  --fig-accent: #2b6c8f; --fig-hazard: #d9432f; color-scheme: light; }}
* {{ box-sizing: border-box; }}
body {{ background: var(--bg); color: var(--text); font: 17px/1.75 var(--body); margin: 0;
  padding-inline: 16px; padding-block: 0 96px; -webkit-font-smoothing: antialiased; }}
.bar {{ position: sticky; top: env(safe-area-inset-top, 0px); z-index: 2; background: color-mix(in srgb, var(--bg) 85%, transparent);
  backdrop-filter: blur(8px); border-bottom: 1px solid var(--hair); margin-inline: -16px; padding: 12px 16px; }}
.bar span {{ font: 500 10px/1 var(--mono); letter-spacing: .2em; text-transform: uppercase; color: var(--muted); }}
header, article {{ max-width: 68ch; margin-inline: auto; }}
header {{ padding-block: 56px 24px; }}
.kicker {{ font: 500 10px/1 var(--mono); letter-spacing: .2em; text-transform: uppercase; color: var(--accent); }}
h1 {{ color: var(--fg); font: 600 clamp(2rem, 5vw, 3.1rem)/1.05 var(--body); letter-spacing: -.02em; text-wrap: balance; margin: 16px 0 20px; }}
.meta {{ display: flex; flex-wrap: wrap; gap: 8px 16px; font: 400 10.5px/1.4 var(--mono); letter-spacing: .14em; text-transform: uppercase; }}
.draft {{ color: var(--hot); }}
h2 {{ color: var(--fg); font: 600 24px/1.3 var(--body); letter-spacing: -.01em; text-wrap: balance;
  border-top: 1px solid var(--hair); padding-top: 32px; margin: 48px 0 12px; }}
p, ul, ol {{ margin: 0 0 20px; }}
li {{ margin-bottom: 6px; }} li::marker {{ color: var(--accent); }} ol li::marker {{ font-family: var(--mono); font-size: 13px; }}
strong {{ color: var(--fg); font-weight: 600; }}
a {{ color: var(--accent); text-underline-offset: 3px; }}
code {{ font: 14px var(--code); color: var(--hot); background: var(--bg-elev); padding: 1px 5px; border-radius: 3px; }}
.fig {{ margin: 32px auto; max-width: 760px; width: calc(100% + 0px); }}
.fig svg {{ display: block; width: 100%; height: auto; }}
.fig figcaption {{ font-size: 14px; line-height: 1.55; margin-top: 10px; color: var(--muted); }}
.eng {{ background: var(--bg-elev); border: 1px solid var(--hair); border-radius: 4px; padding: 16px 20px; margin: 0 0 24px; font-size: 15px; line-height: 1.65; }}
.eng p {{ margin: 0 0 10px; }} .eng p:last-child {{ margin: 0; }}
.eng strong:first-child {{ font: 500 10px/1 var(--mono); letter-spacing: .18em; text-transform: uppercase; color: var(--accent); display: block; margin-bottom: 8px; }}
.refs {{ font-size: 14px; }}
.dek {{ color: var(--muted); font: 400 19px/1.55 var(--body); margin: 0 0 22px; max-width: 58ch; text-wrap: pretty; }}
article > p:first-child {{ color: var(--fg); font-size: 19.5px; line-height: 1.7; }}
.pull {{ color: var(--fg); font: 600 22px/1.35 var(--body); letter-spacing: -.01em; border-left: 2px solid var(--accent);
  padding: 2px 0 2px 18px; margin: 28px 0; }}
.pull strong {{ font-weight: 600; }}
.fig-scroll {{ overflow-x: auto; -webkit-overflow-scrolling: touch; border-radius: 8px; }}
@media (max-width: 600px) {{ .fig-scroll svg {{ min-width: 560px; }} }}
h2 + p {{ margin-top: 4px; }}
.eng {{ border-left: 2px solid var(--accent); }}
.table {{ overflow-x: auto; margin: 0 0 24px; border: 1px solid var(--hair); border-radius: 4px; }}
table {{ border-collapse: collapse; width: 100%; font-size: 15px; line-height: 1.5; }}
th {{ font: 500 10px/1.4 var(--mono); letter-spacing: .14em; text-transform: uppercase; text-align: left; color: var(--fg); background: var(--bg-elev); }}
th, td {{ padding: 10px 14px; border-bottom: 1px solid var(--hair); vertical-align: top; }}
tr:last-child td {{ border-bottom: 0; }}
@media (min-width: 900px) {{ .fig {{ margin-inline: calc((68ch - 760px) / 2); width: 760px; max-width: none; }} }}
</style>
<div class="bar"><span>← Blog · Series: {series}</span></div>
<header>
  <div class="kicker">Writing · Part {part}</div>
  <h1>{title}</h1>
  <p class="dek">{dek}</p>
  <div class="meta"><span class="draft">Draft · not for publication</span><span>{words} words of prose</span><span>{mins} min read</span></div>
</header>
<article>
{body}
</article>
"""


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    post_dir = Path.cwd() / sys.argv[1]
    md = (post_dir / "post.md").read_text()
    body, meta = render(md, post_dir)
    prose = md.split("## Words used")[0].split("---", 2)[-1]
    prose = re.sub(r"(?m)^(>|\||!\[|\*[^*]|#).*$", "", prose)
    words = len(prose.split())
    page = PAGE.format(short=meta.get("short", meta.get("title", "Draft")[:40]), series=meta.get("series", ""), part=meta.get("part", ""),
                       title=html.escape(meta.get("title", "")), dek=html.escape(meta.get("dek", "")), words=f"{words:,}", mins=round(words / 230),
                       body=body)
    (post_dir / "preview.html").write_text(page)
    print(post_dir / "preview.html")


if __name__ == "__main__":
    main()
