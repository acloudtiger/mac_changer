#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    # scapy.srp get 2 lists, using scapy.srp()[0] to get the first list, with is answered_list
    answered_list = scapy.srp(arp_request_broadcast, timeout=1)[0]
    for element in answered_list:
        # print(element[1].show()) to find the psrc, hwsrc
        print(element[1].psrc)
        print(element[1].hwsrc)
        print("--------------------------------------------")


scan("192.168.154.2/24")
