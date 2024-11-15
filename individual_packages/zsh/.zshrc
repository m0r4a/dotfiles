PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/bin/site_perl:/usr/bin/vendor_perl:/usr/bin/core_perl:~/scripts:/snap/bin:/opt/sonar-scanner

# Importing my aliases
source ~/.zsh_aliases

# Importing my environment variables
source ~/.zsh_env

# Fzf 
source <(fzf --zsh)

# Autosuggestions
bindkey '^\' autosuggest-accept

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


# Compilation flags
# export ARCHFLAGS="-arch x86_64"


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
