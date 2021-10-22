import random
import sys


class Taker:
    def __init__(self):
        self.last_packages = None

    def start(self, package, addr):
        list_bytes = str(package)[3:len(str(package)) - 2].replace(' ', '').split(',')
        list_bytes = list(map(int, list_bytes))

        if self.last_packages is None:
            self.last_packages = list_bytes
            return

        res = self.recovery_pkg(list_bytes)

        wight = sys.getsizeof(res)
        print(wight)
        print(res)

    def recovery_pkg(self, package):
        """
        @param package: передаваемый пакет. Передавать стоит в виде листа чисел
        @return: восстановленный пакет. Возвращается в виде листа чисел
        """

        if self.last_packages is None:
            self.last_packages = package
            return

        filtered = [idx for idx, p in enumerate(package) if p < 0]

        last_index = 0
        new_pkg = list()
        pkg_i = None
        for index in filtered:
            pkg_i = index
            i = package[last_index:index-1]

            new_pkg.extend(i)
            if last_index + len(i) < (-package[index]):
                p = self.last_packages[last_index + len(i):-package[index]]
                new_pkg.extend(p)

            last_index = (-package[index])

        if pkg_i is not None and pkg_i < len(package):
            new_pkg.extend(package[pkg_i+1:len(package)])
        elif pkg_i is None:
            new_pkg.extend(package)

        return new_pkg


if __name__ == '__main__':
    taker = Taker()

    for a in range(100, 1000):
        item = [x for x in range(a)]
        new_list = item

        last = random.randint(2, 5)
        last1 = random.randint(last, 10)
        if a > 100:
            new_list = list()
            for b in range(100):
                rand = random.randint(last1, last1 + 10)
                rand1 = random.randint(rand, rand + 5)

                if b == 0:
                    new_list.extend(item[:rand])
                    last = rand
                    last1 = rand1
                    continue

                if rand > len(item):
                    new_list.extend(item[last:len(item)])
                    break

                new_list.append(-last1)
                new_list.extend(item[last1:rand])

                last = rand
                last1 = rand1

        taker.recovery_pkg(new_list)
