import numpy as np

from iter_two.core.cahce.cache import CacheManager
from iter_two.taker.taker import Taker


class Aggregator:
    def __init__(self, cache_manager):
        self.cache_manager = cache_manager

    def contrast_last_package(self, package, destination_ip):
        if self.cache_manager.get_last_pkg_cache(destination_ip) is not None:
            lp = np.array(self.cache_manager.get_last_pkg_cache(destination_ip))
            p = np.array(package)
            lp_len = len(lp)
            p_len = len(package)
            tail = []

            if lp_len == p_len:
                diff = abs(np.subtract(lp, p))
            elif lp_len > p_len:
                lp = lp[:p_len]
                diff = abs(np.subtract(lp, p))
            else:
                tail = p[lp_len:]
                p = p[:lp_len]
                diff = abs(np.subtract(lp, p))

            if np.nonzero(diff)[0].size == len(diff):
                if len(tail) != 0:
                    return list(p) + list(tail)
                else:
                    return list(p)
            elif np.nonzero(diff)[0].size == 0:
                p = [-len(diff)]
                if len(tail) != 0:
                    return list(p) + list(tail)
                else:
                    return list(p)
            else:
                nz = np.nonzero(diff)[0]
                prev = None
                slices = []
                if nz[0] != 0:
                    slices.append([0, nz[0]])
                for i in nz:
                    if prev is None:
                        prev = i
                    else:
                        if i - prev >= 2:
                            slices.append([prev + 1, i])
                            prev = i
                        else:
                            prev = i
                if nz[-1] + 1 != len(diff):
                    slices.append([nz[-1] + 1, len(diff)])

                p = list(p)
                shift = 0

                for i in slices:
                    p[i[0] - shift:i[1] - shift] = [-(i[1] - i[0])]
                    shift += (i[1] - i[0] - 1)

                if len(tail) != 0:
                    return list(p) + list(tail)
                else:
                    return list(p)


if __name__ == '__main__':
    package = [0, 12, 123, 35, 0, 0, 0, 5, 3, 5, 7, 3, 2, 67, 243, 34, 6, 87, 86]
    cache_manager = CacheManager()
    p = [0, 45, 456, 45, 23, 56, 12, 123, 35, 0, 0, 0, 5, 3, 5, 7, 3, 2, 435, 5, 88, 93, 67, 243, 34, 6, 87, 86]
    print(package)
    cache_manager.add_last_pkg_cache("192.168.0.106", p)
    aggregator = Aggregator(cache_manager)
    package = aggregator.contrast_last_package(package, "192.168.0.106")
    print(package)
    taker = Taker()
    package = taker.recovery_pkg(package, p)
    print(package)