# Exemplars

Source material for `voice-extraction-protocol.md`. The skill derives a voice signature from
whatever is in this folder at runtime. Adding a file changes the signature. No code change
required.

Comparative measurements across these sources live in `../house-styles.md`.

## Two kinds of file here

**Voice exemplars** (`authored: true`) are the user's own writing, pasted verbatim. These define
the voice to reproduce.

**Craft exemplars** (`authored: false`) are published writing worth learning from. These are
*annotated*, not reproduced: a short set of verbatim excerpts, the measured signature, and a
what-to-copy / what-not-to-copy split. Do not paste whole third-party posts into this repo.

The protocol weights them differently. Copy structure, rhythm, and technique from either. Only
adopt idiolect, recurring stories, and personal reference points from `authored: true`.

## Adding one

Create `NN-short-slug.md`, numbered in order added, with this header:

```markdown
---
source:    [URL, or where it was published]
author:    [who wrote it]
authored:  [true if the user wrote it | false if it is a craft reference]
format:    [linkedin post | blog | thread | newsletter | essay | engineering blog]
added:     YYYY-MM-DD
notes:     [what specifically is worth copying here]
---
```

For `authored: true`, paste the piece **verbatim** below the header, including typos, unusual
capitalisation, and comma splices. Those are signal. A cleaned-up exemplar teaches the wrong
voice.

For `authored: false`, follow the pattern in `02` through `05`: why this one, verbatim excerpts,
measured signature, what to copy, what not to copy.

## Do not average conflicting sources

If the exemplars split into distinct voices, produce two signatures and pick per piece.
Averaging produces mush. With the current set, the four craft exemplars disagree sharply on
sentence length, heading density, and formatting, and that disagreement is the useful part.

## Current set

| File | Author | Authored | Format | Why it is here |
|---|---|---|---|---|
| `01-inference-stack.md` | provided by user | unspecified | LinkedIn post | Mechanism-first decision-procedure post. Lowercase cadence, zero em dashes, ends on a rule. |
| `02-anthropic-engineering.md` | Anthropic Eng | false | engineering blog | Institutional voice that stays specific. The "Instead of X, consider Y" move. |
| `03-danluu-analytical.md` | Dan Luu | false | analytical blog | Argument-first with no scaffolding. Long sentences, zero em dashes, ends without a bow. |
| `04-flyio-opinionated.md` | Fly.io | false | engineering blog | Company blog with a person in it. Survey then a scoped personal recommendation. |
| `05-tailscale-explainer.md` | Tailscale | false | long explainer | 8,800 words that stay readable. Questions carry progression instead of headings. |
| `06-modal-thesis-headings.md` | Modal | false | systems deep-dive | Headings as complete claims. Skim the H2s and you have the argument. |
| `07-baseten-benchmark-discipline.md` | Baseten | false | benchmark post | The reference standard for reporting a number. Conditions in the same breath; named failure boundary. |
| `08-personality-devices.md` | composite | false | composite reference | The voice counterweight. Devices a generic pass destroys, with what each costs. |
| `09-failure-narratives.md` | Uber Eng | false | engineering blog | How to write the part where it did not work. Abandoned approach, unexpected result, scope refusal. |

## Measuring a new craft exemplar

The comparative table in `../house-styles.md` needs these figures. Compute them over the post
body with code blocks excluded:

- word count, sentence count
- mean, median, and standard deviation of sentence length in words
- share of sentences over 30 words and under 8 words
- em dash count, and em dashes per 500 words
- semicolon, colon, and question-mark counts
- heading count, and words per heading

The em-dash-per-500 figure and the words-per-heading-against-questions ratio are the two that
have produced the most transferable findings so far.
