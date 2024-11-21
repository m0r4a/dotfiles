#!/bin/bash

# WALLPAPERS PATH
wallDIR="$HOME/Wallpapers/"

# Retrieve image files
mapfile -d '' PICS < <(find "${wallDIR}" -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.gif" \) -print0)

# Exit if no images are found
if [[ ${#PICS[@]} -eq 0 ]]; then
  echo "No image files found in $wallDIR."
  exit 1
fi

# Set the number of columns (fixed)
columns=3

# Calculate the number of rows needed
total_images=${#PICS[@]}
rows=$(( (total_images + columns - 1) / columns )) # Redondeo hacia arriba

# Limit the number of rows if too many (optional)
max_rows=5
[[ $rows -gt $max_rows ]] && rows=$max_rows

# Generate menu for rofi
menu() {
  for pic_path in "${PICS[@]}"; do
    pic_name=$(basename "$pic_path")
    printf "%s\x00icon\x1f%s\n" "$pic_name" "$pic_path"
  done
}

# Show rofi menu
choice=$(menu | rofi -dmenu -i -columns $columns -lines $rows -config ~/.config/rofi/config-wallpaper.rasi)

# Handle selection
if [[ -z "$choice" ]]; then
  echo "No choice selected."
  exit 0
else
  echo "Selected: $choice"
fi
