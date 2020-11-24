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
        self.y = [y + amp * random.uniform(-0.5, 0.5) for y in self.y]
        self.d_min, self.d_max = -0.5, 0.5
        self.c_min, self.c_max = 0.17, 0.83
        c = self._dichotomy(0.17, 0.83)
        d = self._passive_search(-0.5, 0.5, c)
        if Approximator.verbose:
            # plot of new function
            plt.plot(self.x, self.y, 'ro')
            y_approx = [c * x_ + d for x_ in self.x]
            plt.plot(self.x, y_approx)
            plt.title('New function')
            plt.show()
        return (c, d)
    def _sum_of_squares(self, c: float, d: float):
        s = 0.0
        for i in range(0, self.n):
            x = self.x[i]
            t = self.y[i]
            y = self.c * x + self.d
            s += (y - t) * (y - t)
        return s
    def _passive_search(self, d_min: float, d_max: float, c: float):
        step = (self.b - self.a) / self.n
        eps = 0.1
        res = 0.0
        while ((d_max - d_min) / self.n > eps):
            d = []
            tmp = d_min
            while tmp < d_max:
                d.append(tmp)
                tmp += step
            squares = [self._sum_of_squares(c, d_) for d_ in d]
            res = d[squares.index(min(squares))]
        return res
    def _dichotomy(self, c_min: float, c_max: float):
        eps = 0.1
        delta = 0.01
        while ((c_max - c_min) > eps):
            c1, c2 = 0.5 * (c_min + c_max) - delta, 0.5 * (c_min + c_max) + delta
            d1 = self._passive_search(self.d_min, self.d_max, c1)
            d2 = self._passive_search(self.d_min, self.d_max, c2)
            if self._sum_of_squares(c2, d2) > self._sum_of_squares(c1, d1):
                c_max = c2
            else:
                c_min = c1
        return (c_min + c_max) / 2

if __name__ == "__main__":
    approx = Approximator(n = 20, interval = (-2, 1), params = (0.5, 0))
    res = approx.search(amp = 1)
    print("c = {}, d = {}".format(res[0], res[1]))
