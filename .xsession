#!/bin/sh

userresources=$HOME/.Xresources
usermodmap=$HOME/.Xmodmap
sysresources=/etc/X11/xinit/.Xresources
sysmodmap=/etc/X11/xinit/.Xmodmap

# merge in defaults and keymaps

if [ -f $sysresources ]; then
    xrdb -merge $sysresources
fi

if [ -f $sysmodmap ]; then
    xmodmap $sysmodmap
fi

if [ -f "$userresources" ]; then
    xrdb -merge "$userresources"
fi

if [ -f "$usermodmap" ]; then
    xmodmap "$usermodmap"
fi

# start some nice programs

if [ -d /etc/X11/xinit/xinitrc.d ] ; then
 for f in /etc/X11/xinit/xinitrc.d/?*.sh ; do
  [ -x "$f" ] && . "$f"
 done
 unset f
fi

# Wallpaper
feh --bg-fill Wallpapers/Arch.jpg &
# Picom
picom &
# Dunst
dunst &
# Two screens config (very prone to not work in other devices)
xrandr --output LVDS-1 --primary --mode 1280x800 --pos 0x0 --rotate normal --output DP-1 --mode 1280x800 --pos 1280x0 --rotate normal
# Color calibration
xcalib ~/ColorProfile.icc &
# Network manager applet
nm-applet &
