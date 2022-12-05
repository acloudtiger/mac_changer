#!/usr/bin/env python

import subprocess

# Input for Variables (2.7 using raw_input command , 3.X using input command)
# Variables for interface as Eth0
# Variables for the new MAC address

# interface = input("Interface > ")
# new_mac= input("New MAC > ")

interface = raw_input("Interface > ")
new_mac= raw_input("New MAC > ")

print("[+] Change MAC address for " + interface + " to " + new_mac)

# ifconfig command
# subprocess.call("ifconfig " + interface + " down", shell=True)
# subprocess.call("ifconfig " + interface + "  hw ether " + new_mac + "00:11:22:33:44:66", shell=True)
# subprocess.call("ifconfig " + interface + "  up", shell=True)

# using another method for security issue, eg eth0;ls; for input
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw",  "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
