# Figure system

Explanatory figures that look drawn by someone who cared: one idea per figure, minimal text,
technically exact, themable, and legible on a phone. The kit is
`scripts/figure_kit.py`, its style guide is `examples/figure-style.md`, and its example
output (a monitoring series, "From log line to alert") is in `examples/figures/`.

## Principles

1. **The figure confirms. It doesn't reveal.** State the claim in the paragraph before
   the figure. The title restates it as a finding ("A 15-second scrape misses a 4-second
   spike most of the time"), not as a topic ("Sampling").
2. **Draw the claim; don't describe it.** In the original run, a sentence under a row
   ("each chunk goes to the model when it closes, so a moment waits up to a minute")
   became a dot inside a chunk, an arrow to the chunk's end, and the label "waits for the
   chunk to close".
3. **Less text, better organised.** Give each row one name and one number. Secondary
   notes (other frame rates, how a value was measured) move to the caption or the prose.
   Feedback on a 3-layer label stack in the original run was "a lot of text which could have
   been communicated better with more organization".
4. **No repeated labels.** Four identical "chunk start" labels became tick
   markers plus one label.
5. **No CLI flags or code in figures.** They belong in the engineers' aside. Row labels
   can tell the story instead ("jump, then copy" vs "decode to the exact start").
6. **One accent per figure, on its subject.** If a figure seems to need two accents, it's
   two figures. When several rows each show "the model's input", the accent can mean that
   one role consistently. Write that down in STYLE.md.
7. **A reserved hazard colour.** One colour (here red) marks only the key instant and its
   window. Never use it for "bad", errors or emphasis. If something is bad, say so in the
   title.
8. **Time goes on a time axis.** Comparisons share a scale (before/after rows use one axis).
9. **Numbers are computed, not hand-placed.** Derive counts, positions and probabilities in
   code and assert them (`--check`). Compute "chance" figures over the real distribution,
   not the mean, or label them "for an average-length window".
10. **Figure numbers match the prose.** If the prose uses one clip length, the figure uses the
    same one. If an API rejects a setting, don't draw it as an
    option. Label the row as what it really is (the source itself, not a choice).
11. **Answer the question the figure raises.** If the figure shows a read starting earlier than
    asked, draw the boundary it snapped to and label why (reads start at a chunk
    boundary).
12. **Stylised, not literal.** Draw scenes to scale with hairlines and symbols, with no
    footage, logos or AI images. Make metaphors visible: a mobile crop drawn as a
    phone, with rounded corners and a home bar, or a queue drawn as stacked cards. Group
    elements by meaning ("the requests that failed", "the healthy ones"), not scattered.
13. **Label every element a reader must interpret.** A reviewer asked whose dashed outline
    a figure showed. Label it ("the reviewer's choice", "what the model picked").

## Visual language

- **Canvas**: viewBox width 720, height fitted. Rounded background rect with a 1 px hairline
  border. Side margins 32.
- **Header**: a mono kicker `[ FIG <post>.<n> // TOPIC ]` (12 px, muted, letter-spaced),
  then a sans title (17 px, bold) on one line if possible.
- **Type**: a sans for labels (13 px; 12 px floor, never smaller) and a mono for tags,
  ticks, numbers and units. Pick fonts from the author's site. The original run used
  Hanken Grotesk + Martian Mono.
- **Colour tokens**: `--fig-bg / --fig-ink / --fig-muted / --fig-hair / --fig-accent /
  --fig-hazard`. Each painted element carries a hex fallback plus a var:
  `fill="#dde1e4" style="fill:var(--fig-ink, #dde1e4)"`. Fallbacks are the dark values, so
  a figure loaded through `<img>` still reads. Tokens only reach SVGs that are **inlined**
  in the page.
- **Strokes**: 1 px for hairlines and outlines, 1.5 px for the accent and the one line the
  figure is about. Boxes rx 4, bars rx 3, frame rx 6.
- **Shapes**: arrows are polygons (no `<marker>`). Hatching is drawn lines (no
  `<pattern>`). Zoom wedges use two hairlines and a 35% hair fill. Dashes: `4 3` for a
  requested or threshold line, `4 4` for open-ended or future things.
- **Whitespace**: 40+ between stacked rows, 8+ between a label and its line. Labels never
  sit on lines.
- **Accessibility**: `role="img"`, a `<title>` (kicker + title) and a `<desc>` that states
  every number shown. Update `desc` whenever the figure changes.
- **No ids** beyond title and desc, so inlined SVGs never clash on one page.

## Reusable figure types

| Type | Use | Example in `examples/figures/` |
|---|---|---|
| Series rail | opens every post: the job chain with this post's jobs lit and "NOT COVERED" dashed | the monitoring pipeline, collect → review |
| Output comparison | what the system outputs, good vs bad (or truth vs detected) on one scale, with a dimension bracket for the error | true incident start vs alert time, "detection delay" |
| Zoom ladder | scale: a long span → one unit → the instant that matters, with wedges between levels | a day of traffic → one minute → a 4-second spike |
| Tree + strip | structure: an index or manifest fanning into parts drawn proportional to size, with the parts you need lit | a log index → time-ordered chunks a query reads |
| Two-row timeline | before/after on one shared time axis | reading from the chunk start vs seeking to the timestamp |
| Sampling ticks | rows of ticks at different rates against a hazard band, with computed count/miss columns | 1 s / 5 s / 15 s scrapes against a 4 s spike |
| Row comparison | 2–3 ways to do one thing, one rhythm per row (header, strip, annotation, divider) | fixed windows / sliding windows / the whole incident |

Other domains map onto the same types. Video pipelines: hour → clip → the frame that
matters. Payments: a day → one checkout → the timeout. ML training: an epoch → a batch →
the step where loss spiked. Networking: a session → a burst → the dropped packet.

## Captions

One sentence under the figure in the page, saying how to read it or what's illustrative
("times in UTC", "chunk sizes illustrative except the one we measured").

## Checks before a figure ships

1. `python3 <generator> --check` passes: the layout estimator finds no overlaps or
   overflow, and the asserted counts match.
2. The generator's own preview page shows `layout check: 0 issues`, measured on real glyphs.
3. `scripts/shoot_figures.py <figdir> <outdir> <tag> dark light`, then **read every
   PNG yourself**. Look for collisions, clipping, cramped labels, and accent or hazard
   misuse.
4. The figure's numbers and words match the prose, FACTS and the glossary's public names.
5. Phone: the page lets figures scroll inside their own container under 600 px
   (`min-width: 560px`), so labels stay ≥ 12 px. Don't shrink the text.
6. Keep-out: grep the SVGs for internal names. `check_post.py --keep-out` does this.

## Working with a figure subagent

Give it: the exact files it may edit (generator + STYLE.md only), the standard above, the
prose each figure supports, a numbered change list per figure, the screenshot command, and
"iterate until nothing overlaps; report the changes, judgement calls, PNG paths and the
--check output". Then look at the PNGs yourself before accepting the work.
