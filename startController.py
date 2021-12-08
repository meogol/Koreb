import logging

from iter_two.controller.snif.sniffer import Sniffer
from logs import print_logs
from setting_reader import setting_read

if __name__ == '__main__':

    logs = {'to_log': True, 'to_console':False}

    if logs['to_log']:
        logging.basicConfig(filename="controller.log", level=logging.INFO, filemode="w")

    print_logs(logs=logs, msg="Controller started!\n", log_type="info")

    setting_read(logs)

    sniffer = Sniffer(logs)
    sniffer.to_process()
