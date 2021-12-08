import logging
import socket
import pickle
import numpy

from iter_two.core.server.mysocket import Socket
from logs import print_logs
from setting_reader import setting_res


class SocketClient(Socket):

    def __init__(self, taker_ip=setting_res.get("taker_ip"), port=setting_res.get("port"), logs={'to_log':True, 'to_console': True}):
        """
        COUNT_OF_TRYING - количество попыток отправки одного пакета
        """
        self.logs = logs
        self.COUNT_OF_TRYING = 5
        self.taker_ip = taker_ip
        self.port = port
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

        print_logs(logs=self.logs, msg="TAKER's IP:\t" + self.taker_ip, log_type="debug")
        print_logs(logs=self.logs, msg="TAKER's PORT:\t" + str(self.port), log_type="debug")

        # Декодировать полученную информацию

        back_msg = None

        tryingNum = 0

        while back_msg != '200':
            data = pickle.dumps(send_msg)


            self.soc.sendto(data, (self.taker_ip, self.port))

            self.soc.settimeout(5.0)

            try:
                back_msg = self.soc.recv(1024).decode('utf-8')
            except UnicodeError:
                print_logs(logs=self.logs, msg="UNICODE ERROR!", log_type="exception")

            tryingNum += 1

            print_logs(logs=self.logs, msg="Response from taker:\t" + str(back_msg), log_type="debug")

            self.soc.settimeout(None)

            if back_msg != '200':
                print_logs(logs=self.logs, msg="400 ERROR to get response!", log_type="exception")

                if tryingNum == self.COUNT_OF_TRYING:
                    print_logs(logs=self.logs, msg="PACKAGE WAS SKIPED\n", log_type="info")

                    return back_msg

                else:
                    print_logs(logs=self.logs, msg="Trying to send again...\n", log_type="info")

            else:
                print_logs(logs=self.logs, msg="200 SUCCESS! Package was sent successfully.\n", log_type="info")
                return back_msg
