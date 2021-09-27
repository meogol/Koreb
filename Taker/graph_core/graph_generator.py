<<<<<<< HEAD
<<<<<<< main
class GraphGenerator:
    def __init__(self):
        self.graph = list()  # пока работаем с загдушкой в виде листа

    def add_item(self):
        pass

    def search_item(self):
        pass

    def rebase_graph(self):
        pass

    def remove_item(self, command):
        pass
=======
=======
>>>>>>> graph_plug
import networkx
from matplotlib import pyplot as plt

from Controller.traffic_generator.trafficGenerator import TrafficGenerator
from Taker.graph_core.graph_item import GraphItem


class GraphGenerator:
    def __init__(self):
        self.graph = networkx.Graph()

    def add_command(self, command_list):
        level = 0
        for command in command_list:
            item = GraphItem(command, level)
            self.graph.add_node(item)

            if level != 0:
                last_level = level - 1
                last_item = GraphItem(command_list[last_level], last_level)

                self.graph.add_edge(last_item, item)

            level += 1


if __name__ == '__main__':
    gg = GraphGenerator()
    graph = gg.graph
    a = TrafficGenerator()
    c, cc = 0, 0

    for aa in range(8):
        c, cc = a.get_ip_and_command()
        gg.add_command(cc)

    print(graph.nodes())
    print(graph.adj)

    a = graph.nodes()

    print(a)
    print(a)

    a = a
    # options = {
    #     'node_size': 20,
    #     'width': 2,
    # }
    # nx.draw(graph, with_labels=True,  font_weight='bold', **options)
    # plt.savefig("path.png")
<<<<<<< HEAD
>>>>>>> first upd
=======
>>>>>>> graph_plug
