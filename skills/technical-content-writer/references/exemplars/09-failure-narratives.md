---
source:    https://www.uber.com/us/en/blog/solving-multiple-knapsack/ and https://www.uber.com/us/en/blog/scaling-real-time-traffic/
author:    Uber Engineering (Tarot and DeepETT teams)
authored:  false
format:    engineering blog
added:     2026-08-09
notes:     |
  How to write the part where it did not work. Three moves: the abandoned approach with
  its breaking number, the unexpected regression, and the scope decision stated as a
  refusal. This is the most transferable thing in the big-tech survey.
---

## Why this one

Most posts describe a system that works. The credible ones describe the version that did not,
and say why. These two posts contain the strongest failure narratives in the surveyed corpus,
and the moves are copyable directly.

---

## Move 1: the abandoned approach, with the number that killed it

> Initially, we modeled the incentive allocation challenge as a pure LP (Linear Programming)
> problem... For small batches, it worked beautifully. But as we ramped up traffic, the
> complexity curve hit us hard... It began taking more than 24 hours just to find a feasible
> solution for a relatively small user set.

Then the resolution, with the same measurement on both sides:

> The same dataset of 100,000 users that choked the LP solver for over 24 hours was solved by
> CP-SAT in a matter of minutes.

**The structure:** name the approach → say where it worked → name the breaking point with a
number → name the replacement → give the same measurement for both.

"For small batches, it worked beautifully" is doing real work. Without it the abandoned approach
looks stupid, and a reader in the small-batch case is misled into abandoning something that
would have been fine for them.

## Move 2: the result you did not expect

> When we retrained these downstream models using our new traffic forecasts, we observed a
> decrease in final arrival time accuracy. This was **highly unexpected**, given the increased
> resolution of our traffic forecasts...

An improvement to an input made the output worse. Reporting this costs nothing to omit and
almost every post omits it. It is the single most credible sentence in either piece, because no
marketing pass would have left it in.

**Rule:** if a change had a counter-intuitive effect, that is the most interesting thing you
learned. Lead the section with it.

## Move 3: the scope decision, stated as a refusal

> In theory, that's appealing. In practice, Uber's routing stack is already mature and heavily
> optimized. Rebuilding (or differentiating through) routing would have dramatically expanded
> the project scope and risk. So we chose a simpler boundary.

Four sentences: the appealing option, why it was not taken, what it would have cost, the choice.
No hedging and no apology.

**Rule:** every project refused something. Naming the refusal and its cost is more informative
than the feature list, and it inoculates against the obvious "why didn't you just..." reply.

---

## What the same posts get wrong

Both are shaped by a CMS template that is identical across two unrelated teams: Introduction →
numbered figures → named Impact section → **Conclusion** → Acknowledgments → trademark
disclaimer → author bios → Related Articles carousel.

The mandatory Conclusion is the casualty. Tarot's close restates the introduction's framing
almost verbatim:

> For the engineering community, the key takeaway is the power of hybridizing uplift modeling
> with constraint programming (CP-SAT) and feedback loops like budget pacing.

The reader was just there. The strongest available ending was the LP-to-CP-SAT number, and the
template buried it several sections earlier.

**Lesson:** a required Conclusion section will eat your best ending. If the format forces one,
put something new in it (a limitation, a next decision, an open question) rather than a recap.

---

## What to copy

- The abandoned approach with its breaking number, and where it *did* work.
- The counter-intuitive result, led with rather than buried.
- The scope refusal: appealing option, why not, what it would have cost, the choice.
- Measurements stated the same way on both sides of a before/after.

## What not to copy

- The mandatory Conclusion that restates the introduction.
- Template-uniform structure across authors. The survey found the CMS shaping voice more than
  the individual author did, across two unrelated teams.
