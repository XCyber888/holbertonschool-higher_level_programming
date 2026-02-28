#!/usr/bin/python3
"""Rectangle class with width and height.

This module defines a Rectangle class with private width and height attributes,
including getters and setters with validation.
"""


class Rectangle:
    """Class that defines a rectangle with width and height."""

    def __init__(self, width=0, height=0):
        """Initialize rectangle with optional width and height.

        Args:
            width: width of the rectangle, defaults to 0
            height: height of the rectangle, defaults to 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width attribute with validation.

        Args:
            value: new width value

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height attribute with validation.

        Args:
            value: new height value

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
