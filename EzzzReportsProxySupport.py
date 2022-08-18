import time
from datetime import datetime
from colorama import *
import requests
from requests.sessions import session


print(Fore.RED + '''
███████╗███████╗███████╗███████╗██████╗░███████╗██████╗░░█████╗░██████╗░████████╗░██████╗░░░░█████╗░░█████╗░
██╔════╝╚════██║╚════██║╚════██║██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝░░░██╔══██╗██╔══██╗
█████╗░░░░███╔═╝░░███╔═╝░░███╔═╝██████╔╝█████╗░░██████╔╝██║░░██║██████╔╝░░░██║░░░╚█████╗░░░░██║░░╚═╝██║░░╚═╝
██╔══╝░░██╔══╝░░██╔══╝░░██╔══╝░░██╔══██╗██╔══╝░░██╔═══╝░██║░░██║██╔══██╗░░░██║░░░░╚═══██╗░░░██║░░██╗██║░░██╗
███████╗███████╗███████╗███████╗██║░░██║███████╗██║░░░░░╚█████╔╝██║░░██║░░░██║░░░██████╔╝██╗╚█████╔╝╚█████╔╝
╚══════╝╚══════╝╚══════╝╚══════╝╚═╝░░╚═╝╚══════╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░╚═╝░╚════╝░░╚════╝░
''')




tiktok_url = input("Enter tiktok report request url: ")

while True:

    proxies = requests.get(url="https://advanced.name/freeproxy/62fe15ee3ed95").text.split('\r\n')

    for proxy in proxies:

        try:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")

            req = session().post(tiktok_url, proxies={'http': f'http://{proxy}'})

            print(Fore.RED + f'[{current_time}]' + Fore.WHITE + f' Proxy: {proxy} Sent report')
        except:
            print('no worky :( ')
            input('Press Enter to close the program')
            exit()
