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
import requests

proxies = []

# Get proxies from raw text files
raw_proxy_sites = ["https://api.proxyscrape.com/?request=displayproxies&proxytype=http",
                   "https://api.openproxylist.xyz/http.txt",
                   "https://openproxylist.xyz/http.txt",
                   "http://alexa.lr2b.com/proxylist.txt",
                   "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
                   "https://proxy-spider.com/api/proxies.example.txt",
                   "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
                   "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",
                   "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt",
                   "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt",
                   "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt",
                   "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
                   "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
                   "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
                   "https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
                   "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
                   "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
                   "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
                   "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt",
                   "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/https.txt",
                   "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
                   "https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
                   "http://worm.rip/http.txt",
                   "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/http.txt",
                   "http://rootjazz.com/proxies/proxies.txt",
                   "https://api.proxyscrape.com/?request=displayproxies&proxytype=https",
                   "https://www.proxy-list.download/api/v1/get?type=http",
                   "https://www.proxy-list.download/api/v1/get?type=https",
                   "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
                   "https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt",
                   "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
                   "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
                   "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
                   "https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt",
                   "https://multiproxy.org/txt_all/proxy.txt",
                   "https://proxyspace.pro/http.txt",
                   "https://proxyspace.pro/https.txt",
                   "https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
                   "https://raw.githubusercontent.com/aslisk/proxyhttps/main/https.txt",
                   "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/HTTP.txt",
                   "https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt",
                   "https://raw.githubusercontent.com/saisuiu/uiu/main/free.txt",
                   "https://rootjazz.com/proxies/proxies.txt",
                   "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
                   "https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/main/free.txt",
                   "https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/main/cnfree.txt",
                   "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt",
                   "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies_anonymous/http.txt",
                   "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/http.txt",
                   "https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt",
                   "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt",]

for site in raw_proxy_sites:
    response = requests.get(site)
    for line in response.text.split('\n'):
        if ':' in line:
            ip, port = line.split(':', maxsplit=2)[:2]
            proxies.append(f'{ip}:{port}')

proxy_count = 500000
with open('proxy.txt', 'w') as f:
    for proxy in proxies:
        f.write(proxy + '\n')
        print("Đã Lưu Vào File proxy.txt")
        print("HAV Tool")
