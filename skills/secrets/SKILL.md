---
name: secrets
description: Secret-leak review. Load when the diff adds config, env samples, tokens, keys, passwords, PEM/PFX, .netrc, or long high-entropy strings. Do not load for ordinary source with no credential-shaped data.
license: MIT
compatibility: opencode
---

# Secrets

Review **this change** for credentials that must not land in git.

## Look for

- API tokens, `PRIVATE-TOKEN`, `Authorization: Bearer`, AWS
  keys, private keys (`BEGIN … PRIVATE KEY`), keystore passwords.
- Connection strings with a password in the URI.
- `.env` with real values (not placeholders).
- High-entropy strings assigned to `token`, `secret`, `password`,
  `api_key` that are not clearly test fixtures.

## Do not flag

- `YOUR_TOKEN_HERE` / empty assignments in `.env.example`.
- Public test fixtures the project already documents as fake.
