---
name: dependencies
description: Dependency and lockfile review. Load when the diff changes package.json, package-lock.json, requirements*.txt, Pipfile, pyproject.toml, go.mod, Cargo.toml, vcpkg.json, conanfile, or similar. Do not load when no dependency file changed.
license: MIT
compatibility: opencode
---

# Dependencies

Review **this change** for new or loosened dependencies.
Project rules still win.

## Look for

- A new package that is unused, or used only in a way the
  stdlib already covers.
- Version range that allows a major bump (`*` / `latest`).
- Lockfile not updated together with the manifest (or
  updated without the manifest).
- Postinstall / install scripts on a new npm package.
- A git/HTTP dependency with no pin (commit or tag).
- License that conflicts with this repo’s stated license
  (only if LICENSE / README already states one).
- Duplicate of a library the tree already vendors.

## Impact

A new runtime dependency is on every install path. Say what
pulls it in.

## Do not flag

- Routine patch bumps with a lockfile update and no new
  package.
- `package-lock.json` churn that matches `package.json`.
