#!/usr/bin/env python

import subprocess

# Variables for interface as Eth0
# Variables for the new MAC address
interface = "eth0"
new_mac="00:11:22:33:44:77"

print("[+] Change MAC address for " + interface + " to " + new_mac)

# ifconfig command
subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + "  hw ether " + new_mac + "00:11:22:33:44:66", shell=True)
subprocess.call("ifconfig " + interface + "  up", shell=True)
