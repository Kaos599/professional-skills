#!/usr/bin/env python3
"""slop_scan.py - mechanical scan for anti-slop-writing.

Implements the mechanical checks from references/detection-rubric.md as a
read-only report. It flags patterns; it never judges authorship and it never
rewrites anything. Thresholds are heuristics collected by the skill's corpus
harvest, not validated measurements - treat every finding as something a human
verifies, exactly as the SKILL.md says.

Usage:
    python slop_scan.py draft.md [more.md ...]
    cat draft.md | python slop_scan.py -

Exit codes follow the cluster bands in detection-rubric.md. The script can see
six of the doctrine's seven families (code-layer findings need a human reading
references/code-slop.md), so its top band sits at six:
    0  0-3 pattern families (clean or light pass)
    1  4-5 families (de-slop pass recommended)
    2  all 6 machine-checkable families present (fully generated shape;
       recommend a heavy pass - heavy stays opt-in per SKILL.md)
    3  usage error (file not found, undecodable input)

Known approximations, by design:
  - Sentence splitting is regex-based and can over-split at abbreviations.
  - Specificity-floor and Tier-2-vocabulary-cluster checks remain manual,
    per detection-rubric.md.
  - The scanner counts mentions as well as uses, so quoted examples
    ("studies show") and markdown table rules (|---|) will fire; review hits
    before acting on them.
  - Every finding feeds judgment, never replaces it.

Stdlib only. No network access.
"""

import re
import statistics
import sys
from pathlib import Path

# Tier 1 vocabulary, condensed from references/banned-vocabulary.md.
TIER1_WORDS = {
    "delve", "leverage", "leveraging", "robust", "seamless", "seamlessly",
    "cutting-edge", "tapestry", "pivotal", "utilize", "utilizing", "foster",
    "facilitate", "realm", "intricate", "unlock", "testament", "vibrant",
    "underscore", "underscores", "underscoring", "boasts", "transformative",
    "revolutionary", "groundbreaking", "synergy", "streamline", "embark",
    "embarking", "paramount", "multifaceted", "holistic", "empower",
}

# Mirrors the formal-transition lexicon pinned in detection-rubric.md.
FORMAL_TRANSITIONS_RE = re.compile(
    r"\b(however|furthermore|moreover|additionally|consequently|therefore|"
    r"nevertheless|thus)\b"
)

# Paragraph-opening connectives: the formal eight plus the three discourse
# markers detection-rubric.md lists for the opener check.
PARAGRAPH_CONNECTIVES_RE = re.compile(
    r"^(however|furthermore|moreover|additionally|consequently|therefore|"
    r"nevertheless|thus|overall|ultimately|that said)\b",
    re.IGNORECASE,
)

# Mirrors the hedge list in detection-rubric.md exactly. Do not add
# might/could: ordinary in instructional writing, absent from the rubric.
HEDGES_RE = re.compile(
    r"\b(arguably|generally|typically|often|potentially|may|"
    r"tend(?:s)? to|seem(?:s)?(?: to)?|appear(?:s)?(?: to)?)\b"
)

DASH_RE = re.compile("\u2014|\u2013|--")

UNSOURCED_AUTHORITY = re.compile(
    r"experts agree|studies show|research shows|research suggests|"
    r"industry reports suggest|many argue|widely regarded as",
    re.IGNORECASE,
)

# Approximate passive detector: be-verb + past-participle-shaped token. The
# lookahead skips common adjectives/adverbs (is open, are often); the extra
# alternation catches irregular participles (-ed/-en cannot see made/done).
PASSIVE_RE = re.compile(
    r"\b(is|are|was|were|be|been|being)\s+"
    r"(?!open\b|often\b|even\b|then\b|when\b)"
    r"(\w+ed|\w+en|made|done|found|shown|built|held|kept|sent)\b",
    re.IGNORECASE,
)

# Triad candidate: three comma-separated chunks of 1-3 words joined by ", and".
# Multi-word items are included; distinct-referent triads are filtered by the
# 2+ occurrence requirement (single near-synonym triads stay a manual call,
# matching the unified rule-of-three condition in detection-rubric.md).
RULE_OF_THREE_RE = re.compile(
    r"\b(?:[\w'-]+(?:\s+[\w'-]+){0,2}),\s*(?:[\w'-]+(?:\s+[\w'-]+){0,2}),"
    r"\s+and\s+(?:[\w'-]+(?:\s+[\w'-]+){0,2})\b"
)

SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?)\]])\s+")


def normalize(text):
    """Straighten curly apostrophes so contractions count as one word."""
    return text.replace("\u2019", "'").replace("\u2018", "'")


def split_sentences_in_paragraph(para_text):
    parts = SENTENCE_SPLIT_RE.split(para_text.replace("\n", " "))
    return [p for p in (s.strip() for s in parts) if p]


def split_sentences(text):
    """Sentences never span paragraphs: a missing terminator at a paragraph
    end must not glue two paragraphs into one pseudo-sentence."""
    sentences = []
    for para in split_paragraphs(text):
        sentences.extend(split_sentences_in_paragraph(para))
    return sentences


def split_paragraphs(text):
    return [p for p in re.split(r"\n\s*\n", text) if p.strip()]


def word_count(text):
    return len(re.findall(r"[\w'-]+", text))


def sigma_over_worst_window(lengths):
    """Whole-text sigma up to 150 sentences; beyond that, the worst contiguous
    100-sentence window, as pinned in detection-rubric.md."""
    n = len(lengths)
    if n <= 150:
        return statistics.pstdev(lengths), f"whole text ({n} sentences)"
    worst = min(
        statistics.pstdev(lengths[i:i + 100])
        for i in range(0, n - 99, 10)
    )
    return worst, "worst 100-sentence window"


def scan(text):
    """Return {check_name: detail} for every check that fails."""
    findings = {}
    text = normalize(text)
    sentences = split_sentences(text)
    n_words = max(word_count(text), 1)
    paragraphs = split_paragraphs(text)
    lower = text.lower()

    # Em/en dash density (>1 per 500 words) OR any cluster (2+ in one
    # sentence), per the rubric's two-pronged threshold.
    dashes = len(DASH_RE.findall(text))
    clustered = any(len(DASH_RE.findall(s)) >= 2 for s in sentences)
    if clustered or (dashes and dashes / n_words * 500 > 1):
        why = "clustered in one sentence" if clustered else ">1 per 500 words"
        findings["em_dashes"] = (
            f"{dashes} em/en/double dashes in {n_words} words ({why})"
        )

    # Sentence-length sigma (rubric: <4; volume rules in sigma_over_worst_window)
    lengths = [word_count(s) for s in sentences]
    if len(lengths) >= 30:
        sigma, window = sigma_over_worst_window(lengths)
        if sigma < 4:
            findings["sentence_sigma"] = (
                f"std dev {sigma:.1f} < 4 over {window}"
            )

    run_best, run_cur = 1, 1
    for prev, cur in zip(lengths, lengths[1:]):
        run_cur = run_cur + 1 if abs(prev - cur) <= 5 else 1
        run_best = max(run_best, run_cur)
    if run_best >= 3:
        findings["same_length_runs"] = (
            f"{run_best} consecutive sentences within 5 words of each other"
        )

    # Sentence openers (>50% starting The/This/It/In per paragraph; needs 3+
    # sentences so two-sentence paragraphs cannot trip it alone)
    opener_paras = 0
    for para in paragraphs:
        sents = split_sentences_in_paragraph(para)
        if len(sents) >= 3:
            openers = sum(1 for s in sents if re.match(r"^(The|This|It|In)\b", s, re.IGNORECASE))
            if openers / len(sents) > 0.5:
                opener_paras += 1
    if opener_paras:
        findings["opener_repetition"] = (
            f"{opener_paras} paragraph(s) over 50% The/This/It/In openers"
        )

    # Formal transitions (>8 per 1000 words)
    t_count = len(FORMAL_TRANSITIONS_RE.findall(lower))
    t_rate = t_count / n_words * 1000
    if t_rate > 8:
        findings["formal_transitions"] = (
            f"{t_count} formal transitions ({t_rate:.0f}/1000 words, threshold >8)"
        )

    # Paragraph-opening connectives (>50%)
    conn = sum(1 for p in paragraphs if PARAGRAPH_CONNECTIVES_RE.match(p.strip()))
    if paragraphs and conn / len(paragraphs) > 0.5:
        findings["paragraph_transitions"] = (
            f"{conn}/{len(paragraphs)} paragraphs open with a connective"
        )

    # Hedging density (>5% of words)
    h_count = len(HEDGES_RE.findall(lower))
    if h_count / n_words > 0.05:
        findings["hedging_density"] = (
            f"{h_count} hedge tokens = {h_count / n_words:.1%} of words (>5%)"
        )

    # Passive voice: share of sentences containing at least one construction
    # (>30%, register carve-out is manual per the rubric's repair-path note)
    p_sents = sum(1 for s in sentences if PASSIVE_RE.search(s))
    if sentences and p_sents / len(sentences) > 0.3:
        findings["passive_voice"] = (
            f"{p_sents}/{len(sentences)} sentences contain passive "
            "constructions (>30%) - verify actor-recovery and scientific-"
            "register carve-outs before flagging"
        )

    # Rule of three: 2+ triad candidates (unified condition; single
    # near-synonym triads remain a manual judgment)
    threes = RULE_OF_THREE_RE.findall(text)
    if len(threes) >= 2:
        findings["rule_of_three"] = f"{len(threes)} triads, e.g. \"{threes[0]}\""

    # Paragraph uniformity (most within +/-1 sentence of the median)
    para_lens = [len(split_sentences_in_paragraph(p)) for p in paragraphs]
    if len(para_lens) >= 3:
        mid = statistics.median(para_lens)
        uniform = sum(1 for l in para_lens if abs(l - mid) <= 1)
        if uniform / len(para_lens) > 0.75:
            findings["paragraph_uniformity"] = (
                f"{uniform}/{len(para_lens)} paragraphs within one sentence of each other"
            )

    # Phrase repetition: a 3+-word trigram recurring with the two uses within
    # 500 words of each other (sliding, per the pinned rubric convention)
    words = re.findall(r"[\w']+", lower)
    positions = {}
    for i in range(len(words) - 2):
        gram_tokens = words[i:i + 3]
        if min(len(t) for t in gram_tokens) < 2:
            continue
        positions.setdefault(" ".join(gram_tokens), []).append(i)
    repeats = []
    for gram, idxs in positions.items():
        for a, b in zip(idxs, idxs[1:]):
            if b - a <= 500:
                repeats.append((gram, b - a))
                break
    if repeats:
        gram, dist = min(repeats, key=lambda r: r[1])
        findings["phrase_repetition"] = (
            f"\"{gram}\" recurs {dist} words apart (within-500 rule)"
        )

    # Unsourced authority (any)
    hits = UNSOURCED_AUTHORITY.findall(text)
    if hits:
        findings["unsourced_authority"] = (
            f"{len(hits)} occurrence(s): {sorted(set(h.lower() for h in hits))}"
        )

    # Tier 1 vocabulary (any)
    tier1_hits = sorted({w for w in re.findall(r"[\w-]+", lower) if w in TIER1_WORDS})
    if tier1_hits:
        findings["tier1_vocabulary"] = ", ".join(tier1_hits)

    return findings


# Maps each machine check to its doctrine family, matching the mapping table
# in detection-rubric.md (structural-patterns.md section placements).
FAMILY_OF = {
    "em_dashes": "formatting",
    "sentence_sigma": "rhythm",
    "same_length_runs": "rhythm",
    "opener_repetition": "rhythm",
    "formal_transitions": "vocabulary",
    "paragraph_transitions": "rhythm",
    "hedging_density": "vocabulary",
    "passive_voice": "sentence-level",
    "rule_of_three": "paragraph-level",
    "paragraph_uniformity": "paragraph-level",
    "phrase_repetition": "paragraph-level",
    "unsourced_authority": "content-level",
    "tier1_vocabulary": "vocabulary",
}

# Six machine-visible families; code-layer is the doctrine's seventh and is
# manual, so the script's top band starts at six.
BANDS = [
    (0, 1, 0, "clean or worth mentioning only"),
    (2, 3, 0, "light pass"),
    (4, 5, 1, "machine-assisted shape; de-slop pass recommended"),
    (6, 6, 2, "fully generated shape; recommend a heavy pass (opt-in)"),
]


def band_for(families):
    for lo, hi, code, label in BANDS:
        if lo <= families <= hi:
            return code, label
    return 2, BANDS[-1][3]


def read_input(path_like):
    """Return (label, text) or (label, None) with a message printed."""
    if path_like == "-":
        return "<stdin>", sys.stdin.read()
    p = Path(path_like)
    if not p.is_file():
        print(f"slop_scan: file not found: {path_like}", file=sys.stderr)
        return str(p), None
    raw = p.read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        text = raw.decode("utf-8", errors="replace")
    if text.count("\x00") / max(len(text), 1) > 0.01:
        print(
            f"slop_scan: {path_like} looks binary or mis-decoded (UTF-16?); "
            "not scanning mojibake.",
            file=sys.stderr,
        )
        return str(p), None
    return str(p), text


def main(argv):
    args = argv[1:]
    if not args:
        print(__doc__)
        return 0

    exit_code = 0
    saw_input = False
    for a in args:
        name, text = read_input(a)
        if text is None:
            exit_code = max(exit_code, 3)
            continue
        saw_input = True
        findings = scan(text)
        families = len({FAMILY_OF[k] for k in findings})
        code, band_label = band_for(families)
        exit_code = max(exit_code, code)
        print(f"\n== {name} ==")
        if not text.strip():
            print("empty input; nothing to scan.")
            continue
        print(f"families present: {families} -> {band_label}")
        if not findings:
            print("no mechanical checks fired. Per SKILL.md: if the draft reads fine, say so and stop.")
        for fname, detail in sorted(findings.items()):
            print(f"  [{fname}] {detail}")
        rhythmish = {"formal_transitions", "paragraph_uniformity", "same_length_runs", "sentence_sigma"}
        if len(rhythmish & set(findings)) >= 2:
            print("  note: even rhythm plus formal connectives is also normal competent "
                  "second-language writing (SKILL.md point 4). Name patterns, not verdicts.")
        print("note: these are heuristics, not authorship evidence. Never report them as an AI-vs-human verdict.")
    if not saw_input and exit_code == 0:
        print("slop_scan: no scannable inputs.", file=sys.stderr)
        exit_code = 3
    return exit_code


if __name__ == "__main__":
    sys.exit(main(sys.argv))
