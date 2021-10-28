import re

from iter_two.core.cahce.cache import CacheManager


class AgrPatternSearch:

    @staticmethod
    def sub_finder(current_package, pattern):
        matches = []
        for i in range(len(current_package)):
            if current_package[i] == pattern[0] and current_package[i:i + len(pattern)] == pattern:
                matches.append(pattern)
        return matches

    def agr_cache_patterns(self, package, ip, cache_manager: CacheManager):
        """
        Метод ищет паттерны у текущего пакета и аггрегационного кеша пакетов, отправленных на тот же IP

        Keyword arguments:
            package -- текущий пакет
            ip -- IP, на который был отправлен текущий пакет
            cache_manager -- кеш
        """
        save_cur_package = package
        patterns = []

        if cache_manager.agr_cache_ip_check(ip):
            for item in range(0, cache_manager.number_of_agr_cached_items(ip) - 1):
                for sub_len in range(2, int(len(cache_manager.aggregation_cache.get(ip).receiving_cache(item)) / 2)):
                    for i in range(0, len(cache_manager.aggregation_cache.get(ip).receiving_cache(item)) - sub_len):
                        sub = cache_manager.aggregation_cache.get(ip).receiving_cache(item)[i:i + sub_len]
                        if self.sub_finder(package, sub):
                            if sub not in patterns:
                                patterns.append(sub)

            patterns.sort(key=len)
            patterns.reverse()
            package_str = str(package)[1:-1]
            chk = {}
            id = -1

            for i in patterns:
                if len(self.sub_finder(package, i)) >= 1:
                    str_tmp = str(i)[1:-1]
                    package_str = re.sub(r'\b' + str_tmp, str(id), package_str)
                    if '--' in package_str:
                        package_str = re.sub(r'--\d+', '-' + str_tmp, package_str)
                    chk[str(id)] = i
                    id -= 1
                package = list(map(int, package_str.split(', ')))
            print('________________')
            print('current package: ' + str(save_cur_package))
            print('zip package: ' + str(package))
            print(chk)
            print('________________')
            return patterns
        else:
            print('no aggregation cache for this IP yet')


if __name__ == '__main__':
    asd = AgrPatternSearch()
    qwe = CacheManager()
    asd.agr_cache_patterns([12, 35, 66, 93, 57, 567, 354, 4891, 653124], 45, qwe)

    qwe.add_agr_cache(12, [123, 82, 63, 41, 47, 95, 25, 35, 71, 85, 3, 97, 73, 64, 71, 24, 51, 741])
    qwe.add_agr_cache(12, [123, 82, 23, 41, 47, 95, 25, 74, 71, 85, 3, 97, 85, 64, 57, 24, 96, 741])
    qwe.add_agr_cache(12, [123, 25, 43, 2, 47, 95, 75, 35, 71, 85, 11, 97, 73, 41, 71, 12, 51, 739])
    qwe.add_agr_cache(12, [148, 82, 63, 41, 43, 95, 25, 35, 71, 85, 3, 97, 73, 64, 71, 24, 51, 741])

    q = asd.agr_cache_patterns([123, 53, 63, 41, 47, 95, 25, 24, 71, 85, 3, 97, 73, 64, 36, 24, 51, 741], 12, qwe)
    print(q)
