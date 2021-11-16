import asyncio
import threading
from time import sleep

import socket

from iter_two.taker.taker import Taker


class Socket:
    def __init__(self, taker_ip='192.168.0.101', taker_port=7777, controller_ip='192.168.0.100', controller_port=6666):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__taker_ip = taker_ip
        self.__taker_port = taker_port
        self.__controller_ip = controller_ip
        self.__controller_port = controller_port
        self.__timeout = 60
        self.__taker_addr = (self.__taker_ip, self.__taker_port)
        self.__controller_addr = (self.__controller_ip, self.__controller_port)

        self.taker = Taker()
        self.cache_socket = list()

    def run_listener_server(self):
        self.socket.bind(self.__controller_addr)

        while True:
            self.socket.settimeout(self.__timeout)
            try:
                d = self.socket.recvfrom(10240000000)
            except socket.timeout:
                print('Time is out. {0} seconds have passed'.format(self.__timeout))
                self.send_package()
                continue

            self.data_listener(d)

        self.socket.close()

    def build_and_send_message(self, destination_ip, package):
        """
        @param: destination_ip: ip получателя пакета
        @param: package: пакет в виде набора байт
        @param: resending: отправляется ли пакет повторно
        """
        msg = str(package)
        print("len_agr " + str(len(package)))
        msg = msg.replace("[", "[" + destination_ip + ", ", 1)

        self.cache_socket.append(msg)

        self.send_package()

    def send_package(self):
        for item in self.cache_socket:
            self.socket.sendto(item.encode('utf-8'), self.__addr)

        d = self.socket.recvfrom(10240000000)
        reply = d[0]
        #self.__addr = d[1]
        print('Server reply: ' + reply.decode('utf-8'))
        self.cache_socket.remove(self.cache_socket[0])

    def close_socket(self):
        self.socket.close()

    def data_listener(self, d):
        received = d[0]
        #self.__addr = d[1]

        self.taker.start(received)

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
        s2.build_and_send_message(destination_ip=msg, package=1241)

