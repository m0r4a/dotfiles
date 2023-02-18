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


Red = "#CC241D"
Green = "#98971A"
Yellow = "#D79921"
Blue = "#458588"
Purple = "#B16286"
Aqua = "#689D6A"
Orange = "#D65D0E"

BGH0 = "#1D2021"
FGH0 = "#FBF1C7"

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

BGoff = "#282120"


def icon(icon, padd):
    return widget.TextBox(
    text=icon, 
    fontsize=22, 
    background=left,
    padding=padd)

def myseparator(color):
    return  widget.TextBox(
    text="|",
    fontsize=15,
    background="#282120",
    foreground=color,
    )

def placeHolder():
    return widget.TextBox(
    text="Widget",
    fontsize=15,
    background=BGoff,
    foreground=FGH0,
    )        
        

left = "#458588"
mid = "#B16286"
midsqr = "#D3869B"
right = "#98971A"

primary_widgets = [

## Left
        myseparator(Green),
        placeHolder(),
        myseparator(Blue),
        placeHolder(),
        myseparator(Yellow),
        placeHolder(),
        myseparator(Red),


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
        this_current_screen_border=FG1,

        ),

## Right

        widget.Spacer(),
        myseparator(Green),
        placeHolder(),
        myseparator(Blue),
        placeHolder(),
        myseparator(Yellow),
        placeHolder(),
        myseparator(Red),
]

secondary_widgets = []

widget_defaults = dict(
    font="Hack NFM",
    fontsize=13,
    padding=3,
)
extension_defaults = widget_defaults.copy()
