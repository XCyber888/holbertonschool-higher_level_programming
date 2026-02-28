#!/usr/bin/python3
"""Rectangle class with instance counter.

This module defines a Rectangle class with private width and height attributes,
getters/setters, area, perimeter, string representation, delete message,
and class attribute to count instances.
"""


class Rectangle:
    """Class that defines a rectangle with instance counter."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize rectangle with optional width and height.

        Args:
            width: width of the rectangle, defaults to 0
            height: height of the rectangle, defaults to 0
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Calculate and return the area of the rectangle.

        Returns:
            int: width * height
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle.

        Returns:
            int: 2 * (width + height), or 0 if width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return string representation with # characters.

        Returns:
            str: rectangle made of #, empty if width/height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ""
        for i in range(self.__height):
            rect += "#" * self.__width
            if i < self.__height - 1:
                rect += "\n"
        return rect

    def __repr__(self):
        """Return official string representation for eval.

        Returns:
            str: string that can be used with eval() to recreate object
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print message when instance is deleted and decrement counter."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
