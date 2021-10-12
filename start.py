from threading import Thread
from Taker.api_core import api as api
from Server.server import Server
<<<<<<< Updated upstream:start.py
from Controller.get_respond_from_taker import run as respond_run

=======

"""
"Точка входа"
"""
>>>>>>> Stashed changes:Start/start.py
class StartProgram():
    def __init__(self):
        self.api = api
        self.server = Server()
        th = Thread(target=api.run)
        th.start()

    def lets_go(self):
        """
<<<<<<< Updated upstream:start.py
        Entry to the programm
        """
        th = Thread(target=respond_run())
        th.start()
=======
        Запуск сервера
        """
        self.server.run()
>>>>>>> Stashed changes:Start/start.py

if __name__ == '__main__':
    start = StartProgram()
    start.lets_go()
