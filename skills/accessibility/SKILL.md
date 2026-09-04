---
name: accessibility
description: Accessibility review (WCAG). Load when the diff changes UI, forms, dialogs, focus, ARIA, or images. Combined from addyosmani/agent-skills frontend-ui-engineering accessibility section. Do not load for non-UI diffs.
license: MIT
compatibility: opencode
---

# Accessibility

Review **this change** against WCAG 2.1 AA for what this MR
touched. Combined from addyosmani `frontend-ui-engineering`.

## Look for

- Click handler on a non-focusable element.
- Dialog/modal that does not move focus in, or does not
  return it on close.
- Image with no `alt` (or `alt` that repeats adjacent text).
- Form error not tied to the field (`aria-describedby` /
  `aria-invalid`).
- `outline: none` with no visible focus replacement.
- Motion this MR adds with no `prefers-reduced-motion` path
  when the animation is more than a short fade.
- Hit target smaller than ~24px on a new control.

## Impact

A shared `Modal` / `Button` change hits every screen. `git grep`
the component.

## Do not flag

- Decorative images that already have `alt=""`.
- Demanding a full axe-core run this project does not have.
