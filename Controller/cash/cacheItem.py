
class CacheItem():
    def __init__(self, v, i, c):
        self.value = v
        self.id = i
        self.cacheItem = c

    def __eq__(self, other):
        return (self.cacheItem == other.cacheItem)


    def __hash__(self):
        return hash(self.value) ^ hash(self.id) ^ hash(self.cacheItem)

    def __str__(self):
        return 'CacheItem(value:' + str(self.value) \
               + ' id:' + str(self.id) + 'cacheItem' + str(self.cacheItem) + ')'

    def __repr__(self):
        return '{value:' + str(self.value) \
               + ' id:' + str(self.id) + 'cacheItem' + str(self.cacheItem) + '}'
