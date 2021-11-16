import asyncio
import threading
from time import sleep

import socket

from iter_two.taker.taker import Taker


class SocketListener:
    def __init__(self, host='192.168.0.101', port=7777):
        self.host = host
        self.port = port
        self.fwq = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.fwq.bind((host, port))

    def run_listener_server(self):
        while 1:
            # Получать сообщения и адреса. Recvfrom используется для получения сообщений в UDP
            data, addr = self.fwq.recvfrom(1024)
            # Декодировать полученное сообщение
            recvmsg = data.decode('utf-8')
            # Условия завершения цикла while
            if recvmsg == 'q':
                print("Другой участник добровольно закончил чат с тобой, пока!")
                break
            # Распечатать декодированное сообщение
            print('client msg:' + recvmsg)
            replymsg = input('Ответить:')
            # Отправка сообщения, на которое вы хотите ответить, отправка полученному адресу, отправка в UDP также
            # использует sendto
            self.fwq.sendto(replymsg.encode('utf-8'), addr)

        self.fwq.close()

    def data_listener(self, d):
        pass
