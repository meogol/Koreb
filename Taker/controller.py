import numbers
import time

import requests

from Controller.traffic_generator.trafficGenerator import TrafficGenerator
from Taker.cahce_core.cache_generator import CacheGenerator


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
        print(str(len(command)) + "\t" + str(len(res)))
        print(str(res))

    def serialize_command(self, command):
        res = list()
        for item in command:
            if item.isdigit():
                data = self.cache_generator.get_item(item)
                if data is not None:
                    res.extend(data)
            else:
                res.append(item)

        return res

    def update_graph(self, command_dict):
        for key in command_dict.keys():
            self.cache_generator.add_items(key, command_dict.get(key))

if __name__ == '__main__':

    controller = Controller()
    toSend = True

    while toSend:
        trafficGen = TrafficGenerator()
        ip, traffic = trafficGen.get_ip_and_command()
        toSend = controller.send_taker_pakage(traffic)


