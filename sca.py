import os   #identifies where the OS python libraries
import scapy.all as scapy   #Imports the scapy library for creating a python script
  
arpreq = scapy.ARP()    
arpreq.pdst = '192.168.1.1/24'

arpbrod = scapy.Ether()
arpbrod.dst = 'ff:ff:ff:ff:ff:ff'
  
arpreq_arpbrod = arpbrod / arpreq
clients = scapy.srp(arpreq_arpbrod, timeout = 1)[0]
for element in clients:
    print(element[1].psrc + "      " + element[1].hwsrc)