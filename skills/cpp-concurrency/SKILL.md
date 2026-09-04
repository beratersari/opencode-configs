---
name: cpp-concurrency
description: C++ concurrency review. Load when the diff uses threads, mutexes, atomics, condition variables, pthreads, Win32 threads, Boost.Thread, or shared mutable state across tasks. Do not load for single-threaded code. Never suggest std::thread/mutex/atomic on C++98. Dialect skill already loaded this turn is a hard ceiling.
license: MIT
compatibility: opencode
---

# C++ concurrency

Review **this change** for races, deadlocks, and lifetime across
threads. Project rules and the loaded dialect skill still win.

C++98: pthreads, Win32, or Boost.Thread only. Do not invent
`std::thread`. C++11+: `lock_guard` / `unique_lock`. C++17:
`scoped_lock`. C++20: `jthread` only if that standard is confirmed.

## Look for

- Data race: shared mutable object (including `std::string` /
  containers) written without a happens-before edge.
- Bare `lock`/`unlock`. RAII lock only.
- Two mutexes locked in opposite order. Need `std::lock` +
  `adopt_lock`, or C++17 `scoped_lock`.
- Virtual / callback / foreign code called while holding a lock.
- `std::thread` not joined and not transferred. Flag `detach()`.
- Thread or `std::async` that captures stack locals by reference.
- Condition variable without a predicate loop (spurious wake).
- `std::atomic` on one field used as if the whole struct is safe.
  Relaxed atomics need a proven acquire/release pair.
- `shared_ptr` control block is atomic; the **object** is not.
- Double-checked locking without a proven barrier / C++11 atomic.
- Static initialization order across TUs before `main`.

## Impact

A new shared field is a race even if the lock in **this** function
looks right. `git grep` every writer and reader of that field.

## Do not flag

- Message-passing of uniquely owned data with no shared mutable.
- Suggesting TSan setup the project does not already run.
