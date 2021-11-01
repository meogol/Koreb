import asyncio
import threading
from time import sleep

import socket

from iter_two.taker.taker import Taker


class Socket:
    def __init__(self, host='localhost', port=7777 ):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__host = host
        self.__port = port
        self.__timeout = 60
        self.__addr = (self.__host, self.__port)

        self.taker = Taker()
        self.send_again_cache = list()

    def cache_fill(self, package):
        self.send_again_cache.append(package)

    def cache_clearing(self, package):
        self.send_again_cache.remove(package)

    def run_listener_server(self):
        self.socket.bind(self.__addr)

        while True:
            self.socket.settimeout(self.__timeout)
            try:
                d = self.socket.recvfrom(1024000)
            except socket.timeout:
                print('Time is out. {0} seconds have passed'.format(self.__timeout))
                continue

            self.data_listener(d)

        self.socket.close()

    def send_package(self, destination_ip, package):
        """
        @param: destination_ip: ip получателя пакета
        @param: package: пакет в виде набора байт
        """
        msg = str(package)
        msg = msg.replace("[", "[" + destination_ip + ", ", 1)

        self.socket.sendto(msg.encode('utf-8'), (self.__host, self.__port))

        d = self.socket.recvfrom(102400)
        reply = d[0]
        self.__addr = d[1]
        print('Server reply: ' + reply.decode('utf-8'))

    def close_socket(self):
        self.socket.close()

    def data_listener(self, d):
        received = d[0]
        self.__addr = d[1]

        self.taker.start(received, self.__addr)

        msg = "200"
        self.socket.sendto(msg.encode('utf-8'), self.__addr)


if __name__ == '__main__':
    s1 = Socket()
    s2 = Socket(port=7777)

    t = threading.Thread(target=s1.run_listener_server)
    t.start()

    sleep(1)
    while True:
        msg = input("your message:")
        s2.send_package(destination_ip=msg)

