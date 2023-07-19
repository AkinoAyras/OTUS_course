import pytest
from hw2.src.rectangle import *
from hw2.src.circle import *
from hw2.src.triangle import *
from hw2.src.square import *


def test_square():
    s = Square(1)
    assert s.name == 'square'
    assert s.get_area() == 1
    assert s.get_perimeter() == 4

@pytest.mark.parametrize('side_a, perimetr, area',[
                            (-1, 1, 1),
                            (0, 0, 0),
                        ])
def test_square_negative(side_a, perimetr, area):
    with pytest.raises(ValueError):
        Square(side_a)


def test_add_area_circle():
    s1 = Square(5)
    c1 = Circle(5)
    assert s1.add_area(c1) == 103

def test_add_area_triangle():
    s1 = Square(4)
    t1 = Triangle(5, 6, 3)
    assert s1.add_area(t1) == 23

def test_add_area_square():
    s1 = Square(4)
    s2 = Square(5)
    assert s1.add_area(s2) == 41

def test_add_area_rectangle():
    s1 = Square(1)
    r1 = Rectangle(7, 8)
    assert s1.add_area(r1) == 57
