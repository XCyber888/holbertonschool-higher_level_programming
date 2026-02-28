#!/usr/bin/python3
"""Shapes, Interfaces, and Duck Typing.

This module demonstrates abstract base classes and duck typing.
It defines an abstract Shape class, concrete Circle and Rectangle classes,
and a shape_info function that uses duck typing.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle class inheriting from Shape."""

    def __init__(self, radius):
        """Initialize circle with radius."""
        self.radius = radius

    def area(self):
        """Calculate area of circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate perimeter (circumference) of circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class inheriting from Shape."""

    def __init__(self, width, height):
        """Initialize rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate area of rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate perimeter of rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter of any shape with area/perimeter methods."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
