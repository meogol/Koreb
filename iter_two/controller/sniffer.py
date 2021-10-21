from scapy.utils import rdpcap

from iter_two.controller.aggregator import Aggregator


class Sniffer:
    def __init__(self):
        self.aggregator = Aggregator()

    def traff_file_read(self):
        bytedata = []
        bytedata = rdpcap("info.pcapng", count=3)

        for item in bytedata:
            self.aggregator.start_aggregation("1", item)
