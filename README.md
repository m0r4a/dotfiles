# Dotfiles Repository with Integrated Package Manager

This repository contains my **dotfiles**, organized for efficient management using an integrated package manager built around [GNU Stow](https://www.gnu.org/software/stow/). This setup simplifies the process of enabling and disabling configurations using symlinks, making it easier to manage and switch between setups.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Showcase](#showcase)
- [How to Use](#how-to-use)
- [Available Commands](#available-commands)
- [How It Works](#how-it-works)
- [Example Directory Structure](#example-directory-structure)
- [Contributing](#contributing)
- [TODOs](#todos)

## Introduction

This repository houses my personal dotfiles for tools like Neovim, Hyprland, Zsh, and others. By leveraging an integrated package manager, you can quickly enable or disable these configurations, ensuring a seamless experience across systems. This approach provides flexibility, whether you prefer an interactive terminal interface or command-line efficiency.

## Features

- Centralized storage for dotfiles with a consistent structure.
- Integrated package manager for managing configurations interactively or via the command line.
- Simplifies symlink creation using GNU Stow.
- Automatically detects enabled and disabled packages.
- Compatible with Linux, macOS, and other Unix-based systems.

## Showcase

<p align="center">
    <img src="resources/showcase.gif" alt="GIF of the package manager"/>
</p>


## Showcase

<p align="center">
    <img src="resources/showcase2.gif" alt="GIF of the package manager"/>
</p>

## How to Use

1. Clone this repository into your preferred location:
   ```
   git clone https://github.com/username/dotfiles.git ~/dotfiles
   ```

2. Navigate to the directory:
   ```
   cd ~/dotfiles
   ```

3. Ensure GNU Stow is installed. If not, install it using your package manager:
   ```
   sudo apt install stow      # For Debian-based systems
   sudo pacman -S stow        # For Arch-based systems
   brew install stow          # For macOS
   ```

4. Ensure your dotfiles are organized under the `packages/` directory.

5. Run the package manager in interactive mode:
   ```
   python3 package_manager.py
   ```

6. Alternatively, use command-line options for specific tasks (see [Available Commands](#available-commands)).

## Available Commands

You can use the following command-line options to manage your configurations:

```
-i, --install PACKAGE         Enable one or more packages (e.g., nvim, zsh).
-r, --remove PACKAGE          Disable one or more packages.
-le, --list-enabled           List all currently enabled packages.
-ld, --list-disabled          List all currently disabled packages.
-la, --list-all               List all available packages.
```

Examples:
```
# Enable configurations for nvim and zsh
python3 manager.py -i nvim zsh

# Disable the nvim configuration
python3 manager.py -r nvim

# List all enabled packages
python3 manager.py -le

# List all disabled packages
python3 manager.py -ld
```

## How It Works

1. **Packages Directory:** Dotfiles are grouped into packages under the `packages/` directory. Each package corresponds to a specific tool or application.
2. **Symlinks with Stow:** GNU Stow handles the creation of symlinks in `$HOME` or `$HOME/.config` based on the package structure.
3. **Interactive Mode:** Navigate and toggle packages using an easy-to-use terminal interface.
4. **Direct Commands:** Command-line options allow quick enable/disable actions.

## Example Directory Structure

Organize your dotfiles in the `packages/` directory as follows:
```
dotfiles/
├── packages/
│   ├── nvim/
│   │   ├── .config/
│   │   │   ├── nvim/
│   │   │   │   ├── init.lua
│   │   │   │   ├── etc.lua
│   ├── hypr/
│   │   ├── .config/
│   │   │   ├── hypr/
│   │   │   │   ├── hyprland.conf
│   │   │   │   ├── hyprpaper.conf
│   │   │   │   ├── etc.conf
│   ├── zsh/
│   │   ├── .zshrc
│   │   ├── .zsh_env
│   │   ├── .zsh_etc
```

When enabling the `nvim` package, the manager creates symlinks for its configuration files under `$HOME/.config/nvim`.

When enabling the `zsh` package, the manager creates symlinks for its configuration files directly under `$HOME`, as the files are not located within a .config directory in the package.

## Contributing

Contributions are welcome! Feel free to:

1. Fork the repository.
2. Create a branch for your changes:
   ```
   git checkout -b feature/my-feature
   ```
3. Submit a pull request with a clear description of your improvements.

## Todos

- Add a feature to replace existing dotfiles in the repository with the user's current setup. - For example, copy `$HOME/.config/hypr/` to `packages/hypr/.config/hypr/`. - Ensure proper structure and prompt for confirmation if files already exist.

---

If you encounter any issues or have questions, open an issue in the repository. Enjoy managing your dotfiles effortlessly!
