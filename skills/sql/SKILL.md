---
name: sql
description: SQL and migration review. Load when the diff changes queries, ORMs, schema, migrations, or raw SQL strings. Do not load when no database code changed.
license: MIT
compatibility: opencode
---

# SQL

Review **this change** for injection, data loss, and query bugs.
Project rules still win.

## Look for

- String-built SQL with user input. Need bind parameters.
- Migration that is not reversible when the project’s rules
  require down migrations, or that drops a column with no
  backfill story.
- `DELETE` / `UPDATE` without a WHERE, or a WHERE that is
  always true from a missing bind.
- Unique / foreign-key constraint removed without a reason.
- N+1: a loop that runs one query per row on an unbounded
  list this MR introduced.
- Transaction that does not cover the full write set (partial
  commit on error).
- SELECT `*` on a wide table used as an API payload (leaks
  columns).

## Impact

A query helper used by unchanged callers is in scope. `git grep`
the function that builds the SQL.

## Do not flag

- Parameterized queries that are correct.
- “Add an index” as a style nit unless this MR adds a
  filter that will table-scan unbounded data.
