from graphCore.graphItem import GraphItem


class Graph:
    def __init__(self):
        self.graph = []
        self.this_command = None

    def graph_init(self, ip, request):
        """
        создает первый элемент первого уровня в графе
        :param ip:
        :param request:
        :return:
        """
        if len(self.graph) <= 0:
            self.this_command = GraphItem(request, ip)
            self.graph.append(self.this_command)
        else:
            return

    def graph_add_command(self, ip, request):
        if self.this_command.ip != ip:
            return

        self.this_command = self.this_command.add_item(ip, request, self.this_command)

    def search_command(self, list_command, ip):
        """
        находит узел по последовательности команд
        :param ip:
        :param list_command: последовательность команд
        :return: this_command становится искомым узлом
        """

        for command in list_command:
            for this_graph_line_item in self.graph:
                if command == this_graph_line_item.request\
                        and this_graph_line_item.ip == ip:
                    this_graph_line = this_graph_line_item

        self.this_command = this_graph_line
