# PS1 generated using this website: https://zsh-prompt-generator.site/ 
export PS1="%F{128}[%f%F{71}%*%f%F{128}]%f%F{79}%n%f%F{128}:%f%F{87}%~%f%F{128}$%f"

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
