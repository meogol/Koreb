class PackagesData:
    def __init__(self):
        self.__isEnd = False
        self.__packages = list()
        self.__dst_ip = "ip"

    def add_to_data(self, pkg_number, package, is_end):
        self.__packages.append(pkg_number)
        self.__packages.append(package)
        self.__isEnd = is_end