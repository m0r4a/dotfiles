from libqtile.config import Key
from libqtile.command import lazy

my_terminal = 'alacritty'
# Check in the line 73 if you have problems with the brightness

mod = "mod4"

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Tab", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
   
    # Miscellaneous
    Key([mod], "Menu", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"), 


    #### Custom

    # Apps 
    Key([mod], "Return", lazy.spawn(my_terminal), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn("firefox"), desc="Launch FireFox"),
    Key([mod], "s", lazy.spawn("steam"), desc="Launch steam"),
    Key([mod], "o", lazy.spawn("obsidian"), desc="Launch obsidian"),
    Key([mod], "p", lazy.spawn("bitwarden-desktop"), desc="Launch Bitwarden"),

    # Rofi
    Key([mod], "space", lazy.spawn("rofi -show run -show-icons"), desc="Launch Rofi"),
    Key([mod, "shift"], "space", lazy.spawn("rofi -show window"), desc="Launch Rofi"),

    # Screenshot
    Key([], "Print", lazy.spawn("scrot '/home/m0r4a/Screenshots/%F\ %T.png'"), desc="Takes a ScreenShoot"),
    Key([mod], "Print", lazy.spawn("spectacle"), desc="Takes a ScreenShoot"),

    # Config qtile
    Key([mod, "shift"],"c", lazy.spawn("code ~/.config/qtile/") ),


    # Volume
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    Key([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    # Brightness
    Key([], "Pause", lazy.spawn("brightnessctl set +10%")),
    Key([], "Scroll_Lock", lazy.spawn("brightnessctl set 10%-")),

    # Keyboard layout (qtile widget)
    Key([mod], "k", lazy.widget["keyboardlayout"].next_keyboard(), desc="Next keyboard layout."),
]
