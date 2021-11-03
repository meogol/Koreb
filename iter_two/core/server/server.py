import threading

from iter_two.core.server.serv_socket import Socket


class Server:
    def __init__(self, host='localhost', port=7777):
        self.socket = Socket(host=host, port=port)

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
