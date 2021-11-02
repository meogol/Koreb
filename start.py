import threading
import ctypes, sys
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


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if __name__ == '__main__':
    if is_admin():
        start = StartProgram()
        start.start()
    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
