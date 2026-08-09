---
name: technical-content-writer
description: Write technical content that sounds like a specific human wrote it - LinkedIn posts, blog posts, threads, newsletters, essays about engineering and infrastructure subjects. Derives a voice signature from exemplars before drafting, forces mechanism and numbers over adjectives, and runs an anti-slop gate before output. Use when writing or rewriting any technical content for a public audience.
---

# Technical Content Writer

Distilled from 55 published writing-craft skills (copywriting, LinkedIn, ghostwriting,
technical writing, brand voice, content strategy) plus 45 anti-slop skills. Method and
provenance in `../anti-slop-writing/references/corpus-evidence.md`.

## What this is for

Content about technical subjects, written for people who could tell if you were faking it.
Infrastructure, model serving, data pipelines, systems tradeoffs. The reader can check your
claims, so the writing has to survive being checked.

That constraint is the whole design. Most content-writing advice optimises for persuasion.
This optimises for **being right in a way that is also readable**, which is a different job.

## The order matters

Do not draft first and fix later. Drafting before you have an anchor and a voice signature
produces something you then have to rescue, and rescued drafts keep their original shape.

```
0. Anchor      → what is the actual thing you know?
1. Calibrate   → whose voice, derived from exemplars
2. Shape       → format mechanics and structure
3. Draft       → in the signature, against the anchor
4. Sweep       → five editing passes
5. Gate        → anti-slop scan, hard threshold
6. Ship
```

---

## Step 0: Anchor

**No anchor, no piece.** This is the step people skip, and skipping it is why most technical
content reads interchangeably.

Answer all four before writing a word:

| | |
|---|---|
| **The concrete thing** | The specific system, run, incident, benchmark, or decision this comes from. Not the topic. The thing. |
| **The counter-intuitive claim** | What does this contradict? If it confirms what the reader already believes, there is no piece. |
| **The proof artifact** | The number, trace, config, benchmark, or receipt that makes the claim checkable. |
| **The generalizable lesson** | What the reader can now do differently. |

Pull these from what the user actually has. If a proof artifact is missing, ask **once**. If
there is still none, narrow the claim until it is honest, write the piece around the mechanism
instead of the result, and flag `[NEEDS PROOF]` inline before publishing.

**Never invent a number, customer, benchmark, incident, or quote.** This is absolute. In
technical content the reader can check, and one invented figure destroys everything else you
wrote.

If a claim cannot be made specific, tag it rather than smoothing it:

```
"The fastest solution on the market."
  → [NO-PROOF] → [PLACEHOLDER: benchmark number or third-party comparison]
```

---

## Step 1: Calibrate the voice

Read `references/voice-extraction-protocol.md` and derive a signature from
`references/exemplars/`. Do this every time. Do not carry a signature across sessions from
memory; re-derive it, because the exemplar set changes.

If the user names a target voice not in the exemplars, ask for 3 to 5 samples of it. If they
have none, say so plainly and write in the house signature derived from what is there.

Output a compact `VOICE SIGNATURE` block before drafting. It is an operational spec, not
literary criticism. You will check the draft against it in Step 4.

**To add a voice:** drop samples into `references/exemplars/` as
`NN-short-slug.md` with the front-matter header shown in that folder's README. No code change.

---

## Step 2: Shape

Pick the format, then load its mechanics from `references/structure-playbooks.md`.
That file holds the hard numbers: character limits, fold positions, paragraph lengths,
hashtag placement, CTA position, and the archetypes that fit technical material.

Then pick a **register** from `references/house-styles.md`: analytical, opinionated survey, long
explainer, or institutional procedural. That file carries measured signatures from real
published technical writing, including the two findings that most often get drafts wrong:

- **Nobody good exceeds ~0.6 em dashes per 500 words**, and the writers who build long sentences
  use semicolons instead of reaching for a dash.
- **Heading density trades off against question density.** A long piece needs one or the other
  carrying navigation. Tailscale sustains 8,800 words on 5 headings because it asks a question
  every ~15 sentences. Fly.io needs a heading every ~320 words because it asks almost none.

Three decisions before drafting:

**Which archetype?** Technical content mostly works in one of five shapes:
`myth → mechanism → decision rule` · `incident → diagnosis → generalization` ·
`benchmark → surprise → explanation` · `decision → tradeoff map → recommendation` ·
`build log → what broke → what I would do differently`

**Do you need a persuasion framework at all?** PAS, AIDA, BAB, and StoryBrand are in the
playbook because they are the corpus consensus for marketing copy. **They are usually the wrong
tool here.** Applying PAS to an engineering post produces the manufactured-pain opener that
technical readers filter out on sight. Use a framework when the piece is genuinely selling
something. Otherwise use an archetype.

---

## Step 3: Draft

Write against the anchor, in the signature, in the shape. Rules that apply to every draft:

**Lead with the mechanism, not the outcome.** "Decode is bottlenecked on memory bandwidth
because every step re-reads the weights" beats "decode is slow." A reader who understands the
mechanism can extend it. A reader who knows the outcome cannot.

**Every claim about a practice, cost, or constraint carries a number, a named thing, or a
measurable quantity.** One corpus skill sets this as a hard floor of roughly one per 200 words.
It is a good floor.

**Name the specific identifier, not the category.** Not "the memory bottleneck" but "HBM
bandwidth at 3.35 TB/s." Not "a big context" but "80K tokens." Specificity is not decoration
here; it is the difference between a claim and a vibe.

**State the tradeoff, including what you give up.** "Mac unified memory fits models a 24GB card
never would, but the memory is slower, so you trade throughput for capacity." Technical readers
distrust anything presented as free.

**Take a position.** The generated default is to survey perspectives and close by noting what
the analysis "raises." Say which one you would pick and why.

**Write the decision procedure, not just the analysis.** The most useful technical writing ends
with something the reader can execute: a condition → choice mapping, a threshold, an ordered
list of questions to answer first.

**Explain the term the first time, then use it.** No jargon without a definition, no definition
without then using the term. Do not coin an abbreviation mid-paragraph.

**Show numbers when they change the decision.** Not as ornament. If the number does not move
the reader's choice, it is noise.

---

## Step 4: Sweep

Five passes, in order, each on the whole piece. Full checklists in `references/editing-passes.md`.

1. **Clarity.** Can a competent reader outside your team follow it without rereading?
2. **So what.** Read each claim and literally ask "so what?" No answer means cut.
3. **Prove it.** Every material claim maps to a number, mechanism, source, or observed
   outcome. Anything left over gets tagged, not smoothed.
4. **Specificity.** Run the portability test on every sentence. Swap the company, product,
   and hardware. Anything that survives unchanged is filler.
5. **Voice.** Read against the `VOICE SIGNATURE` from Step 1, dimension by dimension. Sentence
   length distribution, capitalisation, parentheticals, question frequency, connectors, and the
   never-do list.

Score each 0 to 10. Below 8 on any pass, fix and re-run that pass. Do not proceed on a 7.

---

## Step 5: Gate

**Hard gate. Do not skip and do not ship below threshold.**

Run the `anti-slop-writing` skill in audit mode against the draft. Then confirm:

- [ ] Anti-slop audit shows **fewer than 2 pattern families**
- [ ] All five sweeps score 8 or above
- [ ] Every number, name, benchmark, and quote traces to something real
- [ ] No `[NO-PROOF]` or `[PLACEHOLDER]` tags remain, or they are surfaced explicitly to the user
- [ ] Draft matches the voice signature on every dimension
- [ ] Read aloud, it sounds like the person in the exemplars

Fail any line and you iterate. Do not deliver a draft with a note explaining which checks it
failed; fix it first. The only exception is a missing proof point the user must supply, which
you surface at the top of the output.

---

## Step 6: Ship

Deliver the finished piece plus:

```
## Anchor used
concrete thing · claim · proof · lesson

## Voice signature applied
[the block from Step 1]

## Scores
clarity N/10 · so-what N/10 · prove-it N/10 · specificity N/10 · voice N/10
anti-slop: N pattern families

## Needs your input
[any [NEEDS PROOF] items, or "none"]
```

If the piece is for a repo, write it to the right path with front matter. Otherwise output the
full text and a suggested filename.

---

## Hard rules

- Never invent a statistic, benchmark, customer, incident, quote, or result.
- Never state a claim more confidently than the evidence supports. Hedge honestly or narrow the
  claim. Do not delete an honest hedge to sound authoritative.
- Never let a framework override the voice signature. The signature wins.
- Never ship past the Step 5 gate.
- Never open with manufactured curiosity, a rhetorical question, or "In today's."
- Never close with a summary recap or an aphorism.

## Done =

A piece anchored in something real, in a voice derived from actual samples, where every claim
is checkable, that passes the anti-slop gate, and that gives the reader a decision they can
make differently tomorrow.
