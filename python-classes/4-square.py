#!/usr/bin/python3
"""
This module defines a Square class with getters and setters for size.
"""


class Square:
    """Class that defines a square with property-based size management."""
    def __init__(self, size=0):
        """Initializes the square through the size setter."""
        self.size = size

    @property
    def size(self):
        """Getter for the private size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the private size attribute with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
