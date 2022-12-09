#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    # scapy.ls(scapy.ARP()) to check pdst is for ip address
    print(arp_request.summary())



scan("192.168.154.2/24")
