from cmath import sqrt


class Quadratic:
    """Solve quadratic equation."""

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def solve(self):
        delta = self.b**2 - 4 * self.a * self.c
        r1 = (-self.b + sqrt(delta)) / (2 * self.a)
        r2 = (-self.b - sqrt(delta)) / (2 * self.a)
        return r1, r2
