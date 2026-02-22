#!/usr/bin/python3
"""
This module defines a Square class that can print itself using #.
"""


class Square:
    """Class that defines a square and a method to print it."""
    def __init__(self, size=0):
        """Initializes the square."""
        self.size = size

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character # to stdout."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
