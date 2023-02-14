from libqtile import widget
from libqtile.command import lazy
from libqtile import qtile

# Esto es og widgets

# pp is for purple
pp=["start the list with 1 bro, wtf","e1bee7", "#ce93d8", "#ba68c8", "#ab47bc", "#9c27b0", "#8e24aa", "#8b1fa2", "#6a1b91", "#4a148c"]

# bu is for blue
bu=["start the list with 1 bro, wtf", "#bbdefb", "#90caf9", "#64b5f6", "#42a5f5", "#2196f3", "#1e88e5", "#1976d2", "#1565c0", "#0d47a1"]

# gn is for green
gn=["start the list with 1 bro, wtf", "#c8e6c9", "#81c784", "#66bb6a", "#4caf50", "#43a047", "#388e3c", "#2e7d32", "#1b5e20"]

def sidebarLeft(position):
    return widget.TextBox(
    text="",
    fontsize=22,
    foreground=position,
    padding=0
    )

def sidebarRight(position):
    return widget.TextBox(
    text="",
    fontsize=22,
    foreground=position,
    padding=0
    )

def icon(icon, padd):
    return widget.TextBox(
    text=icon, 
    fontsize=22, 
    background=left,
    padding=padd)

def myseparator():
    return  widget.TextBox(
    text="",
    fontsize=12,
    background=left,
    foreground=[pp[8],pp[7]],
    )

left=[pp[5],pp[4],pp[3],pp[2]]
mid=[bu[5],bu[4],bu[3],bu[2]]
right=[gn[5],gn[4],gn[3],gn[2]]

primary_widgets = [
    ### Left
                sidebarLeft(left),
                icon("ﮮ", 3),
                widget.CheckUpdates(
                    font='Hack Nerd Font Mono',
                    fontshadow="000000",
                    fontsize="14",
                    distro='Arch',
                    colour_have_updates="ffffff",
                    colour_no_updates="#00ff21",
                    display_format='{updates}',
                    background=left,
                    no_update_string="",
                    update_interval=1800,
                    padding=3, 
                ),
                myseparator(),
                icon("墳", 3),
                widget.Volume(
                    background=left,
                    padding=2,
                ),
                myseparator(),
                widget.Battery(
                    background=left,
                    format='{char} {percent:2.0%}',
                    full_char="",
                    charge_char="",
                    discharge_char="",
                    low_percentage=0.2,
                    low_foreground="#FF0000",
                    notify_below=10,
                    notification_timeout=4,
                    show_short_text=False,
                    update_interval=1

                ),
                sidebarRight(left),
                widget.TextBox(text=" "),
#                widget.Image(
#                    filename='~/.config/qtile/icns/Teams.png',
#                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("teams")},
#                ),
    ### Mid
                widget.Spacer(),
                sidebarLeft(mid),
                widget.GroupBox(
                    active='#000000',
                    inactive="#ffffff",
                    background=mid,
                    borderwidth=2,
                    font="Hack NFM",
                    fontsize=24,
                    rounded=True,
                    #Color de el cuadrito cuando lo seleccionas
                    highlight_color=[bu[6],bu[5], bu[4], bu[3]],
                    highlight_method='line',
                    #Color de la barra de cuando lo selecionas
                    this_current_screen_border=[pp[7],pp[5]],
                    other_screen_border="ffffff"
                ),
                sidebarRight(mid),
                widget.Spacer(),
    ### Right 
                sidebarLeft(right),
                widget.TextBox(text="", background=right, fontsize=24, padding=0),
                widget.Clock(
                    format="%b %d - %H:%M",
                    fontsize=14,
                    background=right,
                    padding=8,
                ),
                widget.CurrentLayoutIcon(
                    background=right,
                    scale=0.7,
                    padding=-3,
                ),
                sidebarRight(right),
                
]

secondary_widgets = []

widget_defaults = dict(
    font="Hack NFM",
    fontsize=13,
    padding=3,
)
extension_defaults = widget_defaults.copy()
