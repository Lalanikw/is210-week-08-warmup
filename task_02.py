#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""excercise if statement"""


def bool_to_str(bval):
    """making a boolean function with if and else.

    Args:
        bval (boolean): evaluates the truthiness or falsiness

    returns:
        boolean: truthiness or falsiness

    examples:
        >>>bool_to_str(' ')
        >>>'No'
        >>>bool_to_str(True)
        >>>'Yes'
    """
    retval = 'No'
    if bval:
        retval = 'Yes'
    return retval
