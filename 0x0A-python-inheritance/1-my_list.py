#!/usr/bin/python3
"""Defining an inherited list class MyList."""


class MyList(list):
    """Implements sorted printing for the buit-in list class."""

    def print_sorted(self):
        """Printing a list in sorted ascending order."""
        print(sorted(self))
