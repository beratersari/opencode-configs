---
name: javascript
description: JavaScript and TypeScript review. Load when the diff changes *.js, *.jsx, *.ts, *.tsx, *.mjs, *.cjs, or package.json app code. Do not load when no JS/TS files changed.
license: MIT
compatibility: opencode
---

# JavaScript / TypeScript

Review **this change** for JS/TS correctness. Project rules
still win. Do not demand TypeScript in a JS-only repo.

## Look for

- Unhandled promise (`async` function called without `await`
  / `.catch` on a path that can reject).
- `==` where `null`/`undefined`/string coercion changes
  control flow this MR added.
- Prototype pollution: assign `body` onto `{}` with
  `__proto__` / `constructor` keys.
- XSS: `innerHTML`, `document.write`, or `eval` / `new Function`
  on user data.
- `let` / `const` temporal dead zone, or `var` leak into a
  closure in a loop.
- React: hook after a conditional, stale closure, missing
  effect cleanup this MR introduced.
- `any` / `@ts-ignore` hiding a real contract break.

## Impact

A changed export’s importers are in scope. `git grep` the
export name.

## Do not flag

- Semicolons / Prettier nits.
- `any` in a test mock the project already uses.
