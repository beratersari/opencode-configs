---
name: caching
description: Caching skill. Load when adding or changing caches, TTLs, ETags, Redis, memcached, or HTTP cache headers. Use for implement, debug, or review.
license: MIT
compatibility: opencode
---

# Caching

## Rules

- Unbounded cache (no max entries / TTL) on a request
  path.
- Cache key that omits a dimension that changes the
  value (user, locale, auth, version).
- Stale-on-write: mutation that does not invalidate
  the key.
- Caching personalized or secret data in a shared
  public cache.
- Thundering herd: no single-flight / lock on miss.
- Negative cache that hides a recovered backend
  forever.

## Do not

- Demand Redis when an in-process map is enough and
  already used.
