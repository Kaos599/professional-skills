# Preview page design

`scripts/build_preview.py <post-dir>` turns `post.md` into one self-contained HTML page:
a private review copy that reads like the author's real blog. Restyle it to match the
author's site before the first publish (phase 1c gives you the tokens).

## Layout

- One reading column of about 68ch. Figures break out to 760 px on desktop (≥ 900 px).
- Under 600 px, figures sit in `.fig-scroll` (`overflow-x: auto`) with `min-width: 560px`
  on the SVG, so 12 px labels stay legible. Without this, a 720-wide SVG on a 343 px phone
  column renders labels at about 5.7 px. The page body itself must never scroll sideways.
- A sticky top bar (`top: env(safe-area-inset-top, 0px)`) with the series name. The header
  holds a mono kicker (`Writing · Part N`), the H1, a **dek** (one-line summary, muted,
  larger), and a meta row: a red "Draft · not for publication" tag, **words of main prose**
  (not total words), and read time.

## Components

| Element | Treatment |
|---|---|
| First paragraph | lede: larger (≈19.5 px), full ink colour |
| Body text | its own `--text` token between ink and muted, for contrast in both themes |
| H2 | 24 px, a hairline rule above, 48 px top margin |
| One-bold-sentence paragraph | pull line: 22 px, 600 weight, 2 px accent left border |
| `> **For engineers.**` | aside: raised background, hairline border, 2 px accent left border, 15 px, label in mono caps |
| Figure | inlined SVG (so the theme tokens reach it), then a one-sentence caption at 14 px |
| Tables | inside an `overflow-x: auto` container; header cells in mono caps |
| Inline code | the code font, raised background, the hot colour |

## Theme

Every colour is a token. The original run was dark-first (deep-nord: bg `#111213`, raised
`#181a1c`, ink `#dde1e4`, muted `#a4a9ac`, accent `#8eaab6`, hot `#ff6450`), with a light
"blueprint" theme (bg `#e4f7f6`, ink `#131519`, accent `#2b6c8f`, hot `#d9432f`).
Light values go under `@media (prefers-color-scheme: light) :root:not([data-theme="dark"])`
and again under `:root[data-theme="light"]`. Set `color-scheme` in each block. `body`
gets an explicit token background. Figure tokens (`--fig-*`) live in the same blocks.

Fonts come from Google Fonts only (an Artifact CSP rule), each with a real fallback stack.
The original run used Hanken Grotesk (body), Martian Mono (labels) and DM Mono (code).

## Publishing (Claude Code Artifact tool)

- Publish the preview privately and give the user the link. Republish from the same file
  path to keep the URL, with a `label` like "Draft v6".
- `<title>` is a 2–4 word name (front-matter `short`), stable across republishes. Pass
  `icon` only on the first publish.
- Don't hand-run the generic builder over a project that has its own builder. Its title
  fallback will rename the artifact.
- **Testing phone width locally**: the local file has no viewport meta (the publish
  skeleton adds one), so prepend
  `<meta name="viewport" content="width=device-width,initial-scale=1">` to a temporary
  copy. Headless Chrome on macOS has a minimum window width of about 500 px, so a 390 px
  screenshot gets cropped and looks clipped. Measure overflow with `--dump-dom` and a
  script that writes `innerWidth`, `scrollWidth` and any element whose right edge passes
  `innerWidth` (excluding scroll containers) into a `data-` attribute.
