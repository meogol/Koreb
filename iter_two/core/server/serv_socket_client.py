import logging
import socket
import pickle
import numpy

from iter_two.core.server.mysocket import Socket
from logs import print_logs
from setting_reader import setting_res


class SocketClient(Socket):

    def __init__(self, taker_ip=setting_res.get("taker_ip"), port=setting_res.get("port"),
                 logs={'to_log': True, 'to_console': True}):
        """
        COUNT_OF_TRYING - количество попыток отправки одного пакета
        """
        self.logs = logs
        self.COUNT_OF_TRYING = 5
        self.taker_ip = taker_ip
        self.port = port
        super().__init__(self.host, self.port, "client")

    def check_package_list_size(self, package):
        """
        Метод проверяет входящий пакет на соответствие максимальной длине сокета. При несоответствии - разбивается так,
        чтобы в себе хранить отрезок определённой длины, номер, длину среза, длину изначального пакета

        :param package:  Пакет для разбиения
        :return: Лист из листов, где каждый из них - часть изначального пакета, хранящего в конце:
            1) порядковый номер
            2) длину среза изначального пакета
            3) длину изначального пакета, который мы резали
        """
        packages = list()

        if len(package) >= 2000:
            exceed = round(len(package) / 20)

            last_slice_pos = 0
            pkg_counter = 1

            slice_size = round(len(package) / exceed + 1)

            if exceed == 1:
                for i in range(exceed + 1):
                    if pkg_counter == exceed + 1: pkg_counter = -1

                    packages.append(package[last_slice_pos: last_slice_pos + slice_size])
                    packages[i].append(pkg_counter)
                    packages.append(len(package[last_slice_pos: last_slice_pos + slice_size]))
                    packages[i].append(len(package))
                    last_slice_pos += slice_size
                    pkg_counter += 1

                if last_slice_pos != len(package):
                    packages.append(package[last_slice_pos: len(package) - last_slice_pos])


            else:
                for i in range(exceed):
                    if pkg_counter == exceed: pkg_counter = -1

                    packages.append(package[last_slice_pos: last_slice_pos + slice_size])
                    packages[i].append(pkg_counter)
                    packages[i].append(len(package[last_slice_pos: last_slice_pos + slice_size]))
                    packages[i].append(len(package))
                    last_slice_pos += slice_size
                    pkg_counter += 1

                if last_slice_pos != len(package):
                    packages.append(package[last_slice_pos: len(package) - last_slice_pos])


        else:
            packages[0].append(package)
            packages[0].append(-1)
            packages[0].append(len(package))

        return packages

    def build_and_send_message(self, destination_ip, package):
        """
        @param: destination_ip: ip получателя пакета
        @param: package: пакет в виде набора байт
        @param: resending: отправляется ли пакет повторно
        """
        message_to_send = package
        message_to_send = self.check_package_list_size(message_to_send)

        # Используйте этот сокет для кодирования того, что вы вводите, и отправьте его на этот адрес и
        # соответствующий порт

        print_logs(logs=self.logs, msg="TAKER's IP:\t" + self.taker_ip, log_type="debug")
        print_logs(logs=self.logs, msg="TAKER's PORT:\t" + str(self.port), log_type="debug")

        # Декодировать полученную информацию

        back_msg = None

        tryingNum = 0

        i = 0
        while (back_msg != '200') and (i < len(message_to_send)):
            data = pickle.dumps(message_to_send[i])

            i += 1

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


if __name__ == '__main__':
    soc = SocketClient()
    package = list(range(1, 100))
    soc.check_package_list_size(package)
