#!/usr/bin/env python3
"""figure_kit.py: a stdlib-only SVG figure kit for a technical blog series.

WHAT IT IS
    One file that holds the whole visual system for a series' explanatory figures:
    tokens (themable --fig-* CSS custom properties with dark hex fallbacks), a type
    scale, drawing primitives, a series rail, a layout estimator (--check) and a
    preview page whose figCheck() re-checks every figure against real glyph boxes.
    Python 3 standard library only. No dependencies.

    The builders at the bottom (fig_1_0 .. fig_1_6) are a worked example series,
    "From log line to alert", with one figure per reusable figure type:
        series rail, zoom ladder, tree + strip, two-row timeline,
        sampling ticks, row comparison, before/after with a dimension bracket.
    Replace them with your own. Keep the primitives.

HOW TO USE IT IN A SERIES
    1. Copy this file to <series>/figures/build_figures.py.
    2. Edit SERIES_STAGES (the rail config, top of the "Series rail" section).
    3. Replace the example builders and the FIGURES table with your own.
    4. Run it. By default it writes fig-*.svg + preview.html NEXT TO ITSELF.

RUN
    python3 build_figures.py                  # build all figures + preview.html next to the script
    python3 build_figures.py --check          # same, then exit 1 on any layout/assert warning
    python3 build_figures.py --out DIR        # write into DIR instead
    open DIR/preview.html                     # dark + light side by side, live layout check

    Headless figCheck (the banner must read "layout check: 0 issues"):
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new \
        --virtual-time-budget=5000 --dump-dom file://$PWD/preview.html | grep -A3 'id="report"'

EXAMPLE OUTPUT
    Generated from the skill root with
        python3 scripts/figure_kit.py --out examples/figures --check
    into examples/figures/ (SVGs + preview.html). The style guide is
    examples/figure-style.md.

PRIMITIVES
    frame(fig_id, kicker, title, body, height, desc)   -> full <svg> string
    content_top(title)                                 -> first free y under the header
    rail(lit_stages, y=None, ...)                      -> (svg, bottom_y)
    rail_figure(fig_id, fig_no, lit_stages, title, desc, ...) -> full <svg> string
    time_axis(x0, x1, y, t0, t1, ticks, ...)           -> (svg, Scale)
    ticks(xs, y, h, ...)                               -> svg
    bracket(x1, x2, y, label=None, ...)                -> svg
    box(x, y, w, h, label=None, sub=None, state=...)   -> svg
    arrow(x1, y1, x2, y2, ...)                         -> svg
    text(...), wrap(...), rect(...), line(...), polygon(...), circle(...),
    hatch(...), rrect_path(...), Scale(d0, d1, x0, x1)
"""

from __future__ import annotations

import argparse
import math
import re
import sys
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent

# ---------------------------------------------------------------------------
# Tokens
# ---------------------------------------------------------------------------

W = 720                 # viewBox width, every figure
MX = 32                 # side margin
X0, X1 = MX, W - MX     # content column 32..688 (656 px)

# token -> (dark, light). Dark is the fallback baked into every SVG.
# --fig-hazard is reserved for the one critical instant or window a figure is
# about (an incident window, a deadline). Never for "bad", errors or emphasis.
TOKENS = {
    "bg":      ("#181a1c", "#eef9f8"),
    "ink":     ("#dde1e4", "#131519"),
    "muted":   ("#a4a9ac", "#4a5560"),
    "hair":    ("#2e3438", "#b7cac9"),
    "accent":  ("#8eaab6", "#2b6c8f"),
    "hazard":  ("#ff6450", "#d9432f"),
}

SANS = "Hanken Grotesk, Inter, system-ui, sans-serif"
MONO = "Martian Mono, DM Mono, ui-monospace, monospace"

# type scale (px)
KICKER_SIZE = 12
TITLE_SIZE = 17
LABEL_SIZE = 13
SMALL_SIZE = 12         # floor: nothing smaller, ever
MONO_SIZE = 12

# stroke weights
HAIR_W = 1
LINE_W = 1
STRONG_W = 1.5

LIT_FILL_OPACITY = 0.12   # accent fill behind a lit element
HAZARD_FILL_OPACITY = 0.18  # hazard fill for a window (band, cells)
ZOOM_FILL_OPACITY = 0.35  # hair fill of zoom / fan wedges

# ---------------------------------------------------------------------------
# Low-level helpers
# ---------------------------------------------------------------------------


def var(tok: str) -> str:
    """CSS custom property reference with the dark fallback."""
    return f"var(--fig-{tok}, {TOKENS[tok][0]})"


def _n(v: float) -> str:
    """Compact number formatting for coordinates."""
    s = f"{v:.2f}".rstrip("0").rstrip(".")
    return "0" if s == "-0" else s


def paint(fill: str | None = None, stroke: str | None = None, sw: float | None = None,
          fo: float | None = None, so: float | None = None, dash: str | None = None,
          cap: str | None = None) -> str:
    """Paint attributes. Each colour is written twice: a plain presentation
    attribute (dark hex, survives sanitisers that drop `style`) and a `style`
    declaration with var(--fig-*, dark) that the host page can theme."""
    attrs, style = [], []
    if fill is None:
        attrs.append('fill="none"')
    else:
        attrs.append(f'fill="{TOKENS[fill][0]}"')
        style.append(f"fill:{var(fill)}")
    if stroke is not None:
        attrs.append(f'stroke="{TOKENS[stroke][0]}"')
        style.append(f"stroke:{var(stroke)}")
        attrs.append(f'stroke-width="{_n(sw if sw is not None else LINE_W)}"')
    if fo is not None:
        attrs.append(f'fill-opacity="{_n(fo)}"')
    if so is not None:
        attrs.append(f'stroke-opacity="{_n(so)}"')
    if dash:
        attrs.append(f'stroke-dasharray="{dash}"')
    if cap:
        attrs.append(f'stroke-linecap="{cap}"')
    out = " ".join(attrs)
    if style:
        out += f' style="{";".join(style)}"'
    return out


# ---------------------------------------------------------------------------
# Text measurement (estimates; preview.html re-checks with real glyph boxes)
# ---------------------------------------------------------------------------

_NARROW = set("iljtfr.,:;'|!()[]-/ ")


def est_w(s: str, size: float = LABEL_SIZE, mono: bool = False, weight: int = 400,
          ls_em: float = 0.0) -> float:
    """Rough advance width. Mono ~0.65 em (7.8 px at 12 px); sans per-class."""
    if mono:
        w = len(s) * 0.65 * size
    else:
        w = 0.0
        for ch in s:
            if ch == " ":
                k = 0.26
            elif ch in _NARROW:
                k = 0.31
            elif ch in "MW":
                k = 0.86
            elif ch in "mw":
                k = 0.80
            elif ch.isupper():
                k = 0.66
            elif ch.isdigit():
                k = 0.56
            elif ch in "→–·":   # arrow, en dash, middle dot
                k = 0.62
            else:
                k = 0.53
            w += k * size
        if weight >= 600:
            w *= 1.05
    return w + ls_em * size * len(s)


# Every text() call registers an estimated box here; frame() checks overlaps.
_TEXTS: list[tuple[float, float, float, float, str]] = []
WARNINGS: list[str] = []


def text(x: float, y: float, s: str, size: float = LABEL_SIZE, font: str = "sans",
         weight: int = 400, color: str = "ink", anchor: str = "start",
         ls_em: float = 0.0) -> str:
    """One line of text. `y` is the baseline. font = 'sans' | 'mono'."""
    if size < SMALL_SIZE:
        raise ValueError(f"text below the {SMALL_SIZE}px floor: {s!r} at {size}px")
    mono = font == "mono"
    w = est_w(s, size, mono, weight, ls_em)
    left = {"start": x, "middle": x - w / 2, "end": x - w}[anchor]
    _TEXTS.append((left, y - 0.74 * size, left + w, y + 0.22 * size, s))
    ls = f' letter-spacing="{_n(ls_em)}em"' if ls_em else ""
    return (f'<text x="{_n(x)}" y="{_n(y)}" font-family="{MONO if mono else SANS}" '
            f'font-size="{_n(size)}" font-weight="{weight}" text-anchor="{anchor}"{ls} '
            f'{paint(fill=color)}>{escape(s)}</text>')


def wrap(s: str, max_w: float, size: float, weight: int = 400, mono: bool = False) -> list[str]:
    """Greedy word wrap against est_w."""
    lines, cur = [], ""
    for word in s.split():
        trial = f"{cur} {word}".strip()
        if cur and est_w(trial, size, mono, weight) > max_w:
            lines.append(cur)
            cur = word
        else:
            cur = trial
    if cur:
        lines.append(cur)
    return lines


# ---------------------------------------------------------------------------
# Shapes
# ---------------------------------------------------------------------------


def rect(x, y, w, h, fill=None, stroke=None, sw=None, fo=None, rx=4, dash=None) -> str:
    return (f'<rect x="{_n(x)}" y="{_n(y)}" width="{_n(w)}" height="{_n(h)}" rx="{_n(rx)}" '
            f'{paint(fill=fill, stroke=stroke, sw=sw, fo=fo, dash=dash)}/>')


def line(x1, y1, x2, y2, color="hair", sw=HAIR_W, dash=None, so=None, cap=None) -> str:
    return (f'<line x1="{_n(x1)}" y1="{_n(y1)}" x2="{_n(x2)}" y2="{_n(y2)}" '
            f'{paint(stroke=color, sw=sw, dash=dash, so=so, cap=cap)}/>')


def polygon(points, fill=None, stroke=None, sw=None, fo=None) -> str:
    pts = " ".join(f"{_n(px)},{_n(py)}" for px, py in points)
    return f'<polygon points="{pts}" {paint(fill=fill, stroke=stroke, sw=sw, fo=fo)}/>'


def circle(cx, cy, r, fill=None, stroke=None, sw=None, fo=None) -> str:
    return (f'<circle cx="{_n(cx)}" cy="{_n(cy)}" r="{_n(r)}" '
            f'{paint(fill=fill, stroke=stroke, sw=sw, fo=fo)}/>')


def rrect_path(x, y, w, h, r) -> str:
    """Path data for a rounded rectangle (clockwise). Append it to an outer
    rectangle path with fill-rule="evenodd" to cut a rounded window out of a
    dimming layer (see the style guide, "Stylised scenes")."""
    return (f"M{_n(x + r)},{_n(y)}H{_n(x + w - r)}A{_n(r)},{_n(r)} 0 0 1 {_n(x + w)},{_n(y + r)}"
            f"V{_n(y + h - r)}A{_n(r)},{_n(r)} 0 0 1 {_n(x + w - r)},{_n(y + h)}"
            f"H{_n(x + r)}A{_n(r)},{_n(r)} 0 0 1 {_n(x)},{_n(y + h - r)}"
            f"V{_n(y + r)}A{_n(r)},{_n(r)} 0 0 1 {_n(x + r)},{_n(y)}Z")


def arrow(x1, y1, x2, y2, color="muted", sw=LINE_W, head=6.0, half=3.4, dash=None) -> str:
    """Line ending in a small solid triangle at (x2, y2). No <marker> ids, so a
    figure can be inlined many times on one page without id clashes."""
    ang = math.atan2(y2 - y1, x2 - x1)
    ca, sa = math.cos(ang), math.sin(ang)
    bx, by = x2 - head * ca, y2 - head * sa
    tri = [(x2, y2), (bx - half * sa, by + half * ca), (bx + half * sa, by - half * ca)]
    return line(x1, y1, bx, by, color=color, sw=sw, dash=dash) + polygon(tri, fill=color)


def hatch(x, y, w, h, spacing=6.0, color="muted", sw=HAIR_W, so=0.7) -> str:
    """45-degree hatch lines clipped analytically to a rectangle (no <pattern> ids)."""
    out = []
    k = x + y + spacing / 2
    while k < x + w + y + h:
        xa, xb = max(x, k - (y + h)), min(x + w, k - y)
        if xa < xb:
            out.append(line(xa, k - xa, xb, k - xb, color=color, sw=sw, so=so))
        k += spacing
    return "".join(out)


BOX_STATES = {
    # state: (stroke, stroke width, fill, fill opacity, label colour, label weight)
    "lit":    ("accent", STRONG_W, "accent", LIT_FILL_OPACITY, "ink", 700),
    "plain":  ("muted", LINE_W, None, None, "ink", 600),
    "dim":    ("hair", HAIR_W, None, None, "muted", 500),
    "dashed": ("hair", HAIR_W, None, None, "muted", 500),
}


def box(x, y, w, h, label=None, sub=None, state="plain", label_size=LABEL_SIZE,
        sub_font="mono", lines: list[str] | None = None, ls_em=0.0, label_color=None) -> str:
    """Rounded box (rx 4) with a centred label (one or more lines) and optional
    mono sub-label. state: lit | plain | dim | dashed. Warns if text overflows."""
    stroke, sw, fill, fo, lcol, lweight = BOX_STATES[state]
    lcol = label_color or lcol
    dash = "4 3" if state == "dashed" else None
    out = [rect(x, y, w, h, fill=fill, stroke=stroke, sw=sw, fo=fo, dash=dash)]
    rows: list[tuple[str, str]] = [("label", s) for s in (lines or ([label] if label else []))]
    if sub:
        rows.append(("sub", sub))
    if rows:
        lh = label_size + 4
        block = lh * len(rows)
        base = y + (h - block) / 2 + label_size * 0.78 + 1
        for i, (kind, s) in enumerate(rows):
            cy = base + i * lh
            if kind == "label":
                piece = text(x + w / 2, cy, s, size=label_size, weight=lweight, color=lcol,
                             anchor="middle", ls_em=ls_em)
                tw = est_w(s, label_size, False, lweight, ls_em)
            else:
                piece = text(x + w / 2, cy, s, size=SMALL_SIZE, font=sub_font, color="muted",
                             anchor="middle")
                tw = est_w(s, SMALL_SIZE, sub_font == "mono")
            if tw > w - 12:
                WARNINGS.append(f"box text overflows ({tw:.0f} > {w - 12:.0f}): {s!r}")
            out.append(piece)
    return "".join(out)


def bracket(x1, x2, y, label=None, direction="down", color="ink", tick=6.0,
            label_color=None, size=LABEL_SIZE, weight=600, font="sans", sw=LINE_W) -> str:
    """Horizontal bracket from x1 to x2 at y. direction='down': end ticks point
    down at the thing below and the label sits above; 'up' is the mirror."""
    d = tick if direction == "down" else -tick
    out = [line(x1, y, x2, y, color=color, sw=sw), line(x1, y, x1, y + d, color=color, sw=sw),
           line(x2, y, x2, y + d, color=color, sw=sw)]
    if label:
        ly = y - 8 if direction == "down" else y + 8 + size * 0.74
        out.append(text((x1 + x2) / 2, ly, label, size=size, weight=weight, font=font,
                        color=label_color or color, anchor="middle"))
    return "".join(out)


class Scale:
    """Linear map from data (e.g. seconds) to x."""

    def __init__(self, d0, d1, x0, x1):
        self.d0, self.d1, self.x0, self.x1 = d0, d1, x0, x1

    def __call__(self, v):
        return self.x0 + (v - self.d0) * (self.x1 - self.x0) / (self.d1 - self.d0)


def time_axis(x0, x1, y, t0, t1, tick_values, fmt=None, unit="s", color="muted",
              tick_len=4.0) -> tuple[str, Scale]:
    """Hairline axis with mono tick labels below. The unit is appended to the
    last label only. Returns (svg, scale)."""
    sc = Scale(t0, t1, x0, x1)
    fmt = fmt or (lambda v: f"{v:g}")
    out = [line(x0, y, x1, y, color="hair")]
    for i, v in enumerate(tick_values):
        x = sc(v)
        out.append(line(x, y, x, y + tick_len, color=color))
        lab = fmt(v)
        ly = y + tick_len + 14
        out.append(text(x, ly, lab, size=MONO_SIZE, font="mono", color=color, anchor="middle"))
        if unit and i == len(tick_values) - 1:
            # unit after the last label, so the number itself stays centred on its tick
            ux = x + est_w(lab, MONO_SIZE, True) / 2 + 5
            out.append(text(ux, ly, unit, size=MONO_SIZE, font="mono", color=color))
    return "".join(out), sc


def ticks(xs, y, h=10.0, color="muted", sw=LINE_W, up=True) -> str:
    """Vertical tick marks at each x, standing on baseline y (up) or hanging from it."""
    d = -h if up else h
    return "".join(line(x, y, x, y + d, color=color, sw=sw) for x in xs)


def check(cond: bool, msg: str) -> None:
    """Assert a computed figure number. Failures become --check warnings."""
    if not cond:
        WARNINGS.append(msg)


# ---------------------------------------------------------------------------
# Frame (svg root + header)
# ---------------------------------------------------------------------------

KICKER_Y = 36
TITLE_Y = 62
TITLE_LH = 22
HEADER_GAP = 34


def title_lines(title: str) -> list[str]:
    """Wrap the title to the content width. A "\n" in the title forces a break
    (use it to put two short sentences on two lines instead of orphaning a word)."""
    out = []
    for part in title.split("\n"):
        out += wrap(part, X1 - X0, TITLE_SIZE, weight=700)
    return out


def content_top(title: str) -> float:
    """First y available for figure content under the kicker + title."""
    return TITLE_Y + TITLE_LH * (len(title_lines(title)) - 1) + HEADER_GAP


def _check_texts(fig_id: str, height: float) -> None:
    pad = 1.0
    for i, a in enumerate(_TEXTS):
        if a[0] < 8 or a[2] > W - 8 or a[1] < 8 or a[3] > height - 8:
            WARNINGS.append(f"{fig_id}: text near/outside frame edge: {a[4]!r}")
        for b in _TEXTS[i + 1:]:
            if (a[0] < b[2] - pad and b[0] < a[2] - pad and a[1] < b[3] - pad
                    and b[1] < a[3] - pad):
                WARNINGS.append(f"{fig_id}: text overlap {a[4]!r} / {b[4]!r}")


def frame(fig_id: str, kicker: str, title: str, body: str, height: float, desc: str) -> str:
    """Wrap body in the standard figure root: rounded background, mono kicker,
    bold title (wrapped), role=img with <title>/<desc>."""
    height = int(math.ceil(height))
    head = [text(X0, KICKER_Y, kicker, size=KICKER_SIZE, font="mono", color="muted",
                 ls_em=0.12)]
    for i, ln in enumerate(title_lines(title)):
        head.append(text(X0, TITLE_Y + i * TITLE_LH, ln, size=TITLE_SIZE, weight=700))
    _check_texts(fig_id, height)
    _TEXTS.clear()
    if ";" in title + desc + kicker:
        WARNINGS.append(f"{fig_id}: semicolon in title, kicker or desc (use two sentences)")
    tid, did = f"{fig_id}-title", f"{fig_id}-desc"
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {height}" '
        f'width="{W}" height="{height}" role="img" aria-labelledby="{tid} {did}" '
        f'class="sv-fig" data-fig="{fig_id}">\n'
        f'<title id="{tid}">{escape(kicker)} {escape(" ".join(title.split()))}</title>\n'
        f'<desc id="{did}">{escape(desc)}</desc>\n'
        f'{rect(0.5, 0.5, W - 1, height - 1, fill="bg", stroke="hair", sw=1, rx=6)}\n'
        + "\n".join(head) + "\n" + body + "\n</svg>\n"
    )


# ---------------------------------------------------------------------------
# Series rail (shared by every post)
# ---------------------------------------------------------------------------

# ===== SERIES CONFIG: edit these for your series ==========================
# (key, label lines, default coverage tag). Coverage None = not covered by the
# series (drawn dashed, tagged NOT COVERED). Labels: one or two short uppercase
# lines, each must fit the card width minus 12 (the generator warns).
SERIES_STAGES = [
    ("collect-logs",     ("COLLECT LOGS",),          "POST 1"),
    ("parse-enrich",     ("PARSE &", "ENRICH"),      None),
    ("store-index",      ("STORE &", "INDEX"),       "POST 1"),
    ("detect-anomalies", ("DETECT", "ANOMALIES"),    "POST 2"),
    ("alert",            ("ALERT",),                 "POST 2"),
    ("review-tune",      ("REVIEW &", "TUNE"),       "POST 3"),
]
RAIL_PER_ROW = 3        # cards per row; 6 stages -> 3 + 3
NOT_COVERED = "NOT COVERED"
# ==========================================================================


def rail(lit_stages, coverage=None, labels=None, y: float | None = None, x0: float = X0,
         x1: float = X1, stages=None, per_row: int | None = None, box_h: float = 78,
         gap: float = 24, row_gap: float = 44) -> tuple[str, float]:
    """The series chain of jobs as cards, `per_row` per row, wrapping with a
    return connector (down from the last card of a row, back left, down into
    the first card of the next).

    lit_stages: stage indices or keys ('store-index', ...) to light for this post.
    coverage:   optional list (one per stage) or {key: tag} overriding the coverage
                tag printed at the foot of each card; None / "NOT COVERED" draws the
                card dashed + muted.
    labels:     optional {key or index: (line, ...)} replacing a card's label lines
                for this figure only, in the same style as every other card.
    Lit = accent stroke + 12% accent fill + bold ink label; covered elsewhere =
    hairline + muted; not covered = dashed hairline + muted. Returns (svg, bottom_y)."""
    stages = SERIES_STAGES if stages is None else stages
    per_row = RAIL_PER_ROW if per_row is None else per_row
    keys = [s[0] for s in stages]
    idx = lambda s: keys.index(s) if isinstance(s, str) else int(s)  # noqa: E731
    lit = {idx(s) for s in lit_stages}
    tags = [s[2] for s in stages]
    if isinstance(coverage, dict):
        for k, v in coverage.items():
            tags[idx(k)] = v
    elif coverage is not None:
        tags = list(coverage)
    label_of = {idx(k): tuple(v) for k, v in (labels or {}).items()}
    y = 96 if y is None else y
    n = len(stages)
    bw = (x1 - x0 - gap * (per_row - 1)) / per_row
    div_y = 52                       # card divider, relative to card top
    pos = []
    for i in range(n):
        r, c = divmod(i, per_row)
        pos.append((x0 + c * (bw + gap), y + r * (box_h + row_gap)))
    out = []
    for i, ((_key, lines, _t), (bx, by)) in enumerate(zip(stages, pos)):
        on = i in lit
        tag = tags[i]
        covered = tag not in (None, NOT_COVERED)
        state = "lit" if on else ("dim" if covered else "dashed")
        out.append(box(bx, by, bw, box_h, state=state))
        rows = label_of.get(i) or lines
        lh = 16
        base = by + (div_y - lh * len(rows)) / 2 + 12
        lcol, lw = ("ink", 700) if on else ("muted", 500)
        for j, s in enumerate(rows):
            out.append(text(bx + bw / 2, base + j * lh, s, size=LABEL_SIZE, weight=lw,
                            color=lcol, anchor="middle"))
            tw = est_w(s, LABEL_SIZE, False, lw)
            if tw > bw - 12:
                WARNINGS.append(f"rail text overflows ({tw:.0f} > {bw - 12:.0f}): {s!r}")
        out.append(line(bx + 10, by + div_y, bx + bw - 10, by + div_y,
                        color="accent" if on else "hair", so=0.5 if on else None,
                        dash="4 4" if not covered else None))
        out.append(text(bx + bw / 2, by + div_y + 17, tag if covered else NOT_COVERED,
                        size=MONO_SIZE, font="mono", color="ink" if on else "muted",
                        anchor="middle", ls_em=0.08))
        if i < n - 1:
            nx, ny = pos[i + 1]
            if ny == by:             # same row: straight arrow
                out.append(arrow(bx + bw + 5, by + div_y / 2, nx - 5, by + div_y / 2))
            else:                    # wrap: down from this card, back left, down into next
                mid = by + box_h + row_gap / 2
                cx, ncx = bx + bw / 2, nx + bw / 2
                out.append(line(cx, by + box_h + 4, cx, mid, color="muted"))
                out.append(line(cx, mid, ncx, mid, color="muted"))
                out.append(arrow(ncx, mid, ncx, ny - 4))
    bottom = pos[-1][1] + box_h
    return "".join(out), bottom


def rail_figure(fig_id: str, fig_no: str, lit_stages, title: str, desc: str,
                coverage=None, labels=None, kicker: str = "THE JOB") -> str:
    """A whole series-map figure in one call (fig <post>.0 at the top of each post)."""
    top = content_top(title)
    body, bottom = rail(lit_stages, coverage=coverage, labels=labels, y=top + 4)
    return frame(fig_id, f"[ FIG {fig_no} // {kicker} ]", title, body, bottom + 28, desc)


# ===========================================================================
# EXAMPLE SERIES: "From log line to alert". Replace everything from here to
# FIGURES with your own builders.
# ===========================================================================

# Shared facts, so every figure and its desc use the same numbers.
DAY_S = 24 * 60 * 60            # one day of traffic, seconds
MINUTE_S = 60
INCIDENT_S = 4                  # the incident window (a latency spike), seconds
INCIDENT_START_S = 38           # fig 1.6: incident start inside the first 1-minute window
CHECK_S = 5                     # fig 1.6: the detector's check runs this long after a window closes
SCRAPES_S = (1, 5, 15)          # fig 1.4: scrape intervals compared
# fig 1.2 / 1.3: one service's chunks, (start minute after 12:00, size MB). The last
# start is where the chunk still being written begins. Sizes illustrative.
CHUNKS = [(0, 64), (8, 64), (15, 48), (23, 64), (31, 56), (38, 64)]
OPEN_CHUNK_START = 46
QUERY_MIN = (26, 42)            # the query window, minutes after 12:00


def _clock(minute: int) -> str:
    return f"12:{minute:02d}"


def fig_1_0() -> str:
    return rail_figure(
        "fig-1-0", "1.0", ["collect-logs", "store-index"],
        "Getting from a log line to an alert is a chain of six jobs",
        "Six jobs in order, drawn as cards in two rows of three: collect logs (post 1), "
        "parse and enrich (not covered in this series), store and index (post 1), detect "
        "anomalies (post 2), alert (post 2), review and tune (post 3). Collect logs and "
        "store and index are highlighted as this post's subject.",
        kicker="THE PIPELINE")


def fig_1_1() -> str:
    title = "The incident that matters lasts seconds in a day of logs"
    T = content_top(title)
    lx, bx0, bx1 = X0, 264.0, float(X1)
    bw = bx1 - bx0
    out = []
    bar_h = 12
    gap = 92  # row pitch; leaves room for the zoom wedge between rows
    check(DAY_S == 86_400, "fig-1-1: a day is not 86,400 s")

    # One name and one number per row. Anything else goes in the caption.
    def row_labels(top, name, mono):
        return (text(lx, top + 14, name, weight=700)
                + text(lx, top + 34, mono, size=MONO_SIZE, font="mono", color="muted"))

    def zoom(x0, x1, y_from, y_to):
        return (polygon([(x0, y_from), (x1, y_from), (bx1, y_to), (bx0, y_to)], fill="hair",
                        fo=ZOOM_FILL_OPACITY)
                + line(x0, y_from, bx0, y_to) + line(x1, y_from, bx1, y_to))

    # Row 1: one day. 60 s of 86,400 s is ~0.3 px here: drawn at 4 px so it stays visible.
    r1 = T + 2
    out.append(rect(bx0, r1 + 4, bw, bar_h, stroke="muted", sw=LINE_W, rx=3))
    out.append(row_labels(r1, "One day of traffic", f"{DAY_S:,} S"))
    s1x = bx0 + bw * 0.62
    s1w = max(4.0, bw * MINUTE_S / DAY_S)
    out.append(rect(s1x, r1 + 1, s1w, bar_h + 6, fill="accent", rx=1))

    # Row 2: one minute (the zoomed accent span), with the incident in it
    r2 = r1 + gap
    out.append(zoom(s1x, s1x + s1w, r1 + 4 + bar_h + 3, r2 + 4))
    out.append(rect(bx0, r2 + 4, bw, bar_h, fill="accent", fo=LIT_FILL_OPACITY,
                    stroke="accent", sw=STRONG_W, rx=3))
    out.append(row_labels(r2, "One minute", f"{MINUTE_S} S"))
    s2w = bw * INCIDENT_S / MINUTE_S
    s2x = bx0 + bw * 0.56
    out.append(rect(s2x, r2 + 1, s2w, bar_h + 6, fill="hazard", rx=1))

    # Row 3: the incident window, one cell per second
    r3 = r2 + gap
    cell_top = r3 + 4
    out.append(zoom(s2x, s2x + s2w, r2 + 4 + bar_h + 3, cell_top))
    n, g = INCIDENT_S, 6.0
    cw = (bw - g * (n - 1)) / n
    ch = 40
    for i in range(n):
        cx = bx0 + i * (cw + g)
        out.append(rect(cx, cell_top, cw, ch, fill="bg", rx=3))   # hide the zoom fill
        out.append(rect(cx, cell_top, cw, ch, fill="hazard", fo=HAZARD_FILL_OPACITY,
                        stroke="hazard", sw=HAIR_W, rx=3))
    out.append(bracket(bx0, bx0 + cw, cell_top + ch + 10, label="1 s", direction="up",
                       color="muted", size=MONO_SIZE, weight=400, font="mono", tick=5))
    out.append(row_labels(r3, "The incident window", f"{INCIDENT_S} S"))

    share = INCIDENT_S / DAY_S * 100
    check(f"{share:.3f}" == "0.005", f"fig-1-1: incident share {share:.4f}% != 0.005%")
    height = cell_top + ch + 10 + 8 + 9 + 30
    return frame("fig-1-1", "[ FIG 1.1 // SCALE ]", title, "".join(out), height,
                 f"Three zoom levels. One day of traffic is {DAY_S:,} seconds, with a tiny "
                 f"highlighted span. That span expands to one minute, {MINUTE_S} seconds, with a "
                 f"short red span. That span expands to the incident window, {INCIDENT_S} "
                 f"seconds, drawn as {INCIDENT_S} light red one-second cells. The incident is "
                 f"about {share:.3f} percent of the day.")


def _chunk_bounds() -> list[tuple[int, int, int]]:
    """(start_min, end_min, size_mb) for each closed chunk."""
    starts = [s for s, _ in CHUNKS] + [OPEN_CHUNK_START]
    return [(starts[i], starts[i + 1], CHUNKS[i][1]) for i in range(len(CHUNKS))]


def _chunks_for_query() -> list[int]:
    q0, q1 = QUERY_MIN
    return [i for i, (a, b, _) in enumerate(_chunk_bounds()) if a < q1 and q0 < b]


def fig_1_2() -> str:
    title = "A query reads only the few chunks that cover its window"
    T = content_top(title)
    out = []
    bounds = _chunk_bounds()
    lit = set(_chunks_for_query())
    check(lit == {3, 4, 5}, f"fig-1-2: query chunks {sorted(lit)} != [3, 4, 5]")

    # index tree
    mw, mh = 236, 52
    mx = W / 2 - mw / 2
    out.append(box(mx, T, mw, mh, label="LOG INDEX", sub="by service, then time",
                   state="plain", ls_em=0.04))
    cw, chh = 200, 36
    cy = T + mh + 40
    c1x, c2x = 100.0, W - 100.0 - cw
    out.append(box(c1x, cy, cw, chh, label="api service", state="plain"))
    out.append(box(c2x, cy, cw, chh, label="web service", state="dim"))
    fork_y = T + mh + 18
    out.append(line(W / 2, T + mh, W / 2, fork_y, color="muted"))
    out.append(line(c1x + cw / 2, fork_y, c2x + cw / 2, fork_y, color="muted"))
    out.append(arrow(c1x + cw / 2, fork_y, c1x + cw / 2, cy - 1))
    out.append(arrow(c2x + cw / 2, fork_y, c2x + cw / 2, cy - 1))

    # chunk strip, time-ordered, widths proportional to size
    ppm, g = 1.3, 4.0          # px per MB, gap
    S = cy + chh + 78
    sh = 44
    xs = []
    x = float(X0)
    for _a, _b, mb in bounds:
        xs.append((x, x + mb * ppm))
        x += mb * ppm + g
    seg_end = xs[-1][1]
    out.append(polygon([(c1x, cy + chh), (c1x + cw, cy + chh), (seg_end, S - 2), (X0, S - 2)],
                       fill="hair", fo=ZOOM_FILL_OPACITY))
    out.append(line(c1x, cy + chh, X0, S - 2))
    out.append(line(c1x + cw, cy + chh, seg_end, S - 2))
    for i, ((a, b), (t0, _t1, _mb)) in enumerate(zip(xs, bounds)):
        on = i in lit
        if on:
            out.append(rect(a, S, b - a, sh, fill="accent", fo=LIT_FILL_OPACITY, stroke="accent",
                            sw=STRONG_W))
        else:
            out.append(rect(a, S, b - a, sh, fill="bg", stroke="muted", sw=LINE_W))
        out.append(text((a + b) / 2, S + sh / 2 + 4.5, _clock(t0), size=MONO_SIZE, font="mono",
                        weight=600 if on else 400, color="ink" if on else "muted",
                        anchor="middle"))
    # open-ended chunk still being written: dashed top/bottom/left, no right edge
    lx0 = seg_end + g
    out.append(line(lx0, S, X1, S, color="muted", dash="4 4"))
    out.append(line(lx0, S + sh, X1, S + sh, color="muted", dash="4 4"))
    out.append(line(lx0, S, lx0, S + sh, color="muted", dash="4 4"))
    mid = (lx0 + X1) / 2 + 2
    out.append(text(mid, S + 19, "still being", size=SMALL_SIZE, color="muted", anchor="middle"))
    out.append(text(mid, S + 35, "written →", size=SMALL_SIZE, color="muted", anchor="middle"))

    # the query window and what to read
    def tx(minute):
        for (a, b), (t0, t1, _mb) in zip(xs, bounds):
            if t0 <= minute <= t1:
                return a + (b - a) * (minute - t0) / (t1 - t0)
        raise ValueError(minute)

    q0, q1 = QUERY_MIN
    out.append(bracket(tx(q0), tx(q1), S - 12, label="query window", direction="down"))
    first, last = min(lit), max(lit)
    a_lit, b_lit = xs[first][0], xs[last][1]
    dy = S + sh + 14
    out.append(bracket(X0, xs[0][1], dy, direction="up", color="muted", tick=5,
                       label=f"{bounds[0][2]} MB", size=MONO_SIZE, weight=400, font="mono"))
    out.append(bracket(a_lit, b_lit, dy, direction="up", color="accent", tick=5, sw=STRONG_W))
    out.append(text((a_lit + b_lit) / 2, dy + 20, f"read only these {len(lit)}", size=LABEL_SIZE,
                    weight=600, color="accent", anchor="middle"))
    sizes = ", ".join(f"{mb}" for _a, _b, mb in bounds)
    return frame("fig-1-2", "[ FIG 1.2 // THE INDEX ]", title, "".join(out), dy + 20 + 30,
                 "A log index splits by service, then by time. The api service has six closed "
                 f"chunks in time order, starting at {', '.join(_clock(a) for a, _b, _m in bounds)}, "
                 f"drawn with widths proportional to their sizes ({sizes} MB). A seventh chunk, "
                 f"dashed, is still being written. A query for {_clock(q0)} to {_clock(q1)} "
                 f"overlaps only the chunks starting at "
                 f"{', '.join(_clock(bounds[i][0]) for i in sorted(lit))}, so it reads only those "
                 f"{len(lit)}. Sizes are illustrative.")


def fig_1_3() -> str:
    title = ("Reading from the chunk start returns too much.\n"
             "Seeking to the timestamp returns the window.")
    T = content_top(title)
    out = []
    bounds = _chunk_bounds()
    lit = _chunks_for_query()
    show = [lit[0] - 1] + lit                     # one context chunk, then the query's chunks
    t_lo, t_hi = bounds[show[0]][0], bounds[show[-1]][1]
    q0, q1 = QUERY_MIN
    first = bounds[lit[0]][0]                     # start of the chunk holding the query start
    extra = q0 - first
    check(extra == 3, f"fig-1-3: extra minutes {extra} != 3")
    ax0 = 236.0
    sc = Scale(t_lo, t_hi, ax0, float(X1))
    starts = [bounds[i][0] for i in show] + [t_hi]
    req, req_end = sc(q0), sc(q1)
    key_y = T + 8                           # chunk-start marker row
    seg_y, seg_h = T + 22, 28
    bar_h = 26
    rowA = seg_y + seg_h + 42               # bar tops, both rows on one time scale
    rowB = rowA + bar_h + 44
    bottom = rowB + bar_h + 16

    # chunk starts: one label, a small marker on every boundary, and a hairline down
    # through the rows (the first stops at the strip, it carries no story)
    xs = [sc(t) for t in starts]
    out.append(text(xs[0] - 14, key_y + 4, "chunk starts", size=SMALL_SIZE, color="muted",
                    anchor="end"))
    for i, x in enumerate(xs[:-1]):
        out.append(polygon([(x - 4, key_y - 3), (x + 4, key_y - 3), (x, key_y + 4)],
                           fill="muted"))
        out.append(line(x, key_y + 7, x, seg_y + seg_h if i == 0 else bottom, color="hair"))
    for i in range(len(show)):
        a, b = xs[i], xs[i + 1]
        out.append(rect(a + 2, seg_y, b - a - 4, seg_h, fill="bg", stroke="muted", sw=LINE_W))
        out.append(text((a + b) / 2, seg_y + seg_h / 2 + 4.5, _clock(starts[i]), size=MONO_SIZE,
                        font="mono", color="muted", anchor="middle"))

    def row_label(top, name, story):
        return (text(X0, top + 10, name, size=MONO_SIZE, font="mono", weight=600, ls_em=0.06)
                + text(X0, top + 27, story, size=SMALL_SIZE, color="muted"))

    cs = sc(first)                          # the chunk start the read jumps to
    note_x = cs - 10                        # notes sit in the empty context column
    mid_y = bar_h / 2 + 4.5

    # Row A: read from the chunk start (extra lines before the window)
    out.append(row_label(rowA, "FROM CHUNK START", "jump, then read on"))
    out.append(rect(cs, rowA, req_end - cs, bar_h, fill="muted", fo=0.16, stroke="muted",
                    sw=LINE_W))
    out.append(rect(cs, rowA, req - cs, bar_h, fill="accent", fo=LIT_FILL_OPACITY * 2,
                    stroke="accent", sw=STRONG_W))
    out.append(text(note_x, rowA + mid_y, f"{extra} min too early", size=SMALL_SIZE,
                    weight=600, color="accent", anchor="end"))
    out.append(text(req_end - 10, rowA + mid_y, "result", size=SMALL_SIZE, color="ink",
                    anchor="end"))

    # Row B: seek to the exact timestamp
    out.append(row_label(rowB, "SEEK TO TIMESTAMP", "skip to the exact time"))
    out.append(rect(cs, rowB, req - cs, bar_h, stroke="hair", sw=HAIR_W))
    out.append(hatch(cs + 1, rowB + 1, req - cs - 2, bar_h - 2, color="muted", so=0.55))
    out.append(rect(req, rowB, req_end - req, bar_h, fill="muted", fo=0.16, stroke="muted",
                    sw=LINE_W))
    out.append(text(note_x, rowB + mid_y, "skipped", size=SMALL_SIZE, color="muted",
                    anchor="end"))
    out.append(text(req_end - 10, rowB + mid_y, "result", size=SMALL_SIZE, color="ink",
                    anchor="end"))

    # query start / end
    for x, lab in ((req, "query start"), (req_end, "query end")):
        out.append(line(x, seg_y + seg_h + 6, x, bottom, color="ink", sw=STRONG_W, dash="4 3"))
        out.append(text(x, bottom + 18, lab, size=SMALL_SIZE, weight=600, anchor="middle"))
    return frame("fig-1-3", "[ FIG 1.3 // SEEKING ]", title, "".join(out), bottom + 44,
                 f"Four chunks of the api service on one time axis, starting at "
                 f"{', '.join(_clock(t) for t in starts[:-1])}. The query starts at {_clock(q0)}, "
                 f"inside the chunk that starts at {_clock(first)}, and ends at {_clock(q1)}. "
                 f"Top row, reading from the chunk start: the reader jumps to {_clock(first)} and "
                 f"reads on, so the result starts {extra} minutes too early. Bottom row, seeking "
                 f"to the timestamp: the lines from {_clock(first)} to {_clock(q0)} are skipped, "
                 f"and the result runs exactly from the query start to the query end.")


def _sampling_stats() -> tuple[dict[int, int], dict[int, int], float, float]:
    """In-window counts (worst-case phase shown) and miss chances for SCRAPES_S."""
    b0 = 6.5
    b1 = b0 + INCIDENT_S
    counts, misses = {}, {}
    for g in SCRAPES_S:
        times = [k * g for k in range(int(round(30 / g)))]          # 0 <= t < 30
        counts[g] = sum(1 for t in times if b0 <= t <= b1)
        # chance that a spike of length INCIDENT_S at a uniformly random phase holds no sample
        misses[g] = round(max(0.0, (g - INCIDENT_S) / g) * 100)
    return counts, misses, b0, b1


def fig_1_4() -> str:
    counts, misses, b0, b1 = _sampling_stats()
    slow = max(SCRAPES_S)
    title = (f"A {slow}-second scrape misses a {INCIDENT_S}-second spike "
             f"{misses[slow]}% of the time")
    T = content_top(title)
    out = []
    ax0, ax1 = 188.0, 492.0              # axis starts clear of the widest row label
    sc = Scale(0.0, 30.0, ax0, ax1)
    rows = [(f"EVERY {g} S", g) for g in SCRAPES_S]
    c_count, c_miss = 556.0, float(X1)          # right edges of the two value columns
    base0, pitch = T + 76, 52
    band_top, band_bot = T + 34, base0 + pitch * (len(rows) - 1) + 12
    out.append(rect(sc(b0), band_top, sc(b1) - sc(b0), band_bot - band_top, fill="hazard",
                    fo=HAZARD_FILL_OPACITY - 0.02, rx=2))
    out.append(text((sc(b0) + sc(b1)) / 2, T + 22, f"{INCIDENT_S} s spike", size=SMALL_SIZE,
                    weight=600, color="hazard", anchor="middle"))
    for col, (l1, l2) in ((c_count, ("IN", "WINDOW")),
                          (c_miss, ("MISS CHANCE", f"{INCIDENT_S} S SPIKE"))):
        out.append(text(col, T + 8, l1, size=MONO_SIZE, font="mono", color="muted",
                        anchor="end", ls_em=0.08))
        out.append(text(col, T + 23, l2, size=MONO_SIZE, font="mono", color="muted",
                        anchor="end", ls_em=0.08))
    for r, (name, g) in enumerate(rows):
        base = base0 + r * pitch
        times = [k * g for k in range(int(round(30 / g)))]
        inside = [t for t in times if b0 <= t <= b1]
        outside = [t for t in times if not (b0 <= t <= b1)]
        out.append(line(ax0, base, ax1, base, color="hair"))
        out.append(ticks([sc(t) for t in outside], base, h=10, color="muted"))
        out.append(ticks([sc(t) for t in inside], base, h=20, color="accent", sw=STRONG_W))
        out.append(text(X0, base - 1, name, size=MONO_SIZE, font="mono", weight=600,
                        ls_em=0.06))
        out.append(text(c_count, base - 1, str(counts[g]), size=15, font="mono", weight=600,
                        color="accent" if inside else "ink", anchor="end"))
        out.append(text(c_miss, base - 1, f"{misses[g]}%", size=13, font="mono",
                        weight=600 if misses[g] else 400,
                        color="ink" if misses[g] else "muted", anchor="end"))
        if g == slow:
            out.append(text(X0, base + 17, "worst-case", size=SMALL_SIZE, color="muted"))
            out.append(text(X0, base + 32, "phase shown", size=SMALL_SIZE, color="muted"))
    check(counts == {1: 4, 5: 1, 15: 0}, f"fig-1-4: in-window counts {counts} != 4/1/0")
    check(misses == {1: 0, 5: 20, 15: 73}, f"fig-1-4: miss chances {misses} != 0/20/73")
    check(misses[slow] > 50, "fig-1-4: the slow scrape no longer misses most spikes")
    axis, _ = time_axis(ax0, ax1, band_bot + 14, 0.0, 30.0, [0, 10, 20, 30])
    out.append(axis)
    return frame("fig-1-4", "[ FIG 1.4 // SAMPLING ]", title, "".join(out), band_bot + 14 + 46,
                 f"Time axis from 0 to 30 seconds with a red band from {b0:g} to {b1:g} s marking "
                 f"a {INCIDENT_S}-second latency spike. Three rows of scrape ticks. Every 1 s puts "
                 f"{counts[1]} samples inside the spike, every 5 s puts {counts[5]}, and every 15 s "
                 f"(samples at 0, 15 s) puts none in this worst-case phase. Over a random phase the "
                 f"chance that a {INCIDENT_S}-second spike holds no sample is {misses[1]} percent at "
                 f"1 s, {misses[5]} percent at 5 s and {misses[15]} percent at 15 s, computed as "
                 f"the interval minus the spike length, over the interval.")


def fig_1_5() -> str:
    title = "Fixed windows, sliding windows and whole incidents feed a detector differently"
    T = content_top(title)
    out = []
    # Three rows, one rhythm: mono header, a 32-high strip, annotation, hairline divider.
    # Accent marks one detector input per row: the window holding the spike, one sliding
    # window, the whole incident. The spike itself is a neutral ink dot.
    strip_h = 32
    head_to_strip = 14
    row_gap = 22                  # last element of a row -> divider -> next header

    def header(y, s):
        return text(X0, y, s, size=MONO_SIZE, font="mono", color="muted", ls_em=0.12)

    def divider(y_bottom):
        dy = y_bottom + row_gap
        out.append(line(X0, dy, X1, dy, color="hair"))
        return dy + row_gap + 9          # next header baseline

    def lit_or_plain(x, y, w, h, lit, dash=None):
        if lit:
            return rect(x, y, w, h, fill="accent", fo=LIT_FILL_OPACITY, stroke="accent",
                        sw=STRONG_W, rx=3)
        return rect(x, y, w, h, fill="hair" if not dash else "bg",
                    fo=ZOOM_FILL_OPACITY if not dash else None,
                    stroke="muted", sw=LINE_W, rx=3, dash=dash)

    # Row 1: fixed 1-minute windows. The detector sees a window when it closes.
    h1 = T + 8
    out.append(header(h1, "FIXED WINDOWS"))
    ly, n_ch, lg = h1 + head_to_strip, 6, 6.0
    lcw = (X1 - X0 - lg * (n_ch - 1)) / n_ch
    ev_chunk, ev_frac = 2, 0.28
    for i in range(n_ch):
        x = X0 + i * (lcw + lg)
        if i == n_ch - 1:
            out.append(lit_or_plain(x, ly, lcw, strip_h, False, dash="4 3"))
            out.append(text(x + lcw / 2, ly + strip_h / 2 + 4.5, "open", size=SMALL_SIZE,
                            color="muted", anchor="middle"))
        else:
            out.append(lit_or_plain(x, ly, lcw, strip_h, i == ev_chunk))
    dim_y = ly + strip_h + 10
    out.append(bracket(X0, X0 + lcw, dim_y, label="1 min", direction="up", color="muted",
                       size=MONO_SIZE, weight=400, font="mono", tick=5))
    cx = X0 + ev_chunk * (lcw + lg)
    ex, ce = cx + ev_frac * lcw, cx + lcw
    out.append(circle(ex, ly + strip_h / 2, 3.6, fill="ink"))
    out.append(line(ex, dim_y - 5, ex, dim_y, color="muted"))
    out.append(arrow(ex, dim_y, ce - 1, dim_y, head=5, half=3))
    out.append(text((ex + ce) / 2, dim_y + 17, "waits for the window to close",
                    size=SMALL_SIZE, weight=600, anchor="middle"))
    h2 = divider(dim_y + 21)

    # Row 2: sliding windows. A stretch of the day zooms out to overlapping windows.
    out.append(header(h2, "SLIDING WINDOWS"))
    by = h2 + head_to_strip
    out.append(rect(X0, by, X1 - X0, strip_h, fill="hair", fo=ZOOM_FILL_OPACITY, stroke="muted",
                    sw=LINE_W, rx=3))
    out.append(text(X0 + 14, by + strip_h / 2 + 4.5, "the whole day", weight=600))
    ww, stride, wx0 = 112.0, 28.0, 196.0
    last_x = wx0 + 4 * stride + ww
    sw_, sx = 12.0, (wx0 + last_x) / 2 - 6
    zy = by + strip_h + 30                 # zoomed stretch: hairline the windows sit on
    out.append(polygon([(sx, by + strip_h + 3), (sx + sw_, by + strip_h + 3), (last_x, zy),
                        (wx0, zy)], fill="hair", fo=ZOOM_FILL_OPACITY))
    out.append(line(sx, by + strip_h + 3, wx0, zy))
    out.append(line(sx + sw_, by + strip_h + 3, last_x, zy))
    out.append(line(wx0, zy, last_x, zy, color="muted"))
    out.append(rect(sx, by - 3, sw_, strip_h + 6, fill="accent", fo=LIT_FILL_OPACITY,
                    stroke="accent", sw=STRONG_W, rx=2))
    wy0, wh, wp = zy + 8, 12, 16
    for i in range(5):
        x, y = wx0 + i * stride, wy0 + i * wp
        if i == 2:
            out.append(rect(x, y, ww, wh, fill="accent", fo=LIT_FILL_OPACITY * 2,
                            stroke="accent", sw=STRONG_W, rx=3))
        else:
            out.append(rect(x, y, ww, wh, fill="bg", stroke="muted", sw=LINE_W, rx=3))
    ay = wy0 + 4 * wp + wh / 2
    out.append(arrow(last_x + 6, ay, last_x + 40, ay))
    nx = last_x + 52
    out.append(text(nx, ay - 3, "a 5-minute window slides", size=SMALL_SIZE, weight=600))
    out.append(text(nx, ay + 13, "one step per minute", size=SMALL_SIZE, color="muted"))
    h3 = divider(wy0 + 4 * wp + wh)

    # Row 3: the whole incident as one input. It is read once the incident has ended.
    out.append(header(h3, "WHOLE INCIDENT"))
    cy, cw = h3 + head_to_strip, 320.0
    out.append(lit_or_plain(X0, cy, cw, strip_h, True))
    n, pad = 23, 10.0
    tx0 = X0 + pad + 14                     # ticks start clear of the start dot
    xs = [tx0 + i * (X0 + cw - pad - tx0) / (n - 1) for i in range(n)]
    out.append(ticks(xs, cy + strip_h - 8, h=strip_h - 16, color="accent", sw=LINE_W))
    out.append(text(X0 + cw + 16, cy + strip_h / 2 + 4.5, "start to end, one input",
                    size=SMALL_SIZE, weight=600))
    dy3 = cy + strip_h + 10
    sx3 = X0 + pad
    out.append(circle(sx3, cy + strip_h / 2, 3.6, fill="ink"))
    out.append(line(sx3, dy3 - 5, sx3, dy3, color="muted"))
    out.append(arrow(sx3, dy3, X0 + cw - 1, dy3, head=5, half=3))
    out.append(text(X0 + cw / 2, dy3 + 17, "waits for the incident to end", size=SMALL_SIZE,
                    weight=600, anchor="middle"))
    bottom = dy3 + 17
    return frame("fig-1-5", "[ FIG 1.5 // FEEDING A DETECTOR ]", title, "".join(out),
                 bottom + 28,
                 "Three rows. Fixed windows: traffic cut into 1-minute windows, five closed and "
                 "a sixth, dashed, still open. A spike, drawn as a dot early in the third window, "
                 "waits for the window to close before that window goes to the detector. Sliding "
                 "windows: a short stretch of the whole day zooms out to five overlapping "
                 "windows. A 5-minute window slides one step per minute. Whole incident: one "
                 "incident goes in whole, start to end, as one input, and it waits for the "
                 "incident to end. In each row the one detector input is highlighted.")


def _detection() -> tuple[int, int]:
    """Alert time and detection delay for the fixed-window detector of fig 1.5."""
    window_close = (INCIDENT_START_S // MINUTE_S + 1) * MINUTE_S
    alert = window_close + CHECK_S
    return alert, alert - INCIDENT_START_S


def fig_1_6() -> str:
    alert, delay = _detection()
    check((alert, delay) == (65, 27), f"fig-1-6: alert/delay {alert}/{delay} != 65/27")
    title = f"The alert fires {delay} seconds after the incident starts"
    T = content_top(title)
    out = []
    ax0, ax1 = 188.0, X1 - 24.0          # room for the axis unit after the last tick
    sc = Scale(0.0, 120.0, ax0, ax1)
    bar_h = 24
    pitch = 46
    rows_y = [T + 6 + i * pitch for i in range(3)]       # bar tops

    def row_label(top, name):
        return text(X0, top + bar_h / 2 + 4.5, name, size=MONO_SIZE, font="mono", weight=600,
                    ls_em=0.06)

    # Row 1: the detector's 1-minute windows
    y1 = rows_y[0]
    out.append(row_label(y1, "WINDOWS"))
    for k in range(2):
        a, b = sc(k * MINUTE_S), sc((k + 1) * MINUTE_S)
        out.append(rect(a + 2, y1, b - a - 4, bar_h, fill="bg", stroke="muted", sw=LINE_W, rx=3))
    out.append(text((sc(0) + sc(MINUTE_S)) / 2, y1 + bar_h / 2 + 4.5, "1 min",
                    size=MONO_SIZE, font="mono", color="muted", anchor="middle"))

    # Row 2: the true incident (hazard)
    y2 = rows_y[1]
    out.append(row_label(y2, "INCIDENT"))
    out.append(line(ax0, y2 + bar_h / 2, ax1, y2 + bar_h / 2, color="hair"))
    i0, i1 = sc(INCIDENT_START_S), sc(INCIDENT_START_S + INCIDENT_S)
    out.append(rect(i0, y2, i1 - i0, bar_h, fill="hazard", rx=2))

    # Row 3: the alert, as a marker
    y3 = rows_y[2]
    out.append(row_label(y3, "ALERT"))
    out.append(line(ax0, y3 + bar_h / 2, ax1, y3 + bar_h / 2, color="hair"))
    xa = sc(alert)
    out.append(polygon([(xa, y3 + 3), (xa + 8, y3 + bar_h / 2), (xa, y3 + bar_h - 3),
                        (xa - 8, y3 + bar_h / 2)], fill="ink"))

    # where the first window closes, carried down to the alert row
    xc = sc(MINUTE_S)
    out.append(line(xc, y1 + bar_h + 1, xc, y3 + bar_h, color="hair"))

    # projections + the dimension bracket (the subject)
    br_y = y3 + bar_h + 22
    out.append(line(i0, y2 + bar_h + 2, i0, br_y - 1, color="muted", dash="2 3"))
    out.append(line(xa, y3 + bar_h - 1, xa, br_y - 1, color="muted", dash="2 3"))
    out.append(bracket(i0, xa, br_y, direction="up", color="accent", tick=6, sw=STRONG_W))
    out.append(text((i0 + xa) / 2, br_y + 20, f"detection delay, {delay} s", size=LABEL_SIZE,
                    weight=600, color="accent", anchor="middle"))

    axis, _ = time_axis(ax0, ax1, br_y + 46, 0.0, 120.0, [0, 30, 60, 90, 120])
    out.append(axis)
    return frame("fig-1-6", "[ FIG 1.6 // DETECTION DELAY ]", title, "".join(out),
                 br_y + 46 + 18 + 28,
                 f"Time axis from 0 to 120 seconds. Top row, the detector's two 1-minute windows. "
                 f"Middle row, the true incident: a {INCIDENT_S}-second red band starting at "
                 f"{INCIDENT_START_S} s. Bottom row, the alert, a marker at {alert} s, after the "
                 f"first window closes at {MINUTE_S} s and the check runs for {CHECK_S} s. A "
                 f"bracket from the incident start to the alert is labelled detection delay, "
                 f"{delay} s.")


FIGURES = {
    "fig-1-0-series-rail.svg": fig_1_0,
    "fig-1-1-zoom-ladder.svg": fig_1_1,
    "fig-1-2-index-chunks.svg": fig_1_2,
    "fig-1-3-seek.svg": fig_1_3,
    "fig-1-4-sampling.svg": fig_1_4,
    "fig-1-5-windows-vs-whole.svg": fig_1_5,
    "fig-1-6-detection-delay.svg": fig_1_6,
}

# ---------------------------------------------------------------------------
# Preview page
# ---------------------------------------------------------------------------


def _token_css(idx: int) -> str:
    return "".join(f"--fig-{k}:{v[idx]};" for k, v in TOKENS.items())


def _suffix_ids(svg: str, suffix: str) -> str:
    """Make ids unique when the same SVG is inlined twice."""
    svg = re.sub(r'id="([^"]+)"', lambda m: f'id="{m.group(1)}{suffix}"', svg)
    return re.sub(r'aria-labelledby="([^"]+)"',
                  lambda m: 'aria-labelledby="' + " ".join(i + suffix for i in m.group(1).split())
                  + '"', svg)


PREVIEW_CHECK_JS = r"""
// Real-glyph layout check: text/text overlaps, text crossing a line or a box edge,
// text outside the frame. Results go to #report and window.__figReport.
function figCheck(){
  const out=[];
  document.querySelectorAll('.col-dark svg.sv-fig').forEach(svg=>{
    const fig=svg.dataset.fig, vb=svg.viewBox.baseVal;
    const T=[...svg.querySelectorAll('text')].map(t=>({b:t.getBBox(),s:t.textContent}));
    const L=[...svg.querySelectorAll('line')].map(l=>({x1:+l.getAttribute('x1'),y1:+l.getAttribute('y1'),x2:+l.getAttribute('x2'),y2:+l.getAttribute('y2')}));
    const R=[...svg.querySelectorAll('rect')].slice(1).map(r=>({x:+r.getAttribute('x'),y:+r.getAttribute('y'),w:+r.getAttribute('width'),h:+r.getAttribute('height')}));
    const hit=(b,x1,y1,x2,y2)=>{ // segment vs box (axis-aligned segments only, others sampled)
      for(let k=0;k<=40;k++){const x=x1+(x2-x1)*k/40,y=y1+(y2-y1)*k/40;
        if(x>b.x+0.5&&x<b.x+b.width-0.5&&y>b.y+1.5&&y<b.y+b.height-1.5)return true;}return false;};
    T.forEach((a,i)=>{
      if(a.b.x<6||a.b.x+a.b.width>vb.width-6)out.push(fig+': text at edge: '+a.s);
      T.slice(i+1).forEach(c=>{const p=a.b,q=c.b;
        if(p.x<q.x+q.width&&q.x<p.x+p.width&&p.y+1<q.y+q.height&&q.y+1<p.y+p.height)out.push(fig+': overlap "'+a.s+'" / "'+c.s+'"');});
      L.forEach(l=>{if(hit(a.b,l.x1,l.y1,l.x2,l.y2))out.push(fig+': line through "'+a.s+'"');});
      R.forEach(r=>{const e=[[r.x,r.y,r.x+r.w,r.y],[r.x,r.y+r.h,r.x+r.w,r.y+r.h],[r.x,r.y,r.x,r.y+r.h],[r.x+r.w,r.y,r.x+r.w,r.y+r.h]];
        if(e.some(s=>hit(a.b,...s)))out.push(fig+': box edge through "'+a.s+'"');});
    });
  });
  window.__figReport=out;
  document.getElementById('report').textContent=out.length?out.join('\n'):'layout check: 0 issues';
  return out;
}
document.fonts.ready.then(figCheck);
"""


def build_preview(svgs: dict[str, str]) -> str:
    rows = []
    for name, svg in svgs.items():
        rows.append(
            f'<section><h2>{escape(name)}</h2><div class="pair">'
            f'<div class="col col-dark">{_suffix_ids(svg, "-d")}</div>'
            f'<div class="col col-light">{_suffix_ids(svg, "-l")}</div></div></section>')
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Series Figures Preview</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;600;700&family=Martian+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
  :root{{color-scheme:light dark}}
  body{{margin:0;background:#0b0c0d;color:#a4a9ac;font:13px/1.5 'Hanken Grotesk',system-ui,sans-serif}}
  header{{padding:24px 32px 8px}}
  header p{{margin:4px 0;max-width:900px}}
  #report{{font:12px/1.5 'Martian Mono',ui-monospace,monospace;white-space:pre-wrap;color:#dde1e4;padding:8px 32px}}
  h2{{font:500 12px 'Martian Mono',ui-monospace,monospace;letter-spacing:.08em;color:#a4a9ac;margin:0 0 8px}}
  section{{padding:16px 32px 24px}}
  .pair{{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,680px));gap:24px}}
  .col{{padding:20px;border-radius:8px}}
  .col-dark{{background:#0f1112;{_token_css(0)}}}
  .col-light{{background:#ffffff;{_token_css(1)}}}
  .col svg{{display:block;width:100%;max-width:680px;height:auto}}
</style></head>
<body>
<header><h2>SERIES FIGURES // PREVIEW</h2>
<p>Generated by the figure kit. Left: dark tokens. Right: light tokens. Each figure is the
same inline SVG themed only through --fig-* custom properties.</p></header>
<div id="report">layout check: running</div>
{"".join(rows)}
<script>{PREVIEW_CHECK_JS}</script>
</body></html>
"""


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Build the series figures + preview.html.")
    ap.add_argument("--out", type=Path, default=HERE,
                    help="output directory (default: next to this script)")
    ap.add_argument("--check", action="store_true",
                    help="exit 1 if the layout estimator or a figure assert warns")
    args = ap.parse_args(argv)
    out_dir = args.out.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    svgs = {}
    for name, fn in FIGURES.items():
        svg = fn()
        (out_dir / name).write_text(svg, encoding="utf-8")
        svgs[name] = svg
    (out_dir / "preview.html").write_text(build_preview(svgs), encoding="utf-8")
    print(f"wrote {len(svgs)} SVGs + preview.html to {out_dir}")
    for w in WARNINGS:
        print("WARN", w)
    if args.check and WARNINGS:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
