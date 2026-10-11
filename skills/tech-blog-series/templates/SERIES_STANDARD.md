# Series standard: <series name>

The contract every post follows. Post 1 sets it, and posts 2..N follow it. To break a rule,
write the reason in that post's NOTES.md before drafting.
Tracker: <Claude Doc link or TRACKER.md>

## 1. The series
| # | Post | One idea the reader keeps |
|---|---|---|
| 1 | <prerequisite/context post> | <one sentence> |
| 2 | | |

Readers: <engineer…>, <decision-maker…>, <non-engineer…>. Two layers: story in the body,
mechanism in `> **For engineers.**` asides.

## 2. Voice
<paste the VOICE SIGNATURE>. Plus the bans and budgets from
~/.claude/skills/tech-blog-series/references/writing-standard.md §3.

## 3. Storytelling
Cold open: <scene from a domain everyone knows> → the hard fact → a person → scale →
the jobs → "by hand it's impossible". Keep a person in every opening paragraph, a human
beat in each incident, and return to the scene at the end.

## 4. Post anatomy
Dek · cold open · series rail figure · 3–5 thesis H2s · tried → broke → changed → result ·
"What this does not solve" (with a first-person view) · decision rule · next post (one
sentence) · glossary · references. 1,800–2,600 words of main prose, 4–7 figures.

## 5. Numbers and claims
Every number: unit, scale, comparison, a FACTS row. n in the sentence when n < 30. CIs
that include zero said aloud. Selection, rerun drift, confounds, single labeller. Thresholds
from distributions. `[CLEAR?]` on anything company-sensitive.

## 6. Public names
| Public name | Internal name | Definition |
|---|---|---|
| | | |
Keep out of prose and figures: <internal names>.

## 7. Figures
See figures/STYLE.md (from ~/.claude/skills/tech-blog-series/references/figure-system.md).
Accent = <colour>, reserved hazard colour = <colour, and what it marks>.

## 8. Gates
0 review panel (nemesis + grader + 3 readers), blockers fixed · 1 FACTS complete ·
2 keep-out clean (`check_post.py --keep-out keep-out.txt`) · 3 anti-slop < 2 families ·
4 STE lint · 5 six sweeps ≥ 8 · 6 adversarial review · 7 user clearances recorded.

## 9. Files
```
<series>/SERIES_STANDARD.md  keep-out.txt  build_preview.py
<series>/figures/            generator, SVGs, STYLE.md, preview.html
<series>/post-N-<slug>/      post.md  FACTS.md  NOTES.md  preview.html
```
