#!/usr/bin/python3

import sys

def safe_function(fct, *args):
    """ A function that execute a function safely.

    Args:
        fct: The function to be executed.
        args: Arguments for fct.

    Returns:
        If an error is encountered - None.
        Else - the result of the call to fct.
    """
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
