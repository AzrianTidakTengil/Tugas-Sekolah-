import math


class Circle:
    def __init__(self, r):
        self.r = r

    def Area(self):
        return math.pi * self.r * self.r
