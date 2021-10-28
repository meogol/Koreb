from iter_two.controller.aggregator import Aggregator
from iter_two.core.cahce.cache import CacheManager
from iter_two.core.server.server import Server


class Controller:
    def __init__(self):
        self.server = Server()
        self.aggregator = Aggregator()
        self.cache_manager = CacheManager()

    def analyse_command(self, package):
        res = self.aggregator.contrast_last_package(package)
        self.cache_manager.add_agr_cache(1, package)
        self.server.send_package(package)
