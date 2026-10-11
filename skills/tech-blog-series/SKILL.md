---
name: tech-blog-series
description: Plan, research, write, illustrate and review a technical blog post or a series of posts (your own practice plus industry and research context) with a consistent voice, a hand-built SVG figure system, a fact ledger and an adversarial review panel. Use when asked to write a technical blog or blog series, turn a codebase/paper/research into posts, make explanatory figures for a post, set a standard so later posts stay consistent, or review/grade a technical blog draft (nemesis + 10-metric grader + 3 reader POVs).
---

# Technical blog series

A six-phase workflow for posts that a checking reader (an engineer) and a non-technical
reader (a buyer, a curious outsider) can both get through, where every number is traceable
and every figure was drawn on purpose. It works for one post or a series. It was distilled
from a real multi-post series built through six drafts and three review rounds. Expect a
first draft to fail several gates, and plan for 2–3 panel rounds
(`references/review-panel.md`, `references/lessons-learned.md`).

Roles: **you orchestrate and review. Subagents research, draw and review.** You decide what
goes in, verify what subagents report against the sources before you relay it, and hold the
standard. The user decides on content, clearance and scope.

## Dependencies

Load the writing skills with the Skill tool in phase 1. If one is missing, install it or use
the fallback.

| Skill / agent | Used for | Where to get it | Fallback |
|---|---|---|---|
| `technical-content-writer` | anchor → persona → voice signature → draft → six sweeps → gate | bundled in this repo (`skills/technical-content-writer`) | `references/writing-standard.md` |
| `anti-slop-writing` | audit mode for the gate (< 2 pattern families), clean-drafting rules, and `scripts/slop_scan.py` for the mechanical scan | bundled in this repo (`skills/anti-slop-writing`) | §6 of `references/writing-standard.md` |
| `simplified-technical-english` | a **lint only**: vague words, noun clusters, inconsistent names, paragraph length. Never a rewrite, because it bans contractions | `git clone https://github.com/0xpili/simplified-technical-english ~/.claude/skills/simplified-technical-english` | skip the lint |
| `artifact-design` + Artifact tool | private preview page | built into Claude Code | open `preview.html` locally |
| Claude Docs connector (`docs` skill) | planning tracker | claude.ai connector | `TRACKER.md` in the series folder |
| `nemesis-review` agent | adversarial reviewer | optional custom agent | `general-purpose` + the prompt in `references/review-panel.md` |
| research agents (`researcher`, `deep-ass-research`, Exa or Tavily MCPs) | web research with citations | optional | `general-purpose` agents with WebSearch/WebFetch |

The scripts in `scripts/` need Python 3, plus Google Chrome for screenshots.

## The six phases

| # | Phase | Output | Waits for the user? |
|---|---|---|---|
| 1 | Voice and references | voice signature, design tokens, reference anatomy | yes: intake answers and links |
| 2 | Topic research | evidence inventory, then a concept inventory in the tracker | no |
| 3 | Shape the series | agreed post list, one idea per post | **yes: alignment** |
| 4 | Standard and draft | SERIES_STANDARD, FACTS, NOTES, then post N | no |
| 5 | Figures and preview | SVG figures, screenshots, published preview | no |
| 6 | Review, fix, gate | panel scores, verified findings, vN+1, gates | yes: clearances |

The details and the subagent prompts for each phase are in `references/workflow.md`. Steps
marked ∥ run as parallel subagents, launched in one message.

### 1. Voice and references

- Load `technical-content-writer`, `anti-slop-writing` and `simplified-technical-english`.
- **Ask once, batched** (the question set is in `references/intake.md`): the reference
  sites and blogs to learn from (the author's own site or blog for voice and design, plus
  2 to 4 posts they admire), the audience, the purpose, and the series size.
- **If the author has published writing**: study it ∥, together with the reference blogs
  ∥. Derive a `VOICE SIGNATURE` (format: `references/voice-example.md`),
  the design tokens for the preview page, and the anatomy of each reference: how it opens,
  where the numbers sit, what the figures claim, how it ends.
- **If there's no voice to copy**: ask the shape questions in `intake.md` (person, tone,
  length, story vs reference, analogies, figure density, bans), and build the signature
  from the answers. Offer to save it as a persona file.

### 2. Topic research ∥

Research around the subject, then pull it together:
- **Primary sources** (papers, specs, docs): page-cited claims, method parameters credited
  to the specific method, and **what the source does not cover**. That gap is often where
  the author's own story lives.
- **The author's own evidence** (codebase, data, incident notes, experiments): one subagent
  per area returns claim · number · n · file:line · caveats. Spot-check the numbers the post
  will lean on.
- **Industry and scale facts**: primary sources only, wording matched exactly, vendor claims
  labelled as vendor claims.
- **What it all adds up to**: a concept inventory in a tracker doc. Mark each concept *have
  evidence* / *source only* / *no context* / *needs the user*, and add decisions, open
  questions and the keep-out list.

### 3. Shape the series (with the user)

Bring the concept inventory and one recommended split, then align. A good default is 3 to 5
posts at most, with post 1 as a prerequisite and context post covering the problems, the
major things the team deals with, and how. Don't start writing before the user agrees.

### 4. Standard and draft

Fill in `templates/SERIES_STANDARD.md` (voice, storytelling, anatomy, numbers, public names,
figure rules, gates), `templates/FACTS.md` and `templates/NOTES.md`, then draft from
`templates/post.md`, following `references/writing-standard.md`. Every number gets a FACTS
row as it's written.

### 5. Figures and preview ∥

- Figures are hand-built SVG from a generator, following `references/figure-system.md`.
  Copy `scripts/figure_kit.py` to `<series>/figures/build_figures.py` first,
  because it writes next to itself.
- Screenshot both themes with `scripts/shoot_figures.py`, look at every PNG yourself, and
  iterate.
- Build the preview with `scripts/build_preview.py <post-dir>`, restyled to the author's
  site (`references/page-design.md`), and publish it as a private Artifact.

### 6. Review, fix, gate

- Run the panel ∥: nemesis + 10-metric grader + 3 reader POVs
  (`references/review-panel.md`).
- **Verify the strongest claims yourself** before you relay them. Reviewers overclaim and
  miss things.
- Report once: scores, confirmed issues, where readers drop off, what to keep, **one**
  recommendation, and the batched clearance questions.
- Apply the fixes as vN+1 and log them in NOTES. Then run `scripts/check_post.py`, rebuild,
  and republish.
- **Gates**: FACTS complete · keep-out clean · anti-slop < 2 families · STE lint clean of
  real findings · six sweeps ≥ 8 · no open blockers · clearances recorded.
  The anti-slop gate can run mechanically too:
  `python3 <skills-dir>/anti-slop-writing/scripts/slop_scan.py post.md`.
- **Stop rule**: stop when every gate passes. Re-grade only when the user asks, or when a
  fix round touched evidence or structure.
- Posts 2..N reuse the standard, glossary, figure kit and keep-out list. Re-light the series
  rail and start from phase 4. Run phase 2 again only for new topics.

## Default preferences (confirm in intake; the user's answers win)

- **Relatable first.** Open on a concrete scene from a domain any reader knows, with stakes
  and the one hard physical fact. Then scale ("now do that for every …"), then the chain of
  jobs, then why doing it by hand fails. That's the problem the post is about.
- **Human storytelling.** A person in every opening paragraph, a human beat in each incident,
  and the opening scene returning at the end. Analogies from the reader's world. No fact
  dumps.
- **Generalise.** The author's product is one part. Cover the whole pipeline plus the
  industry and research context.
- **Two layers.** The story goes in the body. Mechanism, flags and statistics go in "For
  engineers" asides.
- **Figures** that look drawn with care: one idea each, minimal text, technically exact.
- **The user's statements about their own system are fixed inputs.** Reviewers don't
  relitigate them.

## Hard rules

- **Never invent** a number, incident, quote, customer or result. A scene framed as
  "Picture…" may carry illustrative detail, but no statistics.
- **No FACTS row, no number.** Removed claims are listed with the reason, and the
  references and title are re-checked after any cut.
- **Keep-out list**, checked before every publish (`check_post.py --keep-out`): internal
  system and model names, customer or partner names without clearance, ids, hosts and
  buckets, internal service names, people other than the author, prompt text, volumes,
  spend, key fragments. Customer names stay `[CLEAR?]` until the user clears them, even if
  the user asked to use them.
- **Evidence honesty** (`writing-standard.md` §5): give n when it's under 30, CIs that
  include zero, selection effects, rerun drift, confounds, a single labeller, and
  distributions rather than means.
- The project's own rules (secrets, commits) win. Never `git add -A`. Don't commit or push
  unless asked.
- One decisive recommendation per report. No option menus.

## Files

```
references/intake.md                questions for phase 1 (references, audience, shape preferences)
references/workflow.md              the six phases in detail, with subagent prompts
references/writing-standard.md      readers, storytelling, voice, anatomy, evidence honesty, anti-slop
references/figure-system.md         visual language, rules, figure types, checks
references/page-design.md           preview page layout, theme, components, phone width, publishing
references/review-panel.md          nemesis / grader / readers prompts, metrics, triage, score history
references/lessons-learned.md       mistakes from a real multi-draft series and the rule each produced
references/voice-example.md         a worked voice signature
templates/                          SERIES_STANDARD.md  FACTS.md  NOTES.md  post.md
scripts/check_post.py               mechanical lint (exit 1 on hard-rule failures)
scripts/build_preview.py            post.md → single themed HTML page with inlined SVGs
scripts/shoot_figures.py            every fig-*.svg → PNG in dark/light via headless Chrome
scripts/figure_kit.py               domain-neutral SVG generator: primitives + one example per figure type
examples/series-standard-example.md a filled-in standard ("From log line to alert", invented)
examples/facts-example.md           a filled-in fact ledger with additions, cuts and do-not-use
examples/cold-opens.md              fact-list vs human openings in five domains
examples/review-report-example.md   the one consolidated message after a panel round
examples/figure-style.md            the kit's style guide (STYLE.md for a series)
examples/figures/                   the kit's example figures (SVG) + preview.html
```
