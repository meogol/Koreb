import networkx

from Controller.traffic_generator.trafficGenerator import TrafficGenerator
from Taker.graph_core.graph_item import GraphItem


class GraphGenerator:
    def __init__(self):
        self.graph = dict()  # это граф. Правда. id-key value-command
        pass

    def add_items(self, id_list, command_list):
        for i in range(len(id_list)):
            self.graph[id_list[i]] = command_list[i]

    def search_item(self, id):
        res = self.graph.get(id)
        if res is None:
            return res
        else:
            return ""


if __name__ == '__main__':
    pass
