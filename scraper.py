from colorama import Fore, Back
from os import system
import os
import requests , uuid , time 
import sys
import json
import random
from bs4 import BeautifulSoup

#checking if your python isn´t 2
if sys.version_info[0] < 3:
	pyversion = python_version()
	print("Alert! Your python version is %s. Use python version 3> to run this code" %(pyversion))
	exit(1)

os.system('cls||clear')
print(Back.BLACK + Fore.MAGENTA + '              zeeeeee-\n            z$$$$$$"\n           d$$$$$$"\n          d$$$$$P\n         d$$$$$P\n        $$$$$$"\n      .$$$$$$"\n     .$$$$$$"\n    4$$$$$$$$$$$$$"\n   z$$$$$$$$$$$$$"\n   """""""3$$$$$"\n         z$$$$P\n        d$$$$"\n      .$$$$$"\n     z$$$$$"\n    z$$$$P\n   d$$$$$$$$$$"\n  *******$$$"\n       .$$$"\n      .$$"\n     4$P"\n    z$"\n   zP\n  z"')
print('')
print('')
print(Fore.CYAN + '          TikTok Name Scraper by yin/who?')
print('')
print('')
print(Fore.LIGHTMAGENTA_EX +'Input File Name')
print('')
print('')
fil = input(Fore.MAGENTA+" root" + Fore.WHITE+"@" + Fore.LIGHTMAGENTA_EX +"yin" + Fore.WHITE+":" + Fore.CYAN+"~" + Fore.WHITE+" ")



while True:
    titles = ["y1n", "yin","yinsec", "t.me/undecryptable", "discord.gg/m922xF9", "gang"]
    tit = random.choice(titles)
    system("title " + tit)
    file = open(fil, 'r')
    for user in file:
        url="https://www.tiktok.com/@" + user.strip()
        headers = {
            'user-agent': 'any',
            'cookie': 'GET YOUR OWN COOKIE FROM YOUR BROWSER'}
        res = requests.get(url,headers=headers)
        soup = BeautifulSoup(res.content, 'html.parser')
        name = soup.find(class_="profile")
        print(Fore.WHITE)
        print(name)
        if res.status_code == 200:
            tit = random.choice(titles)
            system("title " + tit)
            print(Fore.WHITE + "[" + Fore.MAGENTA + "+" + Fore.WHITE + "]" + Fore.MAGENTA + user.strip())
        elif res.status_code == 404:
            tit = random.choice(titles)
            system("title " + tit)
            print(Fore.MAGENTA + 'User Banned/Doesn´t exist')
        else:
            tit = random.choice(titles)
            system("title " + tit)
            print (Fore.RED + 'DEAD IP')
