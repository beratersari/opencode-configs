---
name: messaging
description: Queue and pub/sub skill. Load when changing Kafka, Rabbit, NATS, SQS, pub/sub, or outbox patterns. Use for implement, debug, or review.
license: MIT
compatibility: opencode
---

# Messaging

## Rules

- Handler that is not idempotent on at-least-once
  delivery (the default for most brokers).
- No dead-letter / retry bound on a new consumer.
- Poison message that can block the partition forever.
- Publishing inside a DB transaction without an outbox
  (dual-write).
- Schema change of a payload without a compat plan
  (`api-compat`).
- Missing key on a Kafka-like log when order per
  entity matters.

## Do not

- Demand exactly-once when the broker cannot provide
  it.
