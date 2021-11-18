import numpy as np
from scapy.all import *
from scapy.layers.inet import ICMP, TCP
from scapy.layers.ipsec import IP
from scapy.layers.l2 import Ether

from iter_two.printer import print_len
from iter_two.core.cahce.cache import CacheManager


class Taker:
    def __init__(self):
        self.cache_manager = CacheManager()

    def start(self, package):
        """
        запускает анализ пакета в тейкере
        @param package: пакет в виде числового байткода
        @param addr: кортеж вида (ip, port)
        @return:
        """

        list_bytes = str(package)[2:len(str(package)) - 1].replace(' ', '').replace('[', '').replace(']', '').split(',')
        destination_ip = list_bytes[0].replace("\'", "")  # ip получателя пакета
        list_bytes = list(map(int, list_bytes[1:]))

        if ':' not in destination_ip:

            if self.cache_manager.get_last_pkg_cache(destination_ip) is None:
                self.cache_manager.add_last_pkg_cache(destination_ip, list_bytes)
                list_to_send = bytes(list_bytes)
                self.to_send(destination_ip, list_to_send)

                return

            last_pkg = self.cache_manager.get_last_pkg_cache(destination_ip)
            res = self.recovery_pkg(list_bytes, last_pkg)

            print_len(msg="\nAgregate length:\t", pkg=list_bytes, dst=destination_ip, print_pkg=False)
            print_len(msg="Resource length:\t", pkg=res, dst=destination_ip, print_pkg=False)

            self.cache_manager.add_all_cache(destination_ip, res)

            list_to_send = bytes(res)
            self.to_send(destination_ip, list_to_send)


    def recovery_pkg(self, package, last_pkg):
        """
        восстановление пакета
        @param last_pkg:
        @param package: передаваемый пакет. Передавать стоит в виде листа чисел
        @return: восстановленный пакет. Возвращается в виде листа чисел
        """

        filtered = list()
        for x in package:
            if x >= 0:
                filtered.append(x)
            else:
                filtered.extend([-1] * -x)

        this_pkg = np.array(filtered)
        last_pkg = np.array(last_pkg)

        last = []
        if len(this_pkg) > len(last_pkg):
            prom_pkg = this_pkg[:len(last_pkg)]
            last = this_pkg[len(last_pkg):]
        else:
            prom_pkg = this_pkg

        index_non_zero = [i for i in range(len(prom_pkg)) if prom_pkg[i] < 0]

        this_pkg[index_non_zero] = last_pkg[index_non_zero]

        new_pkg = this_pkg

        return new_pkg

    def to_send(self, dst_ip, package, port=7777):
        package = bytes(package)
        if ':' not in dst_ip:
            pkt = IP(dst=dst_ip)/TCP(dport=port)/Raw(package)
        else:
            pkt = Ether(dst=dst_ip) / TCP(dport=port) / Raw(package)
        send(pkt)


