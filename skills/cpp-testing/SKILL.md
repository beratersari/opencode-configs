---
name: cpp-testing
description: C++ test review. Load when the diff adds or changes tests, gtest/gmock, Catch2, doctest, Boost.Test, CTest, or new public behavior with no test file. Do not load when the MR is build-only or comment-only. Dialect skill already loaded this turn is a hard ceiling.
license: MIT
compatibility: opencode
---

# C++ tests

Review **this change** for missing or lying tests. Project rules
and the loaded dialect skill still win. Do not demand a new
framework or sanitizer the repo does not already run.

## Look for

- New behavior (especially copy/move, empty container, error
  path, or a changed contract) with no test that would fail if
  the bug returned.
- Test that asserts implementation details (private layout)
  instead of the contract.
- `EXPECT_*` that continues after a hard invariant; use
  `ASSERT_*` when later lines are UB on failure.
- Death tests / signal tests that are flaky on the project’s
  claimed platforms.
- Fixture that shares mutable state across tests.
- `add_test` / `gtest_discover_tests` missing for a new
  executable this MR adds.
- A test that “passes” by invoking UB (the defect programs
  themselves) without documenting that they are expected to
  crash or leak.

## Impact

If a production function’s contract changed, existing tests
that still encode the old contract are in scope even if this
MR did not touch them. `git grep` the symbol in `*test*`.

## Do not flag

- “Add CI” when the project has none and this MR is not about
  CI.
- Coverage percentage as a standalone nit.
