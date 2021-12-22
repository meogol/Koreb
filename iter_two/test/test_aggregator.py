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
    last = [0, 132, 123, 35, 0, 0, 0, 5, 3, 5, 7, 3, 22, 167, 23, 134, 6, 27, 86]
    this = [20, 12, 123, 35, 0, 0, 40, 5, 3, 5, 7, 3, 2, 67, 243, 34, 26, 87, 186, 12, 42, 534]
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
