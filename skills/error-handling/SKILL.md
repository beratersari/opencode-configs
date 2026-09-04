---
name: error-handling
description: Cross-language error-handling skill. Load when changing try/catch, Result, error codes, retries, or fallbacks. Use for implement, debug, or review.
license: MIT
compatibility: opencode
---

# Error handling

## Rules

- Swallowing an error and continuing in a bad state.
- Retrying a non-idempotent call without a key.
- Mapping every failure to 500 / generic “error”.
- Losing the cause (empty catch, `raise e` that resets
  the stack when the language has `raise` / `throw;`).
- Sentinel values (`-1`, `null`) that collide with valid
  data, when the project has `Result` / optional.
- Two error channels at once (errno and exception) that
  callers can disagree on.

Suggested fixes must name the root cause (`root-cause`).

## Do not

- Demand exceptions in an error-code codebase or the
  reverse.
