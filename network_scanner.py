#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    # scapy.ls(scapy.ARP())
    arp_request.show()

    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # scapy.ls(broadcast)
    broadcast.show()

    arp_request_broadcast = broadcast/arp_request
    arp_request_broadcast.show()




scan("192.168.154.2/24")
