---
name: redis
description: Redis skill. Load when the diff changes files that import redis / ioredis / stackexchange.redis, or redis.conf.
license: MIT
compatibility: opencode
---

# Redis

Project rules still win.

## Look for

- Key without the project's namespace prefix (collision).
- Unbounded `KEYS *` in production code (`SCAN` if they
  must iterate).
- Cache stampede: this change adds a hot key with no TTL
  or no single-flight the codebase already has.
- `MULTI/EXEC` vs `WATCH` lost-update on a counter this
  change added.
- Storing a secret or session in Redis without the
  existing encryption / httpOnly cookie split.
- Blocking `BLPOP` on the only connection used for
  regular commands.

## Do not flag

- Redis vs Memcached as a rewrite.
- Suggesting Redis Stack modules the deploy does not have.
