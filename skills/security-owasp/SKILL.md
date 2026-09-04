---
name: security-owasp
description: Broad application-security review (OWASP-style). Load when the diff handles untrusted input, crypto, files, subprocesses, deserialization, or new network endpoints. Combined from Anthropic claude-code-security-review / opencode-power-pack security-review. Prefer web-security or auth when the diff is only HTTP or only login. Do not load for pure refactors with no input surface.
license: MIT
compatibility: opencode
---

# Security (OWASP-style)

Combined from Anthropic `claude-code-security-review` as
packaged in waybarrios/opencode-power-pack. Project rules
still win. Use `web-security` / `auth` / `secrets` for those
narrower diffs.

## Look for

- Injection: SQL, OS, LDAP, template, header (CRLF).
- Insecure deserialization (`pickle`, `yaml.load`, Java
  serialization, `eval` / `unserialize`).
- Path traversal and zip-slip on extract/upload.
- Crypto: homemade, ECB, hardcoded IV/key, MD5/SHA1 for
  passwords.
- SSRF / XXE when this MR parses XML or fetches a URL.
- Subprocess with `shell=True` or unsanitized argv.
- New endpoint without the project’s usual auth middleware
  (also load `auth` if identity changed).
- Debug flag or verbose error that leaks stack / secrets
  on a production path.

## Impact

A helper that concatenates input is Critical if any
untrusted caller can reach it. `git grep` the helper.

## Do not flag

- Issues already covered by a more specific skill you
  loaded (`sql`, `auth`, `secrets`).
- Theoretical crypto nits on an unused sample.
