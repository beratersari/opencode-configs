---
name: react
description: React skill. Load when the diff changes *.jsx, *.tsx, or files that import react / react-dom. Do not load for Vue/Svelte-only trees.
license: MIT
compatibility: opencode
---

# React

Project rules still win. Honor the project's React major.

## Look for

- Hook after a conditional / in a loop.
- Missing dependency or an unstable object/function dep that
  retriggers an effect every render (this change).
- Stale closure over props/state in an effect or handler.
- Updating state after unmount (fetch without abort /
  cancelled flag).
- `key` index on a reorderable list this change added.
- Direct DOM / `innerHTML` with user data (XSS).
- Server component calling a client-only API (Next App Router)
  if this tree uses that split.

## Do not flag

- Preferring Redux vs Context as a rewrite.
- Class components in a repo that still uses them.
