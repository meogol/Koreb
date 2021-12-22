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

        scapy_packet = scapy.IP(packet.get_payload())
        packet.drop()

        print_logs(logs=self.logs, msg="PACKAGE:\t" + str(scapy_packet), log_type="info")

        src_ip = scapy_packet.sprintf("%IP.src%")
        dst_ip = scapy_packet.sprintf("%IP.dst%")
        data = list(scapy.raw(scapy_packet))

        setting_read()

        """ NOT A HARDCODE"""
        if src_ip == setting_res.get('client_ip'):
            if ':' not in dst_ip:
                pkt = IP(src=setting_res.get('client_ip'), dst=setting_res.get('server_ip')) / TCP() / Raw(data)
            else:
                pkt = Ether(src=setting_res.get('client_ip'), dst=setting_res.get('server_ip')) / TCP() / Raw(data)
            send(scapy_packet)

            print_logs(logs=self.logs, msg="THIS IS: Response from client", log_type="info")

        else:
            print_logs(logs=self.logs, msg="THIS IS: Server's package", log_type="info")

            self.controller.analyse_command(scapy_packet, dst_ip)

        # print("from_ip:\t" + str(src_ip))
        # print("to_ip:\t\t" + str(dst_ip))
        # print("data:\t\t" + str(data))
        # print()

