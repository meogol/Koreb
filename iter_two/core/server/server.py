import threading

from iter_two.core.server.serv_socket_client import SocketClient
from iter_two.core.server.serv_socket_server import SocketServer
from setting_reader import setting_res


class Server:
    def __init__(self, host='localhost', port=7777):
        self.socket_client = SocketClient(host=str(setting_res.get('host')), port=int(setting_res.get('port')))
        self.socket_server = SocketServer(host=str(setting_res.get('host')), port=int(setting_res.get('port')))

    def init_listener_thread(self):
        t = threading.Thread(target=self.socket_server.run_listener_server)
        t.start()

    def init_listener(self):
        self.socket_server.run_listener_server()

    def send_package(self, destination_ip, package):
        """

        @param destination_ip: ip получателя пакета
        @param package: пакет в виде набора байт
        @return:
        """
        # self.socket_client.build_and_send_message(destination_ip, package)


if __name__ == '__main__':
    serv = Server('192.168.0.102')
    serv.init_listener_thread()
