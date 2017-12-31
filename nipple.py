#!/usr/bin/env python

from playsound import playsound, PlaysoundException
from pynput import keyboard

ctrl_pressed = False


def on_press(key):
    global ctrl_pressed
    if key == keyboard.Key.ctrl:
        ctrl_pressed = True

    try:
        if ctrl_pressed:
            if key == keyboard.Key.f1:
                playsound('nipple1.ogg')
            if key == keyboard.Key.f2:
                playsound('nipple2.ogg')
            if key == keyboard.Key.f3:
                playsound('nipple3.ogg')
            if key == keyboard.Key.f4:
                playsound('nipple4.ogg')
            if key == keyboard.Key.f5:
                playsound('nipple5.ogg')
            if key == keyboard.Key.f6:
                playsound('nipple6.ogg')
            if key == keyboard.Key.f7:
                playsound('nipple7.ogg')
            if key == keyboard.Key.f8:
                playsound('nipple8.ogg')
            if key == keyboard.Key.f9:
                playsound('nipple9.ogg')
            if key == keyboard.Key.f10:
                playsound('nipple10.ogg')
    except PlaysoundException:
        pass


def on_release(key):
    global ctrl_pressed
    if key == keyboard.Key.ctrl:
        ctrl_pressed = False

def main():
    lis = keyboard.Listener(on_press=on_press, on_release=on_release)
    lis.start() # start to listen on a separate thread
    lis.join() # no this if main thread is polling self.keys

if __name__ == '__main__':
    main()
