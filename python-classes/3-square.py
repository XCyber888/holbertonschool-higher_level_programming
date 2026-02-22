#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Square with area calculation."""
    def __init__(self, size=0):
        """Initialize size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return square area."""
        return self.__size ** 2
