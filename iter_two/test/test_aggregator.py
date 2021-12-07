import unittest
from iter_two.controller.aggregator import Aggregator
from iter_two.core.cahce.cache import CacheManager
from iter_two.taker.taker import Taker

class TestAggregator(unittest.TestCase):
    def test_method(self):
        cache = CacheManager()
        taker = Taker()
        last = [0, 132, 123, 35, 0, 0, 0, 5, 3, 5, 7, 3, 22, 167, 23, 134, 6, 27, 86]
        cache.add_all_cache("192.168.0.106", last)
        this = [20, 12, 123, 35, 0, 0, 40, 5, 3, 5, 7, 3, 2, 67, 243, 34, 26, 87, 186]
        agr = Aggregator(cache)
        agr_this = agr.contrast_last_package(this, "192.168.0.106")
        print("Агрегированный:", agr_this)
        ras_pack2 = taker.recovery_pkg(agr_this, last)
        ras = ras_pack2.tolist()
        print("Изначальный:", this)
        print("Восстановле:", ras)
        if this == ras:
            return 1
        else:
            return 0


    def test_contrast_last_package(self):
        cache = CacheManager()
        taker = Taker()
        last = [0, 132, 123, 35, 0, 0, 0, 5, 3, 5, 7, 3, 22, 167, 23, 134, 6, 27, 86]
        cache.add_all_cache("192.168.0.106", last)
        this = [20, 12, 123, 35, 0, 0, 40, 5, 3, 5, 7, 3, 2, 67, 243, 34, 26, 87, 186]
        agr = Aggregator(cache)
        agr_this = agr.contrast_last_package(this, "192.168.0.106")
        print("Агрегированный:", agr_this)
        ras_pack2 = taker.recovery_pkg(agr_this, last)
        ras = ras_pack2.tolist()
        print("Изначальный:", this)
        print("Восстановле:", ras)
        assert this == ras
