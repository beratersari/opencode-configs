---
name: nodejs
description: Node.js runtime skill. Load when the diff changes server JS/TS that imports node:*, express, fastify, koa, or package.json engines.node.
license: MIT
compatibility: opencode
---

# Node.js

Project rules still win. Honor `engines.node`.

## Look for

- Unhandled `rejection` / missing `try` around `await` this
  change added on a request path.
- `fs` without path-normalize; `..` into a data dir.
- `child_process` `shell: true` with non-constant input.
- Mixing callbacks and promises on the same stream.
- Sync `readFileSync` / `execSync` on a request handler.
- Express: missing `next(err)` or a middleware that never
  calls `next` / `res.end`.
- Trusting `X-Forwarded-*` without the proxy setting.

## Do not flag

- ESM vs CJS if the package already mixes them.
- Suggesting Node 22 APIs when `engines` is 18.
