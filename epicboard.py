#!/usr/bin/env python3
import subprocess
import json
import os
import keyboard
import pyautogui

prefix = "/;"

k = {}

with open("./emotes.json", "r") as f:
    k = json.load(f)

def rep(short, path):
    for i in range(len(short) + len(prefix) + 1):
        pyautogui.typewrite(['backspace'])

    copy_image = "xclip -selection clipboard -t image/png -i " + path
    process = subprocess.run(copy_image.split())
    pyautogui.hotkey('ctrl', 'v')

for shortcut, path in k.items():
    keyboard.add_word_listener(prefix + shortcut , lambda: rep(shortcut, path), timeout=30)

keyboard.wait()