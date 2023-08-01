import pytest
from hw2.src.rectangle import *
from hw2.src.circle import *
from hw2.src.triangle import *
from hw2.src.square import *

def test_circle():
    c = Circle(5)
    assert c.name == 'circle'
    assert c.get_area() == 78
    assert c.get_perimeter() == 31

@pytest.mark.parametrize('radius, perimetr, area',[
                            (-1, -6, 3),
                            (0, 0, 0)
                            ])
def test_circle_negative(radius, perimetr, area):
    with pytest.raises(ValueError):
        Circle(radius)


def test_add_area_circle():
    c1 = Circle(5)
    c2 = Circle(8)
    assert c1.add_area(c2) == 279

def test_add_area_triangle():
    c1 = Circle(4)
    t1 = Triangle(5, 6, 3)
    assert c1.add_area(t1) == 57

def test_add_area_square():
    c1 = Circle(4)
    s1 = Square(5)
    assert c1.add_area(s1) == 75

def test_add_area_rectangle():
    c1 = Circle(1)
    r1 = Rectangle(7, 8)
    assert c1.add_area(r1) == 59


