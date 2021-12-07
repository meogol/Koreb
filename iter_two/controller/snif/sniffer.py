#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy
from scapy.layers.inet import IP, TCP
from scapy.layers.l2 import Ether
from scapy.packet import Raw
from scapy.sendrecv import send

from iter_two.controller.controller import Controller
from setting_reader import setting_read, setting_res


class Sniffer:

    def __init__(self):
        self.controller = Controller()

    def to_process(self):
        while True:
            nfqueue = netfilterqueue.NetfilterQueue()
            nfqueue.bind(0, self.to_sniff)
            nfqueue.run()

    def to_sniff(self, packet):
        print(packet.get_payload())
        scapy_packet = scapy.IP(packet.get_payload())
        packet.drop()
        print(scapy_packet)

        src_ip = scapy_packet.sprintf("%IP.src%")
        dst_ip = scapy_packet.sprintf("%IP.dst%")
        data = list(scapy.raw(scapy_packet))

        setting_read()

        """ NOT A HARDCODE"""
        if src_ip == setting_res.get('client_ip'):
            package = bytes(scapy_packet)
            if ':' not in dst_ip:
                pkt = IP(src=setting_res.get('client_ip'), dst=setting_res.get('server_ip')) / TCP() / Raw(data)
            else:
                pkt = Ether(src=setting_res.get('client_ip'), dst=setting_res.get('server_ip')) / TCP() / Raw(data)
            send(scapy_packet)
            print("VANYA OTVECHAETTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
        else:
            print("NE OTVECHAET :c")
            self.controller.analyse_command(scapy_packet, dst_ip)

        print("from_ip:\t" + str(src_ip))
        print("to_ip:\t\t" + str(dst_ip))
        print("data:\t\t" + str(data))
        print()
