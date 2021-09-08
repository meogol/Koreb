
class GraphItem:
    def __init__(self, request, ip, last_item):
        """
        request- string
        ip- string
        """
        self.request = ""
        self.ip = ""
        self.next_items = []
        self.last_item = last_item
        self.percent = 0
        self.level = 0

    def add_item(self, request, ip, last_item):
        self.next_items.append(GraphItem(request, ip, last_item))
