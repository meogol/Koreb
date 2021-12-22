import pickle
import queue

import numpy as np
import numpy as numpy
from scapy.all import *
from scapy.layers.inet import ICMP, TCP
from scapy.layers.ipsec import IP
from scapy.layers.l2 import Ether

import scapy.all as scapy
from iter_two.printer import print_len
from iter_two.core.cahce.cache import CacheManager


class Taker:
    def __init__(self):
        self.cache_manager = CacheManager()
        self.stack = queue.LifoQueue(0)
        self.check_stack_thread = threading.Thread(target=self.check_n_send_pkg_from_stack)
        self.check_stack_thread.start()

    def add_stack(self, package):
        int_list = pickle.loads(package)

        self.stack.put(int_list)

    def check_n_send_pkg_from_stack(self):
        while True:
            if self.stack.empty():
                continue

            pkg = self.stack.get()
            self.start(pkg)

    def start(self, int_list):
        """
        запускает анализ пакета в тейкере
        @param package: пакет в виде числового байткода
        @param addr: кортеж вида (ip, port)
        @return:
        """
        # print("int_pickle\t" + str(int_list))

        if self.cache_manager.get_last_pkg_cache('192.168.1.57') is not None:
            int_list = Taker.recovery_pkg(int_list, self.cache_manager.get_last_pkg_cache('192.168.1.57'))

        # print("int_list\t" + str(int_list))

        self.cache_manager.add_all_cache('192.168.1.57', int_list)

        if type(int_list) == numpy.ndarray:
            int_list = int_list.tolist()

        int_package = 0
        for i in range(len(int_list)):
            int_package += int_list[i] * 10 ** (len(int_list) - i - 1)
        # print("int_package\t" + str(int_package))

        byte_package = int_to_bytes(int_package)
        # print("byte_package\t" + str(byte_package))
        scapy_package = scapy.IP(byte_package)
        send(scapy_package)

    @staticmethod
    def recovery_pkg(package, last_pkg):
        """
        восстановление пакета
        @param last_pkg: прошлый пакет, пришедший на определённый IP
        @param package: передаваемый пакет. Передавать стоит в виде листа чисел
        @return: восстановленный пакет. Возвращается в виде листа чисел
        """
        filtered = list()
        for item in package:
            if item >= 0:
                filtered.append(item)
            else:
                filtered.extend([-1] * -item)

        this_pkg = np.array(filtered)
        last_pkg = np.array(last_pkg)

        tail = []
        if len(this_pkg) > len(last_pkg):
            tail = this_pkg[len(last_pkg + 1):]
            this_pkg = this_pkg[:len(last_pkg)]
        elif len(this_pkg) < len(last_pkg):
            last_pkg = last_pkg[:len(this_pkg)]

        new_pkg = np.where(this_pkg >= 0, this_pkg, last_pkg)

        if len(tail) != 0:
            new_pkg = np.append(new_pkg, tail)
        return new_pkg


def int_to_bytes(x: int) -> bytes:
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')
