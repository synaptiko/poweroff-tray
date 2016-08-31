#!/usr/bin/env python3
import os
from pystray import Icon, Menu, MenuItem
from subprocess import call, DEVNULL
from PIL import Image, ImageDraw

rootDir = os.path.dirname(os.path.realpath(__file__))

image = Image.open(os.path.join(rootDir, 'icon.png'))
image.load()

def onPowerOff(icon):
    call([os.path.join(rootDir, 'power-off.sh')], stdout=DEVNULL, stderr=DEVNULL, cwd=rootDir)

def onRestart(icon):
    call([os.path.join(rootDir, 'restart.sh')], stdout=DEVNULL, stderr=DEVNULL, cwd=rootDir)

menu = Menu(
        MenuItem('Power Off', onPowerOff, True),
        MenuItem('Restart', onRestart))
icon = Icon(name='poweroff-tray', title='Power Off/Restart', icon=image, menu=menu)

def setup(icon):
    icon.visible = True

icon.run(setup)
