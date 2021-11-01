import threading

from iter_two.core.snif.sniffer import Sniffer
from iter_two.core.server.server import Server


class StartProgram:
    def __init__(self):
        self.sniffer = Sniffer()
        self.server = Server()

    def start(self):
        self.server.init_listener_thread()

        th1 = threading.Thread(target=self.sniffer.traff_file_read)
        th1.start()


if __name__ == '__main__':
    start = StartProgram()
    start.start()
