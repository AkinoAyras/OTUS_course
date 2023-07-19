from hw2.src.figure import Figure


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        if side_a <= 0 or side_b <= 0:
            raise ValueError(f"Can't create rectangle")
        self.side_a = side_a
        self.side_b = side_b
        self.name = 'rectangle'

    def get_perimeter(self):
        return (self.side_a + self.side_b) * 2

    def get_area(self):
        return self.side_a * self.side_b
