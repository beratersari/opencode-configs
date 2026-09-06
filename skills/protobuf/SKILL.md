---
name: protobuf
description: Protocol Buffers skill. Load when the diff changes *.proto, generated *pb.go / *.pb.cc / *_pb2.py, or buf.yaml.
license: MIT
compatibility: opencode
---

# Protocol Buffers

Project rules still win. Honor proto2 vs proto3 and the buf/lint config.

## Look for

- Reused field number or changed type on an existing number
  (wire break).
- Removed required proto2 field.
- `reserved` missing after a deleted number / name.
- Enum value reuse; new values should be appended.
- Java/Go package option missing when the project already
  sets it on sibling protos.
- Breaking JSON name change on a public API.

## Do not flag

- gRPC vs Connect as a rewrite (see `grpc`).
- Style of `snake_case` if the file already matches.
