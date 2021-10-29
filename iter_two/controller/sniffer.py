import sys

from scapy.utils import rdpcap

from iter_two.controller.controller import Controller

from iter_two.sniffer.sniffer import Sniffer as sniffsniff


class Sniffer:
    def __init__(self):
        self.controller = Controller()
        self.snif = sniffsniff()

    def traff_file_read(self, face='Беспроводная сеть', pkg='tcp', ip='192.168.0.105', port='51076', count=10):
        """
        params
            face: Указываем интерфейс устройства, с которого будет снифиться трафик
            pkg: Тип пакетов, которые мы будем ловить
            ip: ipv4 адресс вашего устройства
            port: порт, с которого будем слушать
            count: число пакетов, которое хотим выловить

            destination_ip: ip получателя пакета

            snifflist: получаем картеж вида [from_ip, data, snif.res[0]], где from_ip - ip отправителя,
                data - полезная нагрузка пакета, snif.res[0] - сам пакет.
        """
        while True:
            snifflist = self.snif.to_sniff(face, pkg, ip, port, count, True, True, True)

            destination_ip = snifflist[0]

            data_bytes = snifflist[2].__bytes__()
            wight = sys.getsizeof(data_bytes)
            print(wight)
            list_bytes = list(data_bytes)

            print(list_bytes)
            self.controller.analyse_command(list_bytes, destination_ip)
