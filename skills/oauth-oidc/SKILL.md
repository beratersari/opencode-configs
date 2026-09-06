---
name: oauth-oidc
description: OAuth 2 / OIDC skill. Load when the diff changes OAuth/OIDC client or issuer code, JWKS, or callback routes.
license: MIT
compatibility: opencode
---

# OAuth 2 / OIDC

Project rules still win. Use `auth` for general session/password.

## Look for

- Authorization code flow missing `state` (CSRF) or
  PKCE on a public client.
- Token in a query string or log.
- Redirect URI that is a prefix match (`https://evil.com`
  vs `https://evil.com.example`).
- `id_token` accepted without issuer / audience / expiry
  / signature check the library already offers.
- Implicit flow added for a new confidential client.
- Refresh token stored in localStorage when the app
  otherwise uses httpOnly cookies.

## Do not flag

- Inventing a new IdP.
- Suggesting Device flow for a first-party web app.
