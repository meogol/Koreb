from TrafficGenerator.TrafficGenerator import get_ip_and_command
from graphCore.graph import Graph


class GraphGenerator:
    def __init__(self):
        self.graph = Graph()

    def create_command(self):
        """
        заполняет граф элементами из сгенерированного набора
        :return:
        """
        ip, command = get_ip_and_command()
        command_list = []

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
