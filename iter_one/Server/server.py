from scapy.all import *
from iter_one.Controller.sniffer import Sniffer

class Server():
    def __init__(self):
        self.sniffer = Sniffer()

    def scan_pcapng_file(self):
        """
        Writes to bytedata all packages from pcap file (type - packetlist)
        """
        bytedata = []
        bytedata = rdpcap("info.pcapng", count=3)

        for item in bytedata:
            self.send_bytedata_to_sniffer(item)


    def send_bytedata_to_sniffer(self, item):
        """
        Sends bytedata of one package to sniffer
        """
        self.sniffer.send_command_to_controller(item)

    def run(self):
        self.scan_pcapng_file()


if __name__ == '__main__':
    src = Server()
    src.scan_pcapng_file()
