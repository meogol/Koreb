import logging
from scapy.all import *
from scapy.layers.dns import DNS
from scapy.layers.inet import UDP
from scapy.layers.inet import *


class test():

    def __init__(self):
        pass

    def show(self):
        self.a = rdpcap("info.pcapng", count=1000)
        print(self.a)

if __name__ == '__main__':
    src = test()
    src.show()
    i = 200
