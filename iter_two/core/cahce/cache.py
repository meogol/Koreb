from iter_two.core.cahce.aggregation_cache import AggregationCache
from iter_two.core.cahce.previous_cache import PreviousCache


class CacheManager:

    def __init__(self):
        self.last_package_cache = PreviousCache()
        self.aggregation_cache = dict()

    def add_all_cache(self, ip, package):
        self.add_agr_cache(ip, package)
        self.add_last_pkg_cache(ip, package)

    def add_agr_cache(self, ip, package):
        agr_cache = self.aggregation_cache.setdefault(ip, AggregationCache())
        agr_cache.add_cache(package)

    def add_last_pkg_cache(self, ip, package):
        self.last_package_cache.update_previous_cache(ip, package)

    def get_arg_cache(self, ip):
        self.aggregation_cache.get(ip)

    def get_last_pkg_cache(self, ip):
        self.last_package_cache.get_previous_cache(ip)
