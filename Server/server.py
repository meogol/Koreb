import logging
from scapy.all import *
from scapy.layers.dns import DNS
from scapy.layers.inet import UDP
from scapy.layers.inet import *
from Controller.sniffer import Sniffer


class Server():

    def __init__(self):
        self.sniffer = Sniffer()

    def scan_pcapng_file(self):
        """
        Writes to bytedata all packages from pcap file in bytecode
        """
        bytedata = []
        bytedata = rdpcap("info.pcapng", count=10)  # 81188

        for item in bytedata:
            src.send_bytedata_to_sniffer(item)

    def send_bytedata_to_sniffer(self, item):
        """
        Sends bytecode of one package to sniffer
        """
        self.sniffer.send_command_to_controller(item)


if __name__ == '__main__':
    src = Server()
    src.scan_pcapng_file()
