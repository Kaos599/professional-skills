# Structure playbooks

Format mechanics with the hard numbers, plus the archetypes that fit technical material.
Numbers are corpus consensus across 55 writing-craft skills; where skills disagree, the split
is shown.

---

## LinkedIn

The most-covered format in the corpus and the one with the firmest numbers.

| Element | Value | Consensus |
|---|---|---|
| Hard character limit | 3,000 | unanimous |
| Optimal length | 1,300 to 1,600 characters | 2 skills; a third says 1,500 to 2,500 |
| "See more" fold | ~150 to 210 characters | skills quote 150, 210, and 210–235 |
| Hook | first 2 to 3 lines | unanimous |
| Paragraph length | 1 to 3 lines | unanimous |
| Hashtags | 3 to 5, at the very end, after a line break | 2 skills |
| Longer than 3,000 chars | make it an article, not a post | 2 skills |

**Treat the fold as ~150 characters, not 210.** Mobile truncates earlier than desktop and the
corpus figures disagree. Writing to the tighter number is safe in both.

**Everything above the fold must stand alone as a complete statement.** Not a teaser, not half
a sentence. If the reader never clicks "see more", the visible part should still have told them
something true.

Structure that works for technical posts:

```
Line 1        the claim, complete, under 150 chars
Line 2        the mechanism or the counter-intuitive part
[blank]
body          short paragraphs, 1–3 lines, whitespace between every thought
[blank]
close         the rule or the decision, not a summary
[blank]
hashtags      3–5, after a line break
```

**Reveal ~80%, hold ~20%.** Give away the result and the subject; hold back some of the *how*.
Giving away everything removes the reason to read the body. Holding back the result is
clickbait, which technical audiences punish.

Other corpus notes: post a summary of why a link matters rather than dropping a bare URL;
reply to early comments promptly; do not tag people who did not ask to be tagged; do not stuff
hashtags for reach.

---

## Blog and long-form

- **Short paragraphs, 2 to 4 sentences** for web reading.
- **Vary section lengths deliberately.** Important sections get space; standard sections
  compress; empty sections get deleted. Uniform section length is a slop tell.
- **Tables when the same shape repeats 3+ times with the same fields.** Prose otherwise.
- **Prose carries argument; lists carry parallel items.** If the items are not genuinely
  parallel, write sentences.
- **Prose-then-list**, not list-then-prose. Introduce in a sentence, then enumerate.
- Headings answer reader questions: "How to size a GPU for decode" beats "Sizing — general."
- Sentence case headings.
- One H1.
- Corpus SEO figures, for what they are worth: reading grade 7 to 9; primary keyword in H1 and
  first 100 words; keyword density 0.5 to 1.5%; meta description 150 to 160 characters; slug
  3 to 6 words, no dates. Apply only when the piece is genuinely search-targeted. Do not let
  keyword placement bend a technical explanation.

---

## Newsletter

- Subject line is the headline; preview text (~first 90 characters) is the subhead. Together
  they set open rate. The preview should complement the subject, not repeat it.
- Subject lines declarative and specific. Newsletters live on trust, so clickbait costs more
  than it earns.
- **One primary CTA**, in the final paragraph or a P.S. Restraint is rewarded.
- Pull quotes render reliably as styled blockquotes across clients.

---

## Thread

- Each unit must stand alone and also advance the argument.
- No "1/" numbering unless the platform convention requires it.
- The last unit is the payload, not a recap.

---

## Archetypes for technical content

Use these instead of persuasion frameworks. Each maps to a real shape technical writing takes.

**Myth → mechanism → decision rule**
Name what people believe. Explain the mechanism that makes it wrong. End with the rule that
follows. *This is the shape of `exemplars/01-inference-stack.md`.*

**Incident → diagnosis → generalization**
What broke. What actually caused it, with the trace. What class of system has this problem.

**Benchmark → surprise → explanation**
The number nobody expected. Why it happened. What it means for a choice the reader faces.

**Decision → tradeoff map → recommendation**
The choice. Each option with what it costs, honestly. What you would pick and under what
conditions. Never present an option as free.

**Build log → what broke → what I would do differently**
Chronological, with the mistakes left in. The mistakes are the value.

---

## Persuasion frameworks

Corpus consensus for marketing copy. Included for completeness. **Usually the wrong tool for
technical content.** Applying PAS to an engineering post produces the manufactured-pain opener
that technical readers filter on sight. Use one only when the piece genuinely sells something.

| Framework | Expansion | Use when |
|---|---|---|
| **PAS** | Problem → Agitate → Solution | most-cited in the corpus; reader already feels the pain |
| **BAB** | Before → After → Bridge | transformation is the point |
| **AIDA** | Attention → Interest → Desire → Action | cold audience, full funnel in one piece |
| **StoryBrand** | reader is hero, brand is guide | brand narrative, positioning |
| **4Ps** | Promise → Picture → Proof → Push | landing pages |

If you use one, the voice signature still wins where they conflict.

---

## Hooks

Techniques the corpus endorses, with the constraint that in technical writing the hook must
also be **true and checkable**.

- **The claim, stated flat.** Often the strongest option. "VRAM tells you what fits, not how
  fast the model runs."
- **The specific number.** "We cut p99 auth latency from 500ms to 45ms by not checking tokens."
- **The concrete artifact.** "This is what 3,982 commits in 14 days looks like."
- **The correction.** "Most people size GPUs by VRAM. That measures the wrong thing."
- **The unexpected specificity.** "The meeting that changed the architecture lasted 4 minutes."

Banned as openers, by heavy corpus consensus and by the anti-slop gate:

`In today's [anything]` · `Imagine a world where` · `Picture this:` · `What if I told you` ·
`Buckle up` · `Let's dive in` · `Unlock the power of` · `Unpopular opinion:` ·
`Whether you're a [X] or a [Y]` · `Most people think X. The reality is Y.` ·
`Excited to share` · any rhetorical question · three rhetorical questions in a row

Note the last banned item is the *symmetric two-clause hook*. It works once. Used as a default
it becomes a fingerprint, and the corpus flags it as saturating.
