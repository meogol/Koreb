import socket

from iter_two.core.server.mysocket import Socket
from setting_reader import setting_res


class SocketClient(Socket):
    def __init__(self, host=setting_res.get("host"), port=setting_res.get("port")):
        self.host = host
        self.port = port
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

        print("host\t" + self.host)
        print("port\t" + str(self.port))
        self.host = "192.168.102"
        self.port = 7777
        self.soc.sendto(send_msg.encode('utf-8'), (self.host, self.port))

        # Декодировать полученную информацию

        back_msg = self.soc.recv(1024).decode('utf-8')
        """
        print("BACK:")
        print(str(back_msg))
        print()
        """
        self.sock.settimeout(500.0)
        back_msg = None
        back_msg = self.soc.recv(1024).decode('utf-8')
        self.sock.settimeout(None)
        if back_msg is None:
            return 400
        else:
            return back_msg



