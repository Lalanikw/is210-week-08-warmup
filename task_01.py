#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""fibonacci sequence"""


def fibonacci(maxint):
    """making a fibonacci sequence with a while loop up to maxint.

    Args:
        maxint (int): upper bound of the loop
        a (int): default value = 0
        b (int): default value = 1
        seq (list): list of numbers

    returns:
        list: values for b

    examples:
        >>>fibonacci(10)
        >>>> [0, 1, 1, 2, 3, 5, 8]
    """
    retval = []
    a = 0
    b = 1
    retval.append(a)
    while b < maxint:
        retval.append(b)
        a, b = b, a+b
    return retval
