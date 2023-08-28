#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """A function that prints an integer with "{:d}".format().

    When a VeiwError message is encountered, a corresponding message
    is printed to standard error.

    Args:
        value (int): The integer to be printed.

    Returns:
        If a TypeError is encountered - False.
        Else: - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
