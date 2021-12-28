# Kabegami-chan


Personal project I made while learning python, just sharing if someone want to use it.\
I think this will be usefull because windows slideshow wallpaper only picks from the root folder and not its subfolders.\
Selects images randomly from a folder and its subfolders, and set it as wallpaper.\
It can be timed to change it periodically or change just change it once.\
It will also works on posix systems
---
# Requirements

- Windows. needs python installed
- Posix. needs feh. python probably is already installed.
---

# Wallpaper manager.

  - just run the main.py file
  - create a shortcut, put somewhere you can easily double click it
  - add a keyboard shortcut so you can change wallpaper with a single click
  - edit the config file with the path to your wallpaper folder and timer for slideshow
---
# Command line arguments

  - -p or --path "path/to/folder" folder where the images to be used as wallpapers are located.
  - -t or --timer X a number in seconds it will wait that ammount of seconds before changing wallpaper.
  - if you do not fill these when runing this script it will prompt you to fill it anyway.
---