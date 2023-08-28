#!/usr/bin/python3

def safe_print_integer(value):
    """ A function that prints integer with "{:d}".format().

    Args:
        value (int): is the integer to be printed.

    Returns:
        If a TypeError of ValueError occurs - False.
        Else - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
