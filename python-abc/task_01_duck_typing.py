#!/usr/bin/python3
"""
Shapes, Interfaces, and Duck Typing

This module demonstrates abstract base classes and duck typing in Python.
It defines an abstract Shape class with area and perimeter methods,
concrete Circle and Rectangle classes, and a shape_info function that
uses duck typing to print shape information.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for all geometric shapes."""

    @abstractmethod
    def area(self):
        """Calculate area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle class that inherits from Shape."""

    def __init__(self, radius):
        """Initialize circle with radius."""
        self.radius = radius

    def area(self):
        """Calculate area of circle (πr²)."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculate perimeter (circumference) of circle (2πr)."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class that inherits from Shape."""

    def __init__(self, width, height):
        """Initialize rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate area of rectangle (width × height)."""
        return self.width * self.height

    def perimeter(self):
        """Calculate perimeter of rectangle (2×(width+height))."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print area and perimeter of any shape using duck typing.

    Args:
        shape: any object that implements area() and perimeter() methods
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
