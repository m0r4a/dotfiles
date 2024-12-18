#!/bin/bash

# WALLPAPERS PATH
wallDIR="$HOME/Wallpapers/"

# Variables
focused_monitor=$(hyprctl monitors | awk '/^Monitor/{name=$2} /focused: yes/{print name}')

CURRENT_WALLPAPER_PATH=$(grep -m 1 '^wallpaper=' "$HOME/.cache/wal/colors.sh" | cut -d '=' -f 2 | tr -d '"')

# Getting the images
mapfile -d '' PICS < <(find "${wallDIR}" -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.gif" \) -print0)

# Temp value for random_pic
RANDOM_PIC=""

# Loop until the random pic isn't the same as the current one
while [[ "$RANDOM_PIC" == "$CURRENT_WALLPAPER_PATH" || -z "$RANDOM_PIC" ]]; do
    RANDOM_PIC="${PICS[$((RANDOM % ${#PICS[@]}))]}"
done

RANDOM_PIC_NAME="random"

# Rofi command
rofi_command="rofi -i -show -dmenu -config ~/.config/rofi/config-wallpaper.rasi"

# Function to display the wallpaper menu
menu() {
  formatted_name=$(echo "$RANDOM_PIC_NAME" | sed 's/_/ /g')
  printf "%s\x00icon\x1f%s\n" "$formatted_name" "$RANDOM_PIC"

  for pic_path in $(printf "%s\n" "${PICS[@]}" | sort); do
    pic_name=$(basename "$pic_path")
    formatted_pic_name=$(echo "$pic_name" | cut -d. -f1 | sed 's/_/ /g')
    printf "%s\x00icon\x1f%s\n" "$formatted_pic_name" "$pic_path"
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

  choice=$(echo $choice | sed 's/ /_/g')

  if [[ -z "$choice" ]]; then
    echo "No choice selected. Exiting."
    exit 0
  fi

  if [[ "$choice" == "$RANDOM_PIC_NAME" ]]; then
    wal -s --cols16 -i "$RANDOM_PIC" --backend haishoku --theme $choice
    change_wal "$RANDOM_PIC"
  else
    for pic_path in "${PICS[@]}"; do
      if [[ "$(basename "$pic_path")" == "$choice"* ]]; then
        wal -s --cols16 -i "$pic_path" --backend haishoku --theme $choice
        change_wal "$pic_path"
        break
      fi
    done
  fi

  killall waybar && waybar &
}

main
