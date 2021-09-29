import numbers

from Controller.cash.cacheItem import CacheItem

class CommandCache():
    def __init__(self):
        self.cache_active = list()
        self.predicted = list()

    def append_to_cash(self, i):
        self.cache_active = CacheItem(1, 2, i)
        if self.cache_active not in self.predicted:
            self.predicted.append(self.cache_active)

    def compare_lists(self):
        pass

    def update_active(self):
        pass

    def check_lifeline(self):
        pass


if __name__ == '__main__':
    rect = CommandCache()
    rect.append_to_cash([1, 5, 8])