---
name: nextjs
description: Next.js skill. Load when the diff changes next.config.*, app/, pages/, or files that import next/*.
license: MIT
compatibility: opencode
---

# Next.js

Project rules still win. Honor App Router vs Pages from the tree.

## Look for

- Secret (`process.env` without `NEXT_PUBLIC_`) imported into
  a Client Component.
- `fetch` cache / revalidate that serves user-specific data
  as static.
- Server Action that mutates without the project's auth check.
- `redirect` / `cookies` used in a Client Component.
- Image / rewrite that open-redirects (`//evil`).
- Middleware matcher that skips an auth path this change added.

## Do not flag

- Rewriting Pages Router to App Router unprompted.
- Suggesting the latest Next major if package.json is pinned.
