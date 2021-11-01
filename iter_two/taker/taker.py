import random
import sys
import numpy as np
from scapy.sendrecv import send
from iter_two.core.cahce.cache import CacheManager


class Taker:
    def __init__(self):
        self.cache_manager = CacheManager()

    def start(self, package):
        """
        запускает анализ пакета в тейкере
        @param package: пакет в виде числового байткода
        @param addr: кортеж вида (ip, port)
        @return:
        """

        list_bytes = str(package)[3:len(str(package)) - 2].replace(' ', '').split(',')
        destination_ip = list_bytes[0]  # ip получателя пакета
        list_bytes = list(map(bytes, map(int, list_bytes[1:])))

        print(list_bytes)

        if self.cache_manager.get_last_pkg_cache(destination_ip) is None:
            self.cache_manager.add_last_pkg_cache(destination_ip, list_bytes)
            self.to_send(list_bytes)
            return
        else:
            last_pkg = self.cache_manager.get_last_pkg_cache(destination_ip)
            res = self.recovery_pkg(list_bytes, last_pkg)

            self.cache_manager.add_agr_cache(destination_ip, res)

            print(len(res))
            print(res)
            print("________________")

            self.to_send(res)

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
            prom_pkg = last_pkg * this_pkg[:len(last_pkg)]
            last = this_pkg[len(last_pkg):]
        else:
            prom_pkg = last_pkg[:len(this_pkg)] * this_pkg

        index_non_zero = np.unique(np.where(prom_pkg < 0)[0])

        this_pkg[index_non_zero] = last_pkg[index_non_zero]

        new_pkg = np.concatenate((this_pkg, last))

        return new_pkg

    def to_send(self, package):
        send(package)

if __name__ == '__main__':
    taker = Taker()

    pkg = ['162.159.135.234', 75, 612, 501, 533, 233, 550, 355, 6, 170, 853, 554, 5, 195, 475, 34, 958, 351, 723, 789, 784, 423, 901, 320, 601, 502]
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
