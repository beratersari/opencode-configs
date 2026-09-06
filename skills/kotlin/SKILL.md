---
name: kotlin
description: Kotlin skill. Load when the diff changes *.kt, *.kts, or Gradle Kotlin DSL. Use for Android and JVM Kotlin.
license: MIT
compatibility: opencode
---

# Kotlin

Project rules still win. Honor the project's language version.

## Look for

- `!!` on a nullable that this change can actually be null.
- `lateinit` read before init; race if another thread sets it.
- `==` vs `===` (structural vs referential).
- Coroutine: capturing a cancelled `Job`, or `runBlocking` on
  the UI / main dispatcher.
- `GlobalScope.launch` in app code (leaks; use a scoped job).
- Data class `copy` that drops a required invariant.
- Java interop: platform types used without a null check the
  call site now needs.

## Do not flag

- `.let` / `.apply` style nits.
- Suggesting Compose APIs in a non-Compose module.
