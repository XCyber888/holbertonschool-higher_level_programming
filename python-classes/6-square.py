#!/usr/bin/python3
"""
This module defines a Square class with size and position.
"""


class Square:
    """Class that defines a square with size, position and printing."""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes square with size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position with specific tuple validation."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with # and uses position for spaces."""
        if self.__size == 0:
            print()
            return
        [print("") for i in range(self.__position[1])]
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
