# PS1 generated using this website: https://zsh-prompt-generator.site/ 
export PS1="%B%F{141}%~%f%b "

# Add homebrew python to PATH
export PATH=/usr/local/opt/python@3.8/libexec/bin:${PATH}

# Quickly access dot files
alias zshrc="cd ~ && vim .zshrc"
alias vimrc="cd ~ && vim .vimrc"

# Quickly navigate to home, root, and workspace directories
alias home="cd ~"
alias root="cd /"
alias code="cd ~/Documents/Code"

# Always include hidden files
alias ls="ls -a"

# Recursively remove directories and prompt before removal
alias rm="rm -ir"

# Recursively remove directories without prompting before removal
alias rmf="rm -fr"

# Alias for common ngrok command
alias nk="ngrok http -host-header=rewrite"

