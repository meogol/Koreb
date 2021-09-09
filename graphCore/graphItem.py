
class GraphItem:
    def __init__(self, request, ip):
        """
        базовый конструктор для создания первого элемента графа
        :param request:
        :param ip:
        """
        self.request = request
        self.ip = ip
        self.next_items = []
        self.last_item = last_item
        self.percent = 0
        self.level = 0

    def __init__(self, request, ip, last_item, level):
        """
        вызывается только из класса графа
        request- string
        ip- string
        """
        self.request = request
        self.ip = ip
        self.next_items = []
        self.last_item = last_item
        self.percent = 0
        self.level = level

    def add_item(self, request, ip, last_item):
        """
        :param request: запрос
        :param ip:
        :param last_item: прошлый родительский элемент узла
        :return:
        """
        self.next_items.append(GraphItem(request, ip, last_item, self.level+1))
