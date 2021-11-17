import numpy as np


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


