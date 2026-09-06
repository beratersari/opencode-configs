---
name: scala
description: Scala skill. Load when the diff changes *.scala, *.sc, build.sbt, or project/*.scala.
license: MIT
compatibility: opencode
---

# Scala

Project rules still win. Honor `scalaVersion` (2.13 vs 3).

## Look for

- Discarded `Future` / `IO` without execution or error
  channel this change introduced.
- Mutable `var` shared across threads without synchronization.
- `asInstanceOf` / `null` where `Option` was the local style.
- Implicit / given search that changes overload resolution
  in a surprising way at this call site.
- Pattern match that is not exhaustive on a sealed hierarchy
  this change extended.
- Blocking (`Await.result`) on an execution context used
  for async work.

## Do not flag

- Cats vs ZIO vs Future as a rewrite.
- Suggesting Scala 3 syntax in a 2.13-only module.
