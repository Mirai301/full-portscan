#! /bin/bash
echo "[*]Usage: $ port_scan.sh 192.168.xx.xx 10000"
ip=$1
port=$2

# command
command="$(which nc) -vz $ip 1-$port 2>&1 | grep succeeded"
echo $command
# exec
eval $command

echo \

# udp-port-scan
read -n1 -p "Do you want to perform a udp port scan?(y/n): " yn
if [[ $yn = [yY] ]]; then
    # command
    command="$(which nc) -uvz $ip 1-$port 2>&1 | grep succeeded"
    # exec
    eval $command
else
    exit
fi