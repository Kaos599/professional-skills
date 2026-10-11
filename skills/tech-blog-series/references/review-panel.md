# Review panel

Three reviewers run **in parallel** (one message, three Agent calls), each a fresh agent.
They read the post, FACTS, NOTES, the series standard and the rendered figure PNGs. They
edit nothing. You verify their claims, triage them, and report once.

Fill in `<…>` placeholders. Always include the user's fixed decisions, so reviewers don't
relitigate them, and the known open clearance items, so they confirm rather than re-flag.

## 1. Nemesis (adversarial)

Agent: `nemesis-review` (or `general-purpose` with this prompt).

```
Brutally adversarial review of a technical blog post draft (<vN>). Do NOT edit files. Report only.
Base dir: <series dir>. Read: <post.md> (target), FACTS.md, NOTES.md (check that the previous
review's findings were actually fixed and the fixes didn't add new errors), SERIES_STANDARD.md,
figures/STYLE.md, figures/*.svg. LOOK at the rendered figures: <png glob> and the page top <png>.
Context: <one paragraph: series, post's job, author and their role, audience>.
Owner decisions not to relitigate: <list>. Known open clearance items (confirm they're the only ones): <list>.
Attack: technical correctness (<domain topics>, any probability or arithmetic), evidence honesty vs
FACTS and the repo sources it cites (spot-check sources under <repo>), regressions from the last fixes,
figure accuracy vs prose (labels, scales, what's drawn), keep-out leaks (<internal names>),
voice rules (<bans>), anti-slop tells.
Output: verdict + score /100; BLOCKERS, MAJOR, MINOR with line numbers, exact quotes, concrete fixes;
max 5 "keep" items. Under 1,200 words.
```

## 2. Grader (10 metrics + gates)

```
You are the grader on a blog review panel. Do NOT edit files. Report only.
Read: <post.md> (<vN>), FACTS.md, NOTES.md (prior scores: <history>), SERIES_STANDARD.md, STYLE.md.
Look at the rendered figures <png glob> and page top <png>. Load and apply
~/.claude/skills/anti-slop-writing/SKILL.md and ~/.claude/skills/technical-content-writer/SKILL.md
(+ references/editing-passes.md).
Score 0-10 with a one-line justification and the single highest-leverage fix: hook, clarity,
correctness, sourcing, structure, figures, voice, anti-slop, actionability, standard compliance. Then:
- Total /100.
- Anti-slop audit mode: pattern families found (with quotes). Gate: fewer than 2 families.
- Technical-content-writer six sweeps (clarity, so-what/framing, prove-it, specificity, cadence,
  voice), 0-10 each. Gate: 8+.
- STE lint: `python3 ~/.claude/skills/simplified-technical-english/scripts/ste_check.py --mode
  descriptive <post.md>`. Meaningful findings only (ignore contractions and -ing in narrative).
- Mechanical: run `python3 ~/.claude/skills/tech-blog-series/scripts/check_post.py <post.md>` and
  interpret it.
- Does the human/emotional storytelling carry through the post or stop after the opening? Quote
  where it lands and where it's missing.
- Top 5 fixes ranked by score gain, plus the projected score.
Under 1,200 words.
```

## 3. Three readers

```
You simulate three distinct readers of a blog post. Do NOT edit files. Report only.
Read <post.md> top to bottom as each reader and look at the figures as rendered (<png list in
post order>). The "> **For engineers.**" blocks are optional asides.
Readers (stay in character, honest, not polite):
1. <engineer who knows adjacent tech but not this domain>
2. <decision-maker: cares about <outcomes>, buy vs build; not an engineer>
3. <non-engineer from a shared link, who knows <relatable domain>>
For each: scores 1-10 for keep reading past the opening / understood it / trusts it / would share or act;
the exact sentence where they first got lost or bored (quote + line) and their most engaged moment;
which figures helped or confused them and why (per figure); what they wanted that the post didn't
give; one sentence they'd quote.
Then: where the three conflict, and the 5 changes that would help the most readers at once, ranked.
Under 1,100 words total.
```

## The 10 metrics

| Metric | 10 looks like |
|---|---|
| Hook | a scene with stakes and a person; scale without a fact dump; reaches the problem fast |
| Clarity | every term glossed once; output and "lower is better" defined before the first score |
| Correctness | technical claims and arithmetic hold up; figures match the data |
| Sourcing | every number has a FACTS row; references match what the prose still claims |
| Structure | anatomy followed; H2s carry the argument; next post is one sentence |
| Figures | each one confirms a stated claim; minimal text; rules kept; one-sentence captions |
| Voice | matches the signature; one first-person view per section; earned admissions kept |
| Anti-slop | < 2 pattern families |
| Actionability | the decision rule is concrete, with thresholds the reader can apply |
| Standard compliance | the gates, keep-out list, public names, length and caption rules |

## Your job after the panel

1. **Verify before relaying.** For every BLOCKER and every new number a reviewer proposes,
   read the cited lines or recompute from the raw data. Expect all three outcomes:
   - a reviewer claims a mechanism "appears nowhere in the repo", and a grep finds it in an
     audit doc (the reviewer was wrong);
   - a reviewer recomputes a statistic over the raw data and gets a different number (the
     reviewer was right, so the figure changes);
   - a reviewer says an effect is within noise, and the rerun-drift table confirms it.
2. **Triage** into: confirmed blockers · confirmed majors · disputed (with your
   evidence) · user decisions (clearances, scope, new content such as an outcome box).
3. **Report once**:
   - a score table (nemesis /100, grader /100 with the failing gates, reader scores);
   - the confirmed issues grouped by kind (numbers that are wrong, where readers drop off,
     style gates);
   - what all three said to keep;
   - **one** recommendation (usually "apply all as vN+1");
   - the batched user questions.
4. **Apply → log in NOTES** (what changed, which findings each change answers, which are
   left for the user) → add FACTS rows for new numbers → `check_post.py` → rebuild the
   preview → publish → re-grade if the user asks.

## Score history (keep it in NOTES.md)

The format, with illustrative values:

```
| round | nemesis | grader | engineer | decision-maker | non-engineer | gates failing |
|-------|---------|--------|----------|----------------|--------------|---------------|
| v1    |   –     |  ~65   |  7/6/6/6 |    6/6/7/5     |   6/5/4/3    | anti-slop, voice, sourcing |
| v3    |   ~65   |  ~75   |  8/7/7/6 |    7/5/6/4     |   7/4/5/3    | evidence overclaims, keep-out |
| v6    |   ~70   |  ~80   |  8/8/8/7 |    7/5/6/4     |   8/4/6/2    | anti-slop, cadence, captions, keep-out |
```
Reader scores are keep reading / understood / trusts / would share or act.

**What a typical trajectory looks like.** Expect a first full draft to score in the mid-60s
and fail several gates. Two or three panel rounds usually bring it to around 80, mostly
from evidence fixes (overclaims, sources, figure numbers) and from moving statistics into
asides. The last points come from cadence, captions and the clearances only the user can
give. Two patterns are normal:
- the nemesis score moves less than the grader's, because each round it digs deeper;
- the non-engineer's "understood" score is the hardest to raise, and the fix is structural
  (consequence before mechanism, statistics into asides, a human beat per section), not
  wording.

Re-grade after a fix round that touched evidence or structure, or when the user asks. Stop
when every gate passes.
