What it is?
===========
Simple utility which I'm using in i3wm to quickly powering off or restarting my computer… It will place icon into system tray area. This icon will have two action on right-click: *Power Off* and *Restart*. Left click will call *Power Off* which is default action.

Dependencies
============
- `python3`
- [`pystray`](https://github.com/moses-palmer/pystray)
- [`zenity`](https://library.gnome.org/users/zenity/stable/)
- `bash`

How to install it?
==================
Clone this repo and run `pip install -r requirements.txt` inside it.

How to use it?
==============
Add the following into your i3 config file (e.g. `~/.config/i3/config`):
```
exec --no-startup-id /home/xy/SomeStuff/poweroff-tray/run.py >& /dev/null &
```

You'll also need something like this in your `suders.d` file:
```
user machine= NOPASSWD: /usr/bin/shutdown now, /usr/bin/reboot, /usr/bin/systemctl hibernate, /usr/bin/systemctl suspend
```
