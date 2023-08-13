#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """A function that finds all multiples of 2 in a list."""
    multiples_2 = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multiples_2.append(True)
        else:
            multiples_2.append(false)

        return (multiples_2)
