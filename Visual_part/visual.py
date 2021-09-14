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
        pylab.xlim(-30,30)
        pylab.ylim(-30,30)
        plt.grid(True)
        time.sleep(0.02)
        plt.gcf().canvas.flush_events()


    def main_func(self, x, y):
        self.run_visualisation(x, y)
