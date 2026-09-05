---
name: git-commits
description: Atomic commit skill for implementers. Load when committing, splitting history, or writing commit messages. Combined from oh-my-opencode git-master. Do not load in the read-only review agent.
license: MIT
compatibility: opencode
---

# Git commits

Combined from oh-my-opencode `git-master`.

**Discover the format first.** Do not assume a house style.

1. Read `AGENTS.md` (and `CONTRIBUTING.md` / commitlint /
   `commitMsgFormat.md` if present).
2. Read `git log -20 --format=%s` and copy the dominant subject
   pattern.
3. Put the issue key where this repo already puts it (prefix,
   scope, or trailer).
4. If docs and history have no pattern, use
   `[ISSUE-KEY] type: description` with
   `feat|fix|refactor|test|docs|chore|perf|ci|build|revert`.

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
