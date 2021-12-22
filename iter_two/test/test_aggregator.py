from iter_two.controller.aggregator import Aggregator
from iter_two.core.cahce.cache import CacheManager
from iter_two.taker.taker import Taker


def method(last, this):
    cache = CacheManager()
    taker = Taker()
    Last = last
    This = this
    cache.add_all_cache(ip="192.168.0.106", package=Last)
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
def test_contrast_last_package1():
    # в данном тесте сравнение пакетов с одинаковой длинной
    last = [0, 132, 123, 35, 0, 0, 0, 5, 3, 5, 7, 3, 22, 167, 23, 134, 6, 27, 86]
    this = [20, 12, 123, 35, 0, 0, 40, 5, 3, 5, 7, 3, 2, 67, 243, 34, 26, 87, 186]
    a = (method(last, this))
    assert a == 1


# @pytest.mark.agreg_large_this
def test_contrast_last_package2():
    # в данном тесте сравнение пакетов, когда предыдущий короче текущего
    last = [4, 5, 6, 1, 2, 8, 6, 3, 9, 2, 9, 6, 7, 5, 7, 0, 6, 4, 6, 0, 2, 6, 3, 5, 9, 4, 4, 9, 3, 0, 8, 7, 5, 4, 0, 2,
            6, 9, 9, 1, 5, 9, 9, 4, 2, 3, 3, 4, 6, 1, 6, 7, 0, 4, 1, 5, 5, 0, 7, 4, 7, 1, 2, 0, 6, 9, 7, 6, 7, 2, 7, 6,
            9, 0, 6, 7, 4, 3, 2, 3, 5, 2, 2, 6, 2, 0, 0, 3, 8, 7, 3, 4, 3, 6, 6, 5, 9, 5, 0, 3, 5, 3, 4, 8, 5, 9, 6, 3,
            4, 5, 9, 0, 0, 6, 0, 4, 0, 4, 2, 7, 2, 3, 9, 9, 3]
    this = [4, 5, 6, 1, 2, 8, 6, 3, 9, 2, 9, 6, 7, 6, 3, 0, 7, 6, 8, 7, 1, 6, 4, 7, 8, 4, 5, 9, 2, 2, 5, 7, 8, 9, 2, 9,
            4, 1, 0, 2, 7, 8, 6, 2, 2, 2, 1, 3, 4, 5, 6, 5, 6, 8, 8, 4, 0, 7, 0, 4, 3, 9, 6, 2, 2, 2, 6, 0, 9, 2, 4, 2,
            3, 4, 8, 7, 0, 6, 8, 9, 0, 7, 0, 2, 2, 7, 3, 4, 5, 2, 8, 8, 7, 9, 4, 1, 7, 9, 3, 5, 7, 3, 5, 2, 4, 8, 1, 8,
            6, 4, 0, 0, 6, 2, 5, 9, 3, 6, 1, 9, 2, 3, 9, 3, 8]
    a = (method(last, this))
    assert a == 1


# @pytest.mark.agreg_smal_this
def test_contrast_last_package3():
    # в данном тесте сравнение пакетов, когда предыдущий длинее текущего
    last = [0, 132, 123, 35, 0, 0, 0, 5, 3, 5, 7, 3, 22, 167, 23, 134, 6, 27, 86]
    this = [20, 12, 123, 35, 0, 0, 40, 5, 3, 5, 7, 3, 2, 67, 243, 34]
    a = (method(last, this))
    assert a == 1


# @pytest.mark.agreg_smal_this
def test_contrast_last_package4():
    # в данном тесте сравнение пакетов, когда предыдущий длинее текущего
    last = [20, 12, 123, 35, 0, 0, 0, 5, 3, 5, 7, 3, 22, 167, 23, 134, 6, 27, 86]
    this = [20, 12, 123, 35, 0, 0, 40, 5, 3, 5, 7, 3, 2, 67, 243, 34]
    a = (method(last, this))
    assert a == 1
