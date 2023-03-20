import sys
sys.path.append('/home/m0r4a/.config/qtile/settings/widgetsCustom')
from wgSpotify import Spotify

from libqtile import widget
from libqtile.command import lazy
from libqtile import qtile

Inactive = "#504945"
NoBG = "00000000"
Red = "#EE4B2B"
White = "#F9F6EE"

def icon(icon, padd):
    return widget.TextBox(
    text=icon, 
    fontsize=22, 
    background=BGoff,
    foreground=FGoff,
    padding=padd)


def myseparator():
    return  widget.TextBox(
    text="//",
    fontsize=16,
    padding=6,
    background=NoBG,
    foreground=Red,
    )

def miniSeparator():
    return widget.TextBox(
    text=" ",
    fontsize=1,
    padding=1,
    background="#282120",
    )

def placeHolder():
    return widget.TextBox(
    text="Widget",
    fontsize=15,
    background=BGoff,
    foreground=FGoff,
    )        


left = "#458588"
mid = "#B16286"
midsqr = "#D3869B"
right = "#98971A"

primary_widgets = [

## Left
        widget.CurrentLayoutIcon(
            background=NoBG,
            scale=0.6,
            padding=-5,
        ),
        miniSeparator(),
        myseparator(),
        widget.KeyboardLayout(
            background=NoBG,
            foreground=White,
            configured_keyboards=['us','es'],
            display_map={'us':'','es':'󰺛'},
            fontsize=23
        ),
        myseparator(),
        widget.Pomodoro(
            fontsize=14,
            background=NoBG,
            color_active=White,
            color_break=Red,
            color_inactive=Inactive,
            length_pomodori=35,
            length_short_break=10,
            length_long_break=15,
            num_pomodori=4,
            prefix_active=' A: ',
            prefix_inactive=' I',
            prefix_break=' B: ',
            prefix_long_break=' LB: ',
            prefix_paused=' P',
        ),
        myseparator(),
        Spotify(
            format="{icon} {artist} - {track}"
        ),

        ## Mid
        widget.Spacer(),
        widget.GroupBox(
            active=White,
            inactive=Inactive,
            background=NoBG,
            font="Hack NFM",
            fontsize=24,
            highlight_method='line',
            highlight_color=[NoBG, Red],
            this_current_screen_border=Red
        ),

## Right
    widget.Spacer(),
    widget.TextBox(
        text=" ",
        fontsize=5,
        padding=1,
        background=NoBG,
    ),
]

secondary_widgets = []

widget_defaults = dict(
    font="Hack NFM",
    fontsize=13,
    padding=3,
)
extension_defaults = widget_defaults.copy()
