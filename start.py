from threading import Thread

from Taker.api_core import api as api
from Server.server import Server
from Controller.get_respond_from_taker import run as respond_run

class StartProgram():
    def __init__(self):
        self.api = api
        self.server = Server()
        th = Thread(target=api.run)
        th.start()

    def lets_go(self):
        """
        Entry to the programm
        """
        th = Thread(target=respond_run())
        th.start()

if __name__ == '__main__':
    start = StartProgram()
    start.lets_go()
