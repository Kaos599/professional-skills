---
source:    https://www.baseten.co/blog/33-faster-llm-inference-with-fp8-quantization/
author:    Baseten engineering
authored:  false
format:    engineering blog, benchmark post
added:     2026-08-09
notes:     |
  The reference standard for reporting a performance number. Copy the conditions-in-the-
  same-breath discipline and the named failure boundary. This is the exemplar to reach
  for whenever a draft contains a benchmark.
---

## Why this one

Benchmark posts are where technical writing most often degrades into marketing, because a
percentage with no conditions attached looks like evidence and costs nothing to produce. This
post is the counter-example: **every figure carries its measurement conditions in the same
sentence or the one immediately following.**

## The discipline

> By quantizing Mistral 7B to FP8, we observed the following improvements vs FP16 (both using
> TensorRT-LLM on an H100 GPU):
> * An 8.5% decrease in latency in the form of time to first token
> * A 33% improvement in speed, measured as output tokens per second
> * A 31% increase in throughput in terms of total output tokens
>
> These benchmarks are for a specific batch size (32 max requests) and sequence shape (80 input
> and 100 output tokens per request) — we'll dive into a wider range of benchmarks later in the
> article.

Count what is pinned down before the reader reaches the percentages:

| Dimension | Value |
|---|---|
| Model | Mistral 7B |
| Precision | FP8 |
| Baseline | FP16 |
| Framework | TensorRT-LLM |
| Hardware | H100 |
| Batch size | 32 max requests |
| Sequence shape | 80 in / 100 out |
| Metric definition | "output tokens per second", "time to first token" |

Eight conditions. Each percentage also names *what* was measured, not just that it improved.
"33% faster" is meaningless; "33% improvement in speed, measured as output tokens per second"
is checkable.

## Naming the failure boundary

The rarer and more valuable move. Most posts report where the technique works. This one reports
where it stops working, with numbers:

> For example, an input sequence of 1000 tokens works well at a batch size of 72, but at a batch
> size of 96 TTFT spikes to over 10 seconds.

This does more for credibility than any of the improvement figures. A reader who plans to run at
batch 96 has just been saved an afternoon, and a reader who did not need that has learned the
authors actually ran the sweep.

## Reporting what did not work

> Previously, we've tried two approaches to 8-bit quantization with INT8. First, we created
> weights-only quantizations of LLMs. While this approach preserved output quality, it required
> activations to still run in FP16, limiting speed improvements. We also tried SmoothQuant to
> quantize all components of a given LLM into INT8, but found that it degraded model output
> quality to unacceptable levels for this model and use case.

Two named prior attempts, each with the specific reason it failed, and a scoped caveat ("for
this model and use case") that stops it from over-claiming about SmoothQuant generally.

Contrast the anti-pattern documented in
`../../../anti-slop-writing/references/structural-patterns.md` under *Objection-handling
disguised as candour*: a limitations section where every item resolves to the author's own
product. Baseten's failures stay failed.

## The checklist this exemplar produces

Before any performance number ships, it carries:

- [ ] What was measured, defined (not "faster" but "output tokens per second")
- [ ] The baseline it improved against
- [ ] Hardware
- [ ] Framework or runtime and version where it matters
- [ ] Batch size
- [ ] Sequence shape, context length, or equivalent workload descriptor
- [ ] The boundary where the result stops holding, if known
- [ ] Sample size or run count, for anything noisy

If the author cannot supply these, **cut the number**. Do not soften it into "significantly
faster", which is the same claim with the evidence removed.

## What to copy

- Conditions in the same breath as the figure, always.
- Metric definitions, not adjectives.
- The named failure boundary with its numbers.
- Failed prior attempts that stay failed, with scoped caveats.

## What not to copy

- Nothing identified. This post is the reference standard for the genre.
