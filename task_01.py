#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""fibonacci sequence"""


def fibonacci(maxint):
    """making a fibonacci sequence with a while loop up to maxint.

    Args:
        maxint (int): upper bound of the loop
        a (int): values
        b (int): values
        result (list): list of numbers

    returns:
        list: values for b

    examples:
        >>>fibonacci(10)
        >>>> [0, 1, 1, 2, 3, 5, 8]
    """
    a, b = 0, 1
    seq = [a, a+b]
    while len(seq) < maxint-2:
        seq += [seq[len(seq)-1] + seq[len(seq)-2]]
    return seq
