import pickle
import numpy as np
from scapy.all import *
import scapy.all as scapy
from iter_two.core.cahce.cache import CacheManager
from logs import print_logs


class Taker:
    def __init__(self, logs={'to_log': True, 'to_console': True}):
        self.logs = logs
        self.cache_manager = CacheManager()

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
        for i in range(len(int_list)) :
            int_package += int_list[i] * 10**(len(int_list)-i-1)

        byte_package = int_to_bytes(int_package)

        print_logs(logs=self.logs, msg="INT LIST:\t\t" + str(int_list), log_type="debug")
        print_logs(logs=self.logs, msg="INT PACKAGE:\t" + str(int_package), log_type="debug")
        print_logs(logs=self.logs, msg="BYTE PACKAGE:\t" + str(byte_package), log_type="debug")

        scapy_package = scapy.IP(byte_package)
        send(scapy_package)

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

            if len(this_pkg) > len(last_pkg):
                prom_pkg = this_pkg[:len(last_pkg)]
            else:
                prom_pkg = this_pkg

            index_non_zero = [i for i in range(len(prom_pkg)) if prom_pkg[i] < 0]

            this_pkg[index_non_zero] = last_pkg[index_non_zero]

            new_pkg = this_pkg

            return new_pkg
        except TypeError:
            print_logs(logs=self.logs, msg="RECOVERY ERROR!", log_type="exception")


def int_to_bytes(x: int) -> bytes:
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')
