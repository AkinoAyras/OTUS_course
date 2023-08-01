import pytest
from hw2.src.rectangle import *
from hw2.src.circle import *
from hw2.src.triangle import *
from hw2.src.square import *

def test_triangle():
    t = Triangle(4, 2, 3)
    assert t.name == 'triangle'
    assert t.get_area() == 2
    assert t.get_perimeter() == 9


@pytest.mark.parametrize('side_a, side_b, side_c', [
                            (-1, 2, 5),
                            (0, 10, -3),
                            (0, 0, 0),
                            (1, -2, 6),
                            (6, 4, -5)
                        ])
def test_rectangle_negative(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)

def test_add_area_circle():
    t1 = Triangle(5, 6, 8)
    c1 = Circle(5)
    assert t1.add_area(c1) == 92

def test_add_area_triangle():
    t1 = Triangle(4, 4, 6)
    t2 = Triangle(5, 6, 3)
    assert t1.add_area(t2) == 14

def test_add_area_square():
    t1 = Triangle(5, 6, 7)
    s1 = Square(5)
    assert t1.add_area(s1) == 39

def test_add_area_rectangle():
    t1 = Triangle(5, 6, 9)
    r1 = Rectangle(7, 8)
    assert t1.add_area(r1) == 70

