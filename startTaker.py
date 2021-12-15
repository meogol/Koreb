import logging

from iter_two.core.server.server import Server
from logs import print_logs
from setting_reader import setting_read, setting_res

if __name__ == '__main__':

    logs = {'to_log': True, 'to_console': False}

    if logs['to_log']:
        logging.basicConfig(filename="taker.log", level=logging.INFO, filemode="w")

    print_logs(logs=logs, msg="Taker started!\n", log_type="info")


    setting_read(logs)

    server = Server(socket_type="server", logs=logs)
    server.init_listener()

    input("End")
