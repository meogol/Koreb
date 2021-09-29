import requests
import random
from flask import Flask, request
from flask_cors import CORS

from Controller.traffic_generator.trafficGenerator import TrafficGenerator

IP_COUNT = 10
CORTEGE_MAX_LEN = 10


def test_request():
    commands = dict()

    traficGen = TrafficGenerator()
    ip, comToSend = traficGen.get_ip_and_command()
    emptyIndex = dict()
    newComToSend = list()
    cortegeCount = 0
    i = 0
    while i < len(comToSend):
        command = ""
        cortegeLen = random.randrange(0, CORTEGE_MAX_LEN, 1)
        fill = random.randrange(0, 2, 1)
        i += cortegeLen

        if cortegeLen != 0:
            if i < len(comToSend):
                if fill == 1:

                    for j in range(cortegeLen):
                        command += comToSend[i+j-cortegeLen]
                    commands[cortegeCount] = command
                    newComToSend.append(str(cortegeCount))
                    cortegeCount += 1
                else:
                    for j in range(cortegeLen):
                        newComToSend.append("EMPTY")
                        emptyIndex[i+j-cortegeLen] = len(newComToSend)-1
            else:
                for j in range(len(comToSend)-(i-cortegeLen)):
                    newComToSend.append("EMPTY")
                    emptyIndex[i - cortegeLen + j] = len(newComToSend) - 1


    keys = list(emptyIndex.keys())
    for i in range(len(keys)):
        newComToSend[emptyIndex.get(keys[i])] = comToSend[keys[i]]

    return commands, newComToSend

if __name__ == '__main__':
    data, commands_to_send = test_request()
    a = requests.post("http://127.0.0.1:5000/post_command/", data)
    requests.post("http://127.0.0.1:5000/post_pkg/", data={'ip': '56', 'pkg': commands_to_send})


