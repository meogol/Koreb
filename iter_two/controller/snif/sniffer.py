#!/usr/bin/env python
import logging

import netfilterqueue
import scapy.all as scapy
from scapy.layers.inet import IP, TCP
from scapy.layers.l2 import Ether
from scapy.packet import Raw
from scapy.sendrecv import send

from iter_two.controller.controller import Controller
from logs import print_logs
from setting_reader import setting_read, setting_res


class Sniffer:

    def __init__(self, logs={'to_log':True, 'to_console': True}):
        self.controller = Controller(logs)
        self.logs = logs

    def to_process(self):
        nfqueue = netfilterqueue.NetfilterQueue()
        while True:
            nfqueue.bind(0, self.to_sniff)
            nfqueue.run()

    def to_sniff(self, packet):
        # print(packet.get_payload())
        scapy_packet = scapy.IP(packet.get_payload())
        packet.drop()
        # print(scapy_packet)


        src_ip = scapy_packet.sprintf("%IP.src%")
        dst_ip = scapy_packet.sprintf("%IP.dst%")
        data = list(scapy.raw(scapy_packet))

        

        """HARDCODE"""
        if src_ip == "192.168.1.45" and dst_ip == "192.168.1.57":
            # package = bytes(scapy_packet)
            # if ':' not in dst_ip:
            #     pkt = IP(src="192.168.0.101", dst="192.168.0.109") / TCP() / Raw(data)
            # else:
            #     pkt = Ether(src="192.168.0.101", dst="192.168.0.109") / TCP() / Raw(data)
            # print("from_ip:\t" + str(src_ip))
            # print("to_ip:\t\t" + str(dst_ip))

            send(scapy_packet)
            # print("VANYA OTVECHAETTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
        elif src_ip == "192.168.1.57" and dst_ip == "192.168.1.45":
            # print("from_ip:\t" + str(src_ip))
            # print("to_ip:\t\t" + str(dst_ip))

            self.controller.analyse_command(scapy_packet, dst_ip)

        # print("data:\t\t" + str(data))
        # print()
