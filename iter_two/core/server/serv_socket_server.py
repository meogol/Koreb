import asyncio
import threading
from time import sleep

import socket

from iter_two.core.server.socket import Socket
from iter_two.taker.taker import Taker
from setting_reader import setting_res


class SocketServer(Socket):
    def __init__(self, host=setting_res.get("host"), port=setting_res.get("port")):
        super().__init__(host, port)

        self.fwq.bind((self.host, self.port))

        self.taker = Taker()

    def run_listener_server(self):
        # Получать сообщения и адреса. Recvfrom используется для получения сообщений в UDP
        data, addr = self.fwq.recvfrom(10240000)
        # Декодировать полученное сообщение
        recvmsg = data.decode('utf-8')
        self.taker.start(recvmsg)

        replymsg = '2'
        self.fwq.sendto(replymsg.encode('utf-8'), addr)

    def data_listener(self, d):
        pass
