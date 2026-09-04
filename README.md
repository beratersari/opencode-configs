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
`skills/<name>/SKILL.md`. The Creasy installer copies every file it
finds; it does not hard-code the review agent.

## Use in another repo

```bash
git submodule add https://github.com/beratersari/opencode-configs.git opencode-configs
git submodule update --init --recursive
```

Then copy or install `agents/` and `skills/` into the OpenCode home
your process uses (`~/.config/opencode` and, if that home exists,
`~/.opencode`).
