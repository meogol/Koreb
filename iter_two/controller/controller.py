from iter_two.controller.sniffer import Sniffer


class Controller:
    def __init__(self):
        self.sniffer = Sniffer()

    def start(self):
        while(True):
            res = self.sniffer.traff_file_read()
