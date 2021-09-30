import asyncio
import time
import requests


class SendDataToTaker:
    def send_pakage(self, item):
        ip = "15"

        requests.post("http://127.0.0.1:5000/post_pkg/", data={'ip': ip, 'pkg': item})

        delay = 20 * len(item)
        if delay > 2000:
            delay = 2000

        time.sleep(delay/1000)
        return 1


    def send_com_list_to_taker(self):

        pass