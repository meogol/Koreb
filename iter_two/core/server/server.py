import threading

from iter_two.core.server.serv_socket import Socket


class Server:
    def __init__(self, host='localhost', port=7777):
        self.socket = Socket(host=host, port=port)

    def init_listener_thread(self):
        t = threading.Thread(target=self.socket.run_listener_server)
        t.start()
