#!/usr/bin/env python


import subprocess

# Assigning variables for my interface
interface = 'eth0'
new_mac = '00:AA:11:BB:22:CC'

print(f'Changing the mac address {interface} to new_mac')

subprocess.call(f'sudo ifconfig {interface} down', shell=True)
subprocess.call(f'sudo ifconfig eth0 hw ether {new_mac}' ,shell=True)
subprocess.call(f'sudo ifconfig {interface} up', shell=True)

