import time
from threading import Thread
from typing import List

from iter_one.Controller.cache.cache_item import CacheItem
from iter_one.Controller.cache.cache_object_life_cycle_control import CacheObjectLifeCycleControl
from iter_one.Controller.cache.id import convert_to_36

class CommandCache:
    def __init__(self):
        self.cache_active = list()
        self.cache_predicted = list()
        self.id = 0
        th = Thread(target=self.check_lifeline)
        th.start()

    def append_to_cache(self, commands):
        item = CacheItem('!' + convert_to_36(self.id) + '!', commands)
        if item not in self.cache_predicted and item not in self.cache_active:
            self.cache_predicted.append(item)
            self.id += 1

    @staticmethod
    def get_item_by_commands(commands, cache):
        """
        возвращает элемент по последовательности команд
        @param cache:
        @type commands: list
        @return: возвращает элемент из кэша или None
        """
        item: List[CacheItem] = list(filter(lambda x: x.commands == commands, cache))
        if len(item) == 0:
            return None

        item[0].is_used = True
        return item[0]

    @staticmethod
    def get_item_by_id(id, cache):
        """
        возвращает элемент по id
        @param cache:
        @param id: номер элемента
        @return: возвращает элемент из кэша
        """
        item = list(filter(lambda x: x.id == id, cache))
        if len(item) == 0:
            return None

        return item[0]

    def update_active(self):
        add_commands_list: List[CacheItem] = list(filter(lambda x: x.value > 70, self.cache_predicted))
        self.cache_active.extend(add_commands_list)

    def check_lifeline(self):
        while True:
            time.sleep(5)
            CacheObjectLifeCycleControl.check_life_cycle(self.cache_active)
            CacheObjectLifeCycleControl.check_life_cycle(self.cache_predicted)
            self.update_active()


if __name__ == '__main__':
    rect = CommandCache()
    rect.append_to_cache([1, 5, 8])
    rect.append_to_cache([1, 5, 8])
    rect.append_to_cache([2, 3, 4])
    rect.append_to_cache([2, 1, 4])
    rect.append_to_cache([3, 3, 4])
    rect.append_to_cache([2, 5, 4])