# Gruvbox

from libqtile import widget
from libqtile.command import lazy
from libqtile import qtile

# Esto es new widgets

# pp is for purple
pp=["start the list with 1 bro, wtf","e1bee7", "#ce93d8", "#ba68c8", "#ab47bc", "#9c27b0", "#8e24aa", "#8b1fa2", "#6a1b91", "#4a148c"]

# bu is for blue
bu=["start the list with 1 bro, wtf", "#bbdefb", "#90caf9", "#64b5f6", "#42a5f5", "#2196f3", "#1e88e5", "#1976d2", "#1565c0", "#0d47a1"]

# gn is for green
gn=["start the list with 1 bro, wtf", "#c8e6c9", "#81c784", "#66bb6a", "#4caf50", "#43a047", "#388e3c", "#2e7d32", "#1b5e20"]


Red = "#FB4934"
Green = "#B8BB26"
Yellow = "#FABD2F"
Blue = "#83A598"
Purple = "#D3869B"
Aqua = "#8EC07C"
Orange = "#FE8019"

BGH0 = "#1D2021"
FGoff = "#FBF1C7"

BGS0 = "#32302F"
FGS0 = "#FBF1C7"

BG1 = "#3C3836"
FG1 = "#EBDBB2"

BG2 = "#504945"
FG2 = "#D5C4A1"

BG3 = "#665C54"
FG3 = "#BDAE93"

BG4 = "#7C6F64"
FG4 = "A89984"

BGoff = "#FF0000"


def icon(icon, padd):
    return widget.TextBox(
    text=icon, 
    fontsize=22, 
    background=BGoff,
    foreground=FGoff,
    padding=padd)


def myseparator(color):
    return  widget.TextBox(
    text="",
    fontsize=16,
    padding=6,
    background="#282120",
    foreground=color,
    )


def myseparator2(color):
    return  widget.TextBox(
    text="",
    fontsize=16,
    padding=6,
    background="#282120",
    foreground=color,
    )

def placeHolder():
    return widget.TextBox(
    text="Widget",
    fontsize=15,
    background=BGoff,
    foreground=FGoff,
    )        

def miniSeparator():
    return widget.TextBox(
    text=" ",
    fontsize=1,
    padding=1,
    background="#282120",
    )

left = "#458588"
mid = "#B16286"
midsqr = "#D3869B"
right = "#98971A"

primary_widgets = [

## Left
        widget.CurrentLayoutIcon(
            background=BGoff,
            scale=0.6,
            padding=-5,
        ),
        miniSeparator(),
        myseparator(Green),
        widget.KeyboardLayout(
                    background=BGoff,
                    foreground=FGoff,
                    configured_keyboards=['us','es'],
                    display_map={'us':'','es':'󰺛'},
                    fontsize=23
        ),
        myseparator(Blue),
        icon("墳", 3),
                widget.Volume(
                    background=BGoff,
                    foreground=FGoff,
                    padding=2,
        ),
        myseparator(Yellow),
        miniSeparator(),
        widget.Net(
            foreground=FGoff,
            format=' {up}   {down} '
        ),


        ## Mid
        widget.Spacer(),
        widget.GroupBox(
            active=FG2,
            inactive=BG2,
            background=BGoff,
            font="Hack NFM",
            fontsize=24,
            highlight_method='line',
            highlight_color=BGS0,
            this_current_screen_border=FG1
        ),

## Right

        widget.Spacer(),
        icon("",5),
        widget.OpenWeather(
            location='Santiago, MX',
            format='{main_temp}°{units_temperature}',
            fontsize=13,
            foreground=FGoff,
            padding=0,
        ),
        miniSeparator(),
        myseparator(Green),
        miniSeparator(),
        widget.Battery(
            background=BGoff,
            foreground=FGoff,
            format='{char} {percent:2.0%}',
            full_char="",
            charge_char="",
            discharge_char="",
            low_percentage=0.2,
            low_foreground=Red,
            notify_below=10,
            notification_timeout=4,
            show_short_text=False,
            update_interval=1

        ),
        myseparator2(Blue),
        widget.Systray(background=BGoff, padding=2),
        miniSeparator(),
        myseparator(Yellow),
        miniSeparator(),
        miniSeparator(),
        icon("",0),
        widget.Clock(
            format="%b %d - %H:%M",
            fontsize=14,
            background=BGoff,
            foreground=FGoff,
            padding=8,
         ),
]

secondary_widgets = []

widget_defaults = dict(
    font="Hack NFM",
    fontsize=13,
    padding=3,
)
extension_defaults = widget_defaults.copy()
