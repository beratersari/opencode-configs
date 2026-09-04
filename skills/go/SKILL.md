---
name: go
description: Go language skill. Load when working with *.go, go.mod, go.sum, or GOPATH/modules. Use for implement, debug, or review.
license: MIT
compatibility: opencode
---

# Go

Project rules still win.

## Rules

- Check every error. Do not assign `_` to an error you can handle.
- Do not share a `map` or slice header across goroutines without
  a mutex or ownership transfer.
- `context.Context` is the first arg on blocking or RPC calls.
  Honor `ctx.Done()`. Do not store `Context` on a struct.
- Close what you open (`Body.Close`, `Rows.Close`) with `defer`.
- `init()` that does I/O or registration order tricks — avoid.
- Module path / `replace` in `go.mod` must match what you import.
- Nil interface vs nil pointer: a nil `*T` in an `error` interface
  is not `== nil`.
- Loop variable capture: Go 1.22+ is per-iteration; older needs
  `x := x` if the project’s version is older.

## Do not

- Suggest generics if `go` version in `go.mod` is before 1.18.
- Flag `if err != nil` as verbose.
