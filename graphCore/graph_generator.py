from graphCore.graph import Graph
from traffic_generator.trafficGenerator import TrafficGenerator


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

    def run_graph(self):
        level = 0
        ip, command = self.traf_gen.get_ip_and_command()
        for item in command:
            self.create_command(ip, item, level)
            self.training_ai(item)
            level += 1

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
    a = 1
