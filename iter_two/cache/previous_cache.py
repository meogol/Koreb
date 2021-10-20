
class PreviousCache:

    def __init__(self):
        self.previous_dict = {}

    def __str__(self):
        return str(self.previous_dict.items())

    def update_previous_cache(self, ip, data):
        if self.previous_dict.get(ip) is not None:
            self.previous_dict[ip] = data
        else:
            self.previous_dict.update({ip : data})


    def get_previous_cache(self, ip):
        return self.previous_dict[ip]



if __name__ == '__main__':
    cache = PreviousCache()
    cache.update_previous_cache('12.12.12.12', 'do smthng, u!')
    print(cache)
    cache.update_previous_cache('12.12.12.13', 'go go go!')
    print(cache)
    cache.update_previous_cache('12.12.12.12', 'Oh no...')
    print(cache)
    print(cache.get_previous_cache('12.12.12.13'))