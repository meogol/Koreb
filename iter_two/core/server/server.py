import logging
import threading

from iter_two.core.server.serv_socket_client import SocketClient
from iter_two.core.server.serv_socket_server import SocketServer
from iter_two.core.server.mysocket import Socket
from setting_reader import setting_res


class Server:
    def __init__(self, socket_type="server", host=str(setting_res.get('host')), port=int(setting_res.get('port')), TO_LOG=True, TO_CONSOLE=True):
        """
        socket_type = "server" or "client"
        """
        self.TO_LOG = TO_LOG
        self.TO_CONSOLE = TO_CONSOLE
        self.socket_type = socket_type

        if self.socket_type == "server":
            self.socket = SocketServer(host=host, port=port, TO_LOG=TO_LOG, TO_CONSOLE=TO_CONSOLE)
        else:
            self.socket = SocketClient(host=host, port=port, TO_LOG=TO_LOG, TO_CONSOLE=TO_CONSOLE)

    def init_listener(self):
        self.socket.run_listener_server()

    def send_package(self, destination_ip, package):
        """
        @param destination_ip: ip получателя пакета
        @param package: пакет в виде набора байт
        @return:
        """

        if self.TO_LOG:
            logging.info("Sending Package...")

        self.socket.build_and_send_message(destination_ip, package)
        """
        back_msg = None
        while back_msg != 200:
            back_msg = self.socket.build_and_send_message(destination_ip, package)
        """
        if self.TO_CONSOLE:
            print("Send package")
            print()
