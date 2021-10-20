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

        file = open("info.txt", 'w')
        bytedata = rdpcap("info.pcapng", count=100)

        for i, res in enumerate(bytedata.res):

            from_ip = bytedata[i].sprintf("%IP.src%")
            if from_ip == "??":
                from_ip = bytedata[i].sprintf("%IPv6.src%")
                if from_ip == "??":
                    from_ip = bytedata[i].src

            to_ip = bytedata[i].sprintf("%IP.dst%")
            if to_ip == "??":
                to_ip = bytedata[i].sprintf("%IPv6.dst%")
                if to_ip == "??":
                    to_ip = bytedata[i].dst

            data = bytedata[i].payload.payload.payload

            file.write(str(to_ip) + '\t' + str(data) + '\n')


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
