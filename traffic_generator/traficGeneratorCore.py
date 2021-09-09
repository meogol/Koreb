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
        self.ip = ['192.168.1.1'
            # , '192.168.1.0', '192.168.0.1', '192.168.0.0', '192.168.0.2'
                   ]
        self.plots = {'192.168.1.1': [],
        #          '192.168.1.0': [],
        #          '192.168.0.1': [],
        #          '192.168.0.0': [],
        #          '192.168.0.2': []
                 }


    def randomize_inner_lists(self):
        """
        function makes 1000 lists of commands with random length 10 - 100
        """
        def rerandom_buffer_list(self):
            for item in range(random.randint(10, 100)):
                self.buffer_list_of_commands.append(random.choice(self.command_list))

        for k in self.plots.keys():
            for i in range(1000):
                rerandom_buffer_list(self)
                self.doubler_buffer_list_of_commands = self.buffer_list_of_commands.copy()
                self.plots['192.168.1.1'].append(self.doubler_buffer_list_of_commands)
                self.buffer_list_of_commands.clear()