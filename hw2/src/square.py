from hw2.src.figure import Figure


class Square(Figure):
    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError(f"Can't create square")
        self.side_a = side_a
        self.name = 'square'

    def get_perimeter(self):
        return self.side_a * 4

    def get_area(self):
        return self.side_a ** 2
