from scapy.all import *

class Sniffer:

    def __init__(self):
        pass

    def show_sniffer_stat(self, net_face, packet_type, ip):
        snif = sniff(filter = packet_type + ' and ' + 'host ' + ip, iface=net_face, count=1)
        # hexical = snif.hexdump()
        # hexical = import_hexcap(hexical)
        print(snif.res)


if __name__ == '__main__':
    sniffer = Sniffer()
    a = 'Беспроводная сеть'
    b = 'udp'
    c = '192.168.0.105'
    sniffer.show_sniffer_stat(a, b, c)
