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


## Senior Technical Authority: The Quiet Expert

A major failure mode of anti-slop editing is confusing "voice preservation" with **performed incompetence**.

Generic anti-slop advice tells editors to preserve self-deprecation, confusion, and admissions of failure ("I don't know what I'm doing", "demoralized : )"). If the author is a senior engineer who designs and deploys production multi-agent systems, forcing beginner apologies or faux-modesty destroys their credibility.

### The Rules of Senior Authority:
1. **Quiet confidence over defensive posturing:** Never sneer at "casual prompt toys" or "amateur developers." The senior engineer doesn't need to punch down; they let the domain constraints demonstrate why naive approaches don't work.
2. **Zero dilution of technical rigor:** Teaching like a peer does NOT mean dumbing down the code or the domain. Keep the exact statutory tax sections (Section 112A, Section 50AA 65% domestic equity rule), exact protocols (MCP JSON-RPC), and exact metrics (38% benchmark overlap, 0.38% TER, ₹6,840 Cr AUM, 68.4% downside capture).
3. **First-person ownership ("I", not "we", not passive):** When an engineer builds something, they say: "I mounted three declarative skills," not "Declarative skills were mounted" (whitepaper slop) and not "We mounted" (fake corporate committee).
4. **Mechanism over mood:** Explain how the DAG resolves dependencies and why T+2 settlement differs from T+4. Don't lecture on philosophy.

### The Calibration Matrix

| Draft Type | Beginner / Hobbyist Tone (Defect) | Arrogant Jargon Theater (Defect) | Senior Technical Authority (Harsh's Standard) |
|---|---|---|---|
| **Opener** | "I've been playing with LLMs and wanted to see if they could fix my money." | "Most developers use LLMs as glorified autocomplete toys, but I engineered a multi-agent loop." | "Personal finance is an unforgiving test for language models. It requires strict asset location, statutory tax rules, and settlement latencies that raw chat prompts cannot solve." |
| **UI Artifact** | "I got the bot to make a cool little webpage for me." | "Generative UI: Compiling an Interactive Real-Time HTML Cockpit." | "Generative UI: Compiling an Interactive Allocation Dashboard." |
| **Execution** | "I sold some funds and waited a few days for the money." | "Capital Deployment Protocol across Tranche 1 and Tranche 2 Settlement DAGs." | "Settlement Timeline: Staging Redemptions Across T+2 and T+4 Clearing Cycles." |
| **Conclusion** | "Agents are pretty cool! Hope this helps you automate stuff." | "The 4 Decoupled Primitives Every Enterprise AI Engineer Needs in 2026." | "When you put these pieces together, agents stop being novelty chatbots and become practical, transparent systems for solving day to day problems." |

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

## A writing sample overrides this skill's defaults

If the author gave you a sample of their own writing, it is evidence about their habits, and
evidence beats rules. The full precedence chain lives in SKILL.md (house style > sample >
genre table > this skill's defaults); the practical consequence here: read the sample first
and note sentence length, word choice, paragraph openings, punctuation habits, repeated
phrases. Then match those habits even where they trip a rule in this skill. A writer who uses
em dashes keeps them at roughly their own rate; do not apply the dash budget as a ban. A
writer who starts paragraphs with "So" keeps doing that. The only things a sample cannot
override are the hard rules - no invented facts, no claim changes, no authorship verdicts.

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
