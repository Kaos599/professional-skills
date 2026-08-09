---
source:    https://tailscale.com/blog/how-nat-traversal-works
author:    Tailscale engineering
authored:  false
format:    long-form technical explainer
added:     2026-08-09
notes:     |
  The reference for the long explainer: 8,800 words that stay readable. Copy the
  layered-disclosure structure and the question-driven progression.
---

## Why this one

8,792 words on NAT traversal that people actually finish. The problem this exemplar solves is
length: how to write something long without it becoming a reference manual nobody reads.

## Measured signature

| | |
|---|---|
| Words | **8,792** |
| Sentences | 420 |
| Mean sentence length | 19.7 words (median 18) |
| Standard deviation | 10.9 |
| p10 / p90 | 8 / 33 words |
| Fragments under 8 words | 8.6% |
| Sentences over 30 words | 12.4% |
| Em dashes | 10 (**0.57 per 500 words**, inside budget) |
| Colons | 48 |
| Semicolons | 5 |
| **Question marks** | **28** |
| Headings | 5 |

The standout numbers: **28 questions across 420 sentences** (one every 15), and only **5
headings for 8,792 words** (one per ~1,760 words).

Both are unusual and both are load-bearing. The questions carry the progression, so the piece
does not need dense headings to stay navigable. Compare the Fly.io post: 9 headings for 2,890
words, one per ~320 words. Opposite strategy, both work, and the difference is the question rate.

## Verbatim excerpt

**Opening:**

> We covered a lot of ground in our post about How Tailscale Works. However, we glossed over how
> we can get through NATs (Network Address Translators) and connect your devices directly to
> each other, no matter what's standing between them. Let's talk about that now!

## Signature

**Opening move: name the thing you skipped last time.** It admits a gap in prior work and fills
it. This gives the piece a reason to exist that is not "here is a topic."

**Questions as the engine.** With one question every ~15 sentences, the reader is repeatedly
told what problem the next section solves before it solves it. This is what replaces headings.

**Progressive disclosure with an explicit escape hatch.** The heading `NAT notes for nerds`
quarantines the deep material so a reader who does not need it can skip cleanly. Signposting a
section as optional is more honest than burying depth or omitting it.

**Expansion on first use.** "NATs (Network Address Translators)" spelled out the first time. In
an 8,800-word piece with a wide audience, this is the difference between an explainer and a spec.

**Heading voice.** "Figuring out firewalls", "The nature of NATs", "Concluding our connectivity
chat" are alliterative and conversational. Same trick as Fly.io, different register.

**"Let's talk about that now!"** Conversational, exclamation mark, first-person plural. Sets a
register that survives 8,800 words of protocol detail. A generic AI pass deletes this line as
throat-clearing, which would be wrong: it is doing register-setting work.

## What to copy

- Open by naming what a previous piece skipped, when true.
- Use questions to carry progression in long pieces. Roughly one per 15 sentences.
- Quarantine deep material under an explicitly optional heading.
- Expand every acronym on first use.
- Calibrate heading density to question density. Many questions, fewer headings. Few questions,
  more headings.

## What not to copy

- The question rate in short pieces. One question every 15 sentences in a 300-word post is
  interrogating the reader.
- The conversational register for reference docs or incident write-ups.
