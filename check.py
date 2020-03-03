# /lib/usr/python3
import requests, json
from colorama import init, Fore, Style
import threading
init(autoreset=True)
#Color script
HEADER = Fore.LIGHTMAGENTA_EX
OKBLUE = Fore.LIGHTBLUE_EX
GREEN = Fore.LIGHTGREEN_EX
WARNING = Fore.LIGHTYELLOW_EX
# INT
lives = 0
deads = 0
no = 0
#Threading
lock = threading.Lock()

def header():
    print('{}         -----------------------------------  '.format(WARNING))
    print('       {1}-=[     {0}IP Country Check{1}            ]=-'.format(GREEN, WARNING))
    print('       {1}-=[   {0}Contact FB: Rahman Gunawan{1}    ]=-'.format(GREEN, WARNING))
    print('       {1}-=[   {0}Created by Rahman Gunawan{1}     ]=-'.format(GREEN, WARNING))
    print('       {1}-=[        {0}Version : 3.0{1}            ]=-'.format(GREEN, WARNING))
    print('         {}-----------------------------------  '.format(WARNING))
    print('')
def main():
    global lives
    global deads
    global no
    listyour = input("Input Your list.TXT : ")
    mail_list = open(listyour,'r')
    livedetectcountry = open('live.txt', 'w+')
    count_mailist = len(open(listyour).readlines())
    for ips in mail_list:
        ip = ips.replace("\n", "")
        response = requests.get('https://4stars.wtf/country.php?ip='+ip, headers= {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',})
        test = response.text
        resultx = json.loads(response.text)
        colorized = resultx['error']
        if colorized == 0:
            lock.acquire()
            result = json.loads(test)
            countryCode = result['country_code']
            countryName = result['country_name']
            no+=1
            lives+=1
            print("[",no,"/"+str(count_mailist)+"]","Country Code :",Style.BRIGHT+Fore.GREEN+countryCode,"- Country Name :",Style.BRIGHT+Fore.LIGHTYELLOW_EX+countryName,"- IP Address :",Style.BRIGHT+Fore.LIGHTCYAN_EX+ip)
            lock.release()
            livedetectcountry.write("Country Code :"+countryCode+"- Country Name :"+countryName+"- IP Address :"+ip+"\n")
        elif colorized == 2:
            lock.acquire()
            print("[",no,"/"+str(count_mailist)+"]","DEAD - "+ip)
            lock.release()

if __name__ == "__main__":
    header()
    t=threading.Thread(target=main)
    t.start()
