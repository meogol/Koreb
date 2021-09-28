import numbers

from Taker.graph_core.graph_generator import GraphGenerator


class Controller:
    def __init__(self):
        self.graph_generator = GraphGenerator()
        pass

    def analyse_command(self, command):
        res = str
        for item in command:
            if item.isnumeric():
                res += self.graph_generator.get_item(item)
            else:
                res += item

        return res

    def update_graph(self, id_list, command_list):
        for i in range(len(id_list)):
            self.graph_generator.add_items(id_list[i], command_list[i])

        pass
