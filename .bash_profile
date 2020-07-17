# PS1 generated using this website: http://bashrcgenerator.com/
export PS1="\[\033[38;5;129m\][\[$(tput sgr0)\]\[\033[38;5;34m\]\t\[$(tput sgr0)\]\[\033[38;5;129m\]]\[$(tput sgr0)\]\[\033[38;5;36m\]\u\[$(tput sgr0)\]\[\033[38;5;129m\]:\[$(tput sgr0)\]\[\033[38;5;38m\]\w\[$(tput sgr0)\]\[\033[38;5;129m\]\\$\[$(tput sgr0)\]"

# Add homebrew python to PATH
export PATH=/usr/local/opt/python@3.8/libexec/bin:${PATH}

# Quickly access dot files
alias bashrc="cd ~ && vim .bash_profile"
alias vimrc="cd ~ && vim .vimrc"

# Navigate to the rood directory quickly
alias ~="cd ~"

# Always include hidden files
alias ls="ls -a"

# Recursively remove directories and prompt before removal
alias rm="rm -ir"

# Recursively remove directories and without prompting before removal
alias rmr="rm -fr"

