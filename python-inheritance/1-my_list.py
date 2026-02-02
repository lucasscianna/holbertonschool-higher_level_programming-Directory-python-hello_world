#!/usr/bin/python3
"""Module that defines a custom list class"""

class MyList(list):
    """Class that inherits from list and adds a method to print a sorted version."""

    def print_sorted(self):
        """Prints the list sorted in ascending order without modifying the original list."""
        print(sorted(self))
