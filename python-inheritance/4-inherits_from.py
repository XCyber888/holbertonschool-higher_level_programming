#!/usr/bin/python3
"""
This module defines a function that checks if an object is an instance
of a class that inherited from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an inherited instance of a class.

    Args:
        obj: The object to check.
        a_class: The class to match against.

    Returns:
        True if obj is an instance of a subclass of a_class;
        otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
