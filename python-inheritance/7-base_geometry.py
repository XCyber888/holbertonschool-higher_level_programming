#!/usr/bin/python3
"""BaseGeometry class.

This module defines a BaseGeometry class with area method and integer_validator.
"""


class BaseGeometry:
    """Base geometry class with area method and integer validator."""

    def area(self):
        """Raise exception that area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer.

        Args:
            name: string name of the value
            value: value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
