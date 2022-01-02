from colorama import Fore, Back
from os import system
import os
import requests , uuid , time 
import sys
import json
import random
from bs4 import BeautifulSoup
from re import sub
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
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
			'cache-control': 'max - age = 0',
			'sec-ch-ua': '"Google Chrome";v = "89", "Chromium";v = "89", ";Not A Brand";v = "99"',
			'sec-ch-ua-mobile': '?0',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'none',
			'sec-fetch-user': '?1',
			'upgrade-insecure-requests': '1',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36'}
        res = requests.get(url,headers=headers)
        soup = BeautifulSoup(res.content, 'html.parser')
        name = soup.find(class_="tiktok-qpyus6-H1ShareSubTitle e198b7gd6")
        print(Fore.WHITE)
        #print(res.text)
        names = str(name)
        names = names.replace('<h1 class="tiktok-qpyus6-H1ShareSubTitle e198b7gd6" data-e2e="user-subtitle">', '').replace('</h1>', '')
        print(Fore.LIGHTMAGENTA_EX + 'profile name: ' + Fore.WHITE + names)
        if res.status_code == 200:
            tit = random.choice(titles)
            system("title " + tit)
            print(Fore.WHITE + "[" + Fore.MAGENTA + "+" + Fore.WHITE + "]" + Fore.MAGENTA + user.strip())
            scraped = open('scraped.txt', 'a', encoding="utf-8")
            scraped.write(names + '\n')
        elif res.status_code == 404:
            tit = random.choice(titles)
            system("title " + tit)
            print(Fore.MAGENTA + 'User Banned/Doesn´t exist')
        elif res.status_code == 403:
            system("title " + tit)
            print(Fore.WHITE + "[" + Fore.RED + f'-' + Fore.WHITE + "] " + Fore.RED + 'IP BLOCKED!')
        else:
            tit = random.choice(titles)
            system("title " + tit)
            print (Fore.RED + 'Something went wrong')