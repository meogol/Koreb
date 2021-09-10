
from Koreb.graphCore.recursive_algorithm import GoAroundGraph
from Koreb.graphCore.graph import Graph
from Koreb.traffic_generator.trafficGenerator import TrafficGenerator


class GraphGenerator:
    def __init__(self):
        self.graph = Graph()
        self.traf_gen = TrafficGenerator()
        self.command_list = []
        self.level = 0

    def create_command(self, ip, command, level):
        """
        :param level:
        :param ip:
        :param command: единичная команда
        :return:
        """
        if level == 0:
            self.graph.graph_init(ip, command)
            self.command_list.append(command)
            return

        self.graph.graph_add_command(ip, command)
        self.command_list.append(command)

    def run_graph(self):
        level = 0
        ip, command = self.traf_gen.get_ip_and_command()
        for item in command:
            self.create_command(ip, item, level)
            self.training_ai(item)
            level += 1

        self.command_list.clear()

    def training_ai(self, command):
        """
        тут слой работы с НС
        :param command:
        :return:
        """
        pass


if __name__ == '__main__':
    graph = GraphGenerator()
    for a in range(10):
        graph.run_graph()
    rec = GoAroundGraph()
    for item in graph.graph.graph:
        rec.recoursive_algorithm(item, 1)

    print(rec.data)
    a = 1
