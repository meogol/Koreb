import random
import sys

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
        list_bytes = list(map(int, list_bytes))
        self.cache_manager.add_agr_cache(addr[0], package)

        if self.cache_manager.get_last_pkg_cache(addr[0]) is None:
            self.cache_manager.add_last_pkg_cache(addr[0], list_bytes)
            return
        else:
            last_pkg = self.cache_manager.get_last_pkg_cache(addr[0])
            res = self.recovery_pkg(list_bytes, last_pkg)

            wight = sys.getsizeof(res)
            print(wight)
            print(res)

    def recovery_pkg(self, package, last_pkg):
        """
        восстановление пакета
        @param last_pkg:
        @param package: передаваемый пакет. Передавать стоит в виде листа чисел
        @return: восстановленный пакет. Возвращается в виде листа чисел
        """

        filtered = list()
        for x in package:
            if x > 0:
                filtered.append(x)
            else:
                filtered.extend([-1]*x)

        last_index = 0
        new_pkg = list()
        pkg_i = None
        for index in filtered:
            pkg_i = index
            i = package[last_index:index - 1]

            new_pkg.extend(i)
            if last_index + len(i) < (-package[index]):
                p = last_pkg[last_index + len(i):-package[index]]
                new_pkg.extend(p)

            last_index = (-package[index])

        if pkg_i is not None and pkg_i < len(package):
            new_pkg.extend(package[pkg_i + 1:len(package)])
        elif pkg_i is None:
            new_pkg.extend(package)

        return new_pkg


if __name__ == '__main__':
    taker = Taker()

    items = list()
    add = 0
    for i in range(100):
        if i+add >= 100:
            break

        n = random.randint(0, 100)
        if 10 < n < 30:
            r = random.randint(3, 8)
            add += r

            items.append(-r)
        else:
            items.append(i+add)

    taker.recovery_pkg(items, [a for a in range(100)])
