import asyncio
import threading
from random import randint
from time import sleep

import socket

from iter_two.core.server.mysocket import Socket
from iter_two.taker.taker import Taker
from setting_reader import setting_res


class SocketServer(Socket):
    def __init__(self, host=setting_res.get("host"), port=setting_res.get("port")):
        host = "192.168.1.110"
        port = 7777
        super().__init__(host, port, "server")
        self.taker = Taker()

    def run_listener_server(self):
        while True:
            # Получать сообщения и адреса. Recvfrom используется для получения сообщений в UDP
            data, addr = self.soc.recvfrom(8192)
            # Декодировать полученное сообщение
            recvmsg = data
            self.taker.add_stack(recvmsg)

            replymsg = '200'

            """
            Для отладки обратной связи
            
            if randint(0, 3) == 1:
                replymsg = '200'
            else:
                replymsg = '400'
            """

            self.soc.sendto(replymsg.encode('utf-8'), addr)


    def data_listener(self, d):
        pass
