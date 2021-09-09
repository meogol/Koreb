import random


class GeneratorCore:

    def __init__(self):
        self.first_ip = list()
        self.second_ip = list()
        self.third_ip = list()
        self.forth_ip = list()
        self.fifth_ip = list()
        self.ip = list()
        self.buffer_list_of_commands = list()
        self.doubler_buffer_list_of_commands = list()
        self.command_list = ['up', 'down', 'left', 'right', 'up-left', 'up-right', 'down-left', 'down-right']
        self.ip = ['192.168.1.1', '192.168.1.0', '192.168.0.1', '192.168.0.0', '192.168.0.2']
        self.plots = {'192.168.1.1': [],
                 '192.168.1.0': [],
                 '192.168.0.1': [],
                 '192.168.0.0': [],
                 '192.168.0.2': []
                 }


    def randomize_inner_lists(self):
        def rerandom_buffer_list(self):
            for item in range(100):
                self.buffer_list_of_commands.append(random.choice(self.command_list))

        for k in self.plots.keys():
            for i in range(10000):
                rerandom_buffer_list(self)
                self.doubler_buffer_list_of_commands = self.buffer_list_of_commands.copy()
                self.plots[k].append(self.doubler_buffer_list_of_commands)
                self.buffer_list_of_commands.clear()