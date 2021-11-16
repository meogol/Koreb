import asyncio
import threading
from time import sleep

import socket

from iter_two.taker.taker import Taker


class SocketListener:
    def __init__(self, host='192.168.0.101', port=7788):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__host = host
        self.__port = port
        self.__timeout = 60
        self.__addr = (self.__host, self.__port)

        self.taker = Taker()
        self.cache_socket = list()

    def run_listener_server(self):
        self.socket.bind(self.__addr)

        while True:
            try:
                d = self.socket.recvfrom(10240000000)
            except socket.timeout:
                print('Time is out. {0} seconds have passed'.format(self.__timeout))
                # self.send_package()
                continue

            self.data_listener(d)

        self.socket.close()

    def close_socket(self):
        self.socket.close()

    def data_listener(self, d):
        received = d[0]
        self.__addr = d[1]

        self.taker.start(received)

        msg = "200"
        self.socket.sendto(msg.encode('utf-8'), self.__addr)
