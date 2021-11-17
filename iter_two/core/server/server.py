import threading

from iter_two.core.server.serv_socket_client import SocketClient
from iter_two.core.server.serv_socket_server import SocketServer
from iter_two.core.server.socket import Socket
from setting_reader import setting_res


class Server:
    def __init__(self, socket_type="server", host=str(setting_res.get('host')), port=int(setting_res.get('port'))):
        """
        socket_type = "server" or "client"
        """
        self.socket_type = socket_type
        self.socket = Socket(host=host, port=port)

    def init_listener(self):
        if self.socket_type == "server":
            self.socket_server = SocketServer(self.socket.getHost(), self.socket.getPort())
            self.socket_server.run_listener_server()
        else:
            return '400 Socket Type Error'

    def send_package(self, destination_ip, package):
        """
        @param destination_ip: ip получателя пакета
        @param package: пакет в виде набора байт
        @return:
        """
        if self.socket_type == "client":
            self.socket_client = SocketClient(self.socket.getHost(), self.socket.getPort())
            self.socket_client.build_and_send_message(destination_ip, package)
        else:
            return '400 Socket Type Error'
