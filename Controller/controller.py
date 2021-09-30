from Taker.api_core.test import test_request, test_neuro
from Controller.traffic_generator.trafficGenerator import TrafficGenerator
from Controller.cache.commandCache import CommandCache
import copy

GOOD_LENTH = 70


class Controller:

    def __init__(self):
        self.command_cache = CommandCache()

    """Ужимает приходящий трафик. Анализирует, достаточно ли ужалось - в случае чего вызывает нейронку"""
    def analyze_package(self, traffic):
        self.traffic = traffic
        com = self.compressed()
        if len(com) > GOOD_LENTH:
            self.run_neuro(5)

    """Возвращает пережатый list"""
    def compressed(self):
        com = copy.deepcopy(self.traffic)
        for cache_item in self.command_cache.cache_predicted:
            for com_item in range(len(com)):
                if cache_item.commands == com[com_item:com_item+len(cache_item.commands)]:
                    start = com_item+1
                    end = com_item+len(cache_item.commands)
                    cache_replace = cache_item.id
                    com[start-1] = cache_replace
                    del com[start:end]

        return com


    """Неронная сеть"""
    def run_neuro(self, new_cache_count):
        """Имитация нейронной сети - добавляет кэш-предикт"""
        test_neuro(new_cache_count, self.traffic, self.command_cache)

    def send_data(self):
        pass

    def upgrade_taker(self):
        pass

    def update_cache(self):
        pass


if __name__ == '__main__':
    trafficGen = TrafficGenerator()
    ip, traffic = trafficGen.get_ip_and_command()
    controller = Controller()
    controller.command_cache.append_to_cache(['right', 'up'])
    controller.command_cache.append_to_cache(['right', 'right'])
    controller.command_cache.append_to_cache(['right', 'up-left', 'right'])
    controller.command_cache.append_to_cache(['right', 'left'])
    controller.command_cache.append_to_cache(['right', 'down'])
    controller.analyze_package(traffic)
