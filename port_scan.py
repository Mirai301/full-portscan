#!/usr/bin/env python3
import sys
from unittest import skip
import nmap

assert len(sys.argv) >= 3, '[*]Usage: $ port_scan.py 192.168.xx.xx 10000'

args = sys.argv
ip = str(args[1])
port = args[2]
# port-number check
assert 65535 >= int(port), "[*]Error: max port-number is 65535 !!"

ports = list()

# port-number-split
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
print(end="\n")
anser = input('Scan udp-port?(need a sudo privileges!!): ')
if anser in 'y':
    print('scan-port: udp-ports')
    print('----------------------------------------------------')
    nm = nmap.PortScanner()
    nm.scan(ip, '-sU -sV -sC -A')
    for host in nm.all_hosts():
            for proto in nm[host].all_protocols():
                lport = nm[host][proto].keys()
                sorted(lport)
                for port in lport:
                    print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
else:
    exit(0)