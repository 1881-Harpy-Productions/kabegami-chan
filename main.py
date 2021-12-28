from os import name, path, walk, system
import ctypes
import random
import time
from sys import argv
import config as var

verbosity = 0
# sanitizing path to convert \ to /
impath = var.path.replace("\\", "/")
slideshow = False  # slideshow mode
argNum = len(argv)  # number of arguments for finding out arguments given
imageList = list()  # list of all images found to folder with the images to be used as wallpaper
pathSet = False
timerSet = False


def verbose(msg: str, warn: bool, level: int):
    if warn and verbosity:
        print(f"\033[93m{msg}\033[0m")
    elif verbosity >= level:
        print(msg)


def findpos(string: str):
    """
    Find in what position the argument is
    :param string: the argument string to search for
    :return:
    """
    position = int(-1)
    for pos in range(len(argv)):
        verbose(f"current argument number:{pos} = {argv[pos]}", False, 2)
        if string == argv[pos]:
            verbose(f"found string", False, 2)
            position = pos
    return position


def setwallpaper():
    """
    sets the wallpaper
    :return:
    """
    wallpaper = random.choice(imageList)
    verbose(f"Wallpaper = {wallpaper}", False, 1)
    if path.exists(wallpaper):
        if name == "nt":
            ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper, 3)
        elif name == "posix":
            system(f"feh --bg-fill -rz {wallpaper}")
    else:
        verbose("Warning: File no longer exists.", True, 1)


def slideshowloop():
    """
    endless loop where the wallpaper is change every set amount of time
    :return:
    """
    while True:
        verbose("Starting Slideshow", False, 1)
        setwallpaper()
        time.sleep(var.timer)


# handling arguments
if "-t" in argv or "--timer" in argv:
    pos = findpos("-t")
    if findpos("--timer") >= pos:
        pos = findpos("--timer")
    try:
        var.timer = int(argv[pos + 1])
        verbose(f"Timer set to {argv[pos + 1]}", False, 1)
    except:
        exit("Error: Time set incorrectly.")
    timerSet = True
    if var.timer >= 1:
        slideshow = True

if "-p" in argv or "--path" in argv:
    pos = findpos("-p")
    if findpos("--path") >= pos:
        pos = findpos("--path")
    verbose(f"path set to {argv[pos + 1]}", False, 1)
    impath = str(argv[pos + 1])
    pathSet = True

# interactive set path
if not pathSet:
    string = str(input(f"Input a path: (leave blank for default path: {impath})\n:"))
    if string:
        verbose("path manualy set", False, 1)
        impath = string
    else:
        verbose("using deafult path", False, 1)

# interactive set slideshow and timer
if not timerSet:
    var.timer = int(input("Set a timer for slideshow: (0 to disable slideshow mode)\n:"))
    if var.timer == 0:
        slideshow = False
    else:
        slideshow = True

# checking if path exists
if not path.exists(impath):
    exit("Error: path to files does not exist")

# Get the list of all files in directory tree at given path
for (dirpath, dirnames, filenames) in walk(impath):
    imageList += [path.join(dirpath, file) for file in filenames]
verbose(f"images found:\n{imageList}", False, 2)

# making sure only jpg and png are in the list
for file in imageList:
    if ".png" not in file or ".jpg" not in file:
        imageList.remove(file)

# makes sure there is any image left in the path
if len(imageList) == 0:
    exit("Error: no images to load")

verbose(f"images found:\n{imageList}", False, 2)
verbose(f"Number of Arguments {argNum}", False, 2)
verbose(f"Arguments given:\n----\n {argv} \n----End of arguments", False, 2)

if slideshow:
    verbose(f"slide show mode is on: {slideshow}", False, 1)
    slideshowloop()
else:
    setwallpaper()
