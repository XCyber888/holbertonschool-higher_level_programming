#!/usr/bin/python3
"""Module for Shape, Circle, Rectangle and duck typing."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter."""
        pass


class Circle(Shape):
    """Circle class."""

    def __init__(self, radius):
        """Constructor."""
        self.radius = radius

    def area(self):
        """Area of circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Perimeter of circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class."""

    def __init__(self, width, height):
        """Constructor."""
        self.width = width
        self.height = height

    def area(self):
        """Area of rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Perimeter of rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Duck typing function to print shape info."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
