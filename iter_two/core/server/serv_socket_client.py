import socket

from iter_two.core.server.mysocket import Socket
from setting_reader import setting_res


class SocketClient(Socket):
    def __init__(self, host=setting_res.get("host"), port=setting_res.get("port")):
        super().__init__(host, port, "client")

    def build_and_send_message(self, destination_ip, package):
        """
        @param: destination_ip: ip получателя пакета
        @param: package: пакет в виде набора байт
        @param: resending: отправляется ли пакет повторно
        """
        send_msg = str(package)
        send_msg = send_msg.replace("[", "[" + destination_ip + ", ", 1)
        # Используйте этот сокет для кодирования того, что вы вводите, и отправьте его на этот адрес и
        # соответствующий порт
        self.soc.sendto(send_msg.encode('utf-8'), (self.host, self.port))

        # Декодировать полученную информацию
        back_msg = self.soc.recv(1024).decode('utf-8')



