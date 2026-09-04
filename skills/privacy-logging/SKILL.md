---
name: privacy-logging
description: Logging and privacy review. Load when the diff adds or changes logs, metrics, traces, analytics, or error reports. Do not load when no logging or telemetry changed.
license: MIT
compatibility: opencode
---

# Logging and privacy

Review **this change** for data that must not be logged.
Project rules still win.

## Look for

- Tokens, passwords, cookies, `Authorization`, or full
  request bodies in a log line this MR added.
- PII (email, phone, national id, exact IP+user) at info
  level without a documented need.
- Exception objects stringified with query strings or
  form data still attached.
- Debug logs left on in a default production path.
- A new telemetry event with a user identifier and no
  retention / opt-out the project already has.

## Impact

A helper `log_request(req)` used by many handlers leaks
every header. `git grep` the helper.

## Do not flag

- Job ids / request ids this project already treats as
  public.
- Error messages that only contain a safe enum / status.
