---
name: cpp-stl
description: C++ STL and container review. Load when the diff uses std::vector, string, map, unordered_map, deque, list, optional, variant, string_view, span, or algorithms from <algorithm>/<numeric>. Do not load when the change does not touch the standard library. Dialect skill already loaded this turn is a hard ceiling.
license: MIT
compatibility: opencode
---

# C++ STL

Review **this change** for container and algorithm bugs. Project
rules and the loaded dialect skill still win. Do not suggest
`string_view` before C++17 or `span` before C++20.

## Look for

- Iterator / reference / pointer invalidation after `push_back`,
  `reserve` that reallocates, `insert`, `erase`, `rehash`, or
  `operator[]` on `map`/`unordered_map` that inserts.
- `front` / `back` / `operator[]` on empty. `at()` throws; `[]`
  is UB on `vector`/`string` out of range.
- `vector<bool>` proxies: do not take `bool&` or a pointer.
- Algorithm with the wrong iterator pair, or an output range
  that is too small (`std::copy` into an empty vector without
  `back_inserter`).
- `remove` / `remove_if` without the subsequent `erase`.
- Associative container `find` result used without an end check.
- `std::optional` / `value()` / `operator*` on empty (C++17).
- Comparator that is not a strict weak ordering (infinite loop
  or lost elements).
- `std::move` out of a node still in a container, then using
  that element.

## Impact

A helper that returns a reference into a container is only safe
if every caller keeps the container alive and does not reallocate.
`git grep` those callers.

## Do not flag

- Correct index loops.
- `emplace` vs `push_back` as a style nit.
