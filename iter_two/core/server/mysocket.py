import socket

from setting_reader import setting_res


class Socket:
    def __init__(self, host=setting_res.get("taker_ip"), port=int(setting_res.get("port")), socket_type="server"):
        self.host = host
        self.port = port

        self.soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        if socket_type == "server":
            self.soc.bind((self.host, self.port))

    def getHost(self):
        return self.host

    def getPort(self):
        return self.port