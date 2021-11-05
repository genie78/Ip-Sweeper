#!/usr/bin/env python3
import subprocess
ip = subprocess.check_output("hostname -i | grep 192.168 | cut -d ' ' -f 1", shell=True)
ipv4 = ip.decode('ascii', 'ignore')
print(f"Your ip : {ipv4}")
n = 0
ip_check = ""
for i in ipv4:
    if n == 3:
        break 
    if i == ".":
        n += 1 
    ip_check += i
    
for i in range(1,255):
    subprocess.call(f'ping -c 1 {ip_check}{i} | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &',shell=True)
