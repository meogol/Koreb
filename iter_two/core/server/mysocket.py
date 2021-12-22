import socket

from setting_reader import setting_res


class Socket:
    def __init__(self, host=setting_res.get("host"), port=setting_res.get("port"), socket_type="server"):
        self.host = '192.168.1.110'
        self.port = 7777
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        if socket_type == "server":
            self.soc.bind((self.host, self.port))

    def getHost(self):
        return self.host

    def getPort(self):
        return self.port