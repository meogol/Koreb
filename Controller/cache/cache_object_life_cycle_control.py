from typing import List

from Controller.cache.cache_item import CacheItem


class CacheObjectLifeCycleControl:
    def __init__(self):
        pass

    @staticmethod
    def check_life_cycle(item_list):
        CacheObjectLifeCycleControl.chek_value(item_list)
        CacheObjectLifeCycleControl.kill_element(item_list)

    @staticmethod
    def chek_value(item_list):
        """
        В зависимосте от поля is_used повышает или понижает value элемента
        @param item_list:
        @return:
        """
        used_list: List[CacheItem] = list(filter(lambda x: x.is_used, item_list))
        not_used_list: List[CacheItem] = list(filter(lambda x: not x.is_used, item_list))

        for item in used_list:
            item.is_used = False

            if item.value + 10 < 100:
                item.value += 10

        for item in not_used_list:
            item.is_used = False

            if item.value - 1 > 0:
                item.value -= 1

            if item.value < 20:
                item.is_kill = True

    @staticmethod
    def kill_element(item_list: List):
        """
        удаляет из кэша все элементы, со значением is_kill = True
        @param item_list:
        @return:
        """
        killed_list: List[CacheItem] = list(filter(lambda x: x.is_kill, item_list))

        for item in killed_list:
            item_list.remove(item)



