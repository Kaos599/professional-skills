---
source:    https://www.anthropic.com/engineering/writing-tools-for-agents
author:    Ken Aizawa, Anthropic Engineering
authored:  false
format:    engineering blog
added:     2026-08-09
notes:     |
  The reference implementation of "company engineering blog that is actually useful."
  Copy the structure and the instead-of-X-consider-Y move. Do not copy the "we" voice
  for personal writing.
---

## Why this one

It does the hardest thing in company technical writing: gives specific, checkable, opinionated
advice while writing in first-person plural for a corporate blog. Most company blogs pick
either specificity or institutional voice and lose the other.

## Verbatim excerpts

**Opening (after the dek):**

> The Model Context Protocol (MCP) can empower LLM agents with potentially hundreds of tools to
> solve real-world tasks. But how do we make those tools maximally effective?

**A concrete recommendation, stated as a substitution:**

> Instead of implementing a `list_users`, `list_events`, and `create_event` tools, consider
> implementing a `schedule_event` tool which finds availability and schedules an event.

**Admitting their own product's failure, with the specific detail:**

> When we launched Claude's web search tool, we identified that Claude was needlessly appending
> `2025` to the tool's `query` parameter, biasing search results and degrading performance (we
> steered Claude in the right direction by improving the tool description).

**Refusing to over-claim:**

> Even your tool response structure—for example XML, JSON, or Markdown—can have an impact on
> evaluation performance: there is no one-size-fits-all solution.

**Closing:**

> With a systematic, evaluation-driven approach to improving tools for agents, we can ensure
> that as agents become more capable, the tools they use will evolve alongside them.

## Signature

**Opening move.** Context sentence, then a question that the post answers. Notably it does NOT
open with "In today's rapidly evolving AI landscape." It names the protocol, states what it
enables, asks the operative question.

**Structure.** Two-act. Act one is procedural (`How to write tools` → prototype → evaluation →
collaborate). Act two is principles (`Principles for writing effective tools` with five named
sub-principles). The post announces this split up front with a bulleted preview of both acts.
That preview is doing real work: it lets a reader skip to act two.

**The signature move: "Instead of X, consider Y."** Repeated throughout with concrete names.
Not "design tools thoughtfully" but three worked substitutions with actual function names. This
is the single most copyable thing in the post.

**Numbers always carry their context.** "206 tokens" vs "72 tokens" for the same response in two
formats. "We restrict tool responses to 25,000 tokens by default." "~⅓ of the tokens." Every
figure names what was measured.

**Self-criticism as evidence.** The `2025` search-query bug is the most credible paragraph in
the post, because a marketing pass would have cut it.

**Hedging is honest and specific.** "Effects vary by LLM and we encourage you to choose a naming
scheme according to your own evaluations." They decline to give a universal answer where they do
not have one, and say why.

**Voice.** First-person plural throughout, second person for instructions ("Start by standing up
a quick prototype"). No humour. Formal but not stiff. Contractions are rare.

**Closing.** Forward-looking synthesis. This is the weakest part of the post and the most
corporate. It restates the thesis rather than ending on the last concrete point.

## What to copy

- The two-act split, announced up front, so readers can skip.
- "Instead of X, consider Y" with real names.
- Numbers with their measurement context attached, every time.
- Naming your own failure with the specific detail.
- Declining to give a universal answer where evaluation should decide.

## What not to copy

- The forward-looking closing paragraph. It is the summary-recap pattern that
  `anti-slop-writing` flags, and the post would be stronger ending on the principles.
- The corporate "we" if the piece is personal. It flattens individual judgment into
  institutional consensus.
