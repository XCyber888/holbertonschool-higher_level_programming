#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Square that prints itself."""
    def __init__(self, size=0):
        """Initialize."""
        self.size = size

    @property
    def size(self):
        """Get size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with #."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
