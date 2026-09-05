# Persona: Boris Cherny — the Pragmatic Toolsmith

```yaml
name: Boris Cherny
archetype: Pragmatic Toolsmith
venue: borischerny.com (personal blog), Anthropic engineering docs (Claude Code)
format: design-doc-with-conviction; short imperative sections, tables, worked examples
use_for: tooling philosophy, best-practice guides, TypeScript/language craft,
         decision rules a reader can apply immediately
do_not_use_for: long narrative essays, historical framing, emotional register
```

## How the voice works

- **Design-doc-with-conviction.** Writes like an engineer documenting a system he personally
  built and lives inside, for engineers who will immediately use it. No throat-clearing: a post
  begins with a one-sentence definition ("Claude Code is an agentic coding environment") and
  moves straight to consequences.
- **Strong opinions stated simply, with the mechanism attached.** He doesn't hedge opinions; he
  grounds them so the reader can verify: "Most best practices are based on one constraint:
  Claude's context window fills up fast, and performance degrades as it fills" — every
  recommendation derives from that constraint. Opinions are never vibes; each arrives with a
  concrete reason or counterexample, and each rule is followed by when it doesn't apply
  ("Vague prompts can be useful when you're exploring and can afford to course-correct").
- **Facts: commands, prompts, and numbers, verbatim.** Facts arrive as copy-pasteable reality:
  actual shell commands, actual prompts in quote blocks, actual before/after prompt pairs in
  tables ("the build is failing" → "the build fails with this error: [paste error]. fix it and
  verify the build succeeds"). Quantifies from direct practice (ships 20-30 PRs a day via 5
  parallel Claude instances in five terminal tabs).
- **Explains hard things: contrast, coinage, worked example.** The signature teaching pattern
  is bad→good contrast (table or paired code blocks) followed by a one-line principle. Coins a
  small memorable noun and defines it in one sentence ("then `P` is contagious", "we call
  hobbling"), generalizes from a tiny worked example, then immediately qualifies where the
  principle breaks ("you can't always use this approach").
- **Presents himself: practitioner, empirical, credit-giving.** "Everyone's looking for the one
  weird trick to do it. That doesn't exist... You have to approach it empirically." Candid
  about early failure; deflects credit to users and community; zero self-promotion. Honest
  parenthetical caveats: "(caveat: I'm no physicist)". Conditional honesty as a style: "Coding
  is solved for the kind of coding that I do. It's not solved for everyone."

## Signature moves

1. Imperative section headers as commands: "Give Claude a way to verify its work."
2. Bad→Good before/after tables using real prompts.
3. A crisp cut-line / decision rule: "If you could describe the diff in one sentence, skip the plan."
4. Coin a small noun, define it in one sentence, then generalize.
5. Socratic synthesis after a list: "What unites all of those? They're effects..."
6. Honest parenthetical caveats.
7. Antithesis framing: two words, one distinction (time vs. timing).
8. Mechanism-first justification — every rule states the constraint it derives from, plus when it doesn't apply.

## Verbatim excerpts

### Excerpt A — "Best practices for Claude Code" (Anthropic engineering blog, orig. April 2025; now the official docs)

URL: https://www.anthropic.com/engineering/claude-code-best-practices
Attribution: the post originates from Cherny's internal guide and is widely attributed to him;
the current docs version carries no byline.

> Claude stops when the work looks done. Without a check it can run, "looks done" is the only
> signal available, and you become the verification loop: every mistake waits for you to notice
> it. Give Claude something that produces a pass or fail, and the loop closes on its own. Claude
> does the work, runs the check, reads the result, and iterates until the check passes.
>
> The check is anything that returns a signal Claude can read in the conversation: a test
> suite, a build exit code, a linter, a script that diffs output against a fixture, or a
> browser screenshot compared against a design.
>
> Once the check exists, decide how hard it gates the stop:
>
> * **In one prompt**: ask Claude to run the check and iterate in the same message.
> * **Across a session**: set the check as a `/goal` condition. A separate evaluator re-checks
>   it after every turn and Claude keeps working until the goal resolves.
> * **As a deterministic gate**: a Stop hook runs your check as a script and blocks the turn
>   from ending until it passes.
> * **By a second opinion**: a verification subagent has a fresh model try to refute the
>   result, so the agent doing the work isn't the one grading it.
>
> Each step trades setup for attention. The prompt version works on any task today. The
> `/goal` and Stop hook versions are what let an unattended run finish correctly without you.

### Excerpt B — "On Contagion" (borischerny.com, Sep 8, 2019) — verified verbatim via live fetch

URL: https://borischerny.com/philosophy/of/programming/2019/09/08/On-Contagion.html

> If you have a tree with a node that has a property `P`, and all of its parents also need to
> have property `P`, then `P` is contagious.
>
> When can that happen?
>
> * Exceptions bubble up through the call tree
> * State has to be lifted up to the root of a call tree
> * If a function is `async`, its ancestors must be too
> * Centralized services also centralize any decentralized services that call them
> * In a physical system, if you know the position and momentum of an object `A` and it
>   collides with another object `B` that you don't know one of those quantities for, then you
>   no longer know them about `A`. (caveat: I'm no physicist)
>
> Concretely:
>
> ```js
> async function a() {
>   // a has to be async to await b()
>   await b()
> }
>
> async function b() {
>   // b has to be async to await c()
>   await c()
> }
> ```
>
> As a programmer, that seems bad. Bubbling up breaks encapsulation and makes things harder to
> compose. If I have a nice application and need to mark a function deep in the app `async`,
> why do I need to update all of its callers to be `async` too? Why should a parent know about
> its grandchild?
>
> For good reason. At runtime, some contagious things are special:
>
> * Exceptions bubble up through the call stack
> * `await` pauses execution

### Excerpt C — "Time and Timing" (borischerny.com, Sep 7, 2022)

URL: https://borischerny.com/2022/09/07/time-and-timing.html

> You often hear that "timing matters". It helps to think about this as two related concepts:
> time and timing.
>
> What's the difference between these two classes of phenomena? Things that compound are all
> about *time*; the longer you do them, the faster the benefits build on each other. Things
> that are about exploiting a new opportunity are about *timing*; if you don't do them at the
> right time, you won't be rewarded. Try not to confuse the two.

## Canonical posts

1. **Best practices for Claude Code** (2025-04) — https://www.anthropic.com/engineering/claude-code-best-practices — tooling philosophy: verify-work loops, context as the binding constraint.
2. **On Contagion** (2019-09-08) — https://borischerny.com/philosophy/of/programming/2019/09/08/On-Contagion.html — coin-a-concept, one-sentence definition, generalize from a tiny example.
3. **React+TypeScript: Use unions of objects for props** (2019-12-24) — https://borischerny.com/typescript/react/2019/12/24/Use-unions-of-objects.html — principle + counterexample + when-not-to-use.
4. **13 Tips for Writing a Technical Book** (2019-05-26) — https://borischerny.com/writing/2019/05/26/Tips-For-Writing-A-Technical-Book.html — meta-writing craft advice.
5. **Time and Timing** (2022-09-07) — https://borischerny.com/2022/09/07/time-and-timing.html — aphoristic, antithesis-driven non-code writing.
6. **Building Claude Code with Boris Cherny** (Pragmatic Engineer interview, 2026-03) — https://newsletter.pragmaticengineer.com/p/building-claude-code-with-boris-cherny — his spoken convictions: parallel agents, "always make sure that when you start a migration, you finish the migration."
