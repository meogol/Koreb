import pickle
import numpy as np
import scapy.all as scapy
import threading

from iter_two.taker.packages_data_class import PackagesData
from scapy.all import *
from iter_two.core.cahce.cache import CacheManager
from logs import print_logs
from queue import LifoQueue


class Taker:
    def __init__(self, logs={'to_log': True, 'to_console': True}):
        self.logs = logs
        self.cache_manager = CacheManager()
        self.stack = LifoQueue()
        self.check_stack_thread = threading.Thread(target=self.check_n_send_pkg_from_stack)
        self.check_stack_thread.start()
        self.packages_data= PackagesData()

    def check_n_send_pkg_from_stack(self, pkg_number, int_package, int_list):
        is_end = False

        while True:
            if self.stack.get() is not None:
                if pkg_number == 
                self.packages_data.add_to_data(pkg_number, int_package, is_end)






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
        int_package = 0
        for i in range(len(int_list)):
            int_package += int_list[i] * 10 ** (len(int_list) - i - 1)

        pkg_number = int_package[len(int_package) - 1]
        int_package = int_package.remove(len(package) - 1)

        self.stack.put(int_list)
        self.check_n_send_pkg_from_stack(self, pkg_number, int_package, int_list)

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
    last = [0, 132, 123, 35, 0, 0, 0, 5, 3, 5, 7, 3, 22, 167, 23, 134, 6, 27, 86]
    pkg = [20, 12, -4, 40, -5, 2, 67, 243, 34, 26, 87, 186, 12, 42, 534]
    t = Taker()
    print(t.recovery_pkg(pkg, last))
