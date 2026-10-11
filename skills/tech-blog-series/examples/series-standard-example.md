# Series standard: From log line to alert

> Example of a filled-in `templates/SERIES_STANDARD.md`, for an invented series about a
> monitoring pipeline. The company, names and numbers are illustrative.

Planning tracker: Claude Doc "Log-to-alert series: planning tracker".

## 1. The series

| # | Post | One idea the reader keeps |
|---|---|---|
| 1 | From log line to stored event | Before any detector runs, you must agree with the pipeline on what time it is and how finely you can afford to look. |
| 2 | Finding the incident | The length of the thing you're trying to catch decides which detection methods can work at all. |
| 3 | Paging the right person | An alert is a decision about someone's night, so precision is a product feature. |
| 4 (optional) | Measuring it honestly | A detector can look great on averages and still miss every short outage. |

Readers: a backend engineer new to observability; an engineering manager who owns
reliability and budget; a curious non-engineer who has seen "something went wrong" on a
checkout page. Two layers: the story in the body, mechanism in `> **For engineers.**`
asides.

## 2. Voice

```
person:       "I" for decisions, "we" for team work
registers:    essay (median ~10 words per sentence) for ideas; walkthrough for mechanisms
devices:      colon reveals; → for pipelines; one number per claim; everyday analogies
contractions: yes
opinions:     one first-person view per H2
never:        exclamation marks, an opening question, semicolons, em dashes, emoji,
              mid-sentence bold, "In this post", recaps, aphorism closers
budgets:      "X, not Y" ≤ 2 per post; one bold rule per section; each rule said once
```

## 3. Storytelling

Cold open: 9:02 on the biggest sales morning of the year. The payment service stops
answering for four seconds, and the dashboard scrapes every fifteen. A customer's card is
declined at the last step and they leave. Someone has to notice, find the four seconds in
a day of logs, work out which service caused it, and wake the right person, while the sale
keeps running. Now do that for every service, every minute. Doing it by hand is impossible,
and that's the problem the series is about. Each incident in the body gets a human beat
(who was paged, what the customer saw). Post 1 ends by returning to the declined card.

## 4. Post anatomy

Dek · cold open (post 1: up to 5 paragraphs; later posts 2–4 sentences) · series rail ·
3–5 thesis H2s · tried → broke → changed → result · "What this does not solve" (with a
first-person view) · decision rule · next post (one sentence) · glossary · references.
1,800–2,600 words of main prose, 4–7 figures.

## 5. Numbers and claims

Every number gets its unit, scale and comparison, plus a FACTS row. Give n in the sentence
when it's under 30. Say when a CI includes zero. Name selection effects, rerun drift,
confounds and single reviewers. Thresholds come from distributions, not means. Anything
company-sensitive is marked `[CLEAR?]`.

## 6. Public names

| Public name | Internal name | Definition used in posts |
|---|---|---|
| event | (internal record type) | One parsed log line with a timestamp and a service |
| chunk | (internal storage unit) | A time-ordered block of events, written once and never changed |
| index | (internal manifest name) | The list of chunks. It keeps changing while data arrives |
| scrape interval | (internal config key) | Seconds between two metric samples |
| incident window | (internal label) | The span where the failure is visible to a customer |
| detection delay | (internal metric name) | Time from the incident start to the first alert. Lower is better |
| on-call engineer | (internal role name) | The person an alert pages |

Keep every internal name out of prose and figures. They're listed in `keep-out.txt` for
`check_post.py`.

## 7. Figures

Follow `figures/STYLE.md` (from the kit). The accent marks the figure's subject. The
hazard colour marks only the incident window. One finding-style title per figure, and
one-sentence captions.

## 8. Gates

0. Panel (nemesis + grader + 3 readers), with the blockers fixed.
1. FACTS complete.
2. Keep-out clean.
3. Anti-slop below 2 families.
4. STE lint.
5. Six sweeps at 8 or above.
6. Adversarial review.
7. Clearances recorded.

## 9. Files

```
log-to-alert/SERIES_STANDARD.md  keep-out.txt  build_preview.py
log-to-alert/figures/            build_figures.py  STYLE.md  fig-*.svg  preview.html
log-to-alert/post-1-log-to-event/ post.md  FACTS.md  NOTES.md  preview.html
```
