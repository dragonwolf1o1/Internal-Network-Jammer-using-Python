# Internal-Network-Jammer-using-Python


## Details:
* This tool is based on networking.
* This is written in Python Language.
* Only the Jamming part works in the Windows operating system not the sniffing part but both Jamming and sniffing work in the Linux operating system.
* The recommended version of Python is ```Python3```.
* The motive to create this tool is that 'many people don't have Wi-Fi adapters so they can't perform deauth on any wifi network but this tool provides stability'.
* A new feature is provided from time to time in this tool, so please follow and check.

## Working:

### Jamming:
* The attacker enters the victim's IP address and MAC address to send the ARP packets.
* This tool sends multiple ARP packets so the router's ARP table changes therefore victim does not access the internet.

### Sniffing:
* In the case of sniffing we use ```sysctl -w net.ipv4.ip_forward=1``` this command to sniff.
* This above command is forwarded victim's network over the internet via your system.
* Attacker is the mediator between the victim and the router so you can see all packets coming through the victim.
* You use multiple applications to see the packet but I recommended ```Wireshark``.

## Instruction
* You see the victim's IP & MAC address using ```arp -a``` command.
* If the above command is not working then you use ```Nmap```, ```arp-scan```, ```netdiscover```
* The users who are connected to your network.

## Installation:

```
git clone https://github.com/dragonwolf1o1/Internal-Network-Jammer-using-Python.git

pip3 install requirements.txt

python3 main.py

```

### Enjoy this tool
