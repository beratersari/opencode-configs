---
name: tdd
description: Test-driven development skill. Load when implementing a bugfix or new behavior, or when a change has no failing test. Combined from obra/superpowers test-driven-development. Use for implement; reviewers may load to judge missing red-green.
license: MIT
compatibility: opencode
---

# TDD

Combined from obra/superpowers `test-driven-development`.

## Rules

- Red: write a test that fails for the right reason.
- Green: smallest change that passes.
- Do not write production code without a failing test
  for a bugfix.
- One behavioral assertion per test when possible.
- Do not mock the unit under test.

Implementing agents: run the test and quote the failure
before editing production code.

Reviewing agents: flag a bugfix with no test that would
have failed before the patch (`verification`).

## Do not

- Demand TDD history on a spike the project labeled as
  such.
