import logging
import socket
import pickle
import numpy

from iter_two.core.server.mysocket import Socket
from setting_reader import setting_res


class SocketClient(Socket):

    def __init__(self, host=setting_res.get("taker_ip"), port=int(setting_res.get("port"))):
        """
        COUNT_OF_TRYING - количество попыток отправки одного пакета
        """
        self.TO_LOG = TO_LOG
        self.TO_CONSOLE = TO_CONSOLE
        self.COUNT_OF_TRYING = 5
        self.host = host
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

        if self.TO_LOG:
            logging.debug("TAKER's IP:\t" + self.host)
            logging.debug("TAKER's PORT:\t" + str(self.port))

        if self.TO_CONSOLE:
            print("host\t" + self.host)
            print("port\t" + str(self.port))

        # Декодировать полученную информацию

        back_msg = None

        tryingNum = 0

        while back_msg != '200':
            data = pickle.dumps(send_msg)


            self.soc.sendto(data, (self.host, self.port))

            self.soc.settimeout(5.0)

            try:
                back_msg = self.soc.recv(1024).decode('utf-8')
            except UnicodeError:
                if self.TO_LOG:
                    logging.exception("UNICODE ERROR!")
                if self.TO_CONSOLE:
                    print("Unicode Error")

            tryingNum += 1

            if self.TO_LOG:
                logging.debug("Response from taker:\t" + str(back_msg))
            if self.TO_CONSOLE:
                print("BACK:")
                print(str(back_msg))

            self.soc.settimeout(None)

            if back_msg != '200':
                if self.TO_LOG:
                    logging.exception("400 ERROR to get response!")
                if self.TO_CONSOLE:
                    print("\n400 ERROR to get response! try again...\n")

                if tryingNum == self.COUNT_OF_TRYING:

                    if self.TO_LOG:
                        logging.info("PACKAGE WAS SKIPED\n")
                    if self.TO_CONSOLE:
                        print("\nPACKAGE WAS SKIPED\n")

                    return back_msg

                else:
                    if self.TO_LOG:
                        logging.info("Trying to send again...\n")

            else:
                if self.TO_LOG:
                    logging.info("200 SUCCESS!\n")
                if self.TO_CONSOLE:
                    print("\n200 SUCCESS!\n")
                return back_msg
