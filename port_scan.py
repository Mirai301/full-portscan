#!/usr/bin/env python
import sys
from unittest import skip
import nmap

try:
    args = sys.argv
    ip = str(args[1])
    port = args[2]
    ports = list()
except:
    print('[*]Usage: $ port_scan.py 192.168.xx.xx 10000', end="\n\n")

def port_split(port):
    for i in range(0, int(port), 2000):
        ports.append(i)

    last_port = int(port) - i + int(ports[-1])
    ports.append(last_port)
    return ports

def main(port):
    ports = port_split(port)
    print('scan_port: 1-' + str(port))
    for i in range(1, len(ports)):
        port_num = str(str(ports[i-1]) + '-' + str(ports[i]))
        
        nm = nmap.PortScanner()
        nm.scan(ip, port_num, '-sV -sC -A')

        if i == 1:
            # print(nm.command_line())
            print('----------------------------------------------------')
        else:
            next

        for host in nm.all_hosts():
            for proto in nm[host].all_protocols():
                lport = nm[host][proto].keys()
                sorted(lport)
                for port in lport:
                    print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))

main(port)