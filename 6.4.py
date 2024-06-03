#!/usr/bin/python3
import os,  time, requests, sys, threading
from colorama import init, Fore
CheckVersion = str(sys.version)

init()
RED = Fore.RED
GREEN = Fore.GREEN
BLUE = Fore.BLUE
YELLOW = Fore.YELLOW
ORANGE = Fore.CYAN
RESET = Fore.RESET

def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux,windows][os.name == 'nt'])

cls()

def Logo():
    from colorama import init, Fore
    import sys, random, time
    init()
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """
   
    ─┼─┼─╔═╗╦═╗╔═╗═╗ ╦╦ ╦  ╔═╗╔═╗╔═╗╔╗╔╔╗╔╔═╗╦═╗─┼─┼─
    ─┼─┼─╠═╝╠╦╝║ ║╔╩╦╝╚╦╝  ╚═╗║  ╠═╣║║║║║║║╣ ╠╦╝─┼─┼─
         ╩  ╩╚═╚═╝╩ ╚═ ╩   ╚═╝╚═╝╩ ╩╝╚╝╝╚╝╚═╝╩╚═     
                      HAV Tool      
    """
    for N, line in enumerate(x.split("\n")):
         sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
         time.sleep(0.05)

Logo()
def xx(PROXY, url):
    try:
        sess = requests.session()
        sess.proxies = {'http': PROXY}
        sess.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                                      ' (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        aa = sess.get(url, timeout=5, proxies={'http': PROXY})
        if aa.status_code == 200:
            print (f'{YELLOW} {PROXY}' + f' {GREEN}Live{RESET}')
            with open('proxylive.txt', 'a') as xX:
                xX.write(PROXY + '\n')
        else:
            print (f"{ORANGE}{PROXY}" + f' {RED}Mala{RESET}')
    except:
        print (f'{ORANGE} {PROXY}' + f' {RED}Mala{RESET}')


def main():
    try:
        if '3.' in CheckVersion:
            try:
                fileproxy = input("  Nhập file .txt chứa proxy ~# ")
            except:
                print('  [-] Error : Enter Your Proxy!')
                sys.exit()
        elif '2.' in CheckVersion:
            try:
                fileproxy = raw_input("  Nhập file .txt chứa proxy ~# ")
            except:
                print('  [-] Error : Enter Your Proxy!')
                sys.exit()
        else:
            print(' Unknown Python Version!')
    except:
        pass
        sys.exit()
    with open(fileproxy, 'r') as x:
        prox = x.read().splitlines()
    thread = []
    for proxy in prox:
        t = threading.Thread(target=xx, args=(proxy, 'https://instagram.com'))
        t.start()
        thread.append(t)
        time.sleep(0.1)
    for j in thread:
        j.join()

main()