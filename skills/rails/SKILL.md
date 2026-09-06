---
name: rails
description: Ruby on Rails skill. Load when the diff changes config/routes.rb, app/models, app/controllers, or db/migrate.
license: MIT
compatibility: opencode
---

# Rails

Project rules still win. Honor the Rails major.

## Look for

- Mass assignment: `params` into `update` without
  `permit` / a form object this app uses.
- SQL interpolate in `where` / `find_by_sql`.
- N+1 this change added (`each` + query); use the
  association load the project already prefers.
- Callback that hides a validation failure.
- CSRF skip on a cookie-session action.
- Migration that is not reversible when the project
  requires `down` / `change`.
- `default_scope` that this change relies on for security.

## Do not flag

- Hotwire vs React as a rewrite.
- Strong params style if the app uses dry-validation.
