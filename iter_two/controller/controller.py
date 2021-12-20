import math

from iter_two.controller.aggregator import Aggregator
from iter_two.core.cahce.cache import CacheManager
from iter_two.core.server.server import Server


class Controller:
    def __init__(self, logs={'to_log': True, 'to_console': True}):
        self.logs = logs
        self.server = Server(socket_type="client", logs=self.logs)
        self.cache_manager = CacheManager()
        self.aggregator = Aggregator(self.cache_manager)

    def analyse_command(self, package, destination_ip):
        """

        @param package: пакет в виде набора байт
        @param destination_ip: ip получателя пакета
        @return:
        """

        int_package = int_from_bytes(bytes(package))

        print('int_package', int_package)

        int_list = [(int_package // (10 ** i)) % 10 for i in range(math.ceil(math.log(int_package, 10)) - 1, -1, -1)]

        if self.cache_manager.get_last_pkg_cache(destination_ip) is not None:
            int_list = self.aggregator.contrast_last_package(int_list, '192.168.1.45')
        self.cache_manager.add_all_cache('192.168.1.45', int_list)

        self.server.send_package(destination_ip, int_list)


def int_to_bytes(x: int) -> bytes:
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')


def int_from_bytes(xbytes: bytes) -> int:
    return int.from_bytes(xbytes, 'big')
