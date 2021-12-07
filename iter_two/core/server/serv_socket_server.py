import asyncio
import threading
from random import randint
from time import sleep

import socket

from iter_two.core.server.mysocket import Socket
from iter_two.taker.taker import Taker
from setting_reader import setting_res


class SocketServer(Socket):
    def __init__(self, taker_ip=setting_res.get("taker_ip"), port=setting_res.get("port"), TO_LOG=True, TO_CONSOLE=True):
        super().__init__(taker_ip, port, "server")
        self.TO_LOG = TO_LOG
        self.TO_CONSOLE = TO_CONSOLE
        self.taker = Taker(TO_LOG=TO_LOG, TO_CONSOLE=TO_CONSOLE)

    def run_listener_server(self):
        while True:
            # Получать сообщения и адреса. Recvfrom используется для получения сообщений в UDP
            data, addr = self.soc.recvfrom(10240000)
            # Декодировать полученное сообщение
            recvmsg = data
            self.taker.start(recvmsg)

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
