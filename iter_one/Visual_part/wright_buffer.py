from iter_one.Visual_part.command_interpritator import CommandInterpritator

class WrightBuffer:
    def __init__(self):
        self.buffer = list()
        self.interp = CommandInterpritator()

    def wright_in_buf(self, commands):
        self.buffer.append(commands)

    def give_buf_back(self):
        return self.buffer

    def clear_buf(self):
        self.buffer.clear()

    def call_interp(self, command):
        self.interp.run_interpritation(command)
