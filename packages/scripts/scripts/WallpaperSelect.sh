#!/bin/bash

# WALLPAPERS PATH
wallDIR="$HOME/Wallpapers/"

# Variables
focused_monitor=$(hyprctl monitors | awk '/^Monitor/{name=$2} /focused: yes/{print name}')

# Retrieve image files using null delimiter to handle spaces in filenames
mapfile -d '' PICS < <(find "${wallDIR}" -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.gif" \) -print0)

# Random picture
RANDOM_PIC="${PICS[$((RANDOM % ${#PICS[@]}))]}"
RANDOM_PIC_NAME=". random"

# Rofi command
rofi_command="rofi -i -show -dmenu -config ~/.config/rofi/config-wallpaper.rasi"

# Function to display the wallpaper menu
menu() {
  printf "%s\x00icon\x1f%s\n" "$RANDOM_PIC_NAME" "$RANDOM_PIC"
  
  # Sort and format options
  for pic_path in $(printf "%s\n" "${PICS[@]}" | sort); do
    pic_name=$(basename "$pic_path")
    printf "%s\x00icon\x1f%s\n" "$(echo "$pic_name" | cut -d. -f1)" "$pic_path"
  done
}

# Function to apply wallpaper changes
change_wal() {
  local wallpaper="$1"
  hyprctl hyprpaper preload "$wallpaper"
  hyprctl hyprpaper wallpaper "eDP-1, $wallpaper"
  hyprctl hyprpaper wallpaper "HDMI-A-1, $wallpaper"

  cp $wallpaper ~/.config/rofi/.current_wallpaper

  config_file="$HOME/.config/hypr/hyprpaper.conf"
  cat > "$config_file" << EOF
preload = $wallpaper
wallpaper = eDP-1, $wallpaper
wallpaper = HDMI-A-1, $wallpaper
# ipc = off
EOF
}

# Main function to handle wallpaper selection
main() {
  local choice=$(menu | $rofi_command | xargs) # Trim whitespace

  if [[ -z "$choice" ]]; then
    echo "No choice selected. Exiting."
    exit 0
  fi

  if [[ "$choice" == "$RANDOM_PIC_NAME" ]]; then
    wal -s --cols16 -i "$RANDOM_PIC" -s
    change_wal "$RANDOM_PIC"
  else
    for pic_path in "${PICS[@]}"; do
      if [[ "$(basename "$pic_path")" == "$choice"* ]]; then
        wal -s --cols16 -i "$pic_path" -s
        change_wal "$pic_path"
        break
      fi
    done
  fi

  killall waybar && waybar &
}

main
