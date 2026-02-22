#!/usr/bin/python3
"""
This module defines a Square class with a private size attribute.

The size of a square is a fundamental property, and making it private
ensures that it can only be modified with proper validation in the future.
"""


class Square:
    """
    A class that represents a square.

    Attributes:
        __size (int): The size of the square's side (private).
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the side of the square.
        """
        self.__size = size
