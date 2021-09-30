class CacheItem:
    def __init__(self, id, commands, value=70):
        self.value = value
        self.id = id
        self.commands = commands
        self.is_used = False
        self.is_kill = False

    def __eq__(self, other):
        return self.commands == other.commands

    def __hash__(self):
        return hash(self.id) ^ hash(self.commands)

    def __str__(self):
        return 'CacheItem(value:' + str(self.value) \
               + ' id:' + str(self.id) + ' commands' + str(self.commands) + ')'

    def __repr__(self):
        return '{value:' + str(self.value) \
               + ' id:' + str(self.id) + ' commands' + str(self.commands) + '}'
