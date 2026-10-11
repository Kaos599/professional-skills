# Figure style: the figure kit

One visual system for every figure in a series. All figures come from one generator,
`scripts/figure_kit.py` (Python 3 stdlib, no deps), copied into the series as
`<series>/figures/build_figures.py`. Don't hand-edit the SVGs. Change the builder and
re-run it:

```bash
python3 build_figures.py                 # writes fig-*.svg + preview.html next to the script
python3 build_figures.py --out DIR       # writes them into DIR instead
python3 build_figures.py --check         # same, but exits 1 on any layout warning or failed assert
open preview.html                        # every figure on dark and light, plus a live layout check
```

`preview.html` loads the real fonts and runs `figCheck()` against the rendered glyph
boxes. It flags text overlapping text, any `<line>` or box edge passing through a label,
and text at the frame edge. The banner at the top must read `layout check: 0 issues`
before a figure ships. Headless:

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new \
  --virtual-time-budget=8000 --dump-dom "file://$PWD/preview.html" \
  | grep -o '<div id="report">[^<]*</div>'
```

The worked example in `examples/figures/` is an imaginary series, "From log line to
alert", built with `python3 scripts/figure_kit.py --out examples/figures --check`.

## Canvas

| | |
|---|---|
| viewBox | `0 0 720 H` (width is always 720; H fits the content) |
| Display | ~680 px column, so 1 unit is about 0.94 px |
| Background | `rect` at 0.5,0.5, 719 x (H-1), `rx 6`, fill `--fig-bg`, 1 px `--fig-hair` border |
| Side margins | 32 (content column 32..688) |
| Header | kicker baseline y=36, title baseline y=62 (+22 per extra wrapped line), content starts 34 below the last title baseline (`content_top(title)`) |
| Bottom padding | about 26-30 below the last element |

## Colour tokens

Every colour goes through a CSS custom property, so the host page decides light or
dark. Each painted element carries the colour twice:
`fill="#dde1e4" style="fill:var(--fig-ink, #dde1e4)"`. The plain attribute is the
dark fallback, which survives sanitisers that strip `style`. The `style` declaration
is the themable one. The fallbacks are the **dark** values.

| token | dark (fallback) | light | use |
|---|---|---|---|
| `--fig-bg` | `#181a1c` | `#eef9f8` | figure background; also the fill of "solid" cells that must hide lines behind them |
| `--fig-ink` | `#dde1e4` | `#131519` | titles, primary labels, emphasised numbers, neutral markers |
| `--fig-muted` | `#a4a9ac` | `#4a5560` | kicker, secondary labels, object outlines, arrows, axis labels |
| `--fig-hair` | `#2e3438` | `#b7cac9` | hairlines, grid lines, frame border, dim boxes, zoom/fan fills (at 35%) |
| `--fig-accent` | `#8eaab6` | `#2b6c8f` | the figure's subject, and nothing else |
| `--fig-hazard` | `#ff6450` | `#d9432f` | the one critical instant or window the figure is about, and nothing else |

Swap the hex values for the author's site palette in `TOKENS` (one place). The host
page sets the tokens, for example:

```css
:root { --fig-bg:#eef9f8; --fig-ink:#131519; --fig-muted:#4a5560;
        --fig-hair:#b7cac9; --fig-accent:#2b6c8f; --fig-hazard:#d9432f; }
@media (prefers-color-scheme: dark) {
  :root { --fig-bg:#181a1c; --fig-ink:#dde1e4; --fig-muted:#a4a9ac;
          --fig-hair:#2e3438; --fig-accent:#8eaab6; --fig-hazard:#ff6450; } }
svg.sv-fig { width:100%; height:auto; display:block; }
```

Custom properties only reach an SVG that is **inlined** in the page. Loaded through
`<img>` or as a CSS background, the SVG falls back to dark, which still reads fine on
any page because it draws its own background.

## Accent rule

- **One accent per figure, only on the figure's subject.** That is the thing the title
  makes a claim about (the lit stages, the chunks a query reads, the extra lines a read
  returns, the samples that land inside the spike, the detection delay). Everything else
  is neutral ink, muted or hair.
- Accent treatment for an area is a 1.5 px accent stroke plus an accent fill at 12%
  (`LIT_FILL_OPACITY`). A small area that must read at a glance can use 24%. Accent
  text is 600 weight.
- If a figure seems to need two accents, it is two figures, or one of the two is
  context and goes neutral.
- When several rows each show the same role, the accent can mean that role in every
  row. Write it down. In fig 1.5 the accent marks "the detector's input" in each row.

## Hazard rule

`--fig-hazard` marks **the one critical instant or window** a figure is about: an
incident window, a deadline, the instant a threshold is crossed. Use it for the band,
the cells (hazard at 18%, `HAZARD_FILL_OPACITY`, with a hazard hairline), one solid
marker for the instant, and their labels. Never use it for errors, warnings, "bad"
values or emphasis. If something is bad, say so in the title. A figure that is not
about that window has no hazard at all (fig 1.5 draws its spike as a neutral ink dot).

## Type

| role | font | size | weight | colour | notes |
|---|---|---|---|---|---|
| kicker | `MONO` | 12 | 400 | muted | uppercase, `letter-spacing 0.12em`, format `[ FIG <post>.<n> // <TOPIC> ]` |
| title | `SANS` | 17 | 700 | ink | a sentence that states the finding, not a topic; auto-wraps at 656; `\n` forces a break between two sentences |
| label | `SANS` | 13 | 400-700 | ink / muted | box labels 600; lit labels 700 |
| small label / note | `SANS` | 12 | 400-600 | muted | the floor; nothing below 12 px (`text()` raises) |
| mono tags, ticks, numbers, units | `MONO` | 12 | 400-600 | muted / ink | uppercase tags get `letter-spacing 0.06-0.12em` |

**No semicolons** in any visible string or `desc`. Use two sentences instead. `frame()`
warns on a semicolon in the kicker, title or desc. A title may be two short sentences
ending in full stops.

`SANS = "Hanken Grotesk, Inter, system-ui, sans-serif"`,
`MONO = "Martian Mono, DM Mono, ui-monospace, monospace"`. Swap them for the site's fonts
and update the Google Fonts link in `build_preview()`.

Fitting text: `est_w()` estimates about 7 px per character at 13 px sans and 7.8 px at
12 px mono. Martian Mono renders a little narrower (about 7.3 px at 12 px). `box()` and
`rail()` warn when a label would overflow (width minus 12). `frame()` warns on estimated
text overlaps and text near the frame edge. `preview.html` re-checks with real glyphs.

**Minimal text.** One name and one number per row. No repeated labels: one label plus
markers beats four copies of the label. No CLI flags or code: row labels tell the story
in plain words ("jump, then read on" vs "skip to the exact time"). Secondary notes go in
the caption or the prose.

## Strokes and shapes

- Strokes are 1 px (`LINE_W`, `HAIR_W`) or 1.5 px (`STRONG_W`, used for accent outlines
  and the one line a figure is about, such as "query start").
- Hairlines (grids, chunk boundaries, zoom edges, frame border) use `--fig-hair`. Object
  outlines (boxes, bars, cells) use `--fig-muted`.
- Boxes have `rx 4`, bars `rx 3`, and the frame `rx 6`.
- Arrows are a 1 px muted line plus a small solid muted triangle (6 long, 6.8 wide),
  drawn as a polygon rather than a `<marker>`, so the SVGs contain no ids beyond
  title/desc.
- Hatching (`hatch()`) is drawn as 45-degree lines clipped analytically. No `<pattern>`.
  Use it for work done but not returned (fig 1.3, "skipped").
- No gradients, shadows, emoji or icons. Dashes are `4 3` for "requested/threshold"
  lines and `4 4` for open-ended or future things. Projection lines use `2 3`.
- Zoom or fan connectors (a span opening out into the next level): two hairlines plus a
  `--fig-hair` fill at 35% (`ZOOM_FILL_OPACITY`).
- **Draw a delay, don't describe it**: a dot at the moment, an arrow to where it is
  handled, and a short label ("waits for the window to close").
- Leave generous whitespace: 40 or more between stacked rows, 24 between rail boxes,
  and 8 or more between a label and the line it labels. Labels never sit on lines.
  Break the line or move the label.

## Box states (`box(..., state=)`)

| state | stroke | fill | label |
|---|---|---|---|
| `lit` | accent 1.5 | accent 12% | ink 700 |
| `plain` | muted 1 | none | ink 600 |
| `dim` | hair 1 | none | muted 500 |
| `dashed` | hair 1, dashed `4 3` | none | muted 500 |

## Accessibility

Every SVG has `role="img"`, `aria-labelledby` pointing at its `<title>` (kicker +
title) and `<desc>` (a plain-language account of everything the figure shows,
including every number). Write the `desc` so a reader who can't see the figure gets
the same finding. Build the `desc` from the same variables as the drawing, so it can't
drift. No ids beyond title and desc, so inlined SVGs never clash on one page
(`preview.html` suffixes the two ids when it inlines each figure twice).

## Primitives (in `figure_kit.py`)

```python
frame(fig_id, kicker, title, body, height, desc) -> str        # svg root + bg + header
content_top(title) -> float                                     # first free y under the header
rail(lit_stages, coverage=None, labels=None, y=None, x0=32, x1=688,
     stages=SERIES_STAGES, per_row=RAIL_PER_ROW, box_h=78, gap=24, row_gap=44) -> (svg, bottom_y)
rail_figure(fig_id, fig_no, lit_stages, title, desc, coverage=None, labels=None,
            kicker="THE JOB") -> str                            # a whole series-map figure
time_axis(x0, x1, y, t0, t1, tick_values, fmt=None, unit="s") -> (svg, Scale)
ticks(xs, y, h=10, color="muted", sw=1, up=True) -> str
bracket(x1, x2, y, label=None, direction="down", color="ink") -> str
box(x, y, w, h, label=None, sub=None, state="plain", lines=None) -> str
arrow(x1, y1, x2, y2, color="muted") -> str
text(x, y, s, size=13, font="sans"|"mono", weight=400, color="ink", anchor="start", ls_em=0)
wrap(s, max_w, size) -> [str]
rect(...), line(...), polygon(...), circle(...), hatch(...), rrect_path(...), Scale(d0, d1, x0, x1)
check(cond, msg)                                                # assert a computed number (--check)
```

`rrect_path()` returns path data for a rounded rectangle. Append it to an outer
rectangle path with `fill-rule="evenodd"` and fill `--fig-bg` at about 55% to dim
everything outside a rounded window in a stylised scene.

## Adding a figure

1. Write a builder in `build_figures.py`:
   ```python
   def fig_2_3() -> str:
       title = "A sentence that states what the figure shows"
       T = content_top(title)
       out = []
       # ... draw with box/arrow/bracket/time_axis/ticks/text, starting at y = T
       check(count == 3, "fig-2-3: expected 3 chunks")
       return frame("fig-2-3", "[ FIG 2.3 // TOPIC ]", title, "".join(out), height,
                    "Plain-language description including every number shown.")
   ```
2. Register it in `FIGURES` as `"fig-2-3-short-slug.svg": fig_2_3`.
3. Run `python3 build_figures.py --check`, open `preview.html`, confirm
   `layout check: 0 issues`, render PNGs with `scripts/shoot_figures.py`, and look at
   both themes.
4. Numbers in a figure must be verified facts or be marked illustrative in the figure
   itself or in the post's caption (fig 1.2's sizes are illustrative). Keep shared facts
   as module constants (`INCIDENT_S`, `CHUNKS`, `QUERY_MIN` in the example) so every
   figure and `desc` uses the same value. Compute derived positions, counts and
   probabilities in code and assert them with `check()` (see `fig_1_4`, which computes
   the in-window counts and miss chances, and builds its title from them). Don't
   hand-place them. Compute "chance" figures over the real distribution, or label them
   for a stated length ("MISS CHANCE, 4 S SPIKE").

File naming: `fig-<post>-<n>-<slug>.svg`. Fig `<post>.0` is the series map. To insert
a figure mid-sequence, renumber the later builders, kickers, `fig_id`s and `FIGURES`
keys in one pass, then delete the superseded SVG files (the script never deletes).

## Example figures ("From log line to alert", post 1)

| fig | type | file | title | subject (accent) | hazard |
|---|---|---|---|---|---|
| 1.0 | series rail | `fig-1-0-series-rail.svg` | Getting from a log line to an alert is a chain of six jobs | this post's jobs (collect, store) | none |
| 1.1 | zoom ladder | `fig-1-1-zoom-ladder.svg` | The incident that matters lasts seconds in a day of logs | the minute that holds the incident | the 4 s incident window |
| 1.2 | tree + strip | `fig-1-2-index-chunks.svg` | A query reads only the few chunks that cover its window | the 3 chunks the query reads | none |
| 1.3 | two-row timeline | `fig-1-3-seek.svg` | Reading from the chunk start returns too much. Seeking to the timestamp returns the window. | the extra 3 minutes returned | none |
| 1.4 | sampling ticks | `fig-1-4-sampling.svg` | A 15-second scrape misses a 4-second spike 73% of the time | the samples inside the spike | the 4 s spike band |
| 1.5 | row comparison | `fig-1-5-windows-vs-whole.svg` | Fixed windows, sliding windows and whole incidents feed a detector differently | the detector's input in each row | none (the spike is an ink dot) |
| 1.6 | before/after + dimension bracket | `fig-1-6-detection-delay.svg` | The alert fires 27 seconds after the incident starts | the detection-delay bracket | the true incident |

Patterns worth reusing:

- **Zoom ladder** (1.1): rows of bars, a name and a mono number on the left, a
  highlighted span in each bar that opens into the next row through a zoom wedge. A span
  too thin to see is drawn at a 4 px minimum (say so in a code comment).
- **Tree + strip** (1.2): a `box()` tree forking into a strip whose widths are
  proportional to a measured quantity, an open-ended dashed cell for "still being
  written", an ink bracket above for what was asked, an accent bracket below for what is
  read.
- **Two-row timeline** (1.3): both rows on one `Scale`, boundary markers drawn once with
  one label, dashed `4 3` ink lines for the requested start and end, the subject in
  accent, discarded work hatched.
- **Sampling ticks** (1.4): one row per rate, accent ticks inside the hazard band,
  right-aligned computed columns, "worst-case phase shown" under the row that misses.
- **Row comparison** (1.5): one rhythm per row (mono header, 32-high strip, short
  annotation, hairline divider).
- **Before/after + dimension bracket** (1.6): rows on a shared time axis, dashed `2 3`
  projections down to an accent bracket that carries the one number.

## Stylised scenes

When a figure shows what the system outputs (a screen, a crop, a dashboard), draw it to
scale with hairlines and simple symbols. No screenshots, logos or AI images. Make the
metaphor visible (a phone window gets rounded corners and a home bar). Place objects in
intentional groups, not scattered. Dim what is outside the subject with `--fig-bg` at
55% through an even-odd path built from `rrect_path()`. Label every element a reader
must interpret ("expected window", not an unlabelled dashed outline).

## Re-lighting the rail

The rail is the series' chain of jobs (`SERIES_STAGES`, the marked config block in the
"Series rail" section), drawn as cards, `RAIL_PER_ROW` per row, joined by a return
connector (down from the last card of a row, back left, down into the first card of the
next). Each card shows its job (one or two 13 px lines), a divider, and a mono coverage
tag at the foot. The example has six stages, 3 + 3:

| key | label | default tag |
|---|---|---|
| `collect-logs` | COLLECT LOGS | POST 1 |
| `parse-enrich` | PARSE & / ENRICH | NOT COVERED (`None`) |
| `store-index` | STORE & / INDEX | POST 1 |
| `detect-anomalies` | DETECT / ANOMALIES | POST 2 |
| `alert` | ALERT | POST 2 |
| `review-tune` | REVIEW & / TUNE | POST 3 |

Card states: **lit** (this post's jobs) = accent 1.5 stroke, 12% accent fill, bold ink
label, ink tag. **Covered elsewhere** = hairline, muted label and tag. **Not covered**
(tag `None` or `"NOT COVERED"`) = dashed hairline border and divider, muted text.

Re-lighting is one call. `lit_stages` takes indices or keys. `coverage` optionally
overrides tags (a full list, or `{key: tag}`). `labels` replaces a card's label lines
for one figure, in the same style as every other card (no add-on sub-labels in a
different font or colour):

```python
# post 1 (fig 1.0)
rail_figure("fig-1-0", "1.0", ["collect-logs", "store-index"],
            "Getting from a log line to an alert is a chain of six jobs", "<desc>",
            kicker="THE PIPELINE")
# post 2
rail_figure("fig-2-0", "2.0", ["detect-anomalies", "alert"], "<title>", "<desc>",
            kicker="THE PIPELINE")
# post 3, with a card relabelled for this figure only
rail_figure("fig-3-0", "3.0", ["review-tune"], "<title>", "<desc>",
            labels={"review-tune": ("REVIEW &", "RETUNE RULES")}, kicker="THE PIPELINE")
```

Or use `rail(lit, coverage=..., labels=..., y=...)` inside a larger figure. It returns
`(svg, bottom_y)`. To change a job's wording or its default coverage, edit
`SERIES_STAGES` (key, label lines, tag) once. Every post's map picks the change up on
the next run. Labels must fit the card width minus 12 (about 190 px at 3 per row, 134 px
at 4 per row). The generator warns if they don't. Pick `RAIL_PER_ROW` so rows are even
or the last row is short by one (6 stages: 3 + 3; 7: 4 + 3; 8: 4 + 4). More than 4 per
row pushes labels under 12 px.
