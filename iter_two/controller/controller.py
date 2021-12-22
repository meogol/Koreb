import pickle

import math
import queue
import threading

import numpy

from iter_two.controller.aggregator import Aggregator
from iter_two.core.cahce.cache import CacheManager
from iter_two.core.server.server import Server
from iter_two.printer import print_len
from iter_two.taker.taker import Taker


class Controller:
    def __init__(self):
        self.server = Server(socket_type="client")
        self.cache_manager = CacheManager()
        self.aggregator = Aggregator(self.cache_manager)
        self.stack = queue.Queue(0)
        self.check_stack_thread = threading.Thread(target=self.analyse_command)
        self.check_stack_thread.start()

    def add_stack(self, package):
        self.stack.put(package)

    def analyse_command(self):
        """

        @param package: пакет в виде набора байт
        @param destination_ip: ip получателя пакета
        @return:
        """
        destination_ip = "192.168.1.45"
        while True:
            if self.stack.empty():
                continue

            int_package = int_from_bytes(bytes(self.stack.get()))
            int_list = [(int_package // (10 ** i)) % 10 for i in range(math.ceil(math.log(int_package, 10)) - 1, -1, -1)]
            self.cache_manager.add_all_cache("192.168.1.1", int_list)
            self.server.send_package(destination_ip, int_list)


def int_to_bytes(x: int) -> bytes:
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')


def int_from_bytes(xbytes: bytes) -> int:
    return int.from_bytes(xbytes, 'big')


def int_to_list(int_pkg):
    result = []
    while int_pkg > 0:
        result.append(int_pkg % 10)
        int_pkg //= 10

    result.reverse()
    return result


if __name__ == '__main__':
    ter = Controller()
    ter.analyse_command(12587463147, 'it')
