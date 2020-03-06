#!/usr/bin/python
#coding: utf-8
import os
from colorama import init, Fore, Style
from threading import Thread
import time, requests, json

#Color script
init(autoreset=True)
HEADER = Fore.LIGHTMAGENTA_EX
OKBLUE = Fore.LIGHTBLUE_EX
GREEN = Fore.LIGHTGREEN_EX
WARNING = Fore.LIGHTYELLOW_EX

def banner():
    print('{}         -----------------------------------  '.format(WARNING))
    print('       {1}-=[   {0}IP Country Check Multi-Thread {1}]=-'.format(GREEN, WARNING))
    print('       {1}-=[   {0}Contact FB: Rahman Gunawan{1}    ]=-'.format(GREEN, WARNING))
    print('       {1}-=[   {0}Created by Rahman Gunawan{1}     ]=-'.format(GREEN, WARNING))
    print('       {1}-=[        {0}Version : 3.1{1}            ]=-'.format(GREEN, WARNING))
    print('         {}-----------------------------------  '.format(WARNING))
    print('')

def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])

def main():
    def tryproxies(ip):
        with open('live.txt', 'a+') as livedetectcountry:
            try:
                response = requests.get('https://4stars.wtf/country.php?ip='+ip, headers= {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',})
                test = response.text
                resultx = json.loads(response.text)
                colorized = resultx['error']
                if colorized == 0:
                    result = json.loads(test)
                    countryCode = result['country_code']
                    countryName = result['country_name']
                    print("Country Code :",Style.BRIGHT+Fore.GREEN+countryCode,"- Country Name :",Style.BRIGHT+Fore.LIGHTYELLOW_EX+countryName,"- IP Address :",Style.BRIGHT+Fore.LIGHTCYAN_EX+ip)
                    livedetectcountry.write("Country Code :"+countryCode+"- Country Name :"+countryName+"- IP Address :"+ip+"\n")
            except Exception as e:
                print(e, ip, "Waktu berlalu: %s" % (time.time() - start))

    start = time.time()
    threadlist = []
    with open(input('[!] ENTER YOUR PROXIES PATH: '), 'r') as file:
        for ip in file:
            ip = ip.replace("\n", "")
            #ip = ip.strip()
            t = Thread(target=tryproxies, args=(ip,))
            t.start()
            threadlist.append(t)

# ---------------------------------- ## ---------------------------------- ## ---------------------------------- #

if __name__ == '__main__':
    cls()
    banner()
    main()
