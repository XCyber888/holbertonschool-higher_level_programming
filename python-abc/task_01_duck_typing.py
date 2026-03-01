#!/usr/bin/python3
"""
Module defines Shape, Circle, and Rectangle for duck typing.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract Shape."""
    @abstractmethod
    def area(self):
        """Area."""
        pass
    @abstractmethod
    def perimeter(self):
        """Perimeter."""
        pass


class Circle(Shape):
    """Circle class."""
    def __init__(self, radius):
        """Init."""
        self.radius = radius
    def area(self):
        """Area."""
        return math.pi * (self.radius ** 2)
    def perimeter(self):
        """Perimeter."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class."""
    def __init__(self, width, height):
        """Init."""
        self.width = width
        self.height = height
    def area(self):
        """Area."""
        return self.width * self.height
    def perimeter(self):
        """Perimeter."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print info."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
