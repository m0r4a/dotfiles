#!/usr/bin/env python3

"""
A terminal-based package manager that uses GNU Stow to manage dotfiles and packages.
It provides an interactive interface to enable/disable packages by creating/removing symlinks.
"""

import sys
import termios
import tty
import os
from os import path
import subprocess
import shutil
import argparse
from typing import List, Tuple

COLORS = {
    'GREEN': "\033[32m",
    'RED': "\033[31m",
    'RESET': "\033[0m"
}

PACKAGE_INSTALL_COMMANDS = {
    'debian': 'sudo apt install stow',
    'fedora': 'sudo dnf install stow',
    'arch': 'sudo pacman -S stow',
    'macos': 'brew install stow',
    'windows': 'why are you using windows?'
}


def create_parser() -> argparse.ArgumentParser:
    """Create and configure the argument parser for the package manager."""
    parser = argparse.ArgumentParser(
        description="Terminal-based package manager using GNU Stow to manage dotfiles and packages.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                    # Run in interactive mode
  %(prog)s -i nvim hypr       # Install specified packages
  %(prog)s -r nvim            # Remove specified package
  %(prog)s -le                # List enabled packages
  %(prog)s -la                # List all available packages
        """
    )

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-i", "--install", nargs="+", metavar="PACKAGE",
                       help="directly install specified packages")
    group.add_argument("-r", "--remove", nargs="+", metavar="PACKAGE",
                       help="directly remove specified packages")
    group.add_argument("-le", "--list-enabled", action="store_true",
                       help="list all enabled packages")
    group.add_argument("-ld", "--list-disabled", action="store_true",
                       help="list all disabled packages")
    group.add_argument("-la", "--list-all", action="store_true",
                       help="list all available packages")

    return parser


def check_stow_installed() -> None:
    """Verify that GNU Stow is installed in the system."""
    if not shutil.which("stow"):
        commands = "\n".join(
            f"  - {distro}: {cmd}"
            for distro, cmd in PACKAGE_INSTALL_COMMANDS.items()
        )
        print(
            f"{COLORS['RED']}Error: GNU Stow is not installed or not found in PATH."
            f"{COLORS['RESET']}\nPlease install it using your package manager:\n{
                commands}"
        )
        sys.exit(1)


class PackageManager:
    def __init__(self, packages_dir: str = "./packages"):
        """Initialize the package manager."""
        self.home = path.expanduser("~")
        self.config_dirs = [self.home, path.join(self.home, ".config")]
        self.packages_dir = packages_dir

    def get_packages(self) -> List[Tuple[str, bool]]:
        """Get list of packages and their installation status."""
        if not path.isdir(self.packages_dir):
            raise FileNotFoundError(
                f"Directory {self.packages_dir} does not exist")

        packages = [
            entry for entry in os.listdir(self.packages_dir)
            if path.isdir(path.join(self.packages_dir, entry))
        ]

        items = [(pkg, self._is_package_installed(pkg)) for pkg in packages]

        return sorted(items, key=lambda x: x[1])

    def get_available_packages(self) -> List[str]:
        """Get list of available package names."""
        if not path.isdir(self.packages_dir):
            raise FileNotFoundError(
                f"Directory {self.packages_dir} does not exist")

        return sorted(
            entry for entry in os.listdir(self.packages_dir)
            if path.isdir(path.join(self.packages_dir, entry))
        )

    def verify_packages_exist(self, packages: List[str]) -> None:
        """Verify that all specified packages exist."""
        available = set(self.get_available_packages())
        invalid = set(packages) - available

        if invalid:
            raise ValueError(
                f"The following packages do not exist: {
                    ', '.join(sorted(invalid))}\n"
                f"Available packages are: {', '.join(sorted(available))}"
            )

    def _is_package_installed(self, package: str) -> bool:
        """Check if a package is installed by looking for its symlinks."""
        package_path = f"packages/{package}/"

        for directory in self.config_dirs:
            try:
                for entry in os.scandir(directory):
                    if (entry.is_symlink() and
                            package_path in os.readlink(entry.path)):
                        return True
            except (FileNotFoundError, PermissionError) as e:
                print(f"Warning: Could not access {directory}: {e}")
        return False

    def update_packages(self, enabled: List[str], disabled: List[str]) -> None:
        """Update packages using GNU Stow."""
        os.chdir(self.packages_dir)

        for package in enabled:
            self._run_stow_command(package, install=True)

        for package in disabled:
            self._run_stow_command(package, install=False)

        os.chdir("..")

    def _run_stow_command(self, package: str, install: bool) -> None:
        """Run stow command for a package."""
        action = "enable" if install else "disable"
        cmd = ["stow", "-D" if not install else "", package, "-t", self.home]
        cmd = [arg for arg in cmd if arg]  # Remove empty strings

        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                print(f"{COLORS['GREEN']}✓{COLORS['RESET']} {
                      action.capitalize()}d: {package}")
            else:
                print(f"{COLORS['RED']}✗{COLORS['RESET']} Failed to {
                      action} {package}: {result.stderr}")
        except subprocess.SubprocessError as e:
            print(f"✗ Error running stow for {package}: {e}")


class TerminalUI:
    @staticmethod
    def get_key() -> str:
        """Read a single keypress or an escape sequence."""
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)

        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
            if ch == '\x1b':
                ch += sys.stdin.read(2)
            return ch
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    @staticmethod
    def draw_menu(items: List[Tuple[str, bool]], active: int) -> None:
        """Draw the interactive menu."""
        print("\033c", end="")  # Clear screen
        print("Select packages to enable/disable\n")

        for i, (item, checked) in enumerate(items):
            prefix = "[*]" if checked else "[ ]"
            cursor = "> " if i == active else "  "
            print(f"{cursor}{prefix} {item}")

        print("\nControls:")
        print("↑/k/n: Up | ↓/j/p: Down | Space: Toggle | Enter: Confirm | q: Quit")


class PackageMenu:
    def __init__(self, package_manager: PackageManager):
        """Initialize the package menu."""
        self.package_manager = package_manager
        self.items = package_manager.get_packages()
        self.original_items = self.items[:]
        self.active = 0
        self._key_actions = {
            'q': lambda: True,
            '\r': lambda: True,
            ' ': self._toggle_current_item,
            **{k: self._move_up for k in ['k', 'p', '\x1b[A']},
            **{k: self._move_down for k in ['j', 'n', '\x1b[B']}
        }

    def _move_up(self) -> bool:
        self.active = (self.active - 1) % len(self.items)
        return False

    def _move_down(self) -> bool:
        self.active = (self.active + 1) % len(self.items)
        return False

    def _toggle_current_item(self) -> bool:
        self.items[self.active] = (
            self.items[self.active][0],
            not self.items[self.active][1]
        )
        return False

    def handle_input(self) -> bool:
        """Handle single keypress input."""
        key = TerminalUI.get_key()
        action = self._key_actions.get(key, lambda: False)
        return action()

    def display_changes(self, enabled: List[str], disabled: List[str]) -> None:
        """Display selected packages and pending changes."""
        print("\nChanges to apply:")
        if enabled:
            print(f"{COLORS['GREEN']}To enable:{
                  COLORS['RESET']}", ", ".join(enabled))
        if disabled:
            print(f"{COLORS['RED']}To disable:{
                  COLORS['RESET']}", ", ".join(disabled))

    def run(self) -> Tuple[List[str], List[str]]:
        """Run the interactive menu loop."""
        while True:
            TerminalUI.draw_menu(self.items, self.active)
            if self.handle_input():
                break

        return get_changes(self.original_items, self.items)


def get_changes(original: List[Tuple[str, bool]],
                updated: List[Tuple[str, bool]]) -> Tuple[List[str], List[str]]:
    """Determine changes between original and updated states."""
    return (
        [item for (item, new_state), (_, old_state) in zip(updated, original)
         if not old_state and new_state],
        [item for (item, new_state), (_, old_state) in zip(updated, original)
         if old_state and not new_state]
    )


def apply_changes(package_manager: PackageManager,
                  enabled: List[str], disabled: List[str]) -> None:
    """Apply the package changes after confirmation."""
    print("\nPress Enter to confirm or Ctrl+C to cancel...")
    try:
        input()
        print("Applying changes...")
        package_manager.update_packages(enabled, disabled)
        print("Done!")
    except KeyboardInterrupt:
        print("\nOperation cancelled.")


def handle_cli_mode(args: argparse.Namespace, package_manager: PackageManager) -> None:
    """Handle command-line interface mode operations."""
    try:
        if args.install:
            package_manager.verify_packages_exist(args.install)
            package_manager.update_packages(enabled=args.install, disabled=[])

        elif args.remove:
            package_manager.verify_packages_exist(args.remove)
            package_manager.update_packages(enabled=[], disabled=args.remove)

        elif any([args.list_enabled, args.list_disabled, args.list_all]):
            packages = package_manager.get_packages()
            if args.list_enabled:
                _display_package_list("Enabled packages:",
                                      [pkg for pkg, enabled in packages if enabled])
            elif args.list_disabled:
                _display_package_list("Disabled packages:",
                                      [pkg for pkg, enabled in packages if not enabled])
            else:  # list_all
                enabled = [pkg for pkg, is_enabled in packages if is_enabled]
                disabled = [pkg for pkg,
                            is_enabled in packages if not is_enabled]

                print("Available packages:")
                if enabled:
                    print(f"\n{COLORS['GREEN']}Enabled:{COLORS['RESET']}")
                    print("\n".join(f"  {pkg}" for pkg in enabled))
                if disabled:
                    print(f"\n{COLORS['RED']}Disabled:{COLORS['RESET']}")
                    print("\n".join(f"  {pkg}" for pkg in disabled))

    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def _display_package_list(title: str, packages: List[str]) -> None:
    """Helper function to display a list of packages."""
    if packages:
        print(f"{title}")
        print("\n".join(f"  {pkg}" for pkg in packages))
    else:
        print(f"No packages are currently {title.lower().rstrip(':')}")


def main():
    """Main program loop."""
    try:
        check_stow_installed()
        parser = create_parser()
        args = parser.parse_args()
        package_manager = PackageManager()

        if any([args.install, args.remove, args.list_enabled,
               args.list_disabled, args.list_all]):
            handle_cli_mode(args, package_manager)
            return

        menu = PackageMenu(package_manager)
        enabled, disabled = menu.run()

        if not enabled and not disabled:
            print("\nNo changes to apply.")
            return

        menu.display_changes(enabled, disabled)
        apply_changes(package_manager, enabled, disabled)

    except KeyboardInterrupt:
        print("\nOperation cancelled.")
    except Exception as e:
        print(f"\nError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
