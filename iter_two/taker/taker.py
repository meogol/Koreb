import random
import sys
import numpy as np
from iter_two.core.cahce.cache import CacheManager


class Taker:
    def __init__(self):
        self.cache_manager = CacheManager()

    def start(self, package, addr):
        """
        запускает анализ пакета в тейкере
        @param package: пакет в виде числового байткода
        @param addr: кортеж вида (ip, port)
        @return:
        """

        list_bytes = str(package)[3:len(str(package)) - 2].replace(' ', '').split(',')
        destination_ip = list_bytes[0]  # ip получателя пакета
        list_bytes = list(map(int, list_bytes[1:]))

        if self.cache_manager.get_last_pkg_cache(destination_ip) is None:
            self.cache_manager.add_all_cache(destination_ip, list_bytes)
            return

        last_pkg = self.cache_manager.get_last_pkg_cache(destination_ip)
        res = self.recovery_pkg(list_bytes, last_pkg)
        print("len_res" + str(len(res)))
        print()

        self.cache_manager.add_all_cache(destination_ip, res)

    def recovery_pkg(self, package, last_pkg):
        """
        восстановление пакета
        @param last_pkg:
        @param package: передаваемый пакет. Передавать стоит в виде листа чисел
        @return: восстановленный пакет. Возвращается в виде листа чисел
        """

        filtered = list()
        for x in package:
            if x >= 0:
                filtered.append(x)
            else:
                filtered.extend([-1] * -x)

        this_pkg = np.array(filtered)
        last_pkg = np.array(last_pkg)

        last = []
        if len(this_pkg) > len(last_pkg):
            prom_pkg = this_pkg[:len(last_pkg)]
            last = this_pkg[len(last_pkg):]
        else:
            prom_pkg = this_pkg

        index_non_zero = [i for i in range(len(prom_pkg)) if prom_pkg[i] < 0]

        this_pkg[index_non_zero] = last_pkg[index_non_zero]

        new_pkg = this_pkg

        return new_pkg

    def to_send(self, dst_ip, package):
        package = bytes(package)
        pkt = IP(dst=dst_ip)/TCP(dport=7777)/Raw(package)
        #bytes(pkt)
        print(pkt)
        send(pkt)

if __name__ == '__main__':
    taker = Taker()

    pkg = ['192.168.0.106', 75, 1, 250]

    while True:
        taker.start(pkg)

    items = list()
    add = 0
    for i in range(100):
        if i + add >= 95:
            break

        n = random.randint(0, 100)
        if 10 < n < 30:
            r = random.randint(3, 8)
            add += r

            items.append(-r - 1)
        else:
            items.append(i + add)

    taker.recovery_pkg(items, [a for a in range(100)])
