import os

os.system('cls')

from colorama import init, Fore, Style
import time

init(autoreset=True)

text = "Đang vào tool"
for char in text:
    print(f"{Fore.WHITE}{Style.BRIGHT}{char}{Style.RESET_ALL}", end="", flush=True)
    time.sleep(0.05)
print()

time.sleep(2)

print(Style.RESET_ALL)

# Phần còn lại của code
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
import requests
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
time=datetime.now().strftime("%H:%M:%S")
import socket
from pystyle import *
#import màu
luc = "\033[1;32m"
trang = "\033[1;37m"
do = "\033[1;31m"
vang = "\033[0;93m"
hong = "\033[1;35m"
xduong = "\033[1;34m"
xnhac = "\033[1;36m"
red='\u001b[31;1m'
yellow='\u001b[33;1m'
green='\u001b[32;1m'
blue='\u001b[34;1m'
tim='\033[1;35m'
xanhlam='\033[1;36m'
xam='\033[1;30m'
black='\033[1;19m'
#today nand clear
data_machine = []
today = date.today()
os.system('clear')
#daystime
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
def get_ip_from_url(url):
    response = requests.get(url)
    ip_address = socket.gethostbyname(response.text.strip())
    return ip_address
url = "http://kiemtraip.com/raw.php"
ip = get_ip_from_url(url)
dr = " \033[1;97m[\033[1;31m+_+\033[1;97m] => "
def logo():
    os.system("cls" if os.name == "nt" else "clear")
    logo=f"""
Tool Buff Like Bằng Pro5
"""
    print(logo)
#=======================[ NHẬP KEY ]=======================
os.system("cls" if os.name == "nt" else "clear")
logo()

import threading
import requests
from pystyle import *
import time
import sys
import ssl
import random
from http import cookiejar
from urllib3.exceptions import InsecureRequestWarning
import time
import os
import datetime
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context


class BlockCookies(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False
    
class Main:
    def __init__(self, __file_name, __post):
        self.__success = 0
        self.__errors = 0
        self.rqs = 0
        self.rpm = 0
        self.rps = 0
        self.rqs = 0
        self.__post = __post
        self.__client = requests.Session()
        self.__client.cookies.set_policy(BlockCookies())
        try:
            self._file = open(__file_name).read().split('\n')
            self.total = str(len(self._file))
            print(f' [*] Total Token: {self.total}')
            sleep(3)
        except:
            sys.exit((f' [+] No Such File "{__file_name}"                                                                        '))
    def title(self, start):
        while True:
            curr_time = str(
                datetime.timedelta(
                    seconds = (
                        time.time() 
                        - start
                    )
                )
            ).split(".")[0]
            os.system(f'title Total: {str(len(self._file))} ^| Elapsed Time: {curr_time} ^| Success: {self.__success} ^| Fail: {self.__errors} ^| Cpm: {self.rpm} ^| Thread_Count: {threading.active_count()} ^| v2.1')
            time.sleep(0.5)
    
    def random_ico(self, length):
        icon = '🌁🌉🌌🌃🌆🌇🏙🎆🎇🌠🎑🌄🌅🏜🏞🌋🗻🏔⛰🗾⛺🏕🏝🏖🌼🌸🌺🏵️🌻🌷🌹🥀💐🌾🎋☘🍀🍃🍂🍁🌱🌿🎍🌵🌴🌳🌳🎄🍄🌜🌚❄🌪🌊☂️💦🌈🌩️🌥️⛅'
        result_ico = ''.join(random.choice(icon) for i in range(length))
        return result_ico

    def likes(self, token):
        __start = time.time()
        link = 'https://graph.facebook.com/'+self.__post+'/likes'
        data = {
                'access_token': token,
                }
        response = self.__client.post(link, data=data, verify=False, stream=False, allow_redirects=False).json()
        self.rqs += 1
        if True == response:
            print(f" [+] Likes! [{response}] [Execution: {round(time.time() - __start, 1)}s]")
            self.__success += 1
            time.sleep(0.05)
        else:
            self.__errors += 1
    def __share(self, token):
        self.likes(token)
        try:
            get_ = requests.get('https://graph.facebook.com/me/accounts?access_token='+token, verify=False, stream=False, allow_redirects=False).json()['data']
            for access in get_:
                tok = access['access_token']
                self.likes(tok)
        except:
             self.__errors += 1
    def rpsm_loop(self):
        while True:
            initial = self.rqs
            time.sleep(1.5)
            rps = round((self.rqs - initial) / 1.5, 1)
            self.rpm = round(rps * 60, 1)
    def start(self):
        threading.Thread(
                target = self.rpsm_loop, 
            ).start()
        threading.Thread(
                target = self.title, 
                daemon = True,
                args=[time.time()]
            ).start()
        for token in self._file:
            threading.Thread(target=self.__share, args=[token]).start()
            while threading.active_count() > 1000:
                pass
def run():
    __file = input("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Flie Đứa Token: \033[1;32m")
    __post = input("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập ID Bài Viết: \033[1;32m")
    Main(__file, __post).start()

if '__main__' == __name__:
    run()