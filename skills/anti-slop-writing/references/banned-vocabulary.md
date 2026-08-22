# Banned vocabulary, tiered by corpus consensus

`[n]` = how many of 100 harvested writing skills ban this term **in a ban context**
(the term appears within ~300 characters of avoid / never / cut / banned / replace / remove).
Method in `corpus-evidence.md`.

**Read the caveat first.** Current frontier models have largely dropped Tier 1 vocabulary.
Absence of these words is not evidence of human authorship. Vocabulary is the *weakest*
of the three signal classes. Structure is stronger. Clusters are stronger still.

---

## Tier 1: replace on sight

Banned by a large share of the corpus. Almost never the clearest available word.

| Word | [n] | Use instead |
|---|---|---|
| delve | 25 | look at, dig into, examine |
| leverage (as verb) | 23 | use |
| robust | 23 | name the property: fast, tested, handles N |
| seamless | 20 | say what has no friction, or cut |
| cutting-edge | 19 | state the version, date, or benchmark |
| tapestry | 18 | cut entirely |
| pivotal | 18 | state what changed |
| utilize | 17 | use |
| foster | 16 | cause, help, cultivate |
| facilitate | 15 | help, run, enable |
| realm | 14 | field, area, or cut |
| intricate | 14 | complicated, or name the complication |
| unlock | 13 | state the actual outcome |
| testament (to) | 12 | state the fact |
| navigate (figurative) | 12 | fine for UI/wayfinding; cut elsewhere |
| vibrant | 11 | cut |
| underscore / underscores | 11 | shows, or cut |
| boasts | 11 | has |
| transformative | 10 | state the before and after |
| revolutionary | 10 | state what is new |
| groundbreaking | 10 | state what is new |
| synergy | 9 | cut |
| streamline | 9 | name what got shorter |
| embark | 9 | start |
| paramount | 8 | most important, or cut |
| multifaceted | 8 | cut |
| holistic | 8 | cut |
| empower | 8 | let, allow |
| supercharge · elevate · ever-evolving · game-changer · beacon · meticulous | — | cut |

The last row carries no count because these terms sit below the corpus threshold but are
retained anyway: they are emitted by current models at rates the harvest predates. Treat the
dash as "unverified", not "rare". (`harness` moved to the agent-jargon block below; it is a
legitimate literal word that only goes bad as metaphor.)

**Copula avoidance.** Restore plain `is` and `has` - judged per clause, never blind-swapped,
since `represents` and `marks` are sometimes the accurate verb:
`serves as` [12] · `stands as` [10] · `represents` · `marks` · `features` (meaning has) ·
`offers` (meaning has) · `holds the distinction of` · `functions as` · `ventured into`

**Verbal false limbs.** Replace with one verb:
`has the ability to` [8] → can · `make a decision` → decide · `make an application` → apply ·
`give consideration to` → consider · `provide assistance` → help · `make contact with` → call ·
`exhibit a tendency to` → tend to · `has the potential to` → can

---

## Tier 2: flag when 2+ appear in one paragraph

Legitimate in isolation. A cluster is the tell.

**Filler adverbs and intensifiers**
just [55] · actually [33] · clearly [24] · very [21] · really [14] · simply [12] ·
significantly [12] · perhaps [9] · fundamentally [9] · basically [8] · truly · literally ·
essentially · importantly · crucially · inherently · absolutely · extremely · incredibly

Keep any of these when it carries genuine emphasis, uncertainty, contrast, or the author's
spoken rhythm. Cut when it adds nothing. "Just" is the most-banned single token in the corpus
and also the most over-corrected. Do not strip it mechanically.

**Formal connectives.** Replace with the plain one:
moreover [16] → also · however [16] → but · furthermore [15] → also ·
additionally [13] → also · overall [9] → cut · ultimately [8] → cut ·
consequently → so · nonetheless → still · thus / hence → so · that said [5] → but

Often the right fix is **no connector at all**. Start the next thought.

**Puffery adjectives**
comprehensive [28] · crucial [16] · innovative [13] · vital [8] · compelling · profound ·
enduring · indispensable · invaluable · quintessential · state-of-the-art [6] ·
best-in-class [6] · world-class [7] · next-generation · first-of-its-kind

**Abstract nouns used figuratively**
landscape [27] · narrative [23] · journey [20] · insights [18] · paradigm [11] ·
ecosystem · mosaic · fabric (of society) · cornerstone · pillar · catalyst

**Hedging adverbs.** The corpus reports these at inflated rates in model output:
typically · often · sometimes · potentially · usually · arguably · generally ·
tend to · may · seem to · appear to

**Padding verbs used as filler.** Say what the thing does:
ensuring / ensures · highlights · supports · reflects · showcases · emphasizes ·
demonstrates · illustrates (when used as a trailing gesture rather than a real verb)

**Agent-culture jargon.** The metaphor register coding assistants emit about themselves. These
are newer than most of the corpus, which is why the counts are missing; they are the "next
tapestry" predicted by the staleness caveat at the top of this file. **Flag any figurative use
on sight; the Tier 2 two-per-paragraph rule does not apply to this block.** Scope each ban to
figurative use with the qualifier shown. Literal technical uses stay legal:

- substrate → base, stack, or name the layer [as metaphor]
- primitive (as a noun for "a basic thing") → building block, operation, or name it
- vector (metaphorical: of change, of attack) → direction, way, route; keep the math/graphics sense
- scaffolding (as metaphor) → structure, skeleton, or cut
- harness (as metaphor for "a framework") → framework or setup; keep the literal test-harness sense
- modality (for "kind of data") → data type, format; keep the ML term of art in ML contexts
- orchestrate / conductor metaphors → run, coordinate, schedule
- gold-plating (figurative) → more than the job needs
- nexus (figurative) → hub, link, or cut
- surface ("API surface" is fine; "on the writing surface of the problem" is not)

---

## Tier 3: context-dependent

Do not flag automatically. Flag only if the surrounding text is already scoring high.

dive / deep dive [22] · actionable [13] · align / alignment [10] · optimize · scalable ·
curated · bespoke · nuanced · resonate · unparalleled

---

## Banned phrases

`[n]` = ban-context document frequency out of 100.

**Openers**
- in today's fast-paced world / digital age / era [12]
- in the realm of [7]
- in the world of · in an era of
- at its core [8]
- here's the thing [9]
- let's dive in / let's delve into [10]
- in this article / in this post [8]
- without further ado · buckle up
- picture this: · imagine a world where · what if I told you
- most people think X. The reality is Y.
- unpopular opinion:

**Mid-text filler**
- it's worth noting (that) [14]
- it's important to note (that) [12]
- when it comes to [10]
- in order to [20] → to
- due to the fact that [12] → because
- at this point in time [10] → now
- in terms of · with regard to · in the context of
- needless to say · it should be noted that · one could argue that
- at the end of the day [14]
- the reality is · the truth is · the bottom line is
- this begs the question
- from X to Y (false-range opener; only a tell when X and Y are not on a meaningful scale —
  "from onboarding to payroll" inside an HR piece is real breadth, "everything from billing to
  developer joy" is inflation. Full pattern card in `structural-patterns.md`.)
- whether you're a [X] or a [Y] (false-breadth audience segmenting)

**Unsourced authority.** Name the source or delete the claim:
experts agree [6] · studies show [7] · research shows [5] · industry reports suggest ·
many argue · widely regarded as · observers note · it is generally accepted ·
several sources · some critics argue

**Closers**
- in conclusion [17] · in summary [5] · to sum up · overall · ultimately
- the future looks bright · exciting times lie ahead
- I hope this helps · let me know if you have any questions · feel free to reach out

**Chat artifacts.** Canonical list lives in `formatting-tells.md` under paste-tells; both files
treat these identically: strip on sight, no judgment call. The short version:
Great question! · I hope this helps! · You're absolutely right! · Certainly! ·
While specific details are limited · [insert X here] · `oaicite` · `turn0search0`

**Corporate idiom**
move the needle · low-hanging fruit · boil the ocean · circle back · touch base ·
north star · paradigm shift [5] · smoking gun · perfect storm · double-edged sword ·
tip of the iceberg · take it to the next level · game changer

---

## Reported frequency multipliers

Sourced from individual skills in the corpus that cite their own corpus studies. **Not
independently verified here.** Treat as directional, not as measurements.

- `ensuring`: reported 4.3x overrepresented vs human text, and described as the strongest
  single word tell of 2026
- `provide a valuable insight`: reported 468x
- `left an indelible mark`: reported 317x
- `play a significant role in shaping`: reported 207x. One skill calls
  "plays a [crucial/critical/important] role in shaping" the top trigram of 2026.
- `open a new avenue`: reported 174x
- `gain a comprehensive understanding`: reported 120x
- `comprehensive` 24.5x · `nuanced` 17x · `fundamentally` 17x · `paradigm` 15.1x ·
  `typically` 9.6x · `often` 4.9x
