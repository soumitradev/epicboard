# Epicboard
## What?
It's a program that runs in the background on Linux (This was tested on Ubuntu 20.04 LTS), and replaces specific text with a prefix with images of your choice. It's like a custom emoji keyboard if you will.

## Installation
### Requirements
Python 3 and some other modules. Install requirements using `sudo pip3 install -r requirements.txt`. Make sure you have xclip too! `sudo apt install xclip`

### How can I start using this?
Run `xhost +` to allow the script to connect to your Xserver, and then run `nohup sudo python3 ./epicboard.py &` (Use python3) after installing requirements.

You can add your emote images to the `emotes` folder, and add the path to the `emotes.json` file along with the text that triggers it. There is also a `prefix` variable in `epicboard.py` that specifies the prefix that is needed to trigger the program. The default prefix is `/;`. A default emote is available if you want to test it. It can be activated after running the script and then typing `/;bored` and then a space after that. It directly pastes the emote as an image.

**Note:** For some reason, pyautogui doesnt recognize uppercase characters, so the emote names and prefix are confined to lowercase chars.

### Stopping the script
You can find the process id(s) by running:
```ps ax | grep epicboard.py```

Then, to kill it, run:
```sudo kill -9 <process id>```

### Troubleshooting
If you get some error with Xserver like this:
`Xlib.error.DisplayConnectionError: Can't connect to display ":0": b'No protocol specified\n'`
just run:
`xhost +`

## Why?
I really wanted to customize my emojis on Desktop (esp. on WhatsApp Web), so I made this.

## The Code is bad
I'm trying my best. If you really hate it that bad, just create an Issue or Pull Request.

## You're collecting my data!
No. The code is open source, and is like 26 lines lmao just read through it. No keyboard data is stored.

## License
[MIT License](./LICENSE)
