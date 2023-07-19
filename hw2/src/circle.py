from hw2.src.figure import Figure
import math


class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError(f"Can't create circle")
        self.radius = radius
        self.name = 'circle'

    def get_perimeter(self):
        return int(2 * math.pi * self.radius)

    def get_area(self):
        return int((self.radius ** 2) * math.pi)
