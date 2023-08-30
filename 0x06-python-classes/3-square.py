#!/usr/bin/python3
"""Defining a class Square."""


class Sqaure:
    """Representing a sqaure."""

    def __init__(self, size=0):
        """Initializing a new square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self._size = size

    def area(self):
        """Returning the current area of the square."""
        return (self.__size * self.__size)
