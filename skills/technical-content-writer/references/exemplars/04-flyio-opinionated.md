---
source:    https://fly.io/blog/sandboxing-and-workload-isolation/
author:    Fly.io engineering
authored:  false
format:    company engineering blog, opinionated register
added:     2026-08-09
notes:     |
  Proof that a company blog can have a person in it. Copy the historical-survey
  structure and the willingness to end on a personal recommendation.
---

## Why this one

A company blog that reads like an individual engineer wrote it, because one did. It surveys a
whole problem space and then *takes a side*, which is the thing most company blogs refuse to do.

## Measured signature

| | |
|---|---|
| Words | 2,890 |
| Sentences | 139 |
| Mean sentence length | **19.5 words** (median 17) |
| Standard deviation | **11.3** |
| p10 / p90 | 8 / 35 words |
| Fragments under 8 words | 9.4% |
| Em dashes | 3 (**0.52 per 500 words**, inside the 1-per-500 budget) |
| Semicolons | 23 |
| Colons | 20 |
| Question marks | 4 |
| Headings | 9 |

Semicolon-heavy and dash-light, like the Dan Luu post. This appears to be a real marker of
writers who build long sentences on purpose rather than reaching for a dash as a rhythm crutch.

## Verbatim excerpts

**Opening:**

> Workload isolation makes it harder for a vulnerability in one service to compromise every other
> part of the platform. It has a long history going back to 1990s qmail, and we generally agree
> that it's a good, useful thing.

**Closing:**

> These are all valid options! I'll say this: for ROI purposes, if time and effort is a factor,
> and if I wasn't hosting hostile code, I would probably tune an `nsjail` configuration before I
> bought into a containerization strategy.

## Signature

**Opening move: flat definition plus a concession.** Defines the thing, dates it (1990s qmail),
and concedes the consensus ("we generally agree that it's a good, useful thing") before
complicating it. No hook, no question, no manufactured tension.

**Structure: chronological survey, one technique per heading.** `chroot` → `Privilege
Separation` → `Prelapsarian Containers` → `Incarceration` → `Language Runtimes` → `Emulation` →
`Lightweight Virtualization` → `Firecracker`. Each section is one mechanism, roughly in
historical order. A reader can enter at any heading.

**Heading names carry voice.** "Prelapsarian Containers" and "Incarceration" are jokes. They are
also accurate. This is the cheapest personality-per-word in technical writing and almost nobody
does it, because generic section headers are the default an AI pass produces.

**Named technologies everywhere.** qmail, chroot, nsjail, Firecracker. The post is dense with
specific identifiers rather than categories, which is what makes it checkable.

**Closing: a personal recommendation with its conditions attached.** "for ROI purposes, if time
and effort is a factor, and if I wasn't hosting hostile code, I would probably tune an `nsjail`
configuration." Three explicit conditions, a hedge ("probably"), and a named tool. This is what
taking a position looks like when done honestly: it is falsifiable and scoped.

**"These are all valid options!"** The exclamation mark and the concession before the
recommendation. It signals the recommendation is a judgment, not a verdict.

## What to copy

- Conceding the consensus before complicating it.
- Chronological survey structure when the field has a history.
- Headings with voice in them.
- Ending on a scoped personal recommendation: the conditions, the hedge, and the named choice.
- Switching to "I" for the recommendation even when the post is otherwise institutional.

## What not to copy

- The exclamation mark if it is not your register.
- The joke headings in reference documentation, where scanability beats personality.
