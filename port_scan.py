#!/bin/python
import subprocess,os
import sys

print('[*]Example: $ port_scan.py target_ip target_port')

args = sys.argv
ip = args[1]
port = args[2]
ports = list()

for i in range(0, int(port), 2000):
    print(i)
    ports.append(i)

last_port = int(port) - i + int(ports[-1])
ports.append(last_port)

"""
for i in range(1, len(ports)):
    command = str('nmap -sV -sC -A -p- ' +  str(ports[i-1]) + '-' + str(ports[i]) + ' ' + str(ip))
    os.system(command) 
"""