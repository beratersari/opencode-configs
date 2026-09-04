---
name: verification
description: Evidence review. Load when the MR claims a fix, adds tests, or changes a build/test job. Combined from obra/superpowers verification-before-completion. Do not load for comment-only diffs.
license: MIT
compatibility: opencode
---

# Verification (review)

Adapted from obra/superpowers `verification-before-completion`.
**Evidence before claims.** This reviewer cannot run the
project’s full suite unless the tree already has a command
in the opened files; still flag missing evidence.

## Look for

- A bugfix with no test that would have failed before the
  change (no red-green).
- A test that cannot fail (asserts a tautology, or mocks
  away the unit under test).
- CI job this MR disables or `continue-on-error`s without
  a reason.
- README / commit / MR title that claims “fixed” /
  “all tests pass” while this MR removes the only test of
  that path.
- Golden files or snapshots updated with no explanation of
  the behavior change.

## Impact

If the only proof is “I ran it locally”, say the tree has
no automated witness. Major when this path is a merge gate.

## Do not flag

- Demanding a new CI system the repo does not have.
- Coverage percent as a standalone nit.
