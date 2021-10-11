

class CacheGenerator:
    def __init__(self):
        self.graph = dict()  # id-key value-command
        pass

    def add_items(self, id, command):
        if self.graph.get(id) is None:
            self.graph[id] = command

    def get_item(self, id):
        res = self.graph.get(id)
        if res is None:
            return None
        else:
            return res


if __name__ == '__main__':
    pass
