---
name: auth
description: Authentication and authorization review. Load when the diff changes login, sessions, JWT, OAuth, API tokens, RBAC, permissions, or “who can call this.” Do not load when no identity or access control changed.
license: MIT
compatibility: opencode
---

# Auth

Review **this change** for broken authentication or authorization.
Project rules still win.

## Look for

- Missing authn on a new mutating route or RPC.
- Authz that checks “is logged in” but not “may touch this
  resource” (IDOR: object id from the client).
- Token in a query string, log, or non-HttpOnly cookie.
- JWT with `alg: none`, a hardcoded secret, or no expiry.
- Privilege flag taken from the client body.
- Password compare not constant-time when this MR introduces
  the compare.
- Session fixation: new session not issued after login.

## Impact

A new endpoint that skips the existing auth middleware is
Critical even if the handler body is correct. `git grep` how
sibling routes attach auth.

## Do not flag

- Public health/webhook routes that already verify a secret
  in this project’s documented way.
