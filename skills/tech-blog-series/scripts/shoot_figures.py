#!/usr/bin/env python3
"""Render every fig-*.svg in a folder to PNG, in dark and/or light theme, with headless Chrome.

Usage: python3 shoot_figures.py <figures-dir> <out-dir> <tag> [dark] [light]
Writes <out-dir>/<tag>-<figure-stem>-<mode>.png. Read the PNGs to review figures visually.
Edit THEMES to match the page's figure tokens. macOS Chrome path by default; set CHROME to override.
Note: headless Chrome on macOS has a ~500 px minimum window width, so phone-width screenshots
under that are misleading. Measure layout with --dump-dom and a script instead (see SKILL.md).
"""
import os, re, subprocess, sys, pathlib

CHROME = os.environ.get("CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
THEMES = {
    "dark": ":root{--fig-bg:#181a1c;--fig-ink:#dde1e4;--fig-muted:#a4a9ac;--fig-hair:#2e3438;"
            "--fig-accent:#8eaab6;--fig-hazard:#ff6450;--bg:#111213}",
    "light": ":root{--fig-bg:#eef9f8;--fig-ink:#131519;--fig-muted:#4a5560;--fig-hair:#b7cac9;"
             "--fig-accent:#2b6c8f;--fig-hazard:#d9432f;--bg:#e4f7f6}",
}
FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:'
         'wght@400;600;700&family=Martian+Mono:wght@400;500&display=swap">')

def main():
    figdir, outdir, tag = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), sys.argv[3]
    modes = sys.argv[4:] or ["dark"]
    outdir.mkdir(parents=True, exist_ok=True)
    for f in sorted(figdir.glob("fig-*.svg")):
        svg = re.sub(r"<\?xml[^>]*>", "", f.read_text())
        m = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', svg)
        h = int(float(m.group(2)) * 760 / float(m.group(1))) + 40
        for md in modes:
            html = outdir / f"{tag}-{f.stem}-{md}.html"
            html.write_text(f"{FONTS}<style>{THEMES[md]}body{{margin:0;background:var(--bg);padding:20px}}"
                            f"svg{{width:760px;height:auto;display:block}}</style>{svg}")
            png = outdir / f"{tag}-{f.stem}-{md}.png"
            subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                            f"--window-size=800,{h}", "--virtual-time-budget=3000",
                            f"--screenshot={png.resolve()}", f"file://{html.resolve()}"],
                           capture_output=True)
            print(png)

if __name__ == "__main__":
    main()
