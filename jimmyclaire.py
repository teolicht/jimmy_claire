#! /usr/bin/env python3

import random
import time
import sys
import os
from playsound import playsound
from colored import fg, attr
from colors import *


# path to sounds folder
sounds = "/Users/teodor/Desktop/Python/Jimmy_Claire/sounds/"

# different variations of 'yes'
yes = ['y', 'yes', 'ya', 'ye', 'sure', 'yeah', 'yea', 'yep', 'yup',
       'yas', 'you bet', 'totally', 'yaa', 'yaaa', 'ok', 'k', 'yh']

# different variations of 'no'
no = ['n', 'no', 'nah', 'nope', 'na', 'never', 'nay', 'no way', 'negative']

inputl = fg(grey_70) + "> " + fg(white)


def invalid(a):
    """Print the invalid message"""
    print(attr(1) + fg(red) + "Invalid:" + attr(0) + fg(white), a)


def start():
    """The game start menu"""
    print("1. {} 'start' {}: {}Start the game.".format(fg(green), fg(white), fg(cyan)))
    print("{}2. {}  'exit' {}: {}Exit the program.".format(
        fg(white), fg(green), fg(white), fg(cyan)))

    while True:
        next = input(inputl).lower()

        if next in [1, 'start', 'init', 'initiate', 'begin']:
            first_level()

        elif next in [2, 'exit', 'leave', 'stop', 'cancel']:
            sys.exit(0)

        else:
            invalid(next)
            time.sleep(0.5)


def playAgain():
    """A confirmation in case the user wants to play again after game end / game over"""
    print("Do you want to play again? Y/N")

    while True:
        next = input(inputl).lower()

        if next in yes:
            start()

        elif next in no:
            print(fg(light_green) + "Thanks for playing!")
            sys.exit(0)

        else:
            invalid(next)
            time.sleep(0.5)


start()
