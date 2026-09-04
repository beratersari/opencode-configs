---
name: cpp-numerics
description: C++ integer, size, and floating-point review. Load when the diff does arithmetic on sizes, indices, enumerations, bit shifts, or floats, or mixes signed/unsigned. Do not load for code with no numeric logic. Dialect skill already loaded this turn is a hard ceiling.
license: MIT
compatibility: opencode
---

# C++ numerics

Review **this change** for overflow, wrap, and precision bugs.
Project rules and the loaded dialect skill still win.

## Look for

- Signed overflow (UB). Shift into or past the sign bit.
- `size_t` vs signed `int` in a loop (`i < v.size()` with
  `int i` can warn and, if `size` exceeds `INT_MAX`, mis-compare).
- Untrusted value used as a size or index without a range check.
- Multiplication before a capacity check (`n * elem` overflow).
- Unsigned wrap used as a “negative” error (`size_t n = -1`).
- Enum stored in a too-narrow integer; switch that is not
  exhaustive on a changed enum.
- Float equality (`==`) on computed values. Division by zero
  on integers (UB) or floats used as a control flag.
- `memcpy` of a float/int for punning when a `memcpy` into a
  local of the destination type is the portable C++98 path;
  `bit_cast` only at C++20.

## Impact

A new overflow in a size helper is Critical if any caller uses
the result to allocate or index. `git grep` the helper.

## Do not flag

- Constant arithmetic the compiler folds safely.
- Intentional unsigned modular arithmetic that is commented
  and proven (hash, wraparound buffers).
