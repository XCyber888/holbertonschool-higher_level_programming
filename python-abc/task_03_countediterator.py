#!/usr/bin/python3
"""Module for CountedIterator class."""


class CountedIterator:
    """An iterator that keeps track of the number of items iterated."""

    def __init__(self, iterable):
        """Initialize the iterator and counter."""
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        """Return the current count of iterated items."""
        return self.counter

    def __next__(self):
        """Fetch the next item and increment counter."""
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        """Return the iterator object itself."""
        return self
