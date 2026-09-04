---
name: python
description: Python review. Load when the diff changes *.py, pyproject.toml, requirements*.txt, or *.pyi. Do not load when no Python files changed.
license: MIT
compatibility: opencode
---

# Python

Review **this change** for Python correctness. Project rules
still win. Match the file’s existing style (2 vs 3, typing).

## Look for

- Mutable default argument (`def f(x=[])`).
- Bare `except:` / `except Exception` that swallows and
  continues in a bad state.
- `is` used for value equality (`==` for values, `is` for
  None/singletons).
- Not closing a file / socket; prefer a `with` the project
  already uses.
- Race on a file or dict shared across threads without a
  lock this codebase already has.
- `subprocess` with `shell=True` and a non-constant command.
- `pickle` / `yaml.load` (not `safe_load`) on untrusted data.
- f-string or `%` that builds SQL or a shell command.
- Annotation that lies (`Optional` returned as bare None
  unchecked at the call site this MR added).

## Impact

A changed function’s callers in other modules are in scope.
`git grep` the symbol.

## Do not flag

- Missing type hints on a file that has none.
- `print` in scripts that are not a library.
