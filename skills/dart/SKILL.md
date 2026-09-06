---
name: dart
description: Dart / Flutter skill. Load when the diff changes *.dart, pubspec.yaml, or pubspec.lock.
license: MIT
compatibility: opencode
---

# Dart / Flutter

Project rules still win. Honor the SDK constraint in `pubspec.yaml`.

## Look for

- Unawaited `Future` that can fail (missing `unawaited` /
  `await` / `.catchError` on a path this change added).
- `!` on a nullable that can be null.
- `setState` after `dispose`; use a mounted check.
- Missing `dispose` on a `Controller` / `FocusNode` this
  widget created.
- Building widgets in `build` that should be `const` only
  when the project already treats that as a lint.
- Isolate / compute: passing a non-sendable closure.

## Do not flag

- Preferring Riverpod vs Bloc as a style war.
- Suggesting Dart 3 patterns if the SDK constraint is lower.
