import sys

from scapy.utils import rdpcap

from iter_two.controller.controller import Controller


class Sniffer:
    def __init__(self):
        self.controller = Controller()

    def traff_file_read(self):
        while True:
            bytedata = rdpcap("iter_two/controller/info.pcapng", count=1000).res
            for item in bytedata:
                data_bytes = item.__bytes__()
                wight = sys.getsizeof(data_bytes)
                print(wight)
                list_bytes = list(data_bytes)

                print(list_bytes)
                self.controller.analyse_command(list_bytes)

