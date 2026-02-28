#!/usr/bin/python3
"""Module for shapes and duck typing."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Shape abstract class."""
    @abstractmethod
    def area(self):
        """Area method."""
        pass

    @abstractmethod
    def perimeter(self):
        """Perimeter method."""
        pass


class Circle(Shape):
    """Circle class."""
    def __init__(self, radius):
        """Initialize with radius."""
        self.radius = radius

    def area(self):
        """Calculate area."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate perimeter."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class."""
    def __init__(self, width, height):
        """Initialize with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate area."""
        return self.width * self.height

    def perimeter(self):
        """Calculate perimeter."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print shape info."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
