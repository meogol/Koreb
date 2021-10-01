from Controller.send_data_to_taker import SendDataToTaker
from Taker.api_core.test import test_request, test_neuro
from Controller.traffic_generator.trafficGenerator import TrafficGenerator
from Controller.cache.commandCache import CommandCache
import copy

GOOD_LENTH = 70


class Controller:

    def __init__(self):
        self.command_cache = CommandCache()
        self.sender = SendDataToTaker()

    def analyze_package(self, traffic):
        """Ужимает приходящий трафик. Анализирует, достаточно ли ужалось - в случае чего вызывает нейронку"""
        com = self.compressed(traffic)
        if len(com) > GOOD_LENTH:
            self.run_neuro(5, traffic)

        self.upgrade_taker()
        self.send_data(com)

    def compressed(self, traffic):
        """Возвращает пережатый list"""
        com = copy.deepcopy(traffic)
        for cache_item in self.command_cache.cache_predicted:
            for com_item in range(len(com)):
                if cache_item.commands == com[com_item:com_item + len(cache_item.commands)]:
                    start = com_item + 1
                    end = com_item + len(cache_item.commands)
                    cache_replace = cache_item.id
                    com[start - 1] = cache_replace
                    del com[start:end]

        return com

    def run_neuro(self, new_cache_count, traffic):
        """Имитация нейронной сети - добавляет кэш-предикт"""
        test_neuro(new_cache_count, traffic, self.command_cache)

    def send_data(self, command):
        self.sender.send_pakage(command)

    def upgrade_taker(self):
        self.sender.send_com_list_to_taker(self.command_cache.cache_predicted)

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
