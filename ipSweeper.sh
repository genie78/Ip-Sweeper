#!/bin/bash 
ip="hostname -i | grep 192.168 | cut -d ' ' -f 1  "
echo "Your ip address: "$(eval "$ip")
mip=$(eval "$ip | cut -f 3 -d '.' ")
gop="192.168.$mip"

for i in `seq 1 254` ; do
	ping -c 1 $gop.$i | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
	sleep 0.1
done
