from setting_reader import setting_res


class Socket:
    def __init__(self, host=setting_res.get("host"), port=setting_res.get("port")):
        self.host = host
        self.port = port

    def getHost(self):
        return self.host

    def getPort(self):
        return self.port