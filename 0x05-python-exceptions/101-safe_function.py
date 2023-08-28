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
        res = fct(*args)
    except BaseException as e:
        res = None
        print("Exception: {}".format(e), file=sys.stderr)
    finally:
        return res
