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
import os
import random
import threading
import requests
from pystyle import *
import time
import sys
import datetime
import socket
from cmath import rect
import datetime,base64
from time import sleep
import threading,sys
from urllib.parse import *
from time import strftime
import requests,os
from time import sleep
import hashlib
import time
class MainSHare:
    os.system('clear')
    def __init__(self):
            self.blue = Col.light_gray
            self.lblue = Col.light_gray
            self.red = Col.light_gray
            try:
                self.open_file = open('token.txt').read().split('\n')
                self.open_file.remove('')
                self.total = str(len(self.open_file))
            except:
                quit(self.format_print("$", 'No Such File "token.txt"'))
    def format_print(self, symbol, text):
            return f"""{Col.Symbol(symbol, self.lblue, self.blue)} {self.lblue}{text}{Col.reset}"""
    def format_input(self, symbol, text):
            return f"""{Col.Symbol(symbol, self.red, self.blue)} {self.red}{text}{Col.reset}"""
    def banner(self):
            os.system("cls" if os.name == "nt" else "clear")
            title = '\n\n Vũ Văn Chiến - Zalo: 0862317026\n'
            banner = '\n\n Lưu ý mua token mới có thể chạy share\n'
            print(Colorate.Vertical((Col.light_gray), Center.XCenter(title+'Token: '+self.total)) + Colorate.Vertical((Col.light_gray), Center.XCenter(banner)))
            if self.total == '0':
                quit(self.format_print("@", " Token Number Not Enough!"))
    def share(self, id_post, token):
            rq = random.choice([requests.get, requests.post])
            dt_now = datetime.datetime.now()
            response = rq(f'https://graph.facebook.com/me/feed?method=POST&link=https://m.facebook.com/{id_post}&published=0&access_token={token}').json()
            if "id" in response:
                print({f"{response['id']}"}, " Thành Công - HAV Tool")
            else:
                print(f"Block Rồi !")
    def run_share(self):
            while True:
                main.banner()
                try:
                    id_post = input(f"ID Cần Tăng Share: ")
                    threa = int(input(f"Ae Để Delay Này Tương Ứng Với Số Lượng Token Có Nhé !: "))
                    if id_post != '' and threa > 0:
                        break
                    else:
                        print("THREAD > 0!")
                        time.sleep(3)
                except:
                    print("THREAD INT!")
                    time.sleep(3)
            while True:
                for token in self.open_file:
                    t = threading.Thread(target=self.share, args=(id_post, token))
                    t.start()
                    while threading.active_count() > threa:
                        t.join()
if __name__ == "__main__":
    try:
        main = MainSHare()
        main.run_share()
    except KeyboardInterrupt:
        time.sleep(3)
        sys.exit("bye")