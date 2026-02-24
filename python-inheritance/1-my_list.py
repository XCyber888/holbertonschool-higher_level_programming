#!/usr/bin/python3
"""MyList class that inherits from list.

This module defines a MyList class that inherits from the built-in list class
and provides an additional method to print the list in sorted order.
"""


class MyList(list):
    """A custom list class that inherits from list.

    This class extends the built-in list functionality by adding a method
    to print the list elements in ascending sorted order.
    """

    def print_sorted(self):
        """Print the list in ascending sorted order.

        This method assumes all elements in the list are integers.
        It does not modify the original list.
        """
        print(sorted(self))
