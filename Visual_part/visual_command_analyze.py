from Visual_part.command_interpritator import CommandInterpritator

class VisualCommandAnalyzer:
    def __init__(self):
        self.interp = CommandInterpritator()

    def run_analyze(self, command):
        if isinstance(command, list) == True:
            pass #сюда вставить метод для НС
        else:
            self.interp.run_interpritation(command)


