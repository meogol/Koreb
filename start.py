from threading import Thread
from time import sleep

from Taker.api_core import api as api
from Server.server import Server


class StartProgram():
    def __init__(self):
        self.api = api
        self.server = Server()
        th = Thread(target=self.server.run)
        th.start()

    def lets_go(self):
        self.api.run()


if __name__ == '__main__':
    start = StartProgram()
    start.lets_go()
