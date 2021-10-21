from iter_two.core.server.creator_package import CreatorPackage
from iter_two.core.server.socket import Socket


class Server:
    def __init__(self):
        self.socket = Socket()

    def init_listener(self):
        self.socket.data_listener()



