# Professional Skills for AI Coding Agents

[![skills.sh](https://skills.sh/b/Kaos599/professional-skills)](https://skills.sh/Kaos599/professional-skills)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Two production-grade **agent skills for professional writing** — built for **Claude Code**, installable
with **skills.sh** (`npx skills`), and compatible with any agent that reads `SKILL.md` files.

- **`anti-slop-writing`** — makes writing sound like a person wrote it. Removes AI tells, restores
  voice that AI editing flattened, audits text on demand.
- **`technical-content-writer`** — writes technical content in a derived voice: LinkedIn posts,
  blog posts, threads, newsletters, and essays that survive being checked by the reader.

## Why two skills

They fail differently and are meant to run separately.

- `anti-slop-writing` answers **"does this sound like a person?"**
- `technical-content-writer` answers **"is this any good?"**

A piece can pass one and fail the other. Clean human-sounding prose about nothing still fails the
second. A dense, correct, well-argued piece riddled with em dashes and "in conclusion" still fails
the first. The writer skill calls the anti-slop skill as a hard gate before anything ships.

## Skills

### anti-slop-writing — AI writing detector and humanizing editor

Rewrite, audit, or restore writing so it reads as human. Three modes:

| Mode | What it does |
|---|---|
| **Improve** (default) | Rewrites the draft so it is better *and* sounds like a person |
| **Audit** | Names AI patterns without rewriting — for when someone just wants to know |
| **Restore** | Recovers the person from a draft that an AI already "polished" flat |

Key design decisions, distilled from a corpus of 100 published skills:

- **Structure outlives vocabulary.** `delve`, `tapestry`, and `vibrant` are already gone from
  frontier-model output. Sentence-shape and paragraph-shape tells are not. The skill weights
  structure above word lists.
- **Tells count in clusters, never alone.** One em dash means nothing. Four pattern families
  co-occurring is a finding.
- **No AI-vs-human probability score.** Detectors guess, and they are most wrong against
  non-native English writers. Named patterns are checkable; a score is not.
- **Subtraction is only half the job.** A dedicated step puts the person back — pacing fragments,
  admissions, digressions, edge — because a draft that has been stripped clean is not finished,
  it is bleached.

### technical-content-writer — technical content that sounds like a specific human

Content about technical subjects, written for readers who can tell if you are faking it.
Infrastructure, model serving, data pipelines, systems tradeoffs.

```
0. Anchor      → the concrete thing, the counter-intuitive claim, the proof artifact, the lesson
1. Calibrate   → voice signature derived from exemplars at runtime
2. Shape       → format mechanics and structure archetypes
3. Draft       → in the signature, against the anchor
4. Sweep       → five editing passes, each scored 0–10, nothing ships below 8
5. Gate        → anti-slop scan with a hard threshold
6. Ship
```

- **No anchor, no piece.** Four questions must be answerable before a word is written — and
  inventing a number, benchmark, or quote is absolute.
- **Voice is derived at runtime, not hard-coded.** Drop a sample into `references/exemplars/` and
  the signature changes. No code edit.
- **Mechanism over outcome.** "Decode is bottlenecked on memory bandwidth because every step
  re-reads the weights" beats "decode is slow."

## Install

### via skills.sh (any agent, including Claude Code)

```bash
npx skills add Kaos599/professional-skills
```

Install a single skill:

```bash
npx skills add Kaos599/professional-skills --skill anti-slop-writing
npx skills add Kaos599/professional-skills --skill technical-content-writer
```

Install globally, across all projects:

```bash
npx skills add -g Kaos599/professional-skills --all
```

### as a Claude Code plugin

This repository is a valid Claude Code plugin (it carries `.claude-plugin/plugin.json`) with both
skills under `skills/`:

```bash
claude plugin marketplace add Kaos599/professional-skills
claude plugin install professional-skills
```

Or install the skills directly into any Claude Code project:

```bash
npx skills add Kaos599/professional-skills -a claude-code --all
```

### without installing

Point your agent at the folder or invoke by name:

```bash
# Claude Code / skills.sh
# SKILL.md files with name + description frontmatter are auto-discovered from any of these paths
```

## Repository structure

```
professional-skills/
├── .claude-plugin/
│   ├── plugin.json          # Claude Code plugin manifest
│   └── marketplace.json     # Claude Code marketplace catalog
├── skills/
│   ├── anti-slop-writing/
│   │   ├── SKILL.md
│   │   └── references/      # banned vocabulary, structural patterns, rubric, worked examples
│   └── technical-content-writer/
│       ├── SKILL.md
│       └── references/      # voice protocol, playbooks, editing passes, exemplars
└── README.md
```

Both skills follow the standard `SKILL.md` + `references/` layout, so Claude Code, skills.sh, and
any Agent Skills–compatible host pick them up automatically.

## Adding a voice to technical-content-writer

Drop `NN-short-slug.md` into `references/exemplars/` with the frontmatter header documented in
that folder's README. Paste the piece **verbatim**, typos and all — those are signal. Set
`authored: true` for your own writing, `authored: false` for writing you admire; the protocol
weights them differently.

## Provenance

The anti-slop and writing-craft content is distilled from a harvest of 100 published skills on
skills.sh (~387,000 words across 45 anti-slop and 55 writing-craft skills), analyzed with
ban-context document frequency so skills that *ban* a word are counted separately from skills that
*use* it. The exemplars and house-style measurements come from a separate pass over real published
technical writing, with sources cited per entry.

## License

MIT
