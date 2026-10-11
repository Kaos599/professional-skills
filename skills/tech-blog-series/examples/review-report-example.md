# Review report to the user (example)

> Example of the one consolidated message sent after a panel round (phase 6), for the
> invented "From log line to alert" post 1. Numbers are illustrative. Note the shape: a
> score table, verified findings grouped by kind, a keep list, one recommendation, and the
> batched questions.

---

All three reviews of draft v3 are in. It's better than v2 but not ready yet. I checked the
two biggest new claims against the source data, and both hold up.

| Review | Score |
|---|---|
| Nemesis | 70/100 (v2: 62) |
| 10-metric grader | 78/100. 3 gates still fail: anti-slop (2 families), cadence (7), keep-out |
| Readers (keep reading / understood / trust / share) | Engineer 8/8/7/7 · Eng manager 7/5/6/4 · Non-engineer 8/4/6/3 |

**Numbers that are wrong**
- **The sampling figure uses the mean spike length.** Over the 41 real incidents, a 15 s
  scrape misses 52% of them, not the 38% the mean gives. I recomputed it from the notebook.
- **"The new rule is clearly better on short spikes"**: n = 7 and the CI includes zero.
  Hedge it.
- **"At once" vs "on one day"** in the scale paragraph. The source says one day.

**Where readers drop off**
- The statistics paragraph in section 1: the engineer trusts it, and the other two leave
  there. I'll keep two plain sentences and move the rest to an aside.
- The non-engineer wants the declined-card customer back. Right now they vanish after the
  opening.

**Style gates**: the "each chunk is immutable" rule is said three times, 14 sentences run
over 30 words, and the captions run to 2–3 sentences.

**Keep**: the opening scene, the test-harness bug story, the scrape-interval figure (once
the number is fixed), and the decision rule.

I recommend applying all of the above as v4 now, which the grader projects at about 86. Two
things need your call:
1. Can the post tell the test-harness incident and give the paging volume (23 per week)?
2. Do you want a short "in practice" box for managers (detection delay, cost per million
   events)? If yes, which cost number is publishable?
