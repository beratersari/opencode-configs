---
name: php
description: PHP skill. Load when the diff changes *.php, composer.json, or composer.lock. Use for Laravel/Symfony only when those files also change.
license: MIT
compatibility: opencode
---

# PHP

Project rules still win. Honor the `composer.json` PHP version.

## Look for

- SQL or shell built with string concat of request input.
- `unserialize` / `eval` / `extract` on untrusted data.
- Missing `declare(strict_types=1)` only if the file / package
  already uses it and this change omitted it.
- Type error: `?T` returned as bare `null` unchecked.
- CSRF / session fixation if this change adds a state-changing
  endpoint without the project's existing token check.
- `password_hash` / `password_verify` — do not invent a home
  brew hasher.

## Do not flag

- Short open tags in a codebase that already uses them.
- Suggesting attributes / enums below the declared PHP version.
