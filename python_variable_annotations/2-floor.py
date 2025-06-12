#!/usr/bin/env python3
"""
Module that provides mathematical floor operations with type annotations.

This module contains functions for performing mathematical operations
using Python 3 type annotations for better code clarity and type checking.
"""

import math


def floor(n: float) -> int:
    """
    Return the floor of a floating point number.

    Args:
        n (float): The floating point number to floor.

    Returns:
        int: The floor of n as an integer.
    """
    return math.floor(n)
