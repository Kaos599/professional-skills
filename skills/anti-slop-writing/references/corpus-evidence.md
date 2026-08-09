# Corpus evidence and method

Everything in this skill is derived from published agent skills, not from intuition. This file
records how the corpus was built and what the counts actually mean, so the claims can be
checked or re-run.

## Method

**Discovery.** The skills.sh REST API requires a Vercel OIDC token, but the public
`npx skills find <query>` CLI is unauthenticated. Twenty queries were run:

```
ai slop · anti slop writing · humanize writing · writing style · technical writing ·
copywriting · content writing · editing prose · linkedin post · social content ·
brand voice · ghostwriting · storytelling · newsletter writing · blog post writing ·
essay writing · writing clearly · plain english · detect ai text · em dash
```

That produced 392 distinct skills. These were split into two buckets by slug pattern
(anti-slop/humanize/detect vs writing-craft), ranked by install count, and the top of each
bucket was downloaded.

**Retrieval.** `npx skills use <owner/repo@skill>` prints the full SKILL.md and downloads
supporting files to a temp directory. Both were captured. This matters: the skills.sh web pages
truncate SKILL.md, and the meaty content (banned-word lists, rubrics) usually lives in
`references/` files rather than in SKILL.md itself.

**Corpus.** 100 skill documents, ~387,000 words.
45 anti-slop / humanizing, 55 writing craft.

**Analysis.** Two passes.

1. *Ban-context document frequency.* For each candidate term, count how many of the 100
   documents mention it within ~300 characters of a ban trigger (avoid, never, banned,
   forbidden, cut, remove, replace, do not use, red flag). This separates "the skill bans this
   word" from "the skill happens to use this word in its own prose". Raw frequency conflates
   the two and badly overstates common words.
2. *Rule-line extraction.* Bullet lines under headings matching ban/pattern/rubric/structure
   topics were extracted and deduplicated, yielding 4,137 distinct rule statements
   (2,164 slop, 1,990 craft), which were then read and clustered by hand.

**Note on dedup.** Exact-string deduplication collapsed almost nothing. Only 13 lines appeared
verbatim in 3+ documents out of 4,137. The same rule is phrased 94 different ways across the
corpus. All consensus counts below are therefore term-level, not sentence-level.

## Structural consensus

How many of 100 skills address each topic at all. This is the clearest signal in the dataset,
and it is why this skill weights structure above vocabulary.

| Topic | Skills addressing it |
|---|---|
| Em dash handling | 84 |
| Abstraction vs specificity | 71 |
| Sentence/paragraph uniformity (burstiness) | 43 |
| Hedging and qualifiers | 42 |
| Emoji in headings and bullets | 32 |
| Summary-recap endings | 25 |
| Passive voice | 21 |
| "Not X but Y" negative contrast | 21 |
| Unsourced authority | 19 |
| Rule of three | 18 |
| Throat-clearing openers | 16 |
| Rhetorical question openers | 16 |
| Sentence case vs title case | 15 |
| Perplexity / detector scoring | 12 |
| Participial `-ing` pseudo-analysis | 12 |
| Synonym cycling | 11 |
| Bold mid-sentence emphasis | 11 |
| Fake-profound kickers | 8 |
| Portability test | 2 |

Two observations worth carrying forward:

- The two highest-consensus items are not word bans. Em dash handling and the
  abstraction/specificity axis are what the field actually agrees on.
- The **portability test appears in only 2 of 100 skills** despite being, on inspection, the
  single most transferable diagnostic in the whole corpus. Rarity is not a proxy for value.
  It is promoted to a first-class step in this skill.

## Vocabulary consensus

Ban-context document frequency, out of 100. Full tiered list in `banned-vocabulary.md`.

**Words:** just 55 · actually 33 · comprehensive 28 · landscape 27 · delve 25 · clearly 24 ·
robust 23 · narrative 23 · leverage 23 · dive 22 · very 21 · seamless 20 · journey 20 ·
cutting-edge 19 · tapestry 18 · pivotal 18 · insights 18 · utilize 17 · moreover 16 ·
however 16 · foster 16 · crucial 16 · furthermore 15 · facilitate 15 · realm 14 · really 14 ·
intricate 14 · unlock 13 · innovative 13 · additionally 13 · actionable 13 · testament 12 ·
simply 12 · significantly 12 · navigate 12 · highlighting 12 · vibrant 11 · underscore 11 ·
paradigm 11 · boasts 11 · transformative 10 · revolutionary 10 · groundbreaking 10 · align 10 ·
synergy 9 · streamline 9 · perhaps 9 · overall 9 · fundamentally 9 · embark 9 · vital 8 ·
ultimately 8 · paramount 8 · multifaceted 8 · holistic 8 · empower 8 · basically 8

**Phrases:** not just 29 · in order to 20 · in conclusion 17 · not only 15 ·
it's worth noting 14 · at the end of the day 14 · serves as 12 · it's important to note 12 ·
in today's fast-paced 12 · due to the fact that 12 · when it comes to 10 · stands as 10 ·
let's dive in 10 · at this point in time 10 · here's the thing 9 · in this article 8 ·
has the ability to 8 · at its core 8 · world-class 7 · studies show 7 · in the realm of 7 ·
state-of-the-art 6 · experts agree 6 · best-in-class 6 · that said 5 · research shows 5 ·
paradigm shift 5 · in summary 5 · ever-evolving landscape 5 · deep dive 5

## Where the corpus disagrees

Recorded because a skill that hides its disagreements is less useful than one that states them.

**Em dashes.** Strict skills ban them outright as a major tell. Moderate skills allow 1 to 2 in
a long piece when they clearly beat other punctuation. At least one skill explicitly cites a
published rebuttal arguing the em dash signal is overstated. *Resolution used here:* zero under
500 words, at most one per 500 words above that, never clustered.

**Filler adverbs.** Some skills ban `just`, `actually`, `simply` outright. Others insist on
keeping them where they carry emphasis, uncertainty, or the author's spoken rhythm. *Resolution:*
Tier 2, flagged only in clusters. `just` is both the most-banned token in the corpus and the
most over-corrected.

**Front-loading.** Some skills mandate thesis-first in every paragraph and section. Others warn
that forcing every unit into the same point-detail-background shape is itself a tell.
*Resolution:* front-load when it improves clarity, not as a rule.

**Fragments and short sentences.** Some skills prescribe short punchy sentences for impact.
Others flag "dramatic fragmentation" and stacked one-liners as slop. *Resolution:* vary based
on meaning, never to hit a variance statistic. Forced burstiness is its own tell.

**Rhetorical questions.** Banned outright by some, allowed as an author-voice trait by others.
*Resolution:* banned as an opener, allowed sparingly mid-text.

**Detector scores.** 12 skills quote perplexity numbers or integrate commercial detection APIs.
Others explicitly refuse to output a probability. *Resolution:* never output an
AI-vs-human verdict. Detectors guess, and they are most wrong against non-native English
writers. Named patterns are checkable; a probability is not.

## Reliability

- Ban-context counts are mechanical and reproducible from the corpus.
- The frequency multipliers quoted in `banned-vocabulary.md` (`ensuring` at 4.3x,
  `provide a valuable insight` at 468x, and so on) are **claims made by individual skills about
  their own corpus studies**. They were not independently verified. Treat as directional.
- Threshold numbers in `detection-rubric.md` are collected from the corpus, not validated here.
- Install counts skew the sample toward popular skills, which skews toward word-list approaches
  because those are easy to write and easy to demo. The structural material is drawn from a
  smaller, generally higher-quality subset.

## Principal sources

Highest-signal skills in the anti-slop bucket, by install count at harvest:
`humanizerai/agent-skills@humanize` · `petergyang/no-ai-slop@no-ai-slop` ·
`yetone/kill-ai-slop@kill-ai-slop` · `obra/the-elements-of-style@writing-clearly-and-concisely` ·
`jpeggdev/humanize-writing@humanize-writing` · `neolabhq/context-engineering-kit@write-concisely` ·
`yeachan-heo/oh-my-claudecode@ai-slop-cleaner` · `rand/cc-polymath@anti-slop` ·
`realrossmanngroup/no_ai_slop_writing_rules@no-ai-slop` ·
`jalaalrd/anti-ai-slop-writing@anti-ai-slop-writing` · `athola/claude-night-market@slop-detector` ·
`charlesroper/skills@on-writing-well` · `nicepkg/ai-workflow@ai-slop-detector`

To re-run the harvest, repeat the discovery and retrieval steps above. The corpus will drift as
skills are published and models change, which is the point of recording the method rather than
only the conclusions.
