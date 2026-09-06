---
name: typescript
description: TypeScript skill. Load when the diff changes *.ts, *.tsx, tsconfig*.json, or *.d.ts. Do not load for JS-only repos with no TS files.
license: MIT
compatibility: opencode
---

# TypeScript

Project rules still win. Honor `tsconfig` `strict` / `target`.
Do not demand TypeScript in a JS-only tree.

## Look for

- `any` / `as any` / `@ts-ignore` hiding a contract break this
  change introduced.
- `!` non-null assertion on a value that can be undefined.
- Type that lies (`User` without `id` when callers require it).
- `enum` numeric pitfalls; prefer string unions the file
  already uses.
- Widening `string` where a literal union was the API.
- `satisfies` / `const` assertion only if `target` allows it.
- Excess property checks bypassed via index signature or
  spread of `any`.

## Do not flag

- Missing types on a file that is already loosely typed.
- `any` in a test mock the project already uses.
