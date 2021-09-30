from typing import List

from Controller.cash.cache_item import CacheItem


class CommandCache:
    def __init__(self):
        self.cache_active = list()
        self.cache_predicted = list()
        self.id = 0

    def append_to_cash(self, commands):
        item = CacheItem(self.id, commands)
        if item not in self.cache_predicted and item not in self.cache_active:
            self.cache_predicted.append(item)
            self.id += 1

    def get_item_by_commands(self, commands):
        """
        возвращает элемент по последовательности команд
        @type commands: list
        @return: возвращает элемент из кэша или None
        """
        item: List[CacheItem] = list(filter(lambda x: x.commands == commands, self.cache_predicted))
        if len(item) == 0:
            return None

        item[0].is_used = True
        return item[0]

    def get_item_by_id(self, id):
        """
        возвращает элемент по id
        @param id: номер элемента
        @return: возвращает элемент из кэша
        """
        item = list(filter(lambda x: x.id == id, self.cache_predicted))
        if len(item) == 0:
            return None

        return item[0]

    def compare_lists(self):
        pass

    def update_active(self):
        pass

    def check_lifeline(self):
        pass


if __name__ == '__main__':
    rect = CommandCache()
    rect.append_to_cash([1, 5, 8])
    rect.append_to_cash([1, 5, 8])
    rect.append_to_cash([2, 3, 4])
    rect.append_to_cash([2, 1, 4])
    rect.append_to_cash([3, 3, 4])
    rect.append_to_cash([2, 5, 4])

    a = rect.get_item_by_commands([1, 5, 18])
    b = rect.get_item_by_id(111)
    b = b
