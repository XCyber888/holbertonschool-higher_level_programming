#!/usr/bin/python3
"""Rectangle class with square method.

This module defines a Rectangle class with private width and height attributes,
getters/setters, area, perimeter, string representation, delete message,
instance counter, print_symbol, compare method, and class method square.
"""


class Rectangle:
    """Class that defines a rectangle with square method."""

    number_of_instances = 0
    print_symbol = "#"

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
        if not isinstance(value, int):
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
        if not isinstance(value, int):
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
        """Return string representation with print_symbol.

        Returns:
            str: rectangle made of print_symbol, empty if width/height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = []
        for i in range(self.__height):
            rect.append(str(self.print_symbol) * self.__width)
        return "\n".join(rect)

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest rectangle based on area.

        Args:
            rect_1: first rectangle, must be Rectangle instance
            rect_2: second rectangle, must be Rectangle instance

        Returns:
            Rectangle: rect_1 if area >= rect_2.area, else rect_2

        Raises:
            TypeError: if rect_1 or rect_2 is not a Rectangle instance
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Create a square rectangle with width = height = size.

        Args:
            size: size of the square, defaults to 0

        Returns:
            Rectangle: new Rectangle instance with width = height = size
        """
        return cls(size, size)
