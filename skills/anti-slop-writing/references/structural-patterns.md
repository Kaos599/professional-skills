# Structural patterns

The shapes. These survive model updates in a way vocabulary does not, so they carry more
diagnostic weight than any word list. Ordered roughly by corpus consensus.

Each entry gives the name, what it is, a bad example marked ✗, and the rewrite marked ✓.

---

## Sentence-level

### Negative contrast (the pivot)

The most model-characteristic sentence shape in the corpus. Setting up a point by first stating
what it is not.

✗ "It's not just a tool, it's a transformation."
✗ "The question isn't the model. It's the eval."
✗ "This isn't about speed. It's about correctness."
✓ State the positive directly: "The eval matters more than the model."

Keep the shape only when the reader genuinely holds the misconception and correcting it is the
point. Never invent a strawman to knock down. Use it once in a piece, never as the skeleton.

The family has a positive-framed variant that reads as friendly and is just as formulaic:

✗ "It's not just X, it's Y." · "not only X but also Y"
✗ "Observability isn't just about logs, it's about understanding."
✗ "This matters not just today but for years to come."
✓ State Y, drop the negation: "Understanding matters more than collection."

### Negative listing

✗ "Not a framework. Not a library. A runtime."
✓ Just say what it is.

### Participial pseudo-analysis

A trailing `-ing` clause that performs interpretation without adding information.

✗ "The launch adds file search, highlighting the team's commitment to better workflows."
✓ "The launch adds file search, so users can find old drafts without leaving the editor."

Watch: highlighting · underscoring · reflecting · showcasing · demonstrating · emphasizing ·
contributing to · paving the way for · setting the stage for

### Significance inflation

Telling the reader something matters instead of showing it.

✗ "The launch marks a pivotal moment for the company."
✓ "The launch is the company's first paid product."

Watch: stands as a testament · marks a pivotal moment · plays a vital role · solidifies its
position · underscores its significance · redefining what it means to · shaping the future of ·
left an indelible mark

### Copula avoidance

Dodging plain `is` and `has`.

✗ "The app serves as a centralized hub for sponsor management."
✓ "The app tracks sponsors, drafts, due dates, and approvals in one place."

### Colon reveal

Noun phrase, colon, dramatic lowercase payoff.

✗ "The detail that makes it work: a separate agent grades it."
✓ "A separate agent does the grading, which is what makes it work."

Colons are for lists, labels, and quotes. Not for manufactured drama.

### Weasel attribution

Authority with no name attached.

✗ "Experts agree that response time drives conversion."
✓ Name the study, the person, or the internal measurement. If there is none, delete the claim
or ask the author. Never invent a source.

### Hedge stacking

✗ "While this may vary, generally speaking, in most cases, it's worth noting that..."
✓ Collapse the stack to one hedge. Never to zero: if the claim genuinely needs qualification,
  one hedge stays.

The hedge rules elsewhere in this skill reconcile like this: stacked filler hedges collapse
(here), honest uncertainty hedges are protected no matter how they read (hard rules,
`preserving-voice.md` §2), and the 5% density cap in `detection-rubric.md` applies to filler
hedges, not meaning-bearing ones. The test is whether the hedge carries information the author
believed. "I don't know why this works" is evidence; "it may potentially perhaps be argued" is
padding.

### Hedging disguised as reassurance

Permission and shrugs inserted where a conclusion should be.

✗ "And that's okay." · "That's fine." (after every problem statement)
✗ "Not always. Not perfectly."
✓ Either take the position or leave the complication standing without absolving it.

### False agency

Inanimate abstractions doing human verbs, which conveniently removes the human who is
responsible.

✗ "A complaint becomes a fix within days." · "the data tells us" · "the market rewards clarity"
✓ Name the actor: "The on-call engineer fixes complaints within days." If no specific person or
team fits, address the reader: "you will ship faster". The pattern exists because it launders a
claim into a law of nature; restoring the actor restores both accountability and credibility.

### False balance

✗ "On one hand the cost is higher. On the other, the latency is lower."
✓ Take the position. Concede the real counterpoint in one clause.

### Fake-strong verbs

Reaching for an impressive verb when a plain one is clearer.

✗ "The integration significantly improves engineering productivity."
✓ "The integration cut review time from 30 minutes to 8."

### Synonym cycling (elegant variation)

Rotating terms for style.

✗ "The agent reviews the draft. The assistant scores the piece. The tool suggests fixes."
✓ "The agent reviews the draft, scores it, and suggests fixes."

One name for one thing. Repeat the clear word.

### Intensifier without evidence

"significantly", "dramatically", "substantially". If no number backs it, cut the adverb or
supply the number.

---

## Paragraph and section level

### Throat-clearing openers

"Here's the thing," "Let me be clear," "I'll be honest," "The uncomfortable truth is."
Cut and state the point. Keep a personal aside when it creates real context, tension, or
character.

Generalizes beyond the list: any "here's what/this/that [noun]" construction is throat-clearing
before the point. Cut it and state the point.

The casual-register variants count too: "One thing that bit me:", "Real talk:", "Okay so."
Remove the announcement, not just its formal tone; the formal and the folksy version are the
same tell in different clothes.

### Faux-insight setups

"What most people get wrong," "Here's what nobody tells you," "This is the part everyone skips."
These flatter the writer as lone expert.

✗ "The part everyone misses: distribution is the real moat."
✓ "Distribution is the moat."

### Fake-experience openers

"I've seen this play out," "I've seen it all the time," "I see this constantly."
Either name the specific instance or cut it.

### Rhetorical question openers

Including the one-word setup: "The reality?" "The result?" "The kicker?"
Convert to a declarative.

### Temporal openers

"In today's world," "In the ever-evolving landscape of," "As we navigate the complexities of."
Open with a specific fact, scene, or claim.

### Meta-commentary and self-narration of structure

"In this article we will discuss," "Let's break this down," "First, I'll cover..."
The reader can see the headings. Cut it.

### Interpretive metadiscourse

Stepping outside the subject to tell the reader how to read. "That last part matters more than
it sounds." "This distinction is key." "As you can see."
If the point is clear, delete. If it is not, add support instead of instruction.

### Rule of three

Reflex triads whether the content has three parts or not.

✗ "fast, reliable, and efficient" · "catalyst, partner, and foundation"
✓ Use two items or four. Check the count is real. Break the rhythm.

### Summary-recap endings

"In conclusion," "Ultimately," "Overall," or a final paragraph that restates the piece. The
reader was just there. End on the last concrete point, takeaway, or next action.

### Fake-profound kickers

The closing metaphor, aphorism, or mic-drop line. Delete it. Do not rewrite it into a better
metaphor and do not preserve the rhythm. End on the clearest concrete sentence already in the
draft. If it needs closure, add a plain takeaway.

The test that catches the whole species: if a line sounds like a pull-quote, rewrite it.
Writing engineered to be quotable is writing engineered to be pasted, and readers can tell.

### Leftover drafting artifacts

Reasoning scaffolding that survived into the final text because the model argued with itself
on the way to the draft and shipped both sides.

**Answering objections no one raised:**
✗ "This isn't mainly about cost." · "I'm not saying you should rewrite everything."
✓ If the objection is real in the reader's mind, address it directly. If it is not, the
  sentence is defending against an interlocutor who does not exist. Cut it.

**Rejecting fake alternatives:**
✗ "A tempting option would be to cache everything, but that has drawbacks."
✓ Either explain why caching is wrong for this case with specifics, or don't bring it up. The
  "tempting option" was never on the table; the sentence only performs deliberation.

### Vague declaratives

Sentences that announce importance, depth, or structure without showing any of it.

✗ "The reasons are structural." · "The implications are significant." · "The stakes are high."
✓ Name the specific reason, implication, or stake, or cut the sentence.

Generalizes: if a sentence says something is important, deep, or structural without showing the
thing, cut it or replace it with the specific thing.

### Formulaic challenges and outlook sections

"Despite challenges, X continues to thrive," "the future looks bright," a "Challenges and
Future Prospects" heading over empty content.

### Essayistic arc regardless of format

Contextualize, explore perspectives, add a qualification, close by noting what this "raises".
LinkedIn post or pricing memo, same shape. Match the arc to the format.

### Repeated callout patterns

"What this means for you:", "The takeaway:", "Why it matters:" appearing every section.
Merge into the prose.

---

## Rhythm

### Uniform sentence length

The strongest measurable structural tell. Flag when standard deviation is under ~4 words over a
100-sentence window, or when 3+ consecutive sentences fall within 5 words of each other.

✓ Mix 4-to-10-word sentences with 25-to-36-word ones. One corpus skill reports human baseline as
mean 18.3 words, median 15, standard deviation 15.3, with ~11% of sentences being fragments
under 5 words.

### Mechanical burstiness

The over-correction. Forcing abrupt fragments between long sentences to fake variation. Stacked
punchy one-liners are their own tell. Vary based on meaning, not on a target statistic.

### Uniform paragraph length

Every paragraph 4 to 6 sentences.

✓ Let some run one sentence and others run six. Weight sections asymmetrically: important parts
get space, standard parts compress, empty parts disappear.

### Sentence-opener repetition

If more than half the sentences in a paragraph start with The / This / It / In, rewrite the
openers.

### Transition on every paragraph

✓ Cut roughly half. Often no transition is needed, so just start the next thought. Let paragraph
breaks do the transitional work.

### Parataxis

Three or more short declaratives in a row with no connective. Merge or connect them, unless the
staccato is the author's real voice.

### Identical section anatomy

Every section following setup, explanation, conclusion. Identical paragraph counts. Every
section closing with a neat takeaway.

✓ Let some sections end abruptly. Not everything needs a bow.

---

## Content-level

### Abstraction where a fact belongs

The highest-frequency failure in the corpus.

✗ "The integration improved efficiency."
✓ "The integration cut deploy time from 40 minutes to 4."

One skill sets a hard floor: every paragraph describing a practice, cost, or restriction must
contain at least one number, dollar amount, named thing, or measurable quantity.

### The portability test

Swap the company, person, product, and country. If the sentence survives unchanged, it is
filler. Replace with something specific to this subject or cut it.

Variant, the three-product swap: could three unrelated products use this line unchanged?

### Category instead of identifier

"copyright law" when you mean 17 U.S.C. §1201. "software updates" when you mean over-the-air
firmware pushes. The specific name is stronger.

### Temporal vagueness

"in recent years", "recently" with no date.

### False ranges

"From X to Y" where X and Y are not on any meaningful scale between them.

✗ "We handle everything from billing to developer experience."
✓ List the actual scope, or pick the two ends that matter and say why they are the ends.

Real ranges survive the check: "from 40 minutes to 4" has numbers on a scale; "from startups to
enterprises" is at least a size axis. The tell is breadth inflation: a range that exists to make
the subject look comprehensive rather than to locate anything.

### Generic examples

Hypothetical or abstract rather than drawn from real experience.

### Novelty inflation

Treating an applied idea as an invention, or coining an undefined term and then reusing it as if
the reader knows it.

### Knowledge-cutoff hedging

"While specific details are limited," "as of my last update." Delete or find the source.

### Objection-handling disguised as candour

A "Common pitfalls", "Limitations", or "Challenges" section where **every** item is immediately
paired with the author's own solution. It has the shape of honesty and the function of a sales
script.

✗ "Pitfall: fine-tuning can overfit on small datasets. Mitigation: our platform's automatic
early stopping prevents this."
✓ Name at least one limitation you have not solved, or cut the section.

**The test:** does any item in the limitations section remain unresolved by the end of the
piece? If every one resolves to the author's product, it is marketing wearing a lab coat.

Compare real candour, which names a specific failed attempt and does not rescue it: *"We also
tried SmoothQuant to quantize all components of a given LLM into INT8, but found that it
degraded model output quality to unacceptable levels for this model and use case."*
(Baseten, FP8 quantization post.)

Related and worse: a piece that **lectures on rigor it does not practise**. One surveyed post
instructs readers to "design domain-specific evaluation harnesses with clear quantitative
metrics" while supplying no benchmark of its own anywhere in the piece.

### Benchmark without conditions

A throughput, latency, or accuracy claim with no hardware, batch size, sequence shape, or
baseline attached. Common in vendor engineering posts and near-universal in generated technical
copy, because the model has the shape of a benchmark sentence without the measurement.

✗ "Achieves ultra-low latency with custom speculative decoding."
✗ "33% faster inference."
✓ "By quantizing Mistral 7B to FP8 we observed a 33% improvement in output tokens per second vs
FP16, both using TensorRT-LLM on an H100, at a batch size of 32 max requests and a sequence
shape of 80 input / 100 output tokens per request."

A number without its conditions is not a fact. It is a screenshot. Flag it, and if the author
cannot supply the conditions, cut the number rather than softening it.
