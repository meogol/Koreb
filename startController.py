import logging

from iter_two.controller.snif.sniffer import Sniffer
from setting_reader import setting_read

if __name__ == '__main__':

    TO_LOG = True
    TO_CONSOLE = True

    if TO_LOG:
        logging.basicConfig(filename="controller.log", level=logging.INFO, filemode="w")
        logging.info("Controller started!\n")

    setting_read(TO_LOG, TO_CONSOLE)

    sniffer = Sniffer(TO_LOG, TO_CONSOLE)
    sniffer.to_process()
