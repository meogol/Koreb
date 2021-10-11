import numbers

from Taker.cahce_core.cache_generator import CacheGenerator


class Controller:
    def __init__(self):
        self.cache_generator = CacheGenerator()
        pass

    def analyse_command(self, ip, command):
        res = self.serialize_command(command)
        print()
        print(str(len(command)) + "\t" + str(len(res)))
        print(str(res))

    def serialize_command(self, command):
        res = list()
        for item in command:
            if item.isdigit():
                data = self.cache_generator.get_item(item)
                if data is not None:
                    res.extend(data)
            else:
                res.append(item)

        return res

    def update_graph(self, command_dict):
        for key in command_dict.keys():
            self.cache_generator.add_items(key, command_dict.get(key))
