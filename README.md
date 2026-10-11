<div align="center">

# <span style="background: linear-gradient(135deg, #8B5CF6 0%, #EC4899 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">Professional Skills</span>

### Agent skills for professional writing, built for **Claude Code**, **Codex**, and **skills.sh**

Three production-grade skills: make anything you ship sound like a person wrote it, and take a technical blog series from research to a reviewed, illustrated draft.

[![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-Plugin-D97757?style=flat-square&logo=claude&logoColor=white)](https://code.claude.com)
[![Codex Plugin](https://img.shields.io/badge/Codex-Plugin-10A37F?style=flat-square&logo=openai&logoColor=white)](https://developers.openai.com/codex)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Format-8A2BE2?style=flat-square)](https://agentskills.io)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](LICENSE)

```
npx skills add Kaos599/professional-skills --all
```

</div>

---

## What's inside

Three skills, each a `SKILL.md` plus a `references/` folder. The two writing skills fail differently and run separately; the writer calls the anti-slop skill as a hard gate before anything ships. `tech-blog-series` sits on top of both: it orchestrates research, drafting, figures and review for long-form technical posts, and uses the other two for voice and the anti-slop gate.

<div style="border: 1px solid rgba(127,127,127,0.35); border-radius: 12px; padding: 20px 24px; margin: 16px 0; background: rgba(127,127,127,0.06);">

### `anti-slop-writing`

**Make AI text sound human.** Rewrites drafts that read as machine-generated, restores the voice that AI editing flattened, and audits text for AI tells when asked.

**Three modes:**

1. **Improve** (default): rewrite so it is better and sounds like a person.
2. **Audit**: name the AI patterns, quote the line, give the fix. No rewrite, no score.
3. **Restore**: rescue the person from a draft an AI already "polished" flat.

**Why it works:**

- Structure outlives vocabulary. Word lists go stale; sentence-shape and paragraph-shape tells do not.
- Tells count in clusters, never alone. One em dash means nothing; several pattern families co-occurring is a finding.
- No AI-vs-human probability verdicts. Detectors guess, and they are most wrong against non-native English writers.
- Subtraction is only half the job. A dedicated step puts the person back, because a stripped draft is bleached, not finished.
- Ships with a read-only scanner (`scripts/slop_scan.py`) so the mechanical checks run in CI, not just in a model's head.

**Use when:** a draft feels generic or corporate, when polishing anything an LLM helped write, or before publishing anything.

</div>

<div style="border: 1px solid rgba(127,127,127,0.35); border-radius: 12px; padding: 20px 24px; margin: 16px 0; background: rgba(127,127,127,0.06);">

### `technical-content-writer`

**Technical content that sounds like a specific human.** Writes LinkedIn posts, blog posts, threads, newsletters, and essays for readers who can tell if you are faking it.

**The pipeline:**

```
0. Anchor     -> the concrete thing, the domain constraint, the proof, the utility
1. Persona    -> who the author is as an engineer, and the stance they write from
2. Calibrate  -> voice signature derived from exemplars or a persona at runtime
3. Shape      -> format mechanics and structure archetypes
4. Draft      -> in the signature and persona, against the anchor
5. Sweep      -> six editing passes, each scored 0 to 10
6. Gate       -> anti-slop audit, hard threshold, nothing ships above the clean band
7. Ship
```

**Why it works:**

- Voice is derived from samples at runtime. Drop a file into `references/exemplars/` and the signature changes; no code edit.
- Mechanism beats outcome. "Decode is bottlenecked on memory bandwidth because every step re-reads the weights" beats "decode is slow."
- Every claim carries a number or a named thing. No anchor means no piece, and inventing a number, benchmark, or quote is absolute.

**Use when:** writing or rewriting any technical content for a public audience.

</div>

<div style="border: 1px solid rgba(127,127,127,0.35); border-radius: 12px; padding: 20px 24px; margin: 16px 0; background: rgba(127,127,127,0.06);">

### `tech-blog-series`

**A deep technical blog post or series, from research to reviewed draft.** Plans, researches, writes, illustrates and reviews long-form technical posts (your own practice plus industry and research context) that an engineer can check and a non-engineer can follow.

**Six phases:**

```
1. Voice and references -> intake questions, voice signature, design tokens, reference anatomy
2. Topic research       -> papers, your own evidence, industry facts, then a concept inventory
3. Shape the series     -> agree the post split with the user before writing
4. Standard and draft   -> series standard, fact ledger, notes, then the post
5. Figures and preview  -> hand-built SVG figures in both themes, a private preview page
6. Review, fix, gate    -> nemesis + 10-metric grader + 3 reader POVs, verified, fixed, gated
```

**Why it works:**

- No fact row, no number. Every claim traces to a file:line or URL in `FACTS.md`, and cuts are recorded.
- Evidence honesty is a rule, not a vibe: n under 30 is stated, CIs that include zero are said aloud, selection effects, rerun drift and confounds are named, and thresholds come from distributions, not means.
- Human storytelling with two layers: a scene and a person in the body, mechanism and statistics in "For engineers" asides.
- Figures from a stdlib-only SVG kit (`scripts/figure_kit.py`): one idea per figure, one accent, a reserved hazard colour, computed numbers with `--check` asserts, themable for dark and light.
- A review panel that runs in parallel, and an orchestrator that verifies reviewers' claims against the source before relaying them.
- Ships `check_post.py` (mechanical lint, exits 1 on hard-rule failures), `build_preview.py`, `shoot_figures.py`, templates and worked examples.

**Use when:** writing a technical blog or series, turning a codebase, paper or experiment log into posts, making explanatory figures, or reviewing and grading a technical draft.

</div>

---

## Install

### skills.sh: any agent, one command

Works with Claude Code, Codex, and 30+ agents. Skills land in the right directory for your agent automatically.

```bash
# All skills, all agents
npx skills add Kaos599/professional-skills --all

# A single skill
npx skills add Kaos599/professional-skills --skill anti-slop-writing

# Globally, across all projects
npx skills add -g Kaos599/professional-skills --all
```

### Claude Code: as a plugin

This repository is a valid Claude Code plugin with all three skills bundled under `skills/`.

```bash
claude plugin marketplace add Kaos599/professional-skills
claude plugin install professional-skills
```

Or install the skills directly:

```bash
npx skills add Kaos599/professional-skills -a claude-code --all
```

### Codex: as a plugin

This repository is a valid Codex / ChatGPT plugin (`.codex-plugin/plugin.json`) with a repo marketplace.

```bash
codex plugin marketplace add Kaos599/professional-skills
```

Then open Codex and install **Professional Skills** from the `/plugins` browser, or install the skills directly:

```bash
npx skills add Kaos599/professional-skills -a codex --all
```

> [!TIP]
> **Private repository?** All three install paths work with your existing `gh` / git credentials; no extra setup needed.

### Without installing

Point your agent at the folder, or copy the skill folders anywhere on the standard `SKILL.md` discovery paths (`.claude/skills/`, `.agents/skills/`, ...):

```bash
cp -R skills/anti-slop-writing ~/.agents/skills/
cp -R skills/technical-content-writer ~/.agents/skills/
cp -R skills/tech-blog-series ~/.agents/skills/
```

---

## Try it

Prompts that trigger the skills:

```
This draft reads like AI slop. Make it sound like me.            -> anti-slop-writing
Does this sound like it was written by a person? Be honest.      -> anti-slop-writing (audit)
Write a LinkedIn post about the inference stack we just shipped. -> technical-content-writer
Turn my README into a blog post that engineers will trust.       -> technical-content-writer
Plan a 3-post series on how our ingest pipeline works.          -> tech-blog-series
Make the figures for this post, and review it with the panel.   -> tech-blog-series
```

## Repository structure

```
professional-skills/
├── .claude-plugin/          Claude Code plugin (plugin.json + marketplace.json)
├── .codex-plugin/           Codex / ChatGPT plugin manifest
├── .agents/plugins/         Codex repo marketplace
├── skills/
│   ├── anti-slop-writing/
│   │   ├── SKILL.md
│   │   ├── references/      banned vocabulary, structural patterns, rubric, code slop, worked examples
│   │   └── scripts/         slop_scan.py (read-only mechanical scanner)
│   ├── technical-content-writer/
│   │   ├── SKILL.md
│   │   └── references/      voice protocol, playbooks, editing passes, exemplars, personas
│   └── tech-blog-series/
│       ├── SKILL.md
│       ├── references/      workflow, intake, writing standard, figure system, review panel, lessons
│       ├── templates/       SERIES_STANDARD, FACTS, NOTES, post skeleton
│       ├── scripts/         check_post, build_preview, shoot_figures, figure_kit (stdlib only)
│       └── examples/        filled-in standard, fact ledger, cold opens, review report, example figures
├── README.md
└── LICENSE
```

All three skills follow the standard `SKILL.md` + `references/` Agent Skills layout, so any host (Claude Code, Codex, skills.sh, or any agent that reads `SKILL.md` files) picks them up automatically.

## Adding a voice to technical-content-writer

Drop `NN-short-slug.md` into `references/exemplars/` with the frontmatter header documented in that folder's README. Paste the piece **verbatim**, typos and all; those are signal. Set `authored: true` for your own writing, `authored: false` for writing you admire; the protocol weights them differently.

## Provenance

The anti-slop and writing-craft content is distilled from a harvest of **100 published skills on skills.sh** (~387,000 words across 45 anti-slop and 55 writing-craft skills), analyzed with ban-context document frequency so skills that *ban* a word are counted separately from skills that *use* it. The exemplars and house-style measurements come from a separate pass over real published technical writing, with sources cited per entry. `tech-blog-series` is distilled from building a real multi-post technical series through six drafts and three review rounds; its lessons, rules and examples are generalized from that run, and its example series is invented.

---

<div align="center">

**Professional Skills** · MIT License · Built for Claude Code, Codex, and skills.sh

[Agent Skills](https://agentskills.io) · [Report an issue](https://github.com/Kaos599/professional-skills/issues)

</div>
