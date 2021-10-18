from iter_one.Taker.graphCore.graph import Graph
from iter_one.Controller.traffic_generator.trafficGenerator import TrafficGenerator
from iter_one.Visual_part.visual_command_analyze import VisualCommandAnalyzer
from iter_one.Visual_part.wright_buffer import WrightBuffer


class GraphGenerator:
    def __init__(self):
        self.graph = Graph()
        self.traf_gen = TrafficGenerator()
        self.command_list = []
        self.level = 0
        self.run_visual = VisualCommandAnalyzer()
        self.wright_buf = WrightBuffer()
        self.buf = list()

    def create_command(self, ip, command, level):
        """
        верхний уровень функции добавления команды в граф. Автоматически заполяет command_list
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
        """
        точка входа для работы с графом. Тут же запускается НС
        :return:
        """
        level = 0
        ip, command = self.traf_gen.get_ip_and_command()

        for item in command:
            self.create_command(ip, item, level)
            self.training_ai(item)
            level += 1
            # self.wright_buf.call_interp(item)

        self.command_list.clear()

    def training_ai(self, command):
        """
        тут слой работы с НС
        :param command:
        :return:
        """
        pass


if __name__ == '__main__':
    plt.ion()

    graph = GraphGenerator()
    for a in range(100000):
        graph.run_graph()

    plt.ioff()
    plt.show()
