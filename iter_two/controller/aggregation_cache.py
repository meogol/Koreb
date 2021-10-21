
class Agregation_cache:
    def __init__(self):
        self.cache = [0]*10


    def add_cache(self, commands):
        self.cache.insert(0, commands)
        del self.cache[10]

    def receiving_cache(self, number):
        """получение элемента кэша"""
        return self.cache[number]

if __name__ == '__main__':
    add = Agregation_cache()
    add.add_cache([12, 3, 40])
    add.add_cache([37, 80, 214])
    add.add_cache([5, 90, 43])
    add.add_cache([654, 234, 4435])
    add.add_cache([782, 578, 354])
    add.add_cache([531, 786, 621])
    add.add_cache([513, 45, 972])
    add.add_cache([6452, 215, 60])
    add.add_cache([943, 45, 267])
    add.add_cache([563, 542, 228])
    add.add_cache([372, 6523, 389])
    add.add_cache([267, 821, 26])
    add.add_cache([687, 87, 65])
    print(add.receiving_cache(7))