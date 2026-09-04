---
name: docker
description: Container review. Load when the diff changes Dockerfile, docker-compose*.yml, Containerfile, or Kubernetes manifests that define images. Do not load when no container file changed.
license: MIT
compatibility: opencode
---

# Docker / containers

Review **this change** for a image that is unsafe or will not
build. Project rules still win.

## Look for

- Running as root in the final stage with no reason.
- Secrets in `ENV` / `ARG` that remain in an image layer
  (`docker history`).
- `ADD` of a remote URL, or `COPY` of `.git` / `.env`.
- `latest` base image this MR introduces, when the project
  pins tags elsewhere.
- Extra exposed ports, or `network_mode: host` in compose
  without a comment.
- A compose bind-mount of the docker socket.
- Missing `USER` after a root-only install step.
- Healthcheck / CMD that will not find the binary this MR
  just renamed.

## Impact

A Dockerfile used by CI and by local `compose` has two
callers. `git grep` the image name.

## Do not flag

- Distroless vs debian as taste.
- Multi-stage that is already correct.
