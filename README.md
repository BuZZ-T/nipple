# nipple.py

`nipple.py` is a small and easy to use soundboard.
It was developed for Linux, but also works on other operation systems.

The name is a reference to the "Nippelboard" used by Stefan Raab in TV Total.

## Setup

Install the necessary dependencies via *pip*:

##### For using playsound
`sudo pip install -r requirements-playsound.txt`

##### For using pygame mixer
`sudo pip install -r requirements-pygame.txt`

##### Differences between sound libraries

* **[playsound](https://github.com/TaylorSMarks/playsound)** is not able to stop the currently playing sound. So trying to start a sound file, while one is already playing, will queue it and play it after the currently playing sound has stopped. That also means that pressing a shortcut multiple times will play the sound multiple times. Playsound on macOS does not support playing *.ogg files.
* **[pygame](https://github.com/pygame/pygame)** is a library for 2D game development. So you install much more stuff than you actually need just for playing a sound file. But it is able to pause the currently playing sound on starting a new one. Also initializing pygame needs a notable cpu load in idle when `nipple.py` is running and the start of the playing has a little delay.

So choose your weapon at your taste.

`nipple.py` will try to start *pygame*, if it's not installed, it will fallback to *playsound*. If both are not installed, it will quit with error.
You can enforce using *playsound* when both *playsound* and *pygame* are installed, by starting it with `--playsound`.

## Usage

Place your sound files in folder described in the variable `AUDIO_FOLDER` at the beginning of `nipple.py`, by default it's the folder where `nipple.py` is placed. Name them `nipple_<fn_key>.<extension>` or `nipple_shift_<fn_key>.<extension>`.

`<fn_key>` can be a function key from *F1* to *F12*.

Currently supported file extensions are:

* .mp3
* .ogg (not on macOS, as playsound does not support it)
* wav
* opus (not when using pygame, as it does not support it)

Not supported audio formats are filtered and not added to the internal audio file list!

The folder may look like this:
```
├── LICENSE.md
├── nipple.py
├── nipple_f1.ogg
├── nipple_f2.ogg
├── nipple_f3.ogg
├── nipple_f4.ogg
├── nipple_f5.ogg
├── nipple_f6.wav
├── nipple_f7.ogg
├── nipple_f8.ogg
├── nipple_f9.ogg
├── nipple_f10.mp3
├── nipple_f11.ogg
├── nipple_f12.ogg
├── nipple_shift_f1.ogg
├── nipple_shift_f2.opus
├── README.md
├── requirements-playsound.txt
└── requirements-pygame.txt
```


After starting just with `python nipple.py`, you can play a sound with **ctrl+f1** to **ctrl+f12** and **ctrl+shift+f1** to **ctrl+stift+f12**

**ctrl+f1** will play `nipple_f1.<extension>`, **ctrl+f2** will play `nipple_f2.<extension>`, etc.
**ctrl+shift+f1** will play `nipple_shift_f1.<extension>`, **ctrl+shift+f2** will play `nipple_shift_f2.<extension>`, etc.

**BE AWARE:**
* ** When placing multiple files with the same function key, `os.listdir` decides which of them is chosen. No error or warning will be placed in this case!**
* If you add new sound files, you have to restart `nipple.py`, as it only checks the sound files at the start.


Be aware that the keyboard event propagation is not stopped when a sound is played. So **ctrl+f5** will reload your website, if your current window is a browser, because your browser will recognize that **f5** was pressed!

## Audio format support

### pygame

*pygame* has no support for opus at the moment. So use *playsound* for opus files or convert them to a supported audio format. (only tested on linux...)

### macOS 
*(tested with 10.13.1 - High Sierra)*

* MacOS restricts monitoring the keyboard for security reasons. Therefore you must run nipple as root. `sudo nipple.py`
* Playing *.ogg files is not supported for playsound in macOS. When using `nipple.py` use another file format.
* MacOS, as a default uses the F-Keys for special functions. Please note that you might need to change this default behavior or also press the fn-key.

## License

This software is licensed under the GPL v3

## TODOs

* Check support for opus files, currently only Linux is tested!
* Test pygame / playsound on Windows
* Add (cross-platform) `pyinotify` to update the internal audio file list when audio files are added without the need to restart `nipple.py`.
