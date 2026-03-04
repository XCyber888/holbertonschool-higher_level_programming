#!/usr/bin/python3
"""
Module that creates an Object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a JSON file.

    Args:
        filename (str): The name of the file.
    Returns:
        object: Python data structure.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
