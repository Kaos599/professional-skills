# Workflow: the six phases in detail

∥ = parallel subagents launched in one message. Use a fresh subagent per task. Resume one
only to fix its own work. Keep raw fetches (HTML, PDFs, text dumps) in the scratchpad.

---

## Phase 1: Voice and references

**1a. Load the writing skills**: `technical-content-writer`, `anti-slop-writing`,
`simplified-technical-english`.

**1b. Intake.** Ask the batched questions in `intake.md`: references, audience, purpose and
scope, plus the shape questions if there's no voice to copy.

**1c. Study the references ∥**, one subagent per site or post:

- *The author's site* (voice and design):
  > Fetch <site>, its blog index and these posts: <urls>. Report (a) design tokens: background,
  > ink, muted, hairline and accent colours for dark and light, fonts (Google Fonts names),
  > column width, heading scale and spacing; (b) voice: three verbatim excerpts showing how a post
  > opens, explains a mechanism and closes, plus sentence length, use of first person,
  > contractions, bold and lists. Under 600 words.
- *Each admired post* (anatomy, not phrasing):
  > Read <url>. Extract how it opens (first 3 sentences), how each section moves from claim to
  > evidence, where the numbers sit, what each figure claims, how it handles what it doesn't
  > know, and how it ends. List 5 transferable techniques, each with a quote.

**1d. Synthesise.** Write the `VOICE SIGNATURE` (from the author's posts, or from the intake
answers), the design tokens for the preview page, and a short list of reference techniques
to use. If no persona file exists, offer to save one.

---

## Phase 2: Topic research

**2a. Primary sources ∥** (papers, specs, official docs). One subagent per source, or read
it yourself:
> Read <source>. Return page/section-cited notes: definitions; method parameters, credited to
> the specific method rather than the survey as a whole; quotes, with the surrounding paragraph so
> it's clear what each quote is actually about; and a list of what this source does NOT cover
> that a practitioner would need.

**2b. The author's own evidence ∥**, one subagent per area (for example: ingest, processing,
model/cost, evaluation, incidents):
> In <repo/data/notes>, find every measured result about <area>. For each: claim, number, n,
> comparison, CI or noise floor, file:line, caveats (selection, single labeller, confounds,
> superseded by a later doc). Flag anything documented as a trap or bug. Don't run paid jobs.
> Don't open secret files.

Then spot-check the 3–5 numbers the post will lean on hardest. Read the cited lines yourself.

**2c. Industry and scale facts ∥**, one subagent per sector or organisation:
> Find the primary source for <fact> (the organisation's own page, rules document or filing).
> Return the exact figure, its date, a verbatim quote, and the URL. Label vendor marketing
> claims as such. Report the wording exactly ("on one day" is not "at once").

**2d. Pull it together: the concept inventory.** Make the tracker (a Claude Doc, or
TRACKER.md):
- the series plan placeholder;
- a concept table: concept · candidate post · status (*have evidence* / *source only* /
  *no context* / *needs user*) · source;
- research gaps and tasks, decisions (quoting the user), open questions;
- the keep-out list and a link to the standard.

Claude Docs batches hold at most 64 blocks. Keep tables lean (one dropdown column).

---

## Phase 3: Shape the series (with the user)

Bring: the concept inventory, one recommended split (with one alternative only if it's
genuinely close), the one idea each post leaves the reader with, and what post 1 must set
up. Expect the user to reshape it. Record their decisions in the tracker. Don't draft
until they agree.

---

## Phase 4: Standard and draft

1. Fill in `templates/SERIES_STANDARD.md`, starting from `writing-standard.md` and the voice
   signature. Copy `templates/FACTS.md` and `templates/NOTES.md` into the post folder.
2. Write `keep-out.txt` (one term per line) for `check_post.py`.
3. Draft from `templates/post.md`. Anchor it first (`technical-content-writer` Step 0: the
   concrete thing, the domain constraint, the proof artifact, the generalisable utility).
   Add a FACTS row with every number. Run `check_post.py` before showing the user.
4. Run the six sweeps from `technical-content-writer` yourself and fix anything under 8.

---

## Phase 5: Figures and preview

1. Copy `scripts/figure_kit.py` → `<series>/figures/build_figures.py`. Write a
   `figures/STYLE.md` from `figure-system.md`, with the series' accent and hazard colour.
2. For each figure, state its claim in the preceding paragraph, then build it. A figure
   subagent ∥ works well. Give it the files it may edit, the standard, the prose per
   figure, a numbered change list, and the screenshot command.
3. `scripts/shoot_figures.py <figdir> <outdir> <tag> dark light`, then read every PNG
   yourself.
4. `scripts/build_preview.py <post-dir>` (restyle its tokens to the author's site first),
   then publish a private Artifact. Republish from the same path to keep the URL.

---

## Phase 6: Review, fix, gate

1. Run the panel ∥ (`review-panel.md`). Give every reviewer the user's fixed inputs and the
   known clearance items.
2. Verify each blocker and each new number a reviewer proposes. Read the cited lines, or
   recompute from the raw data.
3. Report once. Apply the fixes as vN+1, log them in NOTES, add FACTS rows, re-run
   `check_post.py`, rebuild and republish.
4. Run the gates (SKILL.md). Stop when they pass.
5. For the next post, reuse everything and re-light the rail. Re-run phase 2 only for new
   topics.

## Verification habits (every phase)

- Read the primary table or cited lines before relaying a subagent's number. Research agents
  misquote tables and licences.
- "X appears nowhere" from a reviewer means grep for it before you agree.
- Recompute any reviewer-proposed statistic from the raw data before you adopt it.
- Check who a person in the evidence actually was before renaming their role. It may be
  the author.
