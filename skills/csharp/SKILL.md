---
name: csharp
description: C# / .NET skill. Load when working with *.cs, *.csproj, *.sln, or Directory.Build.props. Use for implement, debug, or review.
license: MIT
compatibility: opencode
---

# C#

Project rules still win. Honor `LangVersion` / TFM.

## Rules

- `IDisposable`: `using` / `await using`. Do not fire-and-forget
  a `Task` that owns a resource.
- `async void` only for event handlers.
- `ConfigureAwait(false)` in libraries; UI apps may need the
  context.
- `==` on strings: ordinal vs culture. Be explicit for IDs.
- Nullable reference types: do not `!` away a real null.
- `lock` on a `this` or a `string` interned literal.
- EF: N+1, tracking vs no-tracking, unbounded `ToList()`.
- Do not suggest `required` / file-scoped namespaces if the
  TFM is older than the feature.

## Do not

- Rewrite the project into minimal APIs as a style nit.
