import logging
import threading

from iter_two.core.server.serv_socket_client import SocketClient
from iter_two.core.server.serv_socket_server import SocketServer
from logs import print_logs
from setting_reader import setting_res



class Server:
    def __init__(self, socket_type="server", taker_ip="localhost", port=7777, logs={'to_log':True, 'to_console': True}):
        """
        socket_type = "server" or "client"
        """
        global setting_res
        taker_ip = str(setting_res.get('taker_ip'))
        port = int(setting_res.get('port'))
        self.logs = logs
        self.socket_type = socket_type

        if self.socket_type == "server":
            self.socket = SocketServer(taker_ip=taker_ip, port=port, logs=self.logs)
        else:
            self.socket = SocketClient(taker_ip=taker_ip, port=port, logs=self.logs)

    def init_listener(self):
        self.socket.run_listener_server()

    def send_package(self, destination_ip, package):
        """
        @param destination_ip: ip получателя пакета
        @param package: пакет в виде набора байт
        @return:
        """

        print_logs(logs=self.logs, msg="Sending Package...", log_type="info")

        self.socket.add_to_stack(destination_ip, package)
        """
        back_msg = None
        while back_msg != 200:
            back_msg = self.socket.build_and_send_message(destination_ip, package)
        """