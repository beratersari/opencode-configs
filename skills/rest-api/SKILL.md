---
name: rest-api
description: HTTP REST API skill. Load when designing or changing REST endpoints, status codes, pagination, or OpenAPI. Use for implement, debug, or review.
license: MIT
compatibility: opencode
---

# REST APIs

## Rules

- Mutating GET. Use POST/PATCH/DELETE for side effects.
- Wrong status: 200 on create (prefer 201 + Location),
  500 for a client validation error (use 4xx).
- Pagination missing on an unbounded list this change adds.
- Breaking JSON field rename without deprecation (see
  `api-compat`).
- Auth middleware skipped on a new route (see `auth`).
- Error body shape that does not match existing endpoints.
- Caching: `Cache-Control` on personalized data, or no
  `ETag`/`If-None-Match` when the API already uses them.

## Do not

- Demand GraphQL or gRPC as a rewrite.
