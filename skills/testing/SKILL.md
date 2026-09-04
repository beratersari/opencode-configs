---
name: testing
description: General automated-testing skill (any language). Load when adding or changing tests, fixtures, or test runners. Language-specific extras: cpp-testing, tdd. Use for implement, debug, or review.
license: MIT
compatibility: opencode
---

# Testing

## Rules

- Test the contract, not private layout.
- A bugfix needs a test that failed before the fix
  (`tdd`, `verification`).
- Deterministic: no wall-clock, network, or unordered
  map iteration unless faked.
- Isolation: tests must not depend on run order or
  leftover files.
- Fixture that hides the interesting input.
- Snapshot updated with no note of the behavior
  change.

## Do not

- Coverage percent as the only finding.
- Demand a new framework.
