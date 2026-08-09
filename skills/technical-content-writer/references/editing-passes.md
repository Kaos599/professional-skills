# Editing passes

Five sweeps, each over the whole piece, in this order. Score each 0 to 10. Below 8, fix and
re-run that pass before moving on. Do not proceed on a 7.

Order matters. Specificity edits are wasted on a claim that "so what" would have cut.

---

## 1. Clarity

Can a competent reader outside your team follow this without rereading?

- One idea per paragraph. Three to five sentences maximum, fewer for social.
- Untangle sentences that are genuinely hard to follow. Do not flatten cadence that is merely
  distinctive.
- Every term defined the first time, then used. No jargon without a definition, no definition
  without subsequent use.
- No invented abbreviations. Use only ones already in circulation.
- One name for one thing. Do not rename a concept mid-piece for variety.
- Unambiguous pronouns. "It", "they", and "this" need clear antecedents.
- Active voice by default. Passive is fine when the actor is genuinely unknown or unimportant.
- Verbs do the work. "Decided", not "made a decision."
- Put related information together rather than scattering explanations of the same idea.

**Score 10:** a reader two steps removed from the subject follows it start to finish.
**Score 5:** they follow it but reread twice.

---

## 2. So what

Read each claim and literally ask "so what?"

- No answer means cut it.
- A weak answer means it is context, not payload. Demote it or compress it.
- If the whole piece has no answer, go back to Step 0. The anchor was never there.
- Does the reader end up able to *do* something differently? Name the thing.

Also check: does the piece take a position, or does it survey positions and close by observing
what the analysis "raises"? The second is the generated default. Take the position.

**Score 10:** every paragraph earns its place and the reader can act on the whole.

---

## 3. Prove it

Every material claim maps to a number, a mechanism, a named source, or an observed outcome.

- Walk each claim. Tag anything unsupported as `[NO-PROOF]`.
- Replace vague attribution with a named source, or delete the claim. "Experts agree",
  "studies show", "industry reports suggest" all fail this pass.
- **Never invent a source, benchmark, number, or quote to satisfy this pass.** Convert to
  `[PLACEHOLDER: what is needed]` and surface it to the user.
- Verify anything checkable: file paths, function names, config keys, CLI flags, package names,
  version numbers, cited URLs. Generated drafts invent these confidently.
- Adjectives get replaced by proof. "Powerful analytics" becomes "shows which pages kill
  signups." "Robust" becomes the property you actually mean.
- Named tradeoffs, including what the reader gives up. Anything presented as free is suspect.
- Honest hedging stays. Do not delete a real qualification to sound more authoritative.

**Score 10:** a hostile reader with domain knowledge could check every claim and find nothing
overstated.

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
  number, named thing, or measurable quantity. Roughly one per 200 words.
- Content that cannot be made specific is probably filler. Cut it rather than tagging it.

Before and after, from the corpus:

```
"Saves time"           → "Cuts weekly reporting from 4 hours to 15 minutes"
"Used by many teams"   → "Used by 4,200 teams across 60 countries"
"Improved efficiency"  → "Cut deploy time from 40 minutes to 4"
"A skilled technician" → "The repair takes five minutes and needs no soldering"
```

**Score 10:** no sentence in the piece could appear unchanged in someone else's post.

---

## 5. Voice

Read against the `VOICE SIGNATURE` from Step 1, **dimension by dimension**. An overall
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

Then read it aloud. Rhythm problems are audible where they are invisible on screen.

Final question: **would the author recognise this as their own writing?** Competent but generic
means the signature was applied as decoration rather than structure. Go back to drafting.

**Score 10:** it is indistinguishable from the exemplars on every measured dimension.

---

## After the sweeps

Proceed to the Step 5 gate in `SKILL.md`. The gate runs the `anti-slop-writing` skill and has a
hard threshold. The sweeps are not a substitute for it. They check whether the piece is good,
the gate checks whether it reads as machine-written. Those are different failures.
