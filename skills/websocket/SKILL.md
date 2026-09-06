---
name: websocket
description: WebSocket skill. Load when the diff changes websocket / ws / socket.io / channels consumers or Upgrade handlers.
license: MIT
compatibility: opencode
---

# WebSocket

Project rules still win.

## Look for

- Missing origin / auth check on the upgrade this change
  added (CSWSH).
- Unbounded message size / queue (memory DoS).
- Fan-out without back-pressure; one slow client stalls
  or grows a buffer forever.
- Trusting client frames as if they were server-internal
  RPCs (authorize each message).
- Ping/pong / idle timeout missing when sibling sockets
  already have it.
- Thread / event-loop block inside the receive handler.

## Do not flag

- Socket.IO vs raw WS as a rewrite.
