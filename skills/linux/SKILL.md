---
name: linux
description: Linux / POSIX admin skill. Load when the diff changes systemd units, *.service, shell installers for Linux, or /etc config templates.
license: MIT
compatibility: opencode
---

# Linux

Project rules still win.

## Look for

- World-writable script or `chmod 777`.
- `curl | sh` as the only install path without a pin /
  checksum the project already uses elsewhere.
- systemd unit missing `User=` / running as root when
  sibling units do not.
- Hardcoded `/tmp` race without `mktemp`.
- `set -e` missing on an installer that must fail closed.
- Listening on `0.0.0.0` for an admin port the docs say
  is loopback-only.

## Do not flag

- systemd vs sysv as a rewrite.
- Distro package name nits (apt vs dnf) unless the
  script claims a specific distro.
