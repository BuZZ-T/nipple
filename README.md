# nipple.py

`nipple.py` is a small and easy to use soundboard.
It was developed for Linux, but would probably also work on other operation systems.

The name is a reference to the "Nippelboard" used by Stefan Raab in TV Total.

## Setup

Install the necessary dependencies via *pip*:

##### For using playsound
`sudo pip install -r requirements-playsound.txt`

##### For using pygame mixer
`sudo pip install -r requirements-pygame.txt`

##### Differences between sound libraries

* **[playsound](https://github.com/TaylorSMarks/playsound)** is not able to stop the currently playing sound. So trying to start a sound file, while one is already playing, will queue it and play it after the currently playing sound has stopped. That also means that pressing a shortcut multiple times will play the sound multiple times.
* **[pygame](https://github.com/pygame/pygame)** is a library for 2D game development. So you install much more stuff than you actually need just for playing a sound file. But it is able to pause the currently playing sound on starting a new one. Also initializing pygame needs a notable cpu load in idle when `nipple.py` is running.

So choose your weapon at your taste.

`nipple.py` will try to start *pygame*, if it's not installed, it will fallback to *playsound*. If both are not installed, it will quit with error.
You can enforce using *playsound* when both *playsound* and *pygame* are installed, by starting it with `--playsound`

## Usage

Place your sound files in the same folder as `nipple.py` and name them `nipple<x>.ogg` or `nipple_s<x>.ogg`.
The folder may look like this:
```
├── LICENSE.md
├── nipple.py
├── nipple1.ogg
├── nipple2.ogg
├── nipple3.ogg
├── nipple4.ogg
├── nipple5.ogg
├── nipple6.ogg
├── nipple7.ogg
├── nipple8.ogg
├── nipple9.ogg
├── nipple10.ogg
├── nipple11.ogg
├── nipple12.ogg
├── nipple_s1.ogg
├── nipple_s2.ogg
├── README.md
├── requirements-playsound.txt
└── requirements-pygame.txt
```

After starting just with `python nipple.py`, you can play a sound with **ctrl+f1** to **ctrl+f12** and **ctrl+shift+f1** to **ctrl+stift+f12**

**ctrl+f1** will play `nipple1.ogg`, **ctrl+f2** will play `nipple2.ogg`, etc.
**ctrl+shift+f1** will play `nipple_s1.ogg`, **ctrl+shift+f2** will play `nipple_s2.ogg`, etc.



Be aware that the keyboard event propagation is not stopped when a sound is played. So **ctrl+f5** will reload your website, if your current window is a browser, because your browser will recognize that **f5** was pressed!

## License

This software is licensed under the GPL v3

## TODOs

* Add support for other media types than just OGG Vorbis
* Test on Windows and MacOS
