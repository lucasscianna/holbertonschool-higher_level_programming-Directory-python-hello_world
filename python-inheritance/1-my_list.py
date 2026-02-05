#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """Implements a list with print_sorted method."""

    def print_sorted(self):
        """Print the list in ascending order without modifying it."""
        print(sorted(list(self)))
