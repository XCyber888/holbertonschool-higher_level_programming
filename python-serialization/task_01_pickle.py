#!/usr/bin/python3
"""
Module for serializing and deserializing custom objects using pickle.
"""
import pickle


class CustomObject:
    """A custom class with name, age, and student status."""

    def __init__(self, name, age, is_student):
        """Initializes the CustomObject."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the object attributes in a specific format."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serializes the current instance to a file."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserializes an instance from a file."""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.UnpicklingError, Exception):
            return None
