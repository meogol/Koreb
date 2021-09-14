from Visual_part.visual_make_ping import PingGenerator
from Visual_part.visual import RunVisualisation

class CommandInterpritator:
    def __init__(self):
        self.command_list = ['up', 'down', 'left', 'right', 'up-left', 'up-right', 'down-left', 'down-right']
        self.ping = PingGenerator()
        self.x = 0
        self.y = 0
        self.vis =RunVisualisation()

    def run_interpritation(self, command):
        if command is None:
            pass  # вывод ошибки на экран
        elif command == 'up':
            self.y += 1
            self.ping.make_ping(self.x, self.y)
        elif command == 'down':
            self.y -= 1
            self.ping.make_ping(self.x, self.y)
        elif command == 'left':
            self.x -= 1
            self.ping.make_ping(self.x, self.y)
        elif command == 'right':
            self.x += 1
            self.ping.make_ping(self.x, self.y)
        elif command == 'up-left':
            self.x -= 1
            self.y += 1
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
            self.x += 1
            self.y -= 1
            self.ping.make_ping(self.x, self.y)
        else:
            pass

    def run_interpritation_neuro(self, command):
        for item in command:
            if item is None:
                pass  # вывод ошибки на экран
            elif item == 'up':
                self.y += 1
                self.vis.main_func(self.x, self.y)
            elif item == 'down':
                self.y -= 1
                self.vis.main_func(self.x, self.y)
            elif item == 'left':
                self.x -= 1
                self.vis.main_func(self.x, self.y)
            elif item == 'right':
                self.x += 1
                self.vis.main_func(self.x, self.y)
            elif item == 'up-left':
                self.x -= 1
                self.y += 1
                self.vis.main_func(self.x, self.y)
            elif item == 'up-right':
                self.x += 1
                self.y += 1
                self.vis.main_func(self.x, self.y)
            elif item == 'down-left':
                self.x -= 1
                self.y -= 1
                self.vis.main_func(self.x, self.y)
            elif item == 'down-right':
                self.x += 1
                self.y -= 1
                self.vis.main_func(self.x, self.y)
            else:
                pass