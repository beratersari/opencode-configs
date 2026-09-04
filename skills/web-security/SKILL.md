---
name: web-security
description: Web and HTTP security review. Load when the diff touches HTTP handlers, HTML, URLs, cookies, CORS, file uploads, SSRF-prone fetch, or user-controlled paths. Do not load for non-network C++ or offline tools.
license: MIT
compatibility: opencode
---

# Web security

Review **this change** for injection and request-smuggling bugs.
Project rules still win.

## Look for

- XSS: user input in HTML/JS without encoding. `innerHTML`,
  template strings, or Markdown rendered as HTML.
- Open redirect / SSRF: server fetch or redirect to a
  caller-controlled URL.
- Path traversal: `../` in a file path from the request.
- CORS `*` with credentials, or reflecting `Origin`.
- Cookie without `HttpOnly` / `Secure` / `SameSite` on a
  session cookie this MR adds.
- Host header used as a URL or password-reset link.
- Upload that keeps the client filename or a dangerous MIME.

## Impact

`git grep` the handler name. A helper that “only concatenates
strings” is Critical if any HTTP path reaches it.

## Do not flag

- Static HTML with no user data.
- CSRF on a documented public, side-effect-free GET.
