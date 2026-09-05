---
name: anti-slop-writing
description: Make writing sound like a person wrote it. Rewrites drafts that read as machine-generated, restores voice that AI editing flattened, and audits text for AI tells when asked. Use when a draft feels generic or corporate, when asked to de-slop or humanize text, when polishing anything an LLM helped write, before publishing a post or doc, or when someone asks whether writing "sounds like AI". Do not use it to adjudicate authorship disputes: this skill names patterns and never outputs an AI-vs-human verdict.
---

# Anti-Slop Writing

Make the writing better and make it sound like a person. Removing tells is the means, not the end.

Distilled from 45 published anti-slop and humanizing skills. Harvest method and hard counts in
`references/corpus-evidence.md`.

**Prefer clean drafting to cleanup.** When you are also the author, apply these rules while
writing rather than running a repair pass afterwards. A post-hoc pass recovers less than not
generating the tells in the first place; this skill exists for text that already exists.

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
3. **The failure mode is over-correction, in three forms (The Three Ditches).**
   - *Ditch 1 — Bleaching:* running the subtraction (Steps 1-5) and skipping Step 6 leaves flat,
     cautious, personality-free prose. This is the one this skill is most likely to cause.
     Deleting is easy; the hard half is Step 6.
   - *Ditch 2 — Academic whitepaper slop:* over-correcting into a detached, passive, third-person
     clinical register or royal "we" that reads like a committee report.
   - *Ditch 3 — Performed incompetence:* confusing human voice with self-deprecation, confusion,
     or beginner apologies. If the author is a senior engineer who builds production systems, do
     NOT strip their authority or force faux-modesty. But a senior engineer's *earned, specific*
     admissions of uncertainty are voice, not incompetence - see the test in
     `references/preserving-voice.md` before touching them.
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
Cluster bands calibrate your recommendation in this mode; they never authorize an edit.

A follow-up pass after an audit starts over at Step 0 with a fresh baseline and dose decision;
do not carry state across modes.

**RESTORE.** A specific and common case: the draft was *already* edited by an AI and came back
flattened. The tells are mostly gone but so is the person. Work from whatever earlier draft or
sample of the author's writing you can get.

RESTORE runs Steps 0, 6, and 7. During Step 0, check what the polish pass left behind: any Tier
1 word, banned phrase, paste-tell, or failing mechanical check gets its minimal fix from the
relevant step first. Paste-tells are stripped in every mode without a judgment call. Dose here
describes how far Step 6 reaches: light restores flagged losses only; medium also rebuilds
rhythm and specificity from what the author had.

If no earlier draft or writing sample exists at all, do not invent a personality. Mine the
current draft for its core point and any opinion it contains, restore those, and cap the pass
at medium. On this path skip the eight-trait diff walk in Step 6, because nothing was
subtracted; instead check every restored addition against the mined core point.

## Dose

Decide before editing. State which you chose in the output.

| Dose | When | What you touch |
|---|---|---|
| **Light** | strong draft, a few tells | named patterns only, nothing else |
| **Medium** | default | patterns, rhythm, and specificity |
| **Heavy** | reads as fully generated, author agrees | structure and argument order too |

**Heavy is opt-in.** Never restructure someone's argument because it would be tidier. Ask the
author before running heavy. If the draft needs a heavy pass and you were not asked for one, do
a medium pass and say what a heavy one would change as a `Heavy plan` bullet under
`Left alone deliberately`.

If the author authorizes heavy after editing began, finish the current dose first, then run
heavy as a second pass on the edited draft. State both doses in `What changed`:
`Dose: medium, then heavy on request`. Never restart from the original draft; re-running
subtraction over already-cut text manufactures the over-correction this skill fears.

If the draft is already good, **say so and stop.** "Two minor things, otherwise this reads fine"
is a complete and correct output. Manufacturing findings to look useful is its own failure.

## Genre calibration

The rules below are not uniform across formats. Set this in Step 0.

| Format | Em dashes | Contractions | Fragments | Structure |
|---|---|---|---|---|
| Social post | zero under 500w | yes | yes | loose |
| Outreach, cold email | zero | yes | yes | no headings, one ask |
| Blog, essay | ≤1 per 500w | yes | sparingly | headings ok |
| Launch post, release notes | ≤1 per 500w | yes | sparingly | callouts and taglines allowed; comparative claims still need numbers |
| Technical docs | ≤1 per 500w | yes | no | headings required |
| Resume, cover letter | zero | sparingly | verb-first fragments ok | no admissions injected; skip the Step 6 additions |
| Slide deck | zero | no | deck-native | bold and list conventions are the medium; formatting-tells layout bans do not apply |
| Commit message | zero | no | no | imperative subject, prose body |
| Legal, medical, formal | as house style | no | no | house style wins |

Precedence, highest first: **house style guide > supplied writing sample > genre table >
this skill's defaults.** A sample overrides every threshold in `references/detection-rubric.md`
except the hard rules; where a genre row conflicts with the Step 6 keep-lists (commit messages
and legal text take no contractions), the genre table wins. Mixed-format pieces take the
stricter dash cell and the looser structure cell.

## Out of scope, and what to say instead

- "Make this shorter." Length is not slop. Agree a target length and cut by argument, or
  decline; this skill's rules can lengthen a draft when specificity demands it.
- "Make it punchier for social." Hooks and kickers are the genre there. Apply the social-post
  row rather than the fake-profound-kicker ban.
- "Rewrite it in [named person]'s voice." Requires their writing samples. Without samples,
  decline rather than performing Generic Executive Tone.
- Slide decks and UI copy follow their genre rows above, not the blog defaults.

## Procedure

### 0. Establish the baseline

Step 0 runs in every mode, without exception; RESTORE sources its voice signals from the
earlier draft or sample instead of the current one.

Read the whole draft. Note internally, do not output:

- The core point in one sentence. If you cannot find it, ask rather than guessing.
- 3 to 5 **voice signals to protect**: vocabulary, cadence, bluntness, humour, digressions,
  admissions, profanity, level of polish.
- Author authority: Is the author an experienced practitioner? Protect their authority.
- Format, audience, and genre row from the table above.
- Dose.

If format, audience, or goal is unknown in any mode, ask the single combined question before
proceeding - who is this for, and what should they take away? - then redo these notes if the
answer changes the genre row or dose. Collect any further author questions as you work and ask
them once, batched, before editing begins.

Anything you cannot attribute to a rule below stays exactly as written. That is the default,
not a fallback.

### 1. Run the mechanical scan

Countable. Run before making judgment calls. The full 15-check list with thresholds and
reasoning lives in `references/detection-rubric.md` and is canonical; this table is the
working subset.

| Check | Flag when |
|---|---|
| Em dashes | above the genre budget, or any cluster |
| Sentence-length spread | standard deviation under 4 words per 100-sentence window; on shorter texts use the same-length-runs check instead |
| Consecutive same-length runs | 3+ sentences within 5 words of each other |
| Sentence-opener repetition | over half a paragraph's sentences start with The / This / It / In |
| Paragraph-opening transitions | over half the paragraphs open with a connective |
| Formal transitions | more than ~8 per 1,000 words |
| Hedging density | over ~5% of words |
| Passive constructions | over ~30% of sentences, and no register reason keeps them |
| Rule-of-three lists | any list of exactly three near-synonyms |
| Paragraph-length uniformity | most paragraphs within one sentence of each other |
| Phrase repetition | any phrase repeated within 500 words |
| Unsourced authority | "experts agree" / "studies show" with no name |
| Specificity floor | a paragraph describing a practice, cost, or claim with no number, name, date, or measurable quantity |

Scan scope: exclude quoted examples, blockquotes presented as exhibits, and code fences from
every count. If a protected region contains live slop, say so under `Not flagged` with the
reason. Measurement conventions - windows, units, thresholds - are pinned in
`references/detection-rubric.md`; follow them exactly so two readers get one answer.

Steps 1 to 5 are scans: record findings, fix nothing yet.

**Scan mechanically, never fix mechanically.** A find-and-replace across a draft produces
sentences that are grammatical and wrong, because the right substitute differs by clause. Fix
per occurrence. This skill's own reference files were damaged exactly this way once.

### 2. Run the pattern scan

`references/structural-patterns.md`. The shapes that survive model updates:

- **Negative contrast.** "It's not X, it's Y". The most model-characteristic sentence shape. State Y.
- **Participial pseudo-analysis.** Trailing `-ing` clauses that pretend to interpret: "highlighting the importance of", "underscoring the shift".
- **Significance inflation.** "stands as a testament", "marks a pivotal moment". State the fact.
- **Copula avoidance.** "serves as", "represents" where "is" is clearer.
- **Throat-clearing and faux-insight openers.** "Here's the thing", "What most people get wrong".
- **Downplaying others.** "Most developers do X, but I do Y", "unlike casual prompt toys". Cut the sneer. True authority is quiet; focus on domain constraints.
  The line to draw: contempt for people ("most developers use toys") is slop; correcting a factual misconception ("most people size GPUs by VRAM — that measures the wrong thing") is a legitimate hook.
- **Failure-framing in headings.** "Why X breaks down / fails". Reframe around domain constraints.
- **Jargon theater.** Reject aerospace/finance cosplay ("cockpit", "tranches", "accretion drift"). Use plain technical English ("dashboard", "clearing timeline Phase 1/Phase 2").
- **Summary-recap endings.** "In conclusion", or a final paragraph restating the piece.
- **Fake-profound kickers.** The closing aphorism. Delete it, do not improve it.

### 3. Run the vocabulary scan

`references/banned-vocabulary.md`. Tier 1 replaces on sight. Tier 2 flags only when 2+ appear in
one paragraph. Tier 3 is context-dependent and often legitimate. Tier 4 flags Jargon Theater on
sight (editorial policy tier, not corpus-derived - see that file's note).

**When you remove a flagged word, rewrite the sentence.** Swapping in a synonym leaves the
machine sentence intact with different paint.

### 4. Run the formatting scan

`references/formatting-tells.md`. Emoji headings, bold mid-sentence, the numbered-bold-colon
list shape, bullets where prose reads better, smart quotes pasted from a chat window, leftover
placeholders and citation markup.

If the draft contains fenced code, also run `references/code-slop.md` against the code layer
under the current dose: comment, name, and docstring fixes ride the vocabulary tier;
refactoring- and testing-tier work waits for an opted-in heavy pass and says so.

### 5. Apply the portability test

Swap the company, person, product, and country. If the sentence survives unchanged, it is
filler. Replace it with a fact, mechanism, number, consequence, or judgment specific to this
subject, or cut it.

Highest-leverage single test in the skill. Most slop is not badly written. It is *unattached to
anything*.

**Now apply the fixes, once, in priority order:** content-level failures first (portability,
abstraction, unsourced claims), then paragraph and sentence shapes, then vocabulary, then
formatting trivia. A pass that spends its effort on dashes while leaving filler sentences
untouched has its priorities inverted.

### 6. Put the person back

**The half everyone skips.** After the fixes the draft is clean and often dead. Steps 1 to 5
are subtraction; this is the only step that adds. A draft that has been through subtraction
alone is not finished, it is bleached.

**Read `references/preserving-voice.md` before doing this step.** It catalogues the eight things
an editing pass reliably destroys, and it defines the authority test that prevents the Third
Ditch (performed incompetence). The short version: an AI pass optimises for clarity, confidence,
and inoffensiveness, while distinctive writing depends on timing, admitted uncertainty, and
calculated risk.

Walk the eight items against your own diff: pacing fragments · self-undermining hedges ·
digressive parentheticals · named people in vulnerable disclosures · deliberate repetition ·
unresolved endings · one-off register breaks · self-deprecation that is actually a claim.

For each one you removed, answer: **was this an error, or was this the person?** If you cannot
tell, leave it in and flag it. Then apply the authority test: an admission that is **specific
and earned** (it names a mechanism, a number, or a concrete failed attempt) is voice and stays;
an admission that is **generic and undefended** (a vague mood with nothing attached) is slop and
goes. An incident narrative ("what broke") is never manufactured drama - it is the specificity
this skill requires.

Work from what the source supports. Never invent an anecdote, statistic, or opinion the author
did not have.

- **Restore the specific.** Where you cut a vague claim, ask the author for the real number
  rather than leaving a hole. A gap is better than a lie, but the fact is better than both.
- **Vary rhythm on meaning.** Mix 4-to-10-word sentences with 25-to-36-word ones, driven by what
  each sentence does, not by a target statistic. A 2-to-4-sentence paragraph is a reasonable
  default, but deliberately break it: some paragraphs run one sentence, some five or six.
  Uniform paragraph length is itself a flagged tell. Forced fragments between long sentences
  are their own tell.
- **Let paragraphs be uneven.** Some one sentence, some six. Important sections get space,
  standard sections compress, empty sections get deleted.
- **Keep contractions.**
- **Keep first-person ownership.** Where the author writes as an individual practitioner, keep
  confident first-person singular ("I built", "I architected"). Never substitute the detached
  academic third-person or the royal "we" for it - except where the register genuinely requires
  impersonal voice (scientific, legal, formal: the genre table wins).
- **Keep the edge.** Strong opinions, blunt language, humour, profanity, self-interruptions, and
  honest admissions, where they belong to the author.
- **Keep the admissions.** The specific, earned ones. These are the least fakeable thing in
  writing and the first thing an AI pass deletes.
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

Then answer the two integrity questions, in this order:

1. **What still sounds AI-generated?** Fix what you find.
2. **Did the rewrite add or remove any fact, name, number, date, quote, or claim?** Treat an
   unsupported addition and a silently lost claim as the same class of error. Restore or flag.

If a mechanical check still fails after one fix round, either run at most one more round or
report the residual in the output. Two rounds is the hard bound; do not loop silently, and do
not stop while a known failure is unmentioned.

Final question: **would the author recognise this as their own writing?** Cleaner but no longer
theirs means you over-corrected. Go back to Step 6.

## Hard rules

- Never change what is claimed. Only how it is said.
- Never rewrite quoted material, titles, or text being discussed rather than used. If a draft
  quotes slop as an example, the example stays slop.
- Never invent a fact, statistic, source, quote, or opinion to replace a vague one. Flag it.
- Never soften or inflate a claim. "Around 40%" stays "around 40%". "I think it might work"
  stays a maybe. Deleting an honest hedge to sound authoritative is a lie about confidence.
- Never output a verdict on whether a human or a model wrote something.
- Never downplay other developers or treat peers as inferior ("most developers use toys"). The
  ban targets contempt for people, not correction of misconceptions.
- Never frame headings around others "failing" or "breaking down"; frame around domain constraints.
- Never strip senior technical authority or replace confident first-person singular ("I built")
  with detached academic third-person ("the system was evaluated") or the royal "we", when the
  author writes as an individual practitioner. In scientific, legal, and formal registers the
  genre table wins.
- Never replace an em dash with a hyphen, en dash, or double hyphen. Swapping one dash glyph
  for another trades the tell instead of removing it. Use a period, comma, or parentheses,
  chosen per clause.
- Never restructure an argument on a light or medium dose.
- Cutting must be proportional to the actual slop.

## Output format

Two shapes come before the template:

- **Zero-change.** The scan finds nothing failing and the draft reads fine: return a short
  verdict, optional notes under `Needs you`, and the line `No edit made.` Never render template
  sections with nothing in them.
- **Husk draft.** If subtraction would remove more than half the draft, or every surviving
  sentence needs an author-supplied fact, do not ship the remains. Return the patterns found,
  the `Needs you` list, and stop. An emptied draft is not an edited one.

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
pattern is either fixed or consciously kept with a stated reason, anything that needed a real
fact is flagged rather than invented - or the scan came back clean and the correct output was
no edit at all.
