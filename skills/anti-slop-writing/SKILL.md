---
name: anti-slop-writing
description: Make writing sound like a person wrote it. Rewrites drafts that read as machine-generated, restores voice that AI editing flattened, and audits text for AI tells when asked. Use when a draft feels generic or corporate, when polishing anything an LLM helped write, before publishing a post or doc, or when someone asks whether writing "sounds like AI".
---

# Anti-Slop Writing

Make the writing better and make it sound like a person. Removing tells is the means, not the end.

Distilled from 45 published anti-slop and humanizing skills. Harvest method and hard counts in
`references/corpus-evidence.md`.

## Read this first, or the rest will mislead you

**Word lists are the weakest signal and they are going stale.** `delve`, `tapestry`, `vibrant`,
and `myriad` are largely absent from current frontier-model output. A draft that avoids them is
not human. It is just newer.

Four consequences that govern everything below:

1. **Structure outlives vocabulary.** Sentence-shape and paragraph-shape tells survive model
   updates. Word tells do not. Weight structure higher.
2. **Tells are diagnostic in clusters, not alone.** One em dash means nothing. Em dashes plus a
   rule-of-three plus an "In conclusion" section plus uniform paragraph lengths is a confession.
   Never flag a single occurrence as evidence.
3. **The failure mode is over-correction.** Stripping every flagged token turns distinctive
   human writing into flat, cautious prose. That is a different kind of slop, and it is the one
   this skill is most likely to cause. Deleting is easy; the hard half is Step 6.
4. **These heuristics are biased against non-native English speakers.** Simpler vocabulary,
   more formal connectives, and more even sentence rhythm are all normal in competent
   second-language writing, and all trip the checks below. Never tell someone their writing
   "sounds like AI" on rhythm and connective evidence alone. Name specific patterns and let
   them judge.

## Three modes

**IMPROVE (default).** The draft needs to be better and sound like a person. Rewrite it. Return
the edited draft plus a `What changed` section. This is what to do unless told otherwise.

**AUDIT.** Someone wants to know if a piece reads as machine-written, without a rewrite. Name
each pattern, quote the line, give the fix in a few words. Do not rewrite. Do not output a
probability that the text was AI-generated: you cannot know that, detectors guess, and they are
most wrong against the writers named in point 4. Named patterns are checkable. A score is not.

**RESTORE.** A specific and common case: the draft was *already* edited by an AI and came back
flattened. The tells are gone but so is the person. Skip Steps 3 and 4, go straight to Step 6,
and work from whatever earlier draft or sample of the author's writing you can get.

## Dose

Decide before editing. State which you chose in the output.

| Dose | When | What you touch |
|---|---|---|
| **Light** | strong draft, a few tells | named patterns only, nothing else |
| **Medium** | default | patterns, rhythm, and specificity |
| **Heavy** | reads as fully generated, author agrees | structure and argument order too |

**Heavy is opt-in.** Never restructure someone's argument because it would be tidier. If the
draft needs a heavy pass and you were not asked for one, do a medium pass and say what a heavy
one would change.

If the draft is already good, **say so and stop.** "Two minor things, otherwise this reads fine"
is a complete and correct output. Manufacturing findings to look useful is its own failure.

## Genre calibration

The rules below are not uniform across formats. Set this in Step 0.

| Format | Em dashes | Contractions | Fragments | Structure |
|---|---|---|---|---|
| Social post | zero | yes | yes | loose |
| Blog, essay | ≤1 per 500w | yes | sparingly | headings ok |
| Technical docs | ≤1 per 500w | yes | no | headings required |
| Commit message | zero | no | no | imperative subject, prose body |
| Legal, medical, formal | as house style | no | no | house style wins |

Where a house style guide exists, it beats this skill.

## Procedure

### 0. Establish the baseline

Read the whole draft. Note internally, do not output:

- The core point in one sentence. If you cannot find it, ask rather than guessing.
- 3 to 5 **voice signals to protect**: vocabulary, cadence, bluntness, humour, digressions,
  admissions, profanity, level of polish.
- Format, audience, and genre row from the table above.
- Dose.

Anything you cannot attribute to a rule below stays exactly as written. That is the default,
not a fallback.

### 1. Run the mechanical scan

Countable. Run before making judgment calls. Thresholds and reasoning in
`references/detection-rubric.md`.

| Check | Flag when |
|---|---|
| Em dashes | above the genre budget, or any cluster |
| Sentence-length spread | standard deviation under ~4 words over a 100-sentence window |
| Consecutive same-length runs | 3+ sentences within 5 words of each other |
| Sentence-opener repetition | over half a paragraph's sentences start with The / This / It / In |
| Formal transitions | more than ~8 per 1,000 words |
| Hedging density | over ~5% of words |
| Passive constructions | over ~30% of sentences |
| Rule-of-three lists | any list of exactly three near-synonyms |
| Paragraph-length uniformity | most paragraphs within one sentence of each other |
| Unsourced authority | "experts agree" / "studies show" with no name |
| Specificity floor | any paragraph with no number, name, date, or measurable quantity |

**Scan mechanically, never fix mechanically.** A find-and-replace across a draft produces
sentences that are grammatical and wrong, because the right substitute differs by clause. Fix
per occurrence. This skill's own reference files were damaged exactly this way once.

### 2. Run the pattern scan

`references/structural-patterns.md`. The shapes that survive model updates, each with a bad
example and the rewrite. Highest-yield, by corpus frequency:

- **Negative contrast.** "It's not X, it's Y". The most model-characteristic sentence shape.
  State Y.
- **Participial pseudo-analysis.** Trailing `-ing` clauses that pretend to interpret:
  "highlighting the importance of", "underscoring the shift".
- **Significance inflation.** "stands as a testament", "marks a pivotal moment". State the fact.
- **Copula avoidance.** "serves as", "represents" where "is" is clearer.
- **Throat-clearing and faux-insight openers.** "Here's the thing", "What most people get wrong".
- **Summary-recap endings.** "In conclusion", or a final paragraph restating the piece.
- **Fake-profound kickers.** The closing aphorism. Delete it, do not improve it.

### 3. Run the vocabulary scan

`references/banned-vocabulary.md`. Tier 1 replaces on sight. Tier 2 flags only when 2+ appear in
one paragraph. Tier 3 is context-dependent and often legitimate.

**When you remove a flagged word, rewrite the sentence.** Swapping in a synonym leaves the
machine sentence intact with different paint.

### 4. Run the formatting scan

`references/formatting-tells.md`. Emoji headings, bold mid-sentence, the numbered-bold-colon
list shape, bullets where prose reads better, smart quotes pasted from a chat window, leftover
placeholders and citation markup.

### 5. Apply the portability test

Swap the company, person, product, and country. If the sentence survives unchanged, it is
filler. Replace it with a fact, mechanism, number, consequence, or judgment specific to this
subject, or cut it.

Highest-leverage single test in the skill. Most slop is not badly written. It is *unattached to
anything*.

### 6. Put the person back

**The half everyone skips.** After Steps 1 to 5 the draft is clean and often dead. Steps 1 to 5
are subtraction; this is the only step that adds. A draft that has been through subtraction
alone is not finished, it is bleached.

**Read `references/preserving-voice.md` before doing this step.** It catalogues the eight things
an editing pass reliably destroys, with verbatim examples of what is at stake. The short version:
an AI pass optimises for clarity, confidence, and inoffensiveness, while distinctive writing
depends on timing, admitted uncertainty, and calculated risk. Those are in direct tension, and
the pass will resolve the tension the wrong way unless you stop it.

The eight, as a checklist against your own diff: pacing fragments · self-undermining hedges ·
digressive parentheticals · named people in vulnerable disclosures · deliberate repetition ·
unresolved endings · one-off register breaks · self-deprecation that is actually a claim.

For each one you removed, answer: **was this an error, or was this the person?** If you cannot
tell, leave it in and flag it.

Work from what the source supports. Never invent an anecdote, statistic, or opinion the author
did not have.

- **Restore the specific.** Where you cut a vague claim, ask the author for the real number
  rather than leaving a hole. A gap is better than a lie, but the fact is better than both.
- **Vary rhythm on meaning.** Mix 4-to-10-word sentences with 25-to-36-word ones, driven by what
  each sentence does, not by a target statistic. Forced fragments between long sentences are
  their own tell.
- **Let paragraphs be uneven.** Some one sentence, some six. Important sections get space,
  standard sections compress, empty sections get deleted.
- **Keep contractions.**
- **Keep the edge.** Strong opinions, blunt language, humour, profanity, self-interruptions, and
  honest admissions, where they belong to the author.
- **Keep the admissions.** "I got this wrong for a year", "I still don't fully understand why".
  These are the least fakeable thing in writing and the first thing an AI pass deletes.
- **Keep the digressions** that serve the voice even when they do not serve the argument.
- **Let sections end without a bow.** Not everything needs a closing line.
- **Repeat the plain word** rather than rotating synonyms.
- **Take the position.** If the draft surveys options and closes by noting what the analysis
  "raises", say which one you would pick. If the author's view is unclear, ask.

`references/worked-examples.md` shows this end to end, including a case where the correct output
is "leave it alone".

### 7. Self-check before output

Re-run the mechanical scan on your own output. Then read it aloud, because AI rhythm is audible
where it is invisible on screen.

Final question: **would the author recognise this as their own writing?** Cleaner but no longer
theirs means you over-corrected. Go back to Step 6.

## Hard rules

- Never change what is claimed. Only how it is said.
- Never invent a fact, statistic, source, quote, or opinion to replace a vague one. Flag it.
- Never soften or inflate a claim. "Around 40%" stays "around 40%". "I think it might work"
  stays a maybe. Deleting an honest hedge to sound authoritative is a lie about confidence.
- Never output a verdict on whether a human or a model wrote something.
- Never replace an em dash with a hyphen. Use a period, comma, or parentheses, chosen per clause.
- Never restructure an argument on a light or medium dose.
- Cutting must be proportional to the actual slop.

## Output format

**Improve mode**

```
[full edited draft]

## What changed
Dose: [light / medium / heavy]
- [pattern removed], N instances
- [structural change], and why
## Left alone deliberately
- [voice trait], and why it stays
## Needs you
- [any claim I cut or flagged that needs a real number or source]
```

**Audit mode**

```
## Patterns found
1. [Pattern name] · "quoted line" → fix in a few words
## Mechanical scan
[checks that failed, with counts]
## Not flagged
[voice traits that look deliberate and should be protected]
```

## Done =

The writing is better, the author would still recognise it as theirs, every rule-triggered
pattern is either fixed or consciously kept with a stated reason, and anything that needed a
real fact is flagged rather than invented.
