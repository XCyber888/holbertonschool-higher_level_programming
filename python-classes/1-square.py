#!/usr/bin/python3
"""
This module defines a Square class with a private instance attribute.

The size of the square is a crucial property, and by making it private,
we ensure that the internal state of the object is protected.
"""


class Square:
    """
    A class that represents a square.

    Attributes:
        __size (int): The width and height of the square.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the side of the square.
        """
        self.__size = size
