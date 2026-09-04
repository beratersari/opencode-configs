---
name: cpp-headers-odr
description: C++ header, ODR, and ABI review. Load when the diff changes a header (*.h, *.hh, *.hpp, *.hxx, *.inl) or moves a symbol between header and source. Do not load for .cpp-only edits that do not change a published declaration. Dialect skill already loaded this turn is a hard ceiling.
license: MIT
compatibility: opencode
---

# C++ headers, ODR, ABI

Review **this change** for One Definition Rule and published-API
breaks. Project rules and the loaded dialect skill still win.

## Look for

- Missing or colliding include guards / `#pragma once` plus a
  second guard name that already exists.
- `using namespace` in a header.
- Non-inline function or static data **defined** in a header
  (ODR / duplicate symbols).
- Include what you use: a header that needs a complete type but
  only forward-declares it (or the reverse: includes a heavy
  header when a pointer/reference would do).
- Default argument added or changed on a published function
  (callers compiled against the old header silently change).
- Layout change of a published struct (member add/remove/reorder,
  virtual added) without an ABI story. Flag when this type is
  used across a library boundary.
- Inline vs out-of-line change that alters whether a symbol is
  exported.
- Macro that evaluates an argument twice or lacks parentheses.

## Impact

`git grep` the header stem and the changed declarations. Every
includer is a dependent. A default-argument or layout change in
an unchanged caller is in scope.

## Do not flag

- Private headers used in one TU.
- “Add `#pragma once`” when a correct unique guard already exists.
