---
name: api-compat
description: Published API / wire-compat review. Load when the diff changes a public HTTP/RPC schema, protobuf/OpenAPI, exported library header, or CLI flags. Combined from PR-agent / impact-analyzer “coordinated updates” and oh-my-opencode git-master “what did history already promise.” Do not load for private helpers.
license: MIT
compatibility: opencode
---

# API compatibility

Review **this change** for a break callers will compile or
run against. Combined from impact-analyzer style (PR-agent /
llimllib) and oh-my-opencode’s “history already promised
this”.

## Look for

- Removed or renamed field / flag / header without a
  deprecation window the project already uses.
- Type change (string → int, optional → required) on a
  published JSON/protobuf field.
- Default argument or default JSON key changed (silent
  behavior change for old clients).
- Status code / error shape change that existing clients
  switch on.
- Semver: a breaking change in a library this repo
  versions, with no major bump (only if VERSION / tags
  exist).
- OpenAPI / proto file not updated together with the
  handler (or the reverse).

## Impact

`git grep` the route, message name, and old field. Unchanged
clients in this repo are in scope.

## Do not flag

- Additive optional fields.
- Internal DTOs used in one service.
