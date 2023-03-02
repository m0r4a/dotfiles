# dotfiles
🇲🇽  [ Versión en español](/README_es.md)

These are the dotfiles for my Arch Linux

# Table of Contents

- [Arch Installation](#arch-installation)
- [Packages](#packages)
  - [With custom config](#with-custom-config)
  - [Without custom config](#without-custom-config)
- [Basic sys utils](#basic-sys-utils)
- [BlackArch repo](#blackarch-repo)
- [Window managers](#window-managers)
  - [Qtile](#qtile)
- [Configs in detail](#configs-in-detail)


## Arch Installation

### This installation is very likely to not work for you, so just ignore this part of the readme.

```bash
timedatectl set-ntp true
```

#### Creation and formatting of the partition

_being:_

_sda1: EFI partition_

_sda2: root partition_

_sda3: home partiton_

_sda4: swap partiton_

```bash
cfdisk
mkfs.ext4 /dev/sda2
mkfs.ext4 /dev/sda3
mkswap /dev/sda4
swapon /dev/sda4
```

#### Mounting partitons

```bash
mount /dev/sda2 /mnt
mkdir /mnt/home
mount /dev/sda3 /mnt/home
mkdir /mnt/boot
mount /dev/sda1 /mnt/boot
```

#### Installaton of the system

```bash
pacstrap /mnt base linux-lts linux-lts-headers linux-firmware intel-ucode neovim
genfstab -U /mnt >> /mnt/etc/fstab
```

#### Setting up the sytem 

```bash
arch-chroot /mnt
ln -sf /usr/share/zoneinfo/America/Monterrey /etc/localtime
hwclock --systohc
nvim /etc/locale.gen	# Uncomment en_US.UFT-8 UTF-8 & es_MX.UTF-8 UTF-8
locale-gen
echo "LANG=en_US.UTF-8" > /etc/locale.conf
echo "KEYMAP=us" > /etc/vconsole.conf
echo "Arch" > /etc/hostname
```

```bash
nvim /etc/hosts

127.0.0.1	localhost
::1		localhost
127.0.1.1	Arch.localhost Arch
```

``` bash
passwd
```

#### Install the bare minimum 

_Note: this are the bare minimum till "xorg"_

```bash
pacman -Sy efibootmgr networkmanager grub base-devel git bluez bluez-utils pulseaudio pulseaudio-bluetooth alsa-utils xorg qtile lightdm lightdm-gtk-greeter alacritty picom firefox
```

#### Grub install

```bash
grub-install --target=x86_64-efi --efi-directory=/boot
grub-mkconfig -o /boot/grub/grub.cfg
```

#### Enabe system services 

```bash
systemctl enable NetworkManger
systemctl enable bluetooth
systemctl enable lightdm
systemctl start sshd
```

#### User configuration & sudo configuration

``` bash
useradd -m m0r4a
passwd m0r4a
usermod -aG wheel,audio,video,storage m0r4a
chmod u+w /etc/sudoers
nvim /etc/sudoers
84j	and uncomment: %wheel ALL=(ALL:ALL) ALL
chmod u-w /etc/sudoers
```

#### Final steps

``` bash
exit
umount -R /mnt
shutdown now
```

#### My stuff

``` bash
sudo pacman -S code pavucontrol obsidian arandr neofetch scrot brightnessctl imv feh xcalib bat lsd unzip python-pip lightdm-webkit2-greeter openssh xdg-utils libnotify dunst lxappearance qt5ct
```

_With yay_

```bash
yay -S  notification-daemon 
```

_With cargo_

cargo install toipe

## Packages

### With custom config

#### GUI
| Application |       Use         | Source |
|:-----------:|      :----:       | :---: |
| [qtile](http://docs.qtile.org/en/stable/ "Qtile docs") | Window manager | Pacman | 
|[alacritty](https://github.com/alacritty/alacritty "Alacritty's Github page") | Terminal emulator (vanilla)| Pacman |
|[VSCode (code)](https://code.visualstudio.com/docs "VSCode docs") | code editor | AUR |
| [lightdm](https://wiki.archlinux.org/title/LightDM "LightDM's arch entry") | login manager | Pacman |
| obsidian | note-taking app | AUR |
| neovim | text editor | Pacman |
| rofi | launcher |
| spectacle | screenshot utility |
| ly | Display Manager |



#### Terminal based
| Application |       Use         |
|:-----------:|      :----:       |
| [ picom ](https://wiki.archlinux.org/title/picom "Picom's Arch entry") | compositor |
| lightdm-gtk-greeter | default cfg for lightdm |
| lightdm-webkit2-greeter | thing for theming lightdm |
| [ yay ](https://github.com/Jguer/yay "Yay's GitHub repo") | package installer for the AUR |
| [neofetch ](https://github.com/dylanaraps/neofetch/wiki "Neofetch's wiki") | displays system info
| zsh | new shell intepreter
| oh-my-zsh | better zsh |
| starship | prompt editor |
| dunst | Notification manager? |

### Without custom config

#### GUI

| Application |       Use         |
|:-----------:|      :----:       |
| firefox |  web browser |
| pavucontrol | sound manager |
| discord | self expl. |
| arandr | Graphical Screen Manager |
| simplescreenrecorder | Records Screen |
| eww | Wacky widgets |
| bitwarden | Password manager |
| todoist | Todo-list app |
| lxappearance | Changing system theme |
| qt5ct | Same that lxappearance |
| Apostrophe | MD editor |



#### Terminal based

| Application |       Use         |
|:-----------:|      :----:       |
| htop | ram? viewer |
| lsd | a better ls |
| bat | a better cat |
| unzip | self exp. |
| python-pip | library installer for python |
| feh | wallpaper manager |
| scrot | utility for taking screenshots |
| xcalib | icc manager |
| brightnessctl | self explanatory |
| imv | image preview tool |
| papirus-icon-theme | self exp. |
| rustup | compiler for rust |
| snap | package installer |
| xdg-utils | manage XDG MIME apps |
| toipe | typing test |


### Installed programming lang.

- Rust
  - rustup
- Go


## BlackArch repo

### A little guide about how to install the blackarch repo

- Install curl (if not installed)

``` bash
sudo pacman -S curl
```

- Download the setup script using:

``` bash
curl -O https://blackarch.org/strap.sh
```

- Give execution privileges and run it with sudo:

``` bash
chmod +x strap.sh
sudo ./strap.sh
rm strap.sh
```

#### List everything from the repo

``` bash
pacman -Sgg | grep blackarch | cut -d ' ' -f2 | sort -u
```

#### List all blackarch categories

``` bash
pacman -Sg | grep blackarch | sed 's/blackarch-/ /'
```

#### Install a whole category

``` bash
sudo pacman -S blackarch-category
```

## Window managers

### Qtile
##### Apps used in the config file:

_Note: before you copy the qtile config make sure you have **alacritty** installed_

Install the hack nerd font from [here](https://www.nerdfonts.com/font-downloads), unzip it and move it to: /usr/share/fonts



*Note: If you use a different terminal, change it in ~/.config/qtile/settings/keys.py on `my_terminal = alacritty`*

##### Pip dependencies 

```bash
pip install psutil dbus-next
```

# Configs in detail

- [Neovim](#neovim)
- [Obsidian](#obsidian)
- [Zsh](#zsh)
- [LightDM](#lightdm)
- [Eww](#eww)
- [Yay](#yay)
- [Git](#git)

## Neovim

_Note: install xsel for nvim_ 

## Obsidian 



## Zsh

### OhMyZsh's Plugins

#### Default

- git
- archlinux
- command-not-found
- rust

#### Custom 

- zsh-syntax-highlighting
- zsh-autosuggestions


### Starship, prompt editor
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin faucibus felis nulla, quis bibendum nulla varius ut. Morbi ligula tellus, tincidunt sed vulputate eget, hendrerit in ex. 

## Eww

### Install guide

1. Install rustup

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

2. Clone eww github's repo

```bash
git clone https://github.com/elkowar/eww
```

```bash
cd eww
```

3. Build it

```bash
cargo build --release
```

Build for wayland:

```bash
cargo build --release --no-default-features --features=wayland
```

## Yay

### Short install guide 

``` bash
cd /opt
sudo git clone https://aur.archlinux.org/yay-git.git
sudo chown -R yourUser:yourUser ./yay-git
cd yay-git
makepkg -si
```

## Git

### Set up git with: 

``` bash
git config --global user.email "you@example.com"  
```

```bash
git config --global user.name "Your Name"
```

``` bash
git config --global init.defaultBranch <name>
```

## Todoist

### You have to have configured a default desktop, here's little guide about how to do it on Arch

#### Install xdg-utils

```bash
sudo pacman -S xdg-utils
```

#### Run this commands _(if you use something else than firefox, change it)_

```bash
xdg-mime query default x-scheme-handler/http
firefox
xdg-settings get default-web-browser
firefox
```
