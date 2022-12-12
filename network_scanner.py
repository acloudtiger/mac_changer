#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    # scapy.srp get 2 lists, using scapy.srp()[0] to get the first list, with is answered_list
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose= False)[0]

    print("IP\t\t\tMAC Address\n--------------------------------------------")
    clients_list = []
    for element in answered_list:
        client_dict = {"ip" : element[1].psrc, "mac" : element[1].hwsrc}
        clients_list.append(client_dict)
        # print(element[1].show()) to find the psrc, hwsrc
        print(element[1].psrc + "\t\t" + element[1].hwsrc)
    print(clients_list)


scan("192.168.154.2/24")
