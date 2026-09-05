# Editing passes

Six sweeps, each over the whole piece, in this order. Score each 0 to 10. Below 8, fix and
re-run that pass before moving on. Do not proceed on a 7.

Order matters. Specificity edits are wasted on a claim that "so what" would have cut.

---

## 1. Clarity & Plain English

Can a competent reader outside your team follow this without rereading?

- One idea per paragraph. Two to four sentences is the working default; deliberately break it
  where meaning demands. Do not flatten cadence that is merely distinctive.
- Untangle sentences that are genuinely hard to follow.
- **Plain English headings:** purge jargon theater. Use "dashboard" (not "cockpit"), "clearing
  timeline" (not "tranches"), plain operational terms anyone understands instantly.
- Every term defined the first time, then used. No jargon without a definition, no definition
  without subsequent use.
- No invented abbreviations. Use only ones already in circulation.
- One name for one thing. Do not rename a concept mid-piece for variety.
- Unambiguous pronouns. "It", "they", and "this" need clear antecedents.
- Active voice by default. Passive is fine when the actor is genuinely unknown or unimportant.
- Verbs do the work. "Decided", not "made a decision."
- Put related information together rather than scattering explanations of the same idea.

**Score 10:** a reader two steps removed from the subject follows it start to finish, and every
heading is plain, honest English.

---

## 2. So what & Problem Framing

Read each claim and literally ask "so what?"

- No answer means cut it.
- A weak answer means it is context, not payload. Demote it or compress it.
- If the whole piece has no answer, go back to Step 0. The anchor was never there.
- Does the reader end up able to *do* something differently? Name the thing.

Then walk every heading and transitional sentence:

- Eliminate failure-framing: "Why X breaks down", "Why casual prompting falls short", "The
  failure modes of...". Reframe as domain explanations: "The Real Challenges of Automating
  Personal Finances", "Statutory Constraints That Shape the Pipeline".
- Domain limits (statutory rules, memory bandwidth, latency budgets, protocol ceilings) are the
  primary antagonist - not other developers, tools, or methods failing.

Also check: does the piece take a position, or does it survey positions and close by observing
what the analysis "raises"? The second is the generated default. Take the position.

**Score 10:** every paragraph earns its place, the piece takes a position, and every heading
explains the domain rather than someone's failure.

---

## 3. Prove it & Authority

Every material claim maps to a number, a mechanism, a named source, or an observed outcome.

- Walk each claim. Tag anything unsupported as `[NO-PROOF]`.
- Replace vague attribution with a named source, or delete the claim. "Experts agree",
  "studies show", "industry reports suggest" all fail this pass.
- **Never invent a source, benchmark, number, or quote to satisfy this pass.** Convert to
  `[PLACEHOLDER: what is needed]` and surface it to the user.
- **Verify anything checkable:** file paths, function names, config keys, CLI flags, package
  names, version numbers, cited URLs. Generated drafts invent these confidently.
- Adjectives get replaced by proof. "Powerful analytics" becomes "shows which pages kill
  signups." "Robust" becomes the property you actually mean.
- The author's actual identifiers - spec sections, protocols, metrics, timings - stay intact
  and unabridged. Never round, abbreviate, or paraphrase them out.
- Named tradeoffs, including what the reader gives up. Anything presented as free is suspect.
- Honest hedging stays. Do not delete a real qualification to sound more authoritative.

Then the stance checks:

- **Author authority:** does the author sound like the practitioner they actually are? Strip
  accidental beginner apologies or performed incompetence ("I don't know what I'm doing") - but
  keep admissions that are specific and earned (they name a mechanism, number, or failed
  attempt). Genuine struggle is not slop.
- **Zero downplaying:** delete all sneers at "most developers", "prompt toys", or "amateurs".
  Correcting a factual misconception is fine; contempt for people is not.
- **Grounded everyday utility:** does the piece end on real, practical day-to-day systems? Cut
  grandiose posturing about "enterprise infrastructure".
- **First-person ownership:** where the author writes as an individual practitioner, use clear
  grounded first-person singular ("I built", "I architected"). Never hide behind the royal "we"
  or passive third-person - except where the register genuinely requires impersonal voice.

**Score 10:** a hostile reader with domain knowledge could check every claim and find nothing
overstated, and the author sounds like a confident senior builder teaching peers.

---

## 4. Specificity

Run the portability test on every sentence: swap the company, product, hardware, and person.
If the sentence survives unchanged, it is filler.

- Replace generic claims with names, numbers, dates, versions, and mechanisms.
- Name the identifier, not the category. Not "the memory bottleneck" but the actual bandwidth
  figure. Not "a large context" but the token count.
- Vague time ("quickly", "soon"), vague quantity ("many", "several"), and vague outcome
  ("better performance", "saves time") all get replaced or cut.
- Floor: every paragraph describing a practice, cost, or constraint carries at least one
  number, named thing, or measurable quantity. Roughly one per 200 words. Paragraphs that
  narrate, transition, or express opinion are exempt - do not stuff metrics into them.
- Content that cannot be made specific is probably filler. Cut it rather than tagging it.

Before and after:

```
"Saves time"           → "Cuts weekly reporting from 4 hours to 15 minutes"
"Used by many teams"   → "Used by 4,200 teams across 60 countries"
"Improved efficiency"  → "Cut deploy time from 40 minutes to 4"
"A skilled technician" → "The repair takes five minutes and needs no soldering"
```

**Score 10:** no sentence in the piece could appear unchanged in someone else's post.

---

## 5. Cadence & Structure

Check the reading rhythm and the visual shape of the piece.

- **Narrative rhythm:** paragraphs mostly 2-4 sentences, with deliberate variation - some one
  sentence, some five or six. Uniform paragraph length is itself a slop tell.
- **Zero bullet dumps:** bullet points carry only genuinely parallel discrete items (e.g. the
  items of an allocation, the entries of a checklist). If bullets contain multi-paragraph
  explanations, convert them to narrative prose.
- **Prose carries argument; lists carry parallel items.** Prose-then-list, not list-then-prose.
- **No walls of text:** monolithic blocks of prose that cause eye fatigue get split.
- Sentence-length spread matches the voice signature; no run of 3+ sentences within 5 words of
  each other.

**Score 10:** high signal density with a light feel - the reader's eye never tires and never
skims a grocery list.

---

## 6. Voice & Whole-Piece Balance

Read against the `VOICE SIGNATURE` from Step 2, **dimension by dimension**. An overall
impression check passes drafts that are wrong in every measurable way.

- [ ] Mean sentence length within ±2 words of the signature
- [ ] Sentence-length spread matches; no run of 3+ sentences within 5 words of each other
- [ ] Paragraph lengths vary as the signature does
- [ ] Capitalisation convention matches line by line
- [ ] Parenthetical rate and usage match
- [ ] Question frequency and kind match
- [ ] Em dash count matches the signature, usually zero
- [ ] Connectors drawn from the author's actual set, not rotated for variety
- [ ] Receipts per 100 words match the signature rate
- [ ] Opening line belongs in the collected openings set
- [ ] Closing line belongs in the collected closings set
- [ ] Every item on the never-do list checked individually

Then the whole-piece balance, applied on top (never instead of the dimensions above):

- Does quiet authority coexist with accessible peer teaching? Authority without arrogance,
  clarity without academic whitepaper detachment.
- Is technical rigor preserved without posturing?

Then read it aloud. Rhythm problems are audible where they are invisible on screen.

Final question: **would the author recognise this as their own writing?** Competent but generic
means the signature was applied as decoration rather than structure. Go back to drafting.

**Score 10:** it is indistinguishable from the exemplars on every measured dimension, and all
five previous sweeps held simultaneously.

---

## After the sweeps

Proceed to the Step 6 gate in `SKILL.md`. The gate runs the `anti-slop-writing` skill in audit
mode and has a hard threshold. The sweeps are not a substitute for it. They check whether the
piece is good; the gate checks whether it reads as machine-written. Those are different
failures.
