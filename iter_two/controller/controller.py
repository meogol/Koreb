import math

from iter_two.controller.aggregator import Aggregator
from iter_two.core.cahce.cache import CacheManager
from iter_two.core.server.server import Server

class Controller:
    def __init__(self, TO_LOG, TO_CONSOLE):
        self.TO_LOG = TO_LOG
        self.TO_CONSOLE = TO_CONSOLE
        self.server = Server(socket_type="client", TO_LOG=TO_LOG, TO_CONSOLE=TO_CONSOLE)
        self.cache_manager = CacheManager()
        self.aggregator = Aggregator(self.cache_manager)

    def analyse_command(self, package, destination_ip):
        """

        @param package: пакет в виде набора байт
        @param destination_ip: ip получателя пакета
        @return:
        """

        int_package = int_from_bytes(bytes(package))
        int_list = [(int_package//(10**i))%10 for i in range(math.ceil(math.log(int_package, 10))-1, -1, -1)]
        self.server.send_package(destination_ip, int_list)


def int_to_bytes(x: int) -> bytes:
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')


def int_from_bytes(xbytes: bytes) -> int:
    return int.from_bytes(xbytes, 'big')
