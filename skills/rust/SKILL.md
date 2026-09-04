---
name: rust
description: Rust language skill. Load when working with *.rs, Cargo.toml, or Cargo.lock. Use for implement, debug, or review.
license: MIT
compatibility: opencode
---

# Rust

Project rules still win. Match the crate’s edition.

## Rules

- Do not `unwrap()` / `expect` on a library path unless a
  programming bug is the only possibility. Return `Result`.
- `clone()` as an escape from the borrow checker is a smell
  when the type is large or interior-mutable.
- `unsafe` needs a documented invariant next to the block.
- `Send`/`Sync` on a type that holds `Rc` or raw pointers is
  unsound.
- Lock poisoning: decide recover vs propagate; do not ignore
  `unwrap` on `Mutex::lock` in a library.
- Async: do not hold a `std::sync::Mutex` across `.await`.
- Edition / MSRV in `Cargo.toml` is a ceiling for syntax
  (`let-else`, `async fn` in traits).

## Do not

- Rewrite working safe code as `unsafe` for speed without
  measurement.
