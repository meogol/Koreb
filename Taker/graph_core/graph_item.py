class GraphItem:
    def __init__(self, request, level):
        self.request = request
        self.level = level

    def __eq__(self, other):
        return (self.level == other.level and
                self.request == other.request)

    def __hash__(self):
        return hash(self.request) ^ hash(self.level)

    def __str__(self):
        return 'GraphItem(request:' + str(self.request)\
               + ' level:' + str(self.level) + ')'

    def __repr__(self):
        return '{request:' + str(self.request)\
               + ' level:' + str(self.level) + '}'
