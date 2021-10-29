import sys

from scapy.utils import rdpcap

from iter_two.controller.controller import Controller

from iter_two.sniffer.sniffer import Sniffer as sniffsniff

class Sniffer:
    def __init__(self):
        self.controller = Controller()
        self.snif = sniffsniff()

    def traff_file_read(self):
        """
        params:
            face: Указываем интерфейс устройства, с которого будет снифиться трафик
            pkg: Тип пакетов, которые мы будем ловить
            ip: ipv4 адресс вашего устройства
            port: порт, с которого будем слушать
            count: число пакетов, которое хотим выловить

            destination_ip: ip получателя пакета
            buf: буфер для обработки байт-кода пакета для встраивания ip адреса получателя перед первым байтом

            snifflist: получаем картеж вида [from_ip, data, snif.res[0]], где from_ip - ip отправителя,
                data - полезная нагрузка пакета, snif.res[0] - сам пакет.
        """
        while True:
            # пока задаём это хардкодом, потом поправим
            face = 'Ethernet'
            pkg = 'tcp'
            ip = '192.168.0.190'
            port = '51076'
            count = 10

            snifflist = self.snif.to_sniff(face, pkg, ip, port, count, True, True, True)

            destintion_ip = snifflist[0]
            buf = str(snifflist[2])
            buf = buf.replace("'", "", 2)
            buf = buf.replace("b\\", destintion_ip+'\\',1)
            buf = str.encode(buf, encoding='utf-8')

            # data_bytes = buf.__bytes__()
            # wight = sys.getsizeof(data_bytes)
            # print(wight)
            list_bytes = list(buf)

            print(list_bytes)
            self.controller.analyse_command(list_bytes)
