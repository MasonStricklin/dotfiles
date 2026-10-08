# ~/.hushlogin hides macOS's Last login banner; children inherit the shown marker.
# Example: ✦ sat oct 3 · 3:30 pm; once per shell session
if [[ -o interactive && -z ${ZSH_GREETING_SHOWN:-} ]]; then
    zmodload zsh/datetime
    strftime -s greeting_time '%a %b %-d · %-I:%M %p' "$EPOCHSECONDS"
    print -P -- "%F{209}✦%f %F{245}${(L)greeting_time}%f"
    export ZSH_GREETING_SHOWN=1
    unset greeting_time
fi

# Prompt — bold clay orange; %~ shortens home to ~.
# %B/%b toggle bold; %F{209}/%f set/reset color.
# Example: ~ or ~/Documents/Code
PS1="%B%F{209}%~%f%b "

# Local executables — includes Claude Code.
export PATH="$HOME/.local/bin:$PATH"

# History — save commands immediately to ~/.zsh_history
HISTFILE="$HOME/.zsh_history"
HISTSIZE=50000   # Commands kept in memory; extra room for duplicate expiry.
SAVEHIST=40000   # Commands retained on disk between sessions.
# Save as entered; discard duplicates first when full; skip consecutive repeats.
setopt INC_APPEND_HISTORY HIST_EXPIRE_DUPS_FIRST HIST_IGNORE_DUPS

# Completion — Tab completes commands, paths, and arguments.
# Example: git switch <Tab> lists branches.
autoload -Uz compinit
compinit

# Shortcuts — config and navigation
alias zshrc="cd ~ && vim .zshrc"
alias vimrc="cd ~ && vim .vimrc"

alias home="cd ~"
alias root="cd /"
alias code="cd ~/Documents/Code"
alias cg="cd ~/Documents/ChatGPT"

# Files — ls includes dotfiles; rmi recursively deletes with confirmation
# Ordinary rm keeps its standard behavior.
alias ls="ls -a"
alias rmi="rm -ir"

# fzf — Ctrl-R history, Ctrl-T files, Alt-C directories
if command -v fzf >/dev/null 2>&1; then
    source <(fzf --zsh)
fi

# Suggestions — ghosted history matches; Right Arrow accepts
# Look in Apple Silicon, then Intel Homebrew; load the first installed copy.
for suggestions_file in \
    /opt/homebrew/share/zsh-autosuggestions/zsh-autosuggestions.zsh \
    /usr/local/share/zsh-autosuggestions/zsh-autosuggestions.zsh; do
    if [[ -r "$suggestions_file" ]]; then
        source "$suggestions_file"
        break
    fi
done
unset suggestions_file

# Highlighting — commands and quoted strings get distinct colors.
# Load last so it sees the other plugins' editing widgets; either Homebrew prefix.
# Example: git is green; gti is red.
for highlighting_file in \
    /opt/homebrew/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh \
    /usr/local/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh; do
    if [[ -r "$highlighting_file" ]]; then
        source "$highlighting_file"
        break
    fi
done
unset highlighting_file

# Claude Code: give each new session the next free prompt-bar color (ROYGBIV order)
claude() {
  local dir=~/.claude/session-colors
  # /color has no indigo; purple stands in for violet. pink/cyan are overflow.
  local pool=(red orange yellow green blue purple pink cyan)
  local color f pid used=()

  mkdir -p "$dir"
  for f in "$dir"/*(N); do
    pid=${f:t}
    if kill -0 "$pid" 2>/dev/null; then
      used+=("$(<"$f")")
    else
      rm -f -- "$f"         # stale claim from a dead session
    fi
  done

  for color in "${pool[@]}"; do
    (( ${used[(Ie)$color]} )) || break
  done

  # Only auto-color when no positional prompt and not print/resume mode.
  local a
  for a in "$@"; do
    case "$a" in
      -p|--print|-r|--resume|-c|--continue) exec command claude "$@" ;;
      -*) ;;
      *) exec command claude "$@" ;;
    esac
  done

  print -r -- "$color" > "$dir/$$"
  exec command claude "/color $color" "$@"
}

# Machine-local additions, kept outside this repo
[[ -r "$HOME/.zshrc.local" ]] && source "$HOME/.zshrc.local"
