import unittest
from iter_two.controller.aggregator import Aggregator
from iter_two.core.cahce.cache import CacheManager
from iter_two.taker.taker import Taker

class TestAggregator(unittest.TestCase):
    def test_contrast_last_package(self):
        cache = CacheManager()
        taker = Taker()
        last = [0, 132, 123, 35, 0, 0, 0, 5, 3, 5, 7, 3, 22, 167, 23, 134, 6, 27, 86]
        cache.add_all_cache("192.168.0.106", last)
        this = [20, 12, 123, 35, 0, 0, 40, 5, 3, 5, 7, 3, 2, 67, 243, 34, 26, 87, 186]
        agr = Aggregator(cache)
        agr_this = agr.contrast_last_package(this, "192.168.0.106")
        ras_pack2 = taker.recovery_pkg(agr_this, last)
        r ==1
        assert last == ras_pack2
