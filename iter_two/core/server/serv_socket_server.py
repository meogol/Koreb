import asyncio
import threading
from time import sleep

import socket

from iter_two.taker.taker import Taker


class SocketServer:
    def __init__(self, host='192.168.0.101', port=7777):
        self.host = host
        self.port = port
        self.fwq = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.fwq.bind((host, port))

        self.taker = Taker()

    def run_listener_server(self):
        while 1:
            # Получать сообщения и адреса. Recvfrom используется для получения сообщений в UDP
            data, addr = self.fwq.recvfrom(10240000)
            # Декодировать полученное сообщение
            recvmsg = data.decode('utf-8')
            self.taker.start(recvmsg)

            replymsg = '2'
            self.fwq.sendto(replymsg.encode('utf-8'), addr)

        self.fwq.close()

    def data_listener(self, d):
        pass


if __name__ == '__main__':
    s = SocketServer()
    s.run_listener_server()
