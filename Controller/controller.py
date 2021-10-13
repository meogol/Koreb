import random

import requests

from Controller.send_data_to_taker import SendDataToTaker
from Taker.api_core.test import test_request, test_neuro
from Controller.traffic_generator.trafficGenerator import TrafficGenerator
from Controller.cache.commandCache import CommandCache
from Controller import get_respond_from_taker as responder
import copy
from scapy.all import *

GOOD_LENGTH = 30


class Controller:

    def __init__(self):
        self.command_cache = CommandCache()
        self.sender = SendDataToTaker()

    def analyze_package(self, traffic):
        """Ужимает приходящий трафик. Анализирует, достаточно ли ужалось - в случае чего вызывает нейронку"""
        if_404 = traffic
        requests.post('http://127.0.0.1:4998/respond/', data={'status':'404', 'command': if_404})
        print("Длина изначальная " + str(len(traffic)) )
        print("Изначальная строка \n" + traffic)
        com = self.compressed(traffic)
        if len(com) > GOOD_LENGTH:
            self.run_neuro(5, traffic)

        self.upgrade_taker()
        self.send_data(com)

    def compressed(self, traffic):
        com = copy.deepcopy(traffic)
        for cache_item in self.command_cache.cache_predicted:
            if com.find(cache_item.commands) != -1:
                cache_replace = cache_item.id
                k = len(cache_item.commands)
                replaceable = com[com.find(cache_item.commands):com.find(cache_item.commands) + k]
                com = com.replace(replaceable, str(cache_replace))
        return com

    def run_neuro(self, new_cache_count, traffic):
        """Имитация нейронной сети - добавляет кэш-предикт"""
        test_neuro(new_cache_count, traffic, self.command_cache)

    def send_data(self, command):
        self.sender.send_pakage(command)
    def upgrade_taker(self):
        self.sender.send_com_list_to_taker(self.command_cache.cache_predicted)


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
