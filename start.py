import threading

from iter_two.controller.sniffer import Sniffer
from iter_two.taker.taker import Taker


class StartProgram():
    def __init__(self):
        self.sniffer = Sniffer()
        self.taker = Taker()

    def start(self):
        th1 = threading.Thread(target=self.sniffer.traff_file_read)
        th1.start()
        self.taker.start()


if __name__ == '__main__':
    start = StartProgram()
    start.start()
