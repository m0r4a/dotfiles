PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/bin/site_perl:/usr/bin/vendor_perl:/usr/bin/core_perl:~/scripts:/snap/bin:/opt/sonar-scanner:/home/m0r4a/.local/share/gem/ruby/3.3.0/bin

# Importing my aliases
source ~/.zsh_aliases

## Private stuff
source ~/.zsh_private

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

# This function lets you convert .dot files from the
# Python “diagrams” library to .png images with no background.
dotpng() {
  local name="${1%.*}"
  local input="${name}.dot"
  local output="${name}.png"

  if [[ ! -f "$input" ]]; then
    echo "❌ Error: '$input' does not exist." >&2
    return 1
  fi

  dot -Tpng -Ncolor=black -Nfontcolor=white -Gfontcolor=white -Gbgcolor=transparent "$input" -o "$output" \
    && echo "✅ Generated: $output" \
    || echo "❌ Failed to generate PNG from $input" >&2
}


if [ $(echo $TERM) = "xterm-kitty" ]; then
  fastfetch --kitty ~/.config/fastfetch/darkrai.png --logo-padding-right 2 --logo-padding-left 3
fi

# Syntax highlighting plugin for oh-my-zsh

source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# Starship prompt editor

eval "$(starship init zsh)"

eval "$(zoxide init --cmd cd zsh)"
