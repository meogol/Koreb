import socket
import pickle
import numpy

from iter_two.core.server.mysocket import Socket
from setting_reader import setting_res


class SocketClient(Socket):

    def __init__(self, host=setting_res.get("host"), port=setting_res.get("port")):
        """
        COUNT_OF_TRYING - количество попыток отправки одного пакета
        """
        self.COUNT_OF_TRYING = 5
        self.host = "192.168.0.103"
        self.port = 7777
        super().__init__(self.host, self.port, "client")

    def build_and_send_message(self, destination_ip, package):
        """
        @param: destination_ip: ip получателя пакета
        @param: package: пакет в виде набора байт
        @param: resending: отправляется ли пакет повторно
        """
        send_msg = package
        # Используйте этот сокет для кодирования того, что вы вводите, и отправьте его на этот адрес и
        # соответствующий порт

        # print("host\t" + self.host)
        # print("port\t" + str(self.port))

        # Декодировать полученную информацию

        back_msg = None

        tryingNum = 0
        while back_msg != '200':
            data = pickle.dumps(send_msg)
            self.soc.sendto(data, (self.host, self.port))

            self.soc.settimeout(5.0)

            back_msg = self.soc.recv(1024).decode('utf-8')

            tryingNum += 1
            # print("BACK:")
            # print(str(back_msg))

            self.soc.settimeout(None)

            if back_msg != '200':
                # print("\n400 ERROR to get response! try again...\n")

                if tryingNum == self.COUNT_OF_TRYING:
                    # print("\nSKIP PACKET\n")
                    return back_msg

            else:
                # print("\n200 SUCCESS!\n")
                return back_msg
