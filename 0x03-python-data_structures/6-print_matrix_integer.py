#!/usr/bin/python3

"""A fuction that prints a matrix of integer"""
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        print(' '.join('{:d}'.format(j)for j in i))
