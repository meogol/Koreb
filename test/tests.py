#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy


def print_and_accept(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    # print("pkg:" + str(scapy_packet.show()))
    print(packet)
    packet.drop()
 

nfqueue = netfilterqueue.NetfilterQueue()
nfqueue.bind(0, print_and_accept)
nfqueue.run()

