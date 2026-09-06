---
name: powershell
description: PowerShell skill. Load when the diff changes *.ps1, *.psm1, *.psd1, or Windows .bat that calls powershell.
license: MIT
compatibility: opencode
---

# PowerShell

Project rules still win. Scripts used from cmd.exe must stay
ASCII-safe (no smart quotes, no em dash).

## Look for

- Automatic variables used as locals (`$PID`, `$args`, `$host`,
  `$error`, `$profile`).
- `Invoke-Expression` / `iex` on unsanitized input.
- Unescaped `"` inside single-quoted regexes that cmd will
  parse (PS 5.1).
- `echo ... > file` inside a `.bat` (cmd redirect). Prefer
  `^>` or no `>`.
- `Set-ExecutionPolicy` changes as part of an app script.
- Missing `$ErrorActionPreference = 'Stop'` on an installer
  that must fail closed.

## Do not flag

- Verb-Noun naming on a 20-line helper.
- Requiring PowerShell 7 when the file is for Windows PS 5.1.
