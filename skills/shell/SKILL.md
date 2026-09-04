---
name: shell
description: Shell and Windows-script review. Load when the diff changes *.sh, *.bash, *.zsh, *.bat, *.cmd, or *.ps1. Do not load when no shell script changed.
license: MIT
compatibility: opencode
---

# Shell scripts

Review **this change** for injection and portability. Project
rules still win.

## Look for

- Unquoted expansions (`$var` / `$@` vs `"$@"`) that split
  or glob user input.
- `eval` or `bash -c` with concatenated user data.
- `curl | sh` or downloading a script and running it.
- `rm -rf $dir` without a quote or a rooted prefix check.
- `set -e` with a pipe (need `pipefail`) when the script
  already claims to fail on error.
- Windows `.bat`: unescaped `>` / `&` / `%VAR%` that breaks
  or runs extra commands. `echo` of `->` as a redirect.
- PowerShell: `Invoke-Expression` on untrusted text.
- Hardcoded secrets (also load `secrets` if they appear).

## Impact

A helper script called from CI or install is in scope even if
this MR only changed the helper. `git grep` the script name.

## Do not flag

- Missing `set -e` on a 5-line sourced snippet that already
  checks every command.
