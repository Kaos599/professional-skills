---
source:    multiple (see per-quote attribution)
author:    Simon Willison, Julia Evans, Dan Luu, Fly.io, Rachel by the Bay
authored:  false
format:    composite reference
added:     2026-08-09
notes:     |
  The personality gap. Exemplars 02-07 are all company blogs and teach structure.
  This one teaches voice: the specific devices that make writing identifiable, drawn
  from writers whose work is unmistakable at a glance.
---

## Why this one exists

Exemplars `02` through `07` are engineering blogs. They teach structure, benchmark discipline,
and heading strategy, and they are all institutionally voiced. Used alone they produce competent,
anonymous writing.

This file is the counterweight. Every quote is a device that would be edited out by a generic
improvement pass, and every one is load-bearing.

---

## Devices, with what they cost if removed

### The self-aware running joke

> Because I'm a sucker for tilting at linguistic windmills... I should really get a less
> confrontational linguistic hobby!
> — Simon Willison

> My dastardly multi-year plan is to trick multiple AI labs into investing vast resources to
> cheat at my benchmark until I get one.
> — Simon Willison

The writer knows the bit is a bit and says so. This is what separates a running joke from a tic.
**Cost if removed:** the piece becomes a list of events with no one behind it.

### The refrain as structure

Willison's year-in-review runs ~26 headings on one template: "The year of reasoning", "The year
of agents", "The year of pelicans riding bicycles", "The year of the snitch!". The repetition
imposes mock-canonical order on what is really a diary.

**Cost if removed:** an editing pass varies these for freshness and the structure collapses into
26 unrelated sections.

### Sincere emotional register

> Sometimes I get really demoralized when debugging and it feels like I'll NEVER make progress.
> I have to remind myself that I've fixed a lot of bugs before, and I'll probably fix this one
> too :)
> — Julia Evans

Caps for feeling, an unironic emoticon, an admission of demoralisation. **Cost if removed:** the
post stops being written by someone who has felt this and becomes advice about feeling it.

### Undercutting your own thesis before the close

> Of course, not all bugs are adventures (that off-by-one error I was debugging today certainly
> did not feel like a fun adventure). But I think it's important to (as much as you can) reflect
> on your bugs and see what you can learn from them.
> — Julia Evans

She names a same-day counterexample to her own argument, then lands anyway. **Cost if removed:**
the claim becomes unfalsifiable and therefore unpersuasive.

### The recursive reasoning chain

> People frequently think that I'm very stupid. I don't find this surprising, since I don't mind
> if other people think I'm stupid, which means that I don't adjust my behavior to avoid seeming
> stupid, which results in people thinking that I'm stupid.
> — Dan Luu

The whole thesis in one breath, as a loop. **Cost if removed:** split into three tidy sentences,
the causal structure that *is* the argument disappears.

### The costly disclosure

> an interviewer at Jane Street really dug into what I'd written in that post and tore me a new
> one for that post (it was the most hostile interview I've ever experienced by a very large
> margin)
> — Dan Luu

Named institution, admitted humiliation. **Cost if removed:** anonymised to "a difficult
interview", it stops being checkable and stops being credible. See
`../../../anti-slop-writing/references/preserving-voice.md` item 4.

### Self-deprecation that is actually a claim

> I don't actually have to be nearly as smart or work nearly as hard as most people to get good
> results... if no one else trying the same thing, that's easy to do!
> — Dan Luu

Reads as modesty, asserts a repeatable strategy. **Cost if removed:** a pass that reads this as
false modesty deletes the actual thesis.

### Profanity as structural punctuation

> ## Fuck Ephemeral Sandboxes
> — Fly.io, an actual section heading

> Shit, it's already there.
> — Fly.io

Used once each, at the emotional peak. **Cost if removed:** laundered to "Moving Beyond
Ephemeral Sandboxes", grammatically superior and rhetorically dead.

### Admitting your own team disagrees

> Here's where I lose you. I know this because it's also where I lose my team, most of whom
> don't believe me about this.
> — Fly.io

> Obviously, I'm trying to sell you something here. But that doesn't make me wrong.
> — Fly.io

Flat acknowledgment of both internal dissent and self-interest. **Cost if removed:** the piece
becomes a pitch pretending not to be one, which readers detect anyway.

### The sustained absurd conceit

> Claude is a hyper-productive five-year-old savant. It's uncannily smart, wants to stick its
> finger in every available electrical socket, and works best when you find a way to let it zap
> itself.
> — Fly.io

Carried across paragraphs rather than dropped after one line. Brandur Leach does the same with a
fictional jetpack-rideshare company sustained through a 6,000-word Postgres spec. **Rule:** one
conceit, consistent, load-bearing. Not three metaphors competing.

### Refusing to manufacture an ending

> It's not clear if they later came back and did "interleave" or otherwise twiddled things...
> If you ever switched on membind with numactl and started a mass slaughter of processes on your
> Linux boxes, this might be why. I hope this helps someone.
> — Rachel by the Bay

> I wouldn't exactly recommend this path, but it seems to have worked out ok.
> — Dan Luu

Both stop rather than concluding. **Cost if removed:** a manufactured tidy moral, which is the
single most common damage an improvement pass does.

### Mid-sentence jargon translation

> someone opened a SEV (that is, a notification of something going wrong)
> — Rachel by the Bay

Inline, no glossary, no condescension. **Cost if removed:** either the jargon stays unexplained
or it gets a paragraph it does not need.

---

## Genre tracks harder than authorship

Brandur Leach is independent and writes like a spec: formally concluded, no admitted
uncertainty, almost no first person. Fly.io is a company blog with profanity in the headings.
Tailscale is a company blog in the same startup register that never exceeds "yikes".

**Do not assume an independent byline licenses personality or that a company byline forbids it.**
Ask what the genre tolerates, then what the author actually does.

## What to copy

- One running device, self-aware, sustained.
- Emotional register where it is real.
- Undercut your own thesis before closing, if there is a real counterexample.
- Name the institution in a costly disclosure, if it is yours to name.
- Stop when you do not know how it ended.
- Translate jargon inline.

## What not to copy

- Profanity, caps, or emoticons that are not your register. Borrowed edge reads worse than none.
- The costly disclosure if the cost falls on someone else.
- Multiple competing conceits. One, or none.
