from iter_two.core.server.serv_socket_client import SocketClient
from iter_two.core.server.serv_socket_server import SocketServer
from iter_two.core.server.mysocket import Socket
from iter_two.core.server.server import Server
from setting_reader import setting_res, setting_read

import threading

async def async_func(text):
    server = Server()
    server.init_listener()
    a = SocketClient.build_and_send_message(package=text, destination_ip='localhost')
    return a

def test_socket():
    text = [0, 132, 123, 35, 0, 0, 0, 5, 3, 5, 7, 3, 22, 167, 23, 134, 6, 27, 86]
    returned_text = async_func(text)
    print("Это этот вывод", returned_text)
    assert "200" == returned_text()