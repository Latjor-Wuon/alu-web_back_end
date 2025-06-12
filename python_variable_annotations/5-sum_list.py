#!/usr/bin/env python3
"""
Module that provides list operations with complex type annotations.

This module contains functions for performing operations on lists
using Python 3 type annotations including complex types from typing module.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floating point numbers.

    Args:
        input_list (List[float]): A list of floating point numbers to sum.

    Returns:
        float: The sum of all numbers in the input list.
    """
    return sum(input_list)
