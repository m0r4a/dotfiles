#!/bin/bash

th="${1,,}"

# ███████╗██╗   ██╗███╗   ██╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗███████╗
# ██╔════╝██║   ██║████╗  ██║██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║██╔════╝
# █████╗  ██║   ██║██╔██╗ ██║██║        ██║   ██║██║   ██║██╔██╗ ██║███████╗
# ██╔══╝  ██║   ██║██║╚██╗██║██║        ██║   ██║██║   ██║██║╚██╗██║╚════██║
# ██║     ╚██████╔╝██║ ╚████║╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║███████║
# ╚═╝      ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
                                                                          

# Function which gives you a random number betwwen 0 and 1 number lower than the argument

rand () {
	echo $(shuf -i 0-$(( $1 - 1 )) -n1)
}

# Function for getting an array of the backgrounds in the specified theme's folder, pick one random item
# and then set the wallpaper and bar according to the theme

## $1=ThemeName $2="$BarName"

theme(){

	local BGS=($(ls ~/Wallpapers/$1))
	local BG=${BGS[$(rand ${#BGS[@]})]}

	if [ $th = $1 ]; then
		feh --bg-fill ~/Wallpapers/$1/$BG &
		sed -i "s/$OGBar/$2/" ~/.config/qtile/settings/screens.py
	fi
}

# Function for creating the bars in a easy way

# $1=size, $2=opacity (between 0-1), $3="Background" (in hex code)

bar(){
	echo "     return bar.Bar(widgets, $1, opacity=$2,background='$3')"
}

if [ $th = "random" ] || [ $th = "rand" ]; then
	Themes=($(ls ~/.config/qtile/settings/themes/ | sed -e 's/__pycache__//' -e 's/.py/ /' | grep "\S"))
	th=${Themes[$(rand ${#Themes[@]})]}
fi




#  ██████╗██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███████╗    ████████╗██╗  ██╗███████╗███╗   ███╗███████╗
# ██╔════╝██║  ██║██╔══██╗████╗  ██║██╔════╝ ██╔════╝    ╚══██╔══╝██║  ██║██╔════╝████╗ ████║██╔════╝
# ██║     ███████║███████║██╔██╗ ██║██║  ███╗█████╗         ██║   ███████║█████╗  ██╔████╔██║█████╗  
# ██║     ██╔══██║██╔══██║██║╚██╗██║██║   ██║██╔══╝         ██║   ██╔══██║██╔══╝  ██║╚██╔╝██║██╔══╝  
# ╚██████╗██║  ██║██║  ██║██║ ╚████║╚██████╔╝███████╗       ██║   ██║  ██║███████╗██║ ╚═╝ ██║███████╗
#  ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝       ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚══════╝
                                                                                                   

# Searching for the original value of the bar

OGBar=$(sed -n 11p ~/.config/qtile/settings/screens.py)

# Setting a var for the path

FILE=~/.config/qtile/settings/themes/$th.py

# Checking if the theme exist, if it does overwrites the widget file with the theme's file

if [ -f "$FILE" ]; then
	cat ~/.config/qtile/settings/themes/$th.py > ~/.config/qtile/settings/widgets.py
	echo "Theme changed"

# If the theme doesn't exist, shows the available themes

else 
    echo "The list of available themes are:"
    ls ~/.config/qtile/settings/themes/ | sed -e 's/__pycache__//' -e 's/.py/ /' | grep "\S"
fi


# ████████╗██╗  ██╗███████╗███╗   ███╗███████╗███████╗
# ╚══██╔══╝██║  ██║██╔════╝████╗ ████║██╔════╝██╔════╝
#    ██║   ███████║█████╗  ██╔████╔██║█████╗  ███████╗
#    ██║   ██╔══██║██╔══╝  ██║╚██╔╝██║██╔══╝  ╚════██║
#    ██║   ██║  ██║███████╗██║ ╚═╝ ██║███████╗███████║
#    ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚══════╝╚══════╝
                                                    

### Gruvbox

GBBar=$(bar 30 1 "282120")

theme gruvbox "$GBBar"


### CyberPunk

CPBar=$(bar 25 1 "00000000")

theme cyberpunk "$CPBar"


### Focus

FocusBar=$(bar 25 1 "00000000")

theme focus "$FocusBar"



#  ██████╗███████╗ ██████╗     ██████╗ ███████╗██╗      ██████╗  █████╗ ██████╗ 
# ██╔════╝██╔════╝██╔════╝     ██╔══██╗██╔════╝██║     ██╔═══██╗██╔══██╗██╔══██╗
# ██║     █████╗  ██║  ███╗    ██████╔╝█████╗  ██║     ██║   ██║███████║██║  ██║
# ██║     ██╔══╝  ██║   ██║    ██╔══██╗██╔══╝  ██║     ██║   ██║██╔══██║██║  ██║
# ╚██████╗██║     ╚██████╔╝    ██║  ██║███████╗███████╗╚██████╔╝██║  ██║██████╔╝
#  ╚═════╝╚═╝      ╚═════╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
                                                                              

if [ -f "$FILE" ]; then
	qtile cmd-obj -o cmd -f reload_config
fi
