# Notes

This are my notes for certain activities/fixes or whatever I do in my linux hoping it helps someone else.

Im looking forward to turn this into a blog or something so people can find solutions/fixes for the same problems I had.

## Table of Contents

- [Electron apps not running with ozone flags](#electron-apps-not-running-with-ozone-flags)

### Electron apps not running with ozone flags

Im running one of my monitors at 1.5x scaling and the other at 1x scaling, this causes electron apps to not run properly, usually the solution is to run the app with the following flags:

```bash
app --enable-features=UseOzonePlatform --ozone-platform=wayland
```

But since I use `wofi` as my application launcher, I had to modify the `.desktop` file for the app to run with the flags.

Example for [vesktop](https://github.com/Vencord/Vesktop):

```bash
sudo nvim /usr/share/applications/vesktop.desktop 
```

And modify the `Exec` line to:

```bash
Exec=/usr/bin/vesktop --enable-features=UseOzonePlatform --ozone-platform=wayland
```

If not works at first sight make sure that you indeed closed Vesktop instead of just minimizing it, you can just log out and log back in to be completely sure.

