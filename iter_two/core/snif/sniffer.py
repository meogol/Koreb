from iter_two.controller.controller import Controller
from scapy.all import *


class Sniffer:
    def __init__(self):
        self.controller = Controller()

    def traff_file_read(self, face='Беспроводная сеть', pkg='tcp', ip='192.168.0.102', port='6868', count=1):
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
            snifflist = self.to_sniff(face, pkg, ip, port, count, False, True, True)

            destination_ip = snifflist[0]

            data_bytes = snifflist[2].__bytes__()
            list_bytes = list(data_bytes)

            self.controller.analyse_command(list_bytes, destination_ip)

    def get_ip(self, snif, id, type):

        """
        Служебный метод для функции to_sniff()
        """

        if snif[id].sprintf("%IP." + type + "%") != "??":
            return snif[id].sprintf("%IP." + type + "%")
        elif snif[id].sprintf("%IPv6." + type + "%") != "??":
            return snif[id].sprintf("%IPv6." + type + "%")
        else:
            if type == "src":
                return snif[id].src
            else:
                return snif[id].dst

    def get_sniff(self, net_face, packet_type="TCP", ip="", port="", host="host ", count=1):

        """
        Служебный метод для функции to_sniff()
        """

        if ip != "":
            return sniff(filter=packet_type + ' and ' + host + ip, iface=net_face, count=count)
        elif port != "":
            return sniff(filter=packet_type + ' port ' + port, iface=net_face, count=count)

    def to_sniff(self, net_face="Беспроводная сеть", packet_type="TCP", ip="", port="", count=1,
                 by_sender=False, by_taker=False, to_file=False):
        """
        *Readme*

        Метод возвращает IP отправителя, Data и весь пакет целиком.
        В файл "info.txt" записываются IP отправителя, IP получателя и Data.

        В метод передаётся:

            net_face - интерфейс сети (???), например передаём "Беспроводная сеть"
            packet_type - тип пакета (TCP, UDP и т.д.)
            ip - отслеживаемый IP-адрес
            port - отслеживаемый port (вместо ip)

            * ip и port не могут быть пустыми одновременно! *

            count - количесвто пакетов, которое необходимо перехватить

            * Метод возвращает данные о последнем пакете => для получения корректных значений
            (т.е. не для записи в файл) стоит count = 1 *

            (by_sender = True, by_taker = True) - Отслеживает все передачи, связанные с IP
            (by_sender = True, by_taker = False) - Ослеживает отправителя по IP
            (by_sender = False, by_taker = True) - Отслеживает получателя по IP
            (by_sender = False, by_taker = False) - Нельзя! return "400 Bad Request"

            to_file = True, если необходима запись в файл (например, для отладки)

        """

        if by_sender and by_taker:
            host = "host "
        elif by_taker:
            host = "dst host "
        elif by_sender:
            host = "src host "
        else:
            return "400 Bad Request"

        snif = self.get_sniff(net_face, packet_type, ip, port, host, count)

        if to_file:
            file = open("info.txt", 'w')

        for i, res in enumerate(snif.res):

            from_ip = self.get_ip(snif, i, "src")
            to_ip = self.get_ip(snif, i, "dst")

            data = snif[i].payload.payload.payload

            if to_file:
                file.write(str(from_ip) + '\t' + str(to_ip) + '\t' + str(data) + '\n')

        if to_file:
            file.close()

        return [to_ip, data, snif.res[0]]
