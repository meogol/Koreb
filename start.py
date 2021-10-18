from threading import Thread
from iter_one.Taker.api_core import server_api as api
from iter_one.Server.server import Server
from iter_one.Controller.get_respond_from_taker import run as respond_run
from iter_one.Server import api as server_api
from time import sleep
from iter_one.Controller.controller import Controller


class StartProgram():
    def __init__(self):
        self.api = api
        self.server = Server()
        self.server_api_runner = server_api
        self.controller = Controller()



    def lets_go(self):
        """
        Entry to the program
        """

        lh = Thread(target=server_api.run)
        lh.start()

        sleep(1)

        nh = Thread(target=respond_run, args=[self.controller])
        nh.start()

        sleep(1)

        th = Thread(target=api.run)
        th.start()

        self.server.run()

if __name__ == '__main__':
    start = StartProgram()
    start.lets_go()
