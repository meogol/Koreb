from iter_two.controller.aggregator import Aggregator
from iter_two.core.cahce.cache import CacheManager
from iter_two.core.server.server import Server


class Controller:
    def __init__(self):
        self.server = Server()
        self.cache_manager = CacheManager()
        self.aggregator = Aggregator(self.cache_manager)

    def analyse_command(self, package, destination_ip):
        """

        @param package: пакет в виде набора байт
        @param destination_ip: ip получателя пакета
        @return:
        """

        res = package

        print()
        print(res)
        print(destination_ip)
        print("len_start "+str(len(package)))

        if self.cache_manager.get_last_pkg_cache(destination_ip) is not None:
            res = self.aggregator.contrast_last_package(package, destination_ip)

        self.cache_manager.add_all_cache(destination_ip, package)
        self.server.send_package(destination_ip, res)
