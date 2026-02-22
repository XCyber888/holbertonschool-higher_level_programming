#!/usr/bin/python3
"""
This module defines a Square class with validation for size.
"""


class Square:
    """Class that defines a square and validates the size."""
    def __init__(self, size=0):
        """Initializes the square and checks if size is an integer >= 0."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
