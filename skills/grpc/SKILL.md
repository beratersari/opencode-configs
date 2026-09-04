---
name: grpc
description: gRPC / protobuf skill. Load when working with *.proto, grpc stubs, or protobuf codegen. Use for implement, debug, or review.
license: MIT
compatibility: opencode
---

# gRPC / protobuf

## Rules

- Never reuse a field number. Never change a field’s type
  in place. Reserve deleted numbers.
- `required` in proto2 is a landmine. Prefer proto3
  optional / presence.
- Breaking: renumber, change cardinality, rename a package
  clients import.
- Deadlines: every client call needs a timeout/context.
- Streaming: backpressure and cancel; do not buffer
  unbounded.
- Error: use status codes, not a 200 + string.

## Do not

- Suggest JSON mapping nits that do not affect this change.
