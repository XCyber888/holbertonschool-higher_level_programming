#!/usr/bin/python3
"""
This module defines an abstract Shape class and its subclasses.
It also demonstrates the concept of duck typing in Python.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for all geometric shapes."""

    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle class that inherits from Shape."""

    def __init__(self, radius):
        """Initialize Circle with a radius."""
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return the perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class that inherits from Shape."""

    def __init__(self, width, height):
        """Initialize Rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter of a shape using duck typing."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
