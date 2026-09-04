---
name: performance
description: Performance skill. Load when changing hot loops, queries, allocations, caches, or N+1 / O(n²) paths. Use for implement, debug, or review.
license: MIT
compatibility: opencode
---

# Performance

## Rules

- N+1 queries or RPCs on an unbounded collection.
- O(n²) on input the API does not bound.
- Copy of a large buffer/string in a loop.
- Sync I/O on a request thread / UI thread.
- Unbounded cache or queue (memory growth).
- Missing index / filter that will scan a table this
  change newly queries.
- Extra serialize/deserialize on a hot path.

Flag only with a realistic size or rate. Do not invent
micro-benchmarks.

## Do not

- `reserve` / `emplace` as a standalone nit.
- “Rewrite in rust” as a performance fix.
