import matplotlib.pyplot as plt
import numpy as np


class RunVisualisation:

    def __init__(self):
        self.fig, self.axes = plt.subplots(nrows=2, ncols=1)

        self.axes[0].set(xlim=[-100, 100],
                         ylim=[-100, 100])
        self.axes[1].set(xlim=[-100, 100],
                         ylim=[-100, 100])

    def run_visualisation(self, x, y):
        plt.clf()
        self.axes[0].scatter([x], [y], 'r')
        self.axes[1].scatter([0], [0], 'r')
        plt.draw()
        plt.gcf().canvas.flush_events()

    def main_func(self, x, y):
        self.run_visualisation(x, y)
