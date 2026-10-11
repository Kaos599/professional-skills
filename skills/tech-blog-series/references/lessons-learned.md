# Lessons learned

These come from building a real multi-post technical series through six drafts and three
review rounds. They're written so they apply to any domain. Each entry gives what went
wrong, then the fix, then where the rule now lives.

## Writing
- **Fact-list openings.** A cold open made of statistics got the feedback "needs emotional,
  humanistic storytelling". → Put a person in each opening paragraph, and frame the scene
  with "Picture…". → Writing standard §2.
- **Stock and sentimental lines.** Generic life moments and assumed feelings were flagged
  by every reviewer. → Use a detail specific to the medium, and cut assumed feelings.
- **The human thread stopped after the opening.** The body read as pure walkthrough. →
  Quote the author's own notes at the turning point, give each incident a human beat, and
  return to the scene in the body and at the end.
- **Bait-and-switch.** The opening scene came from a famous domain, and the data came from
  the author's niche one. → Say why early ("I'll use X because you know it. Our data is
  Y"), and return to the scene.
- **The same rule said three times** (as the fix, as a lesson line, and as a pull line)
  counted as an anti-slop family. → Say it once.
- **The statistics paragraph lost two of three readers.** → Two plain sentences in the
  body, the detail in an aside.

## Evidence
- **"This setting mattered a lot"** said over a CI that included zero, on cases selected
  because they failed. → Say both.
- **"A clear gain"** the same size as the baseline's own rerun drift. → Compare every effect
  with rerun drift.
- **A metric with a tied confound.** A naive "how hard was this case" baseline separated
  good from bad exactly as well as the metric did. → Report the naive baseline.
- **A threshold from a mean.** A miss-chance figure computed from the average event length
  understated misses by about a quarter, because half the events were shorter than
  average. → Compute over the distribution.
- **Misattribution.** A survey quote was about one family of methods, and a parameter came
  from one paper the survey cited. → Read the surrounding paragraph, and attribute to the
  specific method.
- **Wording drift.** A source said "N on one day", and the draft said "N at once". → Match
  the wording exactly.
- **References outliving their claims.** Cutting a claim left its reference and a title
  phrase without a source. → After any cut, sweep the references and the title.
- **Who the person in the evidence was.** The reviewer whose rejections drove the thesis
  was the author. → Writing it in first person fixed a naming conflict and added the
  strongest human beat.

## Figures
- **Too much text**: three label layers per row. → One name and one number per row, with
  notes moved to the caption.
- **Repeated labels and CLI flags.** → Ticks plus one label, and plain-word rows.
- **A claim described instead of drawn** (a delay explained in a sentence). → Draw it: an
  event, an arrow to where it's picked up, and a short label.
- **An impossible option** (a setting drawn that the API rejects). → Relabel it as what it
  really is (the source itself, not a choice).
- **A figure that raises a question** it doesn't answer. → Draw and label the reason.
- **One unit length in the figures, another in the prose.** → Keep the figures consistent
  with the prose.

## Process
- **Subagent and reviewer claims can be wrong either way.** One reviewer said a mechanism
  "appears nowhere in the repo" when an audit doc described it. Another recomputed a
  statistic correctly. → Verify blockers and proposed numbers against the source before
  you relay them.
- **The user's corrections are fixed inputs.** A reviewer's "this step is unnecessary" was
  wrong, because the user's system needs it for a real-time constraint. → Record it in
  NOTES and pass it to every reviewer.
- **Clearance items pile up.** Customer names, incidents, production config and prompt
  paraphrases each need an explicit yes. → Track them in NOTES and ask once, batched.
- **Claude Docs batch limit**: 64 blocks.
- **Files changed on disk**: re-read before writing.
- Long sessions lose artifact watches. Republishing from the same path keeps the URL anyway.
