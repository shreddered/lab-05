import matplotlib.pyplot as plt
import random

class Approximator:
    verbose = True
    def __init__(self, n: int, interval: tuple, params: tuple):
        self.n = n
        self.a, self.b = interval[0], interval[1]
        self.c, self.d = params[0], params[1]
        self.x = [x / n for x in range(self.a * self.n, self.b * self.n)]
        self.y = [self.c * x_ + self.d for x_ in self.x]
    def search(self, amp: int):
        if Approximator.verbose:
            # plot of original function
            plt.plot(self.x, self.y)
            plt.title('Original function')
            plt.show()
        y_err = [y + amp * random.uniform(-0.5, 0.5) for y in self.y]
    def _sum_of_squares(self, c: float, d: float):
        s = 0.0
        for i in range(0, self.n):
            x = self.x[i]
            t = self.y[i]
            y = c * x + d
            s += (y - t) * (y - t)
        return s
    def _passive_search(self, d_min: float, d_max: float):
        return 1.0
    def _dichotomy(self, c_min: float, c_max: float):
        eps = 0.1
        delta = 0.01
        while ((c_max - c_min) > eps):
            c1, c2 = 0.5 * (c_min + c_max) - delta, 0.5 * (c_min + c_max) + delta
            d1, d2 = self._passive_search(self.d_min, self.d_max)

approx = Approximator(n = 20, interval = (-2, 1), params = (0.5, 0))
approx.search(amp = 1)
