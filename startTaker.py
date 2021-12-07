import logging

from iter_two.core.server.server import Server
from setting_reader import setting_read, setting_res

if __name__ == '__main__':

    TO_LOG = True
    TO_CONSOLE = True

    if TO_LOG:
        logging.basicConfig(filename="taker.log", level=logging.INFO, filemode="w")
        logging.info("Taker started!\n")

    setting_read(TO_LOG, TO_CONSOLE)

    server = Server(socket_type="server", host=str(setting_res.get('host')), port=int(setting_res.get('port')), TO_LOG=TO_LOG, TO_CONSOLE=TO_CONSOLE)
    server.init_listener()

    input("End")
