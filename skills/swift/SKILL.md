---
name: swift
description: Swift / SwiftUI skill. Load when the diff changes *.swift, Package.swift, *.xcodeproj, or *.xcworkspace sources.
license: MIT
compatibility: opencode
---

# Swift

Project rules still win. Honor the project's Swift language mode.

## Look for

- Force unwrap `!` / `try!` on a path that can fail.
- Retain cycle: `self` captured strongly in a escaping
  closure; use `[weak self]` when the object owns the closure.
- `unowned` on something that can actually be nil.
- Data race: mutating a class from a background queue without
  isolation (actors / `@MainActor` when that is the project).
- SwiftUI: mutating `@State` from a background task; missing
  `id` on a `ForEach` of dynamic data.
- `try?` that swallows an error this change should surface.

## Do not flag

- SwiftUI view-builder style.
- Suggesting Observation / Swift 6 isolation unless the
  package already uses that mode.
