# OpenCode configs

Shared OpenCode agents and skills. Creasy, and any other project that
runs the same review agents, consume this tree as a git submodule.

Layout matches what the installer copies into the user OpenCode home:

```
agents/           # -> ~/.config/opencode/agents/<name>.md
  review.md
skills/           # -> ~/.config/opencode/skills/<name>/SKILL.md
  cpp98/
  modern-cpp/
```

Add a new agent by dropping `agents/<name>.md`. Add a skill as
`skills/<name>/SKILL.md`. Installers copy every file they find.

## Replace install (this repo)

`install.py` deletes **only** `~/.opencode` and `~/.config/opencode`.
If another OpenCode exists (another folder on PATH, or
`OPENCODE_HOME` / `OPENCODE_INSTALL` / `OPENCODE_BIN`), those files
stay. That directory is removed from the user PATH so `opencode` does
not resolve there. Put the old path back if you still want that copy.
System dirs such as `/usr/local/bin` are not stripped.

```bash
python install.py --root .
# or, after unpacking a CI zip:
install.bat
./install.sh
```

Windows: user PATH in `HKCU\Environment`. Linux: `PATH` plus a marked
block in `~/.profile`. Creasy's own installer does **not** do this; it
only adds files.

## CI artifacts

Push to `main` uploads `opencode-configs-windows.zip` and
`opencode-configs-linux.zip`. Each zip has `agents/`, `skills/`, and
the install scripts.

## Use in another repo

```bash
git submodule add https://github.com/beratersari/opencode-configs.git opencode-configs
git submodule update --init --recursive
```
