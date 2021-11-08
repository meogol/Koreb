import threading

from iter_two.core.server.serv_socket import Socket
from setting_reader import setting_read


class Server:
    def __init__(self, host='localhost', port=7777):
        self.socket = Socket(host=str(setting_read().get('host')), port=int(setting_read().get('port')))

    def init_listener_thread(self):
        t = threading.Thread(target=self.socket.run_listener_server)
        t.start()

    def send_package(self, destination_ip, package):
        """

        @param destination_ip: ip получателя пакета
        @param package: пакет в виде набора байт
        @return:
        """
        self.socket.build_and_send_message(destination_ip, package)


if __name__ == '__main__':
    serv = Server('192.168.0.102')
    serv.init_listener_thread()
