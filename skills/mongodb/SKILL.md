---
name: mongodb
description: MongoDB skill. Load when the diff changes files that import mongodb / mongoose / motor, or *.mongo.js.
license: MIT
compatibility: opencode
---

# MongoDB

Project rules still win.

## Look for

- Operator injection: passing request JSON as a query
  (`$gt`, `$where`) without allow-listing keys.
- Missing filter on `updateMany` / `deleteMany`.
- Write that needed a transaction (multi-doc) and did
  not use one, when the deployment is a replica set.
- Unbounded `find()` without `limit` on an API path.
- Schema field this change reads that older documents
  may not have (no default / migration).
- Index hinted by a new unique constraint that can fail
  on existing dupes.

## Do not flag

- SQL vs Mongo as a rewrite.
- Suggesting Atlas-only APIs on a self-hosted pin.
