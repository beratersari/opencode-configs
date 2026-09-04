---
name: cpp-exceptions
description: C++ exception-safety review. Load when the diff uses try/catch/throw, noexcept, throw specifications, or acquires more than one resource in a constructor. Do not load when there is no exception or multi-resource path. Dialect skill already loaded this turn is a hard ceiling.
license: MIT
compatibility: opencode
---

# C++ exception safety

Review **this change** for exception safety. Project rules and the
loaded dialect skill still win. Do not suggest `noexcept` on C++98
(`throw()` is the C++98 form and is easy to get wrong).

## Look for

- Destructor that throws (including a member dtor during unwind).
- Constructor that acquires A, then throws before B is owned
  (Sutter: one resource per statement / RAII).
- `new T` and `new U` in the same full-expression (if the second
  throws, the first leaks).
- Basic vs strong guarantee: a mutating function that can throw
  after it has already changed observable state, with no rollback.
- `catch (...)` that swallows and continues in a bad state.
- `catch` by value (slicing). Catch `const std::exception&`.
- Exception specification / `noexcept` that is narrower than what
  callees actually throw (`noexcept` + throw → `terminate`).
- Error code ignored on a path the code claims to handle, or a
  new exception type callers do not catch (`git grep` the callers).

## Impact

If the function’s error channel changed (throws now, or throws a
new type), every caller that assumed the old channel is in scope.

## Do not flag

- Letting an exception propagate from a function that does not
  claim the strong guarantee and has not mutated yet.
- Demanding `noexcept` on every getter.
