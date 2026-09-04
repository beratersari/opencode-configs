---
name: root-cause
description: Root-cause review of suggested or implied fixes. Load when the MR is a bugfix, a “quick patch”, or adds a fallback/retry/default that hides an error. Combined from obra/superpowers systematic-debugging. Do not load for greenfield features with no failure path.
license: MIT
compatibility: opencode
---

# Root cause (review)

Adapted from obra/superpowers `systematic-debugging`. This
agent does not apply fixes; it flags patches that treat the
symptom.

**Iron law for findings:** a Suggested fix must name the
root cause, not only paper over the crash.

## Look for

- Catch / default / retry / `|| 0` that swallows the real
  error this MR just hit.
- A null-check added at the use site when the producer still
  returns a dangling / empty value (fix at the source).
- “Works on my machine” fallbacks (hard-coded path, ignored
  HRESULT, empty `catch`).
- Multiple independent bandaids in one MR that each fix a
  new symptom of the same invariant break.
- A test that only asserts “does not throw” with no
  reproduction of the original failure.

## How to judge

Trace the bad value **backward** (`git grep` callers, then
the producer). If the Suggested fix would still leave the
producer wrong, say so and point at the producer.

## Do not flag

- A real root-cause fix plus one local guard as defense in
  depth, when both are justified.
