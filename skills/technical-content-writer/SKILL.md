---
name: technical-content-writer
description: Write technical content that sounds like a specific human wrote it - LinkedIn posts, blog posts, threads, newsletters, essays about engineering and infrastructure subjects. Derives a voice signature from exemplars before drafting, forces mechanism and numbers over adjectives, and runs an anti-slop gate before output. Use when writing or rewriting any technical content for a public audience.
---

# Technical Content Writer

Distilled from 55 published writing-craft skills (copywriting, LinkedIn, ghostwriting,
technical writing, brand voice, content strategy) plus 45 anti-slop skills. Method and
provenance in `../anti-slop-writing/references/corpus-evidence.md`.

## What this is for

Content about technical subjects, written for people who could tell if you were faking it.
Infrastructure, model serving, data pipelines, systems tradeoffs. The reader can check your
claims, so the writing has to survive being checked.

That constraint is the whole design. Most content-writing advice optimises for persuasion.
This optimises for **being right in a way that is also readable**, which is a different job.

## The order matters

Do not draft first and fix later. Drafting before you have an anchor, persona, and voice signature
produces something you then have to rescue, and rescued drafts keep their original shape.

```
0. Anchor      → what is the actual system, domain constraint, and proof?
1. Persona     → who is the author as an engineer, and what stance do they embody?
2. Calibrate   → voice signature derived from exemplars or author profile
3. Shape       → format mechanics and non-adversarial archetypes
4. Draft       → in the signature and persona, against the anchor
5. Sweep       → six editing passes
6. Gate        → 8-point holistic compliance gate, hard threshold
7. Ship
```

---

## Step 0: Anchor

**No anchor, no piece.** This is the step people skip, and skipping it is why most technical
content reads interchangeably.

Answer all four before writing a word:

| | |
|---|---|
| **The concrete thing** | The specific system, run, architecture, benchmark, or code artifact this comes from. Not the topic. The thing. |
| **The domain constraint / tension** | What statutory, physical, mathematical, or systems constraint makes this hard? What boundary condition must be respected? (Never manufacture artificial contrarianism or strawmen). |
| **The proof artifact** | The number, trace, benchmark, config, or clearing schedule that makes the claim checkable. |
| **The generalizable utility** | The practical pattern or decision procedure the reader can adapt for day-to-day systems. |

Pull these from what the user actually has. If a proof artifact is missing, ask **once**. If
there is still none, narrow the claim until it is honest, write the piece around the mechanism
instead of the result, and flag `[NEEDS PROOF]` inline before publishing.

**Never invent a number, customer, benchmark, incident, or quote.** This is absolute. In
technical content the reader can check, and one invented figure destroys everything else you
wrote.

If a claim cannot be made specific, tag it rather than smoothing it:

```
"The fastest solution on the market."
  → [NO-PROOF] → [PLACEHOLDER: benchmark number or third-party comparison]
```

---

## Step 1: Discover the Author Persona & Stance

**No anonymous, disembodied writing.** Before calibrating sentence rhythm, discover who the author is as a practitioner:

1. **Domain Authority & Seniority:** What is the author's real-world background and technical edge? (e.g., Senior AI Engineer building production multi-agent systems, Staff Systems Architect, High-Taste Frontend/Design Engineer). Never default to treating the author as an apprentice or beginner discovering basic concepts.
2. **Core Strengths to Reflect:** What technical superpowers should be evident in the draft? (e.g., deep multi-agent runtime rigor, high-taste design craft, exact statutory/mathematical accuracy).
3. **Authorial Stance:** How does the author teach? The default stance is **Quiet Production Authority & Peer-to-Peer Teaching**: respectful, encouraging, zero downplaying of other developers, zero failure-framing, first-person singular ("I"), plain English headings.

### Persona Presets & Default Profile
Check `references/personas/`. When writing for **Harsh Dayal** (or when running in Harsh's repositories), automatically load `references/personas/harsh-dayal.md` and `references/exemplars/00-harsh-dayal.md`.

---

## Step 2: Calibrate the voice

Read `references/voice-extraction-protocol.md` and derive a signature from
`references/exemplars/`. Do this every time. Do not carry a signature across sessions from
memory; re-derive it, because the exemplar set changes.

If the user names a target voice not in the exemplars, ask for 3 to 5 samples of it. If they
have none, say so plainly and write in the house signature derived from what is there.

Output a compact `VOICE SIGNATURE` block before drafting. It is an operational spec, not
literary criticism. You will check the draft against it in Step 5.

**To add a voice:** drop samples into `references/exemplars/` as
`NN-short-slug.md` with the front-matter header shown in that folder's README. No code change.

---

## Step 3: Shape

Pick the format, then load its mechanics from `references/structure-playbooks.md`.
That file holds the hard numbers: character limits, fold positions, paragraph lengths,
hashtag placement, CTA position, and the archetypes that fit technical material.

Then pick a **register** from `references/house-styles.md`: analytical, opinionated survey, long
explainer, or institutional procedural. That file carries measured signatures from real
published technical writing.

Three decisions before drafting:

**Which archetype?** Technical content mostly works in non-adversarial archetypes:
`domain constraint → architecture / DAG → deterministic guarantees` ·
`production pattern → personal system → protocol / metrics payload` ·
`decision → tradeoff map → recommendation` ·
`benchmark → physical limit → mechanism`

**Persuasion frameworks (PAS, AIDA, BAB) are STRICTLY BANNED for technical writing.** Applying PAS to an engineering post produces manufactured pain points and downplaying that technical readers filter out on sight. Always use an engineering archetype.

---

## Step 4: Draft

Write against the anchor, in the persona, in the signature, in the shape. Rules that apply to every draft:

**First-person builder voice.** If an individual engineer built the system, use clear, grounded first-person singular ("I"). Never retreat into the detached academic third-person or royal "we".

**Plain English headings over jargon theater.** Use honest, descriptive terms. Reject inflated buzzwords (`"dashboard"` not `"cockpit"`, `"clearing timeline"` not `"tranches"`, `"accumulated clutter"` not `"accretion drift"`).

**Zero downplaying of others.** Never open or frame with "most developers do X with toys". Domain constraints are the only antagonist. True authority is quiet; let the problem carry the piece.

**Problem-explanation over failure-framing.** Frame headings and arguments around domain constraints (`"The Real Challenges of Automating Personal Finances"`), never around failure (`"Why standard prompts break down"`).

**Lead with the mechanism, not the outcome.** "Decode is bottlenecked on memory bandwidth because every step re-reads the weights" beats "decode is slow."

**Every claim carries a verifiable metric or statutory section.** State the exact statutory code (Section 112A, Section 50AA), protocol (MCP JSON-RPC), or number (38% overlap, 0.38% TER, ₹6,840 Cr AUM, 68.4% downside capture, T+2 vs T+4 clearing).

**Grounded everyday utility over enterprise grandiosity.** End on practical, transparent systems for solving day-to-day problems. Never posture about "enterprise infrastructure."

**Balanced cadence.** Use 2–4 sentence narrative paragraphs that give the eye breathing room. Restrict bullet points strictly to discrete sets; never dump monolithic text or bulleted shopping lists.

---

## Step 5: Sweep

Six passes, in order, each on the whole piece. Full checklists in `references/editing-passes.md`.

1. **Clarity & Plain English Headings:** Can a competent reader follow it without stumbling? Are all headings free of jargon theater ("cockpit", "tranches")?
2. **Problem Framing:** Are sections framed around domain constraints rather than failure ("breaking down")?
3. **Authority & Stance:** Does the author sound like an experienced practitioner? Is there zero downplaying of peers? Does it end on grounded utility rather than enterprise posturing?
4. **Rigor & Proof:** Are all statutory tax codes, protocols, and exact numbers intact and unabridged?
5. **Specificity & Cadence:** Run the portability test. Are paragraphs balanced (2-4 sentences) with zero bullet dumps?
6. **Voice & Holistic Balance:** Read against the author persona and voice signature. Does quiet authority coexist with accessible peer teaching?

Score each 0 to 10. Below 8 on any pass, fix and re-run that pass. Do not proceed on a 7.

---

## Step 6: Gate

**Hard gate. Do not skip and do not ship below threshold.**

Run the 8-point holistic compliance gate:

- [ ] **Author Authority Intact:** AI Engineer distilling production runtime patterns; zero apprentice/hobbyist apologies.
- [ ] **Zero Downplaying of Others:** No "most developers...", "unlike prompt toys". Domain constraints are the only antagonist.
- [ ] **Problem-Explanation Framing:** Headings and arguments explain domain constraints; zero failure-framing.
- [ ] **Plain English Headings:** Zero jargon theater ("cockpit", "tranches", "accretion drift").
- [ ] **Grounded Everyday Utility:** Real practical systems; zero enterprise grandiosity.
- [ ] **Zero Dilution of Technical Rigor:** Statutory laws (Section 112A, 50AA), MCP JSON-RPC protocol, metrics, and clearing DAG timings preserved and unabridged.
- [ ] **Substance Density & Balanced Cadence:** High signal, light feel; 2-4 sentence narrative paragraphs; no bullet dumps.
- [ ] **Holistic Dialectic Check:** Authority preserved without arrogance; clarity preserved without academic whitepaper slop.

---

## Step 7: Ship

Deliver the finished piece plus:

```
## Anchor used
concrete thing · domain constraint · proof · utility

## Persona & Voice applied
[author persona + voice signature]

## Compliance Gate Scores
clarity 10/10 · framing 10/10 · authority 10/10 · rigor 10/10 · cadence 10/10 · voice 10/10
anti-slop: 0 pattern families

## Needs your input
[any [NEEDS PROOF] items, or "none"]
```

---

## Hard rules

- Never invent a statistic, benchmark, customer, incident, quote, or result.
- Never state a claim more confidently than the evidence supports.
- Never downplay other developers or treat peers as inferior ("most developers use toys").
- Never frame headings around others "failing" or "breaking down"; frame around domain constraints.
- Never replace confident first-person singular ("I built") with detached academic third-person ("the system was evaluated") or the royal "we".
- Never let a framework override the voice signature or author persona.
- Never ship past the Step 6 gate.

## Done =

A piece anchored in something real, in an authentic persona and voice, where every claim
is checkable, that passes the 8-point holistic gate, and that gives the reader practical utility.
