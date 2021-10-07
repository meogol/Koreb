from threading import Thread

from Taker.api_core import api as api
from Server.server import Server


class StartProgram():
    def __init__(self):
        self.api = api
        self.server = Server()
        th = Thread(target=api.run)
        th.start()

    def lets_go(self):
        self.server.run()

if __name__ == '__main__':
    start = StartProgram()
    start.lets_go()
