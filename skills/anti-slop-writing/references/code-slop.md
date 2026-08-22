# Code slop

AI-generated code has a writing layer: comments, docstrings, names, and defensive ceremony.
This file covers the tells in that layer, plus the structural ones that survive review. Scope
it like everything else here: flag in clusters, fix per occurrence, and treat local style as
the master heuristic. When reviewing changes rather than whole files, work on the diff against
the base branch only.

## Comments

**Restating the signature.**
✗ `# increments i by one` above `i += 1`
✓ Delete it. If the line needs narration, the line is usually wrong instead.

**Narrating phases.**
✗ `// Phase 1: fetch users` · `// Now validate the payload`
✓ Delete. Phase commentary describes the author's journey, not the code's behaviour. An
  assertion or a better name does the job: `assert(ok, 'persisted across restart')`.

**Zero-information docstrings.**
✗ `"""Calculates the total."""` above `calculate_total()`
✓ Either document properly (contract, units, failure modes) or do not document at all. A
  30-line docstring on a private helper is the same failure inverted; both are noise.

**Generic TODOs.** A generated TODO has no owner and no reason.
✗ `// TODO: improve this`
✓ A real TODO carries who, what, and why: `// TODO(alina): batch these calls before the Nov
  migration, see INC-412`. Fails that bar means delete it or make it real.

## Defensive slop

Defensive checks are relative to trust level, not universally virtuous.

- Input validation deep inside trusted internal paths where every caller already guarantees
  the invariant
- try/catch wrapped around code that cannot throw, or `except Exception: pass` swallowing
  real failures
- Impossible-condition branches (`if config == None` under a constructor that rejects null)

The tell is abnormal-for-the-codebase, not existence. A parser validating untrusted input is
correct; a private helper re-validating what its only caller validated two lines up is slop.

## Naming

Slop lives at both extremes:

**Overly generic:** `data`, `result`, `temp`, `item`, `info`, `process`, `handleStuff`. Also
`Helper`, `Manager`, `Handler`, `Util` suffixes that name a category instead of a job, and
`foo`/`bar` outside examples.

**Overly verbose:** `getUserDataFromDatabaseAndReturnResult`. Generated code hedges by naming
every step of its own implementation into the identifier.

✓ Name the concept: `overdue_invoices`, `retryBudget`, not `data2` and not
  `fetchAndValidateRetryConfigurationFromServerStore`.

## Structure tells

- Deep nesting where early returns would flatten it. Generated code grows pyramids because it
  handles each case inline as it thinks of it.
- Type-system escapes: casts to `any` (or the language equivalent) used to silence the checker
  rather than to describe reality.
- Abstraction chains: a factory producing strategies behind an interface with exactly one
  implementation. Design-pattern name-dropping in class names is part of the same tell.
- Copy-paste variants of one function differing by a flag, instead of one parameterised
  function.

## Context matters

Carve-outs that keep this file from over-firing:

- Short generic names are correct in small scopes: `i`, `x`, `acc` in a three-line loop.
- Verbose names can be right at API boundaries where the name is documentation.
- Defensive parsing at every trust boundary touching user input is engineering, not slop.
- A one-implementation interface can be deliberate seam-setting for testing. Judge by whether
  the codebase treats it as a seam.

## Cleanup risk tiers

Map each proposed fix to its verification cost before making it:

| Tier | Meaning | Examples |
|---|---|---|
| Immediate | comment/name/docstring edits | delete restating comment, rename `data` |
| Refactoring | behaviour-preserving but structural | early-return flattening, merging copies |
| Testing-required | touches execution | removing a defensive check, unwrapping try/catch |

Never take a Testing-required action as part of a style pass without saying so in the output.
