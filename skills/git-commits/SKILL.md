---
name: git-commits
description: Atomic commit skill for implementers. Load when committing, splitting history, or writing commit messages. Combined from oh-my-opencode git-master. Do not load in the read-only review agent.
license: MIT
compatibility: opencode
---

# Git commits

Combined from oh-my-opencode `git-master`. Match the repo’s
existing `type(scope):` style when present (for example
`feat|fix|refactor|test|docs|chore`).

## Rules

- One logical change per commit. Do not mix a behavior
  fix with an unrelated rename.
- Subject: imperative, ≤72 characters, no trailing period.
- Body: why, not a file list. Wrap at 72.
- Never commit `.env`, tokens, or generated secrets.
- Do not force-push `main`.
- Split when `git diff --stat` shows unrelated paths.

## Do not

- `update` / `wip` / `misc` as the subject.
