# nipple.py

`nipple.py` is a small script providing a soundboard.
It was developed for Linux, but would probably also work on other operation systems.

## Setup

Install the necessary dependencies via *pip*:

`sudo pip install -r requirements.txt`

## Usage

After starting just with `python nipple.py`, you can play a sound with **ctrl+f1** to **ctrl+f10**.  
**ctrl+f1** will play `nipple1.ogg`, **ctrl+f2** will play `nipple2.ogg`, etc.
## TODOs

* Switch from `playsound` to `pygame` as `playsound` can't pause a playing track.
* Add other sound types and check for files
* Test on Windows and MacOS