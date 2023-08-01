import pytest
from hw2.src.rectangle import *
from hw2.src.circle import *
from hw2.src.triangle import *
from hw2.src.square import *


def test_rectangle():
    r = Rectangle(1, 2)
    assert r.name == 'rectangle'
    assert r.get_area() == 2
    assert r.get_perimeter() == 6


@pytest.mark.parametrize('side_a, side_b, perimetr, area', [
    (-1, 2, 2, -2),
    (0, 10, 20, 0),
    (1, -2, 2, -2)
])
def test_rectangle_negative(side_a, side_b, perimetr, area):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)


def test_add_area_circle():
    r1 = Rectangle(5, 6)
    c1 = Circle(5)
    assert r1.add_area(c1) == 108

def test_add_area_triangle():
    r1 = Rectangle(5, 6)
    t1 = Triangle(5, 6, 3)
    assert r1.add_area(t1) == 37

def test_add_area_square():
    r1 = Rectangle(5, 6)
    s1 = Square(5)
    assert r1.add_area(s1) == 55

def test_add_area_rectangle():
    r1 = Rectangle(5, 6)
    r2 = Rectangle(7, 8)
    assert r1.add_area(r2) == 86

