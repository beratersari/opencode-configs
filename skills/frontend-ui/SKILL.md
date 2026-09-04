---
name: frontend-ui
description: Frontend UI review. Load when the diff changes HTML, CSS, React/Vue/Svelte components, Tailwind, or design-system tokens. Combined from oh-my-opencode frontend-ui-ux and addyosmani/agent-skills frontend-ui-engineering. Do not load for backend-only diffs.
license: MIT
compatibility: opencode
---

# Frontend UI (review)

Review **this change** for a broken or inaccessible UI. Project
rules still win. Combined from oh-my-opencode `frontend-ui-ux`
and addyosmani `frontend-ui-engineering`.

## Look for

- Interactive `div`/`span` instead of `button`/`a` (no keyboard).
- Missing label on an input, or icon-only button with no
  `aria-label`.
- Color as the only state (red/green with no text or icon).
- Contrast below 4.5:1 for body text this MR introduced.
- No empty / loading / error state on a new list or fetch.
- Heading level skipped (`h1` → `h3`).
- Hard-coded spacing / hex that ignores the project’s scale
  or tokens (`13px`, random purple).
- Prop-drilled unused props more than ~3 levels on a component
  this MR added.
- Missing `key` on a new list, or index keys on a reorderable
  list.

## Impact

A presentational component used by several pages is in scope
at every call site. `git grep` the export.

## Do not flag

- “Looks generic / AI aesthetic” as a defect unless it
  violates this repo’s tokens.
- Visual taste when the design system is followed.
