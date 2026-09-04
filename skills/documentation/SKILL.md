---
name: documentation
description: Docs skill (Diátaxis). Load when changing README, API docs, tutorials, or comments that teach. Use for implement, debug, or review.
license: MIT
compatibility: opencode
---

# Documentation

Inspired by Diátaxis (mcollina/skills documentation).

## Rules

- Tutorial vs how-to vs reference vs explanation mixed
  in one page so neither a new user nor an expert can
  scan it.
- README command that does not run (wrong flag, missing
  tool this MR just renamed).
- Public API with no contract (args, errors, thread
  safety) when the project documents siblings.
- Comment that contradicts the code (rot).
- Secret or internal URL pasted into docs.

## Do not

- Demand a full Diátaxis site for a one-file tool.
- Flag missing comments on obvious code.
