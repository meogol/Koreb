
class PreviousCache:

    def __init__(self, dict = {'IP':None, 'DATA':None}):
        self.previous_dict = dict.copy()

    def __str__(self):
        return str(self.previous_dict.items())

    def update_previous_cache(self, dict):
        self.previous_dict.clear()
        self.previous_dict.update(dict)

    def get_previous_cache(self):
        return self.previous_dict



if __name__ == '__main__':
    cache = PreviousCache()
    print(cache)
    cache.update_previous_cache({('12.12.12.12', 'do smthng, u!'), ('13.13.13.13', 'oh...')})
    print(cache)