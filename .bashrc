#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return


# --- Mis alias ---

# - Comandos -

alias off='shutdown now'
alias ls='lsd'
alias lsa='lsd -a'
alias ll='lsd -l'
alias cat='bat'
alias blackcategories="pacman -Sg | grep blackarch | sed 's/blackarch-/ /'"
alias p='python3'
alias rmss='rm ~/Screenshots/*'

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



PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/bin/site_perl:/usr/bin/vendor_perl:/usr/bin/core_perl:~/scripts

neofetch
. "$HOME/.cargo/env"
