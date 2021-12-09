import numpy as np

from iter_two.core.cahce.cache import CacheManager
from iter_two.taker.taker import Taker


class Aggregator:
    def __init__(self, cache_manager):
        self.cache_manager = cache_manager

    def contrast_last_package(self, package, destination_ip):
        if self.cache_manager.get_last_pkg_cache(destination_ip) is not None:
            last_pkg = np.array(self.cache_manager.get_last_pkg_cache(destination_ip))
            this_pkg = np.array(package)
            last_pkg_len = len(last_pkg)
            this_pkg_len = len(package)
            tail = []

            if last_pkg_len == this_pkg_len:
                diff = abs(np.subtract(last_pkg, this_pkg))
            elif last_pkg_len > this_pkg_len:
                last_pkg = last_pkg[:this_pkg_len]
                diff = abs(np.subtract(last_pkg, this_pkg))
            else:
                tail = this_pkg[last_pkg_len:]
                this_pkg = this_pkg[:last_pkg_len]
                diff = abs(np.subtract(last_pkg, this_pkg))

            if np.nonzero(diff)[0].size == len(diff):
                if len(tail) != 0:
                    return list(this_pkg) + list(tail)
                else:
                    return list(this_pkg)
            elif np.nonzero(diff)[0].size == 0:
                this_pkg = [-len(diff)]
                if len(tail) != 0:
                    return list(this_pkg) + list(tail)
                else:
                    return list(this_pkg)
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

                this_pkg = list(this_pkg)
                shift = 0

                for i in slices:
                    this_pkg[i[0] - shift:i[1] - shift] = [-(i[1] - i[0])]
                    shift += (i[1] - i[0] - 1)

                if len(tail) != 0:
                    return list(this_pkg) + list(tail)
                else:
                    return list(this_pkg)
