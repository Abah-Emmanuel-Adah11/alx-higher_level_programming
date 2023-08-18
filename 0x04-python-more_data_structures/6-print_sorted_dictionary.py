#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    list_ordered = list(a_dictionary.keys())
    list_ordered.sort()
    for i in list_ordered:
        print("{}: {}".format(i, a_dictionary.get(i)))
