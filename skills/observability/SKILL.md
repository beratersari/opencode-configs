---
name: observability
description: Metrics, traces, and structured logging skill. Load when adding or changing logs, metrics, spans, or dashboards. Use for implement, debug, or review. Pair with privacy-logging for PII.
license: MIT
compatibility: opencode
---

# Observability

## Rules

- New request path with no log or span at the boundary.
- High-cardinality labels (user id, raw URL) on a metric.
- Trace without a parent/context on an outgoing call.
- Log level: debug in a default production logger.
- Metric name that collides or breaks the project’s
  existing prefix.
- Error swallowed with no counter / log (see
  `error-handling`).

Pair with `privacy-logging` when the line can hold PII.

## Do not

- Demand OpenTelemetry if the repo uses another stack.
