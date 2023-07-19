from hw2.src.figure import Figure
import math


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        if side_a <= 0 or side_b <= 0 or side_c <= 0 or (side_a + side_b) < side_c or (side_b + side_c) < side_a \
                or (side_a + side_c) < side_b:
            raise ValueError(f"Can't create triangle")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.name = 'triangle'

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def get_area(self):
        semi_p = (self.side_a + self.side_b + self.side_c) / 2
        return int(math.sqrt(semi_p * (semi_p - self.side_a) * (semi_p - self.side_b) * (semi_p - self.side_c)))
