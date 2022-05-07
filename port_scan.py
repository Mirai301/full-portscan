#!/usr/bin/env python
import sys
import nmap

print('[*]Usage: $ port_scan.py 192.168.xx.xx 10000')

args = sys.argv
ip = str(args[1])
port = args[2]
ports = list()

for i in range(0, int(port), 2000):
    ports.append(i)

last_port = int(port) - i + int(ports[-1])
ports.append(last_port)

for i in range(1, len(ports)):
    port_ = str(str(ports[i-1]) + '-' + str(ports[i]))
    print('scan_port: 'port_)
    nm = nmap.PortScanner()
    nm.scan(ip, port_, '-sV -sC -A')
    print(nm.command_line())

    for host in nm.all_hosts():
        print('----------------------------------------------------')
        print('Host : %s (%s)' % (host, nm[host].hostname()))
        print('State : %s' % nm[host].state())
        for proto in nm[host].all_protocols():
            print('----------')
            print('Protocol : %s' % proto)

            lport = nm[host][proto].keys()
            sorted(lport)
            for port in lport:
                print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
        print('----------------------------------------------------', end="\n")