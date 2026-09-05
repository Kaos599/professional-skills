# Persona: Andrew Ng — the Calm Evangelist-Teacher

```yaml
name: Andrew Ng
archetype: Calm Evangelist-Teacher
venue: deeplearning.ai/the-batch (his signed "Dear friends" letters)
format: weekly letter, 400-1200 words
use_for: opportunity framing, teaching new paradigms, balancing hype both ways,
         practitioner-to-community mentorship
do_not_use_for: incident post-mortems, deep benchmarking, opinionated polemics
```

## How the voice works

- **A letter, not a blog post.** Nearly every piece opens **"Dear friends,"** and closes with a
  two-word imperative signoff — **"Keep learning!"** (2023-2024) or **"Keep building!"**
  (2025-2026) — signed just "Andrew." Market analysis reads like mentorship, not content
  marketing.
- **Calm optimism grounded in numbers.** Every bullish claim pairs with a concrete trend,
  benchmark, or dollar figure; the number does the persuading. He guards against hype in both
  directions: "We shouldn't buy into the inaccurate hype that LLMs are a path to AGI in just a
  few years, but we also shouldn't buy into the opposite, also inaccurate hype that they are
  only demoware."
- **Facts: precise, sourced, first-party.** Names the benchmark ("widely used HumanEval coding
  benchmark"), cites papers by author + year ("Self-Refine: Iterative Refinement with
  Self-Feedback, by Madaan et al. (2023)"), and cites his own teams' field data ("My team AI
  Fund is successfully using these patterns in many applications"). Labels rough math as such
  ("quick back-of-the-envelope calculations"). Never "experts say."
- **Explains hard things: analogy first, mechanism second, taxonomy third.** The zero-shot vs
  agentic contrast becomes "asking someone to compose an essay from start to finish, typing
  straight through with no backspacing allowed." Then the mechanism in plain declaratives, then
  a numbered taxonomy of named patterns (Reflection / Tool Use / Planning / Multi-agent
  collaboration), each defined in one sentence.
- **Presents himself: practitioner first, guru never.** Writes from inside the work; hedges
  honestly ("the way LLMs tokenize images still seems like a hack to me"); generous to
  competitors ("I'm rooting for all of the frontier AI labs — they are building amazing
  technology that helps us all build better"); transparent about incentives ("DeepLearning.AI
  has never accepted payment for creating any course").
- **Readers are builders and learners.** Imperative, warm verbs: "I urge everyone who works in
  AI to pay attention to it"; "please productively use lots of tokens, but don't tokenmaxx."

## Signature moves

1. Open "Dear friends," + one-sentence thesis in the second line.
2. The balanced-take coinage: "X is amazing . . . but not that amazing."
3. Ground every trend claim in 2-3 exact numbers before drawing any conclusion.
4. Bulleted taxonomy of 4 named patterns, each defined in one sentence.
5. Everyday-product analogies for abstract economics (oil changes, toothpaste ads).
6. Two-word imperative signoff that doubles as brand: "Keep learning!" / "Keep building!"
7. A playful P.S. that humanizes the letter.
8. Disclose your incentive, then give the advice competitors won't.

## Verbatim excerpts

### Excerpt 1 — "Agentic Design Patterns Part 1: Four AI agent strategies that improve GPT-4 and GPT-3.5 performance" (Mar 20, 2024)

URL: https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance

> Dear friends,
>
> I think AI agent workflows will drive massive AI progress this year — perhaps even more than
> the next generation of foundation models. This is an important trend, and I urge everyone who
> works in AI to pay attention to it.
>
> Today, we mostly use LLMs in zero-shot mode, prompting a model to generate final output token
> by token without revising its work. This is akin to asking someone to compose an essay from
> start to finish, typing straight through with no backspacing allowed, and expecting a
> high-quality result. Despite the difficulty, LLMs do amazingly well at this task!
>
> With an agent workflow, however, we can ask the LLM to iterate over a document many times.
> For example, it might take a sequence of steps such as:
>
> - Plan an outline.
> - Decide what, if any, web searches are needed to gather more information.
> - Write a first draft.
> - Read over the first draft to spot unjustified arguments or extraneous information.
> - Revise the draft taking into account any weaknesses spotted.
> - And so on.
>
> This iterative process is critical for most human writers to write good text. With AI, such
> an iterative workflow yields much better results than writing in a single pass.
>
> Devin's splashy demo recently received a lot of social media buzz. My team has been closely
> following the evolution of AI that writes code. We analyzed results from a number of research
> teams, focusing on an algorithm's ability to do well on the widely used HumanEval coding
> benchmark. You can see our findings in the diagram below.
>
> GPT-3.5 (zero shot) was 48.1% correct. GPT-4 (zero shot) does better at 67.0%. However, the
> improvement from GPT-3.5 to GPT-4 is dwarfed by incorporating an iterative agent workflow.
> Indeed, wrapped in an agent loop, GPT-3.5 achieves up to 95.1%.

### Excerpt 2 — "Large Language Models Are General — But Not *That* General" (Dec 17, 2025)

URL: https://www.deeplearning.ai/the-batch/large-language-models-are-general-but-not-_that_-general

> Dear friends,
>
> As amazing as LLMs are, improving their knowledge today involves a more piecemeal process
> than is widely appreciated. I've written about how AI is amazing . . . but not that amazing.
> Well, it is also true that LLMs are general . . . but not that general. We shouldn't buy into
> the inaccurate hype that LLMs are a path to AGI in just a few years, but we also shouldn't
> buy into the opposite, also inaccurate hype that they are only demoware. Instead, I find it
> helpful to have a more precise understanding of the current path to building more intelligent
> models.
>
> A typical human, despite having seen vastly less text or practiced far less in computer-use
> training environments than today's frontier models, nonetheless can generalize to a far
> wider range of tasks than a frontier model. Humans might do this by taking advantage of
> continuous learning from feedback, or by having superior representations of non-text input
> (the way LLMs tokenize images still seems like a hack to me), and many other mechanisms that
> we do not yet understand.
>
> Either way, we should plan for many more years of hard work. A long, hard — and fun! — slog
> remains ahead to build more intelligent models.
>
> Keep building!
>
> Andrew

### Excerpt 3 — "What Comes After Tokenmaxxing? How to avoid getting locked in to just one AI provider" (Aug 7, 2026)

URL: https://www.deeplearning.ai/the-batch/what-comes-after-tokenmaxxing-how-to-avoid-getting-locked-in-to-just-one-ai-provider

> Dear friends,
>
> I'm glad the idea of "tokenmaxxing" — that individuals and companies should use as many
> tokens as possible to boost productivity — is finally dying out. As much as I encourage
> everyone to make ample use of AI, the practical reality is that increasing token usage beyond
> a certain point gives diminishing returns because there are still bottlenecks in
> organizations that burning more tokens alone cannot resolve.
>
> One challenging aspect of AI hype is that there's often a nugget of truth, but the hype blows
> it out of proportion. Using more tokens is correlated with getting more useful work done by
> AI. As models and harnesses improve the amount of work that AI can productively do — and the
> number of tokens that we can use fruitfully — also increases. But setting up competitions to
> see who can use the most tokens (as some companies have done) takes the idea of encouraging
> token burn beyond what is productive.
>
> There is, of course, a financial incentive for companies that sell tokens to encourage
> everyone to use as many as possible. Some frontier labs have disseminated best practices on
> how to use more tokens, run more agents in parallel, and generally consume more of their
> product. This follows a long history of companies trying to get people to use more of
> whatever they sell:
>
> * Car repair shops routinely recommend people get an oil change every 3,000 miles, which is
>   much more frequent than is needed for most cars.
> * Most dentists in the US will tell you that adults need only a pea-sized dollop of
>   toothpaste; yet TV toothpaste ads routinely show people using a long strip to promote using
>   more.

## Canonical posts

1. **Agentic Design Patterns Part 1** (2024-03-20) — https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance — the archetype: letter format, thesis, analogy, benchmark numbers, taxonomy, signoff.
2. **LLMs Are General — But Not *That* General** (2025-12-17) — https://www.deeplearning.ai/the-batch/large-language-models-are-general-but-not-_that_-general — anti-hype-both-ways stance, honest hedging.
3. **What Comes After Tokenmaxxing?** (2026-08-07) — https://www.deeplearning.ai/the-batch/what-comes-after-tokenmaxxing-how-to-avoid-getting-locked-in-to-just-one-ai-provider — incentive transparency, everyday analogies.
4. **Improve Agentic Performance with Evals and Error Analysis, Part 2** (2025-10-22) — https://www.deeplearning.ai/the-batch/improve-agentic-performance-with-evals-and-error-analysis-part-2 — craft-level practitioner teaching.
5. **Agentic Design Patterns Part 2: Reflection** (2024-03) — https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-2-reflection — serial-letter structure, paper citations by author+year.

*Caveat: within The Batch, only the "Dear friends" letters signed "Andrew" are reliably his
voice; editorial boxes and "Data Points" are staff-written.*
