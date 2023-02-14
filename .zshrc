# If you come from bash you might have to change your $PATH.
PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/bin/site_perl:/usr/bin/vendor_perl:/usr/bin/core_perl:~/scripts


# Path to your oh-my-zsh installation.
export ZSH="$HOME/.oh-my-zsh"

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME="robbyrussell"

# Case-sensitive completion.
CASE_SENSITIVE="true"


# Uncomment one of the following lines to change the auto-update behavior
# zstyle ':omz:update' mode disabled  # disable automatic updates
# zstyle ':omz:update' mode auto      # update automatically without asking
# zstyle ':omz:update' mode reminder  # just remind me to update when it's time

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS="true"


# Uncomment the following line to display red dots whilst waiting for completion.
# You can also set it to another string to have that shown instead of the default red dots.
# e.g. COMPLETION_WAITING_DOTS="%F{yellow}waiting...%f"
# Caution: this setting can cause issues with multiline prompts in zsh < 5.7.1 (see #5765)
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"


# ------ Plugins ------

# Which plugins would you like to load?
# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/

plugins=(

git
archlinux
command-not-found
rust
zsh-autosuggestions

)


source $ZSH/oh-my-zsh.sh

# ------ User configuration ------

# Language environment
export LANG=en_US.UTF-8

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# --- Mis alias ---

# - Comandos -

alias off='shutdown now'
alias lsa='lsd -a'
alias ll='lsd -l'
alias blackcategories="pacman -Sg | grep blackarch | sed 's/blackarch-/ /'"
alias rmss='rm ~/Screenshots/*'

# - Shortcuts -

alias v='nvim'
alias p='python3'
alias cat='bat'
alias ls='lsd'

# - Git -

alias g='git'
alias ga='git add'
alias gs='git status'
alias gc='git clone'

# - Directorios Rapidos -

## -- go --

alias godsk='cd ~/Desktop'
alias goh='cd ~'
alias godw='cd ~/Downloads'
alias gosc='cd ~/scripts'

## -- pr --
alias prbash='cd ~/workspace/bash'
alias prrust='cd ~/workspace/rust'
alias prpython='cd ~/workspace/python'

# - Configs -

alias cfgqtile='code ~/.config/qtile'
alias cfgbash='nvim ~/.bashrc'
alias cfgzsh='nvim ~/.zshrc'
alias cfgalacritty='nvim ~/.config/alacritty/alacritty.yml'


neofetch
. "$HOME/.cargo/env"

source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh


