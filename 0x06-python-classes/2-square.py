#!/usr/bin/python3
"""defining a class Square."""

class Square:
"""Representing a squre."""

def __init__(self, size=0):
    """Initialing a new Square.

    Args:
        size (int): The size of the new square.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("Size must be >= 0")
    self.__size = size
