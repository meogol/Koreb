import requests
import random
from flask import Flask, request
from flask_cors import CORS

from Controller.cache.cache_item import CacheItem
from Controller.cache.commandCache import CommandCache
from Controller.traffic_generator.trafficGenerator import TrafficGenerator

IP_COUNT = 10
CORTEGE_MAX_LEN = 3
CORTEGE_MIN_LEN = 2


def test_neuro(new_cache_count, traffic, command_cache):
    i = 0
    cache_count = 0
    while i < len(traffic) and cache_count != new_cache_count:
        cortegeLen = random.randrange(CORTEGE_MIN_LEN, CORTEGE_MAX_LEN + 1, 1)
        fill = random.randrange(0, 1, 1)
        i += cortegeLen

        if cortegeLen != 0:
            if i < len(traffic):
                if fill == 0:
                    command_cache.append_to_cache(traffic[i - cortegeLen: i])
                    cache_count += 1


def test_request(control):
    commands = list()
    traficGen = TrafficGenerator()
    ip, comToSend = traficGen.get_ip_and_command()
    newComToSend = list()
    cortegeCount = 0
    i = 0
    while i < len(comToSend):
        cortegeLen = random.randrange(CORTEGE_MIN_LEN, CORTEGE_MAX_LEN + 1, 1)
        fill = random.randrange(0, 2, 1)
        i += cortegeLen

        if cortegeLen != 0:
            if i < len(comToSend):
                if fill == 1:
                    commands[cortegeCount] = comToSend[i - cortegeLen: i]
                    newComToSend.extend(str(cortegeCount))
                    cortegeCount += 1
                else:
                    newComToSend.extend(comToSend[i - cortegeLen: i])
            else:
                newComToSend.extend(comToSend[i - cortegeLen: len(comToSend)])
    if control:  # Заглушка кэша для analyze_package
        return commands
    else:
        return commands, newComToSend


if __name__ == '__main__':
    data, commands_to_send = test_request()
    a = requests.post("http://127.0.0.1:5000/post_command/", data)
    requests.post("http://127.0.0.1:5000/post_pkg/", data={'ip': '56', 'pkg': commands_to_send})
