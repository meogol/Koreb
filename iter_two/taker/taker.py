import pickle
import numpy as np
import scapy.all as scapy
import threading
import queue

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

    def check_n_send_pkg_from_stack(self, pkg_number, int_package, int_list, pkg_length_of_full_set_of_pkgs):
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

        while True:
            if self.stack.empty() != True:
                if pkg_number == -1:
                    is_end = True
                    int_list = self.stack.get()

                    self.packages_data.add_to_data(pkg_number, int_list, is_end, int_package)
                    pkg_list_for_sort.append(self.packages_data)

                else:
                    is_end = False
                    int_list = self.stack.get()

                    self.packages_data.add_to_data(pkg_number, int_list, is_end, int_package)
                    pkg_list_for_sort.append(self.packages_data)

                if len(pkg_list_for_sort) == pkg_length_of_full_set_of_pkgs:
                    pkg_list_for_sort = sorted(pkg_list_for_sort, key = lambda iter: iter.get_number())
                    pkg_list_for_sort.append(pkg_list_for_sort[0])
                    pkg_list_for_sort.remove(0)

                    i = 0
                    for item in pkg_list_for_sort:
                        pkg_buffer_list += item.get_pkg()
                        int_package += pkg_buffer_list[i] * 10 ** (len(pkg_buffer_list) - i - 1)
                        i += 1

                    byte_package = int_to_bytes(int_package)

                    print_logs(logs=self.logs, msg="INT LIST:\t\t" + str(int_list), log_type="debug")
                    print_logs(logs=self.logs, msg="INT PACKAGE:\t" + str(int_package), log_type="debug")
                    print_logs(logs=self.logs, msg="BYTE PACKAGE:\t" + str(byte_package), log_type="debug")

                    scapy_package = scapy.IP(byte_package)

                    send(scapy_package)



    def start(self, package):
        """
        запускает анализ пакета в тейкере
        @param package: пакет в виде числового байткода
        @return:
        """
        int_list = pickle.loads(package)
        """
        Протестить разаггрегатор!!!!!
        """
        scapy_packet = scapy.IP(package.get_payload())
        dst_ip = scapy_packet.sprintf("%IP.dst%")

        int_list = self.recovery_pkg(int_list, self.cache_manager.get_last_pkg_cache(dst_ip))

        pkg_number = int_list[len(int_list) - 2]
        pkg_length_of_full_set_of_pkgs = int_list[len(int_list) - 1]

        int_list = int_list.remove(len(int_list) - 1)
        int_list = int_list.remove(len(int_list) - 2)

        int_package = 0

        self.stack.put(int_list)
        self.check_n_send_pkg_from_stack(self, pkg_number, int_package, int_list, pkg_length_of_full_set_of_pkgs)

    def recovery_pkg(self, package, last_pkg):
        """
        восстановление пакета
        @param last_pkg: прошлый пакет, пришедший на определённый IP
        @param package: передаваемый пакет. Передавать стоит в виде листа чисел
        @return: восстановленный пакет. Возвращается в виде листа чисел
        """
        try:
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
                tail = this_pkg[len(last_pkg):]
                this_pkg = this_pkg[:len(last_pkg)]
            elif len(this_pkg) < len(last_pkg):
                last_pkg = last_pkg[:len(this_pkg)]

            new_pkg = np.where(this_pkg > 0, this_pkg, last_pkg)

            if len(tail) != 0:
                new_pkg = np.append(new_pkg, tail)

            return new_pkg
        except TypeError:
            print_logs(logs=self.logs, msg="RECOVERY ERROR!", log_type="exception")


def int_to_bytes(x: int) -> bytes:
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')


if __name__ == '__main__':
    take = Taker()
    pkg_number = 1
    int_package = 0
    van = [1, 2, 3, 4]
    pkg_leangth = 1
    pkg_length_of_full_set_of_pkgs = 2
    take.stack.put(van)
    take.stack.put(van)
    take.check_n_send_pkg_from_stack(pkg_number, int_package, van, pkg_leangth, pkg_length_of_full_set_of_pkgs)