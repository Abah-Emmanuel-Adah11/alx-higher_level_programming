#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """ A function that Prints x elememts of a list.

    Args:
        my_list (list): The list form which to print elements.
        x (int): The number of elements to be printed from my_list.

    Returns:
        The number of elements printed.
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
