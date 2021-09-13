import time
from Visual_part.visual import RunVisualisation
class PingGenerator:
    def __init__(self):
        self.vis = RunVisualisation()

    def make_ping(self, x,y):
        # time.sleep(2)
        self.vis.run_visualisation(x,y)
        pass