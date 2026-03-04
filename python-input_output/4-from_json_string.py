#!/usr/bin/python3
"""
Module that returns a Python object from a JSON string.
"""
import json


def from_json_string(my_str):
    """
    Returns an object represented by a JSON string.

    Args:
        my_str (str): The JSON string to be converted.
    Returns:
        object: Python data structure.
    """
    return json.loads(my_str)
