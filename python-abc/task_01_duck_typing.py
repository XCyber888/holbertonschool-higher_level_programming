#!/usr/bin/python3
"""Task 01: Shapes, Interfaces, and Duck Typing.

This module demonstrates abstract base classes and duck typing.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate the area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter."""
        pass


class Circle(Shape):
    """Circle class."""

    def __init__(self, radius):
        """Initialize circle."""
        self.radius = radius

    def area(self):
        """Return circle area."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Return circle perimeter."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class."""

    def __init__(self, width, height):
        """Initialize rectangle."""
        self.width = width
        self.height = height

    def area(self):
        """Return rectangle area."""
        return self.width * self.height

    def perimeter(self):
        """Return rectangle perimeter."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter of any shape."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
