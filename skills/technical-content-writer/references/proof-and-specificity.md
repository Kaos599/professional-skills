# Proof and specificity

The mechanics that separate technical writing from technical-sounding writing. This is the
material behind sweeps 3 and 4.

## Why this carries the most weight

71 of 100 harvested skills address the abstraction-versus-specificity axis, second only to em
dashes. It is the highest-consensus *content* rule in the field. It is also the one that
matters most for technical subjects, because the reader can check.

The core observation: **most slop is not badly written. It is unattached to anything.**
Grammatical, fluent, and about nothing in particular. Fixing prose quality does not fix this.
Attaching it to a real object does.

## The portability test

Take any sentence. Swap the company, product, hardware, person, and country.

Survives unchanged → filler. Replace it with a fact, mechanism, number, consequence, or
judgment specific to this subject, or cut it.

Stronger variant, the **three-product swap**: could three unrelated products use this line
unchanged? If yes it is not just vague, it is generic.

```
✗ "The integration improved efficiency across the stack."
   swap the product → still true → filler

✓ "Batching cut p99 from 400ms to 90ms, but added 40ms to p50."
   swap the product → false → real
```

## Category versus identifier

Always name the specific thing.

```
✗ copyright law              ✓ 17 U.S.C. §1201
✗ software updates           ✓ over-the-air firmware pushes to closed-source devices
✗ the memory bottleneck      ✓ HBM read bandwidth at 3.35 TB/s
✗ a large context window     ✓ 80K tokens of prompt
✗ a consumer GPU             ✓ a 24GB 4090
✗ recent improvements        ✓ the v0.6 scheduler rewrite, March 2026
```

The specific name is always stronger than the category. It is also falsifiable, which is the
point.

## The specificity floor

Every paragraph describing a practice, cost, constraint, or result carries at least one number,
dollar amount, named thing, or measurable quantity. One corpus skill sets the working rate at
roughly one per 200 words and treats any paragraph without one as drifted.

For technical writing this is a floor, not a target. Dense technical paragraphs will carry more.

## Adjective to proof

Replace the adjective with the thing that would have made you reach for it.

```
"powerful analytics"    → "shows which pages kill signups"
"robust"                → "handles 40k rps with no retries at p99"
"fast"                  → "45ms, down from 500ms"
"scalable"              → "10k to 100k concurrent, same p99"
"saves time"            → "cuts weekly reporting from 4 hours to 15 minutes"
"significantly better"  → the number, or cut the sentence
"used by many teams"    → "4,200 teams across 60 countries"
```

If you cannot supply the proof, the adjective was a guess. Cut it or tag it.

## Vagueness classes to catch

| Class | Examples | Fix |
|---|---|---|
| Vague time | quickly, fast, soon, recently, in recent years | the duration or the date |
| Vague quantity | many, several, a lot, numerous | the count |
| Vague outcome | better results, improved performance, saves time | the measurement |
| Vague actor | the team, the system, the industry | who specifically |
| Vague magnitude | significantly, dramatically, substantially | the delta |
| Round numbers | "about 100x", "roughly 50%" | the measured figure, or say it is an estimate |

Round numbers that feel invented are their own tell. If a figure is estimated, say so.

## Tagging instead of smoothing

When a claim cannot be made specific, **tag it. Never smooth it and never invent the number.**

```
"Trusted by thousands of teams."
  → [NO-PROOF]
  → [PLACEHOLDER: exact customer count or named logos]

"The fastest option available."
  → [NO-PROOF]
  → [PLACEHOLDER: benchmark figure with hardware and workload, or third-party comparison]
```

Surface every remaining tag at the top of the delivered output under `Needs your input`. Do not
ship a piece with tags buried in the body and no mention of them.

## Attribution

Name the source or delete the claim. These all fail:

`experts agree` · `studies show` · `research suggests` · `industry reports` · `many argue` ·
`widely regarded as` · `observers note` · `it is generally accepted` · `several sources`

If the user has no source, **ask rather than inventing one.** An invented citation is the
single most damaging failure mode in technical content, because it is checkable and it is
checked.

Watch specifically for: journals that do not exist, volume and page numbers that do not exist
for the claimed year, papers assembled from elements of several real sources, and quotes
misattributed to Einstein, Seneca, Confucius, or the Buddha.

## Tradeoffs

Technical readers distrust anything presented as free. State what the choice costs.

```
✗ "Unified memory lets you run much larger models."
✓ "Unified memory fits models a 24GB card never would, but the bandwidth is lower,
   so you trade decode throughput for capacity."
```

The construction is: the benefit, then the mechanism, then what you give up. Omitting the third
part reads as marketing regardless of how accurate the first two are.

## Verify before shipping

Generated drafts invent these confidently. Check each one:

- Backticked file paths: does the file exist?
- Function names, class names, config keys, CLI flags: do they exist in the code?
- Package names in install commands: do they resolve? Watch for names close to real ones.
- Version numbers and release dates
- Cited URLs: does each return 200?
- Benchmark figures: where did this number come from, and on what hardware and workload?

A benchmark number without its hardware and workload is not a fact. It is a screenshot.
