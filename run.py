#!/usr/bin/env python3
from pystray import Icon, Menu, MenuItem
from subprocess import call, DEVNULL
from PIL import Image, ImageDraw

image = Image.open('./icon.png')
image.load()

def onPowerOff(icon):
    call(['./power-off.sh'], stdout=DEVNULL, stderr=DEVNULL)

def onRestart(icon):
    call(['./restart.sh'], stdout=DEVNULL, stderr=DEVNULL)

menu = Menu(
        MenuItem('Power Off', onPowerOff, True),
        MenuItem('Restart', onRestart))
icon = Icon(name='poweroff-tray', title='Power Off/Restart', icon=image, menu=menu)

def setup(icon):
    icon.visible = True

icon.run(setup)
