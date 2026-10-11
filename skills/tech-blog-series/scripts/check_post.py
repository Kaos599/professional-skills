#!/usr/bin/env python3
"""Mechanical checks for a series post (post.md). Standard library only.

Usage:
  python3 check_post.py <post.md> [--keep-out terms.txt] [--max-words 2600] [--min-words 1800]
                                  [--long 30] [--max-para 6] [--max-not-y 2]

Counts what can be counted, so reviewers spend their attention on judgement:
  - main-prose words (excludes front matter, asides "> ", tables, figure lines, captions,
    the glossary section and anything after it)
  - sentences over --long words, paragraphs over --max-para sentences
  - hard-rule violations: semicolons, em dashes, exclamation marks in prose, an opening
    question, mid-sentence bold, more than one bold per H2 section, captions over one sentence
  - "X, not Y" constructions (budget --max-not-y)
  - keep-out terms (internal names, customers, ids) from a file, one term per line, searched
    everywhere including asides, captions and figure files referenced by the post
  - figure count

Exit code 1 if any hard rule fails, so it can gate a publish.
"""
import argparse
import re
import sys
from pathlib import Path

GLOSSARY_HEADINGS = ("## Words used", "## Glossary", "## References")


def split_sentences(text: str) -> list[str]:
    text = re.sub(r"\b(e\.g|i\.e|etc|vs|approx|Fig|fig|No|al)\.", lambda m: m.group(0).replace(".", "§"), text)
    text = re.sub(r"(\d)\.(\d)", r"\1§\2", text)
    parts = re.split(r"(?<=[.?!])[\"')\]]*\s+(?=[A-Z0-9\"'(])", text)
    return [p.replace("§", ".").strip() for p in parts if p.strip()]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("post")
    ap.add_argument("--keep-out")
    ap.add_argument("--max-words", type=int, default=2600)
    ap.add_argument("--min-words", type=int, default=1800)
    ap.add_argument("--long", type=int, default=30)
    ap.add_argument("--max-para", type=int, default=6)
    ap.add_argument("--max-not-y", type=int, default=2)
    a = ap.parse_args()

    path = Path(a.post)
    md = path.read_text()
    body = md.split("---", 2)[2] if md.startswith("---") else md
    main_part = body
    for h in GLOSSARY_HEADINGS:
        if h in main_part:
            main_part = main_part.split(h)[0]

    hard, soft = [], []
    lines = main_part.splitlines()

    # paragraphs of main prose, with their H2 section
    paras, section, cur = [], "(opening)", []
    captions = []
    for ln in lines + [""]:
        s = ln.strip()
        if s.startswith("## "):
            if cur:
                paras.append((section, " ".join(cur)))
                cur = []
            section = s[3:]
            continue
        if not s or s.startswith(("#", ">", "|", "![")):
            if cur:
                paras.append((section, " ".join(cur)))
                cur = []
            continue
        if re.fullmatch(r"\*[^*].*\*", s):
            captions.append(s.strip("*"))
            continue
        if re.match(r"^(\d+\.|-) ", s):
            if cur:
                paras.append((section, " ".join(cur)))
                cur = []
            paras.append((section, re.sub(r"^(\d+\.|-) ", "", s)))
            continue
        cur.append(s)

    prose = "\n".join(p for _, p in paras)
    words = len(prose.split())
    print(f"main-prose words: {words} (target {a.min_words}-{a.max_words})")
    if not a.min_words <= words <= a.max_words:
        soft.append(f"length {words} outside {a.min_words}-{a.max_words}")

    figs = len(re.findall(r"^!\[", body, re.M))
    print(f"figures: {figs}")

    # hard rules on prose (asides included for punctuation rules)
    prose_and_asides = prose + "\n" + "\n".join(l for l in lines if l.startswith(">"))
    for ch, name in ((";", "semicolon"), ("—", "em dash")):
        n = prose_and_asides.count(ch) + sum(c.count(ch) for c in captions)
        if n:
            hard.append(f"{n} {name}(s)")
    excl = len(re.findall(r"!(?!\[)", re.sub(r"!\[", "", prose_and_asides)))
    if excl:
        hard.append(f"{excl} exclamation mark(s) in prose")
    first = paras[0][1] if paras else ""
    if split_sentences(first) and split_sentences(first)[0].endswith("?"):
        hard.append("post opens with a question")

    # bold
    by_section = {}
    for sec, p in paras:
        for m in re.finditer(r"\*\*([^*]+)\*\*", p):
            by_section[sec] = by_section.get(sec, 0) + 1
            before = p[: m.start()].rstrip().rstrip("\"'\u201d\u2019)")
            if before and not before.endswith((".", ":", "?")):
                hard.append(f"mid-sentence bold in '{sec}': **{m.group(1)[:50]}**")
    for sec, n in by_section.items():
        if n > 1:
            hard.append(f"{n} bold spans in section '{sec}' (max 1)")

    # captions
    for c in captions:
        n = len(split_sentences(c))
        if n > 1:
            soft.append(f"caption has {n} sentences: '{c[:60]}...'")

    # sentences and paragraphs
    long_s = []
    for sec, p in paras:
        ss = split_sentences(p)
        if len(ss) > a.max_para:
            soft.append(f"paragraph with {len(ss)} sentences in '{sec}': '{p[:60]}...'")
        for s_ in ss:
            n = len(s_.split())
            if n > a.long:
                long_s.append((n, s_))
    print(f"sentences over {a.long} words: {len(long_s)}")
    for n, s_ in sorted(long_s, reverse=True):
        print(f"  {n:>3}  {s_[:110]}")

    # X, not Y
    not_y = re.findall(r"[^.]*\b\w+, not (?:a |an |the )?\w+[^.]*\.", prose)
    heads = re.findall(r"^## .*, not .*$", body, re.M)
    count = len(not_y) + len(heads)
    print(f'"X, not Y" constructions: {count} (max {a.max_not_y})')
    for x in not_y + heads:
        print(f"  {x.strip()[:110]}")
    if count > a.max_not_y:
        soft.append(f'{count} "X, not Y" constructions')

    # keep-out
    if a.keep_out:
        terms = [t.strip() for t in Path(a.keep_out).read_text().splitlines() if t.strip() and not t.startswith("#")]
        hay = md
        for fig in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", md):
            fp = (path.parent / fig).resolve()
            if fp.exists():
                hay += "\n" + fp.read_text()
        for t in terms:
            pat = re.compile(r"\b" + re.escape(t) + r"\b", re.I)
            hits = len(pat.findall(hay))
            if hits:
                hard.append(f"keep-out term '{t}' appears {hits}x (post or figures)")

    print()
    for h in hard:
        print("FAIL ", h)
    for s_ in soft:
        print("WARN ", s_)
    if not hard and not soft:
        print("all mechanical checks pass")
    return 1 if hard else 0


if __name__ == "__main__":
    sys.exit(main())
