import pickle
import numpy as np
import scapy.all as scapy
import threading
import queue
from scapy.layers.ipsec import IP
from iter_two.taker.packages_data_class import PackagesData
from scapy.all import *
from iter_two.core.cahce.cache import CacheManager
from logs import print_logs



class Taker:
    def __init__(self, logs={'to_log': True, 'to_console': True}):
        self.logs = logs
        self.cache_manager = CacheManager()
        self.stack = queue.LifoQueue(0)
        self.check_stack_thread = threading.Thread(target=self.check_n_send_pkg_from_stack)
        self.check_stack_thread.start()
        self.packages_data = PackagesData()

    def add_to_data(self, pkg_number, int_list, int_package, pkg_length_of_full_set_of_pkgs):
        if pkg_number == -1:
            is_end = True
            self.packages_data.add_to_data(pkg_number, int_list, is_end, int_package, pkg_length_of_full_set_of_pkgs)
            self.stack.put(self.packages_data)

        else:
            is_end = False
            self.packages_data.add_to_data(pkg_number, int_list, is_end, int_package, pkg_length_of_full_set_of_pkgs)
            self.stack.put(self.packages_data)

    def check_n_send_pkg_from_stack(self):
        """
        Метод циклично проверяет стек на наличие пришедших от serv_socket_client пакетов,
        после чего обрабатывает каждый пакет, последовательно вытаскивая из стека.
        Он собирает все пакеты в один, обрабатывает его и получает "payload", который и шлёт клиенту

        :param pkg_number: Порядковый номер пришедшего пакета
        :param int_package: Интовое число байт
        :param int_list: Пришедший пакет в виде листа значений типа инт
        :param pkg_length_of_full_set_of_pkgs: Длина изначального полного пакета
        :return:
        """
        is_end = False
        pkg_list_for_sort = list()
        pkg_buffer_list = list()
        summator = 0


        while True:
            if self.stack.empty() != True:
                pkg = self.stack.get()

                pkg_list_for_sort.append(pkg)

                for item in pkg_list_for_sort:
                    summator += len(item.get_pkg())

                if summator == pkg.get_full_load():
                    pkg_list_for_sort = sorted(pkg_list_for_sort, key = lambda iterator: iterator.get_number())
                    if len(pkg_list_for_sort) > 2:
                        pkg_list_for_sort = pkg_list_for_sort[1:] + pkg_list_for_sort[:0]

                    int_package=0
                    for item in pkg_list_for_sort:
                        pkg_buffer_list += item.get_pkg()

                    for i in range(len(pkg_buffer_list)):
                        int_package += pkg_buffer_list[i] * 10 ** (len(pkg_buffer_list) - i - 1)

                    byte_package = int_to_bytes(int_package)

                    print_logs(logs=self.logs, msg="INT LIST:\t\t" + str(pkg.get_pkg()), log_type="debug")
                    print_logs(logs=self.logs, msg="INT PACKAGE:\t" + str(int_package), log_type="debug")
                    print_logs(logs=self.logs, msg="BYTE PACKAGE:\t" + str(byte_package), log_type="debug")

                    scapy_package = scapy.IP(byte_package)

                    send(scapy_package)

                    summator = 0

    def start(self, package):
        """
        запускает анализ пакета в тейкере
        @param package: пакет в виде числового байткода
        @return:
        """
        int_list = pickle.loads(package)

        # print("int_pickle\t" + str(int_list))

        if self.cache_manager.get_last_pkg_cache('192.168.1.57') is not None:
            int_list = Taker.recovery_pkg(int_list, self.cache_manager.get_last_pkg_cache('192.168.1.57'))

        # print("int_list\t" + str(int_list))

        self.cache_manager.add_all_cache('192.168.1.57', int_list)

        if type(int_list) == numpy.ndarray:
            int_list = int_list.tolist()

        int_package = 0
        for i in range(len(int_list)):
            int_package += int_list[i] * 10 ** (len(int_list) - i - 1)

        # print("int_package\t" + str(int_package))


        byte_package = int_to_bytes(int_package)
        # print("byte_package\t" + str(byte_package))
        scapy_package = scapy.IP(byte_package)
        send(scapy_package)


    @staticmethod
    def recovery_pkg(package, last_pkg):
        """
        восстановление пакета
        @param last_pkg: прошлый пакет, пришедший на определённый IP
        @param package: передаваемый пакет. Передавать стоит в виде листа чисел
        @return: восстановленный пакет. Возвращается в виде листа чисел
        """


        filtered = list()
        for item in package:
            if item >= 0:
                filtered.append(item)
            else:
                filtered.extend([-1] * -item)

        this_pkg = np.array(filtered)
        last_pkg = np.array(last_pkg)

        tail = []
        if len(this_pkg) > len(last_pkg):
            tail = this_pkg[len(last_pkg+1):]
            this_pkg = this_pkg[:len(last_pkg)]
        elif len(this_pkg) < len(last_pkg):
            last_pkg = last_pkg[:len(this_pkg)]

        new_pkg = np.where(this_pkg >= 0, this_pkg, last_pkg)

        if len(tail) != 0:
            new_pkg = np.append(new_pkg, tail)
        return new_pkg


def int_to_bytes(x: int) -> bytes:
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')


if __name__ == '__main__':
    take = Taker()
    pkg_number = 1
    int_package = 0
    van = [1, 2, 3, 4]
    pkg_leangth = 1
    pkg_length_of_full_set_of_pkgs = 1
    take.stack.put(van)
    take.check_n_send_pkg_from_stack(pkg_number, int_package, van, pkg_length_of_full_set_of_pkgs)