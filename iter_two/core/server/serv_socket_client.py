import logging
import queue
import socket
import pickle
import threading

import numpy

from iter_two.core.server.mysocket import Socket
from logs import print_logs
from setting_reader import setting_res


class SocketClient(Socket):

    def __init__(self, taker_ip, port,
                 logs={'to_log': True, 'to_console': True}):
        """
        COUNT_OF_TRYING - количество попыток отправки одного пакета
        """
        self.logs = logs
        self.COUNT_OF_TRYING = 5
        
        self.host = "192.168.0.103"
        self.port = 7777

        super().__init__(self.host, self.port, "client")

    def check_stack(self):
        i = 0
        cart_pkg = None
        while True:

            if self.stack.empty() and cart_pkg is None:
                continue

            if cart_pkg is None:
                cart_pkg = self.stack.get()

            back_msg = self.build_and_send_message(cart_pkg[0], cart_pkg[1])

            i += 1

            if back_msg == '200' or i == 5:
                cart_pkg = None
                i = 0

    def change_list(self, package, packages, last_slice_pos, slice_size, exceed, iterator):
        pkg_counter = 1

        for i in range(exceed + iterator):
            if pkg_counter == exceed + iterator: pkg_counter = -1

            packages[i].append(package[last_slice_pos: last_slice_pos + slice_size])
            packages[i].append(pkg_counter)
            packages[i].append(len(package)-2)
            last_slice_pos += slice_size
            pkg_counter += 1

        if last_slice_pos != len(package):
            packages.append(package[last_slice_pos: len(package) - last_slice_pos])

        return packages

    def check_package_list_size(self, package):
        """
        Метод проверяет входящий пакет на соответствие максимальной длине сокета. При несоответствии - разбивается так,
        чтобы в себе хранить отрезок определённой длины, номер, длину изначального пакета

        :param package:  Пакет для разбиения
        :return: Лист из листов, где каждый из них - часть изначального пакета, хранящего в конце:
            1) порядковый номер
            2) длину изначального пакета, который мы резали
        """
        packages = list()

        if len(package) >= 1200:
            last_slice_pos = 0

            exceed = round(len(package) / 1200)

            slice_size = round(len(package) / exceed + 1)

            if exceed == 1:
                packages = self.change_list(package, packages, last_slice_pos, slice_size, exceed, 1)

            else:
                packages = self.change_list(package, packages, last_slice_pos, slice_size, exceed, 0)

        else:
            packages.append(package)
            packages[0].append(-1)
            packages[0].append(len(package)-2)

        return packages

    def add_to_stack(self, destination_ip, package):
        self.stack.put((destination_ip, package))

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

        # print("host\t" + self.host)
        # print("port\t" + str(self.port))


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
                print_logs(logs=self.logs, msg="UNICODE ERROR!", log_type="exception")

            tryingNum += 1
            
            # print("BACK:")
            # print(str(back_msg))


            print_logs(logs=self.logs, msg="Response from taker:\t" + str(back_msg), log_type="debug")

            self.soc.settimeout(5)

            if back_msg != '200':
                # print("\n400 ERROR to get response! try again...\n")

                if tryingNum == self.COUNT_OF_TRYING:
                    # print("\nSKIP PACKET\n")

                    return back_msg

                else:
                    print_logs(logs=self.logs, msg="Trying to send again...\n", log_type="info")

            else:
              
                # print("\n200 SUCCESS!\n")

                return back_msg


if __name__ == '__main__':
    soc = SocketClient()
    package = list(range(1, 100))
    soc.check_package_list_size(package)
