# Writing standard

What every post in a series obeys. Copy the parts you need into the series'
`SERIES_STANDARD.md` and adapt them to the author's voice signature. The examples below use
a running example series, "From log line to alert" (how monitoring turns raw logs into a
page someone acts on). Swap in your own domain. `examples/cold-opens.md` has more examples
across domains.

## 1. Reader and layers

Write for three readers at once, because the panel tests all three:
- **an engineer** who knows adjacent systems but not this domain, and can check every
  claim;
- **a decision-maker** (an engineering manager, a buyer, a head of product) who wants
  outcomes: delay, cost, reliability, buy vs build;
- **a non-engineer** (from a shared link) who came for the story.

**Two layers.** The main text tells the story in plain words. Protocol detail, flags, spec
section numbers, exact fractions and statistics go in `> **For engineers.**` asides placed
right after the section they belong to. A reader who skips every aside still gets the
argument. An engineer who reads them gets the mechanism.

A statistics-heavy paragraph is the most common point of conflict. The engineer trusts the
post more because of it, and the other two readers leave there. Keep a two-sentence plain
version in the body ("the numbers point that way, but the test was small and can't prove
it") and move the statistics into an aside.

Put the **consequence before the mechanism**. Write "our test queries read the wrong
minute of logs, so we were grading the detector on data it never saw", then explain chunk
boundaries.

Define the system's output, and say which direction is better ("lower is better"), before
the first number that depends on it.

## 2. Storytelling

- **Cold open.** A concrete scene any reader recognises, in the present tense, with
  stakes ("9:02 on the biggest sales morning of the year"). Then the one precise fact that
  makes it hard ("the payment service stops answering for four seconds. The dashboard
  scrapes every fifteen"). Frame the scene with "Picture…" so illustrative details are
  honestly illustrative.
- **Put a person in it.** "Somewhere a customer's card was declined at the last step." Then
  "someone has to notice", and the jobs in that person's terms. Then the clock: "the sale
  doesn't pause while that happens."
- **Specific beats stock.** A detail tied to the medium ("their cart emptied on refresh")
  lands. Generic life moments ("on a train, or putting a child to bed") read as stock.
  Lines that assume a feeling ("their family must be devastated") read as sentimental.
  Cut both.
- **Scale without a fact dump.** One number per source of scale, each tied back to the
  person ("every one of those requests is somebody waiting"). A paragraph of nine numbers
  is the failure readers notice first.
- **Carry the thread through the body.** Each incident needs a human beat: who was
  affected, what it cost, who noticed. The author's own notes are the strongest material.
  Quoting them at the turning point ("my notes kept saying the same thing: 'the alert
  fired after the customer did'") beats any paraphrase.
- **If the scene's domain isn't yours, say so early** ("I'll use online checkout because
  everyone has used it. Our data comes from logistics"). Return to the scene in the body
  and at the end ("the alert can reach the on-call engineer on time and still point at the
  wrong service").
- **Analogies from the reader's world**: an append-only log is like a shop's receipt roll,
  a stale cache is like a printed timetable nobody replaced, sampling is like a strobe
  light. Use at most three per post, each tied to a mechanism.

## 3. Voice (derive per author, then hold it)

Defaults that held up in review:
- "I" for the author's own views and decisions, "we" for team work. Never a royal "we".
- Two registers: an **essay** register for ideas (median about 10 words per sentence, short
  declaratives) and a **walkthrough** register for mechanisms (longer, more numbers).
- Contractions on. STE's no-contraction rule doesn't apply to narrative prose.
- One first-person opinion or decision per H2 ("I think the scrape interval is a product
  decision before it's a storage decision: it's the delay the customer feels.").
- Keep earned admissions ("So I can't prove the timeout is what users were reacting to").
- Never use: exclamation marks, an opening question, semicolons, em dashes (or any dash
  swapped in for one), emoji, mid-sentence bold, numbered lists in the bold-label-colon
  shape, placeholders, "subscribe" closers, summary recaps, or closing aphorisms with no
  mechanism behind them.
- "X, not Y" at most twice per post. It's the most model-characteristic shape.
  Near-variants ("A before B", "What X can catch is…") count toward the same family.
- At most one bold sentence per section, standing alone, stating a fact or a rule. The page
  renders a paragraph that is one bold sentence as a pull line.
- Say each rule once. A fix, then a lesson line, then a bold pull line saying the same
  thing within 120 words counts as an anti-slop pattern family.
- Vary the section endings. Several sections ending on "I now check…" lesson lines read as
  a template.
- Gloss domain words the first time (p99, cardinality, scrape interval), then use them
  plainly. Expand any acronym a non-engineer meets.

## 4. Post anatomy

1. Cold open (the first post of a series may run 5 paragraphs; later posts 2–4 sentences),
   plus a one-line **dek** under the title.
2. Series rail figure with this post's jobs lit, and one line on where we are.
3. 3 to 5 H2s, each a thesis sentence in sentence case. Reading only the H2s gives the
   argument.
4. Inside a section: industry or paper context → what we tried → what broke (number) → what
   we changed → result (number).
5. "What this does not solve" as its own H2, with a first-person view in it.
6. A decision rule: a numbered list the reader can apply.
7. Next post: **one** sentence.
8. Glossary table using the public names, then references with URLs.

Length: 1,800 to 2,600 words of main prose (`check_post.py` counts it), 4 to 7 figures.

## 5. Numbers and evidence honesty

- Every number carries its unit, scale and comparison: "detection delay 41 s (median, 30
  incidents) vs 95 s with the old rule".
- Give n in the sentence when n < 30. "One reviewer, N cases" goes where the parameter is
  introduced, not only in the glossary.
- **CIs**: if the interval includes zero, say so. Never write "mattered a lot" or "a clear
  gain" over it.
- **Selection**: a set picked because it failed will score better on any rerun (regression
  to the mean). Say so.
- **Rerun drift**: compare an effect with the same setup's rerun disagreement. A "clear"
  gain the same size as the baseline's own rerun drift is not yet a gain.
- **Confounds**: report a naive baseline that scores the same ("how busy the hour was
  predicts the outage as well as our metric does").
- **Two noise numbers** (per item vs on an average) each need their label, or they read as
  a contradiction.
- **Distributions, not means**, for thresholds and for any "chance" figure. A miss rate
  computed from the average event length understates misses whenever half the events are
  shorter than average.
- **Wording must match the source exactly**: "on one day" is not "at once", and "says it
  processes" is a vendor claim.
- **Production claims** (what is shipped, what config runs) need user clearance, and must
  say when a research result wasn't shipped.
- **Inferred mechanisms** are hedged ("on the library version we ran", "usually").
- **Public names only.** Keep a glossary that maps internal names to public names, and grep
  for the internal ones before every publish.

## 6. Anti-slop checklist (the gate is < 2 families)

Scan for these clusters:
- negative contrast and reframing pivots;
- repeated lesson-line endings;
- rule-of-three lists of near-synonyms (including the dek);
- uniform paragraph lengths, or runs of 3+ sentences of similar length;
- a fact dump without a person in it;
- unsourced authority ("vendors have done this for years", "teams staff war rooms");
- significance inflation;
- summary recaps;
- fake-profound kickers.

Fix content first (portability test: swap the company name, and if the sentence survives,
it's filler), then sentence shapes, then words.

## 7. Mechanical targets (`scripts/check_post.py`)

Sentences over 30 words: aim for fewer than 8, and keep the long ones for lists and
mechanisms. Paragraphs: at most 6 sentences. Captions: one sentence. The script exits 1 on
hard-rule failures (semicolons, em dashes, exclamation marks, an opening question,
mid-sentence bold, more than one bold per section, keep-out terms).
