from scapy.all import *

class Sniffer:

    def __init__(self):
        pass

    def sniff_to_file_by_port(self, net_face, packet_type, port, count):
        snif = sniff(filter = packet_type + ' port ' + port, iface=net_face, count=count)

        file = open("info.txt", 'w')

        for i, res in enumerate(snif.res):

            from_ip = snif[i].sprintf("%IP.src%")
            if from_ip == "??":
                from_ip = snif[i].sprintf("%IPv6.src%")
            if from_ip == "??":
                from_ip = snif[i].src

            to_ip = snif[i].sprintf("%IP.dst%")
            if to_ip == "??":
                to_ip = snif[i].sprintf("%IPv6.dst%")
            if to_ip == "??":
                to_ip = snif[i].dst

            data = snif[i].payload.payload.payload

            file.write(str(to_ip) + '\t' + str(data) + '\n')
    def sniff_to_file_by_id(self, net_face, packet_type, ip, count):
        snif = sniff(filter = packet_type + ' and ' + 'host ' + ip, iface=net_face, count=count)

        file = open("info.txt", 'w')

        for i, res in enumerate(snif.res):

            from_ip = snif[i].sprintf("%IP.src%")
            if from_ip == "??":
                from_ip = snif[i].sprintf("%IPv6.src%")
            if from_ip == "??":
                from_ip = snif[i].src

            to_ip = snif[i].sprintf("%IP.dst%")
            if to_ip == "??":
                to_ip = snif[i].sprintf("%IPv6.dst%")
            if to_ip == "??":
                to_ip = snif[i].dst

            data = snif[i].payload.payload.payload

            file.write(str(to_ip) + '\t' + str(data) + '\n')

    def sniff_get_parse_by_port(self, net_face, packet_type, port):
        snif = sniff(filter = packet_type + ' port ' + port, iface=net_face, count=1)
        from_ip = snif[0].sprintf("%IP.src%")
        if from_ip == "??":
            from_ip = snif[0].sprintf("%IPv6.src%")
        if from_ip == "??":
            from_ip = snif[0].src

        to_ip = snif[0].sprintf("%IP.dst%")
        if to_ip == "??":
            to_ip = snif[0].sprintf("%IPv6.dst%")
        if to_ip == "??":
            to_ip = snif[0].dst

        data = snif[0].payload.payload.payload

        return [from_ip, data, snif.res[0]]
    def sniff_get_parse_by_ip(self, net_face, packet_type, ip):
        snif = sniff(filter = packet_type + ' and ' + 'host ' + ip, iface=net_face, count=1)
        from_ip = snif[0].sprintf("%IP.src%")
        if from_ip == "??":
            from_ip = snif[0].sprintf("%IPv6.src%")
        if from_ip == "??":
            from_ip = snif[0].src

        to_ip = snif[0].sprintf("%IP.dst%")
        if to_ip == "??":
            to_ip = snif[0].sprintf("%IPv6.dst%")
        if to_ip == "??":
            to_ip = snif[0].dst

        data = snif[0].payload.payload.payload

        return [from_ip, data, snif.res[0]]
    def sniff_get_parse_by_sender_ip(self, net_face, packet_type, ip):

        snif = sniff(filter = packet_type + ' and ' + 'host ' + ip, iface=net_face, count=1)
        while snif[0].sprintf("%IP.src%") != ip:
            snif = sniff(filter=packet_type + ' and ' + 'host ' + ip, iface=net_face, count=1)

        from_ip = snif[0].sprintf("%IP.src%")
        if from_ip == "??":
            from_ip = snif[0].sprintf("%IPv6.src%")
        if from_ip == "??":
            from_ip = snif[0].src

        to_ip = snif[0].sprintf("%IP.dst%")
        if to_ip == "??":
            to_ip = snif[0].sprintf("%IPv6.dst%")
        if to_ip == "??":
            to_ip = snif[0].dst

        data = snif[0].payload.payload.payload

        return [from_ip, data, snif.res[0]]
    def sniff_get_parse_by_taker_ip(self, net_face, packet_type, ip):

        snif = sniff(filter=packet_type + ' and ' + 'host ' + ip, iface=net_face, count=1)
        while snif[0].sprintf("%IP.dst%") != ip:
            snif = sniff(filter=packet_type + ' and ' + 'host ' + ip, iface=net_face, count=1)

        from_ip = snif[0].sprintf("%IP.src%")
        if from_ip == "??":
            from_ip = snif[0].sprintf("%IPv6.src%")
        if from_ip == "??":
            from_ip = snif[0].src

        to_ip = snif[0].sprintf("%IP.dst%")
        if to_ip == "??":
            to_ip = snif[0].sprintf("%IPv6.dst%")
        if to_ip == "??":
            to_ip = snif[0].dst

        data = snif[0].payload.payload.payload

        return [from_ip, data, snif.res[0]]


if __name__ == '__main__':
    sniffer = Sniffer()
    face = 'Беспроводная сеть'
    pkg = 'udp'
    ip = '192.168.0.101'
    port = '51076'
    count = 1
    sniffer.sniff_to_file(face, pkg, ip, count)
    snifflist = sniffer.sniff_get_parse_by_port(face, pkg, port)
    print(snifflist)
