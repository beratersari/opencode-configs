---
name: cpp-templates
description: C++ template and generic-code review. Load when the diff adds or changes templates, dependent names, SFINAE, requires/concepts, or variadic templates. Do not load for non-template C++. Never suggest concepts or requires before C++20. Dialect skill already loaded this turn is a hard ceiling.
license: MIT
compatibility: opencode
---

# C++ templates

Review **this change** for template correctness and ODR. Project
rules and the loaded dialect skill still win.

## Look for

- Dependent name missing `typename` or `template` (two-phase
  lookup). Breaks GCC even when MSVC accepted it.
- Template defined only in a `.cpp` (implicit instantiation in
  another TU fails to link) unless there is an explicit
  instantiation for every used type.
- ODR: the same template specialized differently in two TUs, or
  a non-inline function defined in a header.
- SFINAE / `enable_if` that is too loose; the body then misuses
  the type. C++20: a concept that does not match what the body
  actually needs.
- Deduction that silently picks the wrong overload (`T&&` vs
  `const T&`, `initializer_list` hijacking).
- Unconstrained forwarding reference that steals copy/move.
- Variadic pack not forwarded (`std::forward<Args>(args)...`)
  when the confirmed standard has rvalue refs.
- Exporting a template in a public header that now requires a
  heavier include (compile-time / ABI blast radius).

## Impact

`git grep` the template name. Instantiations in unchanged files
are in scope. A constraint change can break a distant caller.

## Do not flag

- “Rewrite this with concepts” on C++17 or earlier.
- Template style / formatting.
