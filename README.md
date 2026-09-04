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

`install.py` finds the previous OpenCode install even when it is not
under `~/.opencode`. It looks at the user PATH, `opencode` / `opencode.exe`
on that PATH, and `OPENCODE_HOME` / `OPENCODE_INSTALL` / `OPENCODE_BIN`.
A dedicated tree (`…/opencode/bin` or `…/.opencode/bin`) is deleted and
that directory is removed from PATH. A shared tools directory (for
example `/usr/local/bin` next to `git`) only loses the `opencode`
binary; the PATH entry stays. Default homes `~/.opencode` and
`~/.config/opencode` are always removed, then this pack is written
fresh. Deleting a folder without touching PATH is not enough.

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
