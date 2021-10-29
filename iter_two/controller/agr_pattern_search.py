from iter_two.core.cahce.cache import CacheManager


class AgrPatternSearch:

    @staticmethod
    def sub_finder(current_package, pattern):
        """
        Служебный метод для функции agr_cache_patterns()
        """
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

            return patterns
        else:
            print('no aggregation cache for this IP yet')
