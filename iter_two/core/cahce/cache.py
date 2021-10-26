from iter_two.core.cahce.aggregation_cache import AggregationCache


class CacheManager:

    def __init__(self):
        self.last_package_cache = None
        self.aggregation_cache = dict()

    def add_all_cache(self, ip, package):
        cache = self.aggregation_cache.setdefault(ip, AggregationCache())
        cache.add_cache(package)
