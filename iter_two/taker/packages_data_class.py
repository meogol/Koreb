class PackagesData:
    def __init__(self):
        self.__isEnd = False
        self.__package = list()
        self.__number = 0
        self.__dst_ip = "ip"

    def add_to_data(self, pkg_number, package, is_end):
        self.__package.append(package)
        self.__number = pkg_number
        self.__isEnd = is_end

    def get_isEnd(self):
        return self.__isEnd

    def get_dst_ip(self):
        return self.__dst_ip

    def get_number(self):
        return self.__number

    def get_pkg(self):
        return self.__package