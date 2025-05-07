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


red = ("\033[1;31;40m")
green = ("\033[1;32;40m")
white = ("\033[1;37;40m")
blue = ("\033[1;34;40m")

os.system("clear")

def CurrentDir():
	path = os.getcwd()
	print(green + "[" + white + "+" + green + "]" + white + " Your Templates Will Be Saved Here " + path + '/"TemplateName.html"')


def mainMenu():
	menu()

	print(green)
	
	CurrentDir()
	
	mailPick = int(input(green + "root@phishmailer:~ " + white))

	try:

            if mailPick == 1:
                    Instagram()

            elif mailPick == 2:
                    Facebook()

            elif mailPick == 3:
                    Gmail()

            elif mailPick == 4:
                    Linkedin()

            elif mailPick == 5:
                    Spotify()

mainMenu()
