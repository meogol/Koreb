import time
import requests
from typing import List

from Controller.cache.cache_item import CacheItem


class SendDataToTaker:
    @staticmethod
    def send_pakage(pkg, ip="15"):
        weight = "100"
        requests.post("http://127.0.0.1:5000/post_pkg/", data={'ip': ip, 'pkg': pkg})
        requests.post("http://127.0.0.1:5000/logging/", weight)
        delay = 20 * len(pkg)
        if delay > 2000:
            delay = 2000

        time.sleep(delay / 1000)
        return 1

    @staticmethod
    def send_com_list_to_taker(cache_items_list: List[CacheItem]):
        data = dict()

        for item in cache_items_list:
            data[item.id] = item.commands

        requests.post("http://127.0.0.1:5000/post_command/", data)
