#!/usr/bin/python3
"""Module for VerboseList class."""


class VerboseList(list):
    """A list that prints notifications on modifications."""

    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        count = len(items)
        super().extend(items)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
