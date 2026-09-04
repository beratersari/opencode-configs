# OpenCode configs

Shared OpenCode **agents** and a general **skill library**. Creasy
ships the `review` agent today; later agents (implement, plan,
commit) should load the same `skills/` tree. Installers copy every
`skills/*/SKILL.md`. Each skill says when to load.

```
agents/           # -> ~/.config/opencode/agents/<name>.md
  gitlab-reviewer.md  # read-only GitLab reviewer (allow-list of skills)
skills/           # -> ~/.config/opencode/skills/<name>/SKILL.md
```

## Skills

C++ is the largest language group. The rest is for any stack.

**C++ dialect:** `cpp98` `modern-cpp`

**C++ specialists:** `cpp-memory-safety` `cpp-concurrency`
`cpp-exceptions` `cpp-templates` `cpp-headers-odr` `cpp-stl`
`cpp-numerics` `cpp-preprocessor` `cmake-cpp` `cpp-testing`

**Other languages:** `python` `javascript` `go` `rust` `java`
`csharp` `shell`

**Security:** `secrets` `web-security` `auth` `security-owasp`
`cryptography`

**Data / API:** `sql` `rest-api` `graphql` `grpc` `api-compat`
`caching` `messaging`

**UI:** `frontend-ui` `accessibility` `i18n`

**Infra:** `ci` `docker` `kubernetes` `terraform` `dependencies`
`networking` `licensing`

**Quality:** `performance` `observability` `privacy-logging`
`error-handling` `documentation` `testing` `refactoring`
`root-cause` `verification`

**Implementer-only** (do not allow on `review`): `tdd` `debugging`
`git-commits` `planning`

Drawn from [oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode),
[obra/superpowers](https://github.com/obra/superpowers),
[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills),
[anthropics/claude-code-security-review](https://github.com/anthropics/claude-code-security-review),
[waybarrios/opencode-power-pack](https://github.com/waybarrios/opencode-power-pack).
Not copied wholesale (no browser/commit bots on the review agent).

Add a new agent by dropping `agents/<name>.md`. Add a skill as
`skills/<name>/SKILL.md`. Installers copy every file they find.

## Replace install (this repo)

`install.py` **renames** `~/.opencode` to
`~/.opencode_backup_YYYYMMDD_HHMMSS` (and `~/.config/opencode` to
`~/.config/opencode_backup_YYYYMMDD_HHMMSS`). It does not delete those
trees. If another OpenCode exists (another folder on PATH, or
`OPENCODE_HOME` / `OPENCODE_INSTALL` / `OPENCODE_BIN`), those files
stay where they are. That directory is removed from the user PATH so
`opencode` does not resolve there. Put the old path back if you still
want that copy. System dirs such as `/usr/local/bin` are not stripped.

```bash
python install.py --root .
# or, after unpacking the GitHub Actions artifact:
install.bat
./install.sh
```

Windows: user PATH in `HKCU\Environment`. Linux: `PATH` plus a marked
block in `~/.profile`. Creasy's own installer does **not** do this; it
only adds files.

## CI artifacts

Push to `main` uploads folders named
`opencode-configs-1.18.10-windows` and
`opencode-configs-1.18.10-linux` (`OPENCODE_VERSION` in
`packaging/versions.env`). GitHub wraps each folder as a zip; the
download is not a zip of a zip. Each artifact has `agents/`,
`skills/`, and the install scripts.

## Use in another repo

```bash
git submodule add https://github.com/beratersari/opencode-configs.git opencode-configs
git submodule update --init --recursive
```
