#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """A function that Executes a function safely.

    Args:
        fct: The function to be executed.
        args: Arguments for fct.

    Returns:
        If an error occurs - None.
        Else - the result of the call to fct.
    """
    try:
        result = fct(*args)
        return (result)
    if not:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
