import numpy
import numpy as np

from iter_two.core.cahce.cache import CacheManager
from iter_two.taker.taker import Taker


class Aggregator:
    def __init__(self, cache_manager):
        self.cache_manager = cache_manager

    def contrast_last_package(self, package, destination_ip):
        # print("Contrast")
        if self.cache_manager.get_last_pkg_cache(destination_ip) is not None:
            last_pkg = numpy.array(self.cache_manager.get_last_pkg_cache(destination_ip))
            this_pkg = numpy.array(package)
            last_pkg_len = len(last_pkg)
            this_pkg_len = len(package)
            tail = []

            if last_pkg_len > this_pkg_len:
                last_pkg = last_pkg[:this_pkg_len]

            elif last_pkg_len < this_pkg_len:
                tail = this_pkg[last_pkg_len:]
                this_pkg = this_pkg[:last_pkg_len]

            diff = numpy.subtract(last_pkg, this_pkg)

            nonzero_size = numpy.nonzero(diff)[0].size

            if nonzero_size == 0:
                this_pkg = [-len(diff)]

            elif nonzero_size != len(diff):
                nonzero = numpy.nonzero(diff)[0]
                prev = None

                this_pkg = list(this_pkg)
                shift = 0

                if nonzero[0] != 0:
                    this_pkg[0 - shift:nonzero[0] - shift] = [- nonzero[0]]
                    shift += (nonzero[0] - 1)

                for i in nonzero:
                    if prev is not None and i - prev >= 2:
                        this_pkg[prev + 1 - shift:i - shift] = [- i + prev + 1]
                        shift += (i - prev - 2)
                    prev = i

                if nonzero[-1] + 1 != len(diff):
                    this_pkg[nonzero[-1] + 1 - shift:len(diff) - shift] = [- len(diff) + nonzero[-1] + 1]
                    shift += (len(diff) - nonzero[-1] - 2)

            if len(tail) != 0:
                return list(this_pkg) + list(tail)
            else:
                return list(this_pkg)


if __name__ == '__main__':
    package = [0, 12, 123, 35, 0, 0, 0, 5, 3, 5, 7, 3, 2, 67, 243, 34, 6, 87, 86]
    cache_manager = CacheManager()
    p = [0, 45, 456, 45, 23, 56, 12, 123, 35, 0, 0, 0, 5, 3, 5, 7, 3, 2, 435, 5, 88, 93, 67, 243, 34, 6, 87, 86]
    print(package)
    aggregator = Aggregator(cache_manager)
    package = aggregator.contrast_last_package(package, "192.168.0.106")
    print(package)
    taker = Taker()
    package = taker.recovery_pkg(package, p)
    print(package)