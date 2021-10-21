from iter_two.core.server.server import Server


class Controller:
    def __init__(self):
        self.server = Server()

    def analyse_command(self, package):
        self.server.send_package(package)
