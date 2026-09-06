---
name: postgresql
description: PostgreSQL skill. Load when the diff changes *.sql, *postgres*, Flyway/Liquibase PG scripts, or SQLAlchemy/Django models targeting Postgres.
license: MIT
compatibility: opencode
---

# PostgreSQL

Project rules still win. Honor the server major the project runs.

## Look for

- Query without a bind (`%s` / `$1`) for user input.
- Missing index only when this change adds a filter /
  join that will seq-scan a large table the schema shows.
- Transaction that is not wrapping two writes that must
  commit together.
- `NOT NULL` add without a backfill on a live table.
- `varchar` vs `text` nits — skip unless a check constraint
  or index prefix depends on it.
- `LISTEN/NOTIFY` or advisory locks used incorrectly
  (session vs transaction lock).
- RLS policy this change bypasses with a table owner role.

## Do not flag

- MySQL-isms in a file that is not run on Postgres.
- Suggesting PG 16 syntax on an older pin.
