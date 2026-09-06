---
name: html-css
description: HTML and CSS skill. Load when the diff changes *.html, *.css, *.scss, *.sass, or *.less. Use with frontend-ui / accessibility when those apply.
license: MIT
compatibility: opencode
---

# HTML / CSS

Project rules still win.

## Look for

- `innerHTML` / `document.write` with unsanitized data.
- Missing `alt` on an `<img>` this change added (meaningful
  image). Decorative should be `alt=""`.
- Form control without a `<label>` / `aria-label`.
- CSS that removes focus outline with no replacement.
- `position: fixed` overlay that traps focus / cannot
  be dismissed with Escape if the project already does that
  for sibling dialogs.
- Specificity wars — only if this change breaks an existing
  cascade the file already relies on.

## Do not flag

- Tailwind vs CSS modules as a rewrite.
- Pixel-perfect spacing nits.
