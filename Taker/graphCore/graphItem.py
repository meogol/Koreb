class GraphItem:

    def __init__(self, request, ip, last_item=None, level=0):
        """
        с двумя параметрами вызывается только для создания графа
        :param request:
        :param ip:
        :param last_item: указатель на прошлый элемент
        :param level: уровень вложенности элемента
        """
        self.request = request
        self.ip = ip
        self.next_items = []
        self.last_item = last_item
        self.percent = 0
        self.level = level

    def add_item(self, request, ip, last_item):
        """
        бавзовый функционал для добавлнения команд в граф. На прямую вызывать не следует
        :param request: запрос
        :param ip:
        :param last_item: прошлый родительский элемент узла
        :return: добавленный элемент
        """
        item = GraphItem(request, ip, last_item, self.level + 1)
        self.next_items.append(item)
        return item

    def __eq__(self, other):
        return (self.level == other.level and
                self.request == other.request and
                self.ip == other.ip)
