import asyncio
import threading
from time import sleep

import socket

from iter_two.taker.taker import Taker


class SocketClient:
    def __init__(self, host='192.168.0.101', port=7788):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__host = host
        self.__port = port
        self.__timeout = 60
        self.__addr = (self.__host, self.__port)

        self.taker = Taker()
        self.cache_socket = list()

    def build_and_send_message(self, destination_ip, package):
        """
        @param: destination_ip: ip получателя пакета
        @param: package: пакет в виде набора байт
        @param: resending: отправляется ли пакет повторно
        """
        self.socket.connect((self.__host, self.__port))

        msg = str(package)
        print("len_agr" + str(len(package)))
        msg = msg.replace("[", "[" + destination_ip + ", ", 1)

        self.cache_socket.append(msg)

        self.send_package()

    def send_package(self):
        for item in self.cache_socket:
            self.socket.sendto(item.encode('utf-8'), (self.__host, self.__port))

        d = self.socket.recvfrom(10240000000)
        reply = d[0]
        self.__addr = d[1]
        print('Server reply: ' + reply.decode('utf-8'))
        self.cache_socket.remove(self.cache_socket[0])

    def close_socket(self):
        self.socket.close()

