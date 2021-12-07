#!/usr/bin/env python
import logging

import netfilterqueue
import scapy.all as scapy
from scapy.layers.inet import IP, TCP
from scapy.layers.l2 import Ether
from scapy.packet import Raw
from scapy.sendrecv import send

from iter_two.controller.controller import Controller
from setting_reader import setting_read, setting_res


class Sniffer:

    def __init__(self, TO_LOG, TO_CONSOLE):
        self.controller = Controller(TO_LOG, TO_CONSOLE)
        self.TO_LOG = TO_LOG
        self.TO_CONSOLE = TO_CONSOLE

    def to_process(self):
        while True:
            nfqueue = netfilterqueue.NetfilterQueue()
            nfqueue.bind(0, self.to_sniff)
            nfqueue.run()

    def to_sniff(self, packet):

        scapy_packet = scapy.IP(packet.get_payload())
        packet.drop()

        if self.TO_LOG:
            logging.info("PACKAGE:\t" + scapy_packet)
        if self.TO_CONSOLE:
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

            if self.TO_LOG:
                logging.info("THIS IS: Response from client")
            if self.TO_CONSOLE:
                print("THIS IS: Response from client")
        else:
            if self.TO_LOG:
                logging.info("THIS IS: Server's package")
            if self.TO_CONSOLE:
                print("THIS IS: Server's package")

            self.controller.analyse_command(scapy_packet, dst_ip)

        if self.TO_LOG:
            logging.info("FROM:\t" + str(src_ip))
            logging.info("TO:\t\t" + str(dst_ip))
            logging.info("DATA:\t\t" + str(data) + '\n')

        if self.TO_CONSOLE:
            print("from_ip:\t" + str(src_ip))
            print("to_ip:\t\t" + str(dst_ip))
            print("data:\t\t" + str(data))
            print()
