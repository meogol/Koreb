from iter_two.core.server.server import Server


class Taker:
    def __init__(self):
        self.server = Server()

    def start(self):
        self.server.init_listener()
