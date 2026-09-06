---
name: ruby
description: Ruby skill. Load when the diff changes *.rb, Gemfile, Gemfile.lock, or *.rake. Use for Rails when app/ or config/ also changes.
license: MIT
compatibility: opencode
---

# Ruby

Project rules still win. Honor the project's Ruby version.

## Look for

- SQL via string interpolate (`where("x = #{id}")`) — use
  binds the project already uses.
- `rescue Exception` / bare `rescue` that swallows.
- `params` into `update` / `assign_attributes` without a
  strong-params / permit list this app uses.
- Symbol vs string hash key mismatch after a JSON parse.
- Class-var `@@` mutable state in a threaded server.
- `YAML.load` on untrusted input (`safe_load`).

## Do not flag

- `do/end` vs brace style.
- Suggesting endless methods if the Ruby version is older.
