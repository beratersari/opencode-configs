---
name: elixir
description: Elixir / OTP skill. Load when the diff changes *.ex, *.exs, mix.exs, or mix.lock.
license: MIT
compatibility: opencode
---

# Elixir

Project rules still win. Honor the Elixir / OTP versions in `mix.exs`.

## Look for

- Process that can crash without a supervisor this app
  already uses for that kind of work.
- Unbounded mailbox: `send` in a hot loop with no back-pressure.
- `String.to_atom` on user input (atom table exhaustion).
- `Enum` on a huge lazy stream that should stay lazy.
- Ecto: string-interpolated SQL; missing `Repo.transaction`
  when this change writes two rows that must commit together.
- Phoenix: missing CSRF on a state-changing route the
  pipeline already requires elsewhere.

## Do not flag

- `|>` style nits.
- Suggesting LiveView in a JSON-only API.
