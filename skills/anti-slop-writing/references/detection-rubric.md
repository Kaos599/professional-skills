# Detection rubric

Countable checks and how to weigh them. Run these before making judgment calls, so the audit
rests on something the author can verify rather than on your impression.

## The cluster rule

**Never report a single occurrence as evidence.** One em dash means nothing. One rule-of-three
means nothing. Real human writing trips individual checks constantly.

Score by co-occurrence:

| Distinct pattern families present | Reading |
|---|---|
| 0 to 1 | Clean. Do not flag. |
| 2 to 3 | Worth a light pass. Mention, do not alarm. |
| 4 to 6 | Machine-assisted shape. Recommend a de-slop pass. |
| 7+ | Fully generated shape. Recommend the highest justified pass; heavy stays opt-in. In AUDIT mode, report this as a recommendation only. |

The bands calibrate edits, or recommendations when no edit is being made. They are never an
authorship verdict; the hard rule against verdicts stands at every band.

"Pattern families" is a closed set of exactly seven:

1. **sentence-level** - copula avoidance, false agency, negative contrast, participial tacks, and their kin in `structural-patterns.md`
2. **paragraph-level** - openers, uniformity, recap endings, rule-of-three, phrase repetition, false ranges
3. **rhythm** - sentence-length spread, same-length runs, transition cadence
4. **content-level** - abstraction, unsourced authority, portability failures
5. **vocabulary** - any tier of `banned-vocabulary.md`, including agent jargon
6. **formatting** - dashes, emoji headings, paste-tells, everything in `formatting-tells.md`
7. **code-layer** - findings from `code-slop.md`

Six instances of the same tell is one family, not six. Mechanical checks map to families like
this: em dashes to formatting; sigma, runs, opener repetition, and paragraph-opening transitions
to rhythm; rule-of-three, paragraph uniformity, and phrase repetition to paragraph-level;
passive concentration to sentence-level; formal transitions, hedging density, and both vocabulary
tiers to vocabulary; unsourced authority to content-level. The scanner implements six of these;
the code layer and the judgment calls stay with you.

## Mechanical checks

Thresholds collected from the corpus. They are heuristics, not measurements validated here.

| Check | How to measure | Flag threshold |
|---|---|---|
| Em dash density | count ÷ words | > 1 per 500 words, or any cluster |
| Sentence-length σ | std dev of word counts, 100-sentence window | < 4 |
| Same-length runs | consecutive sentences within 5 words | 3+ in a row |
| Sentence openers | share starting The / This / It / In, per paragraph | > 50% |
| Formal transitions | however, furthermore, moreover, additionally, consequently, therefore, nevertheless, thus | > 8 per 1,000 words |
| Paragraph-opening transitions | share of paragraphs opening with a connective | > 50% |
| Hedging density | arguably, tend to, generally, seem, appear, may (filler sense only; permission "you may export" is a manual call), typically, often, potentially ÷ total words | > 5% |
| Passive voice | sentences containing a passive construction ÷ total sentences | > 30% with no register reason |
| Rule-of-three | triads of exactly three; see the unified firing condition in Measurement conventions | 2+ triads, or any near-synonym triad |
| Paragraph uniformity | most paragraphs within ±1 sentence of each other | flag |
| Phrase repetition | any phrase repeated within 500 words | flag |
| Specificity floor | paragraphs with no number, name, date, or measurable quantity | any paragraph describing a practice, cost, or claim |
| Unsourced authority | "experts agree" / "studies show" / "research suggests" with no name | any |
| Tier 1 vocabulary | see `banned-vocabulary.md` | any |
| Tier 2 vocabulary | see `banned-vocabulary.md` | 2+ in one paragraph |

Two measurement notes the table cannot carry:

- **Sentence-length sigma needs volume.** Under roughly 30 sentences the statistic is noise.
  On short texts use the same-length-runs check instead and skip sigma entirely.
- **Passive voice has a repair path, not just a threshold.** When flagged, name the actor:
  "queries are validated" → "the compiler validates queries". Passive is correct when the actor
  is unknown or irrelevant, and it is standard register in scientific and experimental writing.
  The check flags concentration, not existence.

## Measurement conventions

Pin these before counting, or two honest readers get different numbers from the same text:

- **Sigma window.** At 150 sentences or fewer, compute over the whole text. Above that,
  compute over the worst contiguous 100-sentence window and say which you used.
- **Dash allowance.** `floor(words / 500)` dashes permitted in long-form genres, minimum zero.
- **Phrase repetition.** A phrase means three or more consecutive words. It repeats when the
  next occurrence starts within 500 words of where the first ended.
- **Tier 2 clustering counts distinct terms**, not token frequency; two "just"s is one term
  twice, not a cluster of two.
- **Rule of three fires on two or more triads in a piece, or on any single triad of true
  near-synonyms** (same grammatical role, substitutable in context). A triad of distinct
  referents - "metrics, logs, and traces" - never counts.
- **Markdown units.** A paragraph is a blank-line-delimited block, excluding code fences and
  tables. List items count as separate paragraphs for opener and uniformity checks, and as
  part of their parent block for clustering checks. An abbreviation ending in a single capital
  letter does not terminate a sentence.
- **Paragraph-opening connectives** are: however, furthermore, moreover, additionally,
  consequently, therefore, nevertheless, thus, overall, ultimately, that said. Plain
  coordinating openers ("So,", "But,", "And,") are human texture, not transitions; they never
  count.
- **Scan scope.** Exclude quoted examples, blockquotes presented as exhibits, and code fences
  from every count. If a protected region contains live slop, say so under `Not flagged` with
  the reason.

## Qualitative checks

Not countable, but decisive.

- **Portability test.** Swap company, person, product, country. Does the sentence survive? If
  yes, it is filler.
- **Read-aloud test.** AI rhythm is audible where it is invisible on screen. Read the whole
  piece out loud. Anything that would sound wrong said to a colleague gets rewritten.
- **So-what test.** Read each claim and literally ask "so what?" If there is no answer, cut it.
- **Position test.** Does the piece take a position, or does it summarise positions and close
  by observing what the analysis "raises"? The second is the generated default.
- **Curiosity test.** Does the writing wonder about anything, or does it only assert?
- **Recognition test.** Would the author recognise this as their own writing?

## Human-ness signals (presence is positive evidence)

Their absence is not proof of anything, but their presence is hard to fake:

- Unexpected specificity: "the meeting ran 47 minutes", not "about an hour"
- Self-corrections mid-sentence: "the system is fast, well, fast enough"
- Parenthetical asides that are genuinely tangential
- Admissions of uncertainty or mixed feelings
- Strong opinion stated without hedging
- Original analogies rather than stock comparisons
- Sensory or physical detail
- Typos, informal register, profanity where it fits the author
- Digressions that do not serve the argument but do serve the voice
- Paragraphs that end without a conclusion

Unnaturally clean writing with no typos, no informality, no opinion, and no edge is itself
a signal.

## Perplexity and detector tools

Some corpus skills quote perplexity figures (median AI ~21, median human ~36) and reference
commercial detectors. **Do not rely on these and do not report a probability that a human or
model wrote something.** Detectors guess and are wrong in both directions, most damagingly
against non-native English writers. Named patterns are evidence the author can check
themselves. A probability is not.

## Self-check before shipping a de-slop edit

Run every mechanical check on your own output, then confirm:

- [ ] The core claim is unchanged
- [ ] No fact, statistic, source, quote, or opinion was invented
- [ ] No claim was inflated or softened
- [ ] Sentence-length variance is genuine, not forced fragments
- [ ] The author's protected voice traits from step 0 are still present
- [ ] Cutting was proportional to the actual slop
- [ ] It reads aloud like a person
