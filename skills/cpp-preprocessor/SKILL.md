---
name: cpp-preprocessor
description: C/C++ preprocessor review. Load when the diff adds or changes macros, #ifdef/#if, include-path tricks, or X-macros. Do not load for files that only include headers. Dialect skill already loaded this turn is a hard ceiling.
license: MIT
compatibility: opencode
---

# C++ preprocessor

Review **this change** for macro and conditional-compilation
bugs. Project rules and the loaded dialect skill still win.
Prefer `const`, `enum`, or `inline` over a new `#define` when
the dialect already allows it.

## Look for

- Macro that evaluates an argument twice (`MAX(i++, b)`).
- Macro missing parentheses around the body or arguments.
- `#define` that swallows a trailing semicolon or breaks `else`.
- `#ifdef` that leaves an undeclared identifier on one
  platform this MR claims to support.
- Include guard that is not unique (`UTIL_H` in two headers).
- `#include` of a generated path that is not in this MR or
  CMake, so a clean clone will not build.
- Token-paste / stringize that produces an invalid identifier.
- Macro that changes a published API between TUs (ODR).

## Impact

A public macro is part of the API. `git grep` the macro name
in headers and sources, including `#ifdef` sites.

## Do not flag

- Existing project-wide feature macros this MR only reads.
- One-line include guards that are already unique.
