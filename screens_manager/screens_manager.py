#!/usr/bin/env python

""" Display Manager."""

import os
# import time
import subprocess

DISPLAYS = [
    {
        "name": "eDP-1",
        "options": "auto",
        "pos": "0x0"
    },
    {
        "name": "DP-2-1",
        "options": "auto",
        "pos": "1920x0"
    },
    {
        "name": "DP-2-2",
        "options": "auto",
        "pos": "3840x0"
    },
    {
        "name": "HDMI-1",
        "options": "auto",
        "pos": "3840x0"
    },
    {
        "name": "HDMI-2",
        "options": "auto",
        "pos": "1920x0"
    },
]

def get_connected_screens():
    """Get the list of connected screens."""
    connected_screens = []
    cmd1 = ["xrandr|grep connected|grep -v disconnected"]
    proc = subprocess.Popen(
        cmd1,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )

    for line in proc.stdout.readlines():
        if line:
            connected_screens.append(line)

    return connected_screens

def get_configured_screens():
    """Get the list of configured screens."""
    configured_screens = []
    for screen in get_connected_screens():
        if "1920" in screen:
            configured_screens.append(screen)

    return configured_screens

#while True:
CMD_OPTIONS = ""
# If there's more screens connected than configured :
if len(get_connected_screens()) > len(get_configured_screens()):
    CONNSCREEN = [] # List of connected screens
    for s in get_connected_screens():
        screen_name = s.split(' ')[0]
        CONNSCREEN.append(s)
        for dis in DISPLAYS:
            if screen_name == dis["name"]:
                print "configuring: " + dis["name"]
                #if dis not in get_configured_screens():
                CMD_OPTIONS += " --output " + dis["name"]
                CMD_OPTIONS += " --" + dis["options"]
                CMD_OPTIONS += " --pos " + dis["pos"] + " "

    os.system("xrandr" + CMD_OPTIONS)
    #time.sleep(5)
