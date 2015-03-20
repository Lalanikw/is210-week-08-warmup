#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""excercise if statement"""


def bool_to_str(bval):
    """making a fibonacci sequence with a while loop up to maxint.

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
    if bval is True:
        return "Yes"
    else:
        return "No"
