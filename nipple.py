#!/usr/bin/env python

import os
from pynput import keyboard
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('nipple')

ctrl_pressed = False
shift_pressed = False
current_sound_file = None

force_playsound = len(os.sys.argv) > 1 and os.sys.argv[1] == '--playsound'

try:
    if force_playsound:
        raise ImportError

    import pygame
    use_pygame = True
    pygame.mixer.init()
    logger.info('use pygame for playing sound')
except ImportError:
    try:
        from playsound import playsound, PlaysoundException
        use_pygame = False
        logger.info('use playsound for playing sound')
    except ImportError:
        import os
        if force_playsound:
            print "install playsound, when forcing it, or use pygame"
        else: 
            print "install either pygame or playsound (e.g. via pip)"
        os.sys.exit(1)


def play(sound_file):
    if use_pygame:
        try:
            global current_sound_file
            pygame.mixer.music.stop()
            if not sound_file is current_sound_file:
                current_sound_file = sound_file
                pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
        except pygame.error:
            logger.debug('no file "%s" found' % sound_file)
    else:
        try:
            playsound(sound_file)
        except PlaysoundException:
            logger.debug('no file "%s" found' % sound_file)


def on_press(key):
    global ctrl_pressed
    global shift_pressed
    if key == keyboard.Key.ctrl:
        ctrl_pressed = True
    elif key == keyboard.Key.shift:
        shift_pressed = True
    elif str(key)[:5] == 'Key.f':
        if ctrl_pressed and shift_pressed:
            play('nipple_shift_%s.ogg' % str(key)[4:])
        elif ctrl_pressed:
            play('nipple_%s.ogg' % str(key)[4:])


def on_release(key):
    global ctrl_pressed
    global shift_pressed
    if key == keyboard.Key.ctrl:
        ctrl_pressed = False
    elif key == keyboard.Key.shift:
        shift_pressed = False

def main():
    lis = keyboard.Listener(on_press=on_press, on_release=on_release)
    lis.start()
    lis.join()

if __name__ == '__main__':
    main()
