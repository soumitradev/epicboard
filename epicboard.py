#!/usr/bin/env python3
import subprocess
import json
import os
import keyboard
import pyautogui
import time

prefix = "/;"

k = {}

with open("./emotes.json", "r") as f:
    k = json.load(f)


def rep(short, path):
    pyautogui.typewrite(['backspace'] * (len(short) + len(prefix) + 3))

    cur_clip = str(subprocess.run(["xclip", "-o"], capture_output=True).stdout, encoding='utf-8')

    copy_image = "xclip -selection clipboard -t image/png -i " + path
    process = subprocess.run(copy_image.split())

    pyautogui.hotkey('ctrl', 'v')

    time.sleep(0.1)

    ps = subprocess.Popen(('echo', f'{cur_clip}'), stdout=subprocess.PIPE)
    output = subprocess.check_output(('xclip', '-selection', 'clipboard'), stdin=ps.stdout)
    ps.wait()


for shortcut, path in k.items():
    keyboard.add_word_listener(
        prefix + shortcut, lambda: rep(shortcut, path), timeout=30)

keyboard.wait()
