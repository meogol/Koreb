import threading
import ctypes, sys
from iter_two.core.snif.sniffer import Sniffer
from iter_two.core.server.server import Server
from setting_reader import setting_read, setting_res


class StartProgram:
    def __init__(self):
        self.sniffer = Sniffer()
        self.server = Server()

    def start(self):
        self.server.init_listener_thread()
        setting_read()
        th1 = threading.Thread(target=self.sniffer.traff_file_read, kwargs={'pkg': setting_res.get("pkg_type"),
                                                                            'ip': setting_res.get("ip"),
                                                                            'port': setting_res.get("port")})
        th1.start()




if __name__ == '__main__':
    start = StartProgram()
    start.start()
    input("End")

