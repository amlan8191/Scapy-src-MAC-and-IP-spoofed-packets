from scapy.all import *

MAC=input("Enter MAC address to be spoofed: ")
src_IP=input("Enter source IP: ")
dst_IP=input("Enter destination IP: ")
payload=input("Enter payload: ")

pckt=Ether(src=MAC)/IP(src=src_IP,dst=dst_IP)/ICMP()/payload

sendp(pckt,iface="eth0")
