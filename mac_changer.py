#!/usr/bin/env python
import subprocess
import optparse


# Rewrite by using function to change mac
def change_mac(interface, new_mac):
    print("[+] Change MAC address for " + interface + " to " + new_mac)
    # using another method for security issue, eg eth0;ls; for input
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


# OptionParser(): Class
parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")

# parse_args : method
(options, arguments) = parser.parse_args()

change_mac(options.interface, options.new_mac)
