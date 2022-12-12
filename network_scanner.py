#!/usr/bin/env python

import scapy.all as scapy
import optparse


def get_arguments():
    # OptionParser(): Class
    parser = optparse.OptionParser()
    parser.add_option("-i", "--ip", dest="ip", help="Scan IP address range. eg. 192.168.1.1/24")
    # parse_args : method
    return parser.parse_args()

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    # scapy.srp get 2 lists, using scapy.srp()[0] to get the first list, with is answered_list
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose= False)[0]


    clients_list = []
    for element in answered_list:
        client_dict = {"ip" : element[1].psrc, "mac" : element[1].hwsrc}
        clients_list.append(client_dict)
        # print(element[1].show()) to find the psrc, hwsrc
    return clients_list


def print_result(results_list):
    print("IP\t\t\tMAC Address\n--------------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])

(options, arguments) = get_arguments()
scan_result = scan(options.ip)
print_result(scan_result)
