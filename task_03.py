#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""calculate Max Min and average length"""

import decimal


def lexicographics(to_analyze):
    """evaluates the Max, Min and average length of words.

    Args:
        to_analyze (str): statistics of the words

    returns:
        str: length of words

    examples:
        >>>>>> lexicographics('''Don't stop believing,
            Hold on to that feeling.''')
        >>>(17, 3, Decimal('10'))
    """
    line_list = to_analyze.split('\n')
    min_word = 0
    max_word = 0
    total_words = 0
    for line in line_list:
        word_list = line.split(' ')
        word_count = len(word_list)
        if word_count < min_word or min_word == 0:
            min_word = word_count
        if word_count > max_word:
            max_word = word_count
        total_words = total_words + word_count
    average = decimal.Decimal(total_words) / decimal.Decimal(len(line_list))
    return (max_word, min_word, average)
