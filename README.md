# Stow Package Manager for Dotfiles

This repository contains an interactive terminal-based package manager built to handle **dotfiles** using [GNU Stow](https://www.gnu.org/software/stow/). This tool streamlines the process of enabling and disabling configurations through symlinks, making it easier to manage your setup.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [How to Use](#how-to-use)
- [Available Commands](#available-commands)
- [How It Works](#how-it-works)
- [Example Directory Structure](#example-directory-structure)
- [Contributing](#contributing)

## Introduction

This tool is designed for managing dotfiles in a structured way using GNU Stow. By leveraging symlinks, it allows you to enable and disable specific configurations in your home directory or other designated locations. Whether you prefer an interactive interface or quick command-line options, this manager has you covered.

## Features

- Interactive mode for managing packages with an easy-to-use terminal interface.
- Command-line mode for quick actions like enabling or disabling specific packages.
- Compatibility with multiple Linux distributions, macOS, and more.
- Automatically detects enabled and disabled packages.
- Simple feedback with clear output messages for success or errors.

## How to Use

1. Clone this repository into a location of your choice:
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

4. Organize your dotfiles under a `packages/` directory:
   ```
   dotfiles/
   ├── packages/
   │   ├── nvim/
   │   │   ├── init.vim
   │   ├── zsh/
   │   │   ├── .zshrc
   ```

5. Run the package manager in interactive mode:
   ```
   python3 manager.py
   ```

6. Alternatively, use command-line options for specific tasks (see [Available Commands](#available-commands)).

## Available Commands

The following options are available for command-line usage:

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

The tool is built around GNU Stow's functionality:

1. **Packages Directory:** All packages are stored in a `packages/` directory. Each package is a subdirectory containing the dotfiles or configuration files to symlink.
2. **Symlinks:** When you enable a package, GNU Stow creates symlinks in `$HOME` or `$HOME/.config`, depending on the file structure.
3. **Interactive Menu:** In interactive mode, you can use the arrow keys to navigate and toggle packages.
4. **Direct Commands:** Command-line options allow you to skip the interactive interface for quick actions.

## Example Directory Structure

The `packages/` directory should have a structure similar to this:
```
dotfiles/
├── packages/
│   ├── nvim/
│   │   ├── init.vim
│   │   ├── other-config.vim
│   ├── zsh/
│   │   ├── .zshrc
│   ├── tmux/
│   │   ├── .tmux.conf
```

When you enable the `nvim` package, the manager creates symlinks for `init.vim` and other files in the appropriate locations in your home directory.

## Contributing

Contributions are welcome! If you have ideas or improvements for this package manager, feel free to:

1. Fork the repository.
2. Create a new branch with your changes:
   ```
   git checkout -b feature/my-feature
   ```
3. Submit a pull request with a detailed explanation of your changes.

---

If you have any questions or run into issues, feel free to open an issue in the repository. Happy dotfile management!
