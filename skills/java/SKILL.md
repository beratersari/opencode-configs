---
name: java
description: Java / JVM skill. Load when working with *.java, pom.xml, build.gradle, or *.kt that is JVM-only. Use for implement, debug, or review.
license: MIT
compatibility: opencode
---

# Java

Project rules still win. Honor the project’s language level.

## Rules

- Close resources with try-with-resources (`AutoCloseable`).
- `equals`/`hashCode` must stay consistent. Do not use
  mutable fields in `hashCode` for map keys.
- `==` on `Integer` cache vs value: use `equals` for boxed.
- `SimpleDateFormat` is not thread-safe. Prefer
  `DateTimeFormatter` (Java 8+).
- Catching `Exception`/`Throwable` and continuing is a bug
  unless you rethrow or record a fatal.
- `optional.get()` without `isPresent` / `orElse`.
- Spring: constructor injection over field `@Autowired` when
  the project already does that.
- Do not suggest records / sealed / virtual threads unless
  `maven.compiler.release` / `--release` allows it.

## Do not

- Flag checked exceptions as “just use RuntimeException”.
