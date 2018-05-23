#!/usr/bin/env python

from __future__ import print_function

import os
import platform
from pynput import keyboard
import logging
import re
import signal
import sys
from threading import Thread

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('nipple')

# config
AUDIO_EXTENSIONS = ['ogg', 'mp3', 'wav', 'opus']
AUDIO_MAC_EXTENSIONS = [extension for extension in AUDIO_EXTENSIONS if extension != 'ogg']
# AUDIO_PYGAME_EXTENSIONS 
AUDIO_FOLDER = '.'

ALL_AUDIO_FILES = []
ALL_MODIFIER_AUDIO_FILES = []

ctrl_pressed = False
shift_pressed = False
current_sound_file = None

force_playsound = len(os.sys.argv) > 1 and os.sys.argv[1] == '--playsound'

# Define if nipple runs on a macOS system
isMac = platform.system() == "Darwin"

try:
    if force_playsound:
        raise ImportError

    import pygame
    use_pygame = True
    logger.info('use pygame for playing sound')
except ImportError:
    try:
        from playsound import playsound, PlaysoundException
        use_pygame = False
        logger.info('use playsound for playing sound')
    except ImportError:
        import os
        if force_playsound:
            print("install playsound, when forcing it, or use pygame")
        else:
            print("install either pygame or playsound (e.g. via pip)")
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
        except (PlaysoundException, IOError):
            logger.debug('no file "%s" found' % sound_file)


def on_press(key):
    global ctrl_pressed
    global shift_pressed
    if key == keyboard.Key.ctrl:
        ctrl_pressed = True
    elif key == keyboard.Key.shift:
        shift_pressed = True
    elif str(key)[:5] == 'Key.f':
        try:
            if ctrl_pressed and shift_pressed:
                sound_file = ALL_MODIFIER_AUDIO_FILES[int(str(key)[5:])]
            elif ctrl_pressed:
                sound_file = ALL_AUDIO_FILES[int(str(key)[5:])]
            else:
                sound_file = None

            if sound_file:
                play(sound_file)
            elif ctrl_pressed:
                logger.debug('sound file not set for key: %s' % str(key))
            
        except IndexError:
            logger.debug('sound file not set for key: %s' % str(key))


def on_release(key):
    global ctrl_pressed
    global shift_pressed
    if key == keyboard.Key.ctrl:
        ctrl_pressed = False
    elif key == keyboard.Key.shift:
        shift_pressed = False


def insert_with_default(default, array, index, item):
    size = len(array)
    if index >= size:
        array.extend(None for _ in range(size, index + 1))
    array[index] = item


def signal_handler(signal, frame):
    sys.exit(0)


def keyboard_listener():
    lis = keyboard.Listener(on_press=on_press, on_release=on_release)
    lis.start()
    lis.join()


def main():
    extensions = AUDIO_MAC_EXTENSIONS if isMac else AUDIO_EXTENSIONS

    for file_ in os.listdir(AUDIO_FOLDER):
        match = re.findall(r'(.*?)_(shift_)?f(.*)\.(.*)', file_)
        if match:
            name, modifier, key, extension = match[0]
            if name == 'nipple' and key and extension in extensions:
                if modifier:
                    insert_with_default('nipple_shift_f%s.ogg', ALL_MODIFIER_AUDIO_FILES, int(key), file_)
                else:
                    insert_with_default('nipple_f%s.ogg', ALL_AUDIO_FILES, int(key), file_)

    if use_pygame:
        pygame.mixer.init()

    # start blocking thread for keyboard listener
    t = Thread(target=keyboard_listener)
    t.setDaemon(True)
    t.start()

    # block main thread for signal handling
    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()


if __name__ == '__main__':
    main()
