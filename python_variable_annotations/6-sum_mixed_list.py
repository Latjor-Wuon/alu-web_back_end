#!/usr/bin/env python3
"""
Module that provides mixed list operations with complex type annotations.

This module contains functions for performing operations on mixed lists
using Python 3 type annotations including Union types from typing module.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a mixed list of integers and floating point numbers.

    Args:
        mxd_lst (List[Union[int, float]]): A list containing integers and/or
                                          floating point numbers to sum.

    Returns:
        float: The sum of all numbers in the mixed list as a float.
    """
    return sum(mxd_lst)
