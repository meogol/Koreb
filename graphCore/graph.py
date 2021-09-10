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
            return

        for item in self.graph:
            if item.request == request:
                self.this_command = item
                return
            else:
                self.this_command = GraphItem(request, ip)
                self.graph.append(self.this_command)
                return

    def graph_add_command(self, ip, request):
        res = self.get_item_by_command(request, self.this_command)
        if res is None:
            command = self.this_command.add_item(request, ip, self.this_command)
            self.this_command = command
        else:
            self.this_command = res

    def get_item_by_command(self, command, graph_item):
        """
        возвращает элемент следующего уровня, соответствующий команде
        :param command: 
        :param graph_item: 
        :return: 
        """
        for item in graph_item.next_items:
            if item.request == command:
                return item
        return None

    def get_item_by_command_line(self, command_line):
        """
        выполняет поиск команды по порядку вызовов. This_command принимает значение последней комманды в порядке вызов
        :param command_line:
        :return: найденный элемммент графа
        """
        graph_item = None

        for item in self.graph:
            graph_item = item

            for command in command_line:
                graph_item = self.get_item_by_command(command, graph_item)
                if graph_item is None:
                    graph_item = None
                    continue

            self.this_command = graph_item

        return graph_item
