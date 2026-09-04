---
name: cryptography
description: Cryptography skill. Load when changing hashes, MACs, AEAD, TLS, key storage, or password hashing. Use for implement, debug, or review.
license: MIT
compatibility: opencode
---

# Cryptography

## Rules

- Homemade crypto or “XOR with a key”.
- ECB mode, static IV, or MD5/SHA1 for passwords.
- Passwords: use the project’s existing Argon2 / bcrypt
  / scrypt; do not invent a fast hash.
- Keys in source or logs (`secrets`).
- Compare secrets with `==` (timing). Use a constant-
  time compare the language provides.
- Nonce reuse on GCM / ChaCha20-Poly1305.
- Rolling your own JWT / cookie MAC when a library is
  already in the tree.

## Do not

- Suggest a new primitive the platform does not have.
- “Use SHA256” for password storage.
