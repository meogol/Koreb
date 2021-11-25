#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy

from iter_two.controller.controller import Controller


class Sniffer:

    def __init__(self):
        self.controller = Controller()

    def to_process(self):
        while True:
            nfqueue = netfilterqueue.NetfilterQueue()
            nfqueue.bind(0, self.to_sniff)
            nfqueue.run()

    def to_sniff(self, packet):
        scapy_packet = scapy.IP(packet.get_payload())
        packet.drop()

        print(scapy_packet)

        src_ip = scapy_packet.sprintf("%IP.src%")
        dst_ip = scapy_packet.sprintf("%IP.dst%")
        data = list(scapy.raw(scapy_packet))

        self.controller.analyse_command(data, dst_ip)

        print("from_ip:\t" + str(src_ip))
        print("to_ip:\t\t" + str(dst_ip))
        print("data:\t\t" + str(data))
        print()
