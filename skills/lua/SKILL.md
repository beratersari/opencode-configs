---
name: lua
description: Lua / LuaJIT skill. Load when the diff changes *.lua, *.luac, or rockspec files.
license: MIT
compatibility: opencode
---

# Lua

Project rules still win. Honor Lua 5.1 vs 5.3 vs LuaJIT.

## Look for

- `pairs` vs `ipairs` on a sequence with holes.
- Global leak: missing `local` on a new name.
- `setmetatable` `__index` cycles.
- Mixing 1-based sequences with 0-based C indices at the
  binding this change added.
- `load` / `loadstring` on untrusted text.
- Coroutine that yields across a C boundary the host forbids.

## Do not flag

- Suggesting 5.3 bitwise ops on a 5.1 / LuaJIT host.
