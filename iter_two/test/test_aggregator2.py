from iter_two.controller.aggregator import Aggregator
from iter_two.core.cahce.cache import CacheManager
from iter_two.taker.taker import Taker


def method(last, this):
    cache = CacheManager()
    taker = Taker()
    Last = last
    This = this
    # добавление предыдущего пакета в кэш
    agr = Aggregator(cache)
    agr_this = agr.contrast_last_package(package=this, destination_ip="192.168.0.106")
    # агрегация текущего пакета
    print("\n"
          "Изначальный:   ", This)
    print("Предыдущий:    ", Last)
    print("Агрегированный:", agr_this)
    ras_pack2 = taker.recovery_pkg(package=agr_this, last_pkg=Last)
    # распаковка текущего пакета
    ras = ras_pack2.tolist()
    # приведение распакованного текущего пакета к списку
    print("Восстановленный:", ras)
    if This == ras:
        return 1
    else:
        return 0


# @pytest.mark.agreg_same
def test_contrast_last_package1_1():
    cache = CacheManager()
    agr = Aggregator(cache)
    taker = Taker()
    one = [8, 4, 1, 4, 0, 8, 8, 3, 3, 0, 4, 4, 9, 7, 2, 7, 6, 8, 8, 3, 6, 4, 9, 1, 8, 6, 4, 3, 6, 7, 6, 6, 0, 2, 3, 0]
    agr_pack = [[8, 2, 4, 5, 9, 2, 4, 3, 3, 0, 4, 4, 9, 7, 2, 7, 6, 3, 1, 3, 6, 7, 9, 8, 9, 0, 4, 2, 6, 7, 5, 8, 7, 8, 3, 0],
                [1, 3, 4, 2, 2, 3, 7, 8, 4, 0, 4, 4, 9, 7, 2, 7, 6, 8, 3, 3, 4, 4, 9, 3, 2, 7, 9, 0, 7, 9, 9, 9, 6, 2, 3, 0],
                [8, 3, 5, 7, 1, 3, 4, 6, 9, 0, 4, 4, 9, 7, 2, 7, 3, 3, 2, 6, 4, 8, 4, 6, 2, 6, 4, 3, 6, 7, 6, 6, 2, 1, 6, 8]]
    for i in agr_pack:
        cache.add_all_cache(package=one, ip="192.168.0.106")
        agr_this = agr.contrast_last_package(package=i, destination_ip="192.168.0.106")
        print("\n" "Агрегированный:", agr_this)
        ras_pack2 = taker.recovery_pkg(package=i, last_pkg=one)
        n = ras_pack2.tolist()
        print("Восстановленный:", n)
        print("Текущий:", i)
        print("предыдущий:", one)
        if n == i:
            print('good')
        else:
            print('bad')
        one = n

    assert 1 == 1

