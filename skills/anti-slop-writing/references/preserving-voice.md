# Preserving voice

The reference for Step 6. Everything else in this skill is subtraction; this file is the only
part that protects.

Derived from a survey of eight posts by independent technical writers and small-company blogs
(Simon Willison, Julia Evans, Dan Luu, Brandur Leach, Fly.io, Tailscale, Pragmatic Engineer,
Rachel by the Bay), analysing specifically what a generic editing pass destroys.

## The core problem

An AI editing pass optimises for **clarity, confidence, and inoffensiveness**. Distinctive
writing depends on **timing, admitted uncertainty, and calculated risk**. These are in direct
tension. A helpfulness-tuned pass reads the second set as noise to clean up rather than signal
to preserve.

Every item below is a real thing that gets destroyed, with a verbatim example of what is at
stake.

---

## The eight things an editing pass destroys

### 1. Fragments used for pacing

> "Shit, it's already there." (Fly.io)
> "It was the kernel." (Rachel by the Bay)

A smoothing pass turns these into complete sentences and kills the timing. **Rule:** a fragment
following a long sentence is almost always deliberate. Leave it.

### 2. Self-undermining hedges next to a confident claim

> "Someone asked me... if I was saying that agents needed sound cards and USB ports. And, maybe?
> I don't know. Not today." (Fly.io)
> "Here's where I lose you. I know this because it's also where I lose my team, most of whom
> don't believe me about this." (Fly.io)

An edit optimising for authoritative tone removes exactly the admission that builds trust.
**Rule:** never delete an admission of uncertainty to make a claim land harder. That is a lie
about confidence.

### 3. Digressive parentheticals that do not serve the main clause

> "(Why did Anthropic jump from Claude 3.5 Sonnet to 3.7? Because they released a major bump to
> Claude 3.5 in October 2024 but kept the name exactly the same... Anthropic burned a whole
> version number by failing to properly name their new model!)" (Simon Willison)
> "we didn't write our own IdP (because... yikes)." (Tailscale)

Deleted as off-topic, or promoted to full sentences, which loses the private-joke effect.
**Rule:** a parenthetical that does not serve the argument may be serving the voice. Keep it
unless it obscures the sentence.

### 4. Named people and institutions in vulnerable disclosures

> "an interviewer at Jane Street really dug into what I'd written in that post and tore me a new
> one for that post (it was the most hostile interview I've ever experienced by a very large
> margin)" (Dan Luu)

Anonymised into "a difficult interview experience", which destroys the specific detail that
makes the claim falsifiable and therefore credible. **Rule:** if the author named someone, they
decided to. Not your call to anonymise.

### 5. Deliberate repetition as a rhythm device

Willison's "The year of X" refrain across ~26 headings. Tailscale's "And then... And then...".
Read as redundant and varied away. **Rule:** repetition across headings or sentence openings at
regular intervals is structure, not error. Check whether it is a refrain before breaking it.

### 6. Unresolved endings

> "It's not clear if they later came back and did 'interleave' or otherwise twiddled things...
> If you ever switched on membind with numactl and started a mass slaughter of processes on your
> Linux boxes, this might be why. I hope this helps someone." (Rachel by the Bay)
> "I wouldn't exactly recommend this path, but it seems to have worked out ok." (Dan Luu)

Both simply stop. A pass "fixes" this into a manufactured tidy moral. **Rule:** refusing to
manufacture closure when the author does not know how something ended is honest. Adding a
conclusion where the author declined one is the single most common damage this skill can do.

### 7. Register-breaking word choices used once for effect

> "## Fuck Ephemeral Sandboxes" (Fly.io, as an actual section heading)

Laundered into "Moving Beyond Ephemeral Sandboxes": grammatically superior, rhetorically dead.
**Rule:** a register break that appears once in a piece is a deliberate spike. Frequency tells
you: once is a device, five times is a tic.

### 8. Self-deprecation that is not actually modest

> "I don't actually have to be nearly as smart or work nearly as hard as most people to get good
> results... if no one else trying the same thing, that's easy to do!" (Dan Luu)

Reads as false modesty to a generic pass and gets deleted or inflated, missing that it is a
confident claim about a repeatable strategy, not an apology. **Rule:** read what the
self-deprecation is actually asserting before touching it.

---

## Positive signals to protect

Present in the strongest writing surveyed. Hard to fake, easy to delete.

**Admitted not-knowing, stated plainly.**
> "I don't really have an explanation for this." (Willison)
> "It's not clear if they later came back..." (Rachel by the Bay)

**Sincere emotional register, including emoticons and caps.**
> "Sometimes I get really demoralized when debugging and it feels like I'll NEVER make progress.
> I have to remind myself that I've fixed a lot of bugs before, and I'll probably fix this one
> too :)" (Julia Evans)

**Self-undercutting before the close.**
> "Of course, not all bugs are adventures (that off-by-one error I was debugging today certainly
> did not feel like a fun adventure)." (Julia Evans)

**Flat acknowledgment of self-interest.**
> "Obviously, I'm trying to sell you something here. But that doesn't make me wrong." (Fly.io)

**One sustained conceit across a long piece.** Brandur's fictional "Rocket Rides" company
carried through a 6,000-word spec. Fly.io's "hyper-productive five-year-old savant." These
survive because they are consistent, not because they are frequent.

**Mid-sentence jargon translation.**
> "someone opened a SEV (that is, a notification of something going wrong)" (Rachel by the Bay)

**Raw evidence pasted in.** Live terminal transcripts (Fly.io), verbatim syslog lines and
man-page text (Rachel by the Bay), actual SQL and Ruby (Brandur). Proof as artifact rather than
description.

---

## Genre tracks harder than authorship

An important correction to the naive framing. Brandur Leach is independent but writes in
tutorial/spec mode, and on the ending axis he behaves like a corporate blog: formally concluded,
no admitted uncertainty, near-total absence of first person.

**Do not assume an independent byline licenses personality, or that a company byline forbids
it.** Fly.io is a company blog with profanity in the headings. Tailscale is a company blog in
the same "startup voice" register that never exceeds "yikes". Ask what the *genre* tolerates,
then what the *author* actually does.

## The check

Before shipping any edit, walk the eight items above against your diff. For each one you
removed, answer: **was this an error, or was this the person?**

If you cannot tell, leave it in and flag it. A retained oddity costs the reader a second. A
deleted voice trait costs the author their writing.
