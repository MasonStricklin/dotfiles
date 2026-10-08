# dotfiles

## Files

- `.gitignore` — ignores `.DS_Store`
- `.hushlogin` — quiet terminal startup; symlinked into `~`
- `.vimrc` — Vim setup; symlinked into `~`
- `.zshrc` — shell setup; symlinked into `~`
- `AGENTS.md` — for Claude CLI and Codex; symlinked to `~/.claude/CLAUDE.md` and `~/.codex/AGENTS.md`
- `base-mac-settings.md` — setting up a new Mac
- `blockers.md` — workflow blockers to resolve
- `config.ghostty` — Ghostty setup; symlinked to `~/.config/ghostty/config`
- `default-apps.duti` — default apps for code files; run `duti default-apps.duti`
- `kiln.html` — source of truth for colors and fonts
- `skills/` — global skills, one directory each; symlinked into `~/.claude/skills/` and `~/.codex/skills/`
- `zed-settings.json` — Zed setup; symlinked to `~/.config/zed/settings.json`

## Agents: Claude CLI and Codex

Why: Claude CLI (terminal and Zed) and Codex share one instruction file and one skill set, synced across machines through this repo. Prefer tool-neutral files; add a tool-specific one only when no neutral option exists.

- Instructions: `AGENTS.md`; both tools read it through links
- Global skills: `skills/<name>/`; linked into each tool's skills directory
- Project skills: the project's top-level `skills/`; no `.agents/`, no `.claude/`, no links, no copies
- Private layer: a separate private repo (`qdotfiles`) may add employer-specific instructions, shell config and skills; `AGENTS.md` points to it and this repo never depends on it
- Built-in skills: leave in place (`~/.claude/skills/synced/`, `~/.codex/skills/.system/`)
- Skill format: `SKILL.md` plus its files; no tool-specific metadata (`agents/openai.yaml`)

## Change something

1. Make the change in this repo; don't create skills or instructions directly in `~/.claude` or `~/.codex`.
2. Commit and push.
3. Sync every other machine.

## Sync a machine

1. Pull `main`.
2. Link every file under Files to its target; create missing links, repoint wrong ones.
3. Link every `skills/<name>/` into each installed agent's skills directory.
4. Find this machine's actual paths; don't assume they match the ones above.
5. Report each link added or fixed.
