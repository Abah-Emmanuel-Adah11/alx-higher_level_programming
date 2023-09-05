#!/usr/bin/python3
"""Defining a locked class."""


class LockedClass:
    """
    Prevent's the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
