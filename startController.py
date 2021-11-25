
from iter_two.controller.snif.sniffer import Sniffer
from setting_reader import setting_read

if __name__ == '__main__':
    setting_read()

    sniffer = Sniffer()
    sniffer.to_process()
