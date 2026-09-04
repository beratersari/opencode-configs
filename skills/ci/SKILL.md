---
name: ci
description: CI and pipeline review. Load when the diff changes .gitlab-ci.yml, .github/workflows, Jenkinsfile, Azure Pipelines, or similar. Do not load when no pipeline file changed.
license: MIT
compatibility: opencode
---

# CI pipelines

Review **this change** for secret leaks and a pipeline that
will not run what the author thinks. Project rules still win.

## Look for

- Secret echoed, passed as a CLI arg (`curl -H "token: $TOKEN"`
  in a fork PR log), or written into an artifact.
- `pull_request_target` / untrusted checkout that runs
  contributor code with repo secrets.
- `on: pull_request` from forks with write tokens.
- A job that uses `latest` of an action/image with no pin
  when this MR introduces that action.
- A required check this MR removes or whose `if:` now skips
  on the default branch.
- Cache keys that can be poisoned from a fork.
- Windows vs Linux path assumptions that break the other
  runner this project already uses.

## Impact

A disabled test job is a process bug: the next MR will look
green. Say so as Major if this pipeline is the merge gate.

## Do not flag

- Pinning a hash vs a moving tag when the project already
  uses tags everywhere.
