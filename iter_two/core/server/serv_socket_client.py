import socket


class SocketClient:
    def __init__(self, host='192.168.0.101', port=7777):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def build_and_send_message(self, destination_ip, package):
        """
        @param: destination_ip: ip получателя пакета
        @param: package: пакет в виде набора байт
        @param: resending: отправляется ли пакет повторно
        """
        while 1:
            send_msg = str(package)
            send_msg = send_msg.replace("[", "[" + destination_ip + ", ", 1)
            # Используйте этот сокет для кодирования того, что вы вводите, и отправьте его на этот адрес и
            # соответствующий порт
            self.client.sendto(send_msg.encode('utf-8'), (self.host, self.port))

            # Декодировать полученную информацию
            back_msg = self.client.recv(1024).decode('utf-8')

        self.client.close()
