---
name: networking
description: Networking and TLS skill. Load when changing sockets, HTTP clients, TLS, DNS, timeouts, or bind addresses. Use for implement, debug, or review.
license: MIT
compatibility: opencode
---

# Networking

## Rules

- Timeouts on every outbound call (connect + read).
- TLS: do not set `InsecureSkipVerify` / `verify=False` on
  a production path. Pin or use the system store.
- Bind `0.0.0.0` on an admin port without auth.
- IPv6: dual-stack assumptions that break one family.
- Retry without jitter on a non-idempotent method.
- DNS cache forever or never (stale vs thundering herd).
- HTTP/2 or gRPC without a max header / message size.

## Do not

- Demand HTTP/3.
