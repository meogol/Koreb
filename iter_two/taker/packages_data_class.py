class PackagesData:
    def __init__(self):
        self.__isEnd = False
        self.__package = list()
        self.__number = 0
        self.__dst_ip = "ip"
        self.__package_int_load = 0
        self.__full_pkg_load = 0

    def add_to_data(self, pkg_number, package, is_end, load, full_pkg_load):
        self.__package = package
        self.__number = pkg_number
        self.__isEnd = is_end
        self.__package_int_load = load
        self.__full_pkg_load = full_pkg_load

    def get_isEnd(self):
        return self.__isEnd

    def get_dst_ip(self):
        return self.__dst_ip

    def get_number(self):
        return self.__number

    def get_pkg(self):
        return self.__package

    def get_load(self):
        return self.__package_int_load

    def get_full_load(self):
        return self.__full_pkg_load

    def set_load(self, load):
        self.__package_int_load = load
