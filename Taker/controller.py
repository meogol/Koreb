import numbers
import time

import requests

from Controller.traffic_generator.trafficGenerator import TrafficGenerator
from Taker.cahce_core.cache_generator import CacheGenerator
from Controller.get_respond_from_taker import respond


DELAY = 0.01

class Controller:
    def __init__(self):
        self.cache_generator = CacheGenerator()
        pass

    def send_taker_pakage(pkg, ip="15"):
        code = requests.post("http://127.0.0.1:5000/post_taker_pkg/", data={'ip': ip, 'pkg': pkg})
        if code == "418":
            time.sleep(DELAY)
        elif code == "409":
            print("ERROR! TAKER HAS NO MATCH WITH SERVER!")
            return False
        print(code)
        return True

    def analyse_command(self, ip, command):
        res = self.serialize_command(command)
        print()
        print(str(len(command[0])) + "\t" + str(len(res)))
        print(command[0])
        print(str(res))

        kil = 1000

    def serialize_command(self, command):
        res = command[0]
        data = ""
        data1 = ""

        i = 0
        while i < len(res):
            if res[i] == '!' and res[i+2] == '!':
                id = res[i:i+3]
                data = self.cache_generator.get_item(id)
                if data is not None:
                    data1 = data1 + data[0]
                    i += 2
                else:
                    data1 += res[i]
            else:
                data1 = data1 + res[i]
            i += 1
        return data1

    def update_graph(self, command_dict):
        for key in command_dict.keys():
            self.cache_generator.add_items(key, command_dict.get(key))

if __name__ == '__main__':

    controller = Controller()
    toSend = True

    a = list()
    a.append("ПРИВЕТ! !1!")
    print(controller.serialize_command(a))

'''
    while toSend:
        trafficGen = TrafficGenerator()
        ip, traffic = trafficGen.get_ip_and_command()
        toSend = controller.send_taker_pakage(traffic)
'''



