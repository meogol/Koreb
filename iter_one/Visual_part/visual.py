import matplotlib.pyplot as plt
import numpy as np
import time
import pylab

class RunVisualisation:

    def __init__(self):
        pass
    def run_visualisation(self, x, y):
        plt.clf()
        plt.scatter(x, y)
        pylab.xlim(-10,10)
        pylab.ylim(-10,10)
        plt.grid(True)
        time.sleep(0.02)
        plt.gcf().canvas.flush_events()


    def main_func(self, x, y):
        self.run_visualisation(x, y)
