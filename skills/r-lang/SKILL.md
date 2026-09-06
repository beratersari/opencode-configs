---
name: r-lang
description: R language skill. Load when the diff changes *.R, *.r, *.Rmd, DESCRIPTION, or renv.lock.
license: MIT
compatibility: opencode
---

# R

Project rules still win.

## Look for

- `attach()` / `T`/`F` instead of `TRUE`/`FALSE`.
- `sapply` simplifying away a type this caller needs as a list.
- Factor vs character after a CSV read (`stringsAsFactors`).
- Super-assignment `<<-` mutating a parent frame this
  function did not own.
- `eval(parse(text=))` on user input.
- Package version not declared in `DESCRIPTION` / `renv`.

## Do not flag

- Tidyverse vs base as a rewrite.
