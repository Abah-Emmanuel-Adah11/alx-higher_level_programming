#!/usr/bin/python3

def safe_print_list_integers(my_list={}, x=0):
    """A function that print the first x elements of a list that are integers.

    Args:
        my_list (list): The list from whence to print elements
        x (int): The number of elements to be printed from my_list

    Returns;
        The number of elements printed.
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
