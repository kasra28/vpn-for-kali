#!/usr/bin/python3
from os import system as s
from time import sleep as sp

s("clear")

class bcolors:
    CYAN = '\033[96m'
    PURPLE = '\033[95m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

print(bcolors.BOLD + "script write by <kasra akhavan> iranian hacker")
sp(1)
print(bcolors.YELLOW + "kasraakhavan401@gmail.com")
sp(1)
print(bcolors.RED + "this python code requires openvpn on your terminal and script tested on kali linux")
sp(1)
print(bcolors.DARKCYAN + "if you dont have openvpn install you can just type on your terminal sudo apt install openvpn")
sp(2)
print(bcolors.CYAN +'''
Username: vpnbook
Password: e7x76mc
source is https://www.vpnbook.com/freevpn
''')
sp(2)
menu = input(bcolors.GREEN + '''
please enter which vpn did you want to use
1)vpn for download ----> get blockd by google most off the time
2)usa vpn ----> get blockd by google most off the time
3)frence vpn -----> better than other but not good for download stufe
<box>: ''')

if menu == '1':
    choose = input(bcolors.BLUE + "which server do you want to use:\n1)vpnbook-pl226-tcp80\n2)vpnbook-pl226-tcp443\n3)vpnbook-pl226-udp53\n4)vpnbook-pl226-udp25000\n<box>: ")
    if choose == '1':
        s("sudo openvpn vpn1/vpnbook-pl226-tcp80.ovpn")
    elif choose == '2':
        s("sudo openvpn vpn1/vpnbook-pl226-tcp443.ovpn")
    elif choose == '3':
        s("sudo openvpn vpn1/vpnbook-pl226-udp53.ovpn")
    elif choose == '4':
        s("sudo openvpn vpn1/vpnbook-pl226-udp25000.ovpn")
    else:
        exit()
elif menu == '2':
    choose = input(bcolors.BLUE + "which server do you want to use:\n1)vpnbook-us1-tcp80\n2)vpnbook-us1-tcp443\n3)vpnbook-us1-udp53\n4)vpnbook-us1-udp25000\n<box>: ")
    if choose == '1':
        s("sudo openvpn vpn2/vpnbook-us1-tcp80.ovpn")
    elif choose == '2':
        s("sudo openvpn vpn2/vpnbook-us1-tcp443.ovpn")
    elif choose == '3':
        s("sudo openvpn vpn2/vpnbook-us1-udp53.ovpn")
    elif choose == '4':
        s("sudo openvpn vpn2/vpnbook-us1-udp25000.ovpn")
    else:
        exit()
elif menu == '3':
    choose = input(bcolors.BLUE + "which server do you want to use:\n1)vpnbook-fr1-tcp80\n2)vpnbook-fr1-udp53\n3)vpnbook-fr1-udp25000\n<box>: ")
    if choose == '1':
        s("sudo openvpn vpn3/vpnbook-fr1-tcp80.ovpn")
    elif choose == '2':
        s("sudo openvpn vpn3/vpnbook-fr1-udp53.ovpn")
    elif choose == '3':
        s("sudo openvpn vpn3/vpnbook-fr1-udp25000.ovpn")
    else:
        exit()
else:
    print("some thing is wrong")
