from iter_two.core.server.creator_package import CreatorPackage


class Socket:
    def __init__(self):
        pass

    def send_package(self, package):
        pass

    def data_listener(self):
        data = ""
        CreatorPackage.create_package(data)
