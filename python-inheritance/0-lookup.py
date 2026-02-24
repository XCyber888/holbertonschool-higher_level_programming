#!/usr/bin/python3
"""Lookup function module.

This module provides a function that returns the list of available
attributes and methods of an object.
"""


def lookup(obj):
    """Return the list of available attributes and methods of an object.

    Args:
        obj: object to inspect

    Returns:
        list: list of attributes and methods
    """
    return dir(obj)
