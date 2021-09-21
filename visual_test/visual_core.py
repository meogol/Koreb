import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.patches import Rectangle


class VisualCore:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        fig, ax = plt.subplots()
        fig.set_size_inches(6, 6)
        ax.set_xlim(-2, self.x + 3)
        ax.set_ylim(-2, self.y + 3)

        plt.ion()
        plt.show()

        for a in range(100):
            self.__show_point__("", ax)

    def __show_point__(self, command, ax):
        ax.clear()

        rect = Rectangle((0, 0), self.y + 1, self.y + 1, fill=None, edgecolor='r')
        ax.plot(self.x, self.y, ' sb', markersize=18, alpha=0.8)
        ax.add_patch(rect)

        plt.draw()
        plt.gcf().canvas.flush_events()


if __name__ == '__main__':
    vc = VisualCore(10, 10)
    vc.show()

    plt.ioff()
    plt.show()
