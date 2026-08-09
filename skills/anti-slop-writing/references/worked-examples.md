# Worked examples

Four end-to-end passes. All drafts here are synthetic, written to demonstrate the mechanics.
None are quoted from a real author.

Read at least Example 3 before your first pass. It is the one most likely to be skipped and the
one that prevents the most damage.

---

## Example 1: standard generated draft, medium dose

### Before

> In today's fast-paced engineering landscape, observability has become absolutely crucial for
> modern teams. It's not just about collecting logs — it's about understanding your systems at a
> fundamental level.
>
> When it comes to implementing observability, there are three key pillars: metrics, logs, and
> traces. Each plays a vital role in helping teams navigate the complexities of distributed
> systems. Studies show that teams with mature observability practices resolve incidents
> significantly faster.
>
> Our team recently embarked on a journey to revamp our observability stack. The results were
> transformative, highlighting the importance of investing in robust tooling.
>
> In conclusion, observability isn't a luxury — it's a necessity. The teams that thrive will be
> the ones that see clearly.

### Mechanical scan

| Check | Result |
|---|---|
| Em dashes | 3 in 118 words. Budget for a blog is 1 per 500. **Fail** |
| Specificity floor | 0 numbers, 0 named tools, 0 dates in 4 paragraphs. **Fail** |
| Sentence-length σ | 5.8. Borderline |
| Rule of three | "metrics, logs, and traces" is real; "three key pillars" framing is padding |
| Unsourced authority | "Studies show" with no name. **Fail** |
| Tier 1 vocabulary | crucial, vital, navigate, landscape, embark, journey, transformative, robust. **Fail** |

Pattern families present: vocabulary, sentence-level (negative contrast ×2, participial
pseudo-analysis, significance inflation), paragraph-level (temporal opener, summary-recap,
fake-profound kicker), content-level (abstraction). **Five families. Reads as machine-written.**

### Portability test

Every sentence survives swapping the company, the product, and the domain. Paragraph 3 claims a
result and names nothing: not the old stack, not the new one, not the metric that moved. This is
the actual problem. The vocabulary is a symptom.

### After

> Observability gets discussed as three pillars: metrics, logs, and traces. The framing is fine
> and it is also where most teams stop, because the pillars tell you what to collect and nothing
> about what to do when an incident is open at 2am.
>
> We replaced our stack last quarter. Before: Prometheus for metrics, an ELK cluster for logs,
> and no tracing at all, which meant every cross-service latency question turned into an
> afternoon of correlating timestamps by hand. After: OpenTelemetry collectors feeding
> Grafana Tempo, with the same Prometheus retained.
>
> Median time-to-diagnosis on cross-service incidents went from about 40 minutes to about 8.
> That is a small sample, roughly a dozen incidents, so treat it as directional.
>
> The tracing was the part that mattered. Metrics told us something was slow. Logs told us what
> each service did. Neither told us which hop ate the 400ms.

### What changed

Dose: medium.

- Cut 8 Tier 1 words. Each removal was a sentence rewrite, not a synonym swap.
- Cut 3 em dashes, replaced per clause with a period, a comma, and a colon.
- Removed 2 negative contrasts, 1 temporal opener, 1 summary-recap ending, 1 fake-profound
  kicker, 1 participial tack-on.
- Deleted the "Studies show" claim outright rather than sourcing it, because the piece did not
  need it once the author's own number was present.
- Added the specifics the author had: tool names, the before-and-after, the measurement.
- Added the honest caveat about sample size. This is the one addition that makes the number
  believable.
- Paragraph lengths now run 2, 4, 2, 3 sentences instead of a flat 2, 3, 2, 2.

### Left alone deliberately

The three-pillars framing. It is a real convention, not a padded triad, and the author's point
depends on naming it before pushing against it.

### Needs you

The 40-to-8 minute figure and the incident count were reconstructed for this example. In a real
pass, if the author has no measurement, the paragraph gets cut or tagged
`[PLACEHOLDER: median TTD before and after]`. Never fill it in.

---

## Example 2: already-flattened draft, RESTORE mode

The author wrote something good, an AI "polished" it, and the person disappeared. The tells are
gone. So is the writing.

### Before (post-AI-polish)

> Debugging distributed systems presents significant challenges for engineering teams. When
> latency issues occur across service boundaries, identifying the root cause requires systematic
> investigation. Our team encountered such an issue with our authentication service. Through
> careful analysis, we determined that token validation was occurring more frequently than
> necessary. Implementing a caching layer resolved the issue effectively.

Mechanical scan: **passes almost everything.** Zero em dashes. No Tier 1 vocabulary. No banned
phrases. Sentence-length σ is 4.1. A word-list detector calls this clean.

It is not clean. It is bleached. Every sentence is the same length and shape, there is no
person in it, and the actual story has been compressed out.

### After (restored, working from the author's earlier draft and notes)

> Our auth service was slow and I spent two weeks blaming the database.
>
> It wasn't the database. We were re-validating the same JWT on every single request, including
> requests that arrived 50ms apart from the same client. Token validation ran about 200ms.
> Multiply that by every hop in a request chain and you get the afternoon I lost to reading
> Postgres query plans that were fine.
>
> The fix was a cache with event-based invalidation instead of a TTL, because we had tried a TTL
> before and it invalidated too aggressively to help. p99 went from 500ms to 45ms.
>
> I still think the two weeks were partly avoidable. The tracing that would have shown me this
> in an hour existed; I just had not instrumented the auth path.

### What changed

Dose: restore.

- Put back the first person and the actual sequence of events.
- Put back the admission ("I spent two weeks blaming the database", "partly avoidable"). This is
  the single most valuable thing the polish pass deleted and the least fakeable thing in the
  piece.
- Put back the failed prior attempt (the TTL). "Careful analysis" was covering for "we tried
  something and it did not work."
- Put back the numbers the author had: 200ms, 50ms, 500ms to 45ms.
- Broke the uniform rhythm: paragraphs now 1, 4, 2, 2 sentences.

### The lesson

**Passing the mechanical scan is necessary, not sufficient.** A detector-driven pass will
happily certify Example 2's "before" text. Step 6 is what separates this skill from a linter.

---

## Example 3: the draft is fine, leave it alone

This is the most common real case and the one where an eager pass does the most damage.

### Before

> I've been running the eval suite wrong for about six months.
>
> The setup: 400 test cases, each scored by a judge model, aggregated to one number. Looked
> rigorous. The problem is that I was regenerating the judge prompt from a template on every
> run, and the template had a trailing newline that came and went depending on which branch I
> was on. Same test case, same model, different score, roughly 3% of the time.
>
> 3% sounds small. It is larger than most of the improvements I was trying to measure.
>
> Pin your prompts. Hash them. Log the hash next to the score.

### Mechanical scan

| Check | Result |
|---|---|
| Em dashes | 0. Pass |
| Sentence-length σ | 9.2. Pass |
| Tier 1 vocabulary | none. Pass |
| Specificity floor | 400 cases, 6 months, 3%. Pass |
| Rule of three | the closing triad is three distinct actions, not synonyms. Pass |

Pattern families: **zero.** "Looked rigorous" is a two-word fragment; that is voice, not a tell.
The closing three imperatives are a real list, not a reflex triad.

### Correct output

> This reads fine. Two optional notes, neither of which I would change without asking:
>
> - "The setup:" as a colon-label opener is a small tic. It works here. If it opens three
>   sections in the same piece, it becomes a pattern worth breaking.
> - The 3% figure carries the whole argument. If you have the actual run count behind it, one
>   clause would make it harder to argue with.
>
> No edit made.

### The lesson

The fragment, the abrupt open, the four-word closing sentences, and the missing conclusion are
all things a mechanical pass wants to "fix". Fixing them would produce Example 2. **When the
scan comes back clean, say so and stop.**

---

## Example 4: audit mode output

Same draft as Example 1, but the request was "does this sound like AI?" rather than "fix this."
No rewrite.

> ## Patterns found
>
> 1. **Temporal opener** · "In today's fast-paced engineering landscape" → open with a specific
>    fact or claim
> 2. **Negative contrast** · "It's not just about collecting logs — it's about understanding
>    your systems" → state the positive directly
> 3. **Negative contrast** (again) · "observability isn't a luxury — it's a necessity"
> 4. **Unsourced authority** · "Studies show that teams with mature observability practices
>    resolve incidents significantly faster" → name the study or cut the claim
> 5. **Significance inflation** · "plays a vital role", "The results were transformative" →
>    state what actually happened
> 6. **Participial pseudo-analysis** · "highlighting the importance of investing in robust
>    tooling" → make it a sentence or delete
> 7. **Summary-recap ending** · "In conclusion..." → the reader was just there
> 8. **Fake-profound kicker** · "The teams that thrive will be the ones that see clearly" →
>    delete, do not improve
> 9. **Tier 1 vocabulary** · crucial, vital, navigate, landscape, embark, journey,
>    transformative, robust
>
> ## Mechanical scan
>
> | Check | Count | Threshold |
> |---|---|---|
> | Em dashes | 3 in 118 words | 1 per 500 |
> | Paragraphs with no number, name, or date | 4 of 4 | 0 |
> | Unsourced authority | 1 | 0 |
> | Tier 1 vocabulary | 8 | 0 |
>
> Five pattern families co-occurring. On the cluster scale in `detection-rubric.md` that reads
> as machine-written.
>
> ## The underlying problem
>
> The vocabulary is a symptom. Paragraph 3 claims a result and names nothing: not the old stack,
> not the new one, not the metric that moved. Every sentence survives the portability test.
> Fixing the word choices without adding the specifics would produce cleaner text that is still
> about nothing.
>
> ## Not flagged
>
> The three-pillars framing is a real convention, not a padded triad.
>
> Want me to do the rewrite?

Note what audit mode does **not** do: assign a probability, guess at authorship, or rewrite
anything. It names patterns the author can check, points at the root cause, and offers.
