---
name: debugging
description: Systematic debugging skill for implementers. Load when investigating a bug, test failure, or unexpected behavior before changing code. Combined from obra/superpowers systematic-debugging. Reviewers prefer root-cause.
license: MIT
compatibility: opencode
---

# Debugging

Combined from obra/superpowers `systematic-debugging`.

**No fix without a root cause.**

1. Read the full error and stack.
2. Reproduce, or say you cannot.
3. Check what changed (`git log` / `git diff`).
4. Trace the bad value backward to the producer.
5. One hypothesis, smallest test of it.
6. Then fix at the source. See `tdd` and `verification`.

If three fixes failed, stop and question the design.
Do not stack bandaids.

## Do not

- “Try this” lists without a stated hypothesis.
