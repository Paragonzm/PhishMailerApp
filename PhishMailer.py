import time
import os
import sys
import json
import requests
from sys import version_info

from Core.eletter import Instagram
from Core.eletter import Facebook
from Core.eletter import Gmail
from Core.eletter import Spotify
from Core.devicemenu import Linkedin

# Color codes
red = "\033[1;31;40m"
green = "\033[1;32;40m"
white = "\033[1;37;40m"
blue = "\033[1;34;40m"

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def CurrentDir():
    path = os.getcwd()
    print(green + "[" + white + "+" + green + "]" + white +
          " Your Templates Will Be Saved Here: " + path + '/"TemplateName.html"')

def get_user_choice():
    print(green + "[1] Instagram\n[2] Facebook\n[3] Gmail\n[4] Linkedin\n[5] Spotify")
    try:
        return int(input(green + "root@phishmailer:~ " + white))
    except ValueError:
        print(red + "Please enter a valid number.")
        return None

def run_selected_module(choice):
    modules = {
        1: Instagram,
        2: Facebook,
        3: Gmail,
        4: Linkedin,
        5: Spotify
    }
    action = modules.get(choice)
    if action:
        action()
    else:
        print(red + "Invalid option selected.")

def mainMenu():
    clear_screen()
    CurrentDir()
    choice = get_user_choice()
    if choice:
        run_selected_module(choice)

if __name__ == "__main__":
    mainMenu()

