# Voice extraction protocol

Derive an operational voice signature from real samples. Run this at Step 1 of every piece.
Re-derive each time. Do not carry a signature from memory across sessions, because the
exemplar set changes and a stale signature is worse than none.

The output is a spec you will check the draft against in Step 4. Keep it short enough to hold
in working context. This is not literary criticism.

## Source priority

Use the strongest real material available, in this order:

1. The author's own published posts and threads, most recent first
2. Their essays, memos, launch notes, or newsletters
3. Real outbound emails or DMs that worked
4. Their product docs, changelogs, README framing, and site copy
5. Exemplars in `exemplars/` marked as aspirational rather than authored

Never use generic platform examples as source material. "Good LinkedIn posts" as a category
averages into exactly the cadence this skill exists to avoid.

**Prefer 5 to 20 samples.** Below 3, say so explicitly and treat the signature as provisional.

If the source set splits (public launch voice versus working voice, or long-form versus social),
**do not average them.** Produce two signatures and pick per piece. Averaging conflicting
sources produces mush, which is the single most common failure in voice work.

## Measure these dimensions

### Rhythm
- Mean sentence length in words, and the spread. Match the author's mean within ±2 words.
- Distribution: what does the shortest 10% look like, and the longest 10%?
- Fragment rate. Does this author use them? How often?
- Paragraph length in sentences, and whether it varies.

### Compression
Dense and elliptical, or explanatory and complete? How much does the author assume the reader
already knows? Do they define terms or drop them?

### Capitalisation and typography
Conventional, all-lowercase, mixed, or situational? Note this precisely, because it is one of the most
visible signature elements and one of the easiest to get wrong. Also: em dash usage (usually
zero), colon habits, ellipsis, straight vs curly quotes, code formatting for identifiers.

### Person and address
First person singular, plural, or absent? Does the author address the reader as "you"? How
early does "I" appear, if at all?

### Parentheticals
Used for qualification, narrowing, aside, or joke? Or absent? Note both how they are used and
how they are *not*.

### Questions
Frequent, rare, rhetorical, genuine, or absent? If the author never asks rhetorical questions,
that goes on the never-do list and is a hard constraint.

### Claim sharpness
How bluntly are claims made? Is there hedging, and is it honest hedging or softening? Does the
author state opinions outright or route around them?

### Receipts density
How often do numbers, mechanisms, named systems, versions, and specific artifacts appear? Count
them per 100 words. This is the most transferable dimension for technical writing.

### Connectors and transitions
Which connectives does this author actually use? Some use "but" and "so" and nothing else. Some
use none and rely on paragraph breaks. Note the preferred set and use it consistently rather
than rotating for variety.

### Openings and closings
Collect the actual first lines from the sample set. Collect the actual last lines. These are the
highest-signal, most-copyable elements. How does the author end: a rule, an action, a fact, a
question, or nothing?

### Idiolect
- Characteristic filler phrases and verbal habits
- Recurring metaphors and comparison domains
- Preferred vocabulary: which of two synonyms do they reach for?
- Recurring stories or reference points, and how they retell them
- Topics they never touch

### The never-do list
The most useful output of the whole protocol. **Every item must be observable in the source set
or explicitly requested by the user.** Do not populate it from generic anti-slop rules; those
already live in the `anti-slop-writing` skill.

Examples of what belongs here: "never uses em dashes" · "never opens with a question" ·
"never uses exclamation marks" · "never capitalises sentence starts" · "never says 'excited to
share'" · "never closes with a call to action."

## Output format

```
VOICE SIGNATURE
===============
Author:
Source set:        [N samples, what kind, date range]
Confidence:        [high / provisional / low, with reason]
Split:             [none, or: two signatures and when to use each]

Rhythm             mean N words (±2), range N–N, fragments N% , paragraphs N–N sentences
Compression        [dense/explanatory + what is assumed known]
Capitalisation     [exact convention]
Person             [I / we / none; reader addressed as "you"? y/n; "I" appears at line N]
Parentheticals     [how used / how not used]
Questions          [frequency and kind]
Claim sharpness    [blunt / hedged / how]
Receipts           [N numbers or named artifacts per 100 words]
Connectors         [the actual set this author uses]
Openings           [3–5 verbatim first lines from samples]
Closings           [3–5 verbatim last lines from samples]
Idiolect           [vocabulary, metaphor domains, verbal habits]

NEVER
- [observed in source set]
- [observed in source set]
```

## Verifying a draft against the signature

Check dimension by dimension, not by overall impression. Impression checks pass drafts that are
wrong in every measurable way.

1. Compute the draft's mean sentence length. Within ±2 of the signature?
2. Check capitalisation convention line by line.
3. Count parentheticals, questions, and em dashes against the signature rates.
4. Count receipts per 100 words against the signature rate.
5. Check the opening against the collected openings. Does it belong in that set?
6. Check the closing the same way.
7. Walk the never-do list item by item.

Then the final test: **would the author recognise this as their own?** If it is competent but
generic, the signature was applied as decoration rather than structure. Go back to Step 3.

## Privacy

- Store patterns and derived signatures, not raw private messages.
- Do not commit personal voice fingerprints to a tracked repo unless the user asks for that.
- Read only what the user confirms you may read.
