import asyncio
import threading
from time import sleep

from iter_two.core.server.creator_package import CreatorPackage
import socket


class Socket:
    def __init__(self, host='localhost', port=7777 ):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__host = host
        self.__port = port
        self.__timeout = 60
        self.__addr = (self.__host, self.__port)

    def run_listener_server(self):
        self.socket.bind(self.__addr)

        while True:
            print('Waiting for data ({0} seconds)...'.format(self.__timeout))
            self.socket.settimeout(self.__timeout)
            try:
                d = self.socket.recvfrom(1024)
            except socket.timeout:
                print('Time is out. {0} seconds have passed'.format(self.__timeout))
                continue

            self.data_listener(d)

        self.socket.close()

    def send_package(self, package="fhj "):
        msg = package
        self.socket.sendto(msg.encode('utf-8'), (self.__host, self.__port))

        d = self.socket.recvfrom(1024)
        reply = d[0]
        self.__addr = d[1]
        print('Server reply: ' + reply.decode('utf-8'))

    def close_socket(self):
        self.socket.close()

    def data_listener(self, d):
        received = d[0]
        self.__addr = d[1]
        print('Received data: ', received)
        print('From: ', self.__addr)

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
        s2.send_package(msg)

