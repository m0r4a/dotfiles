# If you come from bash you might have to change your $PATH.
PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/bin/site_perl:/usr/bin/vendor_perl:/usr/bin/core_perl:~/scripts:/snap/bin

# Path to your oh-my-zsh installation.
export ZSH="$HOME/.oh-my-zsh"

# This are the variables for the GTK darkmode 
export GTK_THEME=Adwaita:dark
export GTK2_RC_FILES=/usr/share/themes/Adwaita-dark/gtk-2.0/gtkrc
export QT_STYLE_OVERRIDE=Adwaita-Dark

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME="robbyrussell"

# Case-sensitive completion.
CASE_SENSITIVE="true"

DISABLE_UNTRACKED_FILES_DIRTY="true"

# ------ Plugins ------

# Which plugins would you like to load?
# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/

plugins=(
# Default
git
archlinux
rust

# Custom
command-not-found
zsh-autosuggestions
)


source $ZSH/oh-my-zsh.sh

# ------ User configuration ------

# Language environment
export LANG=en_US.UTF-8

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# --- My aliases ---

# - Commands -

alias off='shutdown now'
alias blackcategories="pacman -Sg | grep blackarch | sed 's/blackarch-/ /'"
#alias rmss='rm ~/Screenshots/*'


# - Scripts -
alias lsa='lsd -a'
alias ll='lsd -l'
alias cat='bat'
alias grep='rg'


# - Shortcuts -

alias v='nvim'
alias vim='nvim'
alias p='python3'
alias ls='lsd'

# - Electron apps 
alias discord='webcord --enable-features=UseOzonePlatform,WaylandWindowDecorations --ozone-platform-hint=auto & disown'

# - Rust -

#alias rsc='nvim src/main.rs'

## -- Cargo --

#alias cn='cargo new'
#alias cb='cargo build'
#alias cr='cargo run'

# - Git -

alias g='git'
alias ga='git add'
alias gs='git status'
alias gc='git clone'

# - Edit files -

unalias md
alias md='bash ~/scripts/apostrophe'

# - Quick directories -

## -- GitHub repos --
alias csp='cd ~/workspace/Courses/CS50/Programming_with_Python'

## -- go --

alias godsk='cd ~/Desktop'
alias goh='cd ~'
alias godw='cd ~/Downloads'
alias gosc='cd ~/scripts'
#alias sdev='cd ~/workspace/scriptDev'

## -- pr --
alias prbash='cd ~/workspace/bash'
alias prrust='cd ~/workspace/rust'
alias prpython='cd ~/workspace/python'

# - Configs -

alias cfgbash='nvim ~/.bashrc'
alias cfghypr='nvim ~/.config/hypr/hyprland.conf'
alias cfgzsh='nvim ~/.zshrc'
alias cfgstarship='nvim ~/.config/starship/starship.toml'

# Fastfetch 

####### Old script, I will keep the code in case I figure out to fix it ######
# shiny=$((RANDOM % 500 + 1))

# if [ "$shiny" -eq 265 ]; then
#    pokemon=$(randomFilePicker ~/.config/fastfetch/PokeList/shiny)
# else
#    pokemon=$(randomFilePicker ~/.config/fastfetch/PokeList)
# fi


fastfetch --kitty ~/.config/fastfetch/darkrai.png --logo-padding-right 2 --logo-padding-left 3

# Cargo, rust's compiler

. "$HOME/.cargo/env"

# Syntax highlighting plugin for oh-my-zsh

source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# Starship prompt editor

eval "$(starship init zsh)"

# Changing the default toml location for Starship

export STARSHIP_CONFIG=~/.config/starship/starship.toml

