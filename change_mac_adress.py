#!/usr/bin/env python


import subprocess

# Assigning variables for my interface
interface = input('Enter the interface name: ')

new_mac = input('Enter the new mac-address: ')

print(f'Changing the mac address {interface} to new_mac')

subprocess.call(['sudo','ifconfig', interface, 'down'])
subprocess.call(['sudo', 'ifconfig', interface, 'hw', 'ether', new_mac])
subprocess.call(['sudo', 'ifconfig', interface, 'up'])

print(f'The Changed MAC-Address is -->')
val = subprocess.call(['sudo', 'ifconfig'])
print(val)

