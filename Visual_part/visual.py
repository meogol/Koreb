import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

class RunVisualisation:

    def __init__(self):
        plt.ion()
        self.fig, self.axes = plt.subplots(nrows=2, ncols=1)

    def run_visualisation(self, x, y):
        self.axes[0].set(xlim=[-100, 100],
                         ylim=[-100, 100])
        self.axes[0].scatter([x], [y])

        self.axes[1].set(xlim=[-100, 100],
                         ylim=[-100, 100])
        self.axes[1].scatter([0], [0])


if __name__ == '__main__':


