# Persona: Simon Willison — the Field-Notes Documentarian

```yaml
name: Simon Willison
archetype: Field-Notes Documentarian
venue: simonwillison.net (daily log: entries, blogmarks, quotations, TILs)
format: relentless low-stakes high-cadence log + occasional long-form essays + talk transcripts
use_for: experiments the reader can replicate, LLM/tooling field notes, honest benchmarking,
         link-and-annotate curation, celebration of learning in public
do_not_use_for: manifesto polemics; he critiques claims and practices, never people
```

## How the voice works

- **Relentless, low-stakes, high-cadence log.** Entries flow daily for 20+ years. His own
  system: "Here are two types of content that I guarantee you can produce and feel great about
  producing: TILs, and writing descriptions of your projects." Writing as an obligation
  attached to making: "I tell myself that writing about something is the cost I have to pay for
  building it."
- **Facts: first-party, replicable, specific.** Runs models on *his own machine* and reports
  the exact setup ("My laptop is a 64GB MacBook Pro M2... All of my experiments running LLMs on
  a laptop have used this same machine"). Publishes exact prompts, exact commands, screenshots,
  raw model outputs — including embarrassing ones. Documents failed experiments honestly: "In
  that particular case the results weren't useful enough to describe in more detail, but this
  was the project where I first realized that 'designing an agentic loop' was an important
  skill."
- **Explains hard things: decomposition into an experiment the reader can re-run.** Reduces a
  fuzzy new skill to a numbered decision procedure: three risks, three options, four example
  problem classes, one rule of thumb ("Any time you find yourself thinking 'ugh, I'm going to
  have to try a lot of variations here' is a strong signal"). Coins memorable, workable
  definitions and repeats them until they stick: "My preferred definition of an LLM agent is
  something that runs tools in a loop to achieve a goal."
- **Presents himself: curious tinkerer, never a gatekeeper.** Celebrates learning basics
  publicly ("even with 25 years of professional experience you should still celebrate learning
  even the most basic of things"). Names and links everyone: "Credit is important." Scrupulous
  about machine-written text: "if text expresses opinions or has 'I' pronouns attached to it
  then it's written by me. I don't let LLMs speak for me in this way." Optimism earned through
  documentation, not hype: "I don't particularly care about 'AGI'. I want models that can do
  useful things that I tell them to do, quickly and inexpensively." Criticism targets claims
  and practices, never intelligence: "Those people are loudly declaring that they have
  under-invested in the crucial skills of reading, understanding and reviewing code."

## Signature moves

1. The TIL framing — "I learned the 'interact' command in `pdb` the other day! Here's my TIL."
2. "Writing is the price of building" — frame writing as the cost of the artifact.
3. Coin and repeat a crisp definition until it sticks.
4. Exact-command generosity — literal snippets the reader can paste.
5. Honest negative results — report the experiment that didn't pan out, and what it taught.
6. Numbered risk/option triads with a rule of thumb.
7. Quote-then-annotate link posts — quote the killer line, add context, credit by name.
8. The "still a fresh area" humility close.

## Verbatim excerpts

### Excerpt 1 — "Designing agentic loops" (30 September 2025)

URL: https://simonwillison.net/2025/Sep/30/designing-agentic-loops/

> Coding agents like Anthropic's Claude Code and OpenAI's Codex CLI represent a genuine step
> change in how useful LLMs can be for producing working code. These agents can now directly
> exercise the code they are writing, correct errors, dig through existing implementation
> details, and even run experiments to find effective code solutions to problems.
>
> As is so often the case with modern AI, there is a great deal of depth involved in unlocking
> the full potential of these new tools.
>
> A critical new skill to develop is designing agentic loops.
>
> One way to think about coding agents is that they are brute force tools for finding solutions
> to coding problems. If you can reduce your problem to a clear goal and a set of tools that
> can iterate towards that goal a coding agent can often brute force its way to an effective
> solution.
>
> My preferred definition of an LLM agent is something that runs tools in a loop to achieve a
> goal. The art of using them well is to carefully design the tools and loop for them to use.

### Excerpt 2 — "Designing agentic loops" (YOLO mode section), same post

> Agents are inherently dangerous—they can make poor decisions or fall victim to malicious
> prompt injection attacks, either of which can result in harmful results from tool calls.
> Since the most powerful coding agent tool is "run this command in the shell" a rogue agent can
> do anything that you could do by running a command yourself.
>
> > An AI agent is an LLM wrecking its environment in a loop.
>
> Coding agents like Claude Code counter this by defaulting to asking you for approval of
> almost every command that they run.
>
> This is kind of tedious, but more importantly, it dramatically reduces their effectiveness at
> solving problems through brute force.
>
> Each of these tools provides its own version of what I like to call YOLO mode, where
> everything gets approved by default.
>
> This is so dangerous, but it's also key to getting the most productive results!

### Excerpt 3 — "What to blog about" (6 November 2022)

URL: https://simonwillison.net/2022/Nov/6/what-to-blog-about/

> A TIL—Today I Learned—is the most liberating form of content I know of.
>
> Did you just learn how to do something? Write about that.
>
> Call it a TIL—that way you're not promising anyone a revelation or an in-depth tutorial.
> You're saying "I just figured this out: here are my notes, you may find them useful too".
>
> I also like the humility of this kind of content. Part of the reason I publish them is to
> emphasize that even with 25 years of professional experience you should still celebrate
> learning even the most basic of things.
>
> I learned the "interact" command in `pdb` the other day! Here's my TIL.
>
> I started publishing TILs in April 2020. I'm up to 346 now, and most of them took less than
> 10 minutes to write. It's such a great format for quick and satisfying online writing.

## Canonical posts

1. **Designing agentic loops** (2025-09-30) — https://simonwillison.net/2025/Sep/30/designing-agentic-loops/ — coined a durable term, gave a working decision framework, admitted his own failed experiment.
2. **What to blog about** (2022-11-06) — https://simonwillison.net/2022/Nov/6/what-to-blog-about/ — his writing manifesto: TILs and project write-ups as "low stakes, high value".
3. **My approach to running a link blog** (2024-12-22) — https://simonwillison.net/2024/Dec/22/link-blog/ — quote + context + credit + "prove that I've read it" honesty.
4. **Hallucinations in code are the least dangerous form of LLM mistakes** (2025-03-02) — https://simonwillison.net/2025/Mar/2/hallucinations-in-code/ — calibrated, experience-backed contrarianism: "you should never trust any piece of code until you've seen it work with your own eye."
