#!/usr/bin/python3
<<<<<<< HEAD
"""Shapes, Interfaces, and Duck Typing.

This module demonstrates abstract base classes and duck typing in Python.
It defines an abstract Shape class with area and perimeter methods,
concrete Circle and Rectangle classes, and a shape_info function that
uses duck typing to print shape information.
"""

=======
"""
Module for Shape, Circle, Rectangle and duck typing.
"""
>>>>>>> 726c8ab9bbeb8ae8d2ab1b2955d12e2720371547
from abc import ABC, abstractmethod
import math


class Shape(ABC):
<<<<<<< HEAD
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape."""
=======
    """Abstract class for all shapes."""

    @abstractmethod
    def area(self):
        """Calculate area."""
>>>>>>> 726c8ab9bbeb8ae8d2ab1b2955d12e2720371547
        pass

    @abstractmethod
    def perimeter(self):
<<<<<<< HEAD
        """Calculate and return the perimeter of the shape."""
=======
        """Calculate perimeter."""
>>>>>>> 726c8ab9bbeb8ae8d2ab1b2955d12e2720371547
        pass


class Circle(Shape):
    """Circle class that inherits from Shape."""

    def __init__(self, radius):
<<<<<<< HEAD
        """Initialize circle with radius."""
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate and return the perimeter (circumference) of the circle."""
=======
        """Initialize Circle with radius."""
        self.radius = radius

    def area(self):
        """Return area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return perimeter of the circle."""
>>>>>>> 726c8ab9bbeb8ae8d2ab1b2955d12e2720371547
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class that inherits from Shape."""

    def __init__(self, width, height):
<<<<<<< HEAD
        """Initialize rectangle with width and height."""
=======
        """Initialize Rectangle with width and height."""
>>>>>>> 726c8ab9bbeb8ae8d2ab1b2955d12e2720371547
        self.width = width
        self.height = height

    def area(self):
<<<<<<< HEAD
        """Calculate and return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
=======
        """Return area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return perimeter of the rectangle."""
>>>>>>> 726c8ab9bbeb8ae8d2ab1b2955d12e2720371547
        return 2 * (self.width + self.height)


def shape_info(shape):
<<<<<<< HEAD
    """Print the area and perimeter of a shape using duck typing.

    Args:
        shape: any object that implements area() and perimeter() methods
    """
=======
    """Print area and perimeter of a shape using duck typing."""
>>>>>>> 726c8ab9bbeb8ae8d2ab1b2955d12e2720371547
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
