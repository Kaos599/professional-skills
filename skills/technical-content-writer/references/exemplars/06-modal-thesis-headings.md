---
source:    https://modal.com/blog/truly-serverless-gpus
author:    Modal engineering
authored:  false
format:    engineering blog, systems deep-dive
added:     2026-08-09
notes:     |
  The single most copyable structural device found in the whole survey: headings that
  are complete load-bearing claims. Skim the H2s and you have the argument.
---

## Why this one

~4,780 words on GPU cold starts, and you can read the entire causal chain of the argument
without reading a word of body text. That is not an accident of good headings; it is a
deliberate device that almost nobody else uses.

## The device: thesis-sentence headings

Every heading is a complete sentence making a claim, not a noun phrase labelling a topic:

> ## Why care about serverless GPUs? To maximize GPU Allocation Utilization for inference workloads.
> ## What's so hard about serverless GPUs? Startup latency.
> ## You can remove tens of minutes of latency by taking instance allocation and health checks out of the hot path.

Compare the default that generated drafts produce:

> ## Overview
> ## The Problem
> ## Our Approach
> ## Results
> ## Conclusion

The second set labels containers. The first set *argues*. A reader who skims only the headings
of the Modal post leaves knowing the thesis, the obstacle, and the mechanism. A reader who skims
the second set leaves knowing that a post exists.

### How to write them

1. Draft the section.
2. Ask: what does this section claim? Write that as one sentence.
3. If you cannot, the section has no point and should be cut or merged.

The question-then-answer form (`What's so hard about serverless GPUs? Startup latency.`) is a
good default because it names the reader's question and answers it in the same line.

**Cost:** they are longer than noun-phrase headings and can look cluttered in a table of
contents. Worth it above ~2,000 words. Not worth it in reference docs, where readers navigate by
scanning for a topic noun rather than following an argument.

## Other traits

**Before/after tables instead of prose claims.** The cold-start improvement is given as a table:

> Snapshot OFF | Snapshot ON
> vLLM boot latency (mean) 95,679 ms | 13,797 ms
> SGLang boot latency (mean) 83,713 ms | 17,486 ms

Two engines, absolute milliseconds, mean specified. The reader computes the ratio themselves,
which is more persuasive than being told "7x faster."

**States an unsolved constraint.** Rather than presenting the design as complete:

> Because of the current restriction to a single GPU, they are most commonly used for models
> with sizes in the few to few tens of gigabytes.

**Closes on unfinished work, not a summary:**

> Finally, we've still got a lot of work to do — those RDMA networks don't configure themselves!

This is the strongest ending in the surveyed AI-startup corpus. It is honest, specific, has a
joke in it, and refuses the forward-looking-synthesis close that every other company post
reaches for.

## What to copy

- Thesis-sentence headings for anything over ~2,000 words. The highest-leverage structural
  device in the survey.
- Before/after tables with absolute units, letting the reader compute the ratio.
- Naming a current restriction in the same breath as the capability.
- Ending on the unfinished work.

## What not to copy

- Thesis-sentence headings in reference docs or runbooks, where readers scan for topic nouns.
- The exclamation-mark register if it is not yours.
