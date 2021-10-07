from Controller.cache.cache_item import CacheItem
from Controller.send_data_to_taker import SendDataToTaker

if __name__ == '__main__':
    pkg = [1, 2, 3, 4]
    ci0 = CacheItem(1, ['left', 'right'])
    ci1 = CacheItem(2, ['right', 'right'])
    ci2 = CacheItem(3, ['up', 'left'])
    ci3 = CacheItem(4, ['left', 'up'])
    cache_items_list = [ci0, ci1, ci2, ci3]

    SendDataToTaker.send_pakage(pkg)
    SendDataToTaker.send_com_list_to_taker(cache_items_list)