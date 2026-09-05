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

Do not draft first and fix later. Drafting before you have an anchor, persona, and voice signature
produces something you then have to rescue, and rescued drafts keep their original shape.

```
0. Anchor      → what is the actual system, domain constraint, and proof?
1. Persona     → who is the author as an engineer, and what stance do they embody?
2. Calibrate   → voice signature derived from exemplars or author profile
3. Shape       → format mechanics and non-adversarial archetypes
4. Draft       → in the signature and persona, against the anchor
5. Sweep       → six editing passes
6. Gate        → anti-slop audit + compliance checks, hard threshold
7. Ship
```

---

## Step 0: Anchor

**No anchor, no piece.** This is the step people skip, and skipping it is why most technical
content reads interchangeably.

Answer all four before writing a word:

| | |
|---|---|
| **The concrete thing** | The specific system, run, architecture, benchmark, or code artifact this comes from. Not the topic. The thing. |
| **The domain constraint / tension** | What statutory, physical, mathematical, or systems constraint makes this hard? What boundary condition must be respected? (Never manufacture artificial contrarianism or strawmen). |
| **The proof artifact** | The number, trace, benchmark, config, or clearing schedule that makes the claim checkable. |
| **The generalizable utility** | The practical pattern or decision procedure the reader can adapt for day-to-day systems. |

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

## Step 1: Discover the Author Persona & Stance

**No anonymous, disembodied writing.** Before calibrating sentence rhythm, discover who the author is as a practitioner:

1. **Domain Authority & Seniority:** What is the author's real-world background and technical edge? (e.g., senior engineer shipping production systems, staff systems architect, high-taste frontend/design engineer, researcher). Never default to treating the author as an apprentice or beginner discovering basic concepts - and equally never up-rank a hobbyist into a fake senior voice. The stance must match the author's actual experience.
2. **Core Strengths to Reflect:** What technical strengths should be evident in the draft? (e.g., deep runtime rigor, high-taste design craft, exact numerical accuracy, benchmark discipline).
3. **Authorial Stance:** How does the author teach? The default stance is **Quiet Production Authority & Peer-to-Peer Teaching**: respectful, encouraging, zero downplaying of other developers, zero failure-framing, first-person singular where the author writes as an individual, plain English headings.

### Persona presets

`references/personas/` holds researched voice profiles of well-known technical writers (Andrew Ng, Andrej Karpathy, Boris Cherny, DHH, Simon Willison, Linus Torvalds), each with verbatim excerpts from their blogs. Use them two ways:

- **As a matching lens:** when discovering the author's stance, read the persona files and identify which stance the author's own writing most resembles - it calibrates how you frame authority, facts, and explanation.
- **As a target voice:** if the user names one of these writers (or a similar stance) as the target voice, load that persona file and derive the voice signature from its verbatim excerpts via Step 2.

A user can also place their own author profile at `references/personas/<author-name>.md` following the same format; it takes precedence over the presets.

---

## Step 2: Calibrate the voice

Read `references/voice-extraction-protocol.md` and derive a signature from
`references/exemplars/`. Do this every time. Do not carry a signature across sessions from
memory; re-derive it, because the exemplar set changes.

If the user names a target voice not in the exemplars, ask for 3 to 5 samples of it. If they
have none, say so plainly and write in the house signature derived from what is there.

Output a compact `VOICE SIGNATURE` block before drafting. It is an operational spec, not
literary criticism. You will check the draft against it in Step 5.

**To add a voice:** drop samples into `references/exemplars/` as
`NN-short-slug.md` with the front-matter header shown in that folder's README. No code change.

---

## Step 3: Shape

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

**Which archetype?** Technical content mostly works in non-adversarial archetypes:
`domain constraint → architecture / DAG → deterministic guarantees` ·
`production pattern → personal system → protocol / metrics payload` ·
`decision → tradeoff map → recommendation` ·
`benchmark → physical limit → mechanism`

**Persuasion frameworks (PAS, AIDA, BAB) are usually the wrong tool for technical writing.** Applying PAS to an engineering post produces manufactured pain points and downplaying that technical readers filter out on sight. Reserve them for a piece that genuinely sells something (a launch post, a product announcement) - and even there, prefer the non-adversarial engineering archetypes.

---

## Step 4: Draft

Write against the anchor, in the persona, in the signature, in the shape. Rules that apply to every draft:

**First-person builder voice.** Where the author writes as an individual practitioner, use clear, grounded first-person singular ("I"). Never retreat into the detached academic third-person or royal "we" - except in registers where impersonal voice is house style (scientific, legal, formal).

**Plain English headings over jargon theater.** Use honest, descriptive terms. Reject inflated buzzwords ("dashboard" not "cockpit", "clearing timeline" not "tranches", "accumulated clutter" not "accretion drift").

**Zero downplaying of others.** Never open or frame with "most developers do X with toys". Domain constraints are the only antagonist. Correcting a factual misconception is fine; contempt for people is slop. True authority is quiet; let the problem carry the piece.

**Problem-explanation over failure-framing.** Frame headings and arguments around domain constraints ("The Real Challenges of Automating Personal Finances"), never around failure ("Why standard prompts break down").

**Lead with the mechanism, not the outcome.** "Decode is bottlenecked on memory bandwidth because every step re-reads the weights" beats "decode is slow."

**Every material claim carries a checkable artifact.** A number, a spec section (an RFC, a standard, a statutory code), a protocol, a benchmark, a config key, an identifier the reader can look up. State it exactly - never round, abbreviate, or paraphrase an identifier. (Illustration: "Section 50AA classifies international funds with under 65% domestic equity as debt funds" beats "overseas funds have tax penalties.")

**Name the specific identifier, not the category.** Not "the memory bottleneck" but "HBM bandwidth at 3.35 TB/s." Not "a big context" but "80K tokens."

**State the tradeoff, including what you give up.** "Mac unified memory fits models a 24GB card never would, but the memory is slower, so you trade throughput for capacity." Technical readers distrust anything presented as free.

**Take a position.** The generated default is to survey perspectives and close by noting what the analysis "raises." Say which one you would pick and why.

**Write the decision procedure, not just the analysis.** The most useful technical writing ends with something the reader can execute: a condition → choice mapping, a threshold, an ordered list of questions to answer first.

**Explain the term the first time, then use it.** No jargon without a definition, no definition without then using the term. Do not coin an abbreviation mid-paragraph.

**Show numbers when they change the decision.** Not as ornament. If the number does not move the reader's choice, it is noise.

**Grounded everyday utility over enterprise grandiosity.** End on practical, transparent systems for solving day-to-day problems. Never posture about "enterprise infrastructure."

**Balanced cadence.** Favor 2-4 sentence narrative paragraphs that give the eye breathing room; deliberately break the pattern where meaning demands it - uniform paragraph length is itself a slop tell. Restrict bullet points strictly to discrete sets; never dump monolithic text or bulleted shopping lists. The voice signature wins where it conflicts with this default.

---

## Step 5: Sweep

Six passes, in order, each on the whole piece. Full checklists in `references/editing-passes.md`.

1. **Clarity & Plain English:** Can a competent reader outside your team follow it without rereading? Are all headings free of jargon theater ("cockpit", "tranches")?
2. **So what & Problem Framing:** Does every claim answer "so what?" Is the piece framed around domain constraints rather than failure ("breaking down")? Does it take a position?
3. **Prove it & Authority:** Does every material claim map to a number, mechanism, named source, or observed outcome? Is there zero downplaying of peers? Does it end on grounded utility rather than enterprise posturing?
4. **Specificity:** Run the portability test. Does every paragraph describing a practice, cost, or constraint carry at least one number, named thing, or measurable quantity?
5. **Cadence & Structure:** Are paragraphs balanced with natural rhythm and zero bullet dumps? Do bullets carry only genuinely parallel discrete items?
6. **Voice & Whole-Piece Balance:** Read against the `VOICE SIGNATURE` from Step 2, dimension by dimension. Does quiet authority coexist with accessible peer teaching?

Score each 0 to 10. Below 8 on any pass, fix and re-run that pass. Do not proceed on a 7.

---

## Step 6: Gate

**Hard gate. Do not skip and do not ship below threshold.**

Run the `anti-slop-writing` skill in **audit mode** against the draft. Record the pattern-family count. Then confirm:

- [ ] Anti-slop audit shows **fewer than 2 pattern families**
- [ ] All six sweeps score 8 or above
- [ ] Every number, name, benchmark, config key, and quote traces to something real - verified, not just preserved
- [ ] No `[NO-PROOF]` or `[PLACEHOLDER]` tags remain, or they are surfaced explicitly to the user
- [ ] **Author authority intact:** the author sounds like the seniority and domain discovered in Step 1, with zero apprentice/hobbyist apologies and no invented authority
- [ ] **Zero downplaying of others:** no "most developers...", no "unlike prompt toys". Domain constraints are the only antagonist
- [ ] **Problem-explanation framing:** headings and arguments explain domain constraints; zero failure-framing
- [ ] **Plain English headings:** zero jargon theater ("cockpit", "tranches", "accretion drift")
- [ ] **Grounded everyday utility:** real practical systems; zero enterprise grandiosity
- [ ] **Zero dilution of technical rigor:** the author's actual identifiers - spec sections, protocols, metrics, timings - preserved unabridged
- [ ] **Whole-piece balance:** read aloud; if any sentence could appear in a conference abstract or a corporate press release, rewrite it. Authority without arrogance; clarity without whitepaper detachment

Fail any line and you iterate. Do not deliver a draft with a note explaining which checks it failed; fix it first. The only exception is a missing proof point the user must supply, which you surface at the top of the output.

---

## Step 7: Ship

Deliver the finished piece plus:

```
## Anchor used
concrete thing · domain constraint · proof · utility

## Persona & Voice applied
[author persona + voice signature]

## Scores
clarity N/10 · framing N/10 · proof N/10 · specificity N/10 · cadence N/10 · voice N/10
anti-slop: N pattern families

## Needs your input
[any [NEEDS PROOF] items, or "none"]
```

If the piece is for a repo, write it to the right path with front matter. Otherwise output the
full text and a suggested filename.

---

## Hard rules

- Never invent a statistic, benchmark, customer, incident, quote, or result.
- Never state a claim more confidently than the evidence supports. Hedge honestly or narrow the claim. Do not delete an honest hedge to sound authoritative.
- Never downplay other developers or treat peers as inferior ("most developers use toys").
- Never frame headings around others "failing" or "breaking down"; frame around domain constraints.
- Never replace confident first-person singular ("I built") with detached academic third-person ("the system was evaluated") or the royal "we", where the author writes as an individual practitioner.
- Never let a framework override the voice signature or author persona. The signature wins.
- Never open with manufactured curiosity, a rhetorical question, or "In today's."
- Never close with a summary recap or an aphorism.
- Never ship past the Step 6 gate.

## Done =

A piece anchored in something real, in an authentic persona and voice, where every claim
is checkable, that passes the gate and the anti-slop audit, and that gives the reader
practical utility they can act on tomorrow.
