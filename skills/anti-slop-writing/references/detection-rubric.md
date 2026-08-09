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
| 4 to 6 | Reads as machine-assisted. Recommend a de-slop pass. |
| 7+ | Reads as machine-written. |

"Pattern families" means the categories in `structural-patterns.md` (sentence-level,
paragraph-level, rhythm, content-level) plus vocabulary and formatting. Six instances of the
same tell is one family, not six.

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
| Hedging density | arguably, tend to, generally, seem, appear, may, typically, often, potentially ÷ total words | > 5% |
| Passive voice | passive constructions ÷ sentences | > 30% |
| Rule-of-three | lists of exactly three, especially near-synonyms | any, if repeated |
| Paragraph uniformity | most paragraphs within ±1 sentence of each other | flag |
| Phrase repetition | any phrase repeated within 500 words | flag |
| Specificity floor | paragraphs with no number, name, date, or measurable quantity | any paragraph describing a practice, cost, or claim |
| Unsourced authority | "experts agree" / "studies show" / "research suggests" with no name | any |
| Tier 1 vocabulary | see `banned-vocabulary.md` | any |
| Tier 2 vocabulary | see `banned-vocabulary.md` | 2+ in one paragraph |

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
