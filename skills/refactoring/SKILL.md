---
name: refactoring
description: Behavior-preserving refactor skill. Load when renaming, extracting, moving files, or simplifying without a behavior change. Combined from oh-my-opencode-slim simplify. Use for implement or review.
license: MIT
compatibility: opencode
---

# Refactoring

## Rules

- One behavior-preserving step at a time. Do not mix a
  feature with a rename of 40 files.
- Tests that encode the old contract must stay green
  (or be updated in the same change with a reason).
- Extract only when there are ≥3 copies or a real
  boundary (Rule of Three).
- Blast radius: a public symbol rename needs all
  in-repo callers (`git grep`).
- Do not invert a working abstraction because a new
  name feels nicer (Sandi Metz: duplication > wrong
  abstraction until the third time).

## Do not

- “Rewrite the module” as a review suggestion.
