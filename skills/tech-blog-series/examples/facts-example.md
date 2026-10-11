# FACTS: post 1 (example)

> Example of a filled-in `templates/FACTS.md` for the invented "From log line to alert"
> series. Sources and numbers are illustrative. The point is the shape: every claim is
> traceable, its status is explicit, and cuts are recorded.

| Claim | Value (as stated in the post) | Source | Status |
|---|---|---|---|
| Scrape interval in our default config | 15 s | `infra/prometheus.yml:12` | VERIFIED |
| Median incident length (payments, last quarter) | 38 s (n = 41, IQR 9–120 s) | `analysis/incidents_q3.ipynb`, cell 7 | VERIFIED |
| Share of incidents under 15 s | 29% (12 of 41) | same notebook, cell 9 | VERIFIED. Post says "about 3 in 10" |
| Miss chance for a 4 s spike at a 15 s scrape | 73% | arithmetic: (15 − 4) / 15 | OK (arithmetic) |
| Detection delay, old rule vs new | 95 s vs 41 s median, 30 incidents, CI of the difference [−71, −32] | `evals/detect_v2/results.md:44` | VERIFIED |
| Rerun drift of the detection-delay metric | ±6 s across 3 replays | `evals/detect_v2/results.md:61` | VERIFIED |
| Vendor's ingest volume | "over 2 trillion events a day" | vendor blog, 2026-03-04, URL | VENDOR CLAIM. Post says "the vendor says" |
| Chunk boundary bug made test queries read the wrong minute | first event 0–59 s early on 18 of 20 replays | `postmortems/2026-05-test-harness.md:23` | VERIFIED, [CLEAR?] incident story |
| Paging volume per on-call week | 23 pages | internal dashboard export, 2026-06 | [CLEAR?] volume figure |

## Added in v3

| Claim | Value | Source | Status |
|---|---|---|---|
| The reviewer of the 20 replays was the author | the author labelled all 20 | `evals/labels/README.md:3` | VERIFIED. Paragraph moved to first person |
| Naive baseline ties the metric | "traffic in the hour" predicts paging as well (AUC 0.81 vs 0.82) | `evals/detect_v2/confounds.md:12` | VERIFIED. Disclosed in the body |

## Removed in v3 (and why)

- "Most outages are under a minute": the source was a vendor survey with no method
  section. Cut.
- "The new rule catches every short spike": the CI on short spikes includes zero (n = 7).
  Replaced with a hedged sentence.
- A reference to the vendor report: it was orphaned once the claim above was cut. Removed
  from References too.

## Do not use

- "Scrapes happen exactly every 15 s": the logs show jitter of up to 2 s. Say "about every
  15 s".
