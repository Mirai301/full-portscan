#!/usr/bin/env python3
import sys
import math
import nmap

def tcp_port_scan(target, port_range):
    nm = nmap.PortScanner()
    nm.scan(target, port_range, '-Pn -sV -sC -A')
    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()
            sorted(lport)
            for port in lport:
                if nm[host][proto][port]['state'] == 'open':
                    print(f'\r## {port} : {nm[host][proto][port]["state"]}')

def udp_port_scan(target, port_range):
    nm = nmap.PortScanner()
    nm.scan(target, port_range, '-sU -sV -sC -A')
    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()
            sorted(lport)
            for port in lport:
                if nm[host][proto][port]['state'] == 'open':
                    print(f'\r## {port} : {nm[host][proto][port]["state"]}')

def prompt_message(message):
    while True:
        response = input(message)
        if response.lower() in ['yes', 'y']:
            return True
        elif response.lower() in ['no', 'n']:
            return False
        else:
            print('Invalid input. Please enter yes or no.')

def main():
    assert len(sys.argv) >= 2, '[*]Usage: $ python3 full_nmap.py <target>'

    args = sys.argv
    ip = str(args[1])
    port_range = 65535
    chunk_size = 2000
    num_chunks = math.ceil(port_range / chunk_size)

    # tcp scan
    print('[*] Scanning TCP ports...')
    for i in range(num_chunks):
        start = i * chunk_size
        end = (i + 1) * chunk_size if (i + 1) * chunk_size <= port_range else port_range
        
        # print(f'[*] Scanning ports {start}-{end}') # debug

        tcp_port_scan(ip, f'{start}-{end}')
    print('[*] Finished scanning TCP ports')

    # udp scan
    if prompt_message('Do you want to scan for UDP ports?'):
        print('[*] Scanning UDP ports...')
        for i in range(num_chunks):
            start = i * chunk_size
            end = (i + 1) * chunk_size if (i + 1) * chunk_size <= port_range else port_range
            udp_port_scan(ip, f'{start}-{end}')
        print('[*] Finished scanning UDP ports')

if __name__ == "__main__":
    main()