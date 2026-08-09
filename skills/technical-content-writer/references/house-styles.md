# House styles

How respected technical blogs actually write, measured rather than assumed. Use this to pick a
register before drafting, and to sanity-check a draft's mechanics against real published work.

All figures below were computed directly from the post bodies (code blocks excluded) on
2026-08-09. Verbatim quotes are from the linked sources.

---

## The comparison

| | Dan Luu | Fly.io | Tailscale | Anthropic Eng |
|---|---|---|---|---|
| Post | percentile-latency | sandboxing | NAT traversal | writing tools for agents |
| Words | 2,271 | 2,890 | 8,792 | ~4,000 |
| Mean sentence | **22.3** | 19.5 | 19.7 | not computed |
| Median | 20 | 17 | 18 | |
| Std dev | 12.5 | 11.3 | 10.9 | |
| Over 30 words | **19.8%** | 13.7% | 12.4% | |
| Under 8 words | 9.4% | 9.4% | 8.6% | |
| Em dashes | **0** | 3 | 10 | present |
| Em dash / 500w | 0.00 | 0.52 | 0.57 | |
| Semicolons | 9 | **23** | 5 | rare |
| Questions | 2 | 4 | **28** | several |
| Headings | 6 | 9 | 5 | 13 |
| Words / heading | 379 | **321** | **1,758** | ~300 |

### What generalises

**1. Nobody exceeds ~0.6 em dashes per 500 words.** The strictest is zero. This is the strongest
cross-source agreement in the sample and it matches the anti-slop corpus consensus (84 of 100
skills address em dashes). The `anti-slop-writing` budget of 1 per 500 words is, if anything,
more permissive than what good writers actually do.

**2. Semicolons substitute for em dashes.** Dan Luu: 0 dashes, 9 semicolons. Fly.io: 3 dashes,
23 semicolons. Both build long sentences on purpose and neither reaches for a dash to do it.
Tailscale inverts this (10 dashes, 5 semicolons) and also has the shortest complex-sentence
share. **If you want long sentences without dash-dependence, the semicolon is the tool.**

**3. High variance is universal; short-sentence dogma is not.** Every source runs a standard
deviation above 10, and 12 to 20% of sentences exceed 30 words. Dan Luu's mean is 22.3 words.
The advice to "write short punchy sentences" describes none of these writers. What they share is
*variance*, not shortness.

**4. Heading density trades off against question density.** The clearest finding in the sample:

| | Words per heading | Questions |
|---|---|---|
| Fly.io | 321 | 4 |
| Dan Luu | 379 | 2 |
| Tailscale | **1,758** | **28** |

Tailscale sustains 8,792 words on 5 headings because a question every ~15 sentences tells the
reader what the next passage solves. Fly.io needs a heading every ~320 words because it asks
almost nothing. **Both navigate; pick one mechanism and commit.** A long piece with neither is
unreadable, and a short piece with both is exhausting.

**5. Nobody ends with a summary.** Dan Luu ends on acknowledgements. Fly.io ends on a scoped
personal recommendation. Anthropic's forward-looking close is the weakest ending in the sample
and the most corporate. The summary-recap ending that generated text defaults to appears in none
of these as the actual final move.

---

## The registers

Pick one before drafting. They are not interchangeable.

### Analytical (Dan Luu)

Argument-first, minimal scaffolding, long sentences, structure that enacts the thesis rather
than announcing it. No bullets carrying the argument, no callouts, no bold mid-sentence.

Use when: the argument is genuinely sequential and the reader will read start to finish.
Avoid when: the piece will be scanned, or used as reference.

### Opinionated survey (Fly.io)

Historical or taxonomic survey, one mechanism per heading, headings with jokes in them, then a
scoped personal recommendation at the end. Concedes the consensus before complicating it.

Use when: the field has several established options and the reader needs to choose.
Avoid when: you cannot actually recommend something. A survey that refuses to conclude is the
generated default.

### Long explainer (Tailscale)

Layered disclosure, questions carrying progression, optional deep sections explicitly marked,
every acronym expanded, conversational register sustained over great length.

Use when: the subject genuinely needs 5,000+ words and the audience is mixed.
Avoid when: the piece is short. The mechanics are calibrated to length.

### Institutional procedural (Anthropic Engineering)

Two acts announced up front (procedure, then principles), "Instead of X, consider Y"
substitutions with real names, numbers always carrying their measurement context, self-criticism
used as evidence, first-person plural.

Use when: writing on behalf of a team or company.
Avoid when: the piece depends on individual judgment. The corporate "we" flattens it.

### Benchmark post (Baseten)

Every figure carries its conditions in the same breath: model, baseline, hardware, framework,
batch size, sequence shape, and the metric's definition. Names the boundary where the result
stops holding. Reports failed prior attempts and leaves them failed.

Use when: the piece exists to report a performance result.
Avoid when: you cannot supply the conditions. Then you do not have a benchmark post, you have a
claim, and it should be cut rather than softened into "significantly faster."

See `exemplars/07-baseten-benchmark-discipline.md` for the full checklist.

---

## Two devices worth stealing

### Thesis-sentence headings (Modal)

Headings that are complete load-bearing claims rather than topic labels:

> ## What's so hard about serverless GPUs? Startup latency.
> ## You can remove tens of minutes of latency by taking instance allocation and health checks out of the hot path.

against the generated default of `Overview` / `The Problem` / `Our Approach` / `Results` /
`Conclusion`. Skim the first set and you have the argument; skim the second and you know a post
exists.

Worth it above ~2,000 words. Not in reference docs, where readers scan for topic nouns. Full
method in `exemplars/06-modal-thesis-headings.md`.

### The pattern-comparison template (LangChain)

For any piece that compares approaches, repeat one three-part block per option:

> **How it works**: ...
> **Best for**: ...
> **Key tradeoff**: Adds one extra model call per interaction because results must flow back
> through the main agent. This overhead provides centralized control and context isolation, but
> costs latency and tokens.

Then a table quantifying the comparison. **Key tradeoff is the load-bearing field** and the one
most often omitted. A comparison without per-option costs is a feature list.

---

## Opening moves, measured

Across the AI-native corpus surveyed (11 posts), **claim-first opening dominates: 7 of 11**.
The post states its conclusion in the first sentence, before any scene-setting:

> We've worked with dozens of teams building LLM agents across industries. Consistently, the
> most successful implementations use simple, composable patterns rather than complex
> frameworks.

Credential, then claim, in two sentences. No hook, no question, no "In today's."

This is the safest default for technical content. The alternatives that also work in the sample:
flat definition plus concession (Fly.io), naming what a prior piece skipped (Tailscale), and
analogy-first (Dan Luu, high-risk, only when the analogy *is* the argument).

---

## Register-independent rules

These held across every source examined.

**Numbers carry their context.** Anthropic gives "206 tokens" against "72 tokens" for the *same
response in two formats*. A throughput figure without hardware, batch size, and workload shape
is a screenshot, not a fact. This is the single most common failure in AI-startup benchmark
posts.

**Name the identifier, not the category.** qmail, chroot, nsjail, Firecracker, `thread_ts`,
`nsjail`. Categories are unfalsifiable; names are checkable.

**Say what you gave up.** Fly.io's recommendation carries three explicit conditions. Anthropic
declines to name a best response format and says evaluation should decide. Anything presented as
free reads as marketing.

**Admit the failure with its specific detail.** Anthropic's account of Claude appending `2025` to
search queries is the most credible paragraph in that post, precisely because a marketing pass
would have cut it.

**Concede before complicating.** Fly.io: "we generally agree that it's a good, useful thing"
before the complication. This is more persuasive than manufacturing a contrarian frame.

**Let headings have voice where the format allows.** "Prelapsarian Containers", "Incarceration",
"NAT notes for nerds". The cheapest personality-per-word available, and the first thing a
generic pass replaces with "Background" and "Implementation."

**End on the unfinished work, not a synthesis.** The strongest closing in the surveyed corpus:
*"Finally, we've still got a lot of work to do — those RDMA networks don't configure
themselves!"* (Modal). Compare the weakest, which is a forward-looking restatement of the
thesis. Every register in this file ends on something concrete: a recommendation, an
acknowledgement, an open constraint. None end on a summary.

---

## Register is set by venue, not by organisation

The clearest correction the survey produced, and it overturns the intuitive rule.

**Google published the most personality-heavy post in the sample and the most marketing-driven
one within about two weeks of each other.** The Developers Blog post on elastic TPU training
uses no headings at all, admits a proxy-OOM bug, and signs off *"If you run the demo and it
breaks, let me know on LinkedIn or X. Happy training!"* The Cloud Blog post opens with a product
ad box and an unsourced statistic.

**Uber's two posts share a byte-identical skeleton across two unrelated teams**: Introduction →
numbered figures → named Impact section → Conclusion → Acknowledgments → trademark disclaimer →
author bios → Related Articles carousel. The surveying agent's read: the CMS shapes the voice
more than the individual author does.

Practical consequence: **do not pick a register by looking at whose logo is on the post.** Ask
what the publication venue tolerates. The same company will support a personal sign-off on one
property and require a product CTA on another.

This is the same finding as the authorship one in
`exemplars/08-personality-devices.md`, one level up. Genre beats authorship, and venue beats
both.

## Failure modes specific to vendor and startup blogs

Found in the AI-native survey. Watch for these in your own drafts, since they are the ones that
survive an anti-slop pass because the prose itself is clean.

**The unconditioned benchmark.** "Achieves ultra-low latency with custom speculative decoding."
No unit, no baseline, no hardware. A marketing adjective standing where a number should be.

**Lecturing on rigor you do not practise.** One surveyed post instructs readers to "design
domain-specific evaluation harnesses with clear quantitative metrics" and supplies no benchmark
of its own anywhere. If a piece tells the reader to measure, it measures.

**Objection-handling wearing a lab coat.** A "Common pitfalls" section where every pitfall
resolves to the author's own product in the same bullet. Real limitations sections leave at
least one item unsolved. See `../../anti-slop-writing/references/structural-patterns.md`.

**The launch-post exemption.** Announcement posts routinely skip tradeoffs entirely as a genre
default: every number moves in the author's favour, and there is no workload where the technique
does not help. Launching something is not a reason to drop the honesty bar.

**CMS scaffolding inside the article body.** Templated TL;DR boxes and product CTAs repeated
word-for-word across unrelated posts. Readable as marketing infrastructure rather than editorial
structure, and it costs credibility on the technical content around it.

**Copy-paste errors surviving to publication.** The surveyed corpus contained a
sentence naming the same product twice where two different products were meant, and an emoji
left in one heading of an otherwise formal post. Faster editorial cycles have a cost; a
read-aloud pass catches most of it.

**The mandatory Conclusion that eats your best ending.** A CMS-required Conclusion section
reliably becomes a restatement of the introduction, while the strongest available ending (a
number, a limitation, a decision) sits buried several sections earlier. If the format forces
one, put something *new* in it: a limitation, the next decision, an open question.

**The AI-generated summary block.** One surveyed post leads with an "AI-Generated Summary"
bullet list and the disclaimer *"AI-generated content may summarize information incompletely.
Verify important information"* above human-authored prose. This is a compliance artifact, not a
reading aid, and it signals to a technical reader that nobody was confident enough in the piece
to let it open itself.

---

## Provenance

Measurements computed from fetched post bodies on 2026-08-09. The four sources above were
verified directly. Additional findings from a broader survey of big-tech and AI-startup
engineering blogs are folded into the register descriptions and the register-independent rules;
where a claim rests on a single source it says so.

Word counts for the Anthropic post are approximate because its body was analysed qualitatively
rather than run through the same script.
