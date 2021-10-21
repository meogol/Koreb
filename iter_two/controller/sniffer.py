from scapy.utils import rdpcap

from iter_two.controller.controller import Controller


class Sniffer:
    def __init__(self):
        self.controller = Controller()

    def traff_file_read(self):
        while True:
            bytedata = rdpcap("iter_two/controller/info.pcapng", count=1000)

            for item in bytedata:
                self.controller.analyse_command(item)

