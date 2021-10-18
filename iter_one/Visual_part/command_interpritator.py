from iter_one.Visual_part.visual_make_ping import PingGenerator


class CommandInterpritator:
    def __init__(self):
        self.command_list = ['up', 'down', 'left', 'right', 'up-left', 'up-right', 'down-left', 'down-right']
        self.ping = PingGenerator()
        self.x = 0
        self.y = 0

    def run_interpritation(self, command):
        if command is None:
            pass  # вывод ошибки на экран
        elif command == 'up':
            self.x += 1
            self.y += 1
            self.ping.make_ping(self.x, self.y)
        elif command == 'down':
            self.x -= 1
            self.y -= 1
            self.ping.make_ping(self.x, self.y)
        elif command == 'left':
            self.y -= 1
            self.ping.make_ping(self.x, self.y)
        elif command == 'right':
            self.y += 1
            self.ping.make_ping(self.x, self.y)
        elif command == 'up-left':
            self.x += 1
            self.y -= 1
            self.ping.make_ping(self.x, self.y)
        elif command == 'up-right':
            self.x += 1
            self.y += 1
            self.ping.make_ping(self.x, self.y)
        elif command == 'down-left':
            self.x -= 1
            self.y -= 1
            self.ping.make_ping(self.x, self.y)
        elif command == 'down-right':
            self.x -= 1
            self.y += 1
            self.ping.make_ping(self.x, self.y)
        else:
            pass
