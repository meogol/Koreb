import threading

from iter_two.core.server.serv_socket_client import SocketClient
from iter_two.core.server.serv_socket_server import SocketServer
from iter_two.core.server.mysocket import Socket
from setting_reader import setting_res


class Server:
    def __init__(self, socket_type="server", host=str(setting_res.get('host')), port=int(setting_res.get('port'))):
        """
        socket_type = "server" or "client"
        """
        self.socket_type = socket_type
        host = "192.168.0.103"
        port = 7777
        if self.socket_type == "server":
            self.socket = SocketServer(host=host, port=port)
        else:
            self.socket = SocketClient(host=host, port=port)

    def init_listener(self):
        self.socket.run_listener_server()

    def send_package(self, destination_ip, package):
        """
        @param destination_ip: ip получателя пакета
        @param package: пакет в виде набора байт
        @return:
        """
        self.socket.build_and_send_message(destination_ip, package)
        """
        back_msg = None
        while back_msg != 200:
            back_msg = self.socket.build_and_send_message(destination_ip, package)
        """
        print("Send packet")
        print()
