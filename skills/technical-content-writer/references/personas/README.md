# Personas

Researched voice profiles of well-known technical writers. Each file captures one persona:
how they write, how they present facts, how they explain difficult things, how they present
themselves, their signature moves, **verbatim excerpts** from their published work (with
source URLs), and a canonical post list.

## Purpose

1. **A matching lens for Step 1** (Discover the Author Persona & Stance): when discovering an
   author's stance, identify which preset their writing most resembles. This calibrates how the
   draft should frame authority, facts, and explanation - without imitation of the words.
2. **A target voice:** if the user names one of these writers as the target voice, derive the
   `VOICE SIGNATURE` (Step 2) from the persona file's verbatim excerpts, then verify the draft
   against it in Step 5.

## Use rules

- Excerpts are quoted verbatim from the linked sources. Never quote them into output; use them
  to *calibrate* stance and cadence. The voice signature mechanism (Step 2) is how a persona
  becomes operational.
- A persona describes **stance and craft**, not opinions to copy. DHH's conviction does not
  license contempt for people; Karpathy's self-deprecation is earned, not performed.
- The stance must still match the actual author. A hobbyist does not borrow Torvalds' maintainer
  authority; a researcher does not borrow an evangelist's sign-off.
- A user's own profile placed here as `<author-name>.md` takes precedence over presets.

## Presets

| File | Persona | Archetype | Home |
|---|---|---|---|
| `01-andrew-ng.md` | Andrew Ng | the Calm Evangelist-Teacher | deeplearning.ai/the-batch |
| `02-andrej-karpathy.md` | Andrej Karpathy | the Patient Builder-Researcher | karpathy.github.io |
| `03-boris-cherny.md` | Boris Cherny | the Pragmatic Toolsmith | borischerny.com |
| `04-dhh.md` | David Heinemeier Hansson | the Opinionated Systems-Manifesto Writer | world.hey.com/dhh |
| `05-simon-willison.md` | Simon Willison | the Field-Notes Documentarian | simonwillison.net |
| `06-linus-torvalds.md` | Linus Torvalds | the Show-Me-The-Code Maintainer | LKML / lore.kernel.org |

## How the personas relate to the house rules

- **Facts:** Ng, Karpathy, Willison, and Torvalds all present first-party, checkable evidence
  (benchmarks they ran, receipts, patches). This is why the skill's Prove-it sweep exists.
- **Teaching:** Ng and Karpathy teach by analogy-then-mechanism; Cherny teaches by bad→good
  contrast; Willison teaches by experiments the reader can re-run. None of them downplay
  readers or peers - the "zero downplaying" rule is descriptive of how the best actually write.
- **Authority:** DHH and Torvalds show that strong verdicts do not require sneering; their
  targets are ideas, orthodoxies, and broken designs - never the reader. This is the line the
  "quiet authority" rule encodes.
