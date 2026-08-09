---
source:    https://danluu.com/percentile-latency/
author:    Dan Luu
authored:  false
format:    long-form analytical blog
added:     2026-08-09
notes:     |
  Argument-first writing with almost no formatting scaffolding. Copy the reasoning
  structure and the willingness to write long sentences. Do not copy the sparse
  formatting for docs or social.
---

## Why this one

The opposite pole from a company engineering blog. No bullets carrying the argument, minimal
headings, no code, no diagrams, and it is still one of the clearest things written about
latency. The argument does all the work.

## Measured signature

Computed over the post body, code blocks excluded:

| | |
|---|---|
| Words | 2,271 |
| Sentences | 96 |
| Mean sentence length | **22.3 words** (median 20) |
| Standard deviation | **12.5** |
| p10 / p90 | 8 / 38 words |
| Fragments under 8 words | 9.4% |
| Sentences over 30 words | **19.8%** |
| Em dashes | **0** |
| Semicolons | 9 |
| Question marks | 2 |
| Headings | 6 |

Note the combination: long average sentence, high variance, one fifth of sentences over 30
words, and zero em dashes. This writer builds long sentences with commas and semicolons rather
than reaching for a dash. That is a deliberate and copyable choice.

## Verbatim excerpts

**Opening:**

> Most real-world problems are big enough that you can't just head for the end goal, you have to
> break them down into smaller parts and set up intermediate goals. For that matter, most games
> are that way too. "Win" is too big a goal in chess, so you might have a subgoal like don't get
> forked.

**Closing:**

> Thanks to Leah Hanson for extensive comments on this, and to Scott Feeney and Kyle Littler for
> comments that resulted in minor edits.

## Signature

**Opening move: the analogy before the subject.** The post is about latency percentiles and
opens on goal decomposition and chess. The technical subject does not appear for several
paragraphs. This works because the analogy *is* the argument, not decoration. It is a high-risk
move: it fails badly when the analogy is ornamental.

**Structure by parallel case, not by topic.** The headings are three worked examples from three
unrelated fields (`IQ & Early Childhood Education`, `Cholesterol & Myocardial Infarction`,
`99%-ile Latency & Latency`) followed by `Conclusion`. The technical subject is the *third* case.
The argument is that proxy metrics fail the same way everywhere, and the structure enacts it
rather than asserting it.

**Long sentences, unapologetically.** Nearly 20% run over 30 words. Modern writing advice would
cut these. They earn their length by carrying a full argument with its qualification attached,
rather than splitting into a claim sentence plus a hedge sentence.

**Comma splices as voice.** "you can't just head for the end goal, you have to break them down"
is a comma splice. It is deliberate and it reads like speech.

**No formatting scaffolding.** No bold mid-sentence, no bulleted takeaways, no callout boxes.
Prose carries the argument because the argument is genuinely sequential, not a list.

**Closing: it just stops.** The last line is an acknowledgements sentence. There is no summary,
no forward look, no aphorism. The `Conclusion` heading exists, but the post does not end on a
flourish.

## What to copy

- Structure that enacts the argument instead of announcing it.
- Long sentences when the thought is genuinely long. High variance beats uniform shortness.
- Semicolons and commas instead of em dashes for building complex sentences.
- Ending without a bow.
- Naming the people who reviewed the draft.

## What not to copy

- The sparse formatting for reference docs, runbooks, or anything scanned rather than read.
- The analogy-first opening unless the analogy carries the argument. If it is decorative, it
  reads as throat-clearing.
- The 22-word mean for social posts.
