---
name: cpp-memory-safety
description: C/C++ memory-safety review. Load when the diff uses raw buffers, pointer arithmetic, C string/IO APIs (strcpy, sprintf, gets, scanf, memcpy, memmove), malloc/new, or casts a size from untrusted input. Do not load for pure STL/RAII changes with no raw memory. Dialect skill already loaded this turn is a hard ceiling.
license: MIT
compatibility: opencode
---

# C++ memory safety

Review **this change** for memory corruption and leaks. Project rules
and the loaded dialect skill (`cpp98` or `modern-cpp`) still win.

Fixes must compile at the confirmed standard. Do not suggest
`std::span` before C++20 or `unique_ptr` on C++98.

## Look for

- Unbounded `strcpy` / `strcat` / `sprintf` / `gets` / `scanf("%s")`.
  Need a bound and a guaranteed NUL, or `std::string` if the file
  already uses it.
- `strncpy` / `snprintf` that omit the NUL, or a size of `sizeof(dst)`
  when the destination is not a true array (pointer decay).
- `memcpy` / `memmove` / `memset` with a length from attacker input,
  a signed size, or a type with a user ctor/dtor (not POD / trivial).
- `new`/`delete` mismatch (`new[]` vs `delete`, `malloc` vs `delete`).
- Pointer arithmetic past one-past-the-end; indexing a decayed array
  with a caller-supplied length that is not checked.
- Integer overflow used as an allocation size
  (`n * sizeof(T)` when `n` is untrusted).
- Use-after-free, double-free, returning a pointer/reference to a
  local or to a temporary buffer.
- `realloc` that is used after failure (old pointer is still live)
  or that is assumed not to move.

## Impact

`git grep` the function that owns the buffer. A locally “safe”
helper is still Critical if any caller passes an unbounded or
attacker-controlled length.

## Do not flag

- `memcpy` of a trivial type with a proven constant size.
- Pre-existing C APIs this MR did not touch.
- Style (`nullptr` vs `NULL`) unless it picks the wrong overload.
