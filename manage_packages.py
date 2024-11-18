#!/usr/bin/env python3

"""
A terminal-based package manager that uses GNU Stow to manage dotfiles and packages.
It provides an interactive interface to enable/disable packages by creating/removing symlinks.
"""

import sys
import termios
import tty
import os
import subprocess
from typing import List, Tuple

GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"


class PackageManager:
    def __init__(self, packages_dir: str = "./packages"):
        """
        Initialize the package manager.

        Args:
            packages_dir: Directory containing the packages to manage
        """
        self.home = os.path.expanduser("~")
        self.config_dirs = [self.home, os.path.join(self.home, ".config")]
        self.packages_dir = packages_dir

    def get_packages(self) -> List[Tuple[str, bool]]:
        """
        Get list of packages and their installation status.

        Returns:
            List of tuples containing (package_name, is_installed)

        Raises:
            FileNotFoundError: If packages directory doesn't exist
        """
        if not os.path.isdir(self.packages_dir):
            raise FileNotFoundError(
                f"Directory {self.packages_dir} does not exist")

        packages = [
            entry for entry in os.listdir(self.packages_dir)
            if os.path.isdir(os.path.join(self.packages_dir, entry))
        ]

        return [(pkg, self._is_package_installed(pkg)) for pkg in packages]

    def _is_package_installed(self, package: str) -> bool:
        """
        Check if a package is installed by looking for its symlinks.

        Args:
            package: Name of the package to check

        Returns:
            True if package is installed, False otherwise
        """
        for directory in self.config_dirs:
            try:
                for entry in os.listdir(directory):
                    entry_path = os.path.join(directory, entry)
                    if os.path.islink(entry_path):
                        link_target = os.readlink(entry_path)
                        if f"packages/{package}" in link_target:
                            return True
            except (FileNotFoundError, PermissionError) as e:
                print(f"Warning: Could not access {directory}: {e}")
        return False

    def update_packages(self, enabled: List[str], disabled: List[str]) -> None:
        """
        Update packages using GNU Stow. Enable and disable packages as specified.

        Args:
            enabled: List of packages to enable
            disabled: List of packages to disable
        """
        os.chdir(self.packages_dir)

        for package in enabled:
            self._run_stow_command(package, install=True)

        for package in disabled:
            self._run_stow_command(package, install=False)

        os.chdir("..")

    def _run_stow_command(self, package: str, install: bool) -> None:
        """
        Run stow command for a package.

        Args:
            package: Package name
            install: True to install, False to uninstall
        """
        action = "enable" if install else "disable"
        cmd = ["stow"] + (["-D"] if not install else []) + \
            [package, "-t", self.home]

        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                print(f"{GREEN}✓{RESET} {action.capitalize()}d: {package}")
            else:
                print(f"{RED}✗{RESET} Failed to {
                      action} {package}: {result.stderr}")
        except subprocess.SubprocessError as e:
            print(f"✗ Error running stow for {package}: {e}")


class TerminalUI:
    @staticmethod
    def get_key() -> str:
        """
        Read a single keypress without requiring Enter.

        Returns:
            The pressed key as a string
        """
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    @staticmethod
    def draw_menu(items: List[Tuple[str, bool]], active: int) -> None:
        """
        Draw the interactive menu.

        Args:
            items: List of (package_name, is_selected) tuples
            active: Index of the currently active item
        """
        print("\033c", end="")  # Clear screen
        print("Select packages to enable/disable\n")

        for i, (item, checked) in enumerate(items):
            prefix = "[*]" if checked else "[ ]"
            cursor = "> " if i == active else "  "
            print(f"{cursor}{prefix} {item}")

        print("\nControls:")
        print("↑/k: Up | ↓/j: Down | Space: Toggle | Enter: Confirm | q: Quit")


class PackageMenu:
    def __init__(self, package_manager: PackageManager):
        """
        Initialize the package menu.

        Args:
            package_manager: Instance of PackageManager to use
        """
        self.package_manager = package_manager
        self.items = package_manager.get_packages()
        self.original_items = self.items[:]
        self.active = 0

    def handle_input(self) -> bool:
        """
        Handle single keypress input.
        Returns: True if should exit menu, False to continue
        """
        key = TerminalUI.get_key()

        if key == "q":
            print("\nExiting...")
            return True

        if key == "\r":  # Enter key
            return True

        if key in ["k", "p", "\x1b[A"]:  # Up
            self.active = (self.active - 1) % len(self.items)

        elif key in ["j", "n", "\x1b[B"]:  # Down
            self.active = (self.active + 1) % len(self.items)

        elif key == " ":  # Space
            self.items[self.active] = (
                self.items[self.active][0],
                not self.items[self.active][1]
            )

        return False

    def display_changes(self, enabled: List[str], disabled: List[str]) -> None:
        """Display selected packages and pending changes."""

        print("\nChanges to apply:")
        if enabled:
            print(f"{GREEN}To enable:{RESET}", ", ".join(enabled))
        if disabled:
            print(f"{RED}To disable:{RESET}", ", ".join(disabled))

    def run(self) -> Tuple[List[str], List[str]]:
        """
        Run the interactive menu loop.
        Returns: Tuple of (enabled_packages, disabled_packages)
        """
        while True:
            TerminalUI.draw_menu(self.items, self.active)
            if self.handle_input():
                break

        return get_changes(self.original_items, self.items)


def get_changes(original: List[Tuple[str, bool]],
                updated: List[Tuple[str, bool]]) -> Tuple[List[str], List[str]]:
    """
    Determine changes between original and updated states.

    Args:
        original: Original package states
        updated: Updated package states

    Returns:
        Tuple of (enabled_packages, disabled_packages)
    """
    enabled = []
    disabled = []

    for (orig_item, orig_state), (updated_item, updated_state) in zip(original, updated):
        if orig_item != updated_item:
            raise ValueError("Package name mismatch between states")

        if not orig_state and updated_state:
            enabled.append(orig_item)
        elif orig_state and not updated_state:
            disabled.append(orig_item)

    return enabled, disabled


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


def main():
    """Main program loop."""
    try:
        package_manager = PackageManager()
        menu = PackageMenu(package_manager)

        # Run menu and get changes
        enabled, disabled = menu.run()

        if not enabled and not disabled:
            print("\nNo changes to apply.")
            return

        # Display and apply changes
        menu.display_changes(enabled, disabled)
        apply_changes(package_manager, enabled, disabled)

    except KeyboardInterrupt:
        print("\nOperation cancelled.")
    except Exception as e:
        print(f"\nError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
