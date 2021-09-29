import numbers

from Taker.graph_core.graph_generator import GraphGenerator


class Controller:
    def __init__(self):
        self.graph_generator = GraphGenerator()
        pass

    def analyse_command(self, ip, command):
        res = str
        for item in command:
            if item.isnumeric():
                res += self.graph_generator.get_item(item)
            else:
                res += item

    def update_graph(self, command_dict):
        for key in command_dict.keys():
            self.graph_generator.add_items(key, command_dict.get(key))
