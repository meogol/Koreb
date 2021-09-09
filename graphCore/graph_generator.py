from TrafficGenerator.trafficGenerator import TrafficGenerator
from TrafficGenerator.traficGeneratorCore import GeneratorCore
from graphCore.graph import Graph


class GraphGenerator:
    def __init__(self):
        self.graph = Graph()
        self.traf_gen = TrafficGenerator()


    def create_command(self):
        """
        заполняет граф элементами из сгенерированного набора
        :return:
        """
        command_list = []

        ip, command = self.traf_gen.get_ip_and_command()

        for a in range(100):
            level = 0
            for item in command:
                if level == 0:
                    command_list.append(item)
                    self.graph.graph_init(ip, item)
                    level += 1
                    continue

                command_list.append(item)
                if self.graph.this_command.level != level - 1:
                    self.graph.search_command(command, ip)



                self.graph.graph_add_command(ip, item)
                level += 1



if __name__ == '__main__':
    graph = GraphGenerator()
    graph.create_command()
    a=1

